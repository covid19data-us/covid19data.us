# Docker Image

```sh

docker run -d \
-p 3000:3000 \
--name=grafana \
-e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-worldmap-panel" \
grafana/grafana


docker run -d -p 3001:3000 --name=grafana-mine grafana:mine
```