from sys import argv
from os import path, walk, unlink
hash_name = 'md5'
def file_hash(fname, hash_name):
    import hashlib
    md5 = hashlib.new(hash_name)
    with open(fname) as f:
        while True:
            data = f.read(1024*1024)
            if not len(data):
                return md5.hexdigest()
            md5.update(data)
existing_hashes = [line.strip().split()[0] for line in open(argv[1])]
if len(argv) > 2:
    hash_name = argv[2]

for dirpath,_,files in walk('.'):
    for f in files:
        f = path.join(dirpath, f)
        m = file_hash(f, hash_name)
        if m in existing_hashes:
            unlink(f)
            print(f)
