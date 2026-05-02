---
layout: post
title: "Rotated Digits"
date: 2026-05-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/rotated-digits/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int rotatedDigits(int n) {\n        int count\
        \ = 0;\n        for (int i = 1; i <= n; ++i) {\n            int temp = i;\n\
        \            bool hasDiff = false;\n            bool isInvalid = false;\n  \
        \          while (temp > 0) {\n                int digit = temp % 10;\n    \
        \            if (digit == 3 || digit == 4 || digit == 7) {\n               \
        \     isInvalid = true;\n                    break;\n                }\n   \
        \             if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {\n\
        \                    hasDiff = true;\n                }\n                temp\
        \ /= 10;\n            }\n            if (!isInvalid && hasDiff) {\n        \
        \        count++;\n            }\n        }\n        return count;\n    }\n\
        };"
      java: "class Solution {\n    public int rotatedDigits(int n) {\n        int count\
        \ = 0;\n        for (int i = 1; i <= n; i++) {\n            int temp = i;\n\
        \            boolean hasDiff = false;\n            boolean isInvalid = false;\n\
        \            while (temp > 0) {\n                int digit = temp % 10;\n  \
        \              if (digit == 3 || digit == 4 || digit == 7) {\n             \
        \       isInvalid = true;\n                    break;\n                }\n \
        \               if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {\n\
        \                    hasDiff = true;\n                }\n                temp\
        \ /= 10;\n            }\n            if (!isInvalid && hasDiff) {\n        \
        \        count++;\n            }\n        }\n        return count;\n    }\n}"
      python: "class Solution(object):\n    def rotatedDigits(self, n):\n        \"\"\
        \"\n        :type n: int\n        :rtype: int\n        \"\"\"\n        count\
        \ = 0\n        for i in range(1, n + 1):\n            s = str(i)\n         \
        \   if '3' in s or '4' in s or '7' in s:\n                continue\n       \
        \     if '2' in s or '5' in s or '6' in s or '9' in s:\n                count\
        \ += 1\n        return count"
      python3: "class Solution:\n    def rotatedDigits(self, n: int) -> int:\n     \
        \   count = 0\n        for i in range(1, n + 1):\n            s = str(i)\n \
        \           if any(d in s for d in '347'):\n                continue\n     \
        \       if any(d in s for d in '2569'):\n                count += 1\n      \
        \  return count"
      c: "int rotatedDigits(int n) {\n    int total_count = 0;\n    for (int i = 1;\
        \ i <= n; i++) {\n        int temp = i;\n        int hasDiff = 0;\n        int\
        \ isInvalid = 0;\n        while (temp > 0) {\n            int d = temp % 10;\n\
        \            if (d == 3 || d == 4 || d == 7) {\n                isInvalid =\
        \ 1;\n                break;\n            }\n            if (d == 2 || d ==\
        \ 5 || d == 6 || d == 9) {\n                hasDiff = 1;\n            }\n  \
        \          temp /= 10;\n        }\n        if (!isInvalid && hasDiff) {\n  \
        \          total_count++;\n        }\n    }\n    return total_count;\n}"
      csharp: "public class Solution {\n    public int RotatedDigits(int n) {\n    \
        \    int count = 0;\n        for (int i = 1; i <= n; i++) {\n            int\
        \ temp = i;\n            bool hasDiff = false;\n            bool isValid = true;\n\
        \            while (temp > 0) {\n                int d = temp % 10;\n      \
        \          if (d == 3 || d == 4 || d == 7) {\n                    isValid =\
        \ false;\n                    break;\n                }\n                if\
        \ (d == 2 || d == 5 || d == 6 || d == 9) {\n                    hasDiff = true;\n\
        \                }\n                temp /= 10;\n            }\n           \
        \ if (isValid && hasDiff) {\n                count++;\n            }\n     \
        \   }\n        return count;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar rotatedDigits\
        \ = function(n) {\n    let count = 0;\n    for (let i = 1; i <= n; i++) {\n\
        \        let temp = i;\n        let hasDiff = false;\n        let isValid =\
        \ true;\n        while (temp > 0) {\n            let d = temp % 10;\n      \
        \      if (d === 3 || d === 4 || d === 7) {\n                isValid = false;\n\
        \                break;\n            }\n            if (d === 2 || d === 5 ||\
        \ d === 6 || d === 9) {\n                hasDiff = true;\n            }\n  \
        \          temp = Math.floor(temp / 10);\n        }\n        if (isValid &&\
        \ hasDiff) {\n            count++;\n        }\n    }\n    return count;\n};"
      typescript: "function rotatedDigits(n: number): number {\n    let count = 0;\n\
        \    for (let i = 1; i <= n; i++) {\n        let temp = i;\n        let hasDiff\
        \ = false;\n        let isValid = true;\n        while (temp > 0) {\n      \
        \      let d = temp % 10;\n            if (d === 3 || d === 4 || d === 7) {\n\
        \                isValid = false;\n                break;\n            }\n \
        \           if (d === 2 || d === 5 || d === 6 || d === 9) {\n              \
        \  hasDiff = true;\n            }\n            temp = Math.floor(temp / 10);\n\
        \        }\n        if (isValid && hasDiff) {\n            count++;\n      \
        \  }\n    }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function rotatedDigits($n) {\n        $count = 0;\n        for\
        \ ($i = 1; $i <= $n; $i++) {\n            $temp = $i;\n            $hasDiff\
        \ = false;\n            $isValid = true;\n            while ($temp > 0) {\n\
        \                $d = $temp % 10;\n                if ($d == 3 || $d == 4 ||\
        \ $d == 7) {\n                    $isValid = false;\n                    break;\n\
        \                }\n                if ($d == 2 || $d == 5 || $d == 6 || $d\
        \ == 9) {\n                    $hasDiff = true;\n                }\n       \
        \         $temp = (int)($temp / 10);\n            }\n            if ($isValid\
        \ && $hasDiff) {\n                $count++;\n            }\n        }\n    \
        \    return $count;\n    }\n}"
      swift: "class Solution {\n    func rotatedDigits(_ n: Int) -> Int {\n        var\
        \ count = 0\n        for i in 1...n {\n            var temp = i\n          \
        \  var hasDiff = false\n            var isValid = true\n            while temp\
        \ > 0 {\n                let d = temp % 10\n                if d == 3 || d ==\
        \ 4 || d == 7 {\n                    isValid = false\n                    break\n\
        \                }\n                if d == 2 || d == 5 || d == 6 || d == 9\
        \ {\n                    hasDiff = true\n                }\n               \
        \ temp /= 10\n            }\n            if isValid && hasDiff {\n         \
        \       count += 1\n            }\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun rotatedDigits(n: Int): Int {\n        var count\
        \ = 0\n        for (i in 1..n) {\n            if (isValid(i)) {\n          \
        \      count++\n            }\n        }\n        return count\n    }\n\n  \
        \  private fun isValid(n: Int): Boolean {\n        var num = n\n        var\
        \ changed = false\n        while (num > 0) {\n            val digit = num %\
        \ 10\n            if (digit == 3 || digit == 4 || digit == 7) return false\n\
        \            if (digit == 2 || digit == 5 || digit == 6 || digit == 9) changed\
        \ = true\n            num /= 10\n        }\n        return changed\n    }\n}"
      dart: "class Solution {\n  int rotatedDigits(int n) {\n    int count = 0;\n  \
        \  for (int i = 1; i <= n; i++) {\n      if (isValid(i)) {\n        count++;\n\
        \      }\n    }\n    return count;\n  }\n\n  bool isValid(int n) {\n    bool\
        \ changed = false;\n    int num = n;\n    while (num > 0) {\n      int digit\
        \ = num % 10;\n      if (digit == 3 || digit == 4 || digit == 7) return false;\n\
        \      if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {\n       \
        \ changed = true;\n      }\n      num ~/= 10;\n    }\n    return changed;\n\
        \  }\n}"
      go: "func rotatedDigits(n int) int {\n    count := 0\n    for i := 1; i <= n;\
        \ i++ {\n        if isValid(i) {\n            count++\n        }\n    }\n  \
        \  return count\n}\n\nfunc isValid(n int) bool {\n    changed := false\n   \
        \ num := n\n    for num > 0 {\n        digit := num % 10\n        if digit ==\
        \ 3 || digit == 4 || digit == 7 {\n            return false\n        }\n   \
        \     if digit == 2 || digit == 5 || digit == 6 || digit == 9 {\n          \
        \  changed = true\n        }\n        num /= 10\n    }\n    return changed\n\
        }"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef rotated_digits(n)\n    count\
        \ = 0\n    (1..n).each do |i|\n        count += 1 if is_valid?(i)\n    end\n\
        \    count\nend\n\ndef is_valid?(n)\n    changed = false\n    num = n\n    while\
        \ num > 0\n        digit = num % 10\n        if [3, 4, 7].include?(digit)\n\
        \            return false\n        end\n        if [2, 5, 6, 9].include?(digit)\n\
        \            changed = true\n        end\n        num /= 10\n    end\n    changed\n\
        end"
      scala: "object Solution {\n    def rotatedDigits(n: Int): Int = {\n        var\
        \ count = 0\n        for (i <- 1 to n) {\n            if (isValid(i)) {\n  \
        \              count += 1\n            }\n        }\n        count\n    }\n\n\
        \    def isValid(n: Int): Boolean = {\n        var num = n\n        var changed\
        \ = false\n        while (num > 0) {\n            val digit = num % 10\n   \
        \         if (digit == 3 || digit == 4 || digit == 7) return false\n       \
        \     if (digit == 2 || digit == 5 || digit == 6 || digit == 9) changed = true\n\
        \            num /= 10\n        }\n        changed\n    }\n}"
      rust: "impl Solution {\n    pub fn rotated_digits(n: i32) -> i32 {\n        let\
        \ mut count = 0;\n        for i in 1..=n {\n            let mut num = i;\n \
        \           let mut has_rotated_digit = false;\n            let mut is_valid\
        \ = true;\n            while num > 0 {\n                let digit = num % 10;\n\
        \                match digit {\n                    2 | 5 | 6 | 9 => has_rotated_digit\
        \ = true,\n                    3 | 4 | 7 => {\n                        is_valid\
        \ = false;\n                        break;\n                    }\n        \
        \            _ => {}\n                }\n                num /= 10;\n      \
        \      }\n            if is_valid && has_rotated_digit {\n                count\
        \ += 1;\n            }\n        }\n        count\n    }\n}"
      racket: "(define/contract (rotated-digits n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let ([is-good? (lambda (num)\n                    (let loop ([val num]\n\
        \                               [changed #f])\n                      (if (=\
        \ val 0)\n                          changed\n                          (let\
        \ ([digit (remainder val 10)])\n                            (cond\n        \
        \                      [(member digit '(3 4 7)) #f]\n                      \
        \        [(member digit '(2 5 6 9)) (loop (quotient val 10) #t)]\n         \
        \                     [else (loop (quotient val 10) changed)])))))])\n    (count\
        \ is-good? (range 1 (+ n 1)))))"
      erlang: "-spec rotated_digits(N :: integer()) -> integer().\nrotated_digits(N)\
        \ ->\n    rotated_digits_acc(1, N, 0).\n\nrotated_digits_acc(I, N, Acc) when\
        \ I > N -> Acc;\nrotated_digits_acc(I, N, Acc) ->\n    case check_num(I, false)\
        \ of\n        true -> rotated_digits_acc(I + 1, N, Acc + 1);\n        false\
        \ -> rotated_digits_acc(I + 1, N, Acc)\n    end.\n\ncheck_num(0, Changed) ->\
        \ Changed;\ncheck_num(I, Changed) ->\n    Digit = I rem 10,\n    case Digit\
        \ of\n        3 -> false;\n        4 -> false;\n        7 -> false;\n      \
        \  2 -> check_num(I div 10, true);\n        5 -> check_num(I div 10, true);\n\
        \        6 -> check_num(I div 10, true);\n        9 -> check_num(I div 10, true);\n\
        \        _ -> check_num(I div 10, Changed)\n    end."
      elixir: "defmodule Solution do\n  @spec rotated_digits(n :: integer) :: integer\n\
        \  def rotated_digits(n) do\n    1..n\n    |> Enum.count(&is_good?(&1, false))\n\
        \  end\n\n  defp is_good?(0, changed), do: changed\n  defp is_good?(num, changed)\
        \ do\n    case rem(num, 10) do\n      d when d in [3, 4, 7] -> false\n     \
        \ d when d in [2, 5, 6, 9] -> is_good?(div(num, 10), true)\n      _ -> is_good?(div(num,\
        \ 10), changed)\n    end\n  end\nend"
    approach: 'A number is considered ''good'' if all its digits are rotatable and at
      least one of those digits changes the value of the number upon rotation. The rotatable
      digits that remain the same are 0, 1, and 8, while those that change are 2, 5,
      6, and 9. If a number contains any of the digits 3, 4, or 7, it is invalid because
      those digits do not rotate to any valid digit. Therefore, the algorithm checks
      each integer from 1 to n to ensure it contains no invalid digits and contains
      at least one digit from the set {2, 5, 6, 9}.


      For each number in the range [1, n], we can iterate through its digits using the
      modulo and division operators. We maintain two boolean flags: one to track if
      the number contains any invalid digits (3, 4, 7) and another to track if it contains
      at least one ''changing'' digit (2, 5, 6, 9). If the number consists entirely
      of valid digits and has at least one changing digit, it satisfies the criteria
      for being a good integer. Summing these instances provides the final count.'
    time_complexity: O(n log n) because we iterate through n integers, and for each
      integer, we examine each of its digits. The number of digits in an integer x is
      approximately log10(x), so the total number of operations is proportional to n
      log n.
    space_complexity: O(1) because we only use a constant amount of extra space for
      counters and boolean flags, regardless of the input size n. If strings are used
      to process digits, the space complexity would be O(log n) for the string representation.
    elapsed_time: 78.00797986984253
    model: gemini-3-flash-preview
    generated_at: '2026-05-02 02:04:25 '
