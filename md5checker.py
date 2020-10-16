#!/usr/bin/python

import itertools
import hashlib
import sys

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$#%\"&()=?¿¡{}[]-_+.,:;"
length = 256
done = False
find = "900150983cd24fb0d6963f7d28e17f72"
#find = "e305cdbb739e4eda7ee90551b3f39f63"


for i in range(length):
    def pw_guess():
        res = itertools.permutations(characters,i)
        for guess in res:
            yield guess
    
    options = pw_guess()
    
    for option in options:
        result = hashlib.md5(''.join(option).encode())
        print(result.hexdigest())
        if (result.hexdigest() == find ):
            print("ECONTRADO==================================")
            print(''.join(option))
            sys.exit(0)
