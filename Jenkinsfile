pipeline {
    agent any

    environment {
        // Set up Docker Image name
        DOCKER_IMAGE = 'bludivehub/bluinsights-blog-service'  // Aligning with your DockerHub repo
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

        stage('Decrypt Secrets') {
            steps {
                script {
                    // Decrypt secrets using SOPS
                    sh 'sops -d secrets.yaml.enc > secrets.yaml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Use Docker to build the image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    // Test the Docker image by running a container
                    sh 'docker run --rm ${DOCKER_IMAGE} echo "Test Passed!"'
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Docker login
                    def dockerHubUsername = sh(script: "cat secrets.yaml | grep dockerhub | awk '{print \$2}'", returnStdout: true).trim()
                    def dockerHubPassword = sh(script: "cat secrets.yaml | grep dockerhub | awk '{print \$4}'", returnStdout: true).trim()

                    // Login to DockerHub
                    sh "docker login -u ${dockerHubUsername} -p ${dockerHubPassword}"

                    // Push the Docker image to DockerHub
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            // Clean up decrypted secrets file for security reasons
            sh 'rm -f secrets.yaml'
        }
    }
}
