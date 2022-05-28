import os

print(os.popen('echo Creating and Deploying pods ').read())

print(os.popen('kubectl create  -f deployment.yml  --dry-run=client --validate=false').read())

print(os.popen('kubectl apply -f deployment.yml').read())

print(os.popen('kubectl get pods ').read())