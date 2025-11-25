---
layout: post
title: "Count Operations to Obtain Zero"
date: 2025-11-09 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-operations-to-obtain-zero/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countOperations(int num1, int num2) {\n\
        \        int operations = 0;\n        while (num1 > 0 && num2 > 0) {\n     \
        \       if (num1 >= num2) {\n                num1 -= num2;\n            } else\
        \ {\n                num2 -= num1;\n            }\n            operations++;\n\
        \        }\n        return operations;\n    }\n};"
      java: "class Solution {\n    public int countOperations(int num1, int num2) {\n\
        \        int operations = 0;\n        while (num1 > 0 && num2 > 0) {\n     \
        \       if (num1 >= num2) {\n                num1 -= num2;\n            } else\
        \ {\n                num2 -= num1;\n            }\n            operations++;\n\
        \        }\n        return operations;\n    }\n}"
      python: "class Solution:\n    def countOperations(self, num1: int, num2: int)\
        \ -> int:\n        operations = 0\n        while num1 > 0 and num2 > 0:\n  \
        \          if num1 >= num2:\n                num1 -= num2\n            else:\n\
        \                num2 -= num1\n            operations += 1\n        return operations"
      python3: "class Solution:\n    def countOperations(self, num1: int, num2: int)\
        \ -> int:\n        operations = 0\n        while num1 > 0 and num2 > 0:\n  \
        \          if num1 >= num2:\n                num1 -= num2\n            else:\n\
        \                num2 -= num1\n            operations += 1\n        return operations"
      c: "int countOperations(int num1, int num2) {\n    int operations = 0;\n    while\
        \ (num1 > 0 && num2 > 0) {\n        if (num1 >= num2) {\n            num1 -=\
        \ num2;\n        } else {\n            num2 -= num1;\n        }\n        operations++;\n\
        \    }\n    return operations;\n}"
      csharp: "public class Solution {\n    public int CountOperations(int num1, int\
        \ num2) {\n        int operations = 0;\n        while (num1 > 0 && num2 > 0)\
        \ {\n            if (num1 >= num2) {\n                num1 -= num2;\n      \
        \      } else {\n                num2 -= num1;\n            }\n            operations++;\n\
        \        }\n        return operations;\n    }\n}"
      javascript: "/**\n * @param {number} num1\n * @param {number} num2\n * @return\
        \ {number}\n */\nvar countOperations = function(num1, num2) {\n    let operations\
        \ = 0;\n    while (num1 > 0 && num2 > 0) {\n        if (num1 >= num2) {\n  \
        \          num1 -= num2;\n        } else {\n            num2 -= num1;\n    \
        \    }\n        operations++;\n    }\n    return operations;\n};"
      typescript: "function countOperations(num1: number, num2: number): number {\n\
        \    let operations: number = 0;\n    while (num1 > 0 && num2 > 0) {\n     \
        \   if (num1 >= num2) {\n            num1 -= num2;\n        } else {\n     \
        \       num2 -= num1;\n        }\n        operations++;\n    }\n    return operations;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer $num1\n     * @param\
        \ Integer $num2\n     * @return Integer\n     */\n    function countOperations($num1,\
        \ $num2) {\n        $operations = 0;\n        while ($num1 > 0 && $num2 > 0)\
        \ {\n            if ($num1 >= $num2) {\n                $num1 -= $num2;\n  \
        \          } else {\n                $num2 -= $num1;\n            }\n      \
        \      $operations++;\n        }\n        return $operations;\n    }\n}"
      swift: "class Solution {\n    func countOperations(_ num1: Int, _ num2: Int) ->\
        \ Int {\n        var n1 = num1\n        var n2 = num2\n        var operations\
        \ = 0\n        while n1 > 0 && n2 > 0 {\n            if n1 >= n2 {\n       \
        \         n1 -= n2\n            } else {\n                n2 -= n1\n       \
        \     }\n            operations += 1\n        }\n        return operations\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun countOperations(num1: Int, num2: Int): Int\
        \ {\n        var n1 = num1\n        var n2 = num2\n        var operations =\
        \ 0\n        while (n1 > 0 && n2 > 0) {\n            if (n1 >= n2) {\n     \
        \           n1 -= n2\n            } else {\n                n2 -= n1\n     \
        \       }\n            operations++\n        }\n        return operations\n\
        \    }\n}"
      dart: "class Solution {\n  int countOperations(int num1, int num2) {\n    int\
        \ operations = 0;\n    while (num1 > 0 && num2 > 0) {\n      if (num1 >= num2)\
        \ {\n        num1 -= num2;\n      } else {\n        num2 -= num1;\n      }\n\
        \      operations++;\n    }\n    return operations;\n  }\n}"
      go: "func countOperations(num1 int, num2 int) int {\n    operations := 0\n   \
        \ for num1 > 0 && num2 > 0 {\n        if num1 >= num2 {\n            num1 -=\
        \ num2\n        } else {\n            num2 -= num1\n        }\n        operations++\n\
        \    }\n    return operations\n}"
      ruby: "# @param {Integer} num1\n# @param {Integer} num2\n# @return {Integer}\n\
        def count_operations(num1, num2)\n    operations = 0\n    while num1 > 0 &&\
        \ num2 > 0\n        if num1 >= num2\n            num1 -= num2\n        else\n\
        \            num2 -= num1\n        end\n        operations += 1\n    end\n \
        \   return operations\nend"
      scala: "object Solution {\n    def countOperations(num1: Int, num2: Int): Int\
        \ = {\n        var n1 = num1\n        var n2 = num2\n        var operations\
        \ = 0\n        while (n1 > 0 && n2 > 0) {\n            if (n1 >= n2) {\n   \
        \             n1 -= n2\n            } else {\n                n2 -= n1\n   \
        \         }\n            operations += 1\n        }\n        operations\n  \
        \  }\n}"
      rust: "impl Solution {\n    pub fn count_operations(mut num1: i32, mut num2: i32)\
        \ -> i32 {\n        let mut operations = 0;\n        while num1 > 0 && num2\
        \ > 0 {\n            if num1 >= num2 {\n                num1 -= num2;\n    \
        \        } else {\n                num2 -= num1;\n            }\n          \
        \  operations += 1;\n        }\n        operations\n    }\n}"
      racket: "(define/contract (count-operations num1 num2)\n  (-> exact-integer? exact-integer?\
        \ exact-integer?)\n  (let loop ((n1 num1) (n2 num2) (ops 0))\n    (cond\n  \
        \    ((or (= n1 0) (= n2 0)) ops)\n      ((>= n1 n2) (loop (- n1 n2) n2 (+ ops\
        \ 1)))\n      (else (loop n1 (- n2 n1) (+ ops 1))))))"
      erlang: "-spec count_operations(Num1 :: integer(), Num2 :: integer()) -> integer().\n\
        count_operations(Num1, Num2) ->\n    count_operations_recursive(Num1, Num2,\
        \ 0).\n\ncount_operations_recursive(N1, N2, Ops) when N1 == 0; N2 == 0 ->\n\
        \    Ops;\ncount_operations_recursive(N1, N2, Ops) when N1 >= N2 ->\n    count_operations_recursive(N1\
        \ - N2, N2, Ops + 1);\ncount_operations_recursive(N1, N2, Ops) -> % N1 < N2\n\
        \    count_operations_recursive(N1, N2 - N1, Ops + 1)."
      elixir: "defmodule Solution do\n  @spec count_operations(num1 :: integer(), num2\
        \ :: integer()) :: integer()\n  def count_operations(num1, num2) do\n    do_count_operations(num1,\
        \ num2, 0)\n  end\n\n  defp do_count_operations(n1, n2, ops) when n1 == 0 or\
        \ n2 == 0, do: ops\n  defp do_count_operations(n1, n2, ops) when n1 >= n2, do:\
        \ do_count_operations(n1 - n2, n2, ops + 1)\n  defp do_count_operations(n1,\
        \ n2, ops), do: do_count_operations(n1, n2 - n1, ops + 1)\nend"
    approach: The problem asks us to count the number of operations required to make
      either of two non-negative integers, `num1` or `num2`, equal to zero. An operation
      consists of subtracting the smaller number from the larger number. This process
      is a direct simulation of the Euclidean algorithm for finding the greatest common
      divisor (GCD) using repeated subtraction. The core idea is to continuously apply
      the given rule until one of the numbers reaches zero, incrementing a counter with
      each operation.
    time_complexity: O(max(num1, num2)) with detailed explanation. The algorithm simulates
      the Euclidean algorithm using subtraction. In the worst-case scenario, if one
      number is significantly larger than the other (e.g., `num1 = N` and `num2 = 1`),
      the larger number will be reduced by 1 in each step. This would lead to `N` operations.
      For example, if `num1 = 10^5` and `num2 = 1`, it would take `10^5` operations.
      Since the maximum value for `num1` and `num2` is `10^5`, the number of operations
      can be up to `10^5`, making the time complexity linear with respect to the maximum
      of the input numbers. This is efficient enough given the constraints.
    space_complexity: O(1) with detailed explanation. The algorithm uses a constant
      amount of extra space. It only requires a few variables to store the current values
      of `num1`, `num2`, and the `operations` count. These variables occupy a fixed
      amount of memory regardless of the magnitude of the input integers. No additional
      data structures are used that would scale with the input size.
    elapsed_time: 24.210477590560913
    model: gemini-2.5-flash
    generated_at: '2025-11-24 21:01:13 '
  - solutions:
      cpp: "class Solution {\n    public:\n        int countOperations(int num1, int\
        \ num2) {\n            int count = 0;\n            while (num1 > 0 && num2 >\
        \ 0) {\n                if (num1 >= num2) {\n                    num1 -= num2;\n\
        \                } else {\n                    num2 -= num1;\n             \
        \   }\n                count++;\n            }\n            return count;\n\
        \        }\n    };"
      java: "class Solution {\npublic int countOperations(int num1, int num2) {\n  \
        \  int count = 0;\n    while (num1 > 0 && num2 > 0) {\n        if (num1 >= num2)\
        \ {\n            num1 -= num2;\n        } else {\n            num2 -= num1;\n\
        \        }\n        count++;\n    }\n    return count;\n}\n};"
      python: "class Solution:\ndef countOperations(self, num1: int, num2: int) -> int:\n\
        \    count = 0\n    while num1 > 0 and num2 > 0:\n        if num1 >= num2:\n\
        \            num1 -= num2\n        else:\n            num2 -= num1\n       \
        \ count += 1\n    return count"
      python3: "class Solution:\ndef countOperations(self, num1: int, num2: int) ->\
        \ int:\n    count = 0\n    while num1 > 0 and num2 > 0:\n        if num1 >=\
        \ num2:\n            num1 -= num2\n        else:\n            num2 -= num1\n\
        \        count += 1\n    return count"
      c: "int countOperations(int num1, int num2) {\nint count = 0;\nwhile (num1 > 0\
        \ && num2 > 0) {\n    if (num1 >= num2) {\n        num1 -= num2;\n    } else\
        \ {\n        num2 -= num1;\n    }\n    count++;\n}\nreturn count;\n};"
      csharp: "public class Solution {\npublic int CountOperations(int num1, int num2)\
        \ {\n    int count = 0;\n    while (num1 > 0 && num2 > 0) {\n        if (num1\
        \ >= num2) {\n            num1 -= num2;\n        } else {\n            num2\
        \ -= num1;\n        }\n        count++;\n    }\n    return count;\n}\n};"
      javascript: "var countOperations = function(num1, num2) {\nlet count = 0;\nwhile\
        \ (num1 > 0 && num2 > 0) {\n    if (num1 >= num2) {\n        num1 -= num2;\n\
        \    } else {\n        num2 -= num1;\n    }\n    count++;\n}\nreturn count;\n\
        };"
      typescript: "function countOperations(num1: number, num2: number): number {\n\
        let count: number = 0;\nwhile (num1 > 0 && num2 > 0) {\n    if (num1 >= num2)\
        \ {\n        num1 -= num2;\n    } else {\n        num2 -= num1;\n    }\n   \
        \ count++;\n}\nreturn count;\n};"
      php: "class Solution {\nfunction countOperations($num1, $num2) {\n    $count =\
        \ 0;\n    while ($num1 > 0 && $num2 > 0) {\n        if ($num1 >= $num2) {\n\
        \            $num1 -= $num2;\n        } else {\n            $num2 -= $num1;\n\
        \        }\n        $count++;\n    }\n    return $count;\n}\n};"
      swift: "class Solution {\nfunc countOperations(_ num1: Int, _ num2: Int) -> Int\
        \ {\n    var count = 0\n    var num1 = num1\n    var num2 = num2\n    while\
        \ num1 > 0 && num2 > 0 {\n        if num1 >= num2 {\n            num1 -= num2\n\
        \        } else {\n            num2 -= num1\n        }\n        count += 1\n\
        \    }\n    return count\n}\n};"
      kotlin: "class Solution {\nfun countOperations(num1: Int, num2: Int): Int {\n\
        \    var count = 0\n    var num1 = num1\n    var num2 = num2\n    while (num1\
        \ > 0 && num2 > 0) {\n        if (num1 >= num2) {\n            num1 -= num2\n\
        \        } else {\n            num2 -= num1\n        }\n        count++\n  \
        \  }\n    return count\n}\n};"
      dart: "class Solution {\nint countOperations(int num1, int num2) {\n    int count\
        \ = 0;\n    while (num1 > 0 && num2 > 0) {\n        if (num1 >= num2) {\n  \
        \          num1 -= num2;\n        } else {\n            num2 -= num1;\n    \
        \    }\n        count++;\n    }\n    return count;\n}\n};"
      go: "func countOperations(num1 int, num2 int) int {\ncount := 0\nfor num1 > 0\
        \ && num2 > 0 {\n    if num1 >= num2 {\n        num1 -= num2\n    } else {\n\
        \        num2 -= num1\n    }\n    count++\n}\nreturn count\n};"
      ruby: "def count_operations(num1, num2)\ncount = 0\nwhile num1 > 0 && num2 > 0\n\
        \    if num1 >= num2\n        num1 -= num2\n    else\n        num2 -= num1\n\
        \    end\n    count += 1\nend\ncount\nend;"
      scala: "object Solution {\ndef countOperations(num1: Int, num2: Int): Int = {\n\
        \    var count = 0\n    var num1 = num1\n    var num2 = num2\n    while (num1\
        \ > 0 && num2 > 0) {\n        if (num1 >= num2) {\n            num1 -= num2\n\
        \        } else {\n            num2 -= num1\n        }\n        count += 1\n\
        \    }\n    count\n}\n};"
      rust: "struct Solution;\n    impl Solution {\n        pub fn count_operations(num1:\
        \ i32, num2: i32) -> i32 {\n            let mut count = 0;\n            let\
        \ mut num1 = num1;\n            let mut num2 = num2;\n            while num1\
        \ > 0 && num2 > 0 {\n                if num1 >= num2 {\n                   \
        \ num1 -= num2;\n                } else {\n                    num2 -= num1;\n\
        \                }\n                count += 1;\n            }\n           \
        \ count\n        }\n    };"
      racket: "(define (count-operations num1 num2)\n(let loop ((count 0) (num1 num1)\
        \ (num2 num2))\n    (if (or (= num1 0) (= num2 0))\n        count\n        (loop\
        \ (+ count 1)\n              (if (>= num1 num2)\n                  (- num1 num2)\n\
        \                  num1)\n              (if (>= num1 num2)\n               \
        \   num2\n                  (- num2 num1))))))"
      erlang: "-module(solution).\n    -export([count_operations/2]).\n    count_operations(Num1,\
        \ Num2) when Num1 =:= 0; Num2 =:= 0 ->\n        0;\n    count_operations(Num1,\
        \ Num2) when Num1 >= Num2 ->\n        1 + count_operations(Num1 - Num2, Num2);\n\
        \    count_operations(Num1, Num2) ->\n        1 + count_operations(Num1, Num2\
        \ - Num1)."
      elixir: "defmodule Solution do\n        def count_operations(num1, num2) when\
        \ num1 == 0 or num2 == 0, do: 0\n        def count_operations(num1, num2) when\
        \ num1 >= num2, do: 1 + count_operations(num1 - num2, num2)\n        def count_operations(num1,\
        \ num2), do: 1 + count_operations(num1, num2 - num1)\n    end;"
    approach: The problem can be solved by simulating the process until either of the
      two integers is zero. We start by checking if num1 is greater than or equal to
      num2. If it is, we subtract num2 from num1. Otherwise, we subtract num1 from num2.
      We repeat this process until either num1 or num2 becomes zero. The number of operations
      required is the number of times we perform the subtraction. This approach ensures
      that we always subtract the smaller number from the larger number, which minimizes
      the number of operations required. For example, if num1 = 5 and num2 = 4, we subtract
      num2 from num1 to get num1 = 1 and num2 = 4. Then, we subtract num1 from num2
      to get num1 = 1 and num2 = 3. We repeat this process until either num1 or num2
      becomes zero.
    time_complexity: The time complexity of this approach is O(log min(num1, num2))
      because in the worst-case scenario, we are effectively performing a series of
      subtractions that reduce the smaller number to zero. The number of operations
      required is proportional to the number of times we can divide the smaller number
      by 2 until it becomes zero, which is logarithmic in the size of the smaller number.
    space_complexity: The space complexity of this approach is O(1) because we only
      use a constant amount of space to store the input numbers and the count of operations.
      We do not use any data structures that grow with the size of the input, so the
      space complexity is constant.
    elapsed_time: 4.656049728393555
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-24 21:01:18 '
---

