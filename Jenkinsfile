pipeline {
    
//agent { label 'lbl_agent_node' }

agent any
    stages {
        stage('Checkout') {
            steps {

        checkout([$class: 'GitSCM',
            branches: [[name: '*/main']],
            userRemoteConfigs: [[url: 'https://github.com/satish-gadigi/Hello-World.git']]
        ])
    }
}
               // git 'https://github.com/satish-gadigi/Hello-World.git'
            
        

        stage('Build') {
            steps {
                sh 'docker build -t satishri/hello-world:${BUILD_NUMBER} .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-cred_id',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker tag satishri/hello-world:${BUILD_NUMBER} satishri/hello-world:latest'
                    sh 'docker push satishri/hello-world:latest'
                }
            }
        }
stage('Cleanup Old Container') {
            steps {
                sh '''
                # Stop and remove container if it already exists
                 docker rm -f helloworldappusingjenkins || true
docker ps -q --filter "publish=8080" | xargs -r docker rm -f
                '''
            }
        }

	stage('Deploy')	{
		steps {
sh 'docker run -d --name helloworldappusingjenkins -p 8081:8080 satishri/hello-world:latest'
}
		}
    }
}
