import hashlib

def create_hash(data: dict) -> str:
    ordered_data = {
        "headers": {k: v for k, v in sorted(data["headers"].items())},
        "body": {k: v for k, v in sorted(data["body"].items())}
    }
    data_json = str(ordered_data)
    data_hash = hashlib.md5(data_json.encode()).hexdigest()
    return data_hash