pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yaml'
        DOCKERHUB_CREDS = credentials('Dockerhub-creds')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-jenkins-cred', url: 'https://github.com/Bludive-Devops-Platform/BluInsights_Blog.git', branch: 'main'
            }
        }

        stage('Build and Push Docker Images') {
            steps {
                script {
                    // Login to DockerHub
                    sh """
                        echo '${DOCKERHUB_CREDS_PSW}' | docker login -u '${DOCKERHUB_CREDS_USR}' --password-stdin
                    """

                    // Build all the images using Docker Compose
                    sh """
                        docker compose -f ${DOCKER_COMPOSE_FILE} build
                    """

                    // Push all the images to DockerHub
                    sh """
                        docker compose -f ${DOCKER_COMPOSE_FILE} push
                    """
                }
            }
        }

        stage('Test Docker Images') {
            steps {
                script {
                    // Test all services after building, using a simple test container run
                    sh """
                        docker compose -f ${DOCKER_COMPOSE_FILE} up -d
                        docker ps  # Check if the services are running
                    """
                }
            }
        }

        stage('Security Scan with Snyk') {
            steps {
                script {
                    // Run security scan with Snyk on all images (build and push will be scanned)
                    sh """
                        snyk container test --all-projects
                    """
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    // Clean up containers and volumes to save space
                    sh """
                        docker compose -f ${DOCKER_COMPOSE_FILE} down --volumes --rmi all
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}
