terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {}
}

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "app_server" {
    ami           = "ami-051f8a213df8bc089"  #Amazon Linux 2 AMI (HVM)
    instance_type = "t2.micro"

    tags = {
      Name = var.repository_name
      Date = timestamp()
      AutoStart = "true"
    }

    root_block_device {
        volume_size = var.volume_size
    }  

    key_name = var.ssh_key_name
    security_groups =  [var.security_group_name]
}


output "ec2_ip" {
  value = aws_instance.app_server.public_ip
}