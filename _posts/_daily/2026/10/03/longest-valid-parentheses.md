---
layout: post
title: "Longest Valid Parentheses"
date: 2026-10-03 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Dynamic Programming", "Stack", "Bracket Sequences"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/longest-valid-parentheses/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int longestValidParentheses(string s) {\n\
        \        int left = 0, right = 0, maxLength = 0;\n        int n = s.length();\n\
        \        for (int i = 0; i < n; i++) {\n            if (s[i] == '(') {\n   \
        \             left++;\n            } else {\n                right++;\n    \
        \        }\n            if (left == right) {\n                maxLength = max(maxLength,\
        \ 2 * right);\n            } else if (right > left) {\n                left\
        \ = right = 0;\n            }\n        }\n        left = right = 0;\n      \
        \  for (int i = n - 1; i >= 0; i--) {\n            if (s[i] == '(') {\n    \
        \            left++;\n            } else {\n                right++;\n     \
        \       }\n            if (left == right) {\n                maxLength = max(maxLength,\
        \ 2 * left);\n            } else if (left > right) {\n                left =\
        \ right = 0;\n            }\n        }\n        return maxLength;\n    }\n};"
      java: "class Solution {\n    public int longestValidParentheses(String s) {\n\
        \        int left = 0, right = 0, maxLength = 0;\n        for (int i = 0; i\
        \ < s.length(); i++) {\n            if (s.charAt(i) == '(') {\n            \
        \    left++;\n            } else {\n                right++;\n            }\n\
        \            if (left == right) {\n                maxLength = Math.max(maxLength,\
        \ 2 * right);\n            } else if (right > left) {\n                left\
        \ = right = 0;\n            }\n        }\n        left = right = 0;\n      \
        \  for (int i = s.length() - 1; i >= 0; i--) {\n            if (s.charAt(i)\
        \ == '(') {\n                left++;\n            } else {\n               \
        \ right++;\n            }\n            if (left == right) {\n              \
        \  maxLength = Math.max(maxLength, 2 * left);\n            } else if (left >\
        \ right) {\n                left = right = 0;\n            }\n        }\n  \
        \      return maxLength;\n    }\n}"
      python: "class Solution(object):\n    def longestValidParentheses(self, s):\n\
        \        \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n\
        \        left, right, maxLength = 0, 0, 0\n        for i in range(len(s)):\n\
        \            if s[i] == '(':\n                left += 1\n            else:\n\
        \                right += 1\n            if left == right:\n               \
        \ maxLength = max(maxLength, 2 * right)\n            elif right > left:\n  \
        \              left = right = 0\n\n        left = right = 0\n        for i in\
        \ range(len(s) - 1, -1, -1):\n            if s[i] == '(':\n                left\
        \ += 1\n            else:\n                right += 1\n            if left ==\
        \ right:\n                maxLength = max(maxLength, 2 * left)\n           \
        \ elif left > right:\n                left = right = 0\n\n        return maxLength"
      python3: "class Solution:\n    def longestValidParentheses(self, s: str) -> int:\n\
        \        left = right = max_len = 0\n        for char in s:\n            if\
        \ char == '(':\n                left += 1\n            else:\n             \
        \   right += 1\n            if left == right:\n                max_len = max(max_len,\
        \ 2 * right)\n            elif right > left:\n                left = right =\
        \ 0\n\n        left = right = 0\n        for i in range(len(s) - 1, -1, -1):\n\
        \            if s[i] == '(':\n                left += 1\n            else:\n\
        \                right += 1\n            if left == right:\n               \
        \ max_len = max(max_len, 2 * left)\n            elif left > right:\n       \
        \         left = right = 0\n\n        return max_len"
      c: "int longestValidParentheses(char* s) {\n    int n = 0;\n    while (s[n] !=\
        \ '\\0') n++;\n    int left = 0, right = 0, max_len = 0;\n\n    for (int i =\
        \ 0; i < n; i++) {\n        if (s[i] == '(') {\n            left++;\n      \
        \  } else {\n            right++;\n        }\n        if (left == right) {\n\
        \            if (2 * right > max_len) max_len = 2 * right;\n        } else if\
        \ (right > left) {\n            left = 0;\n            right = 0;\n        }\n\
        \    }\n\n    left = 0;\n    right = 0;\n    for (int i = n - 1; i >= 0; i--)\
        \ {\n        if (s[i] == '(') {\n            left++;\n        } else {\n   \
        \         right++;\n        }\n        if (left == right) {\n            if\
        \ (2 * left > max_len) max_len = 2 * left;\n        } else if (left > right)\
        \ {\n            left = 0;\n            right = 0;\n        }\n    }\n\n   \
        \ return max_len;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int LongestValidParentheses(string\
        \ s) {\n        int left = 0, right = 0, maxLen = 0;\n\n        for (int i =\
        \ 0; i < s.Length; i++) {\n            if (s[i] == '(') {\n                left++;\n\
        \            } else {\n                right++;\n            }\n           \
        \ if (left == right) {\n                maxLen = Math.Max(maxLen, 2 * right);\n\
        \            } else if (right > left) {\n                left = 0;\n       \
        \         right = 0;\n            }\n        }\n\n        left = 0;\n      \
        \  right = 0;\n        for (int i = s.Length - 1; i >= 0; i--) {\n         \
        \   if (s[i] == '(') {\n                left++;\n            } else {\n    \
        \            right++;\n            }\n            if (left == right) {\n   \
        \             maxLen = Math.Max(maxLen, 2 * left);\n            } else if (left\
        \ > right) {\n                left = 0;\n                right = 0;\n      \
        \      }\n        }\n\n        return maxLen;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar longestValidParentheses\
        \ = function(s) {\n    let left = 0, right = 0, maxLen = 0;\n\n    for (let\
        \ i = 0; i < s.length; i++) {\n        if (s[i] === '(') {\n            left++;\n\
        \        } else {\n            right++;\n        }\n        if (left === right)\
        \ {\n            maxLen = Math.max(maxLen, 2 * right);\n        } else if (right\
        \ > left) {\n            left = 0;\n            right = 0;\n        }\n    }\n\
        \n    left = 0;\n    right = 0;\n    for (let i = s.length - 1; i >= 0; i--)\
        \ {\n        if (s[i] === '(') {\n            left++;\n        } else {\n  \
        \          right++;\n        }\n        if (left === right) {\n            maxLen\
        \ = Math.max(maxLen, 2 * left);\n        } else if (left > right) {\n      \
        \      left = 0;\n            right = 0;\n        }\n    }\n\n    return maxLen;\n\
        };"
      typescript: "function longestValidParentheses(s: string): number {\n    let maxLen\
        \ = 0;\n    const stack: number[] = [-1];\n    for (let i = 0; i < s.length;\
        \ i++) {\n        if (s[i] === '(') {\n            stack.push(i);\n        }\
        \ else {\n            stack.pop();\n            if (stack.length === 0) {\n\
        \                stack.push(i);\n            } else {\n                maxLen\
        \ = Math.max(maxLen, i - stack[stack.length - 1]);\n            }\n        }\n\
        \    }\n    return maxLen;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function longestValidParentheses($s) {\n        $maxLen = 0;\n\
        \        $stack = [-1];\n        $n = strlen($s);\n        for ($i = 0; $i <\
        \ $n; $i++) {\n            if ($s[$i] === '(') {\n                array_push($stack,\
        \ $i);\n            } else {\n                array_pop($stack);\n         \
        \       if (empty($stack)) {\n                    array_push($stack, $i);\n\
        \                } else {\n                    $currentLen = $i - $stack[count($stack)\
        \ - 1];\n                    if ($currentLen > $maxLen) {\n                \
        \        $maxLen = $currentLen;\n                    }\n                }\n\
        \            }\n        }\n        return $maxLen;\n    }\n}"
      swift: "class Solution {\n    func longestValidParentheses(_ s: String) -> Int\
        \ {\n        var maxLen = 0\n        var stack: [Int] = [-1]\n        let chars\
        \ = Array(s)\n        for i in 0..<chars.count {\n            if chars[i] ==\
        \ \"(\" {\n                stack.append(i)\n            } else {\n         \
        \       stack.removeLast()\n                if stack.isEmpty {\n           \
        \         stack.append(i)\n                } else {\n                    maxLen\
        \ = max(maxLen, i - stack.last!)\n                }\n            }\n       \
        \ }\n        return maxLen\n    }\n}"
      kotlin: "class Solution {\n    fun longestValidParentheses(s: String): Int {\n\
        \        var maxLen = 0\n        val stack = java.util.ArrayDeque<Int>()\n \
        \       stack.push(-1)\n        for (i in s.indices) {\n            if (s[i]\
        \ == '(') {\n                stack.push(i)\n            } else {\n         \
        \       stack.pop()\n                if (stack.isEmpty()) {\n              \
        \      stack.push(i)\n                } else {\n                    maxLen =\
        \ kotlin.math.max(maxLen, i - stack.peek())\n                }\n           \
        \ }\n        }\n        return maxLen\n    }\n}"
      dart: "class Solution {\n  int longestValidParentheses(String s) {\n    int maxLen\
        \ = 0;\n    List<int> stack = [-1];\n    for (int i = 0; i < s.length; i++)\
        \ {\n      if (s[i] == '(') {\n        stack.add(i);\n      } else {\n     \
        \   stack.removeLast();\n        if (stack.isEmpty) {\n          stack.add(i);\n\
        \        } else {\n          int currentLen = i - stack.last;\n          if\
        \ (currentLen > maxLen) {\n            maxLen = currentLen;\n          }\n \
        \       }\n      }\n    }\n    return maxLen;\n  }\n}"
      go: "func longestValidParentheses(s string) int {\n    maxLen := 0\n    stack\
        \ := []int{-1}\n    for i := 0; i < len(s); i++ {\n        if s[i] == '(' {\n\
        \            stack = append(stack, i)\n        } else {\n            stack =\
        \ stack[:len(stack)-1]\n            if len(stack) == 0 {\n                stack\
        \ = append(stack, i)\n            } else {\n                currentLen := i\
        \ - stack[len(stack)-1]\n                if currentLen > maxLen {\n        \
        \            maxLen = currentLen\n                }\n            }\n       \
        \ }\n    }\n    return maxLen\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef longest_valid_parentheses(s)\n\
        \  max_len = 0\n  stack = [-1]\n  s.each_char.with_index do |char, i|\n    if\
        \ char == '('\n      stack.push(i)\n    else\n      stack.pop\n      if stack.empty?\n\
        \        stack.push(i)\n      else\n        current_len = i - stack.last\n \
        \       max_len = current_len if current_len > max_len\n      end\n    end\n\
        \  end\n  max_len\nend"
      scala: "object Solution {\n  def longestValidParentheses(s: String): Int = {\n\
        \    var maxLen = 0\n    var stack = List[Int](-1)\n    for (i <- 0 until s.length)\
        \ {\n      if (s(i) == '(') {\n        stack = i :: stack\n      } else {\n\
        \        stack = stack.tail\n        if (stack.isEmpty) {\n          stack =\
        \ i :: Nil\n        } else {\n          val currentLen = i - stack.head\n  \
        \        if (currentLen > maxLen) {\n            maxLen = currentLen\n     \
        \     }\n        }\n      }\n    }\n    maxLen\n  }\n}"
      rust: "impl Solution {\n    pub fn longest_valid_parentheses(s: String) -> i32\
        \ {\n        let s_bytes = s.as_bytes();\n        let mut left: usize = 0;\n\
        \        let mut right: usize = 0;\n        let mut max_len: usize = 0;\n\n\
        \        for &b in s_bytes.iter() {\n            if b == b'(' {\n          \
        \      left += 1;\n            } else {\n                right += 1;\n     \
        \       }\n            if left == right {\n                max_len = max_len.max(2\
        \ * right);\n            } else if right > left {\n                left = 0;\n\
        \                right = 0;\n            }\n        }\n\n        left = 0;\n\
        \        right = 0;\n        for &b in s_bytes.iter().rev() {\n            if\
        \ b == b'(' {\n                left += 1;\n            } else {\n          \
        \      right += 1;\n            }\n            if left == right {\n        \
        \        max_len = max_len.max(2 * left);\n            } else if left > right\
        \ {\n                left = 0;\n                right = 0;\n            }\n\
        \        }\n\n        max_len as i32\n    }\n}"
      racket: "(define/contract (longest-valid-parentheses s)\n  (-> string? exact-integer?)\n\
        \  (let ([n (string-length s)])\n    (let* ([pass1 (let loop ([i 0] [l 0] [r\
        \ 0] [m 0])\n                    (if (< i n)\n                        (let*\
        \ ([c (string-ref s i)]\n                               [nl (if (char=? c #\\\
        () (+ l 1) l)]\n                               [nr (if (char=? c #\\)) (+ r\
        \ 1) r)])\n                          (cond\n                            [(=\
        \ nl nr) (loop (+ i 1) nl nr (max m (* 2 nr)))]\n                          \
        \  [(> nr nl) (loop (+ i 1) 0 0 m)]\n                            [else (loop\
        \ (+ i 1) nl nr m)]))\n                        m))]\n           [pass2 (let\
        \ loop ([i (- n 1)] [l 0] [r 0] [m 0])\n                    (if (>= i 0)\n \
        \                       (let* ([c (string-ref s i)]\n                      \
        \         [nl (if (char=? c #\\() (+ l 1) l)]\n                            \
        \   [nr (if (char=? c #\\)) (+ r 1) r)])\n                          (cond\n\
        \                            [(= nl nr) (loop (- i 1) nl nr (max m (* 2 nl)))]\n\
        \                            [(> nl nr) (loop (- i 1) 0 0 m)]\n            \
        \                [else (loop (- i 1) nl nr m)]))\n                        m))])\n\
        \      (max pass1 pass2))))"
      erlang: "-spec longest_valid_parentheses(S :: unicode:unicode_binary()) -> integer().\n\
        longest_valid_parentheses(S) ->\n  List = binary_to_list(S),\n  Max1 = pass_lr(List,\
        \ 0, 0, 0),\n  Max2 = pass_rl(lists:reverse(List), 0, 0, 0),\n  erlang:max(Max1,\
        \ Max2).\n\npass_lr([], _, _, Max) -> Max;\npass_lr([H|T], L, R, Max) ->\n \
        \ {NL, NR} = if H == $( -> {L + 1, R}; true -> {L, R + 1} end,\n  if\n    NL\
        \ == NR -> pass_lr(T, NL, NR, erlang:max(Max, 2 * NR));\n    NR > NL -> pass_lr(T,\
        \ 0, 0, Max);\n    true -> pass_lr(T, NL, NR, Max)\n  end.\n\npass_rl([], _,\
        \ _, Max) -> Max;\npass_rl([H|T], L, R, Max) ->\n  {NL, NR} = if H == $( ->\
        \ {L + 1, R}; true -> {L, R + 1} end,\n  if\n    NL == NR -> pass_rl(T, NL,\
        \ NR, erlang:max(Max, 2 * NL));\n    NL > NR -> pass_rl(T, 0, 0, Max);\n   \
        \ true -> pass_rl(T, NL, NR, Max)\n  end."
      elixir: "defmodule Solution do\n  @spec longest_valid_parentheses(s :: String.t)\
        \ :: integer\n  def longest_valid_parentheses(s) do\n    chars = String.to_charlist(s)\n\
        \    max1 = pass_lr(chars, 0, 0, 0)\n    max2 = pass_rl(Enum.reverse(chars),\
        \ 0, 0, 0)\n    max(max1, max2)\n  end\n\n  defp pass_lr([], _l, _r, max_len),\
        \ do: max_len\n  defp pass_lr([h | t], l, r, max_len) do\n    {nl, nr} = if\
        \ h == ?(, do: {l + 1, r}, else: {l, r + 1}\n    cond do\n      nl == nr ->\
        \ pass_lr(t, nl, nr, max(max_len, 2 * nr))\n      nr > nl -> pass_lr(t, 0, 0,\
        \ max_len)\n      true -> pass_lr(t, nl, nr, max_len)\n    end\n  end\n\n  defp\
        \ pass_rl([], _l, _r, max_len), do: max_len\n  defp pass_rl([h | t], l, r, max_len)\
        \ do\n    {nl, nr} = if h == ?(, do: {l + 1, r}, else: {l, r + 1}\n    cond\
        \ do\n      nl == nr -> pass_rl(t, nl, nr, max(max_len, 2 * nl))\n      nl >\
        \ nr -> pass_rl(t, 0, 0, max_len)\n      true -> pass_rl(t, nl, nr, max_len)\n\
        \    end\n  end\nend"
    approach: 'The algorithm uses a two-pass scanning technique to find the longest
      valid parentheses substring in O(n) time and O(1) space. In the first pass, we
      traverse the string from left to right, maintaining counters for opening ''(''
      and closing '')'' parentheses. Whenever the counts are equal, we update the maximum
      length found so far to be twice the current count. If the number of closing parentheses
      exceeds the number of opening ones, we reset both counters to zero, as the current
      sequence cannot be part of a valid substring.


      Because the first pass alone cannot detect valid sequences where the number of
      opening parentheses always exceeds the closing ones (e.g., ''(()''), a second
      pass is performed from right to left. In this pass, we reverse the logic: we increment
      counters as we move backward and update the maximum length when the counts are
      equal. If the number of opening parentheses exceeds the closing ones, we reset
      the counters. This dual-directional scan ensures that all possible valid substrings
      are accounted for without the need for additional memory structures like a stack.'
    time_complexity: O(n) where n is the length of the string. We iterate through the
      string exactly twice (once forward and once backward), and each character is processed
      in constant time.
    space_complexity: O(1) because we only utilize a few integer variables (left counter,
      right counter, and max length) to keep track of state, regardless of the input
      size.
    elapsed_time: 188.68868041038513
    model: gemini-3-flash-preview
    generated_at: '2026-10-03 03:12:50 '
---

## Problem #32: Longest Valid Parentheses

**Difficulty:** Hard

**Topics:** String, Dynamic Programming, Stack, Bracket Sequences

## Problem Description

<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, return <em>the length of the longest valid (well-formed) parentheses </em><span data-keyword="substring-nonempty"><em>substring</em></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)()())&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()()&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, or <code>&#39;)&#39;</code>.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a two-pass scanning technique to find the longest valid parentheses substring in O(n) time and O(1) space. In the first pass, we traverse the string from left to right, maintaining counters for opening '(' and closing ')' parentheses. Whenever the counts are equal, we update the maximum length found so far to be twice the current count. If the number of closing parentheses exceeds the number of opening ones, we reset both counters to zero, as the current sequence cannot be part of a valid substring.

