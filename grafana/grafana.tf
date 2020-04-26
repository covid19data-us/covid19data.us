### Declare Provider as Grafana
provider "grafana" {
  url  = "http://localhost:3000/"
  auth = "username:password"
}

### Create Grafana Folder
resource "grafana_folder" "collection" {
  title = var.folder
}

### Create Grafana DataSource
resource "grafana_data_source" "covid19data" {
  type          = var.datasource_type
  name          = var.datasource_name
  url           = var.datasource_url
  is_default    = false
}

### Create Grafana Dashboards
resource "grafana_dashboard" "metrics" {
  for_each    = var.dashboards

  folder      = grafana_folder.collection.id
  config_json = file(each.value)
  depends_on  = [grafana_data_source.covid19data]
}