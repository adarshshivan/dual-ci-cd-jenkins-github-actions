# Solution Overview

The solution implements a **Docker-centric CI design** executed through:

- GitHub Actions for managed CI
- Jenkins hosted on AWS EC2
- Jenkins running locally inside Docker

All pipelines perform:
1. Source code checkout
2. Docker image build
3. Container execution
4. Runtime validation using HTTP checks
5. Cleanup of resources

Pipelines are defined as code to ensure reproducibility and auditability.

---