pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/docker-compose --build'
            }
        }
        stage('test')
            steps {
                sh '/usr/local/bin/docker-compose run web python manage.py test importer'
    }
}
}