## Problem #2169: Count Operations to Obtain Zero

**Difficulty:** Easy

**Topics:** Math, Simulation

## Problem Description

<p>You are given two <strong>non-negative</strong> integers <code>num1</code> and <code>num2</code>.</p>

<p>In one <strong>operation</strong>, if <code>num1 &gt;= num2</code>, you must subtract <code>num2</code> from <code>num1</code>, otherwise subtract <code>num1</code> from <code>num2</code>.</p>

<ul>
	<li>For example, if <code>num1 = 5</code> and <code>num2 = 4</code>, subtract <code>num2</code> from <code>num1</code>, thus obtaining <code>num1 = 1</code> and <code>num2 = 4</code>. However, if <code>num1 = 4</code> and <code>num2 = 5</code>, after one operation, <code>num1 = 4</code> and <code>num2 = 1</code>.</li>
</ul>

<p>Return <em>the <strong>number of operations</strong> required to make either</em> <code>num1 = 0</code> <em>or</em> <code>num2 = 0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 2, num2 = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
- Operation 1: num1 = 2, num2 = 3. Since num1 &lt; num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 &gt; num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = 10, num2 = 10
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
- Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
So the total number of operations required is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num1, num2 &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Try simulating the process until either of the two integers is zero.

2. Count the number of operations done.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 21:01:13 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count the number of operations required to make either of two non-negative integers, `num1` or `num2`, equal to zero. An operation consists of subtracting the smaller number from the larger number. This process is a direct simulation of the Euclidean algorithm for finding the greatest common divisor (GCD) using repeated subtraction. The core idea is to continuously apply the given rule until one of the numbers reaches zero, incrementing a counter with each operation.

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
    int countOperations(int num1, int num2) {
        int operations = 0;
        while (num1 > 0 && num2 > 0) {
            if (num1 >= num2) {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations++;
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
class Solution {
    public int countOperations(int num1, int num2) {
        int operations = 0;
        while (num1 > 0 && num2 > 0) {
            if (num1 >= num2) {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations++;
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
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            operations += 1
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            operations += 1
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countOperations(int num1, int num2) {
    int operations = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        operations++;
    }
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountOperations(int num1, int num2) {
        int operations = 0;
        while (num1 > 0 && num2 > 0) {
            if (num1 >= num2) {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations++;
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
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var countOperations = function(num1, num2) {
    let operations = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        operations++;
    }
    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countOperations(num1: number, num2: number): number {
    let operations: number = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        operations++;
    }
    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @return Integer
     */
    function countOperations($num1, $num2) {
        $operations = 0;
        while ($num1 > 0 && $num2 > 0) {
            if ($num1 >= $num2) {
                $num1 -= $num2;
            } else {
                $num2 -= $num1;
            }
            $operations++;
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
    func countOperations(_ num1: Int, _ num2: Int) -> Int {
        var n1 = num1
        var n2 = num2
        var operations = 0
        while n1 > 0 && n2 > 0 {
            if n1 >= n2 {
                n1 -= n2
            } else {
                n2 -= n1
            }
            operations += 1
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
class Solution {
    fun countOperations(num1: Int, num2: Int): Int {
        var n1 = num1
        var n2 = num2
        var operations = 0
        while (n1 > 0 && n2 > 0) {
            if (n1 >= n2) {
                n1 -= n2
            } else {
                n2 -= n1
            }
            operations++
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
class Solution {
  int countOperations(int num1, int num2) {
    int operations = 0;
    while (num1 > 0 && num2 > 0) {
      if (num1 >= num2) {
        num1 -= num2;
      } else {
        num2 -= num1;
      }
      operations++;
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
func countOperations(num1 int, num2 int) int {
    operations := 0
    for num1 > 0 && num2 > 0 {
        if num1 >= num2 {
            num1 -= num2
        } else {
            num2 -= num1
        }
        operations++
    }
    return operations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def count_operations(num1, num2)
    operations = 0
    while num1 > 0 && num2 > 0
        if num1 >= num2
            num1 -= num2
        else
            num2 -= num1
        end
        operations += 1
    end
    return operations
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countOperations(num1: Int, num2: Int): Int = {
        var n1 = num1
        var n2 = num2
        var operations = 0
        while (n1 > 0 && n2 > 0) {
            if (n1 >= n2) {
                n1 -= n2
            } else {
                n2 -= n1
            }
            operations += 1
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
    pub fn count_operations(mut num1: i32, mut num2: i32) -> i32 {
        let mut operations = 0;
        while num1 > 0 && num2 > 0 {
            if num1 >= num2 {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations += 1;
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
(define/contract (count-operations num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((n1 num1) (n2 num2) (ops 0))
    (cond
      ((or (= n1 0) (= n2 0)) ops)
      ((>= n1 n2) (loop (- n1 n2) n2 (+ ops 1)))
      (else (loop n1 (- n2 n1) (+ ops 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_operations(Num1 :: integer(), Num2 :: integer()) -> integer().
count_operations(Num1, Num2) ->
    count_operations_recursive(Num1, Num2, 0).

count_operations_recursive(N1, N2, Ops) when N1 == 0; N2 == 0 ->
    Ops;
count_operations_recursive(N1, N2, Ops) when N1 >= N2 ->
    count_operations_recursive(N1 - N2, N2, Ops + 1);
count_operations_recursive(N1, N2, Ops) -> % N1 < N2
    count_operations_recursive(N1, N2 - N1, Ops + 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_operations(num1 :: integer(), num2 :: integer()) :: integer()
  def count_operations(num1, num2) do
    do_count_operations(num1, num2, 0)
  end

  defp do_count_operations(n1, n2, ops) when n1 == 0 or n2 == 0, do: ops
  defp do_count_operations(n1, n2, ops) when n1 >= n2, do: do_count_operations(n1 - n2, n2, ops + 1)
  defp do_count_operations(n1, n2, ops), do: do_count_operations(n1, n2 - n1, ops + 1)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(max(num1, num2)) with detailed explanation. The algorithm simulates the Euclidean algorithm using subtraction. In the worst-case scenario, if one number is significantly larger than the other (e.g., `num1 = N` and `num2 = 1`), the larger number will be reduced by 1 in each step. This would lead to `N` operations. For example, if `num1 = 10^5` and `num2 = 1`, it would take `10^5` operations. Since the maximum value for `num1` and `num2` is `10^5`, the number of operations can be up to `10^5`, making the time complexity linear with respect to the maximum of the input numbers. This is efficient enough given the constraints.

- **Space Complexity:** O(1) with detailed explanation. The algorithm uses a constant amount of extra space. It only requires a few variables to store the current values of `num1`, `num2`, and the `operations` count. These variables occupy a fixed amount of memory regardless of the magnitude of the input integers. No additional data structures are used that would scale with the input size.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 21:01:18 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by simulating the process until either of the two integers is zero. We start by checking if num1 is greater than or equal to num2. If it is, we subtract num2 from num1. Otherwise, we subtract num1 from num2. We repeat this process until either num1 or num2 becomes zero. The number of operations required is the number of times we perform the subtraction. This approach ensures that we always subtract the smaller number from the larger number, which minimizes the number of operations required. For example, if num1 = 5 and num2 = 4, we subtract num2 from num1 to get num1 = 1 and num2 = 4. Then, we subtract num1 from num2 to get num1 = 1 and num2 = 3. We repeat this process until either num1 or num2 becomes zero.

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
class Solution {
    public:
        int countOperations(int num1, int num2) {
            int count = 0;
            while (num1 > 0 && num2 > 0) {
                if (num1 >= num2) {
                    num1 -= num2;
                } else {
                    num2 -= num1;
                }
                count++;
            }
            return count;
        }
    };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
public int countOperations(int num1, int num2) {
    int count = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        count++;
    }
    return count;
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
def countOperations(self, num1: int, num2: int) -> int:
    count = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
def countOperations(self, num1: int, num2: int) -> int:
    count = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countOperations(int num1, int num2) {
int count = 0;
while (num1 > 0 && num2 > 0) {
    if (num1 >= num2) {
        num1 -= num2;
    } else {
        num2 -= num1;
    }
    count++;
}
return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
public int CountOperations(int num1, int num2) {
    int count = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        count++;
    }
    return count;
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countOperations = function(num1, num2) {
let count = 0;
while (num1 > 0 && num2 > 0) {
    if (num1 >= num2) {
        num1 -= num2;
    } else {
        num2 -= num1;
    }
    count++;
}
return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countOperations(num1: number, num2: number): number {
let count: number = 0;
while (num1 > 0 && num2 > 0) {
    if (num1 >= num2) {
        num1 -= num2;
    } else {
        num2 -= num1;
    }
    count++;
}
return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
function countOperations($num1, $num2) {
    $count = 0;
    while ($num1 > 0 && $num2 > 0) {
        if ($num1 >= $num2) {
            $num1 -= $num2;
        } else {
            $num2 -= $num1;
        }
        $count++;
    }
    return $count;
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
func countOperations(_ num1: Int, _ num2: Int) -> Int {
    var count = 0
    var num1 = num1
    var num2 = num2
    while num1 > 0 && num2 > 0 {
        if num1 >= num2 {
            num1 -= num2
        } else {
            num2 -= num1
        }
        count += 1
    }
    return count
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
fun countOperations(num1: Int, num2: Int): Int {
    var count = 0
    var num1 = num1
    var num2 = num2
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2
        } else {
            num2 -= num1
        }
        count++
    }
    return count
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
int countOperations(int num1, int num2) {
    int count = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        count++;
    }
    return count;
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countOperations(num1 int, num2 int) int {
count := 0
for num1 > 0 && num2 > 0 {
    if num1 >= num2 {
        num1 -= num2
    } else {
        num2 -= num1
    }
    count++
}
return count
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_operations(num1, num2)
count = 0
while num1 > 0 && num2 > 0
    if num1 >= num2
        num1 -= num2
    else
        num2 -= num1
    end
    count += 1
end
count
end;
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
def countOperations(num1: Int, num2: Int): Int = {
    var count = 0
    var num1 = num1
    var num2 = num2
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            num1 -= num2
        } else {
            num2 -= num1
        }
        count += 1
    }
    count
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
    impl Solution {
        pub fn count_operations(num1: i32, num2: i32) -> i32 {
            let mut count = 0;
            let mut num1 = num1;
            let mut num2 = num2;
            while num1 > 0 && num2 > 0 {
                if num1 >= num2 {
                    num1 -= num2;
                } else {
                    num2 -= num1;
                }
                count += 1;
            }
            count
        }
    };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-operations num1 num2)
(let loop ((count 0) (num1 num1) (num2 num2))
    (if (or (= num1 0) (= num2 0))
        count
        (loop (+ count 1)
              (if (>= num1 num2)
                  (- num1 num2)
                  num1)
              (if (>= num1 num2)
                  num2
                  (- num2 num1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
    -export([count_operations/2]).
    count_operations(Num1, Num2) when Num1 =:= 0; Num2 =:= 0 ->
        0;
    count_operations(Num1, Num2) when Num1 >= Num2 ->
        1 + count_operations(Num1 - Num2, Num2);
    count_operations(Num1, Num2) ->
        1 + count_operations(Num1, Num2 - Num1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
        def count_operations(num1, num2) when num1 == 0 or num2 == 0, do: 0
        def count_operations(num1, num2) when num1 >= num2, do: 1 + count_operations(num1 - num2, num2)
        def count_operations(num1, num2), do: 1 + count_operations(num1, num2 - num1)
    end;
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this approach is O(log min(num1, num2)) because in the worst-case scenario, we are effectively performing a series of subtractions that reduce the smaller number to zero. The number of operations required is proportional to the number of times we can divide the smaller number by 2 until it becomes zero, which is logarithmic in the size of the smaller number.

- **Space Complexity:** The space complexity of this approach is O(1) because we only use a constant amount of space to store the input numbers and the count of operations. We do not use any data structures that grow with the size of the input, so the space complexity is constant.

</div>
</details>
