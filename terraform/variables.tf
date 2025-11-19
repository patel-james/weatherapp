variable "location" {
  description = "Azure region for all the resources"
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "weatherapp-rg"
}

variable "container_app_env_name" {
  description = "Name of the container app environment"
  type        = string
  default     = "weatherapp-env"
}

variable "container_app_name" {
  description = "Name of the Container App"
  type        = string
  default     = "weatherapp-api"
}

variable "docker_image" {
  description = "Container image to deploy from docker"
  type        = string
  default     = "pateljames/weatherapp:v2"
}

variable "weather_api_key" {
  description = "API key for OpenWeather"
  type        = string
}
