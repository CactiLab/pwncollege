# pwn.college

Deploy a pwn.college instance!

## Details

The pwn.college infrastructure is based on [CTFd](https://github.com/CTFd/CTFd).
CTFd provides for a concept of users, challenges, and users solving those challenges by submitting flags.
From there, this repository provides infrastructure which expands upon these capabilities.

The pwn.college infrastructure allows users the ability to "start" challenges, which spins up a private docker container for that user.
This docker container will have the associated challenge binary injected into the container as root-suid, as well as the flag to be submitted as readable only by the the root user.
Users may enter this container via `ssh`, by supplying a public ssh key in their profile settings, or via vscode in the browser ([code-server](https://github.com/cdr/code-server)).
The associated challenge binary may be either global, which means all users will get the same binary, or instanced, which means that different users will receive different variants of the same challenge.

## Setup

Clone the repository:

```sh
git clone https://github.com/CactiLab/pwniot/ /opt/academy
```

The only dependency to run the infrastructure is docker, which can be installed with:

```sh
curl -fsSL https://get.docker.com | /bin/sh
```

Now, build the container:

```sh
cd /opt/academy
docker build -t pwniot.academy .
```

Finally, run the infrastructure which will be hosted on domain `my.domain.college` with:

```sh
docker run --privileged -d -v /opt/academy:/opt/pwn.college -p 22:22 -p 80:80 -p 443:443 --name pwniot.academy pwniot.academy
```

> **Warning**
> **(MacOS)**
> 
> It's important to note that while the dojo is capable of operating on MacOS (either x86 or ARM), MacOS has inherent limitations when it comes to nested Linux mounts within a MacOS bind mount. 
> This limitation specifically affects `data/docker`, which necessitates the use of OverlayFS mounts, preventing nested docker orchestration from functioning properly.
> In order to circumvent this issue, you must ensure that`data/docker` is not backed by a MacOS bind mount. 
> This can be accomplished by replacing the bind mount with a docker volume for `data/docker`, which will use a native Linux mount. 
> You can apply this solution using the following Docker command (notice the additional `-v`):
> ```
> docker run --privileged -d -v /opt/academy:/opt/pwn.college -v dojo-data-docker:/opt/pwn.college/data/docker -p 22:22 -p 80:80 -p 443:443 --name pwniot.academy pwniot.academy
> ```

This will run the initial setup, including building the challenge docker image.
If you want to build the full 70+ GB challenge image, you can add `-e DOJO_CHALLENGE=challenge` to the docker args.
Note, however, that docker environment variables only affect the initial setup, after which `./data/config.env` should be modified instead.
Refer to `script/container-setup.sh` for more information.

The dojo will initialize itself to listen on and serve from `localhost.pwn.college` (which resolves 127.0.0.1).
This is fine for development, but to serve your dojo to the world, you will need to update this to your actual hostname in `/opt/dojo/data/config.env`.

It will take some time to initialize everything and build the challenge docker image.
You can check on your container (and the progress of the initial build) with:

```sh
docker exec YOUR_CONTAINER_NAME dojo logs
```

Once things are setup, you should be able to access the dojo and login with username `admin` and password `admin`.
You can change these admin credentials in the admin panel.

## Customization

_All_ dojo data will be stored in the `./data` directory.

Once logged in, you can add a dojo by visiting `/dojos/create`. Dojos are contained within git repositories. 
Refer to [the example dojo](https://github.com/pwncollege/example-dojo) for more information.
