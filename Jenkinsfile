pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                any {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m ./newDelFile.py' 
                //stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
