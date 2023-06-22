import os
import uuid
import boto3

from flask import jsonify

# Initialize the DynamoDB client
dynamodb_client = boto3.client('dynamodb')

# Configure the DynamoDB client for local development if the IS_OFFLINE environment variable is set
if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )

# Retrieve the name of the DynamoDB table from the USERS_TABLE environment variable
USERS_TABLE = os.environ['USERS_TABLE']

# This function interact with DynamoDB to get an user by id


def get_user(user_id):
    # Get the user from DynamoDB using the provided user ID
    result = dynamodb_client.get_item(
        TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
    )
    item = result.get('Item')

    # If the user is not found, return a JSON response with an error message and HTTP status code 404
    if not item:
        return jsonify({'error': 'Could not find user with provided "userId"'}), 404

    # Return a JSON response with the user details (userId and name)
    return jsonify(
        {'userId': item.get('userId').get(
            'S'), 'name': item.get('name').get('S')}
    )

# This function interact with DynamoDB to create an user passing the name


def create_user(request):
    # Generate a unique user_id using uuid.uuid4()
    user_id = str(uuid.uuid4())

    # Retrieve the user's name from the JSON payload in the request
    name = request.json.get('name')

    # If the name is not provided, return a JSON response with an error message and HTTP status code 400
    if not name:
        return jsonify({'error': 'Please provide "name"'}), 400

    # Insert the user into the DynamoDB table using put_item()
    dynamodb_client.put_item(
        TableName=USERS_TABLE, Item={
            'userId': {'S': user_id}, 'name': {'S': name}}
    )

    # Return a JSON response with the created user's userId and name
    return jsonify({'userId': user_id, 'name': name})
