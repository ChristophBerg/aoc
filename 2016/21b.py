#!/usr/bin/python3

from itertools import permutations
import re

pw = list('fbgdceah')
print(pw)

rules = []

with open('21.txt') as f:
    rules = f.readlines()

def scramble(pw):
    for line in rules:
        if m := re.match('swap position (\d) with position (\d)', line):
            a, b = int(m[1]), int(m[2])
            pw[a], pw[b] = pw[b], pw[a]
        elif m := re.match('swap letter (.) with letter (.)', line):
            a, b = pw.index(m[1]), pw.index(m[2])
            pw[a], pw[b] = pw[b], pw[a]
        elif m := re.match('rotate (left|right) (\d) steps?', line):
            shift = int(m[2])
            if m[1] == 'left':
                pw = pw[shift:] + pw[:shift]
            else:
                pw = pw[-shift:] + pw[:-shift]
        elif m := re.match('rotate based on position of letter (.)', line):
            index = pw.index(m[1])
            shift = (index + 2 if index >= 4 else index + 1) % len(pw)
            if shift > 0:
                pw = pw[-shift:] + pw[:-shift]
        elif m := re.match('reverse positions (\d) through (\d)', line):
            a, b = int(m[1]), int(m[2])
            if a == 0:
                pw[a:b+1] = pw[b::-1]
            else:
                pw[a:b+1] = pw[b:a-1:-1]
        elif m := re.match('move position (\d) to position (\d)', line):
            a, b = int(m[1]), int(m[2])
            c = pw.pop(a)
            pw.insert(b, c)
        else:
            raise SyntaxError(line)
    return pw

for perm in permutations(pw):
    pw2 = scramble(list(perm))
    if pw2 == pw:
        print("".join(perm))
