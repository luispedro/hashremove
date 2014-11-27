def file_hash(fname, hash_name):
    import hashlib
    hob = hashlib.new(hash_name)
    with open(fname, 'rb') as f:
        while True:
            data = f.read(1024*1024)
            if not len(data):
                return hob.hexdigest()
            hob.update(data)

