pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
                script{
                    echo 'Hello World'                   
                    sh """chmod +x -R ${env.WORKSPACE}"""
                    cd ../
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
