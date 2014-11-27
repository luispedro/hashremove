import os
import re
from os import path
for line in os.popen("git ls-tree git-annex --full-tree -r"):
    tokens = line.split()
    name = path.basename(tokens[-1])
    m = re.search('^SHA256E-[^-]+--([0-9a-f]+)\..*log$', name)
    if m:
        print(m.group(1))
