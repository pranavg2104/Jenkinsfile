pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
                script{
                    sh """chmod +x -R ${env.WORKSPACE}"""
                    //def path ='[]'
                    //path = readJSON file : "./location.json"
                    $ python newDelFile.py
                    
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
