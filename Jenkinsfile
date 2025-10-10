pipeline {
    agent any

    environment {
        // Docker image repository
        DOCKER_IMAGE = 'bludivehub/bluinsights-blog-service'
        DOCKER_COMPOSE_FILE = 'docker-compose.yaml'
        DOCKERHUB_CREDS = credentials('Dockerhub-creds')
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    // Checkout source code from GitHub using GitHub credentials
                    git credentialsId: 'github-jenkins-cred', url: 'https://github.com/Bludive-Devops-Platform/BluInsights_Blog.git', branch: 'main'
                }
            }
        }

        stage('Build and Push Docker Images') {
            steps {
                script {
                    // Docker login for Jenkins using stored credentials
                    sh """
                        echo '${DOCKERHUB_CREDS_PSW}' | docker login -u '${DOCKERHUB_CREDS_USR}' --password-stdin
                    """
                    
                    // Build and push the Docker images defined in docker-compose.yaml
                    sh """
                        docker compose -f ${DOCKER_COMPOSE_FILE} build
                        docker compose -f ${DOCKER_COMPOSE_FILE} push
                    """
                }
            }
        }

        stage('Test Docker Images') {
            steps {
                script {
                    // Login to DockerHub before running docker-compose up
                    sh """
                        echo '${DOCKERHUB_CREDS_PSW}' | docker login -u '${DOCKERHUB_CREDS_USR}' --password-stdin
                    """

                    // Run Docker Compose to start the services defined in the docker-compose.yaml
                    sh """
                        docker compose -f ${DOCKER_COMPOSE_FILE} up -d
                        docker ps
                    """
                }
            }
        }

        stage('Security Scan with Snyk') {
            steps {
                withCredentials([string(credentialsId: 'snyk-api-token', variable: 'SNYK_TOKEN')]) {
                    sh '''
                        snyk auth $SNYK_TOKEN
                        snyk test --severity-threshold=medium
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                // Clean up unused Docker resources (remove unused images, containers, volumes)
                sh 'docker system prune -f'
            }
        }
    }

    post {
        always {
            // Clean up decrypted secrets file after the pipeline finishes
            sh 'rm -f secrets.yaml'

            // Additional post steps (e.g., sending notifications) can go here
        }
    }
}
