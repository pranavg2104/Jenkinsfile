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
                        emailext attachLog: true, body: 'Build Information', subject: 'Build Information', to: 'pranavgovekar2015@gmail.com'
                    }
                }
            }
        }
    }
