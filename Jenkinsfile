pipeline {
    agent any
        stages {
            stage('Build') {
                steps{
                    script{
                        bat """ python helloworld.py"""                   
                        echo 'Building..'
                        }
                    }
                }
            stage('Test'){
                steps{
                    script{
                        echo 'Testing...'
                    }
                }
            }
            stage('Deploy'){
                steps{
                    script{
                        echo 'Deploying...'
                        //emailext attachLog: true, body: 'Build INFO', subject: 'Build INFO', to: 'pranavgovekar2015@gmail.com'
                        //mail bcc: '', body: 'BUILD INFO', cc: '', from: '', replyTo: '', subject: 'BUILD INFO', to: 'pranavgovekar2015@gmail.com'
                        emailext attachLog: true, body: 'Build INFO', subject: 'Build INFO', to: 'rogerace339@gmail.com'
                    }
                }
            }
        }
    }
