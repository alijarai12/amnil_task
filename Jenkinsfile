pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub'  // Docker Hub credentials stored in Jenkins
        IMAGE_NAME = 'myapp-image'  // Image name for Docker Hub
        IMAGE_TAG = 'latest'  // Tag for the image
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

        // Stage 2: Build and Push Docker Image
        stage('Build and Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS,
                        usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {

                        // Log in to Docker Hub securely
                        sh """
                        echo ${DOCKERHUB_PASSWORD} | sudo docker login -u ${DOCKERHUB_USERNAME} --password-stdin
                        """

                        // Check if the Dockerfile exists in the repository
                        sh "test -f Dockerfile || { echo 'Dockerfile not found!'; exit 1; }"

                        // Build the Docker image from the Dockerfile
                        sh "sudo docker build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG ."

                        // Push the built image to Docker Hub
                        sh "sudo docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:$IMAGE_TAG"
                    }
                }
            }
        }

        // Stage 3: Docker Compose Up (Optional)
        stage('Docker Compose Up') {
            steps {
                script {
                    // This stage is optional and can be skipped if Docker Compose is not needed
                    // If Docker Compose is part of your application, this will start the containers.
                    sh 'docker-compose up -d'  // Start the services defined in docker-compose.yml
                }
            }
        }

    }

    post {
        always {
            // Clean up resources after each build
            echo 'Pipeline finished'
            sh 'docker system prune -f'  // Remove unused Docker images and containers
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
