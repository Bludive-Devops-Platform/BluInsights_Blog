// utils.groovy
def versionTag(String serviceName) {
    return "${serviceName}:${env.BUILD_NUMBER}"
}

return this

