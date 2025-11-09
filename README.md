# ACEest Fitness Tracker – DevOps Assignment

[![CI/CD Pipeline](https://github.com/9kiran/ACEest_Fitness_V2/actions/workflows/main.yml/badge.svg)](https://github.com/9kiran/ACEest_Fitness_V2/actions)  
[![Coverage](https://img.shields.io/badge/Coverage-TBD-brightgreen)](https://sonarcloud.io/summary/overall?id=9kiran_ACEest_Fitness_V2&branch=main)  
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=9kiran_ACEest_Fitness_V2&metric=alert_status)](https://sonarcloud.io/summary/overall?id=9kiran_ACEest_Fitness_V2&branch=main)
[![Coverage Status](https://codecov.io/gh/9kiran/ACEest_Fitness_V2/branch/main/graph/badge.svg)](https://codecov.io/gh/9kiran/ACEest_Fitness_V2)

## Overview
This repository contains the ACEest Fitness Tracker application and demonstrates applied DevOps practices:
- Version control with Git & GitHub
- Unit testing with Pytest and coverage measurement
- Static code analysis and quality gate with SonarCloud
- Containerization using Docker (and Podman compatible)
- Continuous Integration via GitHub Actions
- Deployment strategies illustrated via Kubernetes manifests (Blue-Green, Canary, Rolling Update, A/B Testing)

## Project Features
- GUI application built in Python (Tkinter) representing core fitness and gym functionalities.
- Testable logic separated into `aceest_fitness/core.py` for coverage and maintainability.
- Historical versions of the application tracked under `versions/`.
- CI/CD pipeline triggers on every commit and pull request across all branches.
- Docker image published to Docker Hub for reproducible deployments.
- Kubernetes manifests for multiple deployment strategies.

## Technology Stack
- Python 3.10
- Tkinter for GUI (desktop front-end)
- Pytest for unit testing and coverage
- Docker / Podman for containerization
- GitHub Actions for CI/CD
- SonarCloud for static analysis and code quality
- Kubernetes (optional for local Minikube or cloud provider) for deployment strategies

## Run Locally
### Clone repository
```bash
git clone https://github.com/9kiran/ACEest_Fitness_V2.git
cd ACEest_Fitness_V2
````

### Create & activate virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python aceest_fitness/app_v1_3.py
```

### Execute tests with coverage

```bash
pytest --cov=aceest_fitness --cov-report=term-missing
```

## Docker usage

Build the image:

```bash
docker build -t 9kiran/aceest_fitness:latest .
```

Push the image (after login and tagging accordingly):

```bash
docker push 9kiran/aceest_fitness:latest
```

## CI/CD Pipeline (GitHub Actions)

Triggers: any push to any branch + pull requests.
Key steps:

1. Checkout code
2. Install dependencies
3. Run tests with coverage
4. Scan code with SonarCloud
5. Build and tag Docker image
6. Push image to Docker Hub

## Kubernetes Deployment Strategies

Manifests available under `k8s/` folder demonstrate:

* **Blue-Green Deployment**: two environments (blue & green), switch traffic via Service selector.
* **Canary Deployment**: route a small percentage of traffic to canary version before full rollout.
* **Rolling Update**: gradual replacement of pods with new version.
* **A/B Testing**: parallel deployments (version A vs version B) for feature testing.

## Project Links

* GitHub Repository: [https://github.com/9kiran/ACEest_Fitness_V2](https://github.com/9kiran/ACEest_Fitness_V2)
* SonarCloud Dashboard: [https://sonarcloud.io/summary/overall?id=9kiran_ACEest_Fitness_V2&branch=main](https://sonarcloud.io/summary/overall?id=9kiran_ACEest_Fitness_V2&branch=main)
* Docker Hub: [https://hub.docker.com/r/9kiranpatil/aceest_fitness](https://hub.docker.com/r/9kiranpatil/aceest_fitness)

## Student Info

**Name:** Kiran Patil
**Course:** Introduction to DevOps (CSIZG514/SEZG514)
**Assignment:** Phase 1 – DevOps Project
**Submission Date:** *[Insert date here]*
Would you like me to **generate the actual badge URL for coverage** once your SonarCloud shows the final coverage percentage?
::contentReference[oaicite:0]{index=0}
```
