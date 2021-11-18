# -*- coding: utf-8 -*-
"""
Create Time: 11/17/2021 12:29 PM
Author: Zhou
"""

from django import template

register = template.Library()


def range_filter(value):
    return value[0:500] + "...."


register.filter('range_filter', range_filter)