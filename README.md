# Description
This repository contains a GenAI enabled pdf_summarization_app.py microservice that allows users to summarize a PDF document using natural language processing. 
# Installation
1. Clone the Repository:

git clone https://github.com/your-username/AI-PDF-Summarizer.git

cd AI-PDF-Summarizer

# To upload a Docker image to Amazon Elastic Container Registry (ECR) using AWS CloudFormation, you'll need to follow these steps:

Create an ECR Repository using CloudFormation: Write a CloudFormation Template (CFT) to create an ECR repository.

Build and Tag the Docker Image: Use Docker CLI commands to build and tag the Docker image.

Authenticate Docker to ECR: Get the Docker authentication token for ECR.

Push the Docker Image to ECR: Push the Docker image to the ECR repository

1. Build the Docker Image

Navigate to the directory containing the Dockerfile and pdf_summarization_app.py, and build the Docker image using the following command:

docker build -t pdf-summarizer 

2. Deploy the CloudFormation stack ecr-template.yml to create the ECR repository

   aws cloudformation create-stack --stack-name pdf-summarizer-stack --template-body file://ecr-template.yml --capabilities CAPABILITY_NAMED_IAM
   
3. Push the Docker Image to ECR
4. 
   docker push $aws_account_id.dkr.ecr.$region.amazonaws.com/$repository_name:latest
   
# To deploy your Docker image to an ECS Cluster using AWS CloudFormation (pdf-summarizer-cluster.yml),

ECS Cluster creation.

ECS Task Definition to specify the Docker image.

ECS Service with Auto Scaling.

Auto Scaling Policies triggered by CPU and memory utilization metrics.

Load Balancer setup for routing traffic to the ECS tasks.

# Key Components of the Template:
ECS Cluster: Creates an ECS cluster named pdf-summarizer-cluster.

Task Definition: Defines the ECS task to run the Docker container from your ECR repository.

Load Balancer: Creates an Application Load Balancer (ALB) to route traffic to ECS tasks.

ECS Service: Deploys the task in an ECS service that starts with 3 containers and supports scaling.

Auto Scaling Policies:

CPU Scaling: Automatically scales the service when CPU utilization exceeds 50%.

Memory Scaling: Automatically scales the service when memory utilization exceeds 50%.

IAM Role: Defines an IAM role for allowing ECS and Auto Scaling to interact.

CloudWatch Logs: Logs ECS container output to CloudWatch Logs for monitoring and debugging.

# Deploy the CloudFormation stack (ecs-scaling-template.yml)

aws cloudformation create-stack --stack-name ecs-pdf-summarizer --template-body file://ecs-scaling-template.yml --capabilities CAPABILITY_NAMED_IAM

# Implement CI/CD pipeline to automate the deployment and scaling process in AWS 

## Step 1: Create and Push Docker Image to ECR

1.1 Create an ECR Repository

If you haven't already created the ECR repository using the CloudFormation template, do so first, as described earlier.

1.2 Update buildspec.yml

Create a buildspec.yml file in the root of your project. This file defines the build process for CodeBuild:

This file buildspec.yml does the following:

Logs into ECR.

Builds the Docker image.

Tags and pushes the image to ECR.

Creates an imagedefinitions.json file, which is used by CodeDeploy to update the ECS service.

## Step 2: Set Up the CI/CD Pipeline

2.1 Create a CodePipeline Using CloudFormation (pipeline-template.yml)

Key Components of the Pipeline:

Source Stage:

Uses GitHub as the source repository.

Triggers the pipeline when changes are pushed to the specified branch.

Build Stage:

Uses AWS CodeBuild to build the Docker image, push it to ECR, and generate imagedefinitions.json.

Deploy Stage:

Uses AWS CodeDeploy to deploy the new image to ECS, updating the ECS service.

IAM Roles:

Roles for CodePipeline, CodeBuild, and CodeDeploy to enable the necessary actions.

S3 Artifact Store:

An S3 bucket to store pipeline artifacts (e.g., build outputs).

## Step 3: Deploy the Pipeline (pipeline-template.yml)

aws cloudformation create-stack --stack-name pdf-summarizer-pipeline --template-body file://pipeline-template.yml --capabilities CAPABILITY_NAMED_IAM

## Step 4: Trigger the Pipeline

To trigger the pipeline, push a new commit to the GitHub repository specified in the pipeline's source stage

 # Test Strategy for GenAI-Powered Microservice

 UnitTestCase1.py
 
 IntegrationTestCase1.py
 
 Performance Tests
 
 Tools: Use locust or Apache JMeter for load testing.
 
 Security Testing
 
 bandit -r your_microservice/

 CI/CD Pipeline Overview:

Source: Triggered by code commits to the repository.

Build: Runs unit tests and security scans.

Integration Tests: Deploys to a staging environment and runs integration tests.

Performance Tests: Runs performance tests against the staging environment.

Deploy: If all tests pass, deploy to production with CodeDeploy.

Automated Deployment:

Ensure that the CI/CD pipeline automatically scales the ECS service based on predefined metrics (e.g., CPU, memory).

Security Best Practices:

Enforce the use of HTTPS, API keys, or OAuth for API security.

Use IAM roles with the least privilege principle for accessing AWS resources.

Regularly update dependencies and run vulnerability scans.

This strategy ensures a robust and secure development process for the GenAI-powered microservice, with automated testing and deployment practices that align with industry standards.


# User Stories

UserStoriesForGenAIApplication.pdf

# Architecture Diagram

GenAI Powered PDF Summarizer ArchtectureDaigram.jpg

# Strategic Proposal

Strategic Proposal.pdf
