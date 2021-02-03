pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose -f docker-compose.yml up'
            }
       
    }
}
}
