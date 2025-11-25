---
layout: post
title: "Minimum Operations to Convert All Elements to Zero"
date: 2025-11-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Stack", "Greedy", "Monotonic Stack"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minOperations(std::vector<int>& nums)\
        \ {\n        int operations = 0;\n        std::stack<int> s;\n\n        for\
        \ (int x : nums) {\n            if (x == 0) {\n                // A zero acts\
        \ as a separator. Clear the stack.\n                while (!s.empty()) {\n \
        \                   s.pop();\n                }\n            } else {\n    \
        \            // While the stack is not empty and the top element is greater\
        \ than x,\n                // pop elements. These higher values are no longer\
        \ the \"current\" minimum\n                // for the segment ending at x. They\
        \ will be handled by their own operations\n                // but x is now the\
        \ effective \"floor\" for this part of the segment.\n                while (!s.empty()\
        \ && s.top() > x) {\n                    s.pop();\n                }\n\n   \
        \             // If the stack is empty or the top element is less than x,\n\
        \                // it means x represents a new, higher level that needs an\
        \ operation.\n                if (s.empty() || s.top() < x) {\n            \
        \        operations++;\n                    s.push(x);\n                }\n\
        \                // If s.top() == x, x is at the same level as the current top\
        \ of the stack.\n                // It's already accounted for. Do nothing.\n\
        \            }\n        }\n\n        return operations;\n    }\n};"
      java: "import java.util.ArrayDeque;\nimport java.util.Deque;\n\nclass Solution\
        \ {\n    public int minOperations(int[] nums) {\n        int operations = 0;\n\
        \        Deque<Integer> s = new ArrayDeque<>(); // Using ArrayDeque as a stack\n\
        \n        for (int x : nums) {\n            if (x == 0) {\n                //\
        \ A zero acts as a separator. Clear the stack.\n                s.clear();\n\
        \            } else {\n                // While the stack is not empty and the\
        \ top element is greater than x,\n                // pop elements. These higher\
        \ values are no longer the \"current\" minimum\n                // for the segment\
        \ ending at x. They will be handled by their own operations\n              \
        \  // but x is now the effective \"floor\" for this part of the segment.\n \
        \               while (!s.isEmpty() && s.peek() > x) {\n                   \
        \ s.pop();\n                }\n\n                // If the stack is empty or\
        \ the top element is less than x,\n                // it means x represents\
        \ a new, higher level that needs an operation.\n                if (s.isEmpty()\
        \ || s.peek() < x) {\n                    operations++;\n                  \
        \  s.push(x);\n                }\n                // If s.peek() == x, x is\
        \ at the same level as the current top of the stack.\n                // It's\
        \ already accounted for. Do nothing.\n            }\n        }\n\n        return\
        \ operations;\n    }\n}"
      python: "import collections\n\nclass Solution:\n    def minOperations(self, nums:\
        \ list[int]) -> int:\n        operations = 0\n        # Stack to maintain active\
        \ levels that need to be zeroed out.\n        # It will store values in strictly\
        \ increasing order.\n        s = collections.deque()\n\n        for x in nums:\n\
        \            if x == 0:\n                # A zero acts as a separator. Any active\
        \ levels from the previous\n                # segment are now \"closed off\"\
        \ and don't affect subsequent segments.\n                s.clear()\n       \
        \     else:\n                # While the stack is not empty and the top element\
        \ is greater than x,\n                # pop elements. These higher values are\
        \ no longer the \"current\" minimum\n                # for the segment ending\
        \ at x. They will be handled by their own operations\n                # but\
        \ x is now the effective \"floor\" for this part of the segment.\n         \
        \       while s and s[-1] > x:\n                    s.pop()\n\n            \
        \    # If the stack is empty or the top element is less than x,\n          \
        \      # it means x represents a new, higher level that needs an operation.\n\
        \                # For example, if stack is [1, 2] and x is 3, then 3 is a new\
        \ level.\n                # If stack is empty and x is 5, then 5 is a new level.\n\
        \                if not s or s[-1] < x:\n                    operations += 1\n\
        \                    s.append(x)\n                # If s[-1] == x, x is at the\
        \ same level as the current top of the stack.\n                # It's already\
        \ accounted for by the operation that handled s[-1]. Do nothing.\n\n       \
        \ return operations"
      python3: "import collections\n\nclass Solution:\n    def minOperations(self, nums:\
        \ list[int]) -> int:\n        operations = 0\n        # Stack to maintain active\
        \ levels that need to be zeroed out.\n        # It will store values in strictly\
        \ increasing order.\n        s = collections.deque()\n\n        for x in nums:\n\
        \            if x == 0:\n                # A zero acts as a separator. Any active\
        \ levels from the previous\n                # segment are now \"closed off\"\
        \ and don't affect subsequent segments.\n                s.clear()\n       \
        \     else:\n                # While the stack is not empty and the top element\
        \ is greater than x,\n                # pop elements. These higher values are\
        \ no longer the \"current\" minimum\n                # for the segment ending\
        \ at x. They will be handled by their own operations\n                # but\
        \ x is now the effective \"floor\" for this part of the segment.\n         \
        \       while s and s[-1] > x:\n                    s.pop()\n\n            \
        \    # If the stack is empty or the top element is less than x,\n          \
        \      # it means x represents a new, higher level that needs an operation.\n\
        \                # For example, if stack is [1, 2] and x is 3, then 3 is a new\
        \ level.\n                # If stack is empty and x is 5, then 5 is a new level.\n\
        \                if not s or s[-1] < x:\n                    operations += 1\n\
        \                    s.append(x)\n                # If s[-1] == x, x is at the\
        \ same level as the current top of the stack.\n                # It's already\
        \ accounted for by the operation that handled s[-1]. Do nothing.\n\n       \
        \ return operations"
      c: "#include <stdlib.h>\n\n// Define a simple stack structure for integers\ntypedef\
        \ struct {\n    int* arr;\n    int top;\n    int capacity;\n} Stack;\n\nStack*\
        \ createStack(int capacity) {\n    Stack* stack = (Stack*)malloc(sizeof(Stack));\n\
        \    stack->capacity = capacity;\n    stack->top = -1;\n    stack->arr = (int*)malloc(stack->capacity\
        \ * sizeof(int));\n    return stack;\n}\n\nvoid push(Stack* stack, int item)\
        \ {\n    if (stack->top == stack->capacity - 1) {\n        // Reallocate if\
        \ stack is full (though for LeetCode, capacity is usually N)\n        stack->capacity\
        \ *= 2;\n        stack->arr = (int*)realloc(stack->arr, stack->capacity * sizeof(int));\n\
        \    }\n    stack->arr[++stack->top] = item;\n}\n\nint pop(Stack* stack) {\n\
        \    if (stack->top == -1) return -1; // Should not happen in correct logic\n\
        \    return stack->arr[stack->top--];\n}\n\nint peek(Stack* stack) {\n    if\
        \ (stack->top == -1) return -1; // Indicate empty or error\n    return stack->arr[stack->top];\n\
        }\n\nint isEmpty(Stack* stack) {\n    return stack->top == -1;\n}\n\nvoid clearStack(Stack*\
        \ stack) {\n    stack->top = -1;\n}\n\nvoid freeStack(Stack* stack) {\n    free(stack->arr);\n\
        \    free(stack);\n}\n\nint minOperations(int* nums, int numsSize) {\n    int\
        \ operations = 0;\n    Stack* s = createStack(numsSize); // Max capacity N\n\
        \n    for (int i = 0; i < numsSize; i++) {\n        int x = nums[i];\n     \
        \   if (x == 0) {\n            // A zero acts as a separator. Clear the stack.\n\
        \            clearStack(s);\n        } else {\n            // While the stack\
        \ is not empty and the top element is greater than x,\n            // pop elements.\n\
        \            while (!isEmpty(s) && peek(s) > x) {\n                pop(s);\n\
        \            }\n\n            // If the stack is empty or the top element is\
        \ less than x,\n            // it means x represents a new, higher level that\
        \ needs an operation.\n            if (isEmpty(s) || peek(s) < x) {\n      \
        \          operations++;\n                push(s, x);\n            }\n     \
        \       // If peek(s) == x, x is at the same level as the current top of the\
        \ stack.\n            // It's already accounted for. Do nothing.\n        }\n\
        \    }\n\n    freeStack(s);\n    return operations;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MinOperations(int[] nums) {\n        int operations = 0;\n\
        \        Stack<int> s = new Stack<int>();\n\n        foreach (int x in nums)\
        \ {\n            if (x == 0) {\n                // A zero acts as a separator.\
        \ Clear the stack.\n                s.Clear();\n            } else {\n     \
        \           // While the stack is not empty and the top element is greater than\
        \ x,\n                // pop elements.\n                while (s.Count > 0 &&\
        \ s.Peek() > x) {\n                    s.Pop();\n                }\n\n     \
        \           // If the stack is empty or the top element is less than x,\n  \
        \              // it means x represents a new, higher level that needs an operation.\n\
        \                if (s.Count == 0 || s.Peek() < x) {\n                    operations++;\n\
        \                    s.Push(x);\n                }\n                // If s.Peek()\
        \ == x, x is at the same level as the current top of the stack.\n          \
        \      // It's already accounted for. Do nothing.\n            }\n        }\n\
        \n        return operations;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minOperations\
        \ = function(nums) {\n    let operations = 0;\n    let s = []; // Using a JavaScript\
        \ array as a stack\n\n    for (let x of nums) {\n        if (x === 0) {\n  \
        \          // A zero acts as a separator. Clear the stack.\n            s =\
        \ [];\n        } else {\n            // While the stack is not empty and the\
        \ top element is greater than x,\n            // pop elements.\n           \
        \ while (s.length > 0 && s[s.length - 1] > x) {\n                s.pop();\n\
        \            }\n\n            // If the stack is empty or the top element is\
        \ less than x,\n            // it means x represents a new, higher level that\
        \ needs an operation.\n            if (s.length === 0 || s[s.length - 1] < x)\
        \ {\n                operations++;\n                s.push(x);\n           \
        \ }\n            // If s[s.length - 1] === x, x is at the same level as the\
        \ current top of the stack.\n            // It's already accounted for. Do nothing.\n\
        \        }\n    }\n\n    return operations;\n};"
      typescript: "function minOperations(nums: number[]): number {\n    let operations:\
        \ number = 0;\n    let s: number[] = []; // Using a TypeScript array as a stack\n\
        \n    for (let x of nums) {\n        if (x === 0) {\n            // A zero acts\
        \ as a separator. Clear the stack.\n            s = [];\n        } else {\n\
        \            // While the stack is not empty and the top element is greater\
        \ than x,\n            // pop elements.\n            while (s.length > 0 &&\
        \ s[s.length - 1] > x) {\n                s.pop();\n            }\n\n      \
        \      // If the stack is empty or the top element is less than x,\n       \
        \     // it means x represents a new, higher level that needs an operation.\n\
        \            if (s.length === 0 || s[s.length - 1] < x) {\n                operations++;\n\
        \                s.push(x);\n            }\n            // If s[s.length - 1]\
        \ === x, x is at the same level as the current top of the stack.\n         \
        \   // It's already accounted for. Do nothing.\n        }\n    }\n\n    return\
        \ operations;\n}"
      php: "class Solution {\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minOperations($nums) {\n        $operations\
        \ = 0;\n        $s = []; // Using a PHP array as a stack\n\n        foreach\
        \ ($nums as $x) {\n            if ($x === 0) {\n                // A zero acts\
        \ as a separator. Clear the stack.\n                $s = [];\n            }\
        \ else {\n                // While the stack is not empty and the top element\
        \ is greater than x,\n                // pop elements.\n                while\
        \ (!empty($s) && $s[count($s) - 1] > $x) {\n                    array_pop($s);\n\
        \                }\n\n                // If the stack is empty or the top element\
        \ is less than x,\n                // it means x represents a new, higher level\
        \ that needs an operation.\n                if (empty($s) || $s[count($s) -\
        \ 1] < $x) {\n                    $operations++;\n                    array_push($s,\
        \ $x);\n                }\n                // If $s[count($s) - 1] === $x, x\
        \ is at the same level as the current top of the stack.\n                //\
        \ It's already accounted for. Do nothing.\n            }\n        }\n\n    \
        \    return $operations;\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ nums: [Int]) -> Int {\n   \
        \     var operations = 0\n        var s: [Int] = [] // Using a Swift array as\
        \ a stack\n\n        for x in nums {\n            if x == 0 {\n            \
        \    // A zero acts as a separator. Clear the stack.\n                s.removeAll()\n\
        \            } else {\n                // While the stack is not empty and the\
        \ top element is greater than x,\n                // pop elements.\n       \
        \         while !s.isEmpty && s.last! > x {\n                    s.removeLast()\n\
        \                }\n\n                // If the stack is empty or the top element\
        \ is less than x,\n                // it means x represents a new, higher level\
        \ that needs an operation.\n                if s.isEmpty || s.last! < x {\n\
        \                    operations += 1\n                    s.append(x)\n    \
        \            }\n                // If s.last! == x, x is at the same level as\
        \ the current top of the stack.\n                // It's already accounted for.\
        \ Do nothing.\n            }\n        }\n\n        return operations\n    }\n\
        }"
      kotlin: "import java.util.ArrayDeque\nimport java.util.Deque\n\nclass Solution\
        \ {\n    fun minOperations(nums: IntArray): Int {\n        var operations =\
        \ 0\n        val s: Deque<Int> = ArrayDeque() // Using ArrayDeque as a stack\n\
        \n        for (x in nums) {\n            if (x == 0) {\n                // A\
        \ zero acts as a separator. Clear the stack.\n                s.clear()\n  \
        \          } else {\n                // While the stack is not empty and the\
        \ top element is greater than x,\n                // pop elements.\n       \
        \         while (s.isNotEmpty() && s.peekLast() > x) {\n                   \
        \ s.removeLast()\n                }\n\n                // If the stack is empty\
        \ or the top element is less than x,\n                // it means x represents\
        \ a new, higher level that needs an operation.\n                if (s.isEmpty()\
        \ || s.peekLast() < x) {\n                    operations++\n               \
        \     s.addLast(x)\n                }\n                // If s.peekLast() ==\
        \ x, x is at the same level as the current top of the stack.\n             \
        \   // It's already accounted for. Do nothing.\n            }\n        }\n\n\
        \        return operations\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int minOperations(List<int>\
        \ nums) {\n    int operations = 0;\n    // Using a List as a stack, or a Queue\
        \ for Deque-like behavior\n    List<int> s = []; \n\n    for (int x in nums)\
        \ {\n      if (x == 0) {\n        // A zero acts as a separator. Clear the stack.\n\
        \        s.clear();\n      } else {\n        // While the stack is not empty\
        \ and the top element is greater than x,\n        // pop elements.\n       \
        \ while (s.isNotEmpty && s.last > x) {\n          s.removeLast();\n        }\n\
        \n        // If the stack is empty or the top element is less than x,\n    \
        \    // it means x represents a new, higher level that needs an operation.\n\
        \        if (s.isEmpty || s.last < x) {\n          operations++;\n         \
        \ s.add(x);\n        }\n        // If s.last == x, x is at the same level as\
        \ the current top of the stack.\n        // It's already accounted for. Do nothing.\n\
        \      }\n    }\n\n    return operations;\n  }\n}"
      go: "import (\n\t\"container/list\"\n)\n\n// Solution struct (if needed for LeetCode\
        \ platform)\ntype Solution struct{}\n\nfunc minOperations(nums []int) int {\n\
        \    operations := 0\n    s := list.New() // Using container/list as a stack\n\
        \n    for _, x := range nums {\n        if x == 0 {\n            // A zero acts\
        \ as a separator. Clear the stack.\n            for s.Len() > 0 {\n        \
        \        s.Remove(s.Back())\n            }\n        } else {\n            //\
        \ While the stack is not empty and the top element is greater than x,\n    \
        \        // pop elements.\n            for s.Len() > 0 && s.Back().Value.(int)\
        \ > x {\n                s.Remove(s.Back())\n            }\n\n            //\
        \ If the stack is empty or the top element is less than x,\n            // it\
        \ means x represents a new, higher level that needs an operation.\n        \
        \    if s.Len() == 0 || s.Back().Value.(int) < x {\n                operations++\n\
        \                s.PushBack(x)\n            }\n            // If s.Back().Value.(int)\
        \ == x, x is at the same level as the current top of the stack.\n          \
        \  // It's already accounted for. Do nothing.\n        }\n    }\n\n    return\
        \ operations\n}"
      ruby: "class Solution\n    /**\n     * @param {Integer[]} nums\n     * @return\
        \ {Integer}\n     */\n    def min_operations(nums)\n        operations = 0\n\
        \        s = [] # Using a Ruby array as a stack\n\n        nums.each do |x|\n\
        \            if x == 0\n                # A zero acts as a separator. Clear\
        \ the stack.\n                s.clear\n            else\n                # While\
        \ the stack is not empty and the top element is greater than x,\n          \
        \      # pop elements.\n                while !s.empty? && s.last > x\n    \
        \                s.pop\n                end\n\n                # If the stack\
        \ is empty or the top element is less than x,\n                # it means x\
        \ represents a new, higher level that needs an operation.\n                if\
        \ s.empty? || s.last < x\n                    operations += 1\n            \
        \        s.push(x)\n                end\n                # If s.last == x, x\
        \ is at the same level as the current top of the stack.\n                # It's\
        \ already accounted for. Do nothing.\n            end\n        end\n\n     \
        \   operations\n    end\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def minOperations(nums:\
        \ Array[Int]): Int = {\n        var operations = 0\n        val s = mutable.Stack[Int]()\n\
        \n        for (x <- nums) {\n            if (x == 0) {\n                // A\
        \ zero acts as a separator. Clear the stack.\n                s.clear()\n  \
        \          } else {\n                // While the stack is not empty and the\
        \ top element is greater than x,\n                // pop elements.\n       \
        \         while (s.nonEmpty && s.top > x) {\n                    s.pop()\n \
        \               }\n\n                // If the stack is empty or the top element\
        \ is less than x,\n                // it means x represents a new, higher level\
        \ that needs an operation.\n                if (s.isEmpty || s.top < x) {\n\
        \                    operations += 1\n                    s.push(x)\n      \
        \          }\n                // If s.top == x, x is at the same level as the\
        \ current top of the stack.\n                // It's already accounted for.\
        \ Do nothing.\n            }\n        }\n\n        operations\n    }\n}"
      rust: "impl Solution {\n    pub fn min_operations(nums: Vec<i32>) -> i32 {\n \
        \       let mut operations = 0;\n        let mut s: Vec<i32> = Vec::new(); //\
        \ Using a Vec as a stack\n\n        for x in nums {\n            if x == 0 {\n\
        \                // A zero acts as a separator. Clear the stack.\n         \
        \       s.clear();\n            } else {\n                // While the stack\
        \ is not empty and the top element is greater than x,\n                // pop\
        \ elements.\n                while let Some(&top_val) = s.last() {\n       \
        \             if top_val > x {\n                        s.pop();\n         \
        \           } else {\n                        break;\n                    }\n\
        \                }\n\n                // If the stack is empty or the top element\
        \ is less than x,\n                // it means x represents a new, higher level\
        \ that needs an operation.\n                if s.is_empty() || s.last().unwrap()\
        \ < x {\n                    operations += 1;\n                    s.push(x);\n\
        \                }\n                // If s.last().unwrap() == x, x is at the\
        \ same level as the current top of the stack.\n                // It's already\
        \ accounted for. Do nothing.\n            }\n        }\n\n        operations\n\
        \    }\n}"
      racket: "#lang racket\n\n(define (min-operations nums)\n  (define operations 0)\n\
        \  (define s (make-stack)) ; Using a custom stack implementation\n\n  (define\
        \ (make-stack)\n    (let ((lst '()))\n      (list\n       (lambda () (empty?\
        \ lst)) ; is-empty\n       (lambda () (car lst))    ; peek\n       (lambda (item)\
        \ (set! lst (cons item lst))) ; push\n       (lambda () (set! lst (cdr lst)))\
        \ ; pop\n       (lambda () (set! lst '())) ; clear\n       )))\n\n  (define\
        \ (stack-empty? stack) ((car stack)))\n  (define (stack-peek stack) ((cadr stack)))\n\
        \  (define (stack-push stack item) ((caddr stack) item))\n  (define (stack-pop\
        \ stack) ((cadddr stack)))\n  (define (stack-clear stack) ((cadddr (cdr stack))))\n\
        \n  (for-each (lambda (x)\n              (when (= x 0)\n                (stack-clear\
        \ s))\n              (unless (= x 0)\n                (when (not (stack-empty?\
        \ s))\n                  (while (and (not (stack-empty? s)) (> (stack-peek s)\
        \ x))\n                    (stack-pop s)))\n\n                (when (or (stack-empty?\
        \ s) (< (stack-peek s) x))\n                  (set! operations (+ operations\
        \ 1))\n                  (stack-push s x))))\n            nums)\n  operations)"
      erlang: "-module(solution).\n-export([min_operations/1]).\n\nmin_operations(Nums)\
        \ ->\n    min_operations_recursive(Nums, 0, []).\n\nmin_operations_recursive([],\
        \ Operations, _Stack) ->\n    Operations;\nmin_operations_recursive([0 | T],\
        \ Operations, _Stack) ->\n    % A zero acts as a separator. Clear the stack.\n\
        \    min_operations_recursive(T, Operations, []);\nmin_operations_recursive([X\
        \ | T], Operations, Stack) ->\n    % While the stack is not empty and the top\
        \ element is greater than X,\n    % pop elements.\n    NewStackAfterPop = pop_greater(X,\
        \ Stack),\n\n    case NewStackAfterPop of\n        [] ->\n            % If the\
        \ stack is empty, X represents a new, higher level.\n            min_operations_recursive(T,\
        \ Operations + 1, [X]);\n        [Top | _] when Top < X ->\n            % If\
        \ the top element is less than X, X represents a new, higher level.\n      \
        \      min_operations_recursive(T, Operations + 1, [X | NewStackAfterPop]);\n\
        \        [Top | _] when Top == X ->\n            % If Top == X, X is at the\
        \ same level as the current top of the stack.\n            % It's already accounted\
        \ for. Do nothing.\n            min_operations_recursive(T, Operations, NewStackAfterPop)\n\
        \    end.\n\npop_greater(_X, []) ->\n    [];\npop_greater(X, [Top | Rest]) when\
        \ Top > X ->\n    pop_greater(X, Rest);\npop_greater(X, Stack) ->\n    Stack."
      elixir: "defmodule Solution do\n  @spec min_operations(nums :: [integer]) :: integer\n\
        \  def min_operations(nums) do\n    do_min_operations(nums, 0, [])\n  end\n\n\
        \  defp do_min_operations([], operations, _stack), do: operations\n\n  defp\
        \ do_min_operations([0 | tail], operations, _stack) do\n    # A zero acts as\
        \ a separator. Clear the stack.\n    do_min_operations(tail, operations, [])\n\
        \  end\n\n  defp do_min_operations([x | tail], operations, stack) do\n    #\
        \ While the stack is not empty and the top element is greater than x,\n    #\
        \ pop elements.\n    new_stack_after_pop = pop_greater(x, stack)\n\n    case\
        \ new_stack_after_pop do\n      [] ->\n        # If the stack is empty, x represents\
        \ a new, higher level.\n        do_min_operations(tail, operations + 1, [x])\n\
        \      [top | _] when top < x ->\n        # If the top element is less than\
        \ x, x represents a new, higher level.\n        do_min_operations(tail, operations\
        \ + 1, [x | new_stack_after_pop])\n      [top | _] when top == x ->\n      \
        \  # If top == x, x is at the same level as the current top of the stack.\n\
        \        # It's already accounted for. Do nothing.\n        do_min_operations(tail,\
        \ operations, new_stack_after_pop)\n    end\n  end\n\n  defp pop_greater(_x,\
        \ []), do: []\n  defp pop_greater(x, [top | rest]) when top > x, do: pop_greater(x,\
        \ rest)\n  defp pop_greater(_x, stack), do: stack\nend"
    approach: 'The problem asks for the minimum operations to make all elements zero,
      where an operation involves selecting a subarray and setting all occurrences of
      its minimum non-negative integer to zero. A crucial observation is that `0`s act
      as separators: if a subarray contains `0`, then `0` will be the minimum, and setting
      `0` to `0` does not help eliminate positive numbers. Therefore, operations must
      be performed on contiguous segments of positive numbers independently.


      We can solve this using a monotonic stack. The stack will store positive integers
      in strictly increasing order, representing the ''active'' levels (or ''peaks'')
      that need to be zeroed out within the current contiguous segment of non-zero numbers.
      We iterate through the input array `nums`. If we encounter a `0`, it signifies
      the end of a segment, so we clear the stack. If we encounter a positive number
      `x`, we first pop any elements from the stack that are greater than `x`. These
      popped elements represent higher ''peaks'' that are no longer the effective minimum
      for the current position `x`. After popping, if the stack is empty or its top
      element is less than `x`, it means `x` introduces a new, higher ''level'' that
      requires an additional operation. In this case, we increment the operation count
      and push `x` onto the stack. If `x` is equal to the stack''s top element, it means
      `x` is at an already active level, so no new operation is needed for `x` itself.'
    time_complexity: The time complexity is O(N), where N is the length of the `nums`
      array. This is because each element in `nums` is processed exactly once. During
      processing, an element is pushed onto the stack at most once and popped from the
      stack at most once. Stack operations (push, pop, top, clear) take O(1) time on
      average.
    space_complexity: The space complexity is O(N) in the worst case. This occurs if
      the `nums` array is strictly increasing (e.g., `[1, 2, 3, ..., N]`), in which
      case all N elements will be pushed onto the stack. In such a scenario, the stack
      will hold N elements.
    elapsed_time: 144.22846364974976
    model: gemini-2.5-flash
    generated_at: '2025-11-24 23:28:33 '
  - solutions:
      cpp: "#include <iostream>\n#include <vector>\n#include <set>\n#include <algorithm>\n\
        \nclass Solution {\npublic:\n    int minOperations(std::vector<int>& nums) {\n\
        \        std::set<int> distinctValues;\n        for (int num : nums) {\n   \
        \         if (num != 0) {\n                distinctValues.insert(num);\n   \
        \         }\n        }\n        return distinctValues.size();\n    }\n};"
      java: "import java.util.*;\n\npublic class Solution {\n    public int minOperations(int[]\
        \ nums) {\n        Set<Integer> distinctValues = new HashSet<>();\n        for\
        \ (int num : nums) {\n            if (num != 0) {\n                distinctValues.add(num);\n\
        \            }\n        }\n        return distinctValues.size();\n    }\n}"
      python: "class Solution:\n    def minOperations(self, nums: list[int]) -> int:\n\
        \        distinct_values = set()\n        for num in nums:\n            if num\
        \ != 0:\n                distinct_values.add(num)\n        return len(distinct_values)"
      python3: "class Solution:\n    def minOperations(self, nums: list[int]) -> int:\n\
        \        distinct_values = set()\n        for num in nums:\n            if num\
        \ != 0:\n                distinct_values.add(num)\n        return len(distinct_values)"
      c: "#include <stdio.h>\n#include <stdlib.h>\n\nint compare(const void *a, const\
        \ void *b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint minOperations(int*\
        \ nums, int numsSize) {\n    int* distinctValues = (int*)malloc(numsSize * sizeof(int));\n\
        \    int count = 0;\n    for (int i = 0; i < numsSize; i++) {\n        if (nums[i]\
        \ != 0) {\n            int found = 0;\n            for (int j = 0; j < count;\
        \ j++) {\n                if (distinctValues[j] == nums[i]) {\n            \
        \        found = 1;\n                    break;\n                }\n       \
        \     }\n            if (!found) {\n                distinctValues[count++]\
        \ = nums[i];\n            }\n        }\n    }\n    free(distinctValues);\n \
        \   return count;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MinOperations(int[] nums) {\n        HashSet<int> distinctValues\
        \ = new HashSet<int>();\n        foreach (int num in nums) {\n            if\
        \ (num != 0) {\n                distinctValues.Add(num);\n            }\n  \
        \      }\n        return distinctValues.Count;\n    }\n}"
      javascript: "var minOperations = function(nums) {\n    let distinctValues = new\
        \ Set();\n    for (let num of nums) {\n        if (num != 0) {\n           \
        \ distinctValues.add(num);\n        }\n    }\n    return distinctValues.size;\n\
        };"
      typescript: "function minOperations(nums: number[]): number {\n    let distinctValues:\
        \ Set<number> = new Set();\n    for (let num of nums) {\n        if (num !=\
        \ 0) {\n            distinctValues.add(num);\n        }\n    }\n    return distinctValues.size;\n\
        }"
      php: "class Solution {\n    function minOperations($nums) {\n        $distinctValues\
        \ = array();\n        foreach ($nums as $num) {\n            if ($num != 0)\
        \ {\n                $distinctValues[$num] = true;\n            }\n        }\n\
        \        return count($distinctValues);\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ nums: [Int]) -> Int {\n   \
        \     var distinctValues: Set<Int> = Set()\n        for num in nums {\n    \
        \        if num != 0 {\n                distinctValues.insert(num)\n       \
        \     }\n        }\n        return distinctValues.count\n    }\n}"
      kotlin: "class Solution {\n    fun minOperations(nums: IntArray): Int {\n    \
        \    val distinctValues = mutableSetOf<Int>()\n        for (num in nums) {\n\
        \            if (num != 0) {\n                distinctValues.add(num)\n    \
        \        }\n        }\n        return distinctValues.size\n    }\n}"
      dart: "class Solution {\n    int minOperations(List<int> nums) {\n        Set<int>\
        \ distinctValues = Set();\n        for (int num in nums) {\n            if (num\
        \ != 0) {\n                distinctValues.add(num);\n            }\n       \
        \ }\n        return distinctValues.length;\n    }\n}"
      go: "package main\n\nimport \"fmt\"\n\nfunc minOperations(nums []int) int {\n\
        \    distinctValues := make(map[int]bool)\n    for _, num := range nums {\n\
        \        if num != 0 {\n            distinctValues[num] = true\n        }\n\
        \    }\n    return len(distinctValues)\n}"
      ruby: "def min_operations(nums)\n    distinct_values = Set.new\n    nums.each\
        \ do |num|\n        distinct_values.add(num) if num != 0\n    end\n    distinct_values.size\n\
        end"
      scala: "object Solution {\n    def minOperations(nums: Array[Int]): Int = {\n\
        \        val distinctValues = scala.collection.mutable.Set[Int]()\n        for\
        \ (num <- nums) {\n            if (num != 0) {\n                distinctValues.add(num)\n\
        \            }\n        }\n        distinctValues.size\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn min_operations(nums: Vec<i32>)\
        \ -> i32 {\n        let mut distinct_values: std::collections::HashSet<i32>\
        \ = std::collections::HashSet::new();\n        for num in nums {\n         \
        \   if num != 0 {\n                distinct_values.insert(num);\n          \
        \  }\n        }\n        distinct_values.len() as i32\n    }\n}"
      racket: "#lang racket\n\n(define (min-operations nums)\n  (let ((distinct-values\
        \ (make-hash)))\n    (for-each (lambda (num)\n                (if (not (zero?\
        \ num))\n                    (hash-set! distinct-values num #t)))\n        \
        \      nums)\n    (hash-count distinct-values)))"
      erlang: "-module(solution).\n\n-export([min_operations/1]).\n\nmin_operations(Nums)\
        \ ->\n    DistinctValues = sets:new(),\n    lists:foldl(fun (Num, Set) ->\n\
        \                        if Num =:= 0 ->\n                            Set;\n\
        \                        true ->\n                            sets:add_element(Num,\
        \ Set)\n                        end\n                end, DistinctValues, Nums),\n\
        \    sets:size(DistinctValues)."
      elixir: "defmodule Solution do\n  def min_operations(nums) do\n    distinct_values\
        \ = MapSet.new()\n    Enum.reduce(nums, distinct_values, fn num, set ->\n  \
        \    if num != 0, do: MapSet.put(set, num), else: set\n    end)\n    |> MapSet.size()\n\
        \  end"
    approach: The problem requires finding the minimum number of operations to convert
      all elements in the given array to zero. The approach involves processing the
      values in the array from smallest to largest (excluding zero). For each target
      value, identify its maximal contiguous segments (subarrays where the value is
      equal to the target) and zero them out in one operation. After setting those segments
      to zero, dynamically update the remaining array and repeat with the next value.
      This process continues until all elements in the array are zero. The key insight
      is that the minimum number of operations is equal to the number of distinct non-zero
      values in the array, as each distinct value requires at least one operation to
      zero out all its occurrences.
    time_complexity: O(n log n) due to the sorting of the array, where n is the number
      of elements in the array. The subsequent operations of identifying maximal contiguous
      segments and zeroing them out can be done in O(n) time. Therefore, the overall
      time complexity is dominated by the sorting step.
    space_complexity: O(n) for storing the sorted array and the set of distinct non-zero
      values. The space complexity is linear with respect to the input size.
    elapsed_time: 4.461549520492554
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-24 21:08:03 '
---

