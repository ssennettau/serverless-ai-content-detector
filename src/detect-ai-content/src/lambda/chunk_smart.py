import re
import sys
sys.path.insert(0, '/mnt/efs/packages')

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("roberta-base-openai-detector")

def chunk_splitter(data):
    chunks = []

    current_block = ""
    current_block_tokens = 0

    for line in data.split('\n'):
        line_tokens = tokenizer.encode(line)

        if len(line_tokens) + current_block_tokens > 400:
            chunks.append(current_block)
            current_block = ""
            current_block_tokens = 0
        
        if len(line_tokens) > 400:
            # TODO: Split logic
            # For extremely large inputs, need to be able to split it up based
            # on the tokenized length of the line, and rebuild into a list of 
            # reconstructed paragraphs of the whole sentences... messy.
            raise Exception("Line is too long - can't handle this yet")
        else:
            current_block += line + ' '
            current_block_tokens += len(line_tokens)

    chunks.append(current_block)

    return chunks

def lambda_handler(event, context):
    result= chunk_splitter(event['input'])
    
    return {
        "chunks": result
    }