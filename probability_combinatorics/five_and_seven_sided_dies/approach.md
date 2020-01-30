# Approach

GOTCHA: Obviously calling rand5 twice, adding together, and taking a modulus will not give us the correct probability distribution

So

Because rand5() only has 5 possible outcomes, and we need 7 distinct possible results for rand7(), we need to call rand5() at least twice.

When we call rand5() twice, we have 5 * 5 = 25 possible outcomes. If each of our 7 possible results has an equal chance of occurring, we'll need each outcome
to occur in our set of possible outcomes the same number of times. So our total number of possible outcomes must be divisible by 7.

25 isn't evenly divisble by 7, but 21 is. So when we get one of the last 4 possible outcomes we throw out and roll again.


So we get a O(infinity) for time complexity in the worst case, because we may always have to roll again.

Is it possible to do better if we want a truly uniform solution?

We can prove that there isn't with prime factorization:

When we roll our die n times, we get 5^n possible outcomes. Is there an integer n that will give us a 5^n that's evenly divisible by 7?

No there isn't

Every integer can be expressed as a product of prime numbers (its prime factorization). Every integer only has one prime factorization.

Since 5 is already prime, any number that can be expressed as 5^n will have a prime factorization that is all 5s.

Since 7 is also prime, if any power of 5 were divisible by 7, 7 would be in its prime factorization. But 7 can't be in its prime factorization because its prime factorization is all 5s.
So no power of 5 is divisible by 7.
