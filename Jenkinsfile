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
                        try{
                         def paths = '[]' 
                         paths = readJSON file: "${WORKSPACE}\\location.json"
                        
                         emailext attachLog: false, body: '''$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: Check console output at $BUILD_URL to view the results.''', 
                            subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', 
                            to: "${paths.emails}"
                        }
                        catch(err){
                             echo 'File not found or the email format error'
                             skipRemainingStages = true
                             echo "next stage skip: = ${skipRemainingStages}"   
                        }
                    }
                }
            }
            stage('cleaning-stage'){
                steps{
                    cleanWs notFailBuild: true
                }
            }
        }
    
}
