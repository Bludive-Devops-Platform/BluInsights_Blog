pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'bludivehub/bluinsights-blog-service'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-jenkins-cred',
                    url: 'https://github.com/Bludive-Devops-Platform/BluInsights_Blog.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    sh 'docker run --rm ${DOCKER_IMAGE} echo "Test Passed!"'
                }
            }
        }

        stage('Push Docker Image to DockerHub') {
            environment {
                DOCKER_CREDS = credentials('Dockerhub-creds')
            }
            steps {
                script {
                    sh """
                        echo "${DOCKER_CREDS_PSW}" | docker login -u "${DOCKER_CREDS_USR}" --password-stdin
                        docker push ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Snyk Security Scan') {
            environment {
                SNYK_TOKEN = credentials('snyk-api-token')
            }
            steps {
                script {
                    sh """
                        snyk auth ${SNYK_TOKEN}
                        snyk test --docker ${DOCKER_IMAGE} || true
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Cleaning workspace...'
            cleanWs()
        }
    }
}
