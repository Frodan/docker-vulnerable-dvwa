pipeline {
  agent any
  environment {
    USER_LOGIN = 'test'
    USER_PASS = 'test'
  }
  stages {
    stage('Secrets Scan'){
      agent any
      steps{
        sh 'docker run -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/Frodan/docker-vulnerable-dvwa'
      }
    }
    stage('SAST'){
      agent any
      steps{
        withCredentials([string(credentialsId: 'sonarToken', variable: 'SONAR_TOKEN')]){
          sh "docker run -e SONAR_HOST_URL=http://localhost:9000 -v \"\${PWD}:/usr/src\" --net=\"host\" \
                                    sonarsource/sonar-scanner-cli \
                                    -Dsonar.projectKey=Thesis \
                                    -Dsonar.sources=. \
                                    -Dsonar.projectName=Thesis_Project \
                                    -Dsonar.login=${SONAR_TOKEN}"
        }
      }
    }
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build . --file Dockerfile --tag frodan/thesis_project'
      }
    }
    stage('Deploy'){
      agent any
      steps{
        sh 'docker stop thesis_project'
        sh 'docker run --rm --name thesis_project -d -p 80:80 vulnerables/web-dvwa'
      }
    }
//     stage('Docker Push') {
//       agent any
//       steps {
//         withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
//           sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
//           sh 'docker push frodan/dev_ops:latest'
//         }
//       }
//     }
  }
}