# Grafana Dashboards

Below are the dashboards used in Grafana

## Case Fatality US Rate

## Large Map - Cases by County

## Large Map - Cases World

## Map Panel Dashboard

## State, County - MAP & Case Data

## Tables -  US Case View

## USA Data [metrics]

# Automation Grafana Dashboards

We are using [terraform grafana provider](https://www.terraform.io/docs/providers/grafana/index.html) to update dashboards in the grafana.

[terraform grafana provider](https://www.terraform.io/docs/providers/grafana/index.html) can also be used to create datasources too.

## Pre-Flight Checks

- Make sure you have latest [terraform](https://www.terraform.io/downloads.html) installed
- In file *grafana.tf*
- Please update the *url* variable to point to correct Grafana 
- Please update the *auth* variable correct username and password for Grafana
- In file *variables.tf*
- Please update the name of your dashboard in the map variable *dashboards*

## How to upload dashboards

Please run the following commands to create datasource and upload dashboards in the grafana.

```sh
(⎈ |star-lord:grafana) grafana ] ☘   terraform init
(⎈ |star-lord:grafana) grafana ] ☘   terraform plan
```