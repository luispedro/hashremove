import os
import re
from os import path
for line in os.popen("git ls-tree git-annex --full-tree -r"):
    tokens = line.split()
    m = re.search('^SHA256E-[^-]+--([0-9a-f]+)\..*\.log$', path.basename(tokens[-1]))
    if m:
        print m.group(1)
