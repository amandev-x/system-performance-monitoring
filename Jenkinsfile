// This is an Jenkins CI/CD pipeline script for building, testing, and deploying a system performance monitoring application.

pipeline{
    agent any

    stages{
        // Stage for checking out the code from the repository

        stage("Checkout Code"){
            steps{
                checkout scm 
            }
        }

        // Stage for building the application
        stage("Build Application"){
            steps{
                script {
                     sh 'python3 -m venv .venv'
                     sh 'source .venv//bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage("Run the application"){
            steps{
                sh 'source .venv/bin/activate && python3 monitor.py &'
            }
        }

        stage("Summary"){
            steps{
                echo "System Performance Monitoring Application is up and running."
            }
        }
    }
}