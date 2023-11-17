from flask import Flask, Blueprint, request, redirect, render_template, url_for, current_app, send_from_directory
import os
import csv
from CTFd.plugins import bypass_csrf_protection
from CTFd.utils.user import get_current_user, is_admin
from CTFd.utils.decorators import authed_only, admins_only

import logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)
tutorial = Blueprint('pwncollege_tutorial', __name__)
app = current_app

ALLOWED_EXTENSIONS = {'pdf'}
template_dir = os.path.abspath('../../dojo_theme/static/files')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@tutorial.route('/tutorial/view/pdf/<filename>', methods=['GET'])
def view_pdf_tutorial(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@tutorial.route('/tutorial', methods=['GET', 'POST'])
def view_tutorial():
    files = []
    if os.path.exists('pdf_descriptions.csv'):
        with open('pdf_descriptions.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                filename, description = row
                file_url = url_for('pwncollege_tutorial.view_pdf_tutorial', filename=filename)
                files.append({'name': filename, 'url': file_url, 'description': description})

    links = []
    if os.path.exists('links.txt'):
        with open('links.txt', 'r') as file:
            for i, line in enumerate(file):
                link, description = line.strip().split('|')
                links.append({'name': link, 'link': link, 'description': description, 'identifier': i})

    return render_template('tutorial.html', files=files, links=links)

@tutorial.route('/tutorials/upload-pdf', methods=['POST'])
@authed_only
@bypass_csrf_protection
def upload_pdf():
    if 'file' in request.files:
        file = request.files['file']
        description = request.form.get('description', '')
        if file.filename != '' and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            isExist  = os.path.exists(app.config['UPLOAD_FOLDER'])
            if not isExist:
                os.makedirs(app.config["UPLOAD_FOLDER"])
            file.save(filepath)
            with open('pdf_descriptions.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([filename, description])
    return redirect(url_for('pwncollege_tutorial.view_tutorial'))

@tutorial.route('/tutorials/submit-link', methods=['POST'])
@authed_only
@bypass_csrf_protection
def submit_link():
    link = request.form.get('link')
    description = request.form.get('description', '')
    if link:
        with open('links.txt', 'a') as file:
            file.write(link + '|' + description + '\n')
    return redirect(url_for('pwncollege_tutorial.view_tutorial'))

@tutorial.route('/tutorials/delete/pdf/<filename>', methods=['GET'])
@authed_only
@bypass_csrf_protection
def delete_pdf(filename):
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            os.remove(filepath)

        if os.path.exists('pdf_descriptions.csv'):
            with open('pdf_descriptions.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = [row for row in reader]

            with open('pdf_descriptions.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in rows:
                    if row[0] != filename:
                        writer.writerow(row)

        return redirect(url_for('pwncollege_tutorial.view_tutorial'))
    except Exception as e:
        logging.error(f"Error in delete_pdf: {str(e)}")
        return str(e), 500

@tutorial.route('/tutorials/delete/link/<int:index>', methods=['GET'])
@authed_only
@bypass_csrf_protection
def delete_link(index):
    try:
        if os.path.exists('links.txt'):
            with open('links.txt', 'r') as file:
                lines = file.readlines()

            if 0 <= index < len(lines):
                del lines[index]

            with open('links.txt', 'w') as file:
                file.writelines(lines)
        return redirect(url_for('upload_file'))
    except Exception as e:
        print(str(e))
        logging.error(f"Error in delete_pdf: {str(e)}")
        return str(e), 500
