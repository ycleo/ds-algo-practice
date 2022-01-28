
// size O(1); isEmpty O(1); peek O(1); push O(logN); pop O(logN)

class PriorityQueue {
    constructor(comparator = (a, b) => a > b) {
        this._heap = [];
        this._comparator = comparator;
    }

    // find the heap size
    size() {
        return this._heap.length;
    }
    
    isEmpty() {
        return this._heap.length == 0;
    }

    peek() {
        return this._heap[0];
    }

    _parent(idx) {
        return Math.floor((idx - 1) / 2);
    }

    _leftChild(idx) {
        return idx * 2 + 1;
    }

    _rightChild(idx) {
        return idx * 2 + 2;
    }

    _compare(i, j) {
        return this._comparator(this._heap[i], this._heap[j]);
    }

    _swap(i, j) {
        [this._heap[i], this._heap[j]] = [this._heap[j], this._heap[i]];
    }

    _compareUp() {
        let nodeIdx = this.size() - 1;

        while(0 < nodeIdx && this._compare(nodeIdx, this._parent(nodeIdx))) {
            this._swap(nodeIdx, this._parent(nodeIdx));
            nodeIdx = this._parent(nodeIdx);
        }
    }

    _compareDown() {
        let nodeIdx = 0;
        while (
            (this._leftChild(nodeIdx) < this.size() 
             && this._compare(this._leftChild(nodeIdx), nodeIdx))
            || (this._rightChild(nodeIdx) < this.size()
             && this._compare(this._rightChild(nodeIdx), nodeIdx))
            ) {
                const greaterChild = 
                    this._leftChild(nodeIdx) < this.size()
                    && this._compare(this._leftChild(nodeIdx), this._rightChild(nodeIdx))
                    ? this._leftChild(nodeIdx)
                    : this._rightChild(nodeIdx);
                
                this._swap(greaterChild, nodeIdx);
                nodeIdx = greaterChild;
        }
    }

    push(val) {
        this._heap.push(val);
        this._compareUp();
        return this.size();
    }

    

    pop() {
        if(this.size() > 1)
            this._swap(0, this.size() - 1);

        const popNode = this._heap.pop();
        this._compareDown();
        return popNode;
    }
    
}

const pq = new PriorityQueue();
pq.push(15);
pq.push(12);
pq.push(50);
pq.push(7);
pq.push(40);
pq.push(22);

while(!pq.isEmpty()) {
  console.log(pq.pop());
}