# CI Workflow Breakdown

Each CI pipeline executes the following stages:

1. **Checkout Source Code**
2. **Build Docker Image**
3. **Run Application Container**
4. **Validate Application via HTTP**
5. **Cleanup Containers**

The workflow ensures failures are detected early and consistently across environments.

---
