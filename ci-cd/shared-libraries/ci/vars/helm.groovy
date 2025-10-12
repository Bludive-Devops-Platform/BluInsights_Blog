// helm.groovy
def deployHelmChart(String releaseName, String chartPath, String namespace, Map values = [:]) {
    stage("Deploy Helm Chart: ${releaseName}") {
        def valuesArgs = values.collect { k,v -> "--set ${k}=${v}" }.join(' ')
        sh "helm upgrade --install ${releaseName} ${chartPath} -n ${namespace} ${valuesArgs} --wait"
    }
}

return this

