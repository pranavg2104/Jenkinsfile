pipeline {
    agent none
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:alpine'
                    args '-u root'
                }
            }
            steps {
                //sh """chmod +x -R ${env.WORKSPACE}"""
                sh 'python --version'
                //stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