---

## Problem #788: Rotated Digits

**Difficulty:** Medium

**Topics:** Math, Dynamic Programming

## Problem Description

<p>An integer <code>x</code> is a <strong>good</strong> if after rotating each digit individually by 180 degrees, we get a valid number that is different from <code>x</code>. Each digit must be rotated - we cannot choose to leave it alone.</p>

<p>A number is valid if each digit remains a digit after rotation. For example:</p>

<ul>
	<li><code>0</code>, <code>1</code>, and <code>8</code> rotate to themselves,</li>
	<li><code>2</code> and <code>5</code> rotate to each other (in this case they are rotated in a different direction, in other words, <code>2</code> or <code>5</code> gets mirrored),</li>
	<li><code>6</code> and <code>9</code> rotate to each other, and</li>
	<li>the rest of the numbers do not rotate to any other number and become invalid.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>the number of <strong>good</strong> integers in the range </em><code>[1, n]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

A number is considered 'good' if all its digits are rotatable and at least one of those digits changes the value of the number upon rotation. The rotatable digits that remain the same are 0, 1, and 8, while those that change are 2, 5, 6, and 9. If a number contains any of the digits 3, 4, or 7, it is invalid because those digits do not rotate to any valid digit. Therefore, the algorithm checks each integer from 1 to n to ensure it contains no invalid digits and contains at least one digit from the set {2, 5, 6, 9}.

