#!/usr/bin/env python
"""Compile primes_below.is_prime() using numba."""
import sys

from numba import uint32 as cint
from numba.decorators import jit

import primes_below

# patch is_prime()
primes_below.is_prime = jit(arg_types=[cint], ret_type=cint)(
    primes_below.is_prime)

sys.exit(primes_below.main(sys.argv))
