docker container run -it --rm -v /home/k8s/gatling/results:/opt/gatling/results \
	-v /home/k8s/gatling:/opt/gatling/user-files \
	-v /home/k8s/gatling/target:/opt/gatling/target \
	-e CLUSTER_IP=`tools/getip.sh kubectl istio-system svc/istio-ingressgateway` \
	-e USERS=1 \
	-e SIM_NAME=ReadMusicSim \
	--label gatling \
	denvazh/gatling 
