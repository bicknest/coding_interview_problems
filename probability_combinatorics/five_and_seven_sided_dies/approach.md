# Approach

GOTCHA: Obviously calling rand5 twice, adding together, and taking a modulus will not give us the correct probability distribution

So

Because rand5() only has 5 possible outcomes, and we need 7 distinct possible results for rand7(), we need to call rand5() at least twice.

When we call rand5() twice, we have 5 * 5 = 25 possible outcomes. If each of our 7 possible results has an equal chance of occurring, we'll need each outcome
to occur in our set of possible outcomes the same number of times. So our total number of possible outcomes must be divisible by 7.

25 isn't evenly divisble by 7, but 21 is. So when we get one of the last 4 possible outcomes we throw out and roll again.
