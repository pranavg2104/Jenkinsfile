pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
                script{
                    echo 'Hello World'                   
                    //sh """chmod +x -R ${env.WORKSPACE}"""
                    //sh 'cd C:/Python python./newDelFile.py'
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
