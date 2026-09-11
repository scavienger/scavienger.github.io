---
layout: post
title: "Unique 3-Digit Even Numbers"
date: 2026-09-11 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Recursion", "Enumeration"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/unique-3-digit-even-numbers/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int totalNumbers(vector<int>& digits) {\n\
        \        int counts[10] = {0};\n        for (int d : digits) {\n           \
        \ counts[d]++;\n        }\n        int result = 0;\n        for (int i = 100;\
        \ i <= 998; i += 2) {\n            int d1 = i / 100;\n            int d2 = (i\
        \ / 10) % 10;\n            int d3 = i % 10;\n            counts[d1]--;\n   \
        \         counts[d2]--;\n            counts[d3]--;\n            if (counts[d1]\
        \ >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {\n                result++;\n\
        \            }\n            counts[d1]++;\n            counts[d2]++;\n     \
        \       counts[d3]++;\n        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public int totalNumbers(int[] digits) {\n       \
        \ int[] counts = new int[10];\n        for (int d : digits) {\n            counts[d]++;\n\
        \        }\n        int result = 0;\n        for (int i = 100; i <= 998; i +=\
        \ 2) {\n            int d1 = i / 100;\n            int d2 = (i / 10) % 10;\n\
        \            int d3 = i % 10;\n            counts[d1]--;\n            counts[d2]--;\n\
        \            counts[d3]--;\n            if (counts[d1] >= 0 && counts[d2] >=\
        \ 0 && counts[d3] >= 0) {\n                result++;\n            }\n      \
        \      counts[d1]++;\n            counts[d2]++;\n            counts[d3]++;\n\
        \        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def totalNumbers(self, digits):\n      \
        \  \"\"\"\n        :type digits: List[int]\n        :rtype: int\n        \"\"\
        \"\n        counts = [0] * 10\n        for d in digits:\n            counts[d]\
        \ += 1\n        result = 0\n        for i in range(100, 1000, 2):\n        \
        \    d1, d2, d3 = i // 100, (i // 10) % 10, i % 10\n            counts[d1] -=\
        \ 1\n            counts[d2] -= 1\n            counts[d3] -= 1\n            if\
        \ counts[d1] >= 0 and counts[d2] >= 0 and counts[d3] >= 0:\n               \
        \ result += 1\n            counts[d1] += 1\n            counts[d2] += 1\n  \
        \          counts[d3] += 1\n        return result"
      python3: "class Solution:\n    def totalNumbers(self, digits: List[int]) -> int:\n\
        \        counts = [0] * 10\n        for d in digits:\n            counts[d]\
        \ += 1\n        result = 0\n        for i in range(100, 1000, 2):\n        \
        \    d1, d2, d3 = i // 100, (i // 10) % 10, i % 10\n            counts[d1] -=\
        \ 1\n            counts[d2] -= 1\n            counts[d3] -= 1\n            if\
        \ counts[d1] >= 0 and counts[d2] >= 0 and counts[d3] >= 0:\n               \
        \ result += 1\n            counts[d1] += 1\n            counts[d2] += 1\n  \
        \          counts[d3] += 1\n        return result"
      c: "int totalNumbers(int* digits, int digitsSize) {\n    int counts[10] = {0};\n\
        \    for (int i = 0; i < digitsSize; i++) {\n        counts[digits[i]]++;\n\
        \    }\n    int result = 0;\n    for (int i = 100; i <= 998; i += 2) {\n   \
        \     int d1 = i / 100;\n        int d2 = (i / 10) % 10;\n        int d3 = i\
        \ % 10;\n        counts[d1]--;\n        counts[d2]--;\n        counts[d3]--;\n\
        \        if (counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {\n    \
        \        result++;\n        }\n        counts[d1]++;\n        counts[d2]++;\n\
        \        counts[d3]++;\n    }\n    return result;\n}"
      csharp: "public class Solution {\n    public int TotalNumbers(int[] digits) {\n\
        \        int[] counts = new int[10];\n        foreach (int d in digits) {\n\
        \            counts[d]++;\n        }\n        int result = 0;\n        for (int\
        \ i = 100; i <= 998; i += 2) {\n            int d1 = i / 100;\n            int\
        \ d2 = (i / 10) % 10;\n            int d3 = i % 10;\n            counts[d1]--;\n\
        \            counts[d2]--;\n            counts[d3]--;\n            if (counts[d1]\
        \ >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {\n                result++;\n\
        \            }\n            counts[d1]++;\n            counts[d2]++;\n     \
        \       counts[d3]++;\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} digits\n * @return {number}\n */\nvar totalNumbers\
        \ = function(digits) {\n    const counts = new Array(10).fill(0);\n    for (const\
        \ d of digits) {\n        counts[d]++;\n    }\n    let result = 0;\n    for\
        \ (let i = 100; i <= 998; i += 2) {\n        const d1 = Math.floor(i / 100);\n\
        \        const d2 = Math.floor((i / 10) % 10);\n        const d3 = i % 10;\n\
        \        counts[d1]--;\n        counts[d2]--;\n        counts[d3]--;\n     \
        \   if (counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {\n         \
        \   result++;\n        }\n        counts[d1]++;\n        counts[d2]++;\n   \
        \     counts[d3]++;\n    }\n    return result;\n};"
      typescript: "function totalNumbers(digits: number[]): number {\n    const counts\
        \ = new Array(10).fill(0);\n    for (const d of digits) {\n        counts[d]++;\n\
        \    }\n    let ans = 0;\n    for (let i = 100; i <= 998; i += 2) {\n      \
        \  const freq = new Array(10).fill(0);\n        let temp = i;\n        while\
        \ (temp > 0) {\n            freq[temp % 10]++;\n            temp = Math.floor(temp\
        \ / 10);\n        }\n        let possible = true;\n        for (let j = 0; j\
        \ < 10; j++) {\n            if (freq[j] > counts[j]) {\n                possible\
        \ = false;\n                break;\n            }\n        }\n        if (possible)\
        \ {\n            ans++;\n        }\n    }\n    return ans;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $digits\n     * @return\
        \ Integer\n     */\n    function totalNumbers($digits) {\n        $counts =\
        \ array_fill(0, 10, 0);\n        foreach ($digits as $d) {\n            $counts[$d]++;\n\
        \        }\n        $ans = 0;\n        for ($i = 100; $i <= 998; $i += 2) {\n\
        \            $freq = array_fill(0, 10, 0);\n            $temp = $i;\n      \
        \      while ($temp > 0) {\n                $freq[($temp % 10)]++;\n       \
        \         $temp = (int)($temp / 10);\n            }\n            $possible =\
        \ true;\n            for ($j = 0; $j < 10; $j++) {\n                if ($freq[$j]\
        \ > $counts[$j]) {\n                    $possible = false;\n               \
        \     break;\n                }\n            }\n            if ($possible) {\n\
        \                $ans++;\n            }\n        }\n        return $ans;\n \
        \   }\n}"
      swift: "class Solution {\n    func totalNumbers(_ digits: [Int]) -> Int {\n  \
        \      var counts = [Int](repeating: 0, count: 10)\n        for d in digits\
        \ {\n            counts[d] += 1\n        }\n        var ans = 0\n        for\
        \ i in stride(from: 100, through: 998, by: 2) {\n            var freq = [Int](repeating:\
        \ 0, count: 10)\n            var temp = i\n            while temp > 0 {\n  \
        \              freq[temp % 10] += 1\n                temp /= 10\n          \
        \  }\n            var possible = true\n            for j in 0..<10 {\n     \
        \           if freq[j] > counts[j] {\n                    possible = false\n\
        \                    break\n                }\n            }\n            if\
        \ possible {\n                ans += 1\n            }\n        }\n        return\
        \ ans\n    }\n}"
      kotlin: "class Solution {\n    fun totalNumbers(digits: IntArray): Int {\n   \
        \     val counts = IntArray(10)\n        for (d in digits) {\n            counts[d]++\n\
        \        }\n        var ans = 0\n        for (i in 100..998 step 2) {\n    \
        \        val freq = IntArray(10)\n            var temp = i\n            while\
        \ (temp > 0) {\n                freq[temp % 10]++\n                temp /= 10\n\
        \            }\n            var possible = true\n            for (j in 0..9)\
        \ {\n                if (freq[j] > counts[j]) {\n                    possible\
        \ = false\n                    break\n                }\n            }\n   \
        \         if (possible) {\n                ans++\n            }\n        }\n\
        \        return ans\n    }\n}"
      dart: "class Solution {\n  int totalNumbers(List<int> digits) {\n    List<int>\
        \ counts = List.filled(10, 0);\n    for (int d in digits) {\n      counts[d]++;\n\
        \    }\n    int ans = 0;\n    for (int i = 100; i <= 998; i += 2) {\n      List<int>\
        \ freq = List.filled(10, 0);\n      int temp = i;\n      while (temp > 0) {\n\
        \        freq[temp % 10]++;\n        temp ~/= 10;\n      }\n      bool possible\
        \ = true;\n      for (int j = 0; j < 10; j++) {\n        if (freq[j] > counts[j])\
        \ {\n          possible = false;\n          break;\n        }\n      }\n   \
        \   if (possible) {\n        ans++;\n      }\n    }\n    return ans;\n  }\n}"
      go: "func totalNumbers(digits []int) int {\n    counts := make([]int, 10)\n  \
        \  for _, d := range digits {\n        counts[d]++\n    }\n    ans := 0\n  \
        \  for i := 100; i <= 998; i += 2 {\n        freq := make([]int, 10)\n     \
        \   temp := i\n        for temp > 0 {\n            freq[temp % 10]++\n     \
        \       temp /= 10\n        }\n        possible := true\n        for j := 0;\
        \ j < 10; j++ {\n            if freq[j] > counts[j] {\n                possible\
        \ = false\n                break\n            }\n        }\n        if possible\
        \ {\n            ans++\n        }\n    }\n    return ans\n}"
      ruby: "def total_numbers(digits)\n  counts = Hash.new(0)\n  digits.each { |d|\
        \ counts[d] += 1 }\n  (100..998).step(2).count do |i|\n    d1 = i / 100\n  \
        \  d2 = (i / 10) % 10\n    d3 = i % 10\n\n    counts[d1] -= 1\n    counts[d2]\
        \ -= 1\n    counts[d3] -= 1\n\n    ok = counts[d1] >= 0 && counts[d2] >= 0 &&\
        \ counts[d3] >= 0\n\n    counts[d1] += 1\n    counts[d2] += 1\n    counts[d3]\
        \ += 1\n\n    ok\n  end\nend"
      scala: "object Solution {\n  def totalNumbers(digits: Array[Int]): Int = {\n \
        \   val counts = new Array[Int](10)\n    digits.foreach(d => counts(d) += 1)\n\
        \    var result = 0\n    for (i <- 100 to 998 by 2) {\n      val d1 = i / 100\n\
        \      val d2 = (i / 10) % 10\n      val d3 = i % 10\n\n      counts(d1) -=\
        \ 1\n      counts(d2) -= 1\n      counts(d3) -= 1\n\n      if (counts(d1) >=\
        \ 0 && counts(d2) >= 0 && counts(d3) >= 0) {\n        result += 1\n      }\n\
        \n      counts(d1) += 1\n      counts(d2) += 1\n      counts(d3) += 1\n    }\n\
        \    result\n  }\n}"
      rust: "impl Solution {\n    pub fn total_numbers(digits: Vec<i32>) -> i32 {\n\
        \        let mut counts = [0; 10];\n        for &d in &digits {\n          \
        \  counts[d as usize] += 1;\n        }\n        let mut result = 0;\n      \
        \  for i in (100..1000).step_by(2) {\n            let d1 = i / 100;\n      \
        \      let d2 = (i / 10) % 10;\n            let d3 = i % 10;\n\n           \
        \ counts[d1] -= 1;\n            counts[d2] -= 1;\n            counts[d3] -=\
        \ 1;\n\n            if counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0\
        \ {\n                result += 1;\n            }\n\n            counts[d1] +=\
        \ 1;\n            counts[d2] += 1;\n            counts[d3] += 1;\n        }\n\
        \        result\n    }\n}"
      racket: "(define/contract (total-numbers digits)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([counts (make-vector 10 0)])\n    (for ([d digits])\n\
        \      (vector-set! counts d (+ (vector-ref counts d) 1)))\n    (let loop ([i\
        \ 100] [res 0])\n      (if (> i 998)\n          res\n          (let* ([d1 (quotient\
        \ i 100)]\n                 [d2 (remainder (quotient i 10) 10)]\n          \
        \       [d3 (remainder i 10)])\n            (vector-set! counts d1 (- (vector-ref\
        \ counts d1) 1))\n            (vector-set! counts d2 (- (vector-ref counts d2)\
        \ 1))\n            (vector-set! counts d3 (- (vector-ref counts d3) 1))\n  \
        \          (let ([ok (and (>= (vector-ref counts d1) 0)\n                  \
        \         (>= (vector-ref counts d2) 0)\n                           (>= (vector-ref\
        \ counts d3) 0))])\n              (vector-set! counts d3 (+ (vector-ref counts\
        \ d3) 1))\n              (vector-set! counts d2 (+ (vector-ref counts d2) 1))\n\
        \              (vector-set! counts d1 (+ (vector-ref counts d1) 1))\n      \
        \        (loop (+ i 2) (if ok (+ res 1) res))))))))"
      erlang: "-spec total_numbers(Digits :: [integer()]) -> integer().\ntotal_numbers(Digits)\
        \ ->\n    Counts = lists:foldl(fun(D, Acc) -> \n        maps:put(D, maps:get(D,\
        \ Acc, 0) + 1, Acc) \n    end, #{}, Digits),\n    lists:foldl(fun(I, Acc) ->\n\
        \        D1 = I div 100,\n        D2 = (I div 10) rem 10,\n        D3 = I rem\
        \ 10,\n        case can_form([D1, D2, D3], Counts) of\n            true -> Acc\
        \ + 1;\n            false -> Acc\n        end\n    end, 0, lists:seq(100, 998,\
        \ 2)).\n\ncan_form([], _) -> true;\ncan_form([H | T], Counts) ->\n    case maps:get(H,\
        \ Counts, 0) of\n        0 -> false;\n        N -> can_form(T, maps:put(H, N\
        \ - 1, Counts))\n    end."
      elixir: "defmodule Solution do\n  @spec total_numbers(digits :: [integer]) ::\
        \ integer\n  def total_numbers(digits) do\n    counts = Enum.frequencies(digits)\n\
        \    100..998\n    |> Enum.filter(&(rem(&1, 2) == 0))\n    |> Enum.count(fn\
        \ i ->\n      d1 = div(i, 100)\n      d2 = rem(div(i, 10), 10)\n      d3 = rem(i,\
        \ 10)\n      can_form?([d1, d2, d3], counts)\n    end)\n  end\n\n  defp can_form?([],\
        \ _), do: true\n  defp can_form?([h | t], counts) do\n    case Map.get(counts,\
        \ h, 0) do\n      0 -> false\n      n -> can_form?(t, Map.put(counts, h, n -\
        \ 1))\n    end\n  end\nend"
    approach: 'To solve this problem efficiently, we utilize the fact that there are
      only 450 possible three-digit even numbers (ranging from 100 to 998). Instead
      of generating all permutations of the input digits, which could be less efficient
      and require complex handling of duplicates and leading zeros, we iterate through
      every possible three-digit even number and check if it can be constructed from
      the given pool of digits.


      First, we count the frequency of each digit (0-9) present in the input array.
      Then, for each even number from 100 to 998, we extract its three digits and calculate
      the frequency of each digit required to form that number. If the input pool contains
      enough of each required digit, we increment our counter. This brute-force approach
      over the range of numbers ensures we only count distinct numbers and naturally
      handles the constraints of no leading zeros and single-use digits.'
    time_complexity: O(N) where N is the length of the digits array. The algorithm performs
      a single pass over the input array to count digit frequencies, taking O(N) time,
      followed by a constant 450 iterations (from 100 to 998 in steps of 2) to check
      each candidate even number.
    space_complexity: O(1) because the space used for the digit frequency array is fixed
      at 10 (digits 0-9), which does not grow with the size of the input array.
    elapsed_time: 231.84770917892456
    model: gemini-3-flash-preview
    generated_at: '2026-09-11 02:23:25 '
