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
                        echo 'report-generation'
                      
                        def paths = '[]' 
                        paths = readJSON file: "${WORKSPACE}\\location.json"
                        
                        emailext attachLog: false, body: '''$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: Check console output at $BUILD_URL to view the results.''', 
                            subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', 
                            to: "${emails}"
                       
                        
                    }
                }
            }
        }
    post{
        always{
             
             cleanWs cleanWhenSuccess: false, notFailBuild: true
            //will clean the workspace if any of previous stage fails, not build, aborted or unstable
        }
    }
}
