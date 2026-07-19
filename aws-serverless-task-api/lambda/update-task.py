import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudTasks")


def lambda_handler(event, context):

    body = json.loads(event["body"])

    table.update_item(
        Key={
            "taskID": body["taskID"]
        },
        UpdateExpression="SET #s = :status",
        ExpressionAttributeNames={
            "#s": "status"
        },
        ExpressionAttributeValues={
            ":status": body["status"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Tasks updated successfully again"
        })
    }
