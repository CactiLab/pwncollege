FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV LC_CTYPE=C.UTF-8

RUN apt-get update && \
    apt-get install -y \
        apt-utils \
        build-essential \
        git \
        curl \
        wget \
        jq \
        iproute2 \
        iputils-ping \
        host \
        htop \
        python-is-python3 \
        python3-dev \
        python3-pip \
        openssh-server \
        qemu-user \
        qemu-system-arm \
        gcc-arm-none-eabi

RUN curl -fsSL https://get.docker.com | /bin/sh
RUN echo '{ "data-root": "/opt/pwn.college/data/docker" }' > /etc/docker/daemon.json

RUN pip install \
    docker \
    pytest

# TODO: this can be removed with docker-v22 (buildx will be default)
RUN docker buildx install

RUN git clone --branch 3.4.0 https://github.com/CTFd/CTFd /opt/CTFd

COPY etc/skel/.bashrc /etc/skel/.bashrc

RUN useradd -m hacker
RUN usermod -aG docker hacker
RUN mkdir -p /home/hacker/.docker
RUN echo '{ "detachKeys": "ctrl-q,ctrl-q" }' > /home/hacker/.docker/config.json
RUN wget -O /etc/docker/seccomp.json https://raw.githubusercontent.com/moby/moby/master/profiles/seccomp/default.json

RUN mkdir -p /opt/pwn.college
ADD . /opt/pwn.college

RUN ln -sf /opt/pwn.college/etc/ssh/sshd_config /etc/ssh/sshd_config
RUN ln -s /opt/pwn.college/etc/systemd/system/pwn.college.service /etc/systemd/system/pwn.college.service
RUN ln -s /opt/pwn.college/etc/systemd/system/pwn.college.logging.service /etc/systemd/system/pwn.college.logging.service
RUN ln -s /opt/pwn.college/etc/systemd/system/pwn.college.backup.service /etc/systemd/system/pwn.college.backup.service
RUN ln -s /opt/pwn.college/etc/systemd/system/pwn.college.backup.timer /etc/systemd/system/pwn.college.backup.timer
RUN ln -s /etc/systemd/system/pwn.college.service /etc/systemd/system/multi-user.target.wants/pwn.college.service
RUN ln -s /etc/systemd/system/pwn.college.logging.service /etc/systemd/system/multi-user.target.wants/pwn.college.logging.service
RUN ln -s /etc/systemd/system/pwn.college.backup.timer /etc/systemd/system/timers.target.wants/pwn.college.backup.timer

ADD ctfd/Dockerfile /opt/CTFd/Dockerfile
ADD dojo_plugin/requirements.txt /opt/CTFd/dojo-requirements.txt

RUN find /opt/pwn.college/script -type f -exec ln -s {} /usr/bin/ \;

EXPOSE 22
EXPOSE 80
EXPOSE 443

WORKDIR /opt/pwn.college
CMD ["dojo", "start"]
