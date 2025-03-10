pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub'  // Docker Hub credentials stored in Jenkins
        GITHUB_REPO = 'https://github.com/alijarai12/amnil_task.git'  // GitHub repository URL
    }

    stages {

        // Stage 1: Clone the GitHub repository
        stage('Clone GitHub Repository') {
            steps {
                script {
                    // Pull the latest code from the GitHub repository
                    git url: "${GITHUB_REPO}", branch: 'master'
                }
            }
        }

        // Stage 2: Build and Push Docker Images using Docker Compose
        stage('Build and Push Docker Images') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS,
                        usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {

                        // Log in to Docker Hub securely
                        sh """
                        echo ${DOCKERHUB_PASSWORD} | sudo docker login -u ${DOCKERHUB_USERNAME} --password-stdin
                        """

                        // Check if the docker-compose.yml file exists in the repository
                        sh "test -f docker-compose.yml || { echo 'docker-compose.yml not found!'; exit 1; }"

                        // Build Docker images using Docker Compose
                        sh "sudo docker-compose -f docker-compose.yml build"

                        // Push the Docker images to Docker Hub using Docker Compose
                        sh "sudo docker-compose -f docker-compose.yml push"
                    }
                }
            }
        }

    }

    post {
        always {
            // Clean up resources after each build
            echo 'Pipeline finished'
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
