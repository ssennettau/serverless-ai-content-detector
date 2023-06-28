import hashlib
import json

def lambda_handler(event,context):
    hash = hashlib.sha256()

    input = bytes(event['payload'], "utf-8")
    hash.update(input)

    return {
        'payload': event['payload'],
        'hash': hash.hexdigest()
    }