pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
            script{
                    //def path ='[]'
                    //path = readJSON file : "${D:/jenkinsProject}\\location.json"
                sh """${WORKSPACE}/Jenkinsfile/python helloworld.py"""
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
