[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6690081&assignment_repo_type=AssignmentRepo)
# SFU CMPT 756 Term Project - Team Rocket

We have created a cloud-service based application which uses highly decoupled microservices to serve user with music and playlist. To support this functionality, we build upon the cloud architecture developed in the CMPT756 assignments and add a new microservice called ‘playlist’. We have also experimented with scaling and loading of the system to test the resilience of the application. For the analysis and inference purpose, we have used Grafana, Prometheus and Kiali and triggered the load using Gatling. Below we discuss the details of our cluster architechture.

#### Tools and Technologies: Python, Flask, AWS, Docker, Kubernetes, DynamoDB, Gatling, Jira, Git

The main components of this project are:
#### 1. Set up kubernetes cluster on AWS
#### 2. Develop 3rd microservice in a highly decoupled design
#### 3. Observe a system at load and Scaling
	The Grafana and Kiali dashboard has been set up to view the traffic and effect on the system under stable load and after increasing the load, where load is simulated using Gatling tool. We first begin by giving a static load to our system using a Gatling script, where we send requests for 10 users per service, reaching about 3.5K total requests per minute . We monitor the effects using Grafana dashboard and Kiali dashboard. To encounter the failues coming up from the increasing the load, we scale the system by either increasing numnber of replicas for db service or increasing the number of nodes for the cluster.

#### 4. Failure modes of a system 
We experiment with the resilience of the system by deliberately introducing the failures like HTTP delays and timeouts and implementing traffic-shifting deployments. To simulate these behaviours, we make traffic policy changes in respective *-vs.yaml files and deploy the files to the running cluster to see changes in real time.
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


