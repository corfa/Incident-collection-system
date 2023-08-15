import hashlib
import reprlib

def create_hash(data: dict) -> str:
    try:
        ordered_data = {
            "headers": {k: v for k, v in sorted(data.get("headers").items())},
            "body": {k: v for k, v in sorted(data.get("body").items())}
        }
        data_str = reprlib.repr(ordered_data)
        data_hash = hashlib.md5(data_str.encode()).hexdigest()
        return data_hash
    except:
        raise Exception('Failed to generate hash')
