# Starmicroservices

This is POC project of microservices application based on Starlette framework. Base conception is to split whole application
into atomic REST services which are responsible for only single functionality. Also project was created to use Docker containers
for easier scalability of application and ease of deployment. As a side effect this is providing great and consistent
environment for developers.

One important thing is always how to manage authorization and permissions for other endpoints without checking it each
microservice. This is due to fact that each of microservice need to answer as quick as it is possible. It is easily
achievable using JWT tokens, which can be trusted, when key is stored in safe place.

Another important aspect of handling heavier loads of requests is to use asyncio. Thanks to using coroutines we can increase
response time thanks to releasing CPU when any IO action is performed. In future it can be easily used to fetch data
from database

When writing microservice application you always need to keep in mind that some of source code will be shared between
different services. Great idea is to avoid coping it from one place to another. For this purpose I have created shared
library folder. Currently it is being used as shared volume between microservices, later it can be transformed into
separate library that will be installed next to another files using requirements.txt file

Project was created based on Python 3.7 using asyncio features

## Project structure

List of source code included in repository

- `utils/` - this folder contains common components of application which are shared between different microservices
- `boilerplate_backend/` - this folder contains boilerplate for new microservices, to reduce code that need to be created
and that cannot be shared between other applications
- `auth_backend/` - this folder contains simple implementation of microservice that is responsible for authentication
and authorization, using JWT, for other parts of project
- `resource_backend/` - this folder contains simple microservice that is responsible for returning a current time based
on permissions that are assigned for user
- `webapp/` - this folder contains microservice that is example of using other parts of application in communication together
- `postman/` - this folder contains sample Postman collections that help in starting development process. No longer need
to guess what endpoint and how it should be called

Later this project can be spited into git submodules to separate source code of different parts of code.

## Setup environment

To setup fully working environment follow this steps:

### Create new `.env` file in main folder of project
This file is added to gitignore list, so it will not be commited to ensure that all secrets will remain secrets. In file
`env.example` you always should have the newest version of all available settings variables. For development process
you can just simply copy this file

```shell script
$ cp env.example .env
```

### Start docker-compose project
Even though each microservice is separated container to help in set up development environment docker-compose scripts were
created. This allow to start project fast, after installing docker and docker-compose, with simple command

```shell script
$ docker-compose up
```

For docker and docker-compose installation please consult with [official documentation](https://docs.docker.com/install/)

## Good practices
Always create new microservice using boilerplate. This will allow in faster start of it. Also always include smoke endpoint
which will allow to check status of service. It can be used later in CI and CD processes to check does all microservices
started correctly to avoid situation that one of it is failing and we need to manually reset kubernetes deployment to older
version.

## Usage
This application implements 3 microservices. Each of it have own purpose for this application, here is short description
for them. For more details about endpoints check `/schema` endpoint which produces
[OpenAPI 3](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md)

- `auth_backend` - microservice responsible for authentication and authorisation of user. You have two endpoint, first is
responsible for creating new token, which you provide as `X-Token` header, in JWT format, second is responsible for verifing
permissions
- `resource_backend`- microservice responsible for providing resources to rest of application. This POC project is providing
only time in ISO-8601 format and timestamp
- `webapp` - microservice that was created as demo microservice that is contacting other microservices
