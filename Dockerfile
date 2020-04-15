FROM grafana/grafana

MAINTAINER Sandeep "sandeeplamb@gmail.com"

USER root
ARG SHA="unknown"

ENV GF_PATHS_PLUGINS="/var/lib/grafana/plugins"
ENV GF_CLI="/usr/share/grafana/bin/grafana-cli"

ADD ./configs /tmp/configs
ADD ./grafana /tmp/grafana

RUN mv /tmp/configs/grafana.ini /etc/grafana/grafana.ini \
    && mkdir -p /var/lib/grafana/dashboards \
    && mv /tmp/configs/dashboards.yaml /etc/grafana/provisioning/dashboards/dashboards.yaml \
    && mv /tmp/configs/datasource.yaml /etc/grafana/provisioning/datasources/datasource.yaml \
    && cp /tmp/grafana/*json /var/lib/grafana/dashboards \
    && chown grafana.grafana -R /etc/grafana/provisioning \
    && chown grafana.grafana -R /var/lib/grafana/dashboards

LABEL ${MAINTAINER} ${SHA}

USER grafana
RUN  $GF_CLI --pluginsDir $GF_PATHS_PLUGINS plugins install grafana-worldmap-panel