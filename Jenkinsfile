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
                        bat"""python helloworld.py"""
                    }
                }
            }
        }
    post {
    always {
       mail to: ['pranav.govekar@kpit.com','abdul.akram@kpit.com'],
          subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
          body: "${env.BUILD_URL} has result ${currentBuild.result}"
    }
  }
    }
