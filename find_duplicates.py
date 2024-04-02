import os
from collections import defaultdict
from file_hashing import hash_file

def find_duplicates(directory):
    """Find and return a list of duplicates in the given directory."""
    hashes = defaultdict(list)
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = hash_file(filepath)
            hashes[file_hash].append(filepath)
    return [files for files in hashes.values() if len(files) > 1]
