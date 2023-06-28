def weighted_average(event):
    total_weighted_score = 0
    total_weight = 0

    for obj in event:
        score = float(obj['score'])
        if obj['label'] == 'Fake':
            score = (score - 1) * -1
        payload = obj['payload']
        weight = len(payload)
        total_weighted_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0 

    average = total_weighted_score / total_weight
    return average

def lambda_handler(event, context):
    avg = weighted_average(event)

    label = "Real"
    if (avg < 0.5):
        avg = (avg - 1) * -1
        label = "Fake"

    result = {
        "label": label,
        "score": avg,
        "complete": event        
    }

    return result