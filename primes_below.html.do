# Show annotated C code generated by cython
basename=${1%.*}
redo $basename.c >&2 && cat *.html #xxx
python -mwebbrowser $1 >&2