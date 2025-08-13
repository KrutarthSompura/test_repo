pipeline {
    agent any
    stages{
        satge('Checkout Code'){
            steps{
                git 'https://github.com/KrutarthSompura/test_repo'
            }
        }
        stage('Build'){
            steps{
                sh 'echo "Building the application"'
            }
        }
        stage('Test'){
            steps{
                sh 'echo "Running tests"'
            }
        }
        stage('Deploy'){
            steps{
                sh 'echo "Deploying"'
            }
        }
    }
}
