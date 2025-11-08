// Jenkinsfile
pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = 'dockerhub-creds'    // set credential id in Jenkins
    DOCKERHUB_REPO = 'YOUR_DOCKERHUB_USER/aceest_fitness'
    SONAR_TOKEN = credentials('sonar-token')     // set credential id in Jenkins
    SONAR_HOST_URL = 'http://YOUR_SONAR_HOST:9000' // replace if using Sonar
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install Dependencies') {
      steps {
        sh 'python3 -m venv .venv || python -m venv .venv'
        sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        sh '. .venv/bin/activate && pytest --cov=aceest_fitness --cov-report=xml --cov-report=term-missing'
      }
      post {
        always {
          junit 'tests/*.xml'  // if you generate junit xml; optional
          archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
        }
      }
    }

    stage('SonarQube Analysis') {
      when {
        expression { return env.SONAR_TOKEN != null && env.SONAR_HOST_URL != null }
      }
      steps {
        withSonarQubeEnv('SonarQube') {
          sh '. .venv/bin/activate && sonar-scanner -Dsonar.projectKey=ACEest_Fitness -Dsonar.sources=aceest_fitness -Dsonar.python.coverage.reportPaths=coverage.xml -Dsonar.host.url=' + env.SONAR_HOST_URL + ' -Dsonar.login=' + env.SONAR_TOKEN
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${DOCKERHUB_REPO}:${env.BUILD_NUMBER} ."
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
          sh "docker push ${DOCKERHUB_REPO}:${env.BUILD_NUMBER}"
          sh "docker tag ${DOCKERHUB_REPO}:${env.BUILD_NUMBER} ${DOCKERHUB_REPO}:latest"
          sh "docker push ${DOCKERHUB_REPO}:latest"
        }
      }
    }
  }

  post {
    success {
      echo "Pipeline completed successfully."
    }
    failure {
      echo "Pipeline failed."
    }
  }
}
