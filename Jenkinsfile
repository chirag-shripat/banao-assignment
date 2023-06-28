pipeline {
    agent any
    
    stages {
        stage('Git pull') {
            steps {
                git branch: 'main', url: 'https://github.com/chirag-shripat/banao-assignment.git'
            }
        }
        
        stage('run python file') {
            steps {
                sh 'python file.py'
            }
        }
    }
    
    
}
