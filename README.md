# aws-bedrock-llm-api
Setup of an LLM API utilizing AWS Bedrock for predictions

## Setup & Deploy
```
npm install -g serverless
npm install
serverless plugin install --name serverless-python-requirements
serverless deploy
```

## Example API Call
Once you run `serverless deploy`, the domain and API key values that you will use in the request below will be printed to the console.

Request
```
curl --request POST \
  --url https://<replace-with-your-domain>.execute-api.us-east-1.amazonaws.com/dev/query \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/2023.5.8' \
  --header 'x-api-key: <replace-with-your-api-key>' \
  --data '{
	"prompt": "What'\''s the fastest marathon time?"
}'
```

Response
```
{
	"prompt": "What's the fastest marathon time?",
	"result": " The fastest marathon time is 2 hours, 2 minutes, and 57 seconds, set by Eliud Kipchoge of Kenya at the Berlin Marathon in 2018.\n\nThe women's fastest marathon time is 2 hours, 15 minutes, and 25 seconds, set by Brigid Kosgei of Kenya at the Chicago Marathon in 2019."
}
```
