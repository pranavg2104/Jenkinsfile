pipeline {
    agent any 
    stages {
        stage('Build') { 
            agent {
                any {
                    image 'python: 4246fb19839f' 
                }
            }
            steps {
                sh './newDelFile.py' 
                //stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}
