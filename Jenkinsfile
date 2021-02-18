pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/docker-compose build'
                sh '/usr/local/bin/docker-compose run serviceloader python manage.py makemigations
                sh '/usr/local/bin/docker-compose run serviceloader python manage.py migate importer
            }
        }
        stage('test') {
            steps {
                sh '/usr/local/bin/docker-compose run serviceloader python manage.py test importer --keepdb'
            }
        }
    }
}
