#!/usr/bin/python
#-*- coding: UTF-8 -*-

import math
import time

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def  main():
    # give two vector
    v1,v2 = [1,2,3], [2,3,4]
    print(v1, v2, cosine_similarity(v1,v2))

if __name__ == '__main__':
        start = time.clock()
        main()
        end = time.clock()
        print ("process: %f s" % (end - start))
