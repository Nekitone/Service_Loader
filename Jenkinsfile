pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/docker-compose up --build --abort-on-container-exit'
            }
       
    }
}
}
