import json
import boto3
import openai


def lambda_handler(event, context):
    print("ChatCreatedOrUpdatedSubscriberLambda invoked.")
    dynamodb_event = json.loads(event["detail"])

    # Initialize OpenAI client
    openai.api_key = "your-openai-api-key"

    # Start a new chat session with OpenAI
    chat_session = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": dynamodb_event["NewImage"]["Content"]["S"]},
        ],
    )

    # Extract the assistant's reply
    assistant_reply = chat_session["choices"][0]["message"]["content"]

    # Initialize DynamoDB client
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("your-dynamodb-table-name")

    # Write the assistant's reply to the database
    table.put_item(
        Item={
            "ChatId": dynamodb_event["NewImage"]["ChatId"]["S"],
            "Timestamp": dynamodb_event["NewImage"]["Timestamp"]["S"],
            "Content": assistant_reply,
            "UserId": dynamodb_event["NewImage"]["UserId"]["S"],
            "Access": dynamodb_event["NewImage"]["Access"]["S"],
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Chat creation or update event handled."),
    }
