# Failure Simulation and Recovery

Three controlled failure scenarios were simulated:

## Failure 1 — Application Startup Failure
- **Cause:** Forced runtime exception in application
- **Detection:** Container exits immediately
- **Recovery:** Code fix and redeploy

## Failure 2 — Docker Build Failure
- **Cause:** Missing file referenced in Dockerfile
- **Detection:** Docker build fails
- **Recovery:** Correct file path and rebuild

## Failure 3 — Jenkinsfile Misconfiguration
- **Cause:** Syntax error in Jenkinsfile
- **Detection:** Pipeline parsing fails instantly
- **Recovery:** Restore valid Jenkinsfile syntax

These simulations validated CI robustness and recovery procedures.

---
