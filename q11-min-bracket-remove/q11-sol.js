// LeetCode 1249:
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

// test cases
// 1. "a)bc(d)" => "abc(d)"
// 2. "(ab(c)d" => "(abc)d"  or  "ab(c)d"
// 3. "))((" => ""

// algorithm
// 1. create a stack and transfer the string into an array
// 2. traverse the string
//      if '(' => push into stack
//      if ')' 
//          if stack has a '(' => array[i] = ''
//          if stack has no item => stack.pop()        
// 3. process the stack  
// 4. return the array.join('')                

const minRemoveToMakeValid = function(s) {
    const stack = [];
    const arr = s.split('');  // O(n)
    
    for (let i = 0; i < s.length; i++) { // O(n)
        
        if (s[i] === '(') stack.push(i);
        
        else if (s[i] === ')') {
            if (stack.length === 0) arr[i]  = '';
            else stack.pop();   
        }
    }

    while (stack.length){  // O(n)
        arr[stack.pop()] = '';
    }
    return arr.join(''); // O(n)
}

// space: stack and arr => O(2n) => O(n)
// time: O(4n) => O(n)