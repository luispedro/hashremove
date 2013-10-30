from os import readlink, path, walk
for root,dirs,fs in walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    for f in fs:
        f = path.join(root,f)
        if path.islink(f):
            link = readlink(f)
            if '.git/annex/objects/' in link:
                link,_= path.splitext(link)
                print link[-256/4:]
