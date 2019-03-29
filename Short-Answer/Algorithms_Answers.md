Add your answers to the Algorithms exercises here.

a)

The runtime of the code would be O(1) because the same number of calculations happen regardless of the length of n.
As n isn't incrementing or decrementing, the code would run infinitely.

b)

O(n^4) as we run 4 for loops the length of n. The final for loop runs for slightly longer than the others as it ends at 10 + k rather than just kand the middle two for loops are slightly shorter as they end at n but start at i + 1 or j + 1. However, these differences are very small when compared to what n could be. Therefore we can ignore these small differences and state that O(n^4).

c)

O(n) as the number of calculations is equal to the length of the input.
