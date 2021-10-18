pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script{
                    def path =[]
                    path = readJSON file : "$ {}"
                    bat "python newDelFile.py"
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
