from sys import argv
from os import path, walk
hash_name = 'md5'
if len(argv) > 1:
    hash_name = argv[1]
def file_hash(fname, hash_name):
    import hashlib
    h = hashlib.new(hash_name)
    with open(fname) as f:
        while True:
            data = f.read(1024*1024)
            if not len(data):
                return h.hexdigest()
            h.update(data)
seen = set()
for dirpath,_,files in walk('.'):
    for f in files:
        f = path.join(dirpath, f)
        h = file_hash(f, hash_name)
        if h not in seen:
            print h
            seen.add(h)
