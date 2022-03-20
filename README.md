[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6690081&assignment_repo_type=AssignmentRepo)
# SFU CMPT 756 Term Project - Team Rocket

This repo contains the code to develop the multiple microservices in a cloud environment, in a highly decoupled design. The repo is also used to observe the system at load using Gatling. We build upon the cloud architecture developed in the CMPT756 assignments and added a new microservice called ‘playlist’. So the application incorporates 5 microservices in total, out of which 3 are music, user and playlist services. The remaining 2 are for initializing and loading the data to DynamoDB.


#### Tools and Technologies: Python, Flask, AWS, Docker, Kubernetes, DynamoDB, Gatling, Jira, Git


The main components of this project are:
#### 1. Set up kubernetes cluster on AWS
#### 2. Develop 3rd microservice in a highly decoupled design
#### 3. Observe a system at load using a variety of tools [TBD]
	Gatling was used for testing the system at load.
	At the moment we are having a bit of trouble getting gatling to work as its not picking up the scala files
	We are working on fixing this issue

#### 4. Explore the failure modes of a system [TBD]
#### 5. Explore various approaches to remediate such failures [TBD]


#### Please ensure AWS DynamoDB is accessible/running
Regardless of where your cluster will run, it uses AWS DynamoDB
for its backend database. Check that you have the necessary tables
installed by running

~~~
$ aws dynamodb list-tables
~~~

The resulting output should include tables `User`, `Music` and `Playlist`.

----


