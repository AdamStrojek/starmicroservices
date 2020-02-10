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
