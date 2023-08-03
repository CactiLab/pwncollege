import os
import pathlib

from flask import request, Blueprint, render_template, abort
from CTFd.utils.user import get_current_user, is_admin
from CTFd.utils.decorators import authed_only, admins_only
from CTFd.models import Users

from ..utils import random_home_path, get_active_users, redirect_user_socket
from ..utils.dojo import dojo_route, get_current_dojo_challenge


desktop = Blueprint("pwncollege_desktop", __name__)


def can_connect_to(desktop_user):
    return any((
        is_admin(),
        desktop_user.id == get_current_user().id,
        os.path.exists(f"/var/homes/nosuid/{random_home_path(desktop_user)}/LIVE")
    ))


def can_control(desktop_user):
    return any((
        is_admin(),
        desktop_user.id == get_current_user().id
    ))

def get_users_with_history():
    return os.listdir("/var/homes/data")

@desktop.route("/admin/history/<int:user_id>", methods=["GET"])
@admins_only
def get_history(user_id):
    home = pathlib.Path(f"/var/data/homes/data/{user_id}")
    if home.exists():
        os.system(f"/var/script/dojo history 2 api")
        lines = []
        with open(f"/var/data/homes/history/{user_id}/{os.listdir(f'/var/data/homes/history/{user_id}')[-1]}") as hist:
            lines = hist.readlines()
        return render_template("admin_viewhistory.html", lines=lines, username=Users.query.filter_by(id=user_id).first().name)


@desktop.route("/desktop")
@desktop.route("/desktop/<int:user_id>")
@authed_only
def view_desktop(user_id=None):
    current_user = get_current_user()
    if user_id is None:
        user_id = current_user.id

    user = Users.query.filter_by(id=user_id).first()
    if not can_connect_to(user):
        abort(403)

    try:
        password_type = "interact" if can_control(user) else "view"
        password_path = f"/var/homes/nosuid/{random_home_path(user)}/.vnc/pass-{password_type}"
        password = open(password_path).read()
    except FileNotFoundError:
        password = None

    active = bool(password) if get_current_dojo_challenge(user) is not None else None
    view_only = int(user_id != current_user.id)

    return render_template("desktop.html",
                           active=active,
                           password=password,
                           user_id=user_id,
                           view_only=view_only)


@desktop.route("/desktop/<int:user_id>/")
@desktop.route("/desktop/<int:user_id>/<path:path>")
@authed_only
def forward_desktop(user_id, path=""):
    prefix = f"/desktop/{user_id}/"
    assert request.full_path.startswith(prefix)
    path = request.full_path[len(prefix):]

    user = Users.query.filter_by(id=user_id).first()
    if not can_connect_to(user):
        abort(403)

    return redirect_user_socket(user, ".vnc/novnc.socket", f"/{path}")


@desktop.route("/admin/desktops", methods=["GET"])
@admins_only
def view_all_desktops():
    # active_desktops=True here would filter out only desktops that have been connected to, but that is too slow in
    # the current implementation...
    return render_template("admin_desktops.html", users=get_active_users())

@desktop.route("/admin/history", methods=["GET"])
@admins_only
def view_all_users():
    valid_users = Users.query.filter(Users.id.in_(get_users_with_history())).all()
    return render_template("admin_history.html", users=valid_users)
