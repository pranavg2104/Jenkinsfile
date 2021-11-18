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
                        sh 'python helloworld.py'
                    }
                }
            }
        }
    post {
    always {
       emailext attachlog: true, to: 'rogerace339@gmail.com',
          subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
          body: "${env.BUILD_URL} has result ${currentBuild.result}"
    }
  }
    }
