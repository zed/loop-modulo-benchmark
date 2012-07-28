# create .c file from .py file
exec >&2
####set -x
: ${CYTHON:=cython}

NAME=${1%.*}
DEPS=$NAME.py
redo-ifchange $DEPS

# workaround Cython bug that it doesn't ignore `if not
# cython.compiled: block` during compilation
tmpname=$DEPS.tmp
python -c "import sys, re; print(re.sub(r'(?s)\#\#start_cython_hide.*\#\#end', '', sys.stdin.read()))" <$DEPS >$tmpname

$CYTHON -a --embed $tmpname -o $3
rm $tmpname