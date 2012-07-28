# compile program with embed Python
exec >&2
####set -x
: ${CC:=gcc}
DEPS="$2.c"
redo-ifchange $DEPS
$CC -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes `pkg-config --cflags-only-I python` -c $DEPS -o $3