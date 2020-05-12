# -*- coding: utf-8 -*-
import MapReduce
import sys


def mapper(record):
    mr.emit_intermediate(record[1][:-10], None)


def reducer(key, list_of_values):
    mr.emit(key)


mr = MapReduce.MapReduce()
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
