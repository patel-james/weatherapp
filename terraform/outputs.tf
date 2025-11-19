output "resource_group_name" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.rg.name
}

output "container_app_environment" {
  description = "The Container App Environment name"
  value       = azurerm_container_app_environment.env.name
}

output "container_app_name" {
  description = "The deployed Container App name"
  value       = azurerm_container_app.app.name
}

output "container_app_url" {
  description = "Public URL of the Azure Container App"
  value       = azurerm_container_app.app.latest_revision_fqdn
}
