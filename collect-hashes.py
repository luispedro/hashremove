from sys import argv
from os import path, walk
from hashfile import file_hash
hash_name = 'sha256'

if len(argv) > 1:
    hash_name = argv[1]
seen = set()
for dirpath,_,files in walk('.'):
    for f in files:
        f = path.join(dirpath, f)
        h = file_hash(f, hash_name)
        if h not in seen:
            print(h)
            seen.add(h)
