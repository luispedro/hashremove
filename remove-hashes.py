from sys import argv
from os import path, walk, unlink
hash_name = 'sha256'
def file_hash(fname, hash_name):
    import hashlib
    h = hashlib.new(hash_name)
    with open(fname) as f:
        while True:
            data = f.read(1024*1024)
            if not len(data):
                return h.hexdigest()
            h.update(data)
existing_hashes = [line.strip().split()[0] for line in open(argv[1])]

verbose = True

if len(argv) > 2:
    hash_name = argv[2]

for dirpath,dirs,files in walk('.'):
    try:
        dirs.remove('.git')
    except ValueError:
        pass
    for f in files:
        f = path.join(dirpath, f)
        if not path.isfile(f):
            continue
        m = file_hash(f, hash_name)
        op = 'keep'
        if m in existing_hashes:
            unlink(f)
            op = 'rm'
        if verbose:
            print("{} {}".format(op, f))
