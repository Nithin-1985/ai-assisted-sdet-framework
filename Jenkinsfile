pipeline {
    agent any

    environment {
        BASE_URL = 'https://jsonplaceholder.typicode.com'
        API_USERNAME = 'testuser'
        API_PASSWORD = 'test123'
        BROWSER = 'chromium'
        ENVIRONMENT = 'CI'
    }


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

    post {
    always {
        archiveArtifacts artifacts: 'allure-results/**',
                         allowEmptyArchive: true

        allure([
            results: [[path: 'allure-results']],
            reportBuildPolicy: 'ALWAYS'
        ])
    }
    }
}