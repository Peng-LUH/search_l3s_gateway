pipeline {

	agent any
	
	environment {
        DEMO_SERVER = 'staging.sse.uni-hildesheim.de'
        DEMO_SERVER_USER = "elscha"
        
        dockerImage = ''
        REMOTE_UPDATE_SCRIPT = '/staging/update-compose-project.sh search-l3s'
    }

    stages {

        stage('Git') {
            steps {
                cleanWs()
                git branch: 'main', url: 'https://github.com/e-Learning-by-SSE/search-l3s_gateway-service.git'
            }
        }
		
		stage('Check') {
            steps {
                sh 'python3 -m py_compile *.py'
            }
        }
		
		stage('Build') {
            steps {
                script {
                    // Based on:
                    // - https://e.printstacktrace.blog/jenkins-pipeline-environment-variables-the-definitive-guide/
                    // - https://stackoverflow.com/a/13245961
                    // - https://stackoverflow.com/a/51991389
                    env.API_VERSION = sh(script: 'grep -Po "(?<=    version=\\").*(?=\\",)" setup.py', returnStdout: true).trim()
                    echo "API: ${env.API_VERSION}"
                    dockerImage = docker.build 'e-learning-by-sse/search-l3s_gateway-service'
                    docker.withRegistry('https://ghcr.io', 'github-ssejenkins') {
                        dockerImage.push("${env.API_VERSION}")
                        dockerImage.push('latest')
                    }
                }
            }
        }
				
        // Based on: https://medium.com/@mosheezderman/c51581cc783c
        //stage('Deploy') {
        //    steps {
        //        sshagent(['STM-SSH-DEMO']) {
        //            sh "ssh -o StrictHostKeyChecking=no -l ${DEMO_SERVER_USER} ${env.DEMO_SERVER} bash ${REMOTE_UPDATE_SCRIPT}"
        //        }
        //    }
        //}
    }
}