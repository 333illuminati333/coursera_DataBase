# -*- coding: utf-8 -*-
import MapReduce
import sys


def reducer(key, list_of_values):
	if len(list_of_values)==1:
		print key
		mr.emit((list_of_values[0][0],list_of_values[0][1]))
		mr.emit((list_of_values[0][1],list_of_values[0][0]))


def mapper(record):
    key = record[0]
    value = record[1]
    mr.emit_intermediate(hash(key)+hash(value),record)


mr = MapReduce.MapReduce()
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
