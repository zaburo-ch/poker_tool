#! /usr/bin/env python

""" bbr.py, create color of black body radiation """

import math as M

H = 6.626E-34 #Js
C = 3.0E8 #ms-1
K = 1.38E-23 #JK-1
MAX_TEMP = 10000 # K

def pl(la, t):
    """ equation of black body radiation """
    return (2.0* M.pi*H*C*C)/(M.pow(la, 5)*(M.exp(H*C/(la * K * t)) -1))

def pred(t):
    return pl(650.0E-9, t)

def pgreen(t):
    return pl(510.0E-9, t)

def pblue(t):
    return pl(475.0E-9, t)

def pviolet(t):
    return pl(400.0E-9, t)

def cnorm(val, g):
    return M.floor(val/g)

def bbrcolor_rel(t):
    r = pred(t) + pviolet(t)*0.3
    g = pgreen(t) + pred(t)*0.2 + pblue(t)*0.2
    b = pblue(t) + pviolet(t)*0.7
    norm = max(r, g, b)/255.0
    return '#%02X%02X%02X' % (cnorm(r, norm), cnorm(g, norm), cnorm(b, norm))
    

if __name__ =='__main__':
    import sys
    temp = eval(sys.argv[1])
    print 'normalized: ', bbrcolor_rel(temp)
