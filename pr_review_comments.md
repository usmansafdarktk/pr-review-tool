# GitHub Pull Request Reviews and Comments


---

## PR #30: [Sprint 5 – Modular WordPress Deployment with RDS (Terraform)](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/30)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-06-12T11:04:38Z
- **State:** open

_No review summaries._

_No inline comments._


---

## PR #29: [Sprint 5: WordPress Deployment with RDS using Terraform](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/29)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-06-12T06:54:26Z
- **State:** open

### Review Summaries:

**Reviewer:** `FarsanGul`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-12T07:19:57Z
> Left some comments

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-13T05:15:36Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-13T05:15:55Z
> _No comment text_

### Inline Comments with Code Context:

**Reviewer:** `FarsanGul`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/variables.tf`
- **Line:** `None`
> instance type should be defined in the default variable. Which instance type are we using ?

**Reviewer:** `FarsanGul`
- **File:** `submissions/HuzaifaAwan/modules/rds/main.tf`
- **Line:** `None`
> Send this port id from variable.

**Reviewer:** `FarsanGul`
- **File:** `submissions/HuzaifaAwan/modules/rds/main.tf`
- **Line:** `None`
> Same as above

**Reviewer:** `FarsanGul`
- **File:** `submissions/HuzaifaAwan/modules/rds/main.tf`
- **Line:** `31`
```diff
#subnet group for db
resource "aws_db_subnet_group" "this" {
  name       = "${var.name_prefix}-db-subnet-group"
  subnet_ids = var.private_subnet_ids

  tags = merge(module.main_env.tags,
    {
      Name = "${var.name_prefix}-db-subnet-group"
  })
}

#RDS sg
resource "aws_security_group" "rds_sg" {
  name_prefix = "${var.name_prefix}-rds-sg"
  description = "Allow mysql from ec2"
  vpc_id      = var.vpc_id

  ingress {
    description     = "Allow mysql from ec2"
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [var.ec2_sg_id]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
>>>     cidr_blocks = ["0.0.0.0/0"] <<<   # Line commented on
```
> Use this from variable file as well

**Reviewer:** `FarsanGul`
- **File:** `submissions/HuzaifaAwan/wordpress-deployment/.gitignore`
- **Line:** `9`
```diff
# Terraform
*.tfstate
*.tfstate.backup
.terraform/
*.tfvars
terraform.tfvars
.terraform.lock.hcl
.terraform.tfstate.lock.info
>>> rendered_userdata.sh <<<   # Line commented on
```
> user data should not be in git ignore.

**Reviewer:** `FarsanGul`
- **File:** `submissions/HuzaifaAwan/modules/rds/main.tf`
- **Line:** `None`
> This is not a good approach keeping in mind the security aspects. Use a more secure way for passing credentials.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/modules/rds/main.tf`
- **Line:** `None`
> @FarsanGul feedback addressed.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/variables.tf`
- **Line:** `None`
> @FarsanGul feedback addressed.


---

## PR #28: [feat: add ec2 module and test examples with proper .gitignore](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-30T07:17:58Z
- **State:** closed

### Review Summaries:

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-30T11:05:19Z
> Good Work 
left some comments

**Reviewer:** `huzaifaxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-06-02T06:45:40Z
> LGTM!!!

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T06:52:28Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T06:53:19Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T07:03:53Z
> @usmansafdarktk there are still white lines in your code.

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-06-02T07:51:48Z
> LGTM!

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:46:03Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:46:11Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:46:22Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:46:28Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:46:35Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:46:49Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:47:03Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:47:14Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:47:36Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:47:46Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:47:54Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T09:47:58Z
> _No comment text_

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-06-02T10:09:35Z
> LGTM

Good work

**Reviewer:** `Moiz-0786`
- **State:** `APPROVED`
- **Submitted:** 2025-06-06T00:47:22Z
> LGTM

### Inline Comments with Code Context:

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/README.md`
- **Line:** `None`
> ```suggestion
    <!-- BEGIN_TF_DOCS -->

    <!-- END_TF_DOCS -->
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/main.tf`
- **Line:** `53`
```diff
resource "tls_private_key" "ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated" {
  key_name   = var.key_name
  public_key = tls_private_key.ec2_key.public_key_openssh

  tags = module.main_env.tags
}

resource "local_file" "private_key" {
  content         = tls_private_key.ec2_key.private_key_pem
  filename        = "${path.module}/${var.key_name}.pem"
  file_permission = "0400"
}

resource "aws_security_group" "public_sg" {
  name        = var.public_sg_name
  description = "Security group for public EC2"
  vpc_id      = var.vpc_id

  dynamic "ingress" {
    for_each = var.public_ingress_rules
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = module.main_env.tags
}

resource "aws_security_group" "private_sg" {
```
> just a suggestion to make it somewhat dynamic


```suggestion

resource "aws_security_group_rule" "ingress" {
  count             = length(var.ingress_rules)
  type              = "ingress"
  from_port         = var.ingress_rules[count.index].from_port
  to_port           = var.ingress_rules[count.index].to_port
  protocol          = var.ingress_rules[count.index].protocol
  cidr_blocks       = var.ingress_rules[count.index].cidr_blocks
  description       = var.ingress_rules[count.index].description
  security_group_id = "TBD"
}
```



For variable

```.tf
variable "ingress_rules" {
  description = "Ingress rules to add to Jumphost security group."
  type = list(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
    description = string
  }))
  default = []
}
```


variable declaration like this


```.tf
 ingress_rules = [{
    from_port   = 22,
    to_port     = 22,
    protocol    = "tcp",
    cidr_blocks = ["10.0.0.0/16"],
    description = "Allow traffic from VPC"
  }]
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/main.tf`
- **Line:** `None`
> let variablize it and give its default empty

```.tf

resource "aws_security_group_rule" "ingress" {
  count             = length(var.egree_rules)
  type              = "egress"
  from_port         = var.ingress_rules[count.index].from_port
  to_port           = var.ingress_rules[count.index].to_port
  protocol          = var.ingress_rules[count.index].protocol
  cidr_blocks       = var.ingress_rules[count.index].cidr_blocks
  description       = var.ingress_rules[count.index].description
  security_group_id = "TBD"
}
```


variable declaration

```.tf
variable "egress_rules" {
  description = "egress rules to add to Jumphost security group."
  type = list(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
    description = string
  }))
  default = []
}
```

```.tf
 egress_rules = [{
    from_port   = 0,
    to_port     = 0,
    protocol    = "-1",
    cidr_blocks = ["0.0.0.0/0"],
    description = "Allow traffic from VPC"
  }]
  ```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/main.tf`
- **Line:** `127`
```diff
resource "tls_private_key" "ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated" {
  key_name   = var.key_name
  public_key = tls_private_key.ec2_key.public_key_openssh

  tags = module.main_env.tags
}

resource "local_file" "private_key" {
  content         = tls_private_key.ec2_key.private_key_pem
  filename        = "${path.module}/${var.key_name}.pem"
  file_permission = "0400"
}

resource "aws_security_group" "public_sg" {
  name        = var.public_sg_name
  description = "Security group for public EC2"
  vpc_id      = var.vpc_id

  dynamic "ingress" {
    for_each = var.public_ingress_rules
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = module.main_env.tags
}

resource "aws_security_group" "private_sg" {
  name        = var.private_sg_name
  description = "Security group for private EC2"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr] # Only internal SSH
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = module.main_env.tags
}

# Create ENI (Elastic Network Interface) for Public EC2
resource "aws_network_interface" "public_eni" {
  subnet_id       = var.public_subnet_id
  security_groups = [aws_security_group.public_sg.id]
  tags            = module.main_env.tags
}

# Create ENI for Private EC2
resource "aws_network_interface" "private_eni" {
  subnet_id       = var.private_subnet_id
  security_groups = [aws_security_group.private_sg.id]
  tags            = module.main_env.tags
}

resource "aws_instance" "public" {
```
> make it conditional deploy

```suggestion
resource "aws_instance" "public" {
count = var.enable_eni ? 1 : 0
```

