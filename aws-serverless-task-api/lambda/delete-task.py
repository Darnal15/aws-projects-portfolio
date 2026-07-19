import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudTasks")


def lambda_handler(event, context):

    body = json.loads(event["body"])

    table.delete_item(
        Key={
            "taskID": body["taskID"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Task deleted successfully"
        })
    }
