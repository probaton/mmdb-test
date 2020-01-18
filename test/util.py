import re

def is_valid_uuid(uuid):
    match = re.match("[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", uuid)
    return bool(match)
