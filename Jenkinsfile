pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
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
