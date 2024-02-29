# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:36:50 2024

@author: student
"""

def generate_truth_table():
    header = ["P", "Q", "P ∧ Q", "P ∨ Q", "P ∧ Q", "P ∨ Q", "P → Q", "P ← Q", "P ↔ Q"]
    print("\t".join(header))

    values = [False, True]

    for P in values:
        for Q in values:
            row = [str(P), str(Q), str(P and Q), str(P or Q), str(P and Q), str(P or Q),
                   str((not P) or Q), str(P or (not Q)), str(P == Q)]
            print("\t".join(row))

# 產生並印出真值表
generate_truth_table()
