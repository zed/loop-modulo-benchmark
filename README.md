loop-modulo-benchmark
=====================

Test for-loop, modulo performance using RPython, Pypy, Cython, Jython, CPython 2.x, CPython 3, numba

`primes_below.py` originated from
[Interpreting a benchmark in C, Clojure, Python, Ruby, Scala and others](http://stackoverflow.com/questions/11641098/interpreting-a-benchmark-in-c-clojure-python-ruby-scala-and-others) StackOverflow question.

### Results

    n=100*1000
    | executable     |   time, |        ratio, |
    |                | seconds | w.r.t. python |
    |----------------+---------+---------------|
    | artem_ice (C)  |    2.19 |          0.06 |
    | primes_below   |    2.60 |          0.07 |
    | primes_below-c |    5.70 |          0.15 |
    | pypy           |    7.14 |          0.19 |
    | python (numba) |    7.33 |          0.20 |
    | jython         |   34.36 |          0.92 |
    | python         |   37.53 |          1.00 |
    | python3        |   65.59 |          1.75 |
    #+TBLFM: $3=$2/@9$2;%.2f


- artem_ice : C programming language (for comparison with Python-based variants)
- primes_below-c : RPython
- primes_below : Cython

To produce the results, run:

    $ ./do timings

Note: you could use `make`, [`redo`](https://github.com/apenwarr/redo)
instead of `./do`.

To try individual cases:

    $ EXE="pypy primes_below.py" ./do test


#### Software Versions

    | PyPy    |  1.9.0 |
    | Jython  |  2.5.1 |
    | Python  |  2.7.3 |
    | Python3 |  3.2.3 |
    | Cython  | 0.15.1 |


### Dependencies

*nix environment: gcc, diff, pkg-config, time, bash.

-  `primes_below-c` requires [Pypy source code and binary](http://pypy.org/download.html)
   (`translate.py` script):

        $ PYPY_ROOT=/path/to/pypy-source ./do primes_below-c

- `primes_below` requires `cython` and `pkg-config` should know where
  python headers and libraries are:

        $ pip install cython

        $ CYTHON=venv/bin/cython ./do primes_below


`pypy`, `jython`, `python`, `python3` binaries should be in `PATH`.

- python (numba) requires [numba](https://github.com/numba/numba). Follow installation instructions there