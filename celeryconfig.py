"""
REGISTER DISTRIBUTED TASKS HERE
Ref: http://bit.ly/2xldMEC
"""
register_tasks = [
    'celery_worker',
    'tasks',
]

""" 
`include` is an important config that loads needed modules to the worker
See problem at https://stackoverflow.com/q/55998650/1235074
"""
include = register_tasks + [

]