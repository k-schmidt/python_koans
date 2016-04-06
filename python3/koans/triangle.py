#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#


def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    # pass
    if min([a, b, c]) > 1 and a + c > b:
        #  if a + c > b:

        if a == b and b == c and a == c:
            return "equilateral"

        elif a == b or b == c or a == c:
            return "isosceles"

        else:
            return "scalene"
    # else:  (c > b and a == b) or min([a, b, c]) <= 0 or max([a, b, c]) == b:
    raise TriangleError


# Error class used in part 2.  No need to change this code.


class TriangleError(Exception):
    pass
