# translate *.py (RPython) to *-c program
exec >&2
NAME=${1%-*}.py
redo-ifchange $NAME
: ${PYPY_ROOT:=~/src/pypy}
pypy $PYPY_ROOT/pypy/translator/goal/translate.py --output $3 $NAME