For each number in the range [1, n], we can iterate through its digits using the modulo and division operators. We maintain two boolean flags: one to track if the number contains any invalid digits (3, 4, 7) and another to track if it contains at least one 'changing' digit (2, 5, 6, 9). If the number consists entirely of valid digits and has at least one changing digit, it satisfies the criteria for being a good integer. Summing these instances provides the final count.

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
    int rotatedDigits(int n) {
        int count = 0;
        for (int i = 1; i <= n; ++i) {
            int temp = i;
            bool hasDiff = false;
            bool isInvalid = false;
            while (temp > 0) {
                int digit = temp % 10;
                if (digit == 3 || digit == 4 || digit == 7) {
                    isInvalid = true;
                    break;
                }
                if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
                    hasDiff = true;
                }
                temp /= 10;
            }
            if (!isInvalid && hasDiff) {
                count++;
            }
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
    public int rotatedDigits(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            int temp = i;
            boolean hasDiff = false;
            boolean isInvalid = false;
            while (temp > 0) {
                int digit = temp % 10;
                if (digit == 3 || digit == 4 || digit == 7) {
                    isInvalid = true;
                    break;
                }
                if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
                    hasDiff = true;
                }
                temp /= 10;
            }
            if (!isInvalid && hasDiff) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if '3' in s or '4' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if any(d in s for d in '347'):
                continue
            if any(d in s for d in '2569'):
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int rotatedDigits(int n) {
    int total_count = 0;
    for (int i = 1; i <= n; i++) {
        int temp = i;
        int hasDiff = 0;
        int isInvalid = 0;
        while (temp > 0) {
            int d = temp % 10;
            if (d == 3 || d == 4 || d == 7) {
                isInvalid = 1;
                break;
            }
            if (d == 2 || d == 5 || d == 6 || d == 9) {
                hasDiff = 1;
            }
            temp /= 10;
        }
        if (!isInvalid && hasDiff) {
            total_count++;
        }
    }
    return total_count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int RotatedDigits(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            int temp = i;
            bool hasDiff = false;
            bool isValid = true;
            while (temp > 0) {
                int d = temp % 10;
                if (d == 3 || d == 4 || d == 7) {
                    isValid = false;
                    break;
                }
                if (d == 2 || d == 5 || d == 6 || d == 9) {
                    hasDiff = true;
                }
                temp /= 10;
            }
            if (isValid && hasDiff) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @return {number}
 */
var rotatedDigits = function(n) {
    let count = 0;
    for (let i = 1; i <= n; i++) {
        let temp = i;
        let hasDiff = false;
        let isValid = true;
        while (temp > 0) {
            let d = temp % 10;
            if (d === 3 || d === 4 || d === 7) {
                isValid = false;
                break;
            }
            if (d === 2 || d === 5 || d === 6 || d === 9) {
                hasDiff = true;
            }
            temp = Math.floor(temp / 10);
        }
        if (isValid && hasDiff) {
            count++;
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function rotatedDigits(n: number): number {
    let count = 0;
    for (let i = 1; i <= n; i++) {
        let temp = i;
        let hasDiff = false;
        let isValid = true;
        while (temp > 0) {
            let d = temp % 10;
            if (d === 3 || d === 4 || d === 7) {
                isValid = false;
                break;
            }
            if (d === 2 || d === 5 || d === 6 || d === 9) {
                hasDiff = true;
            }
            temp = Math.floor(temp / 10);
        }
        if (isValid && hasDiff) {
            count++;
        }
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

    /**
     * @param Integer $n
     * @return Integer
     */
    function rotatedDigits($n) {
        $count = 0;
        for ($i = 1; $i <= $n; $i++) {
            $temp = $i;
            $hasDiff = false;
            $isValid = true;
            while ($temp > 0) {
                $d = $temp % 10;
                if ($d == 3 || $d == 4 || $d == 7) {
                    $isValid = false;
                    break;
                }
                if ($d == 2 || $d == 5 || $d == 6 || $d == 9) {
                    $hasDiff = true;
                }
                $temp = (int)($temp / 10);
            }
            if ($isValid && $hasDiff) {
                $count++;
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func rotatedDigits(_ n: Int) -> Int {
        var count = 0
        for i in 1...n {
            var temp = i
            var hasDiff = false
            var isValid = true
            while temp > 0 {
                let d = temp % 10
                if d == 3 || d == 4 || d == 7 {
                    isValid = false
                    break
                }
                if d == 2 || d == 5 || d == 6 || d == 9 {
                    hasDiff = true
                }
                temp /= 10
            }
            if isValid && hasDiff {
                count += 1
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun rotatedDigits(n: Int): Int {
        var count = 0
        for (i in 1..n) {
            if (isValid(i)) {
                count++
            }
        }
        return count
    }

    private fun isValid(n: Int): Boolean {
        var num = n
        var changed = false
        while (num > 0) {
            val digit = num % 10
            if (digit == 3 || digit == 4 || digit == 7) return false
            if (digit == 2 || digit == 5 || digit == 6 || digit == 9) changed = true
            num /= 10
        }
        return changed
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int rotatedDigits(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
      if (isValid(i)) {
        count++;
      }
    }
    return count;
  }

  bool isValid(int n) {
    bool changed = false;
    int num = n;
    while (num > 0) {
      int digit = num % 10;
      if (digit == 3 || digit == 4 || digit == 7) return false;
      if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
        changed = true;
      }
      num ~/= 10;
    }
    return changed;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func rotatedDigits(n int) int {
    count := 0
    for i := 1; i <= n; i++ {
        if isValid(i) {
            count++
        }
    }
    return count
}

func isValid(n int) bool {
    changed := false
    num := n
    for num > 0 {
        digit := num % 10
        if digit == 3 || digit == 4 || digit == 7 {
            return false
        }
        if digit == 2 || digit == 5 || digit == 6 || digit == 9 {
            changed = true
        }
        num /= 10
    }
    return changed
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def rotated_digits(n)
    count = 0
    (1..n).each do |i|
        count += 1 if is_valid?(i)
    end
    count
end

def is_valid?(n)
    changed = false
    num = n
    while num > 0
        digit = num % 10
        if [3, 4, 7].include?(digit)
            return false
        end
        if [2, 5, 6, 9].include?(digit)
            changed = true
        end
        num /= 10
    end
    changed
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def rotatedDigits(n: Int): Int = {
        var count = 0
        for (i <- 1 to n) {
            if (isValid(i)) {
                count += 1
            }
        }
        count
    }

    def isValid(n: Int): Boolean = {
        var num = n
        var changed = false
        while (num > 0) {
            val digit = num % 10
            if (digit == 3 || digit == 4 || digit == 7) return false
            if (digit == 2 || digit == 5 || digit == 6 || digit == 9) changed = true
            num /= 10
        }
        changed
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn rotated_digits(n: i32) -> i32 {
        let mut count = 0;
        for i in 1..=n {
            let mut num = i;
            let mut has_rotated_digit = false;
            let mut is_valid = true;
            while num > 0 {
                let digit = num % 10;
                match digit {
                    2 | 5 | 6 | 9 => has_rotated_digit = true,
                    3 | 4 | 7 => {
                        is_valid = false;
                        break;
                    }
                    _ => {}
                }
                num /= 10;
            }
            if is_valid && has_rotated_digit {
                count += 1;
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (rotated-digits n)
  (-> exact-integer? exact-integer?)
  (let ([is-good? (lambda (num)
                    (let loop ([val num]
                               [changed #f])
                      (if (= val 0)
                          changed
                          (let ([digit (remainder val 10)])
                            (cond
                              [(member digit '(3 4 7)) #f]
                              [(member digit '(2 5 6 9)) (loop (quotient val 10) #t)]
                              [else (loop (quotient val 10) changed)])))))])
    (count is-good? (range 1 (+ n 1)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec rotated_digits(N :: integer()) -> integer().
rotated_digits(N) ->
    rotated_digits_acc(1, N, 0).

rotated_digits_acc(I, N, Acc) when I > N -> Acc;
rotated_digits_acc(I, N, Acc) ->
    case check_num(I, false) of
        true -> rotated_digits_acc(I + 1, N, Acc + 1);
        false -> rotated_digits_acc(I + 1, N, Acc)
    end.

check_num(0, Changed) -> Changed;
check_num(I, Changed) ->
    Digit = I rem 10,
    case Digit of
        3 -> false;
        4 -> false;
        7 -> false;
        2 -> check_num(I div 10, true);
        5 -> check_num(I div 10, true);
        6 -> check_num(I div 10, true);
        9 -> check_num(I div 10, true);
        _ -> check_num(I div 10, Changed)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec rotated_digits(n :: integer) :: integer
  def rotated_digits(n) do
    1..n
    |> Enum.count(&is_good?(&1, false))
  end

  defp is_good?(0, changed), do: changed
  defp is_good?(num, changed) do
    case rem(num, 10) do
      d when d in [3, 4, 7] -> false
      d when d in [2, 5, 6, 9] -> is_good?(div(num, 10), true)
      _ -> is_good?(div(num, 10), changed)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) because we iterate through n integers, and for each integer, we examine each of its digits. The number of digits in an integer x is approximately log10(x), so the total number of operations is proportional to n log n.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for counters and boolean flags, regardless of the input size n. If strings are used to process digits, the space complexity would be O(log n) for the string representation.
