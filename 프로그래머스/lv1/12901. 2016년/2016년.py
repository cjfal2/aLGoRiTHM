import datetime

def solution(a, b):
    return datetime.datetime(2016, a, b).strftime("%A").upper()[0:3]