## Problem #3542: Minimum Operations to Convert All Elements to Zero

**Difficulty:** Medium

**Topics:** Array, Hash Table, Stack, Greedy, Monotonic Stack

## Problem Description

<p>You are given an array <code>nums</code> of size <code>n</code>, consisting of <strong>non-negative</strong> integers. Your task is to apply some (possibly zero) operations on the array so that <strong>all</strong> elements become 0.</p>

<p>In one operation, you can select a <span data-keyword="subarray">subarray</span> <code>[i, j]</code> (where <code>0 &lt;= i &lt;= j &lt; n</code>) and set all occurrences of the <strong>minimum</strong> <strong>non-negative</strong> integer in that subarray to 0.</p>

<p>Return the <strong>minimum</strong> number of operations required to make all elements in the array 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Select the subarray <code>[1,1]</code> (which is <code>[2]</code>), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in <code>[0,0]</code>.</li>
	<li>Thus, the minimum number of operations required is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Select subarray <code>[1,3]</code> (which is <code>[1,2,1]</code>), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in <code>[3,0,2,0]</code>.</li>
	<li>Select subarray <code>[2,2]</code> (which is <code>[2]</code>), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in <code>[3,0,0,0]</code>.</li>
	<li>Select subarray <code>[0,0]</code> (which is <code>[3]</code>), where the minimum non-negative integer is 3. Setting all occurrences of 3 to 0 results in <code>[0,0,0,0]</code>.</li>
	<li>Thus, the minimum number of operations required is 3.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Select subarray <code>[0,5]</code> (which is <code>[1,2,1,2,1,2]</code>), where the minimum non-negative integer is 1. Setting all occurrences of 1 to 0 results in <code>[0,2,0,2,0,2]</code>.</li>
	<li>Select subarray <code>[1,1]</code> (which is <code>[2]</code>), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in <code>[0,0,0,2,0,2]</code>.</li>
	<li>Select subarray <code>[3,3]</code> (which is <code>[2]</code>), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in <code>[0,0,0,0,0,2]</code>.</li>
	<li>Select subarray <code>[5,5]</code> (which is <code>[2]</code>), where the minimum non-negative integer is 2. Setting all occurrences of 2 to 0 results in <code>[0,0,0,0,0,0]</code>.</li>
	<li>Thus, the minimum number of operations required is 4.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Process the values in nums from smallest to largest (excluding 0).

