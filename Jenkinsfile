pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub' 
        GITHUB_REPO = 'https://github.com/alijarai12/amnil_task.git' 
        DOCKER_IMAGE_NAME = "alija10/amnil-pipeline-web" 
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
                    // Login to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Login to Docker Hub
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USER} --password-stdin"
                        
                        // Build the image
                        sh 'docker compose build'
                        
                        // Push the image to Docker Hub
                        sh "docker push ${DOCKER_IMAGE}"
                    }
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
