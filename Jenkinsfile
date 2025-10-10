pipeline {
    agent any

    environment {
        DOCKERHUB_NAMESPACE = 'bludivehub'
    }

    stages {

        /* ==============================
           1. CHECKOUT SOURCE CODE
        ============================== */
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-jenkins-cred',
                    url: 'https://github.com/Bludive-Devops-Platform/BluInsights_Blog.git'
            }
        }

        /* ==============================
           2. BUILD & PUSH DOCKER IMAGES
        ============================== */
        stage('Build and Push Docker Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh '''
                        echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin

                        # Build and push all four services
                        docker build -t ${DOCKERHUB_NAMESPACE}/bluinsights-user-service:latest ./backend/user-service
                        docker push ${DOCKERHUB_NAMESPACE}/bluinsights-user-service:latest

                        docker build -t ${DOCKERHUB_NAMESPACE}/bluinsights-blog-service:latest ./backend/blog-service
                        docker push ${DOCKERHUB_NAMESPACE}/bluinsights-blog-service:latest

                        docker build -t ${DOCKERHUB_NAMESPACE}/bluinsights-comment-service:latest ./backend/comment-service
                        docker push ${DOCKERHUB_NAMESPACE}/bluinsights-comment-service:latest

                        docker build -t ${DOCKERHUB_NAMESPACE}/bluinsights-frontend-service:latest ./frontend
                        docker push ${DOCKERHUB_NAMESPACE}/bluinsights-frontend-service:latest
                    '''
                }
            }
        }

        /* ==============================
           3. TEST DEPLOYMENT WITH DOCKER COMPOSE
        ============================== */
        stage('Test Docker Images') {
            steps {
                sh '''
                    docker compose -f docker-compose.yaml up -d
                    sleep 10
                    docker ps
                '''
            }
        }

        /* ==============================
           4. SECURITY SCAN WITH SNYK
        ============================== */
        stage('Security Scan with Snyk') {
            steps {
                withCredentials([string(credentialsId: 'snyk-api-token', variable: 'SNYK_TOKEN')]) {
                    sh '''
                        snyk auth $SNYK_TOKEN
                        
                        # Scan all container images for vulnerabilities
                        snyk container test ${DOCKERHUB_NAMESPACE}/bluinsights-user-service:latest --file=backend/user-service/Dockerfile --severity-threshold=medium || true
                        snyk container test ${DOCKERHUB_NAMESPACE}/bluinsights-blog-service:latest --file=backend/blog-service/Dockerfile --severity-threshold=medium || true
                        snyk container test ${DOCKERHUB_NAMESPACE}/bluinsights-comment-service:latest --file=backend/comment-service/Dockerfile --severity-threshold=medium || true
                        snyk container test ${DOCKERHUB_NAMESPACE}/bluinsights-frontend-service:latest --file=frontend/Dockerfile --severity-threshold=medium || true
                    '''
                }
            }
        }

        /* ==============================
           5. CLEANUP
        ============================== */
        stage('Clean Up') {
            steps {
                sh '''
                    docker compose down || true
                    docker system prune -f || true
                '''
            }
        }

        /* ==============================
           6. DEPLOY TO KUBERNETES
        ============================== */
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([kubeconfigFile(credentialsId: 'kubeconfig-cred', variable: 'KUBECONFIG')]) {
                    sh '''
                        echo "Deploying to Kubernetes cluster..."
                        kubectl apply -f k8s-manifests/namespace.yaml
                        kubectl apply -f k8s-manifests/
                        echo "Waiting for rollout to complete..."
                        kubectl rollout status deployment/frontend-service -n bluinsights
                        echo "✅ Deployment to Kubernetes successful!"
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed (success or failure).'
        }
        success {
            echo '🎉 All stages executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for details.'
        }
    }
}
