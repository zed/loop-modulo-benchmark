/* C code from http://stackoverflow.com/questions/11641098/ question

   modified to produce the same output as Python-based variants
*/

#include <stdio.h>

static
int isprime(int x) {
  int i;
  for (i = 2; i < x; ++i)
    if (x%i == 0) return 0;
  return 1;
}

static
void findprimes(int m) {
  int i;
  putchar('[');
  for (i = 11; i < m; ++i)
    if (isprime(i) && isprime(i-6)) {
      printf("(%d, %d)%s", i-6, i,
             i != 99929 ? ", " : ""); /*XXX: force correct output formatting */
    }
  puts("]");
}

int main() {
    findprimes(100*1000);
    return 0;
}
