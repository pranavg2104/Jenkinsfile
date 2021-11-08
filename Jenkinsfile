pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
            script{
                    //def path ='[]'
                    //path = readJSON file : "${D:/jenkinsProject}\\location.json"
                    sh "chmod +x -R ${env.WORKSPACE}"
                    sh """./Jenkinsfile/helloworld.py"""
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
