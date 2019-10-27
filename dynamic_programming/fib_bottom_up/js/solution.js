/** fib bottom up */

function fibBottomUp(n) {
  if (n < 0) {
    return "No negative numbers in series";
  }
  if (n === 0) {
    return 0;
  }
  fib = [];
  for (let i = 0; i < n; i++) {
    if (i <= 1) {
      fib[i] = 1;
    } else {
      fib[i] = fib[i - 1] + fib[i - 2];
    }
  }
  return fib[n - 1];
}

module.exports = fibBottomUp;
