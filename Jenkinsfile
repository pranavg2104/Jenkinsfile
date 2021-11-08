pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
                script{
                    
                    sh """chmod +x -R ${env.WORKSPACE}"""
                    sh 'C:\Program Files\Python39\Scripts ./newDelFile.py'
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
