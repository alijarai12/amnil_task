pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub' 
        GITHUB_REPO = 'https://github.com/alijarai12/amnil_task.git' 
        DOCKER_IMAGE_NAME = "alija10/amnil-pipeline-web" 
    }

    stages {


        stage('Build Image') {
            steps {
                script {
                    // Run Docker Compose to build the image
                    sh 'docker compose -f docker-compose.yml build'
                    
                    // Explicitly tag the image after building it
                    sh "docker tag amnil-pipeline-web:latest ${DOCKER_IMAGE_NAME}:latest"
                    
                    
                }
            }
        }
        

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        // Log in to Docker Hub using Jenkins credentials
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                        
                        // Push the tagged image to Docker Hub
                        sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }

        
        stage('Run the Containers  with docker compose ') {
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
