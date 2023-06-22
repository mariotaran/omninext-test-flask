## Usage

### Prerequisites

In order to package your dependencies locally with `serverless-python-requirements`, you need to have `Python3.9` installed locally. You can create and activate a dedicated virtual environment with the following command:

```bash
python3.9 -m venv ./venv
source ./venv/bin/activate
```

Alternatively, you can also use `dockerizePip` configuration from `serverless-python-requirements`. For details on that, please refer to corresponding [GitHub repository](https://github.com/UnitedIncome/serverless-python-requirements).

### Deployment

This example is made to work with the Serverless Framework dashboard, which includes advanced features such as CI/CD, monitoring, metrics, etc.

In order to deploy with dashboard, you need to first login with:

```
serverless login
```

install dependencies with:

```
npm install
```

and then perform deployment with:

```
serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-python-flask-dynamodb-api-project to stage dev (us-east-1)

✔ Service deployed to stack aws-python-flask-dynamodb-api-project-dev (182s)

endpoint: ANY - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com
functions:
  api: aws-python-flask-dynamodb-api-project-dev-api (1.5 MB)
```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [httpApi event docs](https://www.serverless.com/framework/docs/providers/aws/events/http-api/).
