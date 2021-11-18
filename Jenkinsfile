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
                        //emailext attachLog: true, body: 'Build INFO', subject: 'Build INFO', to: 'rogerace339@gmail.com'
                        //mail bcc: '', body: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', cc: '', from: '', replyTo: '', subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', to: 'pranavgovekar2015@gmail.com'
                    }
                }
            }
        }
    post {
    always {
       mail to: 'rogerace339@gmail.com', cc: 'pranavgovekar2015@gmail.com',
          subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
          body: "${currentBuild.log} has result ${currentBuild.result}"
    }
  }
    }
