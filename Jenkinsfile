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
          sh "docker run -e SONAR_HOST_URL=http://localhost:9000 -v \"/home/frodan/jenkins/workspace/Thesis_master@2:/usr/src\" --net=\"host\" \
                                    sonarsource/sonar-scanner-cli \
                                    -Dsonar.projectKey=Thesis \
                                    -Dsonar.sources=. \
                                    -Dsonar.projectName=Thesis_Project \
                                    -Dsonar.login=${SONAR_TOKEN}"
        }
      }
    }
    stage ('Dockerfile Check'){
      agent any
      steps{
        sh 'docker run -v /home/frodan/jenkins/workspace/Thesis_master@2:/myapp aquasec/trivy conf /myapp'
      }
    }

    stage('Docker Build and Push') {
      agent any
      steps {
        sh 'docker build . --file Dockerfile --tag frodan/thesis_project'
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push frodan/thesis_project'
        }
      }
    }


    stage('Deploy'){
      agent any
      steps{
        sh 'docker stop thesis_project'
        sh 'docker run --rm --name thesis_project -d -p 80:80 frodan/thesis_project'
//         sh 'curl -d "create_db=Create+%2F+Reset+Database" -X POST http://172.17.0.1/setup.php'
      }
    }
    stage('DAST') {
      agent any
      steps{
      sh '''
        mkdir -p $PWD/reports $PWD/artifacts;
        docker run \
            -v $PWD/reports:/arachni/reports --net=\"host\" ahannigan/docker-arachni \
            bin/arachni http://project.local  --plugin=autologin:url=http://project.local/login.php,parameters="username=admin&password=password&Login=Login&user_token=fbd9ba9b1d25da438853d66e3e34b065",check="logout.php" --scope-exclude-pattern=Logout --report-save-path=reports/project.local.afr;
        docker run --name=arachni_report  \
            -v $PWD/reports:/arachni/reports ahannigan/docker-arachni \
            bin/arachni_reporter reports/project.local.afr --reporter=html:outfile=reports/project-local-report.html.zip;
        docker cp arachni_report:/arachni/reports/project-local-report.html.zip $PWD/artifacts;
        docker rm arachni_report;
      '''
      archiveArtifacts artifacts: 'artifacts/**', fingerprint: true
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