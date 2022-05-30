import os


print(os.popen('echo Starting Build of Docker Images').read())

print(os.popen('docker build -t appdocker .').read())

print(os.popen('echo Docker Image Build complete').read())

print(os.popen('echo deploying to Kubernetes').read())

print(os.popen('kubectl apply -f deployment.yaml').read())

print(os.popen('echo deploying to Kubernetes complete').read())

print(os.popen('kubectl get pods').read())