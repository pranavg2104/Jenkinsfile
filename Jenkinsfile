pipeline {
    agent{
        docker { 
            image 'python:3.5.1' 
        }
    }

    stages {
        stage('Build') {
            steps{
                script{
                    
                    sh """chmod +x -R ${env.WORKSPACE}"""
                    sh './newDelFile.py'
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
