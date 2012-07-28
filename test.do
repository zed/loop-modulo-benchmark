# test that $EXE produces correct output
exec >&2
####set -x
: ${EXE:=primes_below}
echo $EXE

DEPS=${EXE##* }
redo-ifchange $DEPS

echo NOTE: adding current directory to PATH
PATH=$PATH:. time $EXE >output.txt
diff output.txt output.control
rm output.txt