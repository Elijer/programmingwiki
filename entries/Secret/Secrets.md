# Django + MYSQL Deploy

### Cheatsheet

 | Purpose                              | Command                                         | Notes                                                                                                             |
 | ------------------------------------ | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
 | Login to droplet console             | `ssh jah@157.230.2.209`                         |                                                                                                                   |
 | Activate virtual environment         | `source environments/env1/bin/activate`         | where 'environments' is the folder I store my virtual envs, like 'env1' |
 | Reboot                               | `sudo reboot`                                   |                                                                                                                   |
 | Exit MYSQL server                    | `exit`                                          |                                                                                                                   |
 | Login to MYSQL server as 'root'      | `sudo mysql -u root`                            |                                                                                                                   |
 | Login to MYSQL Server as 'wikiuser3' | `sudo mysql -u wikiuser3`                       |                                                                                                                   |
 | Run server                           | `python manage.py runserver 157.230.2.209:8000` |                                                                                                                   |
 | URL                                  | [This one](http://157.230.2.209:8000/)          |                                                                                                                   |
 |          MYSQL superuser password                           |                voodoo                                 |                                                                                                                   |
 
 ### Cheatsheet 2
 1. ssh into server with superuser: `ssh jah@157.230.2.209`
 2. Check git: `git status`
 3. Activate virtual python environment: `source environments/env1/bin/activate` 
 4. Run app at specific port: `python manage.py runserver 157.230.2.209:8000`
 5. [Go to live server](http://157.230.2.209:8000/pages/Git): which is at this url `157.230.2.209:8000`
 
 