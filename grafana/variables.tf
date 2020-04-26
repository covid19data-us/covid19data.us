variable "folder" {
  description = "grafana folder name"
  type        = string
  default     = "Covid-US"
}

variable "datasource_type" {
  description = "Type of DataSource"
  type        = string
  default     = "prometheus"
}

variable "datasource_name" {
  description = "Name of DataSource"
  type        = string
  default     = "Prometheus"
}

variable "datasource_url" {
  description = "URL of DataSource"
  type        = string
  default     = "http://api.covid19data.us/"
}

variable "dashboards" {
  description = "Grafana dashboards"
  type        = map
  default = {
    a = "Aggregate_World_US.json"
    b = "case_fatality_us_rate.json"
    c = "Large Map - Cases by County.json"
    d = "Large Map - Cases World.json"
    e = "map_panel_dashboard.json"
    f = "New dashboard death rate and death growth.json"
    g = "State, County - MAP & Case Data.json"
    h = "Tables -  US Case View.json"
    i = "USA Data [metrics].json"
  }
}