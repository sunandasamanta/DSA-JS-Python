class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(element) {
        this.items.push(element);
    }

    dequeue() {
        return this.items.shift();
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }

    front() {
        return this.items[0];
    }

    print() {
        console.log(this.items.toString());
    }
}

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
console.log(queue.size()); // Output: 3
console.log(queue.isEmpty()); // Output: false
console.log(queue.front()); // Output: 1
queue.dequeue();
console.log(queue.front()); // Output: 2
queue.print(); // Output: 2,3
