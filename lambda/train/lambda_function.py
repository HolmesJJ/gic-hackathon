import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("train")


def lambda_handler(event, context):
    Id = event.get("Id", None)
    if Id:
        Item = table.get_item(Key={"Id": Id})
        if "Item" in Item:
            response = Item["Item"]
            return {
                "statusCode": 200,
                "body": response
            }
        else:
            return {
                "statusCode": 200,
                "body": {}
            }
    else:
        response = table.scan()["Items"]
        return {
            "statusCode": 200,
            "body": response
        }
