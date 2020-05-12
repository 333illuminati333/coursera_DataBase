# -*- coding: utf-8 -*-
import MapReduce
import sys


max_dim = 5
mr = MapReduce.MapReduce()


def mapper(record):
    global max_dim
    key = str(record[1])+''+str(record[2])
    value = record[0]+''+str(record[3])
    if record[0] == 'a':
        for i in range(max_dim):
            mr.emit_intermediate(str(record[1])+''+str(i), record)

    elif record[0] == 'b':
        for i in range(max_dim):
            mr.emit_intermediate(str(i)+''+str(record[2]),record)


def reducer(key, list_of_values):
    global max_dim
    lst = []
    res = 0
    temp = 0
    for term_1 in list_of_values:
        for term_2 in list_of_values:
            if term_1[0]=='a':
                if term_1[2]==term_2[1] and term_2[0]=='b':
                    temp = term_1[-1]*term_2[-1]
                    res += temp
    mr.emit((int(list(key)[0]),int(list(key)[1]),res))


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
