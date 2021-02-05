pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/docker-compose up -d --built --abort-on-container-exit'
            }
       
    }
}
}
