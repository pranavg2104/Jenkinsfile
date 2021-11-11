pipeline {
    agent any
        stages {
            stage('Build') {
                steps{
                    script{
                        sh """FROM python:2.7
                              RUN yum -y install python
                              RUN yum -y install epel-release && yum clean all  
                              RUN yum -y install python-pip && yum clean all"""
                        echo 'Hello World'
                        sh """chmod +x -R ${env.WORKSPACE}"""
                        sh 'python ./helloworld.py'
                                    //def path ='[]'
                        //path = readJSON file : "./location.json
                        //sh """chmod u+rx ./newDelFile.py"""
                        echo 'Building..'
                        }
                    }
                }
            }
    }
