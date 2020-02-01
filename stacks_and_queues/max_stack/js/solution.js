// Implement the stack class

function Stack() {
  this.items = [];

  this.push = item => {
    this.items.push(item);
  };

  this.pop = () => {
    if (!this.items.length) {
      return null;
    }
    return this.items.pop();
  };

  this.peek = () => {
    if (!this.items.length) {
      return null;
    }
    return this.items[this.items.length - 1];
  };
}

function MaxStack() {
  this.stack = new Stack();
  this.maxStack = new Stack();

  this.push = item => {
    this.stack.push(item);
    if (this.maxStack.peek() === null || this.maxStack.peek() < item) {
      this.maxStack.push(item);
    }
  };

  this.pop = () => {
    const item = this.stack.pop();
    if (item === this.maxStack.peek()) {
      this.maxStack.pop();
    }
    return item;
  };

  this.getMax = () => {
    return this.maxStack.peek();
  };
}

module.exports = MaxStack;
