function Fib() {
    this.memo = {};

    this.fibonacci = (n) => {
        if (n < 0) {
            return "No negative numbers in series";
        }
        else if (n === 0 || n === 1) {
            return n;
        }

        if (this.memo.hasOwnProperty(n)) {
            return this.memo[n];
        }

        const result = this.fibonacci(n -1) + this.fibonacci(n - 2);
        this.memo[n] = result;

        return result;
    };
}

module.exports = Fib;