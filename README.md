# aws_serverless_sample
PipeLine CI/CD required
use docker container => nikolaik/python-nodejs:python3.9-nodejs16
or you can run localy
install Nodejs
install serverlss => npm i serverless
install serverless-python-requirements => serverless plugin install -n serverless-python-requirements
add your requirements in requirement.txt => pip freeze > requirement.txt
set your ACCESS TOKEN and Secret access key => https://www.serverless.com/framework/docs/providers/aws/guide/credentials/
create your handler
add your handler to serverless.yml
run "serverless deploy"