# Project Exchnage Rate

## Commands

* `make setup`  : build and start containers
* `make build`  : build containers
* `make up.d`   : start containers in detached mode
* `make up`     : start containers in attached mode
* `make down`   : stop containers and remove networks
* `make restart`: firsts stop containers then start again
* `make logs`   : attach to log console of containers

### Common Commands

* `make dcshell`      : open django container shell
* `make dshell`       : open django shell
* `make ipshell`      : open django ipython shell
* `make dcattach`     : attach to django container
* `make migrate`      : run `makemigrations and migrate` command in django container
* `make collectstatic`: run `collectstatic` command in django container
* `make test`         : run `test` command in django container
* `make psql`         : run `psql` in postgres container
* `make rediscli`     : run `redis cli` in redis container

### Command to Get API Key

Firstly sh into django container with command:

* `make dcshell`

 After the above command execute following command
* `python manage.py generateapikey <key_name>`

### How to use API key.

Add the API key generated from above command into the Authorization header of each request. Like below:

`Authorization: Api-Key <API_KEY>`



