pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Verify') {
      steps {
        echo 'BluInsights Blog code pulled successfully!'
      }
    }
  }
}
