# nginx-ingress-controller
Example of setting up ingress

Creating a “blue-app” Deployment and expose it via an Internal Service with the following specification:
Image: hashicorp/http-echo
Arguments: -listen:=8080 -text=”I am blue”
Replicas: 2
Port: 8080

Creating a “green-app” Deployment and expose it via an Internal Service with the following specification:
Image: hashicorp/http-echo
Arguments: -listen:=8081 -text=”I am green”
Replicas: 3
Port: 8081

Using nginx ingress controller to expose an http endpoint with the paths “/blue” for the blue-app Deployment, and “/green” for the green-app Deployment.
