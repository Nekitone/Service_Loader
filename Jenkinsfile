pipeline {
    agent { label 'docker' }
    triggers {
        bitbucketPush()
    }
    environment {
        // Specify your environment variables.
        APP_VERSION = '1'
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose -f docker-compose.yml up'
            }
       
    }
}
}
