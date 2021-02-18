pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/docker-compose build'
                sh '/usr/local/bin/docker-compose run serviceloader python manage.py makemigrations'
                sh '/usr/local/bin/docker-compose run serviceloader python manage.py migrate importer'
            }
        }
        stage('test') {
            steps {
                sh '/usr/local/bin/docker-compose run serviceloader python manage.py test importer --keepdb'
            }
        }
    }
}
