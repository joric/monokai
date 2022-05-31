#!/usr/bin/env python3

# this is url http://test.com this is email: test@test.com

from typing import *
from collections import *
from functools import *

class Solution:
    def palindromePairs(self, words: List[str], foo: int=0) -> List[List[int]]:
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    s = words[i]+words[j]
                    if s==s[::-1]:
                        res.append((i,j))
        return res

class SolutionOneliner:
    def palindromePairs(self, words):
        return [(g:=lambda d,a,b,f,i:set([(d[b],i) if f
            else (i,d[b])]) if a==a[::-1]
            and b in d and d[b]!=i else set(), fn:=lambda a,b:(a[0],a[1]|
            g(a[0],b[0],b[1][::-1],0,b[2])|g(a[0],b[1],b[0][::-1],1,b[2]))),
            reduce(fn, ((w[j:], w[:j],i) for i,w in enumerate(words) for j in
            range(len(w)+1)),[{w:i for i,w in enumerate(words)},set()])][1][1]

tests = [
    [ ["abcd","dcba","lls","s","sssll"], [[0,1],[1,0],[3,2],[2,4]] ],
    [ ["bat","tab","cat"], [[0,1],[1,0]] ],
    [ ["a",""], [[0,1],[1,0]]],
]

def z(v):
    x = sorted(sorted(p) for p in v) if v else []
    return x

for t in tests:
    args, res = t[:-1], t[-1]
    out = getattr(Solution(), dir(Solution)[-1])(*args)
    print('out "%.40s" expected "%.40s"' % (out, res), 'OK' if z(out)==z(res) else 'FAIL!')

