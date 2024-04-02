import hashlib

def hash_file(filepath):
    """Generate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()
