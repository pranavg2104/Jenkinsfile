pipeline {
    agent any
        stages {
            stage('Build') {
                /*agent{
                    label 'docker' {
                        iamge 'python:latest'
                    }
                }*/
                steps{
                    script{
                        echo 'Hello World'
                        //sh 'yum install python'
                        sh 'Dockerfile'
                        sh 'chmod +x -R ${env.WORKSPACE}'
                        sh './usr/localpython.exe ./helloworld.py'
                                    //def path ='[]'
                        //path = readJSON file : "./location.json
                        //sh """chmod u+rx ./newDelFile.py"""
                        echo 'Building..'
                        }
                    }
                }
            }
    }