Because the first pass alone cannot detect valid sequences where the number of opening parentheses always exceeds the closing ones (e.g., '(()'), a second pass is performed from right to left. In this pass, we reverse the logic: we increment counters as we move backward and update the maximum length when the counts are equal. If the number of opening parentheses exceeds the closing ones, we reset the counters. This dual-directional scan ensures that all possible valid substrings are accounted for without the need for additional memory structures like a stack.

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
    int longestValidParentheses(string s) {
        int left = 0, right = 0, maxLength = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLength = max(maxLength, 2 * right);
            } else if (right > left) {
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLength = max(maxLength, 2 * left);
            } else if (left > right) {
                left = right = 0;
            }
        }
        return maxLength;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int longestValidParentheses(String s) {
        int left = 0, right = 0, maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLength = Math.max(maxLength, 2 * right);
            } else if (right > left) {
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLength = Math.max(maxLength, 2 * left);
            } else if (left > right) {
                left = right = 0;
            }
        }
        return maxLength;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, maxLength = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxLength = max(maxLength, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif left > right:
                left = right = 0

        return maxLength
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int longestValidParentheses(char* s) {
    int n = 0;
    while (s[n] != '\0') n++;
    int left = 0, right = 0, max_len = 0;

    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            left++;
        } else {
            right++;
        }
        if (left == right) {
            if (2 * right > max_len) max_len = 2 * right;
        } else if (right > left) {
            left = 0;
            right = 0;
        }
    }

    left = 0;
    right = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '(') {
            left++;
        } else {
            right++;
        }
        if (left == right) {
            if (2 * left > max_len) max_len = 2 * left;
        } else if (left > right) {
            left = 0;
            right = 0;
        }
    }

    return max_len;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int LongestValidParentheses(string s) {
        int left = 0, right = 0, maxLen = 0;

        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLen = Math.Max(maxLen, 2 * right);
            } else if (right > left) {
                left = 0;
                right = 0;
            }
        }

        left = 0;
        right = 0;
        for (int i = s.Length - 1; i >= 0; i--) {
            if (s[i] == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxLen = Math.Max(maxLen, 2 * left);
            } else if (left > right) {
                left = 0;
                right = 0;
            }
        }

        return maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let left = 0, right = 0, maxLen = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            left++;
        } else {
            right++;
        }
        if (left === right) {
            maxLen = Math.max(maxLen, 2 * right);
        } else if (right > left) {
            left = 0;
            right = 0;
        }
    }

    left = 0;
    right = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === '(') {
            left++;
        } else {
            right++;
        }
        if (left === right) {
            maxLen = Math.max(maxLen, 2 * left);
        } else if (left > right) {
            left = 0;
            right = 0;
        }
    }

    return maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestValidParentheses(s: string): number {
    let maxLen = 0;
    const stack: number[] = [-1];
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.length === 0) {
                stack.push(i);
            } else {
                maxLen = Math.max(maxLen, i - stack[stack.length - 1]);
            }
        }
    }
    return maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function longestValidParentheses($s) {
        $maxLen = 0;
        $stack = [-1];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') {
                array_push($stack, $i);
            } else {
                array_pop($stack);
                if (empty($stack)) {
                    array_push($stack, $i);
                } else {
                    $currentLen = $i - $stack[count($stack) - 1];
                    if ($currentLen > $maxLen) {
                        $maxLen = $currentLen;
                    }
                }
            }
        }
        return $maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        var maxLen = 0
        var stack: [Int] = [-1]
        let chars = Array(s)
        for i in 0..<chars.count {
            if chars[i] == "(" {
                stack.append(i)
            } else {
                stack.removeLast()
                if stack.isEmpty {
                    stack.append(i)
                } else {
                    maxLen = max(maxLen, i - stack.last!)
                }
            }
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun longestValidParentheses(s: String): Int {
        var maxLen = 0
        val stack = java.util.ArrayDeque<Int>()
        stack.push(-1)
        for (i in s.indices) {
            if (s[i] == '(') {
                stack.push(i)
            } else {
                stack.pop()
                if (stack.isEmpty()) {
                    stack.push(i)
                } else {
                    maxLen = kotlin.math.max(maxLen, i - stack.peek())
                }
            }
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int longestValidParentheses(String s) {
    int maxLen = 0;
    List<int> stack = [-1];
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        stack.add(i);
      } else {
        stack.removeLast();
        if (stack.isEmpty) {
          stack.add(i);
        } else {
          int currentLen = i - stack.last;
          if (currentLen > maxLen) {
            maxLen = currentLen;
          }
        }
      }
    }
    return maxLen;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func longestValidParentheses(s string) int {
    maxLen := 0
    stack := []int{-1}
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            stack = append(stack, i)
        } else {
            stack = stack[:len(stack)-1]
            if len(stack) == 0 {
                stack = append(stack, i)
            } else {
                currentLen := i - stack[len(stack)-1]
                if currentLen > maxLen {
                    maxLen = currentLen
                }
            }
        }
    }
    return maxLen
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def longest_valid_parentheses(s)
  max_len = 0
  stack = [-1]
  s.each_char.with_index do |char, i|
    if char == '('
      stack.push(i)
    else
      stack.pop
      if stack.empty?
        stack.push(i)
      else
        current_len = i - stack.last
        max_len = current_len if current_len > max_len
      end
    end
  end
  max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def longestValidParentheses(s: String): Int = {
    var maxLen = 0
    var stack = List[Int](-1)
    for (i <- 0 until s.length) {
      if (s(i) == '(') {
        stack = i :: stack
      } else {
        stack = stack.tail
        if (stack.isEmpty) {
          stack = i :: Nil
        } else {
          val currentLen = i - stack.head
          if (currentLen > maxLen) {
            maxLen = currentLen
          }
        }
      }
    }
    maxLen
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let mut left: usize = 0;
        let mut right: usize = 0;
        let mut max_len: usize = 0;

        for &b in s_bytes.iter() {
            if b == b'(' {
                left += 1;
            } else {
                right += 1;
            }
            if left == right {
                max_len = max_len.max(2 * right);
            } else if right > left {
                left = 0;
                right = 0;
            }
        }

        left = 0;
        right = 0;
        for &b in s_bytes.iter().rev() {
            if b == b'(' {
                left += 1;
            } else {
                right += 1;
            }
            if left == right {
                max_len = max_len.max(2 * left);
            } else if left > right {
                left = 0;
                right = 0;
            }
        }

        max_len as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (longest-valid-parentheses s)
  (-> string? exact-integer?)
  (let ([n (string-length s)])
    (let* ([pass1 (let loop ([i 0] [l 0] [r 0] [m 0])
                    (if (< i n)
                        (let* ([c (string-ref s i)]
                               [nl (if (char=? c #\() (+ l 1) l)]
                               [nr (if (char=? c #\)) (+ r 1) r)])
                          (cond
                            [(= nl nr) (loop (+ i 1) nl nr (max m (* 2 nr)))]
                            [(> nr nl) (loop (+ i 1) 0 0 m)]
                            [else (loop (+ i 1) nl nr m)]))
                        m))]
           [pass2 (let loop ([i (- n 1)] [l 0] [r 0] [m 0])
                    (if (>= i 0)
                        (let* ([c (string-ref s i)]
                               [nl (if (char=? c #\() (+ l 1) l)]
                               [nr (if (char=? c #\)) (+ r 1) r)])
                          (cond
                            [(= nl nr) (loop (- i 1) nl nr (max m (* 2 nl)))]
                            [(> nl nr) (loop (- i 1) 0 0 m)]
                            [else (loop (- i 1) nl nr m)]))
                        m))])
      (max pass1 pass2))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_valid_parentheses(S :: unicode:unicode_binary()) -> integer().
longest_valid_parentheses(S) ->
  List = binary_to_list(S),
  Max1 = pass_lr(List, 0, 0, 0),
  Max2 = pass_rl(lists:reverse(List), 0, 0, 0),
  erlang:max(Max1, Max2).

pass_lr([], _, _, Max) -> Max;
pass_lr([H|T], L, R, Max) ->
  {NL, NR} = if H == $( -> {L + 1, R}; true -> {L, R + 1} end,
  if
    NL == NR -> pass_lr(T, NL, NR, erlang:max(Max, 2 * NR));
    NR > NL -> pass_lr(T, 0, 0, Max);
    true -> pass_lr(T, NL, NR, Max)
  end.

pass_rl([], _, _, Max) -> Max;
pass_rl([H|T], L, R, Max) ->
  {NL, NR} = if H == $( -> {L + 1, R}; true -> {L, R + 1} end,
  if
    NL == NR -> pass_rl(T, NL, NR, erlang:max(Max, 2 * NL));
    NL > NR -> pass_rl(T, 0, 0, Max);
    true -> pass_rl(T, NL, NR, Max)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec longest_valid_parentheses(s :: String.t) :: integer
  def longest_valid_parentheses(s) do
    chars = String.to_charlist(s)
    max1 = pass_lr(chars, 0, 0, 0)
    max2 = pass_rl(Enum.reverse(chars), 0, 0, 0)
    max(max1, max2)
  end

  defp pass_lr([], _l, _r, max_len), do: max_len
  defp pass_lr([h | t], l, r, max_len) do
    {nl, nr} = if h == ?(, do: {l + 1, r}, else: {l, r + 1}
    cond do
      nl == nr -> pass_lr(t, nl, nr, max(max_len, 2 * nr))
      nr > nl -> pass_lr(t, 0, 0, max_len)
      true -> pass_lr(t, nl, nr, max_len)
    end
  end

  defp pass_rl([], _l, _r, max_len), do: max_len
  defp pass_rl([h | t], l, r, max_len) do
    {nl, nr} = if h == ?(, do: {l + 1, r}, else: {l, r + 1}
    cond do
      nl == nr -> pass_rl(t, nl, nr, max(max_len, 2 * nl))
      nl > nr -> pass_rl(t, 0, 0, max_len)
      true -> pass_rl(t, nl, nr, max_len)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string. We iterate through the string exactly twice (once forward and once backward), and each character is processed in constant time.
- **Space Complexity:** O(1) because we only utilize a few integer variables (left counter, right counter, and max length) to keep track of state, regardless of the input size.
