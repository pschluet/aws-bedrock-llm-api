import json


def query(event, context):
    try:
        prompt = json.loads(event['body'])['prompt']

        return {
            "statusCode": 200, 
            "body": json.dumps({
                "prompt": prompt
            })}
    except:
        return  {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Bad Request: must include 'prompt' in request body."
            })
        }