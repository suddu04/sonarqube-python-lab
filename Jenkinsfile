
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Setup') {
            steps {
                echo 'Preparing Python project'
                sh 'python3 --version'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    script {
                        def qg = waitForQualityGate()

                        if (qg.status != 'OK') {
                            error "Quality Gate failed: ${qg.status}"
                        }

                        echo 'Quality Gate passed!'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Quality Gate passed. Continue with build.'
            }
        }
    }
}
