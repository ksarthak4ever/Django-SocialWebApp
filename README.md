# Django-SocialWebApp

This is a social login webapp using which a user can log via Github, Linkedin and Twitter. This webapp is made using Django, Django REST Framework, Docker, PostgreSQL, django-social-auth etc. This webapp uses session authentication as the authentication framework and has APIs for covering all the functionalities of a User i.e login, setting password, fetch user details, fetching users and searching for a user.

I used Docker for ease of spinning up the env and all related services such as database etc.


## Setup

* You need to have Docker and Docker-compose installed on your machine to run this webapp smoothly.

* Clone this repository and enter command :~ `sudo docker build .` and `sudo docker-compose build` which will build the docker image used to run the webapp.

* Once the image has been built you can simply enter the command `sudo docker-compose up` which will start the containers i.e all the services such as django server and postgres as the database.

* One can then simply go to the route :~ `0.0.0.0:8000` to access the home page of the webapp and proceed to login, normally or using the available platforms.

* To make a superuser one can enter the command :~ `sudo docker-compose run project sh -c "python manage.py createsuperuser` and enter the email and password respectively. I have added the django admin setup for user database.

* I have made different APIs covering all the functionalities of a user and applied permission checks on them as required using custom decorator. As the webapp is using session authentication make sure that after you login you store the csrf token in `X-CSRFToken` header with appropriate value in Postman or any other API testing tool so you can access the rest of the APIs as they require the user to be authorized.