if var.enable == True => 1
else => 0

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/output.tf`
- **Line:** `10`
```diff
output "public_instance_id" {
  value       = aws_instance.public.id
  description = "ID of the public EC2 instance"
}

output "selected_ami_id" {
  value       = data.aws_ami.selected.id
  description = "AMI ID being used by EC2 instances"
}
>>>  <<<   # Line commented on
```
> White line

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/output.tf`
- **Line:** `35`
```diff
output "public_instance_id" {
  value       = aws_instance.public.id
  description = "ID of the public EC2 instance"
}

output "selected_ami_id" {
  value       = data.aws_ami.selected.id
  description = "AMI ID being used by EC2 instances"
}


output "private_instance_id" {
  value       = aws_instance.private.id
  description = "ID of the private EC2 instance"
}

output "public_instance_public_ip" {
  value       = aws_instance.public.public_ip
  description = "Public IP of the public EC2 instance"
}

output "key_pair_name" {
  value       = aws_key_pair.generated.key_name
  description = "Generated EC2 key pair name"
}

output "public_security_group_id" {
  value       = aws_security_group.public_sg.id
  description = "Security group ID for the public EC2 instance"
}

output "private_security_group_id" {
  value       = aws_security_group.private_sg.id
  description = "Security group ID for the private EC2 instance"
>>> } <<<   # Line commented on

```
> white line

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/output.tf`
- **Line:** `45`
```diff
output "public_instance_id" {
  value       = aws_instance.public.id
  description = "ID of the public EC2 instance"
}

output "selected_ami_id" {
  value       = data.aws_ami.selected.id
  description = "AMI ID being used by EC2 instances"
}


output "private_instance_id" {
  value       = aws_instance.private.id
  description = "ID of the private EC2 instance"
}

output "public_instance_public_ip" {
  value       = aws_instance.public.public_ip
  description = "Public IP of the public EC2 instance"
}

output "key_pair_name" {
  value       = aws_key_pair.generated.key_name
  description = "Generated EC2 key pair name"
}

output "public_security_group_id" {
  value       = aws_security_group.public_sg.id
  description = "Security group ID for the public EC2 instance"
}

output "private_security_group_id" {
  value       = aws_security_group.private_sg.id
  description = "Security group ID for the private EC2 instance"
}


output "private_key_pem_path" {
  value       = local_file.private_key.filename
  description = "Path to saved private key PEM file"
}
```
> please add End of line

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/variables.tf`
- **Line:** `10`
```diff
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_name_pattern" {
  description = "AMI name pattern to search for"
  type        = string
>>>   default     = "amzn2-ami-hvm-*-x86_64-gp2" <<<   # Line commented on
}

variable "ami_owners" {
  description = "AMI owners"
  type        = list(string)
  default     = ["amazon"]
}

variable "virtualization_type" {
  description = "Virtualization type to filter by"
  type        = string
  default     = "hvm"
}

```
> white line

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/variables.tf`
- **Line:** `119`
```diff
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_name_pattern" {
  description = "AMI name pattern to search for"
  type        = string
  default     = "amzn2-ami-hvm-*-x86_64-gp2"
}

variable "ami_owners" {
  description = "AMI owners"
  type        = list(string)
  default     = ["amazon"]
}

variable "virtualization_type" {
  description = "Virtualization type to filter by"
  type        = string
  default     = "hvm"
}


variable "vpc_id" {
  description = "VPC ID for security group"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block of the VPC (used for internal private SG access)"
  type        = string
}

variable "public_subnet_id" {
  description = "Subnet ID for public EC2 instance"
  type        = string
}

variable "private_subnet_id" {
  description = "Subnet ID for private EC2 instance"
  type        = string
}

variable "key_name" {
  description = "Key pair name to create"
  type        = string
}

# PUBLIC SECURITY GROUP
variable "public_sg_name" {
  description = "Name of the security group for public EC2 instance"
  type        = string
}

variable "public_ingress_rules" {
  description = "List of ingress rules for public EC2 instance"
  type = list(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  }))
}

# PRIVATE SECURITY GROUP
variable "private_sg_name" {
  description = "Name of the security group for private EC2 instance"
  type        = string
}
```
> please add EOL

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/examples/ec2-test/main.tf`
- **Line:** `3`
```diff
module "env" {
  source = "../../env"
>>>  <<<   # Line commented on
  env_vars = {
    namespace = "xgrid"
    stage     = "dev"
    name      = "ec2"
    team      = "Firebirds"
    owner     = "m.usman@xgrid.co"
  }
}

module "vpc" {
  source             = "../../vpc-module"
  vpc_cidr           = var.vpc_cidr
```
> you can remove env module declaration and just use
env_var= var.env_var

it will inherit property automatically

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/examples/ec2-test/variables.tf`
- **Line:** `1`
```diff
>>> variable "instance_type" { <<<   # Line commented on
```
> you can add env_var here and then give its value in module lateron
```suggestion
variable "env_vars" {
  type        = map(any)
  description = "Environment variables for modules"
  default = {
    namespace = "test"
    stage     = "private"
    name      = "jumphost"
    TF-Module = "jumphost"
    delimiter = "-"
  }
}
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/examples/ec2-test/main.tf`
- **Line:** `None`
> once env_var defined and declared, you can safely remove this bit

**Reviewer:** `munemxgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/README.md`
- **Line:** `None`
> White line

**Reviewer:** `munemxgrid`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/.terraform-docs.yml`
- **Line:** `None`
> White line

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/README.md`
- **Line:** `None`
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/main.tf`
- **Line:** `53`
```diff
resource "tls_private_key" "ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated" {
  key_name   = var.key_name
  public_key = tls_private_key.ec2_key.public_key_openssh

  tags = module.main_env.tags
}

resource "local_file" "private_key" {
  content         = tls_private_key.ec2_key.private_key_pem
  filename        = "${path.module}/${var.key_name}.pem"
  file_permission = "0400"
}

resource "aws_security_group" "public_sg" {
  name        = var.public_sg_name
  description = "Security group for public EC2"
  vpc_id      = var.vpc_id

  dynamic "ingress" {
    for_each = var.public_ingress_rules
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = module.main_env.tags
}

resource "aws_security_group" "private_sg" {
```
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/main.tf`
- **Line:** `None`
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/main.tf`
- **Line:** `127`
```diff
resource "tls_private_key" "ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated" {
  key_name   = var.key_name
  public_key = tls_private_key.ec2_key.public_key_openssh

  tags = module.main_env.tags
}

resource "local_file" "private_key" {
  content         = tls_private_key.ec2_key.private_key_pem
  filename        = "${path.module}/${var.key_name}.pem"
  file_permission = "0400"
}

resource "aws_security_group" "public_sg" {
  name        = var.public_sg_name
  description = "Security group for public EC2"
  vpc_id      = var.vpc_id

  dynamic "ingress" {
    for_each = var.public_ingress_rules
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = module.main_env.tags
}

resource "aws_security_group" "private_sg" {
  name        = var.private_sg_name
  description = "Security group for private EC2"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr] # Only internal SSH
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = module.main_env.tags
}

# Create ENI (Elastic Network Interface) for Public EC2
resource "aws_network_interface" "public_eni" {
  subnet_id       = var.public_subnet_id
  security_groups = [aws_security_group.public_sg.id]
  tags            = module.main_env.tags
}

# Create ENI for Private EC2
resource "aws_network_interface" "private_eni" {
  subnet_id       = var.private_subnet_id
  security_groups = [aws_security_group.private_sg.id]
  tags            = module.main_env.tags
}

resource "aws_instance" "public" {
```
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/output.tf`
- **Line:** `10`
```diff
output "public_instance_id" {
  value       = aws_instance.public.id
  description = "ID of the public EC2 instance"
}

output "selected_ami_id" {
  value       = data.aws_ami.selected.id
  description = "AMI ID being used by EC2 instances"
}
>>>  <<<   # Line commented on
```
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/output.tf`
- **Line:** `35`
```diff
output "public_instance_id" {
  value       = aws_instance.public.id
  description = "ID of the public EC2 instance"
}

output "selected_ami_id" {
  value       = data.aws_ami.selected.id
  description = "AMI ID being used by EC2 instances"
}


output "private_instance_id" {
  value       = aws_instance.private.id
  description = "ID of the private EC2 instance"
}

output "public_instance_public_ip" {
  value       = aws_instance.public.public_ip
  description = "Public IP of the public EC2 instance"
}

output "key_pair_name" {
  value       = aws_key_pair.generated.key_name
  description = "Generated EC2 key pair name"
}

output "public_security_group_id" {
  value       = aws_security_group.public_sg.id
  description = "Security group ID for the public EC2 instance"
}

output "private_security_group_id" {
  value       = aws_security_group.private_sg.id
  description = "Security group ID for the private EC2 instance"
>>> } <<<   # Line commented on

```
> Addressed. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/output.tf`
- **Line:** `45`
```diff
output "public_instance_id" {
  value       = aws_instance.public.id
  description = "ID of the public EC2 instance"
}

output "selected_ami_id" {
  value       = data.aws_ami.selected.id
  description = "AMI ID being used by EC2 instances"
}


output "private_instance_id" {
  value       = aws_instance.private.id
  description = "ID of the private EC2 instance"
}

output "public_instance_public_ip" {
  value       = aws_instance.public.public_ip
  description = "Public IP of the public EC2 instance"
}

output "key_pair_name" {
  value       = aws_key_pair.generated.key_name
  description = "Generated EC2 key pair name"
}

output "public_security_group_id" {
  value       = aws_security_group.public_sg.id
  description = "Security group ID for the public EC2 instance"
}

output "private_security_group_id" {
  value       = aws_security_group.private_sg.id
  description = "Security group ID for the private EC2 instance"
}


output "private_key_pem_path" {
  value       = local_file.private_key.filename
  description = "Path to saved private key PEM file"
}
```
> Addressed. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/variables.tf`
- **Line:** `10`
```diff
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_name_pattern" {
  description = "AMI name pattern to search for"
  type        = string
>>>   default     = "amzn2-ami-hvm-*-x86_64-gp2" <<<   # Line commented on
}

variable "ami_owners" {
  description = "AMI owners"
  type        = list(string)
  default     = ["amazon"]
}

variable "virtualization_type" {
  description = "Virtualization type to filter by"
  type        = string
  default     = "hvm"
}

```
> Addressed. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/ec2-module/variables.tf`
- **Line:** `119`
```diff
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_name_pattern" {
  description = "AMI name pattern to search for"
  type        = string
  default     = "amzn2-ami-hvm-*-x86_64-gp2"
}

