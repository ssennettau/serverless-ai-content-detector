import sys
sys.path.insert(0, '/mnt/efs/packages')

from aws_lambda_powertools import Logger
from aws_lambda_powertools.logging import correlation_paths

logger = Logger(service="infer")

from transformers import pipeline
pipe = pipeline("text-classification", model="roberta-base-openai-detector")

def analyze_data(input):
    data = pipe(input)
    
    return {
        'label': str(data[0]['label']),
        'score': str(data[0]['score'])
    }

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
def lambda_handler(event, context):
    logger.info("Running inference")

    analysis = analyze_data(event['payload'])
    
    return analysis
