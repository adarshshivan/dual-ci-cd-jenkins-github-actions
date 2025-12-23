# Challenges and Solutions

## Challenge — External Docker Registry Access
During local Jenkins execution, Docker image pulls occasionally failed due to TLS handshake timeouts when accessing Docker Hub.

### Root Cause
Dependency on external registry availability and network reliability.

### Solution
Base images were pre-pulled on the host system, allowing CI builds to reuse cached layers.

### Outcome
Improved CI reliability and reduced build times without modifying Dockerfile logic.

---
