from sys import argv
from os import path, walk, unlink
from hashfile import file_hash

hash_name = 'sha256'
if len(argv) < 2:
    import sys
    sys.stderr.write("python {} HASH-FILE [HASH]\n".format(argv[0]))
    sys.exit(1)
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
