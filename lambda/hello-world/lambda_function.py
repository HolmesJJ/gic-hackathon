import json


def lambda_handler(event, context):
    body = event.get("body", None)
    if body:
        body = json.loads(body)
        content = body.get("content", None)
        if content:
            return {
                "statusCode": 200,
                "body": json.dumps(content)
            }
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }
