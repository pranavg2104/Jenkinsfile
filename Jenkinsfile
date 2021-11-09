pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                sh """chmod +x -R ${env.WORKSPACE}"""
                sh 'docker build -t helloworld.py'
                sh 'docker run --rm helloworld.py'
                //stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
