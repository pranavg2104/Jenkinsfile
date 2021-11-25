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
            stage('report-generation'){
                steps{
                    script{
                        echo 'report-generation'
                    }
                }
            }
        }
    post{
        always{
             emailext attachLog: false, body: '''$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: Check console output at $BUILD_URL to view the results.''', 
                            subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', 
                            to: 'pranav.govekar@kpit.com pranavg2104@gmail.com'
             cleanWs cleanWhenSuccess: false, notFailBuild: true
            //will clean the workspace if any of previous stage fails, not build, aborted or unstable
        }
    }
}
