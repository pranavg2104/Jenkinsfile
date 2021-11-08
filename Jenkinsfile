pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
            script{
                    sh"""#!/usr/bin/env python"""
                    sh """chmod +x -R ${env.WORKSPACE}"""
                    //def path ='[]'
                    //path = readJSON file : "./location.json"
                    
                    sh  """chmod u+rx ./newDelFile.py"""
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