variable "ami_owners" {
  description = "AMI owners"
  type        = list(string)
  default     = ["amazon"]
}

variable "virtualization_type" {
  description = "Virtualization type to filter by"
  type        = string
  default     = "hvm"
}


variable "vpc_id" {
  description = "VPC ID for security group"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block of the VPC (used for internal private SG access)"
  type        = string
}

variable "public_subnet_id" {
  description = "Subnet ID for public EC2 instance"
  type        = string
}

variable "private_subnet_id" {
  description = "Subnet ID for private EC2 instance"
  type        = string
}

variable "key_name" {
  description = "Key pair name to create"
  type        = string
}

# PUBLIC SECURITY GROUP
variable "public_sg_name" {
  description = "Name of the security group for public EC2 instance"
  type        = string
}

variable "public_ingress_rules" {
  description = "List of ingress rules for public EC2 instance"
  type = list(object({
    from_port   = number
    to_port     = number
    protocol    = string
    cidr_blocks = list(string)
  }))
}

# PRIVATE SECURITY GROUP
variable "private_sg_name" {
  description = "Name of the security group for private EC2 instance"
  type        = string
}
```
> Addressed. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/examples/ec2-test/main.tf`
- **Line:** `3`
```diff
module "env" {
  source = "../../env"
>>>  <<<   # Line commented on
  env_vars = {
    namespace = "xgrid"
    stage     = "dev"
    name      = "ec2"
    team      = "Firebirds"
    owner     = "m.usman@xgrid.co"
  }
}

module "vpc" {
  source             = "../../vpc-module"
  vpc_cidr           = var.vpc_cidr
```
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/examples/ec2-test/variables.tf`
- **Line:** `1`
```diff
>>> variable "instance_type" { <<<   # Line commented on
```
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/examples/ec2-test/main.tf`
- **Line:** `None`
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/28/commits/2a82dfd745b252a0a0001fb4cad4562b8e4fe75e. kindly review


---

## PR #27: [Sprint 4-PR 3: Public and Private EC2 instances and Examples folder to test module](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/27)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-29T07:18:40Z
- **State:** closed

### Review Summaries:

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-29T10:10:02Z
> Left some comments. Have a look.

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-29T12:52:26Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T06:47:46Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `APPROVED`
- **Submitted:** 2025-06-02T06:51:10Z
> LGTM!

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-02T06:52:06Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-06-02T06:56:10Z
> LGTM!

**Reviewer:** `Usman762`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-06-05T13:14:42Z
> I have mentioned some changes , please look into it.

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-05T14:14:21Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-06-05T14:14:55Z
> _No comment text_

**Reviewer:** `Usman762`
- **State:** `APPROVED`
- **Submitted:** 2025-06-05T14:17:39Z
> LGTM

### Inline Comments with Code Context:

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/examples/ec2-test/main.tf`
- **Line:** `None`
> I would recommednd to use data source get the ami dynamically.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/examples/ec2-test/main.tf`
- **Line:** `None`
> @munemxgrid feedback addressed

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/.gitignore`
- **Line:** `None`
> Add EOL

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/.gitignore`
- **Line:** `None`
> @munemxgrid feedback addressed

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/data.tf`
- **Line:** `None`
> Too many filters only name would be fine remove the other as in the name you are already specifying virtualization , architecture.

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/main.tf`
- **Line:** `None`
> Storing the private key in the project directory would not be a good approach, a better approach would be to store it in "$HOME/.ssh/" instead of project directory because you can accidentally commit it to source control.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/data.tf`
- **Line:** `None`
> @Usman762 feedback addressed

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/main.tf`
- **Line:** `None`
> @Usman762 feedback addressed


---

## PR #26: [Added Sprint 5 Task](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/26)

- **Author:** `FarsanGul`
- **Created at:** 2025-05-27T14:31:02Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #25: [Sprint 5 Task](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/25)

- **Author:** `FarsanGul`
- **Created at:** 2025-05-27T13:21:52Z
- **State:** closed

### Review Summaries:

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T13:27:02Z
> _No comment text_

### Inline Comments with Code Context:

**Reviewer:** `shujaxgrid`
- **File:** `sprints/sprint-05/README.md`
- **Line:** `None`
> Lets remove the structure heading, as both are using their submission directory and should be following that.


---

## PR #24: [Sprint 4-PR 2: Security groups for public and private EC2 instances](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/24)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-27T11:07:08Z
- **State:** closed

### Review Summaries:

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-29T10:01:39Z
> LGTM!

_No inline comments._


---

## PR #22: [Sprint 4-PR 2: Security groups for public and private EC-2 instances](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/22)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-27T08:04:16Z
- **State:** closed

### Review Summaries:

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T08:38:35Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T11:09:37Z
> _No comment text_

### Inline Comments with Code Context:

**Reviewer:** `shujaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/main.tf`
- **Line:** `39`
```diff
# aws public security group 
resource "aws_security_group" "public_ec2_sg" {
  vpc_id = var.vpc_id
  name_prefix = "${var.public_instance_sg_name_tag}-sg"
  description = "Setting up rules for security group for public EC 2 instance"
  
  dynamic "ingress" {
    for_each = var.public_sg_ingress_rule
    content {
      description = ingress.value.description
      from_port = ingress.value.from_port
      to_port = ingress.value.to_port
      protocol = ingress.value.protocol
      cidr_blocks = lookup(ingress.value, "cidr_blocks", null)
      security_groups = lookup(ingress.value, "security_groups", null)
    }
  }

  dynamic "egress" {
    for_each = var.public_sg_egress_rule
    content {
      description = egress.value.description
      from_port = egress.value.from_port
      to_port = egress.value.to_port
      protocol = egress.value.protocol
      cidr_blocks = lookup(egress.value, "cidr_blocks", null)
      security_groups = lookup(egress.value, "security_groups", null)
    }
  }
}

#security group for private ec2 instance
resource "aws_security_group" "private_ec2_sg" {
  vpc_id = var.vpc_id
  name_prefix = "${var.private_instance_sg_name_tag}-sg"
  description = "Setting up rules for security group for private EC 2 instance"

  #core ingress rule for allowing traffic from this module's public security group
>>>   ingress = { <<<   # Line commented on
```
> In Terraform, you cannot assign a map directly to the ingress attribute like that.

Terraform expects repeated block syntax (i.e., multiple ingress {} blocks), not a key-value object like ingress = { ... }.

This is a common mistake — people think they're assigning a value like with a variable, but resource blocks have a different syntax.

used neseted instead:
```
ingress {
  description     = "Allow all traffic from module's public SG"
  from_port       = 0
  to_port         = 0
  protocol        = "-1"
  security_groups = [aws_security_group.public_ec2_sg.id]
}
```

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/main.tf`
- **Line:** `39`
```diff
# aws public security group 
resource "aws_security_group" "public_ec2_sg" {
  vpc_id = var.vpc_id
  name_prefix = "${var.public_instance_sg_name_tag}-sg"
  description = "Setting up rules for security group for public EC 2 instance"
  
  dynamic "ingress" {
    for_each = var.public_sg_ingress_rule
    content {
      description = ingress.value.description
      from_port = ingress.value.from_port
      to_port = ingress.value.to_port
      protocol = ingress.value.protocol
      cidr_blocks = lookup(ingress.value, "cidr_blocks", null)
      security_groups = lookup(ingress.value, "security_groups", null)
    }
  }

  dynamic "egress" {
    for_each = var.public_sg_egress_rule
    content {
      description = egress.value.description
      from_port = egress.value.from_port
      to_port = egress.value.to_port
      protocol = egress.value.protocol
      cidr_blocks = lookup(egress.value, "cidr_blocks", null)
      security_groups = lookup(egress.value, "security_groups", null)
    }
  }
}

#security group for private ec2 instance
resource "aws_security_group" "private_ec2_sg" {
  vpc_id = var.vpc_id
  name_prefix = "${var.private_instance_sg_name_tag}-sg"
  description = "Setting up rules for security group for private EC 2 instance"

  #core ingress rule for allowing traffic from this module's public security group
>>>   ingress = { <<<   # Line commented on
```
> @shujaxgrid feedback addressed. have to close this PR. Refer to https://github.com/Xgrid-Engineering/devops-internship-2025/pull/24 for changes.


---

## PR #21: [Sprint 4-PR 1: Foundational Module Structure & Public Instance SG](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/21)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-27T06:33:30Z
- **State:** closed

### Review Summaries:

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T08:21:15Z
> _No comment text_

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T08:23:29Z
> _No comment text_

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T08:23:40Z
> _No comment text_

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T08:23:49Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T10:42:16Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T10:42:34Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-29T07:52:09Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-29T07:54:43Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-29T09:57:15Z
> LGTM!

### Inline Comments with Code Context:

**Reviewer:** `shujaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/main.tf`
- **Line:** `None`
> Please fix a typo.

**Reviewer:** `shujaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/outputs.tf`
- **Line:** `None`
> dont see such resource in main.tf 'aws_security_group.this' it should be 'aws_security_group.public_ec2_sg.id' please validate

**Reviewer:** `shujaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/outputs.tf`
- **Line:** `None`
> same here.

**Reviewer:** `shujaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/outputs.tf`
- **Line:** `None`
> same here.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/main.tf`
- **Line:** `None`
> @shujaxgrid feedback addressed

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/ec2-module/outputs.tf`
- **Line:** `None`
> @shujaxgrid feedback addressed

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/main.tf`
- **Line:** `29`
```diff
# aws public security group 
resource "aws_security_group" "public_ec2_sg" {
  vpc_id = var.vpc_id
  name_prefix = "${var.public_instance_sg_name_tag}-sg"
  description = "Setting up rules for security group for public EC 2 instance"
  
  dynamic "ingress" {
    for_each = var.ingress_rule
    content {
      description = ingress.value.description
      from_port = ingress.value.from_port
      to_port = ingress.value.to_port
      protocol = ingress.value.protocol
      cidr_blocks = lookup(ingress.value, "cidr_blocks", null)
      security_groups = lookup(ingress.value, "security_groups", null)
    }
  }

  dynamic "egress" {
    for_each = var.egress_rule
    content {
      description = egress.value.description
      from_port = egress.value.from_port
      to_port = egress.value.to_port
      protocol = egress.value.protocol
      cidr_blocks = lookup(egress.value, "cidr_blocks", null)
      security_groups = lookup(egress.value, "security_groups", null)
    }
>>>   } <<<   # Line commented on
```
> Add tags to this resource.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/modules/ec2-module/main.tf`
- **Line:** `29`
```diff
# aws public security group 
resource "aws_security_group" "public_ec2_sg" {
  vpc_id = var.vpc_id
  name_prefix = "${var.public_instance_sg_name_tag}-sg"
  description = "Setting up rules for security group for public EC 2 instance"
  
  dynamic "ingress" {
    for_each = var.ingress_rule
    content {
      description = ingress.value.description
      from_port = ingress.value.from_port
      to_port = ingress.value.to_port
      protocol = ingress.value.protocol
      cidr_blocks = lookup(ingress.value, "cidr_blocks", null)
      security_groups = lookup(ingress.value, "security_groups", null)
    }
  }

  dynamic "egress" {
    for_each = var.egress_rule
    content {
      description = egress.value.description
      from_port = egress.value.from_port
      to_port = egress.value.to_port
      protocol = egress.value.protocol
      cidr_blocks = lookup(egress.value, "cidr_blocks", null)
      security_groups = lookup(egress.value, "security_groups", null)
    }
>>>   } <<<   # Line commented on
```
> @munemxgrid Implemented proper tagging in next PR. https://github.com/Xgrid-Engineering/devops-internship-2025/pull/27


---

## PR #20: [Changed to feature branch workflow from forking and therefore changes being requested to Merge](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-23T07:45:10Z
- **State:** closed

### Review Summaries:

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-23T11:00:32Z
> gave some feedback, please ping again once you've pushed new commits :)

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T08:11:09Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:42:53Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:43:13Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:43:23Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:44:08Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:44:44Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:45:02Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:45:27Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:45:56Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-26T11:46:10Z
> _No comment text_

**Reviewer:** `FarsanGul`
- **State:** `APPROVED`
- **Submitted:** 2025-05-27T06:08:30Z
> LGTM

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T10:45:19Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-27T11:03:27Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-27T11:12:08Z
> LGTM!

**Reviewer:** `huzaifaxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-29T06:50:25Z
> LGTM!

**Reviewer:** `Moiz-0786`
- **State:** `APPROVED`
- **Submitted:** 2025-05-29T07:17:40Z
> LGTM

### Inline Comments with Code Context:

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/test-vpc.tf`
- **Line:** `None`
> lets define it in a variable

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/test-vpc.tf`
- **Line:** `None`
> lets define it in a variable

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/test-vpc.tf`
- **Line:** `None`
> Lets move it in examples directory
examples/vpc-test/main.tf,var.tf,provider.tf

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/README.md`
- **Line:** `19`
```diff
# Terraform VPC Module — Sprint 03

This module provisions a reusable VPC on AWS with:

- 2 Public Subnets
- 2 Private Subnets
- Internet Gateway
- Route Table for Public Subnets

## Usage

Option 1: Direct inline usage

module "vpc" {
```
> ```suggestion
```.tf
module "vpc" {
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/README.md`
- **Line:** `46`
```diff
# Terraform VPC Module — Sprint 03

This module provisions a reusable VPC on AWS with:

- 2 Public Subnets
- 2 Private Subnets
- Internet Gateway
- Route Table for Public Subnets

## Usage

Option 1: Direct inline usage

module "vpc" {
  source = "./vpc-module"

  aws_region              = "us-east-1"
  vpc_cidr                = "10.0.0.0/16"
  availability_zones      = ["us-east-1a", "us-east-1b"]
  public_subnets          = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets         = ["10.0.3.0/24", "10.0.4.0/24"]
  enable_dns_support      = true
  map_public_ip_on_launch = true

  vpc_name                     = "main-vpc"
  igw_name                     = "main-igw"
  public_subnet_name_prefix   = "public-subnet"
  private_subnet_name_prefix  = "private-subnet"
  public_route_table_name     = "public-rt"

  tags = {
    app         = "Terraform"
    created-by  = "Terraform"
    environment = "DevOpsInternship-2025"
    name        = "Muhammad Usman Safder"
    owner       = "usman.safder@xgrid.co"
    creator     = "usman.safder@xgrid.co"
    project     = "VPC Provisioning - Sprint-03"
    team        = "Firebirds"
  }
}

```
> ```suggestion
```.tf
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> just a suggestion

you can also use something like this in env.tf and lateron refer tags as an output


```env.tf
module "main_env" {
  source    = "cloudposse/label/null"
  version   = "0.25.0"
  namespace = lookup(var.env_vars, "namespace", "xgrid")
  stage     = lookup(var.env_vars, "stage", "dev")
  name      = local.module_name
  delimiter = lookup(var.env_vars, "delimiter", "-")

  tags = {
    "TF-Module" = "s208"
  }
}
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> you can refer it later on like

```.tf
 tags = merge(module.main_env.tags, {
 ```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `38`
```diff
# Create the main VPC with DNS support enabled
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = var.enable_dns_support

  tags = merge(var.tags, {
    Name = var.vpc_name
  })
}

# Attach an Internet Gateway (IGW) to the VPC
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = merge(var.tags, {
    Name = var.igw_name
  })
}

# Create public subnets across availability zones with auto-assign public IP
resource "aws_subnet" "public" {
  for_each = { for idx, cidr in var.public_subnets : idx => cidr }

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value
  availability_zone       = var.availability_zones[each.key]
  map_public_ip_on_launch = var.map_public_ip_on_launch

  tags = merge(var.tags, {
    Name = "${var.public_subnet_name_prefix}-${each.key}"
  })
}

# Create private subnets across availability zones (no public IPs assigned)
resource "aws_subnet" "private" {
  for_each = { for idx, cidr in var.private_subnets : idx => cidr }
```
> ```suggestion
  for_each = var.private_subnets
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `42`
```diff
# Create the main VPC with DNS support enabled
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = var.enable_dns_support

  tags = merge(var.tags, {
    Name = var.vpc_name
  })
}

# Attach an Internet Gateway (IGW) to the VPC
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = merge(var.tags, {
    Name = var.igw_name
  })
}

# Create public subnets across availability zones with auto-assign public IP
resource "aws_subnet" "public" {
  for_each = { for idx, cidr in var.public_subnets : idx => cidr }

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value
  availability_zone       = var.availability_zones[each.key]
  map_public_ip_on_launch = var.map_public_ip_on_launch

  tags = merge(var.tags, {
    Name = "${var.public_subnet_name_prefix}-${each.key}"
  })
}

# Create private subnets across availability zones (no public IPs assigned)
resource "aws_subnet" "private" {
  for_each = { for idx, cidr in var.private_subnets : idx => cidr }

  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value
  availability_zone = var.availability_zones[each.key]
```
> this is confusion, please re-check that

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> same suggestion to use module_env like this 


```.tf
 tags = merge(module.main_env.tags, {
```

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/outputs.tf`
- **Line:** `1`
```diff
>>> output "vpc_id" { <<<   # Line commented on
```
> good strategy is to add description in output block as well that explains what this output does

**Reviewer:** `muhammadasgharaliqureshixgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/versions.tf`
- **Line:** `None`
> would recommend to rename it as providers.tf

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `42`
```diff
# Create the main VPC with DNS support enabled
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = var.enable_dns_support

  tags = merge(var.tags, {
    Name = var.vpc_name
  })
}

# Attach an Internet Gateway (IGW) to the VPC
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = merge(var.tags, {
    Name = var.igw_name
  })
}

# Create public subnets across availability zones with auto-assign public IP
resource "aws_subnet" "public" {
  for_each = { for idx, cidr in var.public_subnets : idx => cidr }

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value
  availability_zone       = var.availability_zones[each.key]
  map_public_ip_on_launch = var.map_public_ip_on_launch

  tags = merge(var.tags, {
    Name = "${var.public_subnet_name_prefix}-${each.key}"
  })
}

# Create private subnets across availability zones (no public IPs assigned)
resource "aws_subnet" "private" {
  for_each = { for idx, cidr in var.private_subnets : idx => cidr }

  vpc_id            = aws_vpc.main.id
  cidr_block        = each.value
  availability_zone = var.availability_zones[each.key]
```
> Thanks for helping me understand it better through your comment!
You're right that the current implementation uses index-based access to align CIDR blocks with availability zones. The loop:
```hcl
for idx, cidr in var.public_subnets : idx => cidr
```
produces a map like:
```hcl
{
  0 = "10.0.1.0/24"
  1 = "10.0.2.0/24"
}
```
Then inside the for_each, we use:
```hcl
availability_zone = var.availability_zones[each.key]
```
This works because each.key corresponds to the index (0, 1, ..) of both the subnet and AZ lists, considering they're ordered the same way.
That said, if you'd prefer a more explicit and cleaner mapping, I can replace this logic with zipmap(var.availability_zones, var.public_subnets) which would directly pair each AZ with its CIDR — removing the dependency on list order and making the code easier to read.
Please let me know if you’d prefer that update, happy to make the change!

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/versions.tf`
- **Line:** `None`
> Addressed in https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/outputs.tf`
- **Line:** `1`
```diff
>>> output "vpc_id" { <<<   # Line commented on
```
> Addressed in https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f . kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f kindly review

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `38`
```diff
# Create the main VPC with DNS support enabled
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = var.enable_dns_support

  tags = merge(var.tags, {
    Name = var.vpc_name
  })
}

# Attach an Internet Gateway (IGW) to the VPC
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = merge(var.tags, {
    Name = var.igw_name
  })
}

# Create public subnets across availability zones with auto-assign public IP
resource "aws_subnet" "public" {
  for_each = { for idx, cidr in var.public_subnets : idx => cidr }

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value
  availability_zone       = var.availability_zones[each.key]
  map_public_ip_on_launch = var.map_public_ip_on_launch

  tags = merge(var.tags, {
    Name = "${var.public_subnet_name_prefix}-${each.key}"
  })
}

# Create private subnets across availability zones (no public IPs assigned)
resource "aws_subnet" "private" {
  for_each = { for idx, cidr in var.private_subnets : idx => cidr }
```
> Addressed https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20#discussion_r2106796720 in here

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Addressed in https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f addressed

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/README.md`
- **Line:** `46`
```diff
# Terraform VPC Module — Sprint 03

This module provisions a reusable VPC on AWS with:

- 2 Public Subnets
- 2 Private Subnets
- Internet Gateway
- Route Table for Public Subnets

## Usage

Option 1: Direct inline usage

module "vpc" {
  source = "./vpc-module"

  aws_region              = "us-east-1"
  vpc_cidr                = "10.0.0.0/16"
  availability_zones      = ["us-east-1a", "us-east-1b"]
  public_subnets          = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets         = ["10.0.3.0/24", "10.0.4.0/24"]
  enable_dns_support      = true
  map_public_ip_on_launch = true

  vpc_name                     = "main-vpc"
  igw_name                     = "main-igw"
  public_subnet_name_prefix   = "public-subnet"
  private_subnet_name_prefix  = "private-subnet"
  public_route_table_name     = "public-rt"

  tags = {
    app         = "Terraform"
    created-by  = "Terraform"
    environment = "DevOpsInternship-2025"
    name        = "Muhammad Usman Safder"
    owner       = "usman.safder@xgrid.co"
    creator     = "usman.safder@xgrid.co"
    project     = "VPC Provisioning - Sprint-03"
    team        = "Firebirds"
  }
}

```
> Addressed in https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f. Thankyou

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/test-vpc.tf`
- **Line:** `None`
> Addressed in https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/test-vpc.tf`
- **Line:** `None`
> Addressed in https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/7309e55c4f1b10022ca6115fe9b6fd36e0f71d3f

**Reviewer:** `munemxgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Create variable instead of hardcoding it.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/20/commits/b4e9bfb3609e281de6207dac84b4e389b0b85751. Kindly review


---

## PR #19: [Sprint 3 Task: VPC Infrastructure as Code Using Terraform](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/19)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-22T12:43:08Z
- **State:** closed

### Review Summaries:

**Reviewer:** `Usman762`
- **State:** `APPROVED`
- **Submitted:** 2025-05-22T13:07:30Z
> LGTM , already reviewed in https://github.com/Xgrid-Engineering/devops-internship-2025/pull/18

_No inline comments._


---

## PR #18: [Sprint 3 Task: VPC Infrastructure as Code Using Terraform](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/18)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-15T09:51:16Z
- **State:** closed

### Review Summaries:

**Reviewer:** `FarsanGul`
- **State:** `APPROVED`
- **Submitted:** 2025-05-15T10:45:25Z
> LGTM

**Reviewer:** `munemxgrid`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-15T10:49:18Z
> Left some feedback.

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T12:37:56Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-16T05:35:18Z
> LGTM!

**Reviewer:** `Moiz-0786`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-16T06:59:30Z
> left some comments.

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-16T07:24:38Z
> _No comment text_

**Reviewer:** `Moiz-0786`
- **State:** `APPROVED`
- **Submitted:** 2025-05-19T07:27:15Z
> LGTM

**Reviewer:** `Usman762`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-21T06:45:43Z
> @huzaifaxgrid  please look into the changes

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-21T07:47:32Z
> _No comment text_

**Reviewer:** `Usman762`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-22T11:21:45Z
> _No comment text_

### Inline Comments with Code Context:

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> Create variable for these values.

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> Create variable for this value.

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> Create variable for this too.

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `61`
```diff
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "${var.name_prefix}-vpc"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.name_prefix}-igw"
  }
}

resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.public_subnet_cidrs[count.index]
  map_public_ip_on_launch = true
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "${var.name_prefix}-public-${count.index}"
  }
}

resource "aws_subnet" "private" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "${var.name_prefix}-private-${count.index}"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.name_prefix}-public-rt"
  }
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
```
> Don't use hardcoded values.

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> Create variable for this too.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `61`
```diff
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "${var.name_prefix}-vpc"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.name_prefix}-igw"
  }
}

resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.public_subnet_cidrs[count.index]
  map_public_ip_on_launch = true
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "${var.name_prefix}-public-${count.index}"
  }
}

resource "aws_subnet" "private" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "${var.name_prefix}-private-${count.index}"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.name_prefix}-public-rt"
  }
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
```
> @munemxgrid feedback addressed

**Reviewer:** `Moiz-0786`
- **File:** `submissions/HuzaifaAwan/vpc-module/README.md`
- **Line:** `None`
> Why is such a large range configured for the VPC? Given the architecture and use case, do you actually need such a broad IP range?

**Reviewer:** `Moiz-0786`
- **File:** `submissions/HuzaifaAwan/vpc-module/README.md`
- **Line:** `None`
> why these details are mentioned in the readme file.

**Reviewer:** `Moiz-0786`
- **File:** `submissions/HuzaifaAwan/vpc-module/variables.tf`
- **Line:** `4`
```diff
variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
>>> } <<<   # Line commented on
```
> where is this value declared? I can't see a .gitignore file neither a default value declared.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/variables.tf`
- **Line:** `4`
```diff
variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
>>> } <<<   # Line commented on
```
> @Moiz-0786 feedbacks addressed

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> use variable as `public_subnet_count` instead of `subnet_count` as I can see you are using the same variable for private subnet as well, in that way I will have the freedom to create private and public subnets independently

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> as you are using `subnet_count` variable to create the number of the subnets then using `public_subnet_cidrs`  as well so if there is a diff between these two values let's say that you provide subnet count as 3 and only provide 2 public_subnet_cidrs then this can lead to error a better way to do this would be instead of using this `subnet_count` variable you can use `public_subnet_cidrs` and create the num of subnets based on the provided cidrs.

Hint: Look into `for_each` for this.

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> same remarks as mentioned above for `public_subnet_cidr`

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> use "0.0.0.0/0" as default and you can hardcode this values as it is explicitly saying that this route is for internet access.

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> look into for_each if you change the above approach in public subnet then you will also be updating this.

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/variables.tf`
- **Line:** `None`
> remove this variable.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `None`
> @Usman762 feedbacks addressed

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/variables.tf`
- **Line:** `None`
> description should be private subnet configuration

**Reviewer:** `Usman762`
- **File:** `submissions/HuzaifaAwan/vpc-module/main.tf`
- **Line:** `61`
```diff
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "${var.name_prefix}-vpc"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.name_prefix}-igw"
  }
}

resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.public_subnet_cidrs[count.index]
  map_public_ip_on_launch = true
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "${var.name_prefix}-public-${count.index}"
  }
}

resource "aws_subnet" "private" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "${var.name_prefix}-private-${count.index}"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "${var.name_prefix}-public-rt"
  }
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
```
> This is fine @munemxgrid as the name suggest it is internet_access so no need to add a variable here.


---

## PR #17: [enhance:  VPC module with pre-commit, inline docs, and test-vpc.tf validation](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/17)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-15T09:40:46Z
- **State:** closed

### Review Summaries:

**Reviewer:** `munemxgrid`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-15T10:46:12Z
> Left some feedback. Kindly have a look.

**Reviewer:** `FarsanGul`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T10:55:38Z
> Resolve comments by munem

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T17:55:14Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T17:55:36Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T17:55:43Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-16T05:34:06Z
> LGTM!

**Reviewer:** `Usman762`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-21T07:10:01Z
> _No comment text_

**Reviewer:** `Usman762`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-22T09:57:10Z
> @usmansafdarktk please do the changes.

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-22T11:11:29Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-22T11:11:51Z
> _No comment text_

**Reviewer:** `Usman762`
- **State:** `APPROVED`
- **Submitted:** 2025-05-22T11:17:05Z
> lgtm

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-22T11:19:41Z
> _No comment text_

**Reviewer:** `Usman762`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-23T09:35:25Z
> Please make the required changes

### Inline Comments with Code Context:

**Reviewer:** `munemxgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Create a variable for this value.

**Reviewer:** `munemxgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Create a variable for this too.

**Reviewer:** `munemxgrid`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Create variable for this too.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> The requested changes have been revised in commit [e054e4e](https://github.com/usmansafdarktk/devops-internship-2025/commit/e054e4e).
All hardcoded values, including region, enable_dns_support, and map_public_ip_on_launch — have now been parameterized via variables.

Kindly review at your convenience. thank you.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Revised in commit [e054e4e](https://github.com/usmansafdarktk/devops-internship-2025/commit/e054e4e).

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Revised in commit [e054e4e](https://github.com/usmansafdarktk/devops-internship-2025/commit/e054e4e).

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/providers.tf`
- **Line:** `None`
> As this is a module so you don't put the backend configuration in providers.tf file

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/providers.tf`
- **Line:** `None`
> you backend configuration will be placed in the root module from where you will call this module.

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/infra/outputs.tf`
- **Line:** `None`
> description should be added for an output.

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/infra/providers.tf`
- **Line:** `None`
> don't hardcode this.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/infra/outputs.tf`
- **Line:** `None`
> I wanted to provide some context regarding the recent commit. While attempting to recover the previously deleted outputs.tf and providers.tf files, I inadvertently restored earlier versions that contained outdated configurations, including hardcoded values and missing descriptions. This oversight led to the issues that was encountered.
After addressing these concerns and ensuring all configurations align with our current standards, I've committed the corrected versions. I believe this resolves the problems.
Please review the latest changes in the commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/17/commits/fe8cbba5f36cfb5fff8a4aea151a1aaf5831e3eb and let me know if further adjustments are necessary. Thank you for your understanding and support.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/infra/providers.tf`
- **Line:** `None`
> Addressed. Kindly check

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/providers.tf`
- **Line:** `None`
> Upon reviewing my setup, I realized that I had inadvertently included the backend configuration within the providers.tf file of the infra module for S3 bucket provisioning. , I have moved the backend configuration to the root module as per best practices.
Regarding the vpc-module, I understand that provider configurations should also be defined in the root module and passed down to child modules. I will review the vpc-module to ensure it adheres to this practice and make necessary adjustments. Right now I am trying to understand as to when this provider.tf was created for vpc module as I cannot find it right now. 
Kindly do let me know if there are any more suggestions.

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `3`
```diff

# Specify AWS provider and region
>>> provider "aws" { <<<   # Line commented on
```
> This should not be added in the module. You do not add provider in the module.
But you still create a provider.tf in which you will mention the provider you are using.  see the below link as example
https://github.com/terraform-aws-modules/terraform-aws-ec2-instance/blob/master/versions.tf

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/variables.tf`
- **Line:** `82`
```diff
variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "enable_dns_support" {
  description = "Enable DNS support in VPC"
  type        = bool
  default     = true
}

variable "public_subnets" {
  description = "List of public subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnets" {
  description = "List of private subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.3.0/24", "10.0.4.0/24"]
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "map_public_ip_on_launch" {
  description = "Enable automatic public IP assignment for public subnets"
  type        = bool
  default     = true
}

variable "vpc_name" {
  description = "Name tag for the VPC"
  type        = string
  default     = "main-vpc"
}

variable "igw_name" {
  description = "Name tag for the Internet Gateway"
  type        = string
  default     = "main-igw"
}

variable "public_subnet_name_prefix" {
  description = "Prefix for public subnet name tags"
  type        = string
  default     = "public-subnet"
}

variable "private_subnet_name_prefix" {
  description = "Prefix for private subnet name tags"
  type        = string
  default     = "private-subnet"
}

variable "public_route_table_name" {
  description = "Name tag for the public route table"
  type        = string
  default     = "public-rt"
}

variable "tags" {
  description = "Standard Xgrid tagging convention"
  type        = map(string)
  default = {
    environment = "DevOps Internship 2025"
    name        = "Usman Safder"
    project     = "VPC setup - sprint-03"
    creator     = "usman.safder@xgrid.co"
    team        = "Firebirds"
  }
}
>>>  <<<   # Line commented on
```
> remove extra lines


---

## PR #16: [feat: Add reusable VPC module with tagging for Sprint 3](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/16)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-15T07:43:21Z
- **State:** closed

### Review Summaries:

**Reviewer:** `FarsanGul`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T10:52:35Z
> Suggested couple of changes

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T16:23:47Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T16:24:05Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-16T05:36:29Z
> LGTM!

**Reviewer:** `FarsanGul`
- **State:** `APPROVED`
- **Submitted:** 2025-05-16T06:51:48Z
> LGTM

**Reviewer:** `Moiz-0786`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-16T07:07:23Z
> please adress the comments.

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-16T07:32:41Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-16T07:33:16Z
> _No comment text_

**Reviewer:** `Usman762`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-21T07:03:12Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-22T08:01:20Z
> _No comment text_

**Reviewer:** `Usman762`
- **State:** `APPROVED`
- **Submitted:** 2025-05-22T10:02:16Z
> LGTM

### Inline Comments with Code Context:

**Reviewer:** `FarsanGul`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Make sure to pass the variable name through variable file.

**Reviewer:** `FarsanGul`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Same as above

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> I've addressed the review feedback by passing  values (including region, DNS support, subnet IP assignment, and all Name tags) via variables in commit [ae4b7d6](https://github.com/usmansafdarktk/devops-internship-2025/commit/ae4b7d6).

Thank you for the valuable suggestions — kindly review at your convenience.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> Addressed in commit [ae4b7d6](https://github.com/usmansafdarktk/devops-internship-2025/commit/ae4b7d6).

**Reviewer:** `Moiz-0786`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/README.md`
- **Line:** `None`
> The Usage section should provide a clear explanation of how this module will be utilized in practice. Currently, you have only declared the module without detailing its implementation or practical application.

**Reviewer:** `Moiz-0786`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> can you please explain what this function is doing?

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> This Function allows to dynamically create one public subnet per AZ, use the index (each.key) to select the correct CIDR from var.public_subnets and use the AZ value (each.value) to place each subnet in the appropriate zone.

I've also added comments in code for clarification before this Function. Addressed  in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/16/commits/bc98a8d1692fae11699c04e5f238ac43902a16cc


**EDITED:**  I have adapted the following according to the below suggestion and used CIDR as the primary for creating subnets.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/README.md`
- **Line:** `None`
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/commit/bc98a8d1692fae11699c04e5f238ac43902a16cc . Kindly Review

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> @usmansafdarktk I would suggest instead of taking `availbility_zone` as the primary key to create the no of public subnet and private subnet use their own `public_subnet_cidr` list because this will allow you to create public and private subnets independently. Do the same in private subnet as well.

**Reviewer:** `Usman762`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> When you will use `public_subent` in the for_each you won't be needing `tonumber()` function. do look into that.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/vpc-module/main.tf`
- **Line:** `None`
> I have addressed the feedback in the commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/16/commits/3555006b5ec2e93b26aa7bf0cd1542222fd4e7ac  by using CIDR lists as the primary source for subnet creation. Also removed the unnecessary type conversion.


---

## PR #15: [Refactor: Add .gitignore and Apply Standard Xgrid Tagging to S3 Terraform Resource](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/15)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-14T20:51:31Z
- **State:** closed

### Review Summaries:

**Reviewer:** `FarsanGul`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T10:49:23Z
> Suggested a change

**Reviewer:** `abdul-haseeb-HSB`
- **State:** `APPROVED`
- **Submitted:** 2025-05-15T12:31:04Z
> _No comment text_

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T13:27:00Z
> _No comment text_

**Reviewer:** `FarsanGul`
- **State:** `APPROVED`
- **Submitted:** 2025-05-16T06:43:15Z
> LGTM

**Reviewer:** `Moiz-0786`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-16T07:02:03Z
> please fix the tags.

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-16T07:15:34Z
> _No comment text_

**Reviewer:** `Moiz-0786`
- **State:** `APPROVED`
- **Submitted:** 2025-05-19T07:24:21Z
> LGTM

### Inline Comments with Code Context:

**Reviewer:** `FarsanGul`
- **File:** `submissions/muhammadUsmanSafder/infra/main.tf`
- **Line:** `None`
> Make sure you pass the name through variable file.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/infra/main.tf`
- **Line:** `None`
> ✅ The requested change to pass the bucket name via variable has been implemented in commit [197ecdf](https://github.com/usmansafdarktk/devops-internship-2025/commit/197ecdf). Thank you for the valuable feedback — kindly review when convenient.

**Reviewer:** `Moiz-0786`
- **File:** `submissions/muhammadUsmanSafder/infra/variables.tf`
- **Line:** `1`
> The Owner tag should include your email address, as you are the designated owner of the bucket.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/muhammadUsmanSafder/infra/variables.tf`
- **Line:** `1`
> Addressed in commit https://github.com/Xgrid-Engineering/devops-internship-2025/pull/15/commits/615e8d22067a432455e4aab3fa6e7c2fca05e1cb. Kindly review.


---

## PR #14: [Add README.md for Sprint-02 in infra folder](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/14)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-14T12:16:15Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #13: [Merge pull request #12 from Xgrid-Engineering/main](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/13)

- **Author:** `shujaxgrid`
- **Created at:** 2025-05-14T11:55:57Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #12: [syncing](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/12)

- **Author:** `shujaxgrid`
- **Created at:** 2025-05-14T11:55:03Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #11: [Dev](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/11)

- **Author:** `shujaxgrid`
- **Created at:** 2025-05-14T11:54:10Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #10: [Adding codeonwers](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/10)

- **Author:** `shujaxgrid`
- **Created at:** 2025-05-14T11:23:27Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #9: [syncronizing dev with main](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/9)

- **Author:** `shujaxgrid`
- **Created at:** 2025-05-14T10:28:07Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #8: [syncronizing main with dev](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/8)

- **Author:** `shujaxgrid`
- **Created at:** 2025-05-14T10:26:25Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #7: [Sprint 2 - AWS IAM Setup and First S3 Bucket Provisioning Using Terraform](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/7)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-14T10:09:29Z
- **State:** closed

### Review Summaries:

**Reviewer:** `munemxgrid`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-14T12:18:16Z
> _No comment text_

**Reviewer:** `AbuBakkarBinAkmal`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-14T12:27:54Z
> Left some suggestions, please address and re-request review. Thanks

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-14T13:05:51Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-14T13:06:23Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-15T10:54:33Z
> @huzaifaxgrid Create variables instead of hardcoding values.

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-15T13:18:02Z
> LGTM!

**Reviewer:** `Moiz-0786`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-16T06:49:27Z
> left some comments

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-16T07:25:01Z
> _No comment text_

**Reviewer:** `Moiz-0786`
- **State:** `APPROVED`
- **Submitted:** 2025-05-16T09:24:50Z
> LGTM

**Reviewer:** `usmansafdarktk`
- **State:** `APPROVED`
- **Submitted:** 2025-05-19T06:59:47Z
> Looks Good to Me!

### Inline Comments with Code Context:

**Reviewer:** `AbuBakkarBinAkmal`
- **File:** `submissions/HuzaifaAwan/infra/.terraform/terraform.tfstate`
- **Line:** `None`
> @huzaifaxgrid tfstate files should not be committed to repos, please add this to your gitignore file

**Reviewer:** `AbuBakkarBinAkmal`
- **File:** `submissions/HuzaifaAwan/infra/.terraform/providers/registry.terraform.io/hashicorp/aws/5.97.0/windows_386/LICENSE.txt`
- **Line:** `None`
> Is this file needed?

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/infra/.terraform/terraform.tfstate`
- **Line:** `1`
> The terraform.tfstate file has been committed to GitHub. This is a security risk since state files contain sensitive information including resource IDs and potentially credentials. You should remove this file from version control. Add it to your .gitignore file to prevent future commits.

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/infra/main.tf`
- **Line:** `1`
> Your repository is missing a .gitignore file.

**Reviewer:** `AbuBakkarBinAkmal`
- **File:** `submissions/HuzaifaAwan/infra/main.tf`
- **Line:** `4`
```diff
resource "aws_s3_bucket" "first_bucket" {
  bucket = "huzaifa-first-bucket"

>>>   tags = { <<<   # Line commented on
```
> Let's make sure to follow proper tagging conventions. i.e.

owner
project
safe_to_delete

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/infra/.terraform/terraform.tfstate`
- **Line:** `1`
> feedback addressed.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/infra/.terraform/terraform.tfstate`
- **Line:** `None`
> feedbacks addressed

**Reviewer:** `Moiz-0786`
- **File:** `submissions/HuzaifaAwan/infra/.gitignore`
- **Line:** `None`
> Add EOF.
```suggestion
terraform.tfvars

```

**Reviewer:** `Moiz-0786`
- **File:** `submissions/HuzaifaAwan/infra/providers.tf`
- **Line:** `None`
> why not using the region varibale when you have already declared one.

**Reviewer:** `Moiz-0786`
- **File:** `submissions/HuzaifaAwan/infra/providers.tf`
- **Line:** `None`
> use variables, don't hardcode.

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/infra/providers.tf`
- **Line:** `None`
> @Moiz-0786 feedbacks addressed


---

## PR #6: [Added infra setup for remote backend and S3](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/6)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-14T09:29:37Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #5: [Merge pull request #4 from Xgrid-Engineering/dev](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/5)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-13T17:59:45Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #4: [feat: Add Sprint-01 submission (Usman Safder)](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/4)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-13T17:54:42Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #3: [added sprint 2](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/3)

- **Author:** `shujaxgrid`
- **Created at:** 2025-05-13T11:41:11Z
- **State:** closed

_No review summaries._

_No inline comments._


---

## PR #2: [Task 1: Add Introduction and understanding github](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/2)

- **Author:** `huzaifaxgrid`
- **Created at:** 2025-05-13T06:14:38Z
- **State:** closed

### Review Summaries:

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-13T06:55:50Z
> @huzaifaxgrid please make below changes:

- Update the title of the PR. It should be descriptive enough to understand what we are trying to achieve here. Putting up the file name is never recommended. Also add the tasks number/title to point it.
- README.md should have details of the task, what was assigned here.

**Reviewer:** `abdul-haseeb-HSB`
- **State:** `APPROVED`
- **Submitted:** 2025-05-13T09:18:19Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `CHANGES_REQUESTED`
- **Submitted:** 2025-05-13T09:20:02Z
> _No comment text_

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-13T09:27:13Z
> _No comment text_

**Reviewer:** `huzaifaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-13T09:28:15Z
> _No comment text_

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-13T11:42:17Z
> Your branch is behind when compared to dev branch. Please take a latest pull and then merge after solving the conflicts.

### Inline Comments with Code Context:

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/Sprint1/Huzaifa_about_me.txt`
- **Line:** `None`
> Consider adding line breaks between paragraphs to improve readability.

**Reviewer:** `munemxgrid`
- **File:** `submissions/HuzaifaAwan/Sprint1/README.md`
- **Line:** `None`
> The file path mentioned in "How to Run" section doesn't match the actual file path:

Current: submissions/Huzaifa_about_me.txt
Should be: submissions/HuzaifaAwan/Sprint1/Huzaifa_about_me.txt

**Reviewer:** `huzaifaxgrid`
- **File:** `submissions/HuzaifaAwan/Sprint1/README.md`
- **Line:** `None`
> @munemxgrid feedback addressed


---

## PR #1: [Add Sprint-01 task-01 submission: about me and documentation](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/1)

- **Author:** `usmansafdarktk`
- **Created at:** 2025-05-12T20:10:07Z
- **State:** closed

### Review Summaries:

**Reviewer:** `shujaxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-13T06:58:30Z
> LGTM!

**Reviewer:** `abdul-haseeb-HSB`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-13T08:04:36Z
> Minor Suggestion

**Reviewer:** `munemxgrid`
- **State:** `APPROVED`
- **Submitted:** 2025-05-13T08:41:36Z
> LGTM!

**Reviewer:** `usmansafdarktk`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-13T08:47:32Z
> _No comment text_

**Reviewer:** `abdul-haseeb-HSB`
- **State:** `APPROVED`
- **Submitted:** 2025-05-13T08:48:29Z
> _No comment text_

**Reviewer:** `shujaxgrid`
- **State:** `COMMENTED`
- **Submitted:** 2025-05-13T11:42:35Z
> Your branch is behind when compared to dev branch. Please take a latest pull and then merge after solving the conflicts.

### Inline Comments with Code Context:

**Reviewer:** `abdul-haseeb-HSB`
- **File:** `submissions/Muhammad Usman Safder/Sprint-01/README.md`
- **Line:** `None`
> It’s recommended to avoid using spaces in folder names, as they require manual escaping(in bash, power shell or scripting), which can be error-prone. Instead, consider using naming conventions like camelCase, kebab-case, or snake_case. These formats are safer, cleaner, and offer better compatibility across tools, scripts, and platforms.

**Reviewer:** `usmansafdarktk`
- **File:** `submissions/Muhammad Usman Safder/Sprint-01/README.md`
- **Line:** `None`
> Thank you for pointing it out. Folder is renamed from "Muhammad Usman Safder" → "muhammadUsmanSafder" and README updated as suggested.  
🔗 Fixed in commit [7ecd690](https://github.com/Xgrid-Engineering/devops-internship-2025/pull/1/commits/7ecd69089eee9196c4f9aa4e9f078381380184a5). Let me know if anything else needs adjustment.

