pipeline {
    agent any  
    environment {
        def data = readJSON file:'location.json'
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
                        echo "${data.emails}"
                         
                        try{
//                          def paths = '[]' 
//                          paths = readJSON file: "${WORKSPACE}\\location.json"
                        
                         emailext attachLog: false, body: '''$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS: Check console output at $BUILD_URL to view the results.''', 
                            subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', 
                            to: "${data.emails}"
                        }
                        catch(err){
                             echo 'File not found or the email format error'
                             skipRemainingStages = false
                             echo "next stage skip: = ${skipRemainingStages}"   
                        }
                    }
                }
            }
            stage('cleaning-stage'){
                steps{
                    cleanWs cleanWhenSuccess: false, notFailBuild: true
                }
            }
        }
    
}
