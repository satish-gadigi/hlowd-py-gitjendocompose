pipeline {

	//agent { label 'lbl_agent_node' }

	agent any
		stages {
			stage('Checkout') {
				steps {

					checkout([$class: 'GitSCM',
							branches: [[name: '*/main']],
							userRemoteConfigs: [[url: 'https://github.com/satish-gadigi/hlowd-py-gitjendocompose']]
					])
				}
			}
			// git 'https://github.com/satish-gadigi/Hello-World.git'


			stage('Build') {
				steps {
					sh 'docker build -t satishri/hlowd-py-gitjendocompose:${BUILD_NUMBER} .'
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
							sh 'docker tag satishri/hlowd-py-gitjendocompose:${BUILD_NUMBER} satishri/hlowd-py-gitjendocompose:latest'
							sh 'docker push satishri/hlowd-py-gitjendocompose:latest'
					}
				}
			}
			stage('Cleanup Old Containers basedon port') {
				steps {
					sh '''
					# Stop and remove container if it already running on 8080 port

						docker ps -q --filter "publish=8080" | xargs -r docker rm -f

					# Stop existing stack if running

						docker-compose -f docker-compose.yml down || true
						'''
				}
			}

			//stage('Deploy')	{
			//	steps {
			//sh 'docker run -d --name helloworldappusingjenkins -p 8081:8080 satishri/hello-world:latest'
			//}
			//}
			stage('Deploy with Docker-Compose') {
				steps {
					sh '''

						# Start new stack
						docker-compose -f docker-compose.yml up -d --build
						'''
				}
			}		
		}
}
