pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh """chmod +x -R ${env.WORKSPACE}"""
                sh './helloworld.py' 
                //stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
