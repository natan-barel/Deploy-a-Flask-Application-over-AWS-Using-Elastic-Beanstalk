
# Deploy a Flask Application over AWS Using Elastic Beanstalk

This project covers the step by step guide to deploy an e-learning course catalog website using the **AWS Elastic Beanstalk**. The website is developed using Flask. We'll use different AWS commands on the CLI. Throughout this project, we'll use EB CLI which creates AWS lambda functions, IAM users, API Gateways, EC2 instance, Load balancer, AWS CloudFormation stack, etc.

## AWS Services Used
+ AWS Elastic Beanstalk





### Task 1: AWS CLI Configuration

Begin by configuring AWS on the terminal to get programmatic access to its resources. For this task, generate the AWS `AccessKeyId` and `SecretAccessKey`. Then, use those keys to configure AWS.

For the sake of consistency, use `json` as the default output format.

For this task, perform the following steps:

+ Type the following command into the terminal: 
```shell
aws configure
```

+ After executing the command above, add the following parameters:
```shell
AWS Access Key ID [None]: <AccessKey>
AWS Secret Access Key [None]: <SecretAccessKey>
Default region name [None]: <YOUR_DEFAULT_REGION>
Default output format [None]: json
```

### Task 2: Set Up a Python Virtual Environment

Now, set up a virtual environment for Python using the `virtualenv` tool which can be used to manage Python packages.

For this task, perform the following steps:

+ Go to the `/usercode/elearning` directory and type the command below into the terminal. This will create the virtual environment, `virt`.

```shell
virtualenv virt
```
+ Type the following command into the terminal to activate this virtual environment:

```shell
source virt/bin/activate
```

### Task 3: Install the Dependencies

To deploy the Flask application to the virtual environment, install the necessary packages.

+ Install the `Flask` and `Flask-SQLAlchemy` packages in the environment.
+ An optional step is to enlist all the installed libraries, and verify if the above-mentioned libraries have been installed.
+ Create a new `requirements.txt` file in the `/usercode/elearning/` directory, and add all of the installed libraries into this file.

For this task, perform the following steps:

+ Type the following command into the terminal to install the `Flask` and `Flask-SQLAlchemy` libraries:

```shell
pip install flask==2.0.3 Flask-SQLAlchemy==2.5.1
```

+ An optional step is to type the following command to enlist all of the installed libraries:

```shell
pip freeze
```

+ Type the following command to add all of the enlisted libraries into the `/usercode/elearning/requirements.txt` file:

```shell
pip freeze > /usercode/elearning/requirements.txt
```

### Task 4: Elastic Beanstalk Initialization

To start deploying the `elearning` app to the AWS cloud, initialize the **EB CLI** repository. Provide a **name** for the application. Then, configure a default **key pair** to connect to the EC2 while following the prompts.

For this task, perform the following steps:

+ Type the following command into the terminal to initialize the EB CLI:

```shell
eb init -i
```

+ Specify the same default region that you added in “Task 1.”

+ Provide a new application name.

+ Use the `Python 3.8 running on 64bit Amazon Linux 2` option for the Python version of your application.

+ Set up access using the Secure Shell for the instances.

+ Select a key pair if you have one already, or select the `[ Create new KeyPair ]` option to create a new one. Follow the prompt and provide a name for it.

### Task 5: Deploy the Application

If the EB CLI has been initialized successfully, create an EB environment with the following resources:


+ EC2 instance
+ Instance security group
+ Load balancer
+ Load balancer security group
+ Auto scaling group
+ Amazon S3 bucket
+ Amazon CloudWatch alarms
+ AWS CloudFormation stack
+ Domain name

Now, deploy the application. Start by providing a new name for the environment. For the sake of consistency, name it `flask-env`.

For this task, perform the following steps:

+ Type the following command into the terminal to create a new EB environment named `flask-env`:

```shell
eb create flask-env
```

### Task 6: Verify the Deployment

Now, check the status of the newly created environment to extract the dynamic URL where the application was deployed, like this:

```shell
flask-env.eba-<random_string>.<your_default_region>.elasticbeanstalk.com
```

Use the EB CLI to get the dynamic URL of the environment and go to this URL to see the fully-functioning Flask application deployed on the cloud.

For this task, perform the following steps:

Type the following command into the terminal to check the status of the environment named `flask-env` against a key, `CNAME`:

```shell
eb status flask-env
```

### Task 7: Terminate the EB Environment

For this task, terminate the `flask-env` environment. This includes deleting all the AWS resources associated with this environment, such as Amazon EC2 instances, database instances, load balancers, security groups, and alarms.

For this task, perform the following steps:

+ Type the following command into the terminal to terminate the `flask-env` environment:

```shell
eb terminate flask-env
```

+ Verify if the environment has been deleted by enlisting all the running environments, like this:

```shell
eb list
```

### Task 8: Delete the Application

The AWS resources associated with the application have been deleted. That means you can now delete the application. Use the AWS CLI to delete the application.

For this task, perform the following steps:

+ Type the following command into the terminal to delete an application.

```shell
aws elasticbeanstalk delete-application --application-name <your_application_name>
```

+ Verify if the application has been deleted by enlisting all the `elasticbeanstalk` applications. This can be done by typing the following command:

```shell
aws elasticbeanstalk describe-applications
```




















