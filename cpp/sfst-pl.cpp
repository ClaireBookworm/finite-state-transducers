// % define the alphabet for the following replacement rules
// % The morphological markers <JJ>, <JJR> and <JJS> are deleted
// % on the surface
// ALPHABET = [A-Za-z] [#<JJ><JJR><JJS>]:<> y:i e:<>
// % rule replacing y with i
// $R1$ = y <=> i (#:<> e)
// % rule eliminating e
// $R2$ = e <=> <> (#:<> e)
// % the conjunction of these rules
// $R$ = $R1$ & $R2$
// % create a recognizer for the words in the file "adj"
// $WORDS$ = "adj"
// % append the different endings to the words
// $S$ = $WORDS$ <>:# (<JJ> | {<>}:{er}<JJR> | {<>}:{est}<JJS>)
// % apply the phonological rules to obtain the result transducer
// $S$ || $R$


#include <stdio.h>
#include "fst.h"

int main(int argc, char **argv) {
FILE *file1=fopen("file1","rb");
FILE *file2=fopen("file2","rb");
char *s="Hello";
Automaton a1(file1);
Automaton a2(file2);
Automaton a(s);
(a1 || a2 || a).minimise().lower_level().print_strings(stdout);
}