# -*- coding: utf-8 -*-
"""같은숫자는싫어.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11w2ly0jV8ftX7UOk_P1nfP35uNre6f-m
"""

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i-1] != arr[i]:
            answer.append(arr[i])

    return answer