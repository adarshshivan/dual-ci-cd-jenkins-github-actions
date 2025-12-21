# Commit message: "simulation for startup failure"

```yaml

Started by user Adarsh Shivan
Obtained jenkins/jenkinsfile.aws from git https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/dual-ci-cd-aws
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/dual-ci-cd-aws/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git # timeout=10
Fetching upstream changes from https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
 > git --version # timeout=10
 > git --version # 'git version 2.34.1'
 > git fetch --tags --force --progress -- https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision b08bb25fc428b33d5a7ce8611e6ac61b9e756b55 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f b08bb25fc428b33d5a7ce8611e6ac61b9e756b55 # timeout=10
Commit message: "simulation for startup failure"
 > git rev-list --no-walk 47dd5410024839269076cacb272a2b12f20f84e7 # timeout=10
[Pipeline] }
[Pipeline] // stage
[Pipeline] withEnv
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Checkout Code)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/dual-ci-cd-aws/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git # timeout=10
Fetching upstream changes from https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
 > git --version # timeout=10
 > git --version # 'git version 2.34.1'
 > git fetch --tags --force --progress -- https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision b08bb25fc428b33d5a7ce8611e6ac61b9e756b55 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f b08bb25fc428b33d5a7ce8611e6ac61b9e756b55 # timeout=10
Commit message: "simulation for startup failure"
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build Docker Image)
[Pipeline] sh
+ docker build -t dual-ci-cd-app -f docker/Dockerfile .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  11.78kB
Step 1/7 : FROM python:3.11-slim
 ---> cb352e69d7b6
Step 2/7 : WORKDIR /app
 ---> Using cache
 ---> 774e43bb6f26
Step 3/7 : COPY app/main.py /app/main.py
 ---> fcc5716da56a
Step 4/7 : EXPOSE 8000
 ---> Running in cb6ec816c65f
 ---> Removed intermediate container cb6ec816c65f
 ---> f3003d02627e
Step 5/7 : ENV APP_ENV=production
 ---> Running in 5998e04e13ae
 ---> Removed intermediate container 5998e04e13ae
 ---> 42c563c35e1e
Step 6/7 : ENV APP_PORT=8000
 ---> Running in ce5fcb7a0b18
 ---> Removed intermediate container ce5fcb7a0b18
 ---> 14b926e40aed
Step 7/7 : CMD ["python", "main.py"]
 ---> Running in 238dcdc2e7e5
 ---> Removed intermediate container 238dcdc2e7e5
 ---> d007c540474c
Successfully built d007c540474c
Successfully tagged dual-ci-cd-app:latest
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Container)
[Pipeline] sh
+ docker run -d -p 8000:8000 --name aws-ci-container dual-ci-cd-app
59f1f2be75445aea33acfc0a17d85d054efe23351f441b2536e462a1efea3516
+ sleep 5
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Validate Application)
[Pipeline] sh
+ curl -f http://localhost:8000
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
curl: (7) Failed to connect to localhost port 8000 after 1 ms: Connection refused
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] sh
+ docker stop aws-ci-container
aws-ci-container
+ docker rm aws-ci-container
aws-ci-container
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
ERROR: script returned exit code 7
Finished: FAILURE


```

---