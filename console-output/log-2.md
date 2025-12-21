# Commit message: "fixed curl response"

```yaml

Started by user Adarsh Shivan
Obtained jenkins/jenkinsfile.local from git https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/dual-ci-cd-local
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Declarative: Checkout SCM)
[Pipeline] checkout
Selected Git installation does not exist. Using Default
The recommended git tool is: NONE
No credentials specified
 > git rev-parse --resolve-git-dir /var/jenkins_home/workspace/dual-ci-cd-local/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git # timeout=10
Fetching upstream changes from https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
 > git --version # timeout=10
 > git --version # 'git version 2.47.3'
 > git fetch --tags --force --progress -- https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision cde64393e925e16042c89e2d6b67b9d2a0c69664 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f cde64393e925e16042c89e2d6b67b9d2a0c69664 # timeout=10
Commit message: "fixed curl response"
 > git rev-list --no-walk ffbb204e927a2896145938dd778c6fb2911a7858 # timeout=10
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
 > git rev-parse --resolve-git-dir /var/jenkins_home/workspace/dual-ci-cd-local/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git # timeout=10
Fetching upstream changes from https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git
 > git --version # timeout=10
 > git --version # 'git version 2.47.3'
 > git fetch --tags --force --progress -- https://github.com/adarshshivan/dual-ci-cd-jenkins-github-actions.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
Checking out Revision cde64393e925e16042c89e2d6b67b9d2a0c69664 (refs/remotes/origin/main)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f cde64393e925e16042c89e2d6b67b9d2a0c69664 # timeout=10
Commit message: "fixed curl response"
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build Docker Image)
[Pipeline] sh
+ docker build -t dual-ci-cd-app-local -f docker/Dockerfile .
#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 396B 0.0s done
#1 DONE 0.1s

#2 [internal] load metadata for docker.io/library/python:3.11-slim
#2 DONE 0.0s

#3 [internal] load .dockerignore
#3 transferring context: 82B 0.0s done
#3 DONE 0.0s

#4 [internal] load build context
#4 transferring context: 56B 0.1s done
#4 DONE 0.1s

#5 [1/3] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c
#5 resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c 0.1s done
#5 DONE 0.1s

#6 [2/3] WORKDIR /app
#6 CACHED

#7 [3/3] COPY app/main.py /app/main.py
#7 CACHED

#8 exporting to image
#8 exporting layers done
#8 exporting manifest sha256:a0c4a808f5a78a2b94c1927e7d15e017779a61e89b2ebc47b8195c98374f8ad7 done
#8 exporting config sha256:e30d73a619c63313d2dd58aeecdeca27e0ba4f7f7360cdce7fd1f7de8afc470e done
#8 exporting attestation manifest sha256:d8c4f3d0722a8b2c992788bc4e36f78e0f06933874db0ef127b38a33c028e069 0.0s done
#8 exporting manifest list sha256:1057265395248f1995b90e1c379695f03903a6b1678a5b35e9cd23f4bcd5384e 0.0s done
#8 naming to docker.io/library/dual-ci-cd-app-local:latest 0.0s done
#8 unpacking to docker.io/library/dual-ci-cd-app-local:latest 0.0s done
#8 DONE 0.2s
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Run Container)
[Pipeline] sh
+ docker run -d -p 8001:8000 --name local-ci-container dual-ci-cd-app-local
bcf22e3957ad89a79c31a0d2bfd5c494e8c4c4f1a0d96b2ce0237fc68e190a71
+ sleep 5
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Validate Application)
[Pipeline] sh
+ docker inspect -f {{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}} local-ci-container
+ CONTAINER_IP=172.17.0.3
+ curl -f http://172.17.0.3:8000
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100    86    0    86    0     0   1051      0 --:--:-- --:--:-- --:--:--  1061
Application: Dual CI/CD Demo App
Environment: production
Status: Running Successfully
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] sh
+ docker stop local-ci-container
local-ci-container
+ docker rm local-ci-container
local-ci-container
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