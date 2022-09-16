# GIC CODE TO IMPACT Hackathon 2022

## Notes
Here I list 4 architectures, I strongly recommend architecture 4 or use architecture 1 or 2 as back up, because other architectures have their own problems like shit (I apologize I use this word), such as HTTPS interacting with HTTP, SSL Certificate issues, Cross-origin Resource Sharing issues, etc, it took me a lot of time to solve, I don't think we should waste time dealing with these stupid things caused by AWS.

* Architecture 1 (Backup):
    1. EC2 Host React Web
    2. EC2 Host Python backend
    3. RDS for Relational Data
    4. DynamoDB for NoSQL Data
    5. SageMaker for data analysis
* Architecture 2 (Can work):
    1. EC2 Host React Web
    2. Beanstalk Host Python backend
    3. RDS for Relational Data
    4. DynamoDB for NoSQL Data
    5. SageMaker for data analysis
* Architecture 3 (Not recommended):
    1. EC2 Host React Web
    2. Application Load Balancer + Lambda Host Python backend
    3. RDS for Relational Data
    4. DynamoDB for NoSQL Data
    5. SageMaker for data analysis
* Architecture 4 (Recommended):
    1. Amplify Host React Web
    2. API Gateway + Lambda Host Python backend
        * Application Load Balancer (Can also be used for same simple APIs)
    3. RDS for Relational Data
    4. DynamoDB for NoSQL Data
    5. SageMaker for data analysis

Currently I am using my own AWS account for testing, I released 4 IAM accounts under my account with full permission for backup tomorrow, if we get in trouble when using the AWS account they provided, I think we can just use my account. I have $100 credits and I think it should be enough for it.

## Amplify
I also tried to host a web developed by react using AWS Amplify and GitHub, it is quite smooth and easy to use. https://github.com/HolmesJJ/gic-hackathon-amplify

You may test it under the link below:
* https://master.d342064p5w74fc.amplifyapp.com/
* username: hjj / kk / lwk / yzl / hx
* password: 123456

## Lambda
I created 4 functions using lambda
* login: enter username and password to login (post testing)
* train: get sample training dataset (post testing)
* test: get sample test dataset (post testing)
* hello-world: for simple testing (get/post testing)

## API Gateway
I created 3 APIs based on the lambda
* login (post): https://3e6ew7430f.execute-api.ap-southeast-1.amazonaws.com/login
    ```
    {
        "name": "hjj",
        "password": "123456"
    }
    ```
* train (post): https://tlggiqgf4f.execute-api.ap-southeast-1.amazonaws.com/train
    * Body is optional
    ```
    {
        "Id": 7,
    }
    ```
* test (post): https://7e9422lvm2.execute-api.ap-southeast-1.amazonaws.com/test
    * Body is optional
    ```
    {
        "Id": 1500,
    }
    ```

## Application Load Balancer
I created 1 API based on application load balancer (ALB)
* hello-world: http://hello-world-1242084238.ap-southeast-1.elb.amazonaws.com

## EC2
I also tried to host a server using EC2 ubuntu
* http://13.214.158.192:5000/
    * login: http://13.214.158.192:5000/login
    ```
    {
        "name": "hjj",
        "password": "123456"
    }
    ```
* Configuration
    ```
    sudo apt-get install unzip
    sudo apt-get install tmux
    sudo apt-get install python3-pip

    ssh -i gic.pem ubuntu@ec2-13-214-158-192.ap-southeast-1.compute.amazonaws.com
    scp -i gic.pem beanstalk/app.zip ubuntu@ec2-13-214-158-192.ap-southeast-1.compute.amazonaws.com:~/.
    pip install -r requirements.txt

    tmux new -s gic-hackathon
    python3 application.py

    tmux attach -t gic-hackathon
    ```

## Beanstalk
I also tried to host a server using Beanstalk
* Need to take note the TRICKS (shit) below
    * requirements.txt must be included
    * `application.py` is fixed
    * `application` under flask is fixed
* http://gic-env.eba-pi4mfuxe.ap-southeast-1.elasticbeanstalk.com/
    * login: http://13.214.158.192:5000/login
    ```
    {
        "name": "hjj",
        "password": "123456"
    }
    ```

## DynamoDB
I strongly recommend using DynamoDB for CSV or JSON, you can just simply upload and use lambda to handle the data. I strongly non recommend
RDS for CSV or JSON, it is super trouble to save or load the data.
* Configuration: IAM between Lambda and DynamoDB  
    ```
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:UpdateItem"
            ],
            "Resource": "YOUR-TABLE-ARN"
        }
        ]
    }
    ```

Currently the train and test sample data mentioned above are stored in DynamoDB.

## RDS
I tried to use RDS to store the user data for the login function.

## S3
All the resources like images, csv files, model files can be stored here.
* Need to take note the TRICKS (shit) below
    * Set all the resources to be public, can use the configuration below
* Configuration
    ```
    {
        "Version": "2008-10-17",
        "Statement": [
            {
                "Sid": "AllowPublicRead",
                "Effect": "Allow",
                "Principal": {
                    "AWS": "*"
                },
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::gic-hackathon/*"
            }
        ]
    }
    ```

## SageMaker
I strongly recommend using SageMaker rather than Glue, it is super hard to handle the permission issue of Glue. And I tried to use SageMaker to train a model an it can be save to S3 programmatically.

## Local Environment
* Python 3.7.10
```
conda create --name gic-hackathon python=3.7.10
```
