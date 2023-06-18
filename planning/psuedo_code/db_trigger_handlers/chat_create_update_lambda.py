import json
import boto3


def lambda_handler(event, context):
    print("ChatCreateUpdateLambda invoked.")
    print(json.dumps(event))

    # Use the boto3 library to interact with AWS services
    client = boto3.client("events")

    # Structure your event
    eventBridgeEvent = {
        "Source": "com.myorg.chat",
        "DetailType": "Chat.CreatedOrUpdated",
        "Detail": json.dumps(event),
    }

    response = client.put_events(
        Entries=[
            eventBridgeEvent,
        ]
    )

    print(response)

    return {"statusCode": 200, "body": json.dumps("Chat creation or update processed.")}
