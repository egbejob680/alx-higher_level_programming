#!/usr/bin/python3

for n in range(10):
    for m in range(n + 1, 10):
        if (n == 8):
            print('{:d}{:d}'.format(n, m))
            break
        print('{:d}{:d},'.format(n, m), end=' ')
        