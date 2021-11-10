pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {
                sh 'pip install -r requirements.txt'
                sh """chmod +x -R ${env.WORKSPACE}"""
                sh 'python ./helloworld.py'
                //sh 'docker run --rm helloworld.py'
                //stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
