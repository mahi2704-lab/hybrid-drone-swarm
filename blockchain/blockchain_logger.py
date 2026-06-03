import hashlib
import json
import time

blockchain = []

def create_block(data):

    previous_hash = blockchain[-1]["hash"] if blockchain else "0"

    block = {
        "timestamp": time.time(),
        "data": data,
        "previous_hash": previous_hash
    }

    block_string = json.dumps(block, sort_keys=True).encode()

    block["hash"] = hashlib.sha256(block_string).hexdigest()

    blockchain.append(block)

    return block