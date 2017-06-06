# Docker for Beginners

https://prakhar.me/docker-curriculum/ with code forked at 

https://github.com/arafatm/docker-curriculum/tree/master/flask-app

My code in https://www.github.com/arafatm/docker_for_beginners

## Docker Run

`docker info` displays system wide information 

`docker inspect` for low level information on an object
- `-f` formats output using the given GO template
- `-s` displays total file size for a container
- `--type` returns JSON for specified type

`docker pull busybox`

`docker run busybox`

`docker images`

`docker run busybox echo hello from busybox`

`docker ps` shows currently running containers

`docker ps -a` shows all containers we _ran_

`docker run -it busybox sh` attaches to interactive tty in container 

If we `rm -rf bin` inside the container, exit, then rerun above command we 
notice that docker **creates a new container** every time

`docker rm <CONTAINER ID>` to clean up

Since docker creates new containers, remnants of the container are 
**persisted on disk** and should be cleaned up

`docker rm $(docker ps -a -q -f status=exited)` to delete multiple containers

`docker rmi` to delete images

## Terminology

**Images** - The blueprints of our application which form the basis of 
containers.

**Containers** - Created from Docker images and run the actual application.  

**Daemon** - The background service running on the host that manages building, 
running and distributing Docker containers.

**Client** - The command line tool that allows the user to interact with the 
daemon.

**Hub** - A registry of Docker images.

## Webapps with Docker

`docker run prakhar1989/static-site` will download the image and run it in


`docker run -d -P --name static-site prakhar1989/static-site`
- `-d` detached
- `-P` publish exposed ports. 
- `--name` to give it a human name

`docker port static-site` to view ports

`http://localhost:32769/` to open port listed above ^

`docker run -p 8888:80 prakhar1989/static-site` to specify a custom port to 
foward connections

This docker image is deployable in production

## Images

`docker search ubuntu` to search the hub
- This won't show tags (versions)

`curl 'https://registry.hub.docker.com/v2/repositories/library/ubuntu/tags/'|jq '."results"[]["name"]'` to view tags available for an image
- replace *ubuntu* above with your desired image

`docker pull ubuntu:16.10` to pull ubuntu image with 16.10 tag

Types of images
- **base**
- **child** are built on base images with extra functionality
- **official** are officially maintained by docker
- **user** created by users

## Creating an Image

Creating a Flask app (python microframework)

Edit a dockerfile e.g. 
https://github.com/arafatm/docker-curriculum/blob/master/flask-app/Dockerfile

Once we have the dockerfile `docker build -t arafatm/catnip .`
- Note this will create an `arafatm/catnip` image we can see using `docker 
  images`

`docker run -p 8888:5000 -d --name catnip arafatm/catnip` to run the flask app

## Docker on AWS

`docker push arafatm/catnip` to publish the image
- This also creates a doc page https://hub.docker.com/r/arafatm/catnip/

Create new Elastic Beanstalk app 
https://us-west-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-west-2#/welcome
- "Create New Application" on top right
- "Web Server Environment"
- "Docker" predefined configuration

Edit 
https://github.com/arafatm/docker-curriculum/blob/master/flask-app/Dockerrun.aws.json
