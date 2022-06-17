#This python file assumes following conditions to be True
#1.minikube and kubectl are installed
#2.minikube is running
#3.Necessary files are present in the folder

import subprocess as sp
print(sp.getoutput("kubectl create -f blue_app_deployment.yaml"))
print(sp.getoutput("kubectl create -f green_app_deployment.yaml"))
print(sp.getoutput("kubectl create -f blue_app_service.yaml"))
print(sp.getoutput("kubectl create -f green_app_service.yaml"))
print(sp.getoutput("kubectl create -f travstack_ingress.yaml"))