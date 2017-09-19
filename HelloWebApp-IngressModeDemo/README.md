# Using Docker Swarm and Ingress mode to run a Windows+Linux mixed-OS ‘containerized’ application
### Kallie Bracken, Program Manager, Windows Container Networking

This repository holds the supporting files/source code for a demo that I created, to walk through how to run a Windows+Linux mixed-OS ‘containerized’ application using Docker Swarm and ingress "routing mesh." 


## APP COMPONENTS

### Web Front-End Image (Windows)

- Go to .\WebFrontend-BuildImage
- Build the docker image: `docker build -t hello-count-web-plus .`


### Redis Back-End Image (Linux)

- Pull the redis:alpine image from github; `docker pull redis:alpine`


### System prerequisites

- TODO

## STEPS TO RUN APP USING DOCKER STACK DEPLOY
From this directory, run:
```
docker stack deploy --compose-file .\docker-compose.yml hello
```

## STEPS TO RUN APP MANUALLY

- Initialize swarm
```
docker swarm init
```

- Join workers
```
docker swarm join <JOIN-TOKEN>
docker node ls`
```

- Label nodes
```
docker node update --label-add os=windows <NODE ID>
docker node update --label-add os=windows <NODE ID>
docker node update --label-add os=linux <NODE ID>
```

- Create overlay network
```
docker network create -d overlay hello_net
```

- Create Linux redis service
```
docker service create --name db --endpoint-mode=dnsrr --network hello_net --constraint 'node.labels.os==linux' redis:alpine
```

- Create Windows web service
```
docker service create --name web --publish 8000:8000 --network hello_net --constraint 'node.labels.os==windows' hello-count-web-plus
```

- View app via browser; Show count increase with every refresh BUT container ID/IP don't change
```
docker service ls
ipconfig
http://<IP>:8000/
```

- Scale web service
```
docker service scale web=5
```

- View app via browser; now container ID/IP change!

