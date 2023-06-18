import json
import boto3


def lambda_handler(event, context):
    print("MessageCreateUpdateLambda invoked.")
    print(json.dumps(event))

    # Use the boto3 library to interact with AWS services
    client = boto3.client("events")

    # Structure your event
    eventBridgeEvent = {
        "Source": "com.myorg.message",
        "DetailType": "Message.CreatedOrUpdated",
        "Detail": json.dumps(event),
    }

    response = client.put_events(
        Entries=[
            eventBridgeEvent,
        ]
    )

    print(response)

    return {
        "statusCode": 200,
        "body": json.dumps("Message creation or update processed."),
    }
