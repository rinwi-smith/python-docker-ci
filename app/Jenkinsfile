pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'rinwismith/python-docker-ci'
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rinwi-smith/python-docker-ci.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_HUB_REPO)
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', DOCKER_HUB_CREDENTIALS) {
                        docker.image(DOCKER_HUB_REPO).push('latest')
                    }
                }
            }
        }
    }
}
