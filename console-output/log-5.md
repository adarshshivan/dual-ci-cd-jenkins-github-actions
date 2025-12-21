# Commit message: "Docker build failure simulation"

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
Checking out Revision 84a720090702f9a3bc4f7d1d64890625d057e558 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 84a720090702f9a3bc4f7d1d64890625d057e558 # timeout=10
Commit message: "Docker build failure simulation"
 > git rev-list --no-walk a60851e1b0cc3f46de9a6af64cd6cb4335445e58 # timeout=10
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
Checking out Revision 84a720090702f9a3bc4f7d1d64890625d057e558 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 84a720090702f9a3bc4f7d1d64890625d057e558 # timeout=10
Commit message: "Docker build failure simulation"
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
Step 3/7 : COPY app/main_wrong.py /app/main.py
COPY failed: file not found in build context or excluded by .dockerignore: stat app/main_wrong.py: file does not exist
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Container)
Stage "Run Container" skipped due to earlier failure(s)
[Pipeline] getContext
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Validate Application)
Stage "Validate Application" skipped due to earlier failure(s)
[Pipeline] getContext
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] sh
+ docker stop aws-ci-container
Error response from daemon: No such container: aws-ci-container
+ true
+ docker rm aws-ci-container
Error response from daemon: No such container: aws-ci-container
+ true
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
ERROR: script returned exit code 1
Finished: FAILURE


```

---