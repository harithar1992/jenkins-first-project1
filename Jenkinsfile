
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        -t jenkins-python-app:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker image inspect jenkins-python-app:${BUILD_NUMBER}'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Tests passed and Docker image built!'
        }
        failure {
            echo 'FAILURE: Check Console Output for the error.'
        }
    }
}

