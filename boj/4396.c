#include <stdio.h>

int n;
char map[12][12];
char open[12][12];

int check(int x, int y);
int search(int x, int y);

int main() {
  int i, j, go = 0;

  scanf("%d", &n);

  for (i=0; i<n; i++) scanf("%s", map[i]);
  for (i=0; i<n; i++) scanf("%s", open[i]);

  for (i=0; i<n; i++) {
    if (go) break;
    for (j=0; j<n; j++) if (check(i, j)) { go = 1; break; }
  }

  for (i=0; i<n; i++) {
    for (j=0; j<n; j++) {
      if (go && map[i][j] == '*') printf("*");
      else if (open[i][j] == 'x') printf("%d", search(i, j));
      else printf(".");
    }
    printf("\n");
  }

  return 0;
}

int check(int x, int y) {
  if (open[x][y] == 'x' && map[x][y] == '*') return 1;
  return 0;
}

int search(int x, int y) {
  int c = 0;

  if (x != 0) c += map[x-1][y] == '*'?1:0;
  if (y != 0) c += map[x][y-1] == '*'?1:0;
  if (x != 0 && y != 0) c += map[x-1][y-1] == '*'?1:0;

  if (x != n-1) c += map[x+1][y] == '*'?1:0;
  if (y != n-1) c += map[x][y+1] == '*'?1:0;
  if (x != n-1 && y != n-1) c += map[x+1][y+1] == '*'?1:0;

  if (x != 0 && y != n-1) c += map[x-1][y+1] == '*'?1:0;
  if (x != n-1 && y != 0) c += map[x+1][y-1] == '*'?1:0;

  return c;
}
