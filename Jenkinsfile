pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/docker-compose up --built'
                sh '/usr/local/bin/docker-compose up'
            }
       
    }
}
}
