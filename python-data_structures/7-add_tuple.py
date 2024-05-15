#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    u = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    if len(tuple_a) or len(tuple_b) < 2:
       i = (tuple_b[0] + tuple_a[0], tuple_b[0])  
    return i