pipeline {
    agent any

    stages {
        stage('Verify Checkout') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Install Playwright Browser') {
            steps {
                sh '.venv/bin/python -m playwright install chromium'
            }
        }
        stage('Execute Tests') {
            steps {
                sh '.venv/bin/python -m pytest tests/test_dialogs_frames.py -v'
            }
        }
    }
}