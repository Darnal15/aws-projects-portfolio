import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CloudTasks")


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def lambda_handler(event, context):

    response = table.scan()

    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"], cls=DecimalEncoder)
    }
