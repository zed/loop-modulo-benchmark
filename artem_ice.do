# build ./artem_ice
exec >&2
: ${CC:=gcc}
DEPS="$2.c"
redo-ifchange $DEPS
$CC -DNDEBUG -g -O3 -Wall -Wextra $DEPS -o $3