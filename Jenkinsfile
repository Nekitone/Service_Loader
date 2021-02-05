pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose up --built --abort-on-container-exit'
            }
       
    }
}
}