---

## Problem #3483: Unique 3-Digit Even Numbers

**Difficulty:** Easy

**Topics:** Array, Hash Table, Recursion, Enumeration

## Problem Description

<p>You are given an array of digits called <code>digits</code>. Your task is to determine the number of <strong>distinct</strong> three-digit even numbers that can be formed using these digits.</p>

<p><strong>Note</strong>: Each <em>copy</em> of a digit can only be used <strong>once per number</strong>, and there may <strong>not</strong> be leading zeros.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">digits = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong> The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">digits = [0,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong> The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">digits = [6,6,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong> Only 666 can be formed.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">digits = [1,3,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong> No even 3-digit numbers can be formed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= digits.length &lt;= 10</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
</ul>


## Hints

1. Use brute force to try all possibilities

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we utilize the fact that there are only 450 possible three-digit even numbers (ranging from 100 to 998). Instead of generating all permutations of the input digits, which could be less efficient and require complex handling of duplicates and leading zeros, we iterate through every possible three-digit even number and check if it can be constructed from the given pool of digits.

First, we count the frequency of each digit (0-9) present in the input array. Then, for each even number from 100 to 998, we extract its three digits and calculate the frequency of each digit required to form that number. If the input pool contains enough of each required digit, we increment our counter. This brute-force approach over the range of numbers ensures we only count distinct numbers and naturally handles the constraints of no leading zeros and single-use digits.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang" id="lang-cpp" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-python">
  <input type="radio" name="code-lang" id="lang-python3">
  <input type="radio" name="code-lang" id="lang-c">
  <input type="radio" name="code-lang" id="lang-csharp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-php">
  <input type="radio" name="code-lang" id="lang-swift">
  <input type="radio" name="code-lang" id="lang-kotlin">
  <input type="radio" name="code-lang" id="lang-dart">
  <input type="radio" name="code-lang" id="lang-go">
  <input type="radio" name="code-lang" id="lang-ruby">
  <input type="radio" name="code-lang" id="lang-scala">
  <input type="radio" name="code-lang" id="lang-rust">
  <input type="radio" name="code-lang" id="lang-racket">
  <input type="radio" name="code-lang" id="lang-erlang">
  <input type="radio" name="code-lang" id="lang-elixir">
  <div class="tab-labels">
    <label for="lang-cpp">C++</label>
    <label for="lang-java">Java</label>
    <label for="lang-python">Python</label>
    <label for="lang-python3">Python3</label>
    <label for="lang-c">C</label>
    <label for="lang-csharp">C#</label>
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-php">PHP</label>
    <label for="lang-swift">Swift</label>
    <label for="lang-kotlin">Kotlin</label>
    <label for="lang-dart">Dart</label>
    <label for="lang-go">Go</label>
    <label for="lang-ruby">Ruby</label>
    <label for="lang-scala">Scala</label>
    <label for="lang-rust">Rust</label>
    <label for="lang-racket">Racket</label>
    <label for="lang-erlang">Erlang</label>
    <label for="lang-elixir">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int counts[10] = {0};
        for (int d : digits) {
            counts[d]++;
        }
        int result = 0;
        for (int i = 100; i <= 998; i += 2) {
            int d1 = i / 100;
            int d2 = (i / 10) % 10;
            int d3 = i % 10;
            counts[d1]--;
            counts[d2]--;
            counts[d3]--;
            if (counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {
                result++;
            }
            counts[d1]++;
            counts[d2]++;
            counts[d3]++;
        }
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
    public int totalNumbers(int[] digits) {
        int[] counts = new int[10];
        for (int d : digits) {
            counts[d]++;
        }
        int result = 0;
        for (int i = 100; i <= 998; i += 2) {
            int d1 = i / 100;
            int d2 = (i / 10) % 10;
            int d3 = i % 10;
            counts[d1]--;
            counts[d2]--;
            counts[d3]--;
            if (counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {
                result++;
            }
            counts[d1]++;
            counts[d2]++;
            counts[d3]++;
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        counts = [0] * 10
        for d in digits:
            counts[d] += 1
        result = 0
        for i in range(100, 1000, 2):
            d1, d2, d3 = i // 100, (i // 10) % 10, i % 10
            counts[d1] -= 1
            counts[d2] -= 1
            counts[d3] -= 1
            if counts[d1] >= 0 and counts[d2] >= 0 and counts[d3] >= 0:
                result += 1
            counts[d1] += 1
            counts[d2] += 1
            counts[d3] += 1
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = [0] * 10
        for d in digits:
            counts[d] += 1
        result = 0
        for i in range(100, 1000, 2):
            d1, d2, d3 = i // 100, (i // 10) % 10, i % 10
            counts[d1] -= 1
            counts[d2] -= 1
            counts[d3] -= 1
            if counts[d1] >= 0 and counts[d2] >= 0 and counts[d3] >= 0:
                result += 1
            counts[d1] += 1
            counts[d2] += 1
            counts[d3] += 1
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int totalNumbers(int* digits, int digitsSize) {
    int counts[10] = {0};
    for (int i = 0; i < digitsSize; i++) {
        counts[digits[i]]++;
    }
    int result = 0;
    for (int i = 100; i <= 998; i += 2) {
        int d1 = i / 100;
        int d2 = (i / 10) % 10;
        int d3 = i % 10;
        counts[d1]--;
        counts[d2]--;
        counts[d3]--;
        if (counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {
            result++;
        }
        counts[d1]++;
        counts[d2]++;
        counts[d3]++;
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int TotalNumbers(int[] digits) {
        int[] counts = new int[10];
        foreach (int d in digits) {
            counts[d]++;
        }
        int result = 0;
        for (int i = 100; i <= 998; i += 2) {
            int d1 = i / 100;
            int d2 = (i / 10) % 10;
            int d3 = i % 10;
            counts[d1]--;
            counts[d2]--;
            counts[d3]--;
            if (counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {
                result++;
            }
            counts[d1]++;
            counts[d2]++;
            counts[d3]++;
        }
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
 * @return {number}
 */
var totalNumbers = function(digits) {
    const counts = new Array(10).fill(0);
    for (const d of digits) {
        counts[d]++;
    }
    let result = 0;
    for (let i = 100; i <= 998; i += 2) {
        const d1 = Math.floor(i / 100);
        const d2 = Math.floor((i / 10) % 10);
        const d3 = i % 10;
        counts[d1]--;
        counts[d2]--;
        counts[d3]--;
        if (counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0) {
            result++;
        }
        counts[d1]++;
        counts[d2]++;
        counts[d3]++;
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function totalNumbers(digits: number[]): number {
    const counts = new Array(10).fill(0);
    for (const d of digits) {
        counts[d]++;
    }
    let ans = 0;
    for (let i = 100; i <= 998; i += 2) {
        const freq = new Array(10).fill(0);
        let temp = i;
        while (temp > 0) {
            freq[temp % 10]++;
            temp = Math.floor(temp / 10);
        }
        let possible = true;
        for (let j = 0; j < 10; j++) {
            if (freq[j] > counts[j]) {
                possible = false;
                break;
            }
        }
        if (possible) {
            ans++;
        }
    }
    return ans;
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
     * @return Integer
     */
    function totalNumbers($digits) {
        $counts = array_fill(0, 10, 0);
        foreach ($digits as $d) {
            $counts[$d]++;
        }
        $ans = 0;
        for ($i = 100; $i <= 998; $i += 2) {
            $freq = array_fill(0, 10, 0);
            $temp = $i;
            while ($temp > 0) {
                $freq[($temp % 10)]++;
                $temp = (int)($temp / 10);
            }
            $possible = true;
            for ($j = 0; $j < 10; $j++) {
                if ($freq[$j] > $counts[$j]) {
                    $possible = false;
                    break;
                }
            }
            if ($possible) {
                $ans++;
            }
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func totalNumbers(_ digits: [Int]) -> Int {
        var counts = [Int](repeating: 0, count: 10)
        for d in digits {
            counts[d] += 1
        }
        var ans = 0
        for i in stride(from: 100, through: 998, by: 2) {
            var freq = [Int](repeating: 0, count: 10)
            var temp = i
            while temp > 0 {
                freq[temp % 10] += 1
                temp /= 10
            }
            var possible = true
            for j in 0..<10 {
                if freq[j] > counts[j] {
                    possible = false
                    break
                }
            }
            if possible {
                ans += 1
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun totalNumbers(digits: IntArray): Int {
        val counts = IntArray(10)
        for (d in digits) {
            counts[d]++
        }
        var ans = 0
        for (i in 100..998 step 2) {
            val freq = IntArray(10)
            var temp = i
            while (temp > 0) {
                freq[temp % 10]++
                temp /= 10
            }
            var possible = true
            for (j in 0..9) {
                if (freq[j] > counts[j]) {
                    possible = false
                    break
                }
            }
            if (possible) {
                ans++
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int totalNumbers(List<int> digits) {
    List<int> counts = List.filled(10, 0);
    for (int d in digits) {
      counts[d]++;
    }
    int ans = 0;
    for (int i = 100; i <= 998; i += 2) {
      List<int> freq = List.filled(10, 0);
      int temp = i;
      while (temp > 0) {
        freq[temp % 10]++;
        temp ~/= 10;
      }
      bool possible = true;
      for (int j = 0; j < 10; j++) {
        if (freq[j] > counts[j]) {
          possible = false;
          break;
        }
      }
      if (possible) {
        ans++;
      }
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func totalNumbers(digits []int) int {
    counts := make([]int, 10)
    for _, d := range digits {
        counts[d]++
    }
    ans := 0
    for i := 100; i <= 998; i += 2 {
        freq := make([]int, 10)
        temp := i
        for temp > 0 {
            freq[temp % 10]++
            temp /= 10
        }
        possible := true
        for j := 0; j < 10; j++ {
            if freq[j] > counts[j] {
                possible = false
                break
            }
        }
        if possible {
            ans++
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def total_numbers(digits)
  counts = Hash.new(0)
  digits.each { |d| counts[d] += 1 }
  (100..998).step(2).count do |i|
    d1 = i / 100
    d2 = (i / 10) % 10
    d3 = i % 10

    counts[d1] -= 1
    counts[d2] -= 1
    counts[d3] -= 1

    ok = counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0

    counts[d1] += 1
    counts[d2] += 1
    counts[d3] += 1

    ok
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def totalNumbers(digits: Array[Int]): Int = {
    val counts = new Array[Int](10)
    digits.foreach(d => counts(d) += 1)
    var result = 0
    for (i <- 100 to 998 by 2) {
      val d1 = i / 100
      val d2 = (i / 10) % 10
      val d3 = i % 10

      counts(d1) -= 1
      counts(d2) -= 1
      counts(d3) -= 1

      if (counts(d1) >= 0 && counts(d2) >= 0 && counts(d3) >= 0) {
        result += 1
      }

      counts(d1) += 1
      counts(d2) += 1
      counts(d3) += 1
    }
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
    pub fn total_numbers(digits: Vec<i32>) -> i32 {
        let mut counts = [0; 10];
        for &d in &digits {
            counts[d as usize] += 1;
        }
        let mut result = 0;
        for i in (100..1000).step_by(2) {
            let d1 = i / 100;
            let d2 = (i / 10) % 10;
            let d3 = i % 10;

            counts[d1] -= 1;
            counts[d2] -= 1;
            counts[d3] -= 1;

            if counts[d1] >= 0 && counts[d2] >= 0 && counts[d3] >= 0 {
                result += 1;
            }

            counts[d1] += 1;
            counts[d2] += 1;
            counts[d3] += 1;
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (total-numbers digits)
  (-> (listof exact-integer?) exact-integer?)
  (let ([counts (make-vector 10 0)])
    (for ([d digits])
      (vector-set! counts d (+ (vector-ref counts d) 1)))
    (let loop ([i 100] [res 0])
      (if (> i 998)
          res
          (let* ([d1 (quotient i 100)]
                 [d2 (remainder (quotient i 10) 10)]
                 [d3 (remainder i 10)])
            (vector-set! counts d1 (- (vector-ref counts d1) 1))
            (vector-set! counts d2 (- (vector-ref counts d2) 1))
            (vector-set! counts d3 (- (vector-ref counts d3) 1))
            (let ([ok (and (>= (vector-ref counts d1) 0)
                           (>= (vector-ref counts d2) 0)
                           (>= (vector-ref counts d3) 0))])
              (vector-set! counts d3 (+ (vector-ref counts d3) 1))
              (vector-set! counts d2 (+ (vector-ref counts d2) 1))
              (vector-set! counts d1 (+ (vector-ref counts d1) 1))
              (loop (+ i 2) (if ok (+ res 1) res))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec total_numbers(Digits :: [integer()]) -> integer().
total_numbers(Digits) ->
    Counts = lists:foldl(fun(D, Acc) -> 
        maps:put(D, maps:get(D, Acc, 0) + 1, Acc) 
    end, #{}, Digits),
    lists:foldl(fun(I, Acc) ->
        D1 = I div 100,
        D2 = (I div 10) rem 10,
        D3 = I rem 10,
        case can_form([D1, D2, D3], Counts) of
            true -> Acc + 1;
            false -> Acc
        end
    end, 0, lists:seq(100, 998, 2)).

can_form([], _) -> true;
can_form([H | T], Counts) ->
    case maps:get(H, Counts, 0) of
        0 -> false;
        N -> can_form(T, maps:put(H, N - 1, Counts))
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec total_numbers(digits :: [integer]) :: integer
  def total_numbers(digits) do
    counts = Enum.frequencies(digits)
    100..998
    |> Enum.filter(&(rem(&1, 2) == 0))
    |> Enum.count(fn i ->
      d1 = div(i, 100)
      d2 = rem(div(i, 10), 10)
      d3 = rem(i, 10)
      can_form?([d1, d2, d3], counts)
    end)
  end

  defp can_form?([], _), do: true
  defp can_form?([h | t], counts) do
    case Map.get(counts, h, 0) do
      0 -> false
      n -> can_form?(t, Map.put(counts, h, n - 1))
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the digits array. The algorithm performs a single pass over the input array to count digit frequencies, taking O(N) time, followed by a constant 450 iterations (from 100 to 998 in steps of 2) to check each candidate even number.
- **Space Complexity:** O(1) because the space used for the digit frequency array is fixed at 10 (digits 0-9), which does not grow with the size of the input array.
