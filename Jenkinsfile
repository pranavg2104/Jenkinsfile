pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script{
                    def path ='[]'
                    path = readJSON file : "$ {D:\jenkinsProject}\\location.json"
                    bat """python "${path.build.location}newDelFile.py"""
                    echo 'Building..'
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
