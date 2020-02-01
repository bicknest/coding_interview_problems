# Problem Definition

You have a class `Stack` that implements a stack. It has push, pop and peek methods. It looks something like this:

// JS implementation
class Stack {
    constructor() {
        this.items =[];
    }

    push(items) {
        this.items.push(item);
    }

    pop() {
        if (!this.items.length) {
            return null;
        }
        return this.items.pop();
    }

    peek() {
        if (!this.items.length) {
            return null;
        }
        return this.items[this.items.length - 1];
    }
}

You are given that constraints where you need to access the maxima of a stack as you build it and that look up always has to be very fast O(1)

Using the Stack class, implement another class MaxStack, that has a method getMax/ get_max that retrieves the maximum value of stack in O(1).
Do not worry about using extra space.
