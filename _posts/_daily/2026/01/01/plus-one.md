---
layout: post
title: "Plus One"
date: 2026-01-01 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/plus-one/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> plusOne(vector<int>& digits)\
        \ {\n        int n = digits.size();\n        for (int i = n - 1; i >= 0; --i)\
        \ {\n            if (digits[i] < 9) {\n                digits[i]++;\n      \
        \          return digits;\n            }\n            digits[i] = 0;\n     \
        \   }\n\n        // If we reach here, all digits were 9 (e.g., [9,9,9])\n  \
        \      // We need to prepend a 1 and set all other digits to 0\n        vector<int>\
        \ result(n + 1, 0);\n        result[0] = 1;\n        return result;\n    }\n\
        };"
      java: "class Solution {\n    public int[] plusOne(int[] digits) {\n        int\
        \ n = digits.length;\n        for (int i = n - 1; i >= 0; i--) {\n         \
        \   if (digits[i] < 9) {\n                digits[i]++;\n                return\
        \ digits;\n            }\n            digits[i] = 0;\n        }\n\n        //\
        \ If we reach here, all digits were 9 (e.g., [9,9,9])\n        // We need to\
        \ prepend a 1 and set all other digits to 0\n        int[] result = new int[n\
        \ + 1];\n        result[0] = 1;\n        // The rest of the elements are already\
        \ 0 by default\n        return result;\n    }\n}"
      python: "class Solution:\n    def plusOne(self, digits: List[int]) -> List[int]:\n\
        \        n = len(digits)\n        for i in range(n - 1, -1, -1):\n         \
        \   if digits[i] < 9:\n                digits[i] += 1\n                return\
        \ digits\n            digits[i] = 0\n\n        # If we reach here, all digits\
        \ were 9 (e.g., [9,9,9])\n        # We need to prepend a 1 and set all other\
        \ digits to 0\n        return [1] + digits"
      python3: "class Solution:\n    def plusOne(self, digits: List[int]) -> List[int]:\n\
        \        n = len(digits)\n        for i in range(n - 1, -1, -1):\n         \
        \   if digits[i] < 9:\n                digits[i] += 1\n                return\
        \ digits\n            digits[i] = 0\n\n        # If we reach here, all digits\
        \ were 9 (e.g., [9,9,9])\n        # We need to prepend a 1 and set all other\
        \ digits to 0\n        return [1] + digits"
      c: "/**\n * Note: The returned array must be malloced, and free'd by the caller.\n\
        \ */\nint* plusOne(int* digits, int digitsSize, int* returnSize) {\n    for\
        \ (int i = digitsSize - 1; i >= 0; --i) {\n        if (digits[i] < 9) {\n  \
        \          digits[i]++;\n            *returnSize = digitsSize;\n           \
        \ return digits;\n        }\n        digits[i] = 0;\n    }\n\n    // If we reach\
        \ here, all digits were 9 (e.g., [9,9,9])\n    // We need to create a new array\
        \ of size digitsSize + 1\n    int* result = (int*)malloc(sizeof(int) * (digitsSize\
        \ + 1));\n    result[0] = 1;\n    for (int i = 1; i <= digitsSize; ++i) {\n\
        \        result[i] = 0;\n    }\n    *returnSize = digitsSize + 1;\n    return\
        \ result;\n}"
      csharp: "public class Solution {\n    public int[] PlusOne(int[] digits) {\n \
        \       int n = digits.Length;\n        for (int i = n - 1; i >= 0; i--) {\n\
        \            if (digits[i] < 9) {\n                digits[i]++;\n          \
        \      return digits;\n            }\n            digits[i] = 0;\n        }\n\
        \n        // If we reach here, all digits were 9 (e.g., [9,9,9])\n        //\
        \ We need to prepend a 1 and set all other digits to 0\n        int[] result\
        \ = new int[n + 1];\n        result[0] = 1;\n        // The rest of the elements\
        \ are already 0 by default for int arrays\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} digits\n * @return {number[]}\n */\nvar\
        \ plusOne = function(digits) {\n    const n = digits.length;\n    for (let i\
        \ = n - 1; i >= 0; i--) {\n        if (digits[i] < 9) {\n            digits[i]++;\n\
        \            return digits;\n        }\n        digits[i] = 0;\n    }\n\n  \
        \  // If we reach here, all digits were 9 (e.g., [9,9,9])\n    // We need to\
        \ prepend a 1 and set all other digits to 0\n    const result = new Array(n\
        \ + 1).fill(0);\n    result[0] = 1;\n    return result;\n};"
      typescript: "function plusOne(digits: number[]): number[] {\n    const n = digits.length;\n\
        \    for (let i = n - 1; i >= 0; i--) {\n        if (digits[i] < 9) {\n    \
        \        digits[i]++;\n            return digits;\n        }\n        digits[i]\
        \ = 0;\n    }\n\n    // If we reach here, all digits were 9 (e.g., [9,9,9])\n\
        \    // We need to prepend a 1 and set all other digits to 0\n    const result\
        \ = new Array(n + 1).fill(0);\n    result[0] = 1;\n    return result;\n}"
      php: "class Solution {\n    /**\n     * @param Integer[] $digits\n     * @return\
        \ Integer[]\n     */\n    function plusOne($digits) {\n        $n = count($digits);\n\
        \        for ($i = $n - 1; $i >= 0; $i--) {\n            if ($digits[$i] < 9)\
        \ {\n                $digits[$i]++;\n                return $digits;\n     \
        \       }\n            $digits[$i] = 0;\n        }\n\n        // If we reach\
        \ here, all digits were 9 (e.g., [9,9,9])\n        // We need to prepend a 1\
        \ and set all other digits to 0\n        array_unshift($digits, 1);\n      \
        \  return $digits;\n    }\n}"
      swift: "class Solution {\n    func plusOne(_ digits: [Int]) -> [Int] {\n     \
        \   var digits = digits // Make it mutable\n        let n = digits.count\n \
        \       for i in (0..<n).reversed() {\n            if digits[i] < 9 {\n    \
        \            digits[i] += 1\n                return digits\n            }\n\
        \            digits[i] = 0\n        }\n\n        // If we reach here, all digits\
        \ were 9 (e.g., [9,9,9])\n        // We need to prepend a 1 and set all other\
        \ digits to 0\n        var result = Array(repeating: 0, count: n + 1)\n    \
        \    result[0] = 1\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun plusOne(digits: IntArray): IntArray {\n   \
        \     val n = digits.size\n        for (i in n - 1 downTo 0) {\n           \
        \ if (digits[i] < 9) {\n                digits[i]++\n                return\
        \ digits\n            }\n            digits[i] = 0\n        }\n\n        //\
        \ If we reach here, all digits were 9 (e.g., [9,9,9])\n        // We need to\
        \ prepend a 1 and set all other digits to 0\n        val result = IntArray(n\
        \ + 1)\n        result[0] = 1\n        // The rest of the elements are already\
        \ 0 by default\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> plusOne(List<int> digits) {\n    int n =\
        \ digits.length;\n    for (int i = n - 1; i >= 0; i--) {\n      if (digits[i]\
        \ < 9) {\n        digits[i]++;\n        return digits;\n      }\n      digits[i]\
        \ = 0;\n    }\n\n    // If we reach here, all digits were 9 (e.g., [9,9,9])\n\
        \    // We need to prepend a 1 and set all other digits to 0\n    List<int>\
        \ result = List.filled(n + 1, 0);\n    result[0] = 1;\n    return result;\n\
        \  }\n}"
      go: "func plusOne(digits []int) []int {\n    n := len(digits)\n    for i := n\
        \ - 1; i >= 0; i-- {\n        if digits[i] < 9 {\n            digits[i]++\n\
        \            return digits\n        }\n        digits[i] = 0\n    }\n\n    //\
        \ If we reach here, all digits were 9 (e.g., [9,9,9])\n    // We need to prepend\
        \ a 1 and set all other digits to 0\n    result := make([]int, n + 1)\n    result[0]\
        \ = 1\n    // The rest of the elements are already 0 by default\n    return\
        \ result\n}"
      ruby: "def plus_one(digits)\n    n = digits.length\n    (n - 1).downto(0) do |i|\n\
        \        if digits[i] < 9\n            digits[i] += 1\n            return digits\n\
        \        end\n        digits[i] = 0\n    end\n\n    # If we reach here, all\
        \ digits were 9 (e.g., [9,9,9])\n    # We need to prepend a 1 and set all other\
        \ digits to 0\n    [1] + digits\nend"
      scala: "object Solution {\n    def plusOne(digits: Array[Int]): Array[Int] = {\n\
        \        val n = digits.length\n        for (i <- n - 1 to 0 by -1) {\n    \
        \        if (digits(i) < 9) {\n                digits(i) += 1\n            \
        \    return digits\n            }\n            digits(i) = 0\n        }\n\n\
        \        // If we reach here, all digits were 9 (e.g., [9,9,9])\n        //\
        \ We need to prepend a 1 and set all other digits to 0\n        val result =\
        \ new Array[Int](n + 1)\n        result(0) = 1\n        // The rest of the elements\
        \ are already 0 by default\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {\n\
        \        let mut digits = digits; // Make it mutable\n        let n = digits.len();\n\
        \        for i in (0..n).rev() {\n            if digits[i] < 9 {\n         \
        \       digits[i] += 1;\n                return digits;\n            }\n   \
        \         digits[i] = 0;\n        }\n\n        // If we reach here, all digits\
        \ were 9 (e.g., [9,9,9])\n        // We need to prepend a 1 and set all other\
        \ digits to 0\n        let mut result = vec![0; n + 1];\n        result[0] =\
        \ 1;\n        result\n    }\n}"
      racket: "#lang racket\n(define/contract (plus-one digits)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let* ((num-str (string-join (map number->string\
        \ digits) \"\"))\n         (num (+ (string->number num-str) 1))\n         (result-str\
        \ (number->string num)))\n    (map (lambda (char) (string->number (string char)))\
        \ (string->list result-str))))"
      erlang: "-module(solution).\n-export([plus_one/1]).\n\nplus_one(Digits) ->\n \
        \   % Convert list of digits to a string, then to an integer\n    NumStr = lists:foldl(fun(D,\
        \ Acc) -> io_lib:format(\"~s~p\", [Acc, D]) end, \"\", Digits),\n    Num = list_to_integer(NumStr),\n\
        \n    ResultNum = Num + 1,\n    ResultStr = integer_to_list(ResultNum),\n\n\
        \    % Convert result string back to a list of digits\n    lists:map(fun(C)\
        \ -> C - $0 end, ResultStr)."
      elixir: "defmodule Solution do\n  @spec plus_one(digits :: [integer]) :: [integer]\n\
        \  def plus_one(digits) do\n    num_str = Enum.map_join(digits, \"\", &Integer.to_string/1)\n\
        \    num = String.to_integer(num_str)\n    result_num = num + 1\n\n    result_num\n\
        \    |> Integer.to_string()\n    |> String.graphemes()\n    |> Enum.map(&String.to_integer/1)\n\
        \  end\nend"
    approach: The problem asks us to increment a large integer represented as an array
      of digits. We can simulate the standard addition process by iterating through
      the digits from right to left (least significant to most significant). We start
      by adding one to the rightmost digit. If the digit becomes less than 10 (i.e.,
      no carry-over), we simply update that digit and return the array, as the addition
      is complete. This handles cases like [1,2,3] becoming [1,2,4] or [4,3,2,9] becoming
      [4,3,3,0].
    time_complexity: The time complexity is O(N), where N is the number of digits in
      the input array. In the worst case (e.g., `[9,9,...,9]`), we iterate through all
      N digits once. In the best case (e.g., `[1,2,3]`), we perform a single operation
      and return.
    space_complexity: The space complexity is O(1) in most cases, as we modify the input
      array in place. However, in the worst-case scenario where all digits are 9 (e.g.,
      `[9,9,9]`), we need to create a new array of size N+1 to accommodate the carry-over
      (e.g., `[1,0,0,0]`). This makes the worst-case space complexity O(N).
    elapsed_time: 26.642946243286133
    model: gemini-2.5-flash
    generated_at: '2026-01-01 01:15:37 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> plusOne(vector<int>& digits)\
        \ {\n        for (int i = digits.size() - 1; i >= 0; --i) {\n            if\
        \ (digits[i] < 9) {\n                digits[i]++;\n                return digits;\n\
        \            }\n            digits[i] = 0;\n        }\n        digits.insert(digits.begin(),\
        \ 1);\n        return digits;\n    }\n};"
      java: "class Solution {\n    public int[] plusOne(int[] digits) {\n        for\
        \ (int i = digits.length - 1; i >= 0; i--) {\n            if (digits[i] < 9)\
        \ {\n                digits[i]++;\n                return digits;\n        \
        \    }\n            digits[i] = 0;\n        }\n        int[] newDigits = new\
        \ int[digits.length + 1];\n        newDigits[0] = 1;\n        return newDigits;\n\
        \    }\n}"
      python: "class Solution:\n    def plusOne(self, digits: list[int]) -> list[int]:\n\
        \        for i in range(len(digits) - 1, -1, -1):\n            if digits[i]\
        \ < 9:\n                digits[i] += 1\n                return digits\n    \
        \        digits[i] = 0\n        return [1] + digits"
      python3: "class Solution:\n    def plusOne(self, digits: list[int]) -> list[int]:\n\
        \        for i in range(len(digits) - 1, -1, -1):\n            if digits[i]\
        \ < 9:\n                digits[i] += 1\n                return digits\n    \
        \        digits[i] = 0\n        return [1] + digits"
      c: "void plusOne(int* digits, int digitsSize) {\n    for (int i = digitsSize -\
        \ 1; i >= 0; i--) {\n        if (digits[i] < 9) {\n            digits[i]++;\n\
        \            return;\n        }\n        digits[i] = 0;\n    }\n    int* newDigits\
        \ = (int*)malloc((digitsSize + 1) * sizeof(int));\n    newDigits[0] = 1;\n \
        \   for (int i = 1; i <= digitsSize; i++) {\n        newDigits[i] = digits[i\
        \ - 1];\n    }\n    free(digits);\n}"
      csharp: "public class Solution {\n    public int[] PlusOne(int[] digits) {\n \
        \       for (int i = digits.Length - 1; i >= 0; i--) {\n            if (digits[i]\
        \ < 9) {\n                digits[i]++;\n                return digits;\n   \
        \         }\n            digits[i] = 0;\n        }\n        int[] newDigits\
        \ = new int[digits.Length + 1];\n        newDigits[0] = 1;\n        return newDigits;\n\
        \    }\n}"
      javascript: "var plusOne = function(digits) {\n    for (let i = digits.length\
        \ - 1; i >= 0; i--) {\n        if (digits[i] < 9) {\n            digits[i]++;\n\
        \            return digits;\n        }\n        digits[i] = 0;\n    }\n    return\
        \ [1].concat(digits);\n};"
      typescript: "function plusOne(digits: number[]): number[] {\n    for (let i =\
        \ digits.length - 1; i >= 0; i--) {\n        if (digits[i] < 9) {\n        \
        \    digits[i]++;\n            return digits;\n        }\n        digits[i]\
        \ = 0;\n    }\n    return [1].concat(digits);\n}"
      php: "$plusOne = function($digits) {\n    for ($i = count($digits) - 1; $i >=\
        \ 0; $i--) {\n        if ($digits[$i] < 9) {\n            $digits[$i]++;\n \
        \           return $digits;\n        }\n        $digits[$i] = 0;\n    }\n  \
        \  return array_merge([1], $digits);\n};"
      swift: "class Solution {\n    func plusOne(_ digits: [Int]) -> [Int] {\n     \
        \   var digits = digits\n        for i in stride(from: digits.count - 1, through:\
        \ 0, by: -1) {\n            if digits[i] < 9 {\n                digits[i] +=\
        \ 1\n                return digits\n            }\n            digits[i] = 0\n\
        \        }\n        return [1] + digits\n    }\n}"
      kotlin: "class Solution {\n    fun plusOne(digits: IntArray): IntArray {\n   \
        \     for (i in digits.lastIndex downTo 0) {\n            if (digits[i] < 9)\
        \ {\n                digits[i]++\n                return digits\n          \
        \  }\n            digits[i] = 0\n        }\n        return intArrayOf(1) + digits\n\
        \    }\n}"
      dart: "class Solution {\n    List<int> plusOne(List<int> digits) {\n        for\
        \ (int i = digits.length - 1; i >= 0; i--) {\n            if (digits[i] < 9)\
        \ {\n                digits[i]++;\n                return digits;\n        \
        \    }\n            digits[i] = 0;\n        }\n        return [1]..addAll(digits);\n\
        \    }\n}"
      go: "func plusOne(digits []int) []int {\n    for i := len(digits) - 1; i >= 0;\
        \ i-- {\n        if digits[i] < 9 {\n            digits[i]++\n            return\
        \ digits\n        }\n        digits[i] = 0\n    }\n    return append([]int{1},\
        \ digits...)\n}"
      ruby: "def plus_one(digits)\n    (digits.size - 1).downto(0) do |i|\n        if\
        \ digits[i] < 9\n            digits[i] += 1\n            return digits\n   \
        \     end\n        digits[i] = 0\n    end\n    [1] + digits\nend"
      scala: "object Solution {\n    def plusOne(digits: Array[Int]): Array[Int] = {\n\
        \        for (i <- digits.lastIndex to 0 by -1) {\n            if (digits(i)\
        \ < 9) {\n                digits(i) += 1\n                return digits\n  \
        \          }\n            digits(i) = 0\n        }\n        Array(1) ++ digits\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32>\
        \ {\n        for i in (0..digits.len()).rev() {\n            if digits[i] <\
        \ 9 {\n                digits[i] += 1;\n                return digits;\n   \
        \         }\n            digits[i] = 0;\n        }\n        vec![1].into_iter().chain(digits).collect()\n\
        \    }\n}"
      racket: "(define (plus-one digits)\n    (let loop ((i (- (length digits) 1)))\n\
        \        (cond ((< i 0) (cons 1 digits))\n              ((< (list-ref digits\
        \ i) 9) (list-set! digits i (+ (list-ref digits i) 1)) digits)\n           \
        \   (else (list-set! digits i 0) (loop (- i 1))))))"
      erlang: "-module(solution).\n-export([plus_one/1]).\nplus_one(Digits) ->\n   \
        \ plus_one(Digits, length(Digits) - 1).\nplus_one(Digits, -1) -> [1|Digits];\n\
        plus_one(Digits, Index) ->\n    case lists:nth(Index + 1, Digits) of\n     \
        \   X when X < 9 ->\n            lists:sublist(Digits, 1, Index) ++ [X + 1]\
        \ ++ lists:sublist(Digits, Index + 2, length(Digits));\n        _ ->\n     \
        \       lists:sublist(Digits, 1, Index) ++ [0] ++ plus_one(lists:sublist(Digits,\
        \ Index + 1, length(Digits)), Index - 1)\n    end."
      elixir: "defmodule Solution do\n    def plus_one(digits) do\n        plus_one(digits,\
        \ length(digits) - 1)\n    end\n    defp plus_one(digits, -1) do\n        [1|digits]\n\
        \    end\n    defp plus_one(digits, index) do\n        case Enum.at(digits,\
        \ index) do\n            x when x < 9 ->\n                List.replace_at(digits,\
        \ index, x + 1)\n            _ ->\n                List.replace_at(digits, index,\
        \ 0) |> plus_one(index - 1)\n        end\n    end\nend"
    approach: The problem can be solved by iterating over the array of digits from right
      to left. When a digit is less than 9, we can simply increment it by one and return
      the array. However, if a digit is 9, we need to set it to 0 and carry over the
      increment to the next digit. This process continues until we find a digit that
      is less than 9 or we reach the beginning of the array. If all digits are 9, we
      need to add a new digit at the beginning of the array, which is 1. The key intuition
      here is to handle the carry-over process correctly and to consider the edge case
      where all digits are 9.
    time_complexity: O(n) where n is the number of digits in the array. This is because
      we are potentially iterating over the entire array once.
    space_complexity: O(1) if we do not consider the space required for the output array.
      However, if we consider the space required for the output array, it would be O(n)
      where n is the number of digits in the array. This is because in the worst-case
      scenario, we might need to add a new digit at the beginning of the array.
    elapsed_time: 5.308687686920166
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-01 01:15:42 '
---

## Problem #66: Plus One

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

<p>You are given a <strong>large integer</strong> represented as an integer array <code>digits</code>, where each <code>digits[i]</code> is the <code>i<sup>th</sup></code> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading <code>0</code>&#39;s.</p>

<p>Increment the large integer by one and return <em>the resulting array of digits</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [9]
<strong>Output:</strong> [1,0]
<strong>Explanation:</strong> The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
	<li><code>digits</code> does not contain any leading <code>0</code>&#39;s.</li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-01 01:15:37 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to increment a large integer represented as an array of digits. We can simulate the standard addition process by iterating through the digits from right to left (least significant to most significant). We start by adding one to the rightmost digit. If the digit becomes less than 10 (i.e., no carry-over), we simply update that digit and return the array, as the addition is complete. This handles cases like [1,2,3] becoming [1,2,4] or [4,3,2,9] becoming [4,3,3,0].

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
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        vector<int> result(n + 1, 0);
        result[0] = 1;
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        int[] result = new int[n + 1];
        result[0] = 1;
        // The rest of the elements are already 0 by default
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we reach here, all digits were 9 (e.g., [9,9,9])
        # We need to prepend a 1 and set all other digits to 0
        return [1] + digits
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we reach here, all digits were 9 (e.g., [9,9,9])
        # We need to prepend a 1 and set all other digits to 0
        return [1] + digits
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, and free'd by the caller.
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    for (int i = digitsSize - 1; i >= 0; --i) {
        if (digits[i] < 9) {
            digits[i]++;
            *returnSize = digitsSize;
            return digits;
        }
        digits[i] = 0;
    }

    // If we reach here, all digits were 9 (e.g., [9,9,9])
    // We need to create a new array of size digitsSize + 1
    int* result = (int*)malloc(sizeof(int) * (digitsSize + 1));
    result[0] = 1;
    for (int i = 1; i <= digitsSize; ++i) {
        result[i] = 0;
    }
    *returnSize = digitsSize + 1;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] PlusOne(int[] digits) {
        int n = digits.Length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        int[] result = new int[n + 1];
        result[0] = 1;
        // The rest of the elements are already 0 by default for int arrays
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    const n = digits.length;
    for (let i = n - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }

    // If we reach here, all digits were 9 (e.g., [9,9,9])
    // We need to prepend a 1 and set all other digits to 0
    const result = new Array(n + 1).fill(0);
    result[0] = 1;
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function plusOne(digits: number[]): number[] {
    const n = digits.length;
    for (let i = n - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }

    // If we reach here, all digits were 9 (e.g., [9,9,9])
    // We need to prepend a 1 and set all other digits to 0
    const result = new Array(n + 1).fill(0);
    result[0] = 1;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function plusOne($digits) {
        $n = count($digits);
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($digits[$i] < 9) {
                $digits[$i]++;
                return $digits;
            }
            $digits[$i] = 0;
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        array_unshift($digits, 1);
        return $digits;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var digits = digits // Make it mutable
        let n = digits.count
        for i in (0..<n).reversed() {
            if digits[i] < 9 {
                digits[i] += 1
                return digits
            }
            digits[i] = 0
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        var result = Array(repeating: 0, count: n + 1)
        result[0] = 1
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun plusOne(digits: IntArray): IntArray {
        val n = digits.size
        for (i in n - 1 downTo 0) {
            if (digits[i] < 9) {
                digits[i]++
                return digits
            }
            digits[i] = 0
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        val result = IntArray(n + 1)
        result[0] = 1
        // The rest of the elements are already 0 by default
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> plusOne(List<int> digits) {
    int n = digits.length;
    for (int i = n - 1; i >= 0; i--) {
      if (digits[i] < 9) {
        digits[i]++;
        return digits;
      }
      digits[i] = 0;
    }

    // If we reach here, all digits were 9 (e.g., [9,9,9])
    // We need to prepend a 1 and set all other digits to 0
    List<int> result = List.filled(n + 1, 0);
    result[0] = 1;
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func plusOne(digits []int) []int {
    n := len(digits)
    for i := n - 1; i >= 0; i-- {
        if digits[i] < 9 {
            digits[i]++
            return digits
        }
        digits[i] = 0
    }

    // If we reach here, all digits were 9 (e.g., [9,9,9])
    // We need to prepend a 1 and set all other digits to 0
    result := make([]int, n + 1)
    result[0] = 1
    // The rest of the elements are already 0 by default
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def plus_one(digits)
    n = digits.length
    (n - 1).downto(0) do |i|
        if digits[i] < 9
            digits[i] += 1
            return digits
        end
        digits[i] = 0
    end

    # If we reach here, all digits were 9 (e.g., [9,9,9])
    # We need to prepend a 1 and set all other digits to 0
    [1] + digits
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def plusOne(digits: Array[Int]): Array[Int] = {
        val n = digits.length
        for (i <- n - 1 to 0 by -1) {
            if (digits(i) < 9) {
                digits(i) += 1
                return digits
            }
            digits(i) = 0
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        val result = new Array[Int](n + 1)
        result(0) = 1
        // The rest of the elements are already 0 by default
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut digits = digits; // Make it mutable
        let n = digits.len();
        for i in (0..n).rev() {
            if digits[i] < 9 {
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }

        // If we reach here, all digits were 9 (e.g., [9,9,9])
        // We need to prepend a 1 and set all other digits to 0
        let mut result = vec![0; n + 1];
        result[0] = 1;
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (plus-one digits)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((num-str (string-join (map number->string digits) ""))
         (num (+ (string->number num-str) 1))
         (result-str (number->string num)))
    (map (lambda (char) (string->number (string char))) (string->list result-str))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([plus_one/1]).

plus_one(Digits) ->
    % Convert list of digits to a string, then to an integer
    NumStr = lists:foldl(fun(D, Acc) -> io_lib:format("~s~p", [Acc, D]) end, "", Digits),
    Num = list_to_integer(NumStr),

    ResultNum = Num + 1,
    ResultStr = integer_to_list(ResultNum),

    % Convert result string back to a list of digits
    lists:map(fun(C) -> C - $0 end, ResultStr).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec plus_one(digits :: [integer]) :: [integer]
  def plus_one(digits) do
    num_str = Enum.map_join(digits, "", &Integer.to_string/1)
    num = String.to_integer(num_str)
    result_num = num + 1

    result_num
    |> Integer.to_string()
    |> String.graphemes()
    |> Enum.map(&String.to_integer/1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of digits in the input array. In the worst case (e.g., `[9,9,...,9]`), we iterate through all N digits once. In the best case (e.g., `[1,2,3]`), we perform a single operation and return.

- **Space Complexity:** The space complexity is O(1) in most cases, as we modify the input array in place. However, in the worst-case scenario where all digits are 9 (e.g., `[9,9,9]`), we need to create a new array of size N+1 to accommodate the carry-over (e.g., `[1,0,0,0]`). This makes the worst-case space complexity O(N).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-01 01:15:42 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over the array of digits from right to left. When a digit is less than 9, we can simply increment it by one and return the array. However, if a digit is 9, we need to set it to 0 and carry over the increment to the next digit. This process continues until we find a digit that is less than 9 or we reach the beginning of the array. If all digits are 9, we need to add a new digit at the beginning of the array, which is 1. The key intuition here is to handle the carry-over process correctly and to consider the edge case where all digits are 9.

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
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] newDigits = new int[digits.length + 1];
        newDigits[0] = 1;
        return newDigits;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
void plusOne(int* digits, int digitsSize) {
    for (int i = digitsSize - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return;
        }
        digits[i] = 0;
    }
    int* newDigits = (int*)malloc((digitsSize + 1) * sizeof(int));
    newDigits[0] = 1;
    for (int i = 1; i <= digitsSize; i++) {
        newDigits[i] = digits[i - 1];
    }
    free(digits);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] PlusOne(int[] digits) {
        for (int i = digits.Length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] newDigits = new int[digits.Length + 1];
        newDigits[0] = 1;
        return newDigits;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var plusOne = function(digits) {
    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    return [1].concat(digits);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function plusOne(digits: number[]): number[] {
    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    return [1].concat(digits);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
$plusOne = function($digits) {
    for ($i = count($digits) - 1; $i >= 0; $i--) {
        if ($digits[$i] < 9) {
            $digits[$i]++;
            return $digits;
        }
        $digits[$i] = 0;
    }
    return array_merge([1], $digits);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var digits = digits
        for i in stride(from: digits.count - 1, through: 0, by: -1) {
            if digits[i] < 9 {
                digits[i] += 1
                return digits
            }
            digits[i] = 0
        }
        return [1] + digits
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun plusOne(digits: IntArray): IntArray {
        for (i in digits.lastIndex downTo 0) {
            if (digits[i] < 9) {
                digits[i]++
                return digits
            }
            digits[i] = 0
        }
        return intArrayOf(1) + digits
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    List<int> plusOne(List<int> digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        return [1]..addAll(digits);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func plusOne(digits []int) []int {
    for i := len(digits) - 1; i >= 0; i-- {
        if digits[i] < 9 {
            digits[i]++
            return digits
        }
        digits[i] = 0
    }
    return append([]int{1}, digits...)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def plus_one(digits)
    (digits.size - 1).downto(0) do |i|
        if digits[i] < 9
            digits[i] += 1
            return digits
        end
        digits[i] = 0
    end
    [1] + digits
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def plusOne(digits: Array[Int]): Array[Int] = {
        for (i <- digits.lastIndex to 0 by -1) {
            if (digits(i) < 9) {
                digits(i) += 1
                return digits
            }
            digits(i) = 0
        }
        Array(1) ++ digits
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        for i in (0..digits.len()).rev() {
            if digits[i] < 9 {
                digits[i] += 1;
                return digits;
            }
            digits[i] = 0;
        }
        vec![1].into_iter().chain(digits).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (plus-one digits)
    (let loop ((i (- (length digits) 1)))
        (cond ((< i 0) (cons 1 digits))
              ((< (list-ref digits i) 9) (list-set! digits i (+ (list-ref digits i) 1)) digits)
              (else (list-set! digits i 0) (loop (- i 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([plus_one/1]).
plus_one(Digits) ->
    plus_one(Digits, length(Digits) - 1).
plus_one(Digits, -1) -> [1|Digits];
plus_one(Digits, Index) ->
    case lists:nth(Index + 1, Digits) of
        X when X < 9 ->
            lists:sublist(Digits, 1, Index) ++ [X + 1] ++ lists:sublist(Digits, Index + 2, length(Digits));
        _ ->
            lists:sublist(Digits, 1, Index) ++ [0] ++ plus_one(lists:sublist(Digits, Index + 1, length(Digits)), Index - 1)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def plus_one(digits) do
        plus_one(digits, length(digits) - 1)
    end
    defp plus_one(digits, -1) do
        [1|digits]
    end
    defp plus_one(digits, index) do
        case Enum.at(digits, index) do
            x when x < 9 ->
                List.replace_at(digits, index, x + 1)
            _ ->
                List.replace_at(digits, index, 0) |> plus_one(index - 1)
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of digits in the array. This is because we are potentially iterating over the entire array once.

- **Space Complexity:** O(1) if we do not consider the space required for the output array. However, if we consider the space required for the output array, it would be O(n) where n is the number of digits in the array. This is because in the worst-case scenario, we might need to add a new digit at the beginning of the array.

</div>
</details>
