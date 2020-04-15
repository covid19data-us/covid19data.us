# How to create Docker Image

## Create your own Grafana with DataSource

- Create the docker image using Dockerfile

```sh
(⎈ |star:lord) galaxy ] ☘ docker build -t grafana:mine .
(⎈ |star:lord) galaxy ] ☘ 
```

- Start the docker container

```sh
(⎈ |star:lord) galaxy ] ☘ docker run -d -p 3000:3000 --name=grafana-mine grafana:mine
299eef92be816548a00f6a690689506fe41fe420bd141eef0ae59870caae36ed
(⎈ |star:lord) galaxy ] ☘ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
299eef92be81        grafana:mine        "/run.sh"           5 minutes ago       Up 5 minutes        0.0.0.0:3000->3000/tcp   grafana-mine
(⎈ |star:lord) galaxy ] ☘ 
(⎈ |star:lord) galaxy ] ☘ open -a "Google Chrome" "http://localhost:3000/"
(⎈ |star:lord) galaxy ] ☘ 
```

## Create your own Grafana without DataSource

```sh
(⎈ |star:lord) galaxy ] ☘  docker run -d \
-p 3000:3000 \
--name=grafana \
-e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-worldmap-panel" \
grafana/grafana
(⎈ |star:lord) galaxy ] ☘ 
```