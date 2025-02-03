terraform {
  backend "local" {}
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }

}

variable "filename" {
  type    = string
  default = "example.txt"

}

provider "local" {}

resource "local_file" "example" {
  filename = "${path.module}/${var.filename}"
  content  = "Hello, this is a Terraform-managed file!"
}

output "FileContentBase64" {
  value = local_file.example.content_base64
  
}