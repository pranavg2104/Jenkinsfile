pipeline {
    agent any
        stages {
            stage('mil-sil-testing') {
                steps{
                    script{
                        bat """ python helloworld.py"""                   
                        echo 'MIL SIL TESTING...'
                        }
                    }
                }
            stage('report-email-notification'){
                steps{
                    script{
                        emailext attachLog: true, body: '''$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: Check console output at $BUILD_URL to view the results.''', 
                            subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS! has result ${currentBuild.result}', 
                            to: 'pranav.govekar@kpit.com pranavg2104@gmail.com'
                        echo 'report-email-notification....'
                    }
                }
            }
            stage('post-clean'){
                steps{
                    script{
                        echo 'POST CLEAN...'
                    }
                }
            }
        }
   }
