pipeline {
    agent any
        stages {
            stage('Build') {
                steps{
                    script{
                        bat """ python newDelFile.py"""                   
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
                    }
                }
            }
        }
    }
