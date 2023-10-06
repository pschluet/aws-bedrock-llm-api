import json
import boto3

bedrock = boto3.client(service_name="bedrock-runtime")


def query_llm(prompt: str) -> str:
    request_body = json.dumps({"prompt": prompt, "max_tokens": 1000, "temperature": 0.9})

    modelId = "cohere.command-text-v14"
    app_json = "application/json"

    response = bedrock.invoke_model(
        body=request_body, modelId=modelId, accept=app_json, contentType=app_json
    )
    response_body = json.loads(response.get("body").read())

    print(json.dumps(response_body))

    return response_body.get("generations")[0].get("text")


def query(event, context):
    try:
        prompt = json.loads(event.get("body")).get("prompt")
        result = query_llm(prompt)

        return {
            "statusCode": 200,
            "body": json.dumps({"result": result}),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Internal Server Error: {e}"}),
        }
