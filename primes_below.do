# link executable with python
exec >&2
####set -x
: ${CC:=gcc}
DEPS="$2.o"
redo-ifchange $DEPS
$CC -O3 $DEPS -o $3 `pkg-config --libs-only-l python`
#NOTE: -l$PYTHONXY must be put last