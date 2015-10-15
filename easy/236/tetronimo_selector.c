#include <stdio.h>
#include <stdlib.h>

void shuffle(char *array, int n) {
    if (n > 1) {
        size_t i;
        for (i=0; i<n-1; i++) {
            size_t rnd = (size_t) rand();
            size_t j = i + rnd / (RAND_MAX / (n - i) + 1);
            int t = array[j];
            array[j] = array[i];
            array[i] = t;
        }
    }

}

void print_tetronimo_output(char *pieces, int l) {
    char output[l+1];
    int i=0, k;
    while (i<l) {
        shuffle(pieces, 7);
        for (k=0; k<7; k++) {
            output[i] = pieces[k];
            i++;
        }
    }
    output[l] = '\0';

    printf( "%s\n", output );
}


int main() {
    char pieces[7] = {'O', 'I', 'S', 'Z', 'L', 'J', 'T'};
    int strlen = 50;
    print_tetronimo_output(pieces, strlen);
    return 0;
}
