# Commit message: "fixed docker build fail simulation"

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
Checking out Revision 000a17aa19ad841ca25b33f4d465b768756b4bfb (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 000a17aa19ad841ca25b33f4d465b768756b4bfb # timeout=10
Commit message: "fixed docker build fail simulation"
 > git rev-list --no-walk 84a720090702f9a3bc4f7d1d64890625d057e558 # timeout=10
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
Checking out Revision 000a17aa19ad841ca25b33f4d465b768756b4bfb (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 000a17aa19ad841ca25b33f4d465b768756b4bfb # timeout=10
Commit message: "fixed docker build fail simulation"
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
 ---> Using cache
 ---> f2447525fb64
Step 4/7 : EXPOSE 8000
 ---> Using cache
 ---> 54ce8660ba3d
Step 5/7 : ENV APP_ENV=production
 ---> Using cache
 ---> efab8c94435d
Step 6/7 : ENV APP_PORT=8000
 ---> Using cache
 ---> 0c6f42f9a7b9
Step 7/7 : CMD ["python", "main.py"]
 ---> Using cache
 ---> 924f296a89ff
Successfully built 924f296a89ff
Successfully tagged dual-ci-cd-app:latest
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Container)
[Pipeline] sh
+ docker run -d -p 8000:8000 --name aws-ci-container dual-ci-cd-app
ffb5a711a7580bd2cacfd9046171541dc4452af2de20ab8f7e372f583e6f5351
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
100    86    0    86    0     0   2663      0 --:--:-- --:--:-- --:--:--  2687
Application: Dual CI/CD Demo App
Environment: production
Status: Running Successfully
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
Finished: SUCCESS


```

---