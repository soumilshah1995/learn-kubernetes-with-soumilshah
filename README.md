# learn-kubernetes-with-soumilshah
learn kuberneteswith soumilshah


------------------------- Watch ----------------------------------


* Beginners | Learning Kubernetes in Easy way | Theory |#1
* Link: https://www.youtube.com/watch?v=h_-lsO1ZIQE&list=PLL2hlSFBmWwx9pdmBesD0fr3e-_aJlYBa&index=1&t=68s




* Beginners | Learning Kubernetes in Easy way | Commands and Deploying the Dashboard UI |#2
* Link: https://www.youtube.com/watch?v=1Fleff8SrNA

```bash
Install Docker Desktop 
https://docs.docker.com/desktop/windows/install/

Step 1: 
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml

Step2: generate Token 
kubectl describe secret -n kube-system

Step 3: Start Webserver
kubectl proxy

Step 4: Go to Dashboard
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.


kubectl get pods
kubectl get all
kubectl run my-ngnix --image=ngnix:alpine
kubectl delete pod my-ngnix
```




* Title : Beginners | Learning Kubernetes in Easy way | Probes | Livebness Probe with Demo |#3

* Link : https://www.youtube.com/watch?v=N_EvPa3gQko




* Beginners | Learning Kubernetes in Easy way | Replicas Set |#4
* Link: 

#### Helper commands   
```

kubectl get rs
kubectl delete rs XXXXX
kubectl delete -f deployment.yml
kubectl delete deployment XXXX

kubectl scale --replicas=30 -f deployment.yaml   ## Scale up
kubectl scale --replicas=1 -f deployment.yaml ## Scale down


# Metrics Server Debugging commands 
kubectl -n kube-system get pods
kubectl -n kube-system  describe pod XXXXX
kubectl -n kube-system edit deploy pods

# Get Resources 
kubectl get hpa 
kubectl delete hpa XXX

# Manually Auto Scale through command Line 
kubectl autoscale deployment appdeploy --cpu-percent=20 --min=1 --max=10  
```


* Beginners | What is Helm in Kubernetes how to Install | Hello World Demo
```
helm create first-app

helm template first-app first-app --debug

helm install first-app first-app

helm list

helm upgrade first-app first-app --values ./first-app/values.yaml

helm delete first-app

```



* Beginners | Learning Kubernetes in Easy way | Probes | Livebness Probe with Demo |#3
* Resources https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes




* Title: Learning kubernetes in a easy way  crash course beginner | Intro Video
* Link:  https://www.youtube.com/watch?v=MQJT9a6I2b8
                

* Title: Getting started with Kubernetes Crash Course in 45 Minutes for Beginner
* Link:  https://www.youtube.com/watch?v=8re9IMRFO-0
                


* Title: Production ready architecture with external and internal Load balancing with Kubernetes | Python
* Link:  https://www.youtube.com/watch?v=UpMa10RgfwU
        
   

     
     
------------------------- Connect With Me ----------------------------------


Website : https://soumilshah.herokuapp.com


Github : https://github.com/soumilshah1995


Linkedin : https://www.linkedin.com/in/shah-soumil/


Blog : https://soumilshah1995.blogspot.com/


Youtube :  https://www.youtube.com/channel/UC_eOodxvwS_H7x2uLQa-svw?view_as=subscriber


Donate Me :  https://www.paypal.com/paypalme/soumilshah1995


-----------------------------------------------------

