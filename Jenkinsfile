pipeline {
    agent any
    
    environment{
        def paths = '[]' 
        paths = readJSON file: "${WORKSPACE}\\location.json"
    }
        
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
                    }
                }
            }
        }
    post{
        always{                        
                emailext attachLog: false, body: '''$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: Check console output at $BUILD_URL to view the results.''', 
                        subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', 
                        to: "${paths.emails}"
              
           
//                 echo 'Check the jenkinslog for the error, File not found or the email format error'
//                 skipRemainingStages = true
//                 echo "next stage skip: = ${skipRemainingStages}"
                                         
             cleanWs cleanWhenSuccess: false, notFailBuild: true
            //will clean the workspace if any of previous stage fails, not build, aborted or unstable
        }
    }
}