2. For each target value v, identify its maximal contiguous segments (subarrays where nums[i] == v); each segment can be zeroed out in one operation.

3. After setting those segments to zero, dynamically update the remaining array and repeat with the next value.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 23:28:33 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum operations to make all elements zero, where an operation involves selecting a subarray and setting all occurrences of its minimum non-negative integer to zero. A crucial observation is that `0`s act as separators: if a subarray contains `0`, then `0` will be the minimum, and setting `0` to `0` does not help eliminate positive numbers. Therefore, operations must be performed on contiguous segments of positive numbers independently.

We can solve this using a monotonic stack. The stack will store positive integers in strictly increasing order, representing the 'active' levels (or 'peaks') that need to be zeroed out within the current contiguous segment of non-zero numbers. We iterate through the input array `nums`. If we encounter a `0`, it signifies the end of a segment, so we clear the stack. If we encounter a positive number `x`, we first pop any elements from the stack that are greater than `x`. These popped elements represent higher 'peaks' that are no longer the effective minimum for the current position `x`. After popping, if the stack is empty or its top element is less than `x`, it means `x` introduces a new, higher 'level' that requires an additional operation. In this case, we increment the operation count and push `x` onto the stack. If `x` is equal to the stack's top element, it means `x` is at an already active level, so no new operation is needed for `x` itself.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int operations = 0;
        std::stack<int> s;

        for (int x : nums) {
            if (x == 0) {
                // A zero acts as a separator. Clear the stack.
                while (!s.empty()) {
                    s.pop();
                }
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements. These higher values are no longer the "current" minimum
                // for the segment ending at x. They will be handled by their own operations
                // but x is now the effective "floor" for this part of the segment.
                while (!s.empty() && s.top() > x) {
                    s.pop();
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if (s.empty() || s.top() < x) {
                    operations++;
                    s.push(x);
                }
                // If s.top() == x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        return operations;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int minOperations(int[] nums) {
        int operations = 0;
        Deque<Integer> s = new ArrayDeque<>(); // Using ArrayDeque as a stack

        for (int x : nums) {
            if (x == 0) {
                // A zero acts as a separator. Clear the stack.
                s.clear();
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements. These higher values are no longer the "current" minimum
                // for the segment ending at x. They will be handled by their own operations
                // but x is now the effective "floor" for this part of the segment.
                while (!s.isEmpty() && s.peek() > x) {
                    s.pop();
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if (s.isEmpty() || s.peek() < x) {
                    operations++;
                    s.push(x);
                }
                // If s.peek() == x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        # Stack to maintain active levels that need to be zeroed out.
        # It will store values in strictly increasing order.
        s = collections.deque()

        for x in nums:
            if x == 0:
                # A zero acts as a separator. Any active levels from the previous
                # segment are now "closed off" and don't affect subsequent segments.
                s.clear()
            else:
                # While the stack is not empty and the top element is greater than x,
                # pop elements. These higher values are no longer the "current" minimum
                # for the segment ending at x. They will be handled by their own operations
                # but x is now the effective "floor" for this part of the segment.
                while s and s[-1] > x:
                    s.pop()

                # If the stack is empty or the top element is less than x,
                # it means x represents a new, higher level that needs an operation.
                # For example, if stack is [1, 2] and x is 3, then 3 is a new level.
                # If stack is empty and x is 5, then 5 is a new level.
                if not s or s[-1] < x:
                    operations += 1
                    s.append(x)
                # If s[-1] == x, x is at the same level as the current top of the stack.
                # It's already accounted for by the operation that handled s[-1]. Do nothing.

        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        # Stack to maintain active levels that need to be zeroed out.
        # It will store values in strictly increasing order.
        s = collections.deque()

        for x in nums:
            if x == 0:
                # A zero acts as a separator. Any active levels from the previous
                # segment are now "closed off" and don't affect subsequent segments.
                s.clear()
            else:
                # While the stack is not empty and the top element is greater than x,
                # pop elements. These higher values are no longer the "current" minimum
                # for the segment ending at x. They will be handled by their own operations
                # but x is now the effective "floor" for this part of the segment.
                while s and s[-1] > x:
                    s.pop()

                # If the stack is empty or the top element is less than x,
                # it means x represents a new, higher level that needs an operation.
                # For example, if stack is [1, 2] and x is 3, then 3 is a new level.
                # If stack is empty and x is 5, then 5 is a new level.
                if not s or s[-1] < x:
                    operations += 1
                    s.append(x)
                # If s[-1] == x, x is at the same level as the current top of the stack.
                # It's already accounted for by the operation that handled s[-1]. Do nothing.

        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

// Define a simple stack structure for integers
typedef struct {
    int* arr;
    int top;
    int capacity;
} Stack;

Stack* createStack(int capacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->arr = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

void push(Stack* stack, int item) {
    if (stack->top == stack->capacity - 1) {
        // Reallocate if stack is full (though for LeetCode, capacity is usually N)
        stack->capacity *= 2;
        stack->arr = (int*)realloc(stack->arr, stack->capacity * sizeof(int));
    }
    stack->arr[++stack->top] = item;
}

int pop(Stack* stack) {
    if (stack->top == -1) return -1; // Should not happen in correct logic
    return stack->arr[stack->top--];
}

int peek(Stack* stack) {
    if (stack->top == -1) return -1; // Indicate empty or error
    return stack->arr[stack->top];
}

int isEmpty(Stack* stack) {
    return stack->top == -1;
}

void clearStack(Stack* stack) {
    stack->top = -1;
}

void freeStack(Stack* stack) {
    free(stack->arr);
    free(stack);
}

int minOperations(int* nums, int numsSize) {
    int operations = 0;
    Stack* s = createStack(numsSize); // Max capacity N

    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x == 0) {
            // A zero acts as a separator. Clear the stack.
            clearStack(s);
        } else {
            // While the stack is not empty and the top element is greater than x,
            // pop elements.
            while (!isEmpty(s) && peek(s) > x) {
                pop(s);
            }

            // If the stack is empty or the top element is less than x,
            // it means x represents a new, higher level that needs an operation.
            if (isEmpty(s) || peek(s) < x) {
                operations++;
                push(s, x);
            }
            // If peek(s) == x, x is at the same level as the current top of the stack.
            // It's already accounted for. Do nothing.
        }
    }

    freeStack(s);
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        int operations = 0;
        Stack<int> s = new Stack<int>();

        foreach (int x in nums) {
            if (x == 0) {
                // A zero acts as a separator. Clear the stack.
                s.Clear();
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements.
                while (s.Count > 0 && s.Peek() > x) {
                    s.Pop();
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if (s.Count == 0 || s.Peek() < x) {
                    operations++;
                    s.Push(x);
                }
                // If s.Peek() == x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let operations = 0;
    let s = []; // Using a JavaScript array as a stack

    for (let x of nums) {
        if (x === 0) {
            // A zero acts as a separator. Clear the stack.
            s = [];
        } else {
            // While the stack is not empty and the top element is greater than x,
            // pop elements.
            while (s.length > 0 && s[s.length - 1] > x) {
                s.pop();
            }

            // If the stack is empty or the top element is less than x,
            // it means x represents a new, higher level that needs an operation.
            if (s.length === 0 || s[s.length - 1] < x) {
                operations++;
                s.push(x);
            }
            // If s[s.length - 1] === x, x is at the same level as the current top of the stack.
            // It's already accounted for. Do nothing.
        }
    }

    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[]): number {
    let operations: number = 0;
    let s: number[] = []; // Using a TypeScript array as a stack

    for (let x of nums) {
        if (x === 0) {
            // A zero acts as a separator. Clear the stack.
            s = [];
        } else {
            // While the stack is not empty and the top element is greater than x,
            // pop elements.
            while (s.length > 0 && s[s.length - 1] > x) {
                s.pop();
            }

            // If the stack is empty or the top element is less than x,
            // it means x represents a new, higher level that needs an operation.
            if (s.length === 0 || s[s.length - 1] < x) {
                operations++;
                s.push(x);
            }
            // If s[s.length - 1] === x, x is at the same level as the current top of the stack.
            // It's already accounted for. Do nothing.
        }
    }

    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $operations = 0;
        $s = []; // Using a PHP array as a stack

        foreach ($nums as $x) {
            if ($x === 0) {
                // A zero acts as a separator. Clear the stack.
                $s = [];
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements.
                while (!empty($s) && $s[count($s) - 1] > $x) {
                    array_pop($s);
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if (empty($s) || $s[count($s) - 1] < $x) {
                    $operations++;
                    array_push($s, $x);
                }
                // If $s[count($s) - 1] === $x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        return $operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var operations = 0
        var s: [Int] = [] // Using a Swift array as a stack

        for x in nums {
            if x == 0 {
                // A zero acts as a separator. Clear the stack.
                s.removeAll()
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements.
                while !s.isEmpty && s.last! > x {
                    s.removeLast()
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if s.isEmpty || s.last! < x {
                    operations += 1
                    s.append(x)
                }
                // If s.last! == x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.ArrayDeque
import java.util.Deque

class Solution {
    fun minOperations(nums: IntArray): Int {
        var operations = 0
        val s: Deque<Int> = ArrayDeque() // Using ArrayDeque as a stack

        for (x in nums) {
            if (x == 0) {
                // A zero acts as a separator. Clear the stack.
                s.clear()
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements.
                while (s.isNotEmpty() && s.peekLast() > x) {
                    s.removeLast()
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if (s.isEmpty() || s.peekLast() < x) {
                    operations++
                    s.addLast(x)
                }
                // If s.peekLast() == x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int minOperations(List<int> nums) {
    int operations = 0;
    // Using a List as a stack, or a Queue for Deque-like behavior
    List<int> s = []; 

    for (int x in nums) {
      if (x == 0) {
        // A zero acts as a separator. Clear the stack.
        s.clear();
      } else {
        // While the stack is not empty and the top element is greater than x,
        // pop elements.
        while (s.isNotEmpty && s.last > x) {
          s.removeLast();
        }

        // If the stack is empty or the top element is less than x,
        // it means x represents a new, higher level that needs an operation.
        if (s.isEmpty || s.last < x) {
          operations++;
          s.add(x);
        }
        // If s.last == x, x is at the same level as the current top of the stack.
        // It's already accounted for. Do nothing.
      }
    }

    return operations;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"container/list"
)

// Solution struct (if needed for LeetCode platform)
type Solution struct{}

func minOperations(nums []int) int {
    operations := 0
    s := list.New() // Using container/list as a stack

    for _, x := range nums {
        if x == 0 {
            // A zero acts as a separator. Clear the stack.
            for s.Len() > 0 {
                s.Remove(s.Back())
            }
        } else {
            // While the stack is not empty and the top element is greater than x,
            // pop elements.
            for s.Len() > 0 && s.Back().Value.(int) > x {
                s.Remove(s.Back())
            }

            // If the stack is empty or the top element is less than x,
            // it means x represents a new, higher level that needs an operation.
            if s.Len() == 0 || s.Back().Value.(int) < x {
                operations++
                s.PushBack(x)
            }
            // If s.Back().Value.(int) == x, x is at the same level as the current top of the stack.
            // It's already accounted for. Do nothing.
        }
    }

    return operations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    /**
     * @param {Integer[]} nums
     * @return {Integer}
     */
    def min_operations(nums)
        operations = 0
        s = [] # Using a Ruby array as a stack

        nums.each do |x|
            if x == 0
                # A zero acts as a separator. Clear the stack.
                s.clear
            else
                # While the stack is not empty and the top element is greater than x,
                # pop elements.
                while !s.empty? && s.last > x
                    s.pop
                end

                # If the stack is empty or the top element is less than x,
                # it means x represents a new, higher level that needs an operation.
                if s.empty? || s.last < x
                    operations += 1
                    s.push(x)
                end
                # If s.last == x, x is at the same level as the current top of the stack.
                # It's already accounted for. Do nothing.
            end
        end

        operations
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def minOperations(nums: Array[Int]): Int = {
        var operations = 0
        val s = mutable.Stack[Int]()

        for (x <- nums) {
            if (x == 0) {
                // A zero acts as a separator. Clear the stack.
                s.clear()
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements.
                while (s.nonEmpty && s.top > x) {
                    s.pop()
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if (s.isEmpty || s.top < x) {
                    operations += 1
                    s.push(x)
                }
                // If s.top == x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut operations = 0;
        let mut s: Vec<i32> = Vec::new(); // Using a Vec as a stack

        for x in nums {
            if x == 0 {
                // A zero acts as a separator. Clear the stack.
                s.clear();
            } else {
                // While the stack is not empty and the top element is greater than x,
                // pop elements.
                while let Some(&top_val) = s.last() {
                    if top_val > x {
                        s.pop();
                    } else {
                        break;
                    }
                }

                // If the stack is empty or the top element is less than x,
                // it means x represents a new, higher level that needs an operation.
                if s.is_empty() || s.last().unwrap() < x {
                    operations += 1;
                    s.push(x);
                }
                // If s.last().unwrap() == x, x is at the same level as the current top of the stack.
                // It's already accounted for. Do nothing.
            }
        }

        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (min-operations nums)
  (define operations 0)
  (define s (make-stack)) ; Using a custom stack implementation

  (define (make-stack)
    (let ((lst '()))
      (list
       (lambda () (empty? lst)) ; is-empty
       (lambda () (car lst))    ; peek
       (lambda (item) (set! lst (cons item lst))) ; push
       (lambda () (set! lst (cdr lst))) ; pop
       (lambda () (set! lst '())) ; clear
       )))

  (define (stack-empty? stack) ((car stack)))
  (define (stack-peek stack) ((cadr stack)))
  (define (stack-push stack item) ((caddr stack) item))
  (define (stack-pop stack) ((cadddr stack)))
  (define (stack-clear stack) ((cadddr (cdr stack))))

  (for-each (lambda (x)
              (when (= x 0)
                (stack-clear s))
              (unless (= x 0)
                (when (not (stack-empty? s))
                  (while (and (not (stack-empty? s)) (> (stack-peek s) x))
                    (stack-pop s)))

                (when (or (stack-empty? s) (< (stack-peek s) x))
                  (set! operations (+ operations 1))
                  (stack-push s x))))
            nums)
  operations)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_operations/1]).

min_operations(Nums) ->
    min_operations_recursive(Nums, 0, []).

min_operations_recursive([], Operations, _Stack) ->
    Operations;
min_operations_recursive([0 | T], Operations, _Stack) ->
    % A zero acts as a separator. Clear the stack.
    min_operations_recursive(T, Operations, []);
min_operations_recursive([X | T], Operations, Stack) ->
    % While the stack is not empty and the top element is greater than X,
    % pop elements.
    NewStackAfterPop = pop_greater(X, Stack),

    case NewStackAfterPop of
        [] ->
            % If the stack is empty, X represents a new, higher level.
            min_operations_recursive(T, Operations + 1, [X]);
        [Top | _] when Top < X ->
            % If the top element is less than X, X represents a new, higher level.
            min_operations_recursive(T, Operations + 1, [X | NewStackAfterPop]);
        [Top | _] when Top == X ->
            % If Top == X, X is at the same level as the current top of the stack.
            % It's already accounted for. Do nothing.
            min_operations_recursive(T, Operations, NewStackAfterPop)
    end.

pop_greater(_X, []) ->
    [];
pop_greater(X, [Top | Rest]) when Top > X ->
    pop_greater(X, Rest);
pop_greater(X, Stack) ->
    Stack.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    do_min_operations(nums, 0, [])
  end

  defp do_min_operations([], operations, _stack), do: operations

  defp do_min_operations([0 | tail], operations, _stack) do
    # A zero acts as a separator. Clear the stack.
    do_min_operations(tail, operations, [])
  end

  defp do_min_operations([x | tail], operations, stack) do
    # While the stack is not empty and the top element is greater than x,
    # pop elements.
    new_stack_after_pop = pop_greater(x, stack)

    case new_stack_after_pop do
      [] ->
        # If the stack is empty, x represents a new, higher level.
        do_min_operations(tail, operations + 1, [x])
      [top | _] when top < x ->
        # If the top element is less than x, x represents a new, higher level.
        do_min_operations(tail, operations + 1, [x | new_stack_after_pop])
      [top | _] when top == x ->
        # If top == x, x is at the same level as the current top of the stack.
        # It's already accounted for. Do nothing.
        do_min_operations(tail, operations, new_stack_after_pop)
    end
  end

  defp pop_greater(_x, []), do: []
  defp pop_greater(x, [top | rest]) when top > x, do: pop_greater(x, rest)
  defp pop_greater(_x, stack), do: stack
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the `nums` array. This is because each element in `nums` is processed exactly once. During processing, an element is pushed onto the stack at most once and popped from the stack at most once. Stack operations (push, pop, top, clear) take O(1) time on average.

- **Space Complexity:** The space complexity is O(N) in the worst case. This occurs if the `nums` array is strictly increasing (e.g., `[1, 2, 3, ..., N]`), in which case all N elements will be pushed onto the stack. In such a scenario, the stack will hold N elements.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 21:08:03 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the minimum number of operations to convert all elements in the given array to zero. The approach involves processing the values in the array from smallest to largest (excluding zero). For each target value, identify its maximal contiguous segments (subarrays where the value is equal to the target) and zero them out in one operation. After setting those segments to zero, dynamically update the remaining array and repeat with the next value. This process continues until all elements in the array are zero. The key insight is that the minimum number of operations is equal to the number of distinct non-zero values in the array, as each distinct value requires at least one operation to zero out all its occurrences.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::set<int> distinctValues;
        for (int num : nums) {
            if (num != 0) {
                distinctValues.insert(num);
            }
        }
        return distinctValues.size();
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

public class Solution {
    public int minOperations(int[] nums) {
        Set<Integer> distinctValues = new HashSet<>();
        for (int num : nums) {
            if (num != 0) {
                distinctValues.add(num);
            }
        }
        return distinctValues.size();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        distinct_values = set()
        for num in nums:
            if num != 0:
                distinct_values.add(num)
        return len(distinct_values)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        distinct_values = set()
        for num in nums:
            if num != 0:
                distinct_values.add(num)
        return len(distinct_values)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int minOperations(int* nums, int numsSize) {
    int* distinctValues = (int*)malloc(numsSize * sizeof(int));
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != 0) {
            int found = 0;
            for (int j = 0; j < count; j++) {
                if (distinctValues[j] == nums[i]) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                distinctValues[count++] = nums[i];
            }
        }
    }
    free(distinctValues);
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        HashSet<int> distinctValues = new HashSet<int>();
        foreach (int num in nums) {
            if (num != 0) {
                distinctValues.Add(num);
            }
        }
        return distinctValues.Count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minOperations = function(nums) {
    let distinctValues = new Set();
    for (let num of nums) {
        if (num != 0) {
            distinctValues.add(num);
        }
    }
    return distinctValues.size;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[]): number {
    let distinctValues: Set<number> = new Set();
    for (let num of nums) {
        if (num != 0) {
            distinctValues.add(num);
        }
    }
    return distinctValues.size;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minOperations($nums) {
        $distinctValues = array();
        foreach ($nums as $num) {
            if ($num != 0) {
                $distinctValues[$num] = true;
            }
        }
        return count($distinctValues);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var distinctValues: Set<Int> = Set()
        for num in nums {
            if num != 0 {
                distinctValues.insert(num)
            }
        }
        return distinctValues.count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(nums: IntArray): Int {
        val distinctValues = mutableSetOf<Int>()
        for (num in nums) {
            if (num != 0) {
                distinctValues.add(num)
            }
        }
        return distinctValues.size
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int minOperations(List<int> nums) {
        Set<int> distinctValues = Set();
        for (int num in nums) {
            if (num != 0) {
                distinctValues.add(num);
            }
        }
        return distinctValues.length;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "fmt"

func minOperations(nums []int) int {
    distinctValues := make(map[int]bool)
    for _, num := range nums {
        if num != 0 {
            distinctValues[num] = true
        }
    }
    return len(distinctValues)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_operations(nums)
    distinct_values = Set.new
    nums.each do |num|
        distinct_values.add(num) if num != 0
    end
    distinct_values.size
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        val distinctValues = scala.collection.mutable.Set[Int]()
        for (num <- nums) {
            if (num != 0) {
                distinctValues.add(num)
            }
        }
        distinctValues.size
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut distinct_values: std::collections::HashSet<i32> = std::collections::HashSet::new();
        for num in nums {
            if num != 0 {
                distinct_values.insert(num);
            }
        }
        distinct_values.len() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (min-operations nums)
  (let ((distinct-values (make-hash)))
    (for-each (lambda (num)
                (if (not (zero? num))
                    (hash-set! distinct-values num #t)))
              nums)
    (hash-count distinct-values)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).

-export([min_operations/1]).

min_operations(Nums) ->
    DistinctValues = sets:new(),
    lists:foldl(fun (Num, Set) ->
                        if Num =:= 0 ->
                            Set;
                        true ->
                            sets:add_element(Num, Set)
                        end
                end, DistinctValues, Nums),
    sets:size(DistinctValues).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def min_operations(nums) do
    distinct_values = MapSet.new()
    Enum.reduce(nums, distinct_values, fn num, set ->
      if num != 0, do: MapSet.put(set, num), else: set
    end)
    |> MapSet.size()
  end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) due to the sorting of the array, where n is the number of elements in the array. The subsequent operations of identifying maximal contiguous segments and zeroing them out can be done in O(n) time. Therefore, the overall time complexity is dominated by the sorting step.

- **Space Complexity:** O(n) for storing the sorted array and the set of distinct non-zero values. The space complexity is linear with respect to the input size.

</div>
</details>
