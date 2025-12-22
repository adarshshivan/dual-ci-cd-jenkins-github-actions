# DevOps Project 3 — Dual CI/CD Pipelines with GitHub Actions & Jenkins

This project demonstrates the design and implementation of **dual CI/CD pipelines** using both **GitHub Actions** and **Jenkins**, validating application builds and runtime behavior through Dockerized workflows.

The same application and Docker configuration are executed across multiple CI environments to ensure **pipeline consistency, portability, and reliability**:

- GitHub Actions (managed CI)
- Jenkins on AWS EC2 (self-hosted CI)
- Jenkins on Local Machine (Dockerized Jenkins)

The pipelines follow a **Docker-first CI approach**, including source checkout, image build, container execution, runtime validation, and cleanup.

Cloud resources used during validation were intentionally decommissioned after successful testing to optimize cost, while the setup remains fully reproducible.

### Key Highlights
- Pipeline-as-Code using YAML and Jenkinsfiles
- Docker-based CI validation
- CI parity across cloud and local environments
- Failure simulation and recovery analysis
- Cost-aware infrastructure cleanup

Detailed documentation is available in the [`docs/`](./docs) directory.

---