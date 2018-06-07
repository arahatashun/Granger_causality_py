#!/usr/bin/python
# -*- coding: utf8 -*-
# Author: Shun Arahata
"""
Code for compare graph structure
"""

import numpy as np


def f_score(a, b, threshold=0.1):
    """ Precision Recall F1 Score

    :param a: Matirx
    :param b: Matirx
    :return:
    """
    a = np.copy(a)
    b = np.copy(b)
    a[a < threshold] = 0
    a[a >= threshold] = 1
    b[b < threshold] = 0
    b[b >= threshold] = 1
    true_positive_mat = np.zeros_like(a)
    b_tmp = np.copy(b)
    b_tmp[b < threshold] = -1
    true_positive_mat[b_tmp == a] = 1
    true_positive = np.sum(true_positive_mat)
    precison = true_positive / np.sum(a)
    recall = true_positive / np.sum(b)
    score = 2 * precison * recall / (precison + recall)
    diff_mat = np.zeros_like(a)
    diff_mat[a >= threshold] += 1
    diff_mat[b >= threshold] += 2

    return score, diff_mat
