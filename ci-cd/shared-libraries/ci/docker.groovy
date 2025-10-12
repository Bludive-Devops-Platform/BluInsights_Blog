// docker.groovy
def buildAndScan(String serviceName, String dockerfilePath, String imageTag) {
    stage("Build Docker Image: ${serviceName}") {
        echo "Building Docker image: ${imageTag}"
        sh "docker build -t ${imageTag} ${dockerfilePath}"
    }

    stage("Scan Docker Image with Snyk: ${serviceName}") {
        echo "Scanning image ${imageTag} for vulnerabilities"
        sh "snyk container test $imageName:$tag --severity-threshold=high"
    }
}

def pushImage(String imageTag, String registryCredentialsId) {
    stage("Push Docker Image: ${imageTag}") {
        echo "Pushing Docker image: ${imageTag}"
        withCredentials([usernamePassword(credentialsId: registryCredentialsId, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            sh """
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push ${imageTag}
            """
        }
    }
}

return this

