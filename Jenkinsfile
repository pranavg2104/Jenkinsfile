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
//        mail to: 'pranav.govekar@kpit.com', cc: 'abdul.akram@kpit.com',
//           subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
//           body: "${env.BUILD_URL} has result ${currentBuild.result}"       
        emailext attachLog: true, body: "${PROJECT_NAME} - Build # ${BUILD_NUMBER} - ${BUILD_STATUS}: Check console output at $BUILD_URL to view the results." , subject: "${PROJECT_NAME} - Build # ${BUILD_NUMBER} - ${BUILD_STATUS}!", 
            to: 'pranav.govekar@kpit.com pranavg2104@gmail.com'
    }
  }
    }
