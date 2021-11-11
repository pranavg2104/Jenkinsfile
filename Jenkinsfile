pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                sh 'sudo apt-get install pip'
                sh """chmod +x -R ${env.WORKSPACE}"""
                sh 'python ./helloworld.py'
                //sh 'docker run --rm helloworld.py'
                //stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
