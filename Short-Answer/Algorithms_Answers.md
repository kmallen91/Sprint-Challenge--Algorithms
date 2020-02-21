#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The run time of this function would be O(n) because although n is being multiplied by itself multiply times, a is the constraint for the while loop. So, assuming n is the variable that is input into the function, as n gets larger the function only needs to iterate through n linearly.


b)
The run time complexity of this function would be 0(n^2) because it iterates through the first loop n times and then loops again in the second loop, which is also determined by n


c)
Run time of this function would be 0(n) because it needs to iterate through each instance of 'bunnies' below the given value, which would be determined by the value given, so n times.

## Exercise II

The quickest solution for this would be to replicate a binary sort. In order to achieve this, you would start at floor n / 2, and determine if the egg survives the fall. If it doesn't, then the current floor would become your new 'n' and you would go to the new n / 2 floor. You would continue this until the egg does not break, then you would have a lower constraint, a floor in which the egg survives. From there you would split your previous n with your lower constraint (e.g. original n of 25 and survived a drop from 12, then split would give 18). You would then continue with this pattern until you find the highest floor with which the egg survives. The runtime complexity of this is log(n), which means that as n infinitely increases, the time it takes to find the correct floor reduces significantly.
