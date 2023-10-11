# -*- coding: utf-8 -*-
H,W = map(int, input().split())
h,w = map(int, input().split())

zentai = H*W
nuri = H*w + W*h
kaburi = h*w
ans = zentai - nuri + kaburi

print(ans)