function fibFactory() {
  var memo = {};
  var callCount = 0;

  function fibonacci(n) {
    callCount += 1;
    // uncomment out the line below to show that
    // the closures are working properly to memoize
    // console.log(callCount);
    if (n < 0) {
      return "No negative numbers in series";
    } else if (n === 0 || n === 1) {
      return n;
    }

    if (memo.hasOwnProperty(n)) {
      return memo[n];
    }

    const result = fibonacci(n - 1) + fibonacci(n - 2);
    memo[n] = result;

    return result;
  }
  return fibonacci;
}

module.exports = fibFactory;
