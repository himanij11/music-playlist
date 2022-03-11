[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6690081&assignment_repo_type=AssignmentRepo)
# SFU CMPT 756 Term Project


### 1. Developing for the cloud environment

### 2. Developing 3 microservices using a highly decoupled design:
#### a. Music 
#### b. Users 
#### c. Playlist

### 3. Observing a system at load using a variety of tools

### 4. Exploring the failure modes of a system

### 5. Exploring various approaches to remediate such failures


#### Please ensure AWS DynamoDB is accessible/running
Regardless of where your cluster will run, it uses AWS DynamoDB
for its backend database. Check that you have the necessary tables
installed by running

~~~
$ aws dynamodb list-tables
~~~

The resulting output should include tables `User` and `Music`.

----


