pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub' 
        GITHUB_REPO = 'https://github.com/alijarai12/amnil_task.git' 
        DOCKER_IMAGE_NAME = "alija10/amnil-pipeline-web" 
        DOCKER_TAG = "latest"
    }

    stages {

        stage('Clone GitHub Repository') {
            steps {
                script {
                    git url: "${GITHUB_REPO}", branch: 'master'
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    sh 'docker compose build'

                    // Login to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USER} --password-stdin"
                    }

                    sh 'docker push ${DOCKER_IMAGE_NAME}:${DOCKER_TAG}'
                }
            }
        }
        stage('Run the Containers  with docker-compose ') {
            steps {
                script {
                    sh 'docker compose up -d'
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
