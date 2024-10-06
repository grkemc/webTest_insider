# webTest_insider - Selenium E2E Test Automation in Kubernetes

## Overview

This project implements an end-to-end (E2E) test suite using **Python** and **Selenium**, designed to run within a **Kubernetes** cluster. The tests target Insider's website to verify its pages and functionalities, specifically focusing on careers and job listings.

## Features

- **Selenium-based E2E tests** using `pytest`.
- Containerized test project using **Docker**.
- Two main Kubernetes Pods:
  1. **Test Case Controller Pod**: Manages the test cases.
  2. **Chrome Node Pod**: Executes Selenium tests in a **headless Chrome** browser.
- Configurable **inter-pod communication** for dynamic test distribution and execution.

## Prerequisites

Ensure you have the following tools installed before proceeding:

- [Docker](https://docs.docker.com/get-docker/)
- [Kubernetes (`kubectl`)](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/) (for Kubernetes resource management)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/get-started-install.html) (optional for EKS setup)
- [Python](https://www.python.org/downloads/) (for writing and running Kubernetes deployment scripts)

---

## System Architecture

### 1. Test Controller Pod

- This pod is responsible for managing and distributing the test cases.
- The tests are written in Python and utilize Selenium to automate the browser.
- Communicates with Chrome Node Pods through Kubernetes Services for test execution.

### 2. Chrome Node Pod

- This pod runs a headless Chrome browser to execute Selenium tests.
- Dynamically created based on the `node_count` parameter (min 1, max 5).
- Uses the `seleniarm/standalone-chromium` image to facilitate headless browser functionality.

### 3. Inter-Pod Communication

- The Test Controller Pod communicates with the Chrome Node Pod using a defined `SELENIUM_SERVER_URL`.
- Kubernetes **ClusterIP Services** facilitate communication between the pods.
- DNS-based routing allows the Test Controller Pod to send commands to Chrome Node Pods for execution.

---

## Project Setup & Execution

### Test Cases

The Selenium test cases cover the following scenarios on the [Insider](https://useinsider.com/) website:

1. Verify the home page loads successfully.
2. Navigate to the Careers page and validate various sections (Locations, Teams, Life at Insider).
3. Filter QA jobs by "Location" and "Department" and verify the presence of job listings.
4. Validate that all listed jobs contain specific criteria.
5. Click on a job to ensure redirection to the Lever Application form.

---

### Dockerization & Kubernetes Setup

#### 1. Create a Docker Image for the Test Project

A `Dockerfile` is created to containerize the Python Selenium tests. The Docker image exposes necessary ports and installs all dependencies.

```bash
docker build --platform=linux/amd64 -t gorkemc/webtest_insider:latest .
docker tag gorkemc/webtest_insider:latest gorkemc/webtest_insider:latest
docker push gorkemc/webtest_insider:latest
```

## 2. Setup Kubernetes Pods

- **Test Controller Pod**: Runs the test cases and manages test distribution.
- **Chrome Node Pod**: Runs Selenium tests in a headless Chrome browser.

YAML files for Pod creation:

- `test-controller-pod.yaml`: Defines the Test Controller Pod.
- `chrome-node-pod.yaml`: Defines the Chrome Node Pod.

---

## 3. Configure Helm Charts

Helm is used to dynamically manage the deployments of the Chrome Node and Test Controller Pods. Helm templates ensure that the Chrome Node Pod count can be adjusted using the `node_count` parameter.

---

## 4. Inter-Pod Communication

Ensure that the `SELENIUM_SERVER_URL` is properly set to facilitate communication between the Test Controller Pod and Chrome Node Pod.

Check connectivity using `kubectl`:

```bash
kubectl exec -it test-controller -- curl http://chrome-node:4444/wd/hub/status
```

## Deployment to Kubernetes Cluster

### Local Kubernetes Cluster

1. **Deploy Using Helm**

 ```bash
 helm install selenium-tests .
 ```

## 2. Deploy Using `kubectl`

```bash
kubectl apply -f test-controller-pod.yaml
kubectl apply -f chrome-node-pod.yaml
```

## Python Script for Dynamic Deployment & Execution

1. **Deploy Kubernetes Resources**  
   The script dynamically deploys Chrome Node Pods based on the `node_count` parameter. Test cases are managed and sent from the Test Controller Pod to the Chrome Node Pods.

2. **Script Structure (`deploy_k8s_resources.py`)**
   - **Create Chrome Node Pods**: Deploys the `seleniarm/standalone-chromium` pods for Selenium test execution.
   - **Create Test Controller Pod**: Deploys the pod responsible for running and managing tests.
   - **Check Pod Readiness**: Ensures that all pods are in a running state before initiating tests.

3. **Run the Deployment Script**

```bash
python scripts/deploy_k8s_resources.py
```
