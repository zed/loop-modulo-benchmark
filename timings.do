# produce timings for all cases
exec >&2
####set -x
DEPS=primes_below

EXE="python primes_below_numba.py" redo test

for EXE in $DEPS-c $DEPS ; do
    EXE=$EXE redo test
done

for py in pypy python python3 jython ; do
    EXE="$py $DEPS.py" redo test
done


