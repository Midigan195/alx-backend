#!/usr/bin/env python3
"""
This module defines a function that returns
the start index and end index of specified pages
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns start index and
    end index corresponding to page and number of pages
    """
    return ((page-1) * page_size, page_size * page)
