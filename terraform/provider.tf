terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  subscription_id = "5cd67797-9120-4291-a642-2399c747b9c6"
  tenant_id       = "24db36fc-d58b-42a1-b107-cedf1d2c63f1"
  features {}
}
