pipeline {
  agent any
  environment {
    USER_LOGIN = 'test'
    USER_PASS = 'test'
  }
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build . --file Dockerfile --tag frodan/thesis_project'
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