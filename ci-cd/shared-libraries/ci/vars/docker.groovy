// vars/docker.groovy

// Builds and scans Docker images
def buildAndScan(String imageTag, String dockerfilePath) {
    stage("Build Docker Image: ${imageTag}") {
        echo "Building Docker image: ${imageTag}"
        sh "docker build -t ${imageTag} ${dockerfilePath}"
    }

    stage("Scan Docker Image with Snyk: ${imageTag}") {
        echo "Scanning Docker image ${imageTag} for vulnerabilities"
        // Use string interpolation in a safe way
        sh "snyk container test ${imageTag} --severity-threshold=high"
    }
}

// Pushes Docker images to registry using Jenkins credentials
def pushImage(String imageTag, String registryCredentialsId) {
    stage("Push Docker Image: ${imageTag}") {
        echo "Pushing Docker image: ${imageTag}"
        withCredentials([usernamePassword(credentialsId: registryCredentialsId, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            sh """
            echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin
            docker push ${imageTag}
            """
        }
    }
}

return this

