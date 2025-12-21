# Commit message: "ci: add jenkins pipeline for aws ec2"

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
Cloning the remote Git repository
Cloning repository https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
 > git init /var/lib/jenkins/workspace/dual-ci-cd-aws # timeout=10
Fetching upstream changes from https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
 > git --version # timeout=10
 > git --version # 'git version 2.34.1'
 > git fetch --tags --force --progress -- https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision 3aba7c99ab97e237c60e45a3017e4adf584a7d4f (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 3aba7c99ab97e237c60e45a3017e4adf584a7d4f # timeout=10
Commit message: "ci: add jenkins pipeline for aws ec2"
First time build. Skipping changelog.
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
Checking out Revision 3aba7c99ab97e237c60e45a3017e4adf584a7d4f (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 3aba7c99ab97e237c60e45a3017e4adf584a7d4f # timeout=10
Commit message: "ci: add jenkins pipeline for aws ec2"
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build Docker Image)
[Pipeline] sh
+ docker build -t dual-ci-cd-app -f docker/Dockerfile .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  10.75kB
Step 1/7 : FROM python:3.11-slim
3.11-slim: Pulling from library/python
1733a4cd5954: Pulling fs layer
72cf4c3b8301: Pulling fs layer
4d55cfecf366: Pulling fs layer
3f0cdbca744e: Pulling fs layer
3f0cdbca744e: Waiting
72cf4c3b8301: Verifying Checksum
72cf4c3b8301: Download complete
4d55cfecf366: Verifying Checksum
4d55cfecf366: Download complete
1733a4cd5954: Verifying Checksum
1733a4cd5954: Download complete
3f0cdbca744e: Verifying Checksum
3f0cdbca744e: Download complete
1733a4cd5954: Pull complete
72cf4c3b8301: Pull complete
4d55cfecf366: Pull complete
3f0cdbca744e: Pull complete
Digest: sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c
Status: Downloaded newer image for python:3.11-slim
 ---> cb352e69d7b6
Step 2/7 : WORKDIR /app
 ---> Running in f61fa0c20d9a
 ---> Removed intermediate container f61fa0c20d9a
 ---> 774e43bb6f26
Step 3/7 : COPY app/main.py /app/main.py
 ---> 245a70c8127b
Step 4/7 : EXPOSE 8000
 ---> Running in 1a6c200d09b0
 ---> Removed intermediate container 1a6c200d09b0
 ---> be976a9d36cb
Step 5/7 : ENV APP_ENV=production
 ---> Running in 8df6518bb94a
 ---> Removed intermediate container 8df6518bb94a
 ---> 8d299b9db306
Step 6/7 : ENV APP_PORT=8000
 ---> Running in beb9b820ca0c
 ---> Removed intermediate container beb9b820ca0c
 ---> a2466f810289
Step 7/7 : CMD ["python", "main.py"]
 ---> Running in 80ee2824a643
 ---> Removed intermediate container 80ee2824a643
 ---> ff39f242b030
Successfully built ff39f242b030
Successfully tagged dual-ci-cd-app:latest
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Container)
[Pipeline] sh
+ docker run -d -p 8000:8000 --name aws-ci-container dual-ci-cd-app
4869bc68b36ab1abe000253ee36396659160f40ae59cb6ecccf9296abd0fcc52
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
100    86    0    86    0     0  24891      0 --:--:-- --:--:-- --:--:-- 28666
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
