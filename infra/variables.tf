variable "aws_region" {
  description = "The AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "repository_name" {
  description = "The name of the repository"
  type        = string
}

variable "ssh_key_name" {
  description = "The name of the SSH key to use"
  type        = string
}

variable "security_group_name" {
  description = "The name of the security group to use"
  type        = string
}

variable "volume_size" {
  description = "The size of the volume"
  type        = number
  default     = 8
}