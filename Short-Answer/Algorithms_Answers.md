#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(logn) - as n grows, the runtime grows at a slower rate


b) O(nlogn) - The outer loop is O(n) which grows in a linear time complexity. The inner loop is O(logn) because the runtime for it grows at a slower rate as the input n increases. Thus O(nlogn)


c) O(n) - in this recursive algorithm, as the number of bunnies grows, the runtime will grow at the same rate

## Exercise II

For the egg drop exercise, a binary search algorithm would work to find starting at which floor the egg would start to break when dropped:

Given the range of floors

Determine Middle Floor and drop egg to see if it breaks
middle = hi + low / 2

If egg doesn't break, go higher and find middle
low = middle + 1
middle = hi + low / 2
drop egg from middle

If egg does break, go lower and find middle
hi = middle - 1
middle = hi + low / 2
drop egg from middle

Time Complexity of this Binary Searh would be O(logn) because through each iteration we're cutting the runtime in half.

Another option would be to iterate through all the given floors and drop the egg to find at what floor the egg would break

Time complexity for this, at it's worst case, would be O(n) because the egg may not break until the final floor.


