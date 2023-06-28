import re

def chunk_splitter(data):
    split = []

    data = data.replace('\n',' ')

    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', data)
    
    chunks = []
    current_chunk = ''
    
    for sentence in sentences:
        words = sentence.split()
        
        if len(current_chunk.split()) + len(words) <= 100:
            current_chunk += ' ' + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def lambda_handler(event, context):
    result= chunk_splitter(event['input'])
    
    return {
        "chunks": result
    }