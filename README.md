# RecyclePay API

![RecyclePay API](https://github.com/decadevs/recyclepay-api/actions/workflows/ci.yml/badge.svg?branch=main)

API Service backing client interfaces

## Technologies

- [Python 3.9](https://python.org) : Base programming language for development
- [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
- [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
- [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
- [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
- [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
- [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description

## Getting Started

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `git clone https://github.com/decadevs/recyclepay-api.git` to clone the project repository.

Change directory into the project folder `cd recyclepay-api` and build the base python image used for the project that was specified in **_dockerfile_** by running `docker build .` _Note the dot (.) at end of the command_.

Spin up other services needed for the project that are specified in **_docker-compose.yml_** file by running the command `docker-compose up`. At this moment, your project should be up and running with a warning that _you have unapplied migrations_.

Open up another terminal and run this command `docker-compose exec api python project/manage.py makemigrations` for creating new migrations based on the models defined and also run `docker compose exec api python project/manage.py migrate` to apply migrations.

In summary, these are the lists of commands to run in listed order, to start up the project.

```docker
1. git clone https://github.com/decadevs/recyclepay-api.git
2. cd recyclepay-api
3. docker build .
4. docker-compose up
5. docker-compose exec api python project/manage.py makemigrations
6. docker-compose exec api python project/manage.py migrate
```

## Running Tests

Currently, truthy tests has been provided in each of the application defined in the project, before running the tests with the following command make sure that your api service is up and running.

```docker
docker-compose exec api python project/manage.py test
```

## Endpoints

![recyclepay endpoints](https://user-images.githubusercontent.com/22947152/178920967-2729b151-67b7-4e2f-b8f6-d6487d55d765.png)


## License

The MIT License - Copyright (c) 2020 - Present, Decagon Institute. https://decagonhq.com/

## Contributors

<table>
    <tr>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/22947152?v=4" width="100px;">
                <br /><sub><b>Akorede Olawole</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/42410665?v=4" width="100px;">
                <br /><sub><b>Olusola Afolayan</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/58984618?v=4" width="100px;">
                <br /><sub><b>Samson Kitigo</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/83557813?v=4" width="100px;">
                <br /><sub><b>Nwokocha Maruche</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/98774165?v=4" width="100px;">
                <br /><sub><b>Msendoo Chile</b></sub>
            </div>
        </td>
      </tr>
      <tr>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/21022645?v=4" width="100px;">
                <br /><sub><b>Mark Eke</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/32337103?v=4" width="100px;">
                <br /><sub><b>Ifeanyi Omeata</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/61989480?v=4" width="100px;">
                <br /><sub><b>Jonathan Kolawole</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/86872686?v=4" width="100px;">
                <br /><sub><b>Josiah Akpaetuk</b></sub>
            </div>
        </td>
      </tr>
      <tr>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/67855565?v=4" width="100px;">
                <br /><sub><b>Hakeem Oyerinmade - Lead</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars0.githubusercontent.com/u/61936161?s=400&v=4" width="100px;">
                <br /><sub><b>Rafihatu Oziohu Bello - Lead</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/41590285?v=4" width="100px;">
                <br /><sub><b>Adenike Awofeso - Lead</b></sub>
            </div>
        </td>
      </tr>
</table>
