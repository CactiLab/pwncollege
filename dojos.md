# How to update PwnIoT

## How to update an existing dojo (challenges)
1. Push changes to the dojo repository (https://github.com/CactiLab/software-security-course-binaries)
	* Note: To change challenge or dojo metadata, see [`dojo.yml`](https://github.com/CactiLab/software-security-course-binaries/blob/master/dojo.yml). See [pwn.college documentation](https://github.com/pwncollege/example-dojo#dojo) for more.
2. Log in to admin user account and navigate to the dojo you updated (CSE418)
3. Click **Admin**.
4. Click **Update**. This makes a POST request to an API endpoint that should respond with the following object on success (or an error message on failure)

```json
{
  "success": true
}
```


## `dojo` command
The `dojo` command on the top-level PwnIoT container contains a few subcommands that are really useful for developing and updating the platform. 

You can run it like this from the PwnIoT VM:
```bash
docker exec pwniot.academy dojo help
```

or if you've already entered the `pwniot.academy` container, just run `dojo help` from `/opt/academy`.

`dojo` has a few important capabilities to be aware of:

### `dojo start`
Starts up all the subcontainers. This is the entry point for the whole system and gets called in the `docker run` command.

### `dojo update`
This runs `git pull` to synchronize with the remote branch (if needed) and then rebuilds all containers. Note that sometimes, you'll need to restart CTFd directly with the `dojo restart` command.

### `dojo db`
This opens a mysql client session so that you can view and modify the database. Some things (like editing dojo metadata) are only possible through direct database queries (see https://github.com/pwncollege/dojo/issues/167#issuecomment-1530012014 for info).

### `dojo enter <USER_ID>`
To enter the shell of an active user's session. Note that they must be actively logged in and working on a challenge in order for this to work.

### `dojo history <USER_ID>`
I implemented this—creates a snapshot of their `.bash_history` file and saves it to the `data/homes/history` directory. Note that there isn't currently error catching for when the log file doesn't exist but in most cases this shouldn't be an issue.

You can also access this feature via the admin panel.