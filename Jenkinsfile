pipeline {
    agent {
        label 'docker'
    }

    stages {
        stage('Build') {
            steps{
                script{
                    
                    sh """chmod +x -R ${env.WORKSPACE}"""
                    sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python ./newDelFile.py'
                    //def path ='[]'
                    //path = readJSON file : "./location.json                
                    //sh  """chmod u+rx ./newDelFile.py"""
                    echo 'Building..'
            }
        }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
        
}
