# JOBS.TI

A web application that simulates a job employment site. Made using Django 3.2, Python 3.10.4 and Django REST 3.13.1.

Deployed project: https://jobs-ti-project.herokuapp.com/

Company user credentials:
   * email: cerozi@gmail.com
   * password: testuser123

Employee user credentials:
   * email: math@gmail.com
   * password: testuser123

<hr></hr>

To run the project on your local machine, you need to have Docker Desktop installed. Once you have it, at the root of the project execute the following command on CMD:
```
docker-compose up --build -d
```
```
docker-compose exec web python manage.py migrate
```

Now, the project can be found at your 0.0.0.0:8000. To see the logs, get the container ID and then write:
```
docker logs --follow [container_id]
```





