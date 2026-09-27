---
layout: post
title: "Reverse Substrings Between Each Pair of Parentheses"
date: 2026-09-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Stack", "Bracket Sequences"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string reverseParentheses(string s) {\n \
        \       int n = s.length();\n        vector<int> pair(n);\n        vector<int>\
        \ stack;\n        for (int i = 0; i < n; ++i) {\n            if (s[i] == '(')\
        \ {\n                stack.push_back(i);\n            } else if (s[i] == ')')\
        \ {\n                int j = stack.back();\n                stack.pop_back();\n\
        \                pair[i] = j;\n                pair[j] = i;\n            }\n\
        \        }\n        string res = \"\";\n        int i = 0, d = 1;\n        while\
        \ (i < n && i >= 0) {\n            if (s[i] == '(' || s[i] == ')') {\n     \
        \           i = pair[i];\n                d = -d;\n            } else {\n  \
        \              res += s[i];\n            }\n            i += d;\n        }\n\
        \        return res;\n    }\n};"
      java: "class Solution {\n    public String reverseParentheses(String s) {\n  \
        \      int n = s.length();\n        int[] pair = new int[n];\n        int[]\
        \ stack = new int[n];\n        int top = -1;\n        for (int i = 0; i < n;\
        \ i++) {\n            if (s.charAt(i) == '(') {\n                stack[++top]\
        \ = i;\n            } else if (s.charAt(i) == ')') {\n                int j\
        \ = stack[top--];\n                pair[i] = j;\n                pair[j] = i;\n\
        \            }\n        }\n        StringBuilder res = new StringBuilder();\n\
        \        int i = 0, d = 1;\n        while (i < n && i >= 0) {\n            char\
        \ c = s.charAt(i);\n            if (c == '(' || c == ')') {\n              \
        \  i = pair[i];\n                d = -d;\n            } else {\n           \
        \     res.append(c);\n            }\n            i += d;\n        }\n      \
        \  return res.toString();\n    }\n}"
      python: "class Solution(object):\n    def reverseParentheses(self, s):\n     \
        \   \"\"\"\n        :type s: str\n        :rtype: str\n        \"\"\"\n    \
        \    n = len(s)\n        pair = [0] * n\n        stack = []\n        for i in\
        \ range(n):\n            if s[i] == '(':\n                stack.append(i)\n\
        \            elif s[i] == ')':\n                j = stack.pop()\n          \
        \      pair[i], pair[j] = j, i\n        res = []\n        i, d = 0, 1\n    \
        \    while i < n and i >= 0:\n            if s[i] == '(' or s[i] == ')':\n \
        \               i = pair[i]\n                d = -d\n            else:\n   \
        \             res.append(s[i])\n            i += d\n        return \"\".join(res)"
      python3: "class Solution:\n    def reverseParentheses(self, s: str) -> str:\n\
        \        n = len(s)\n        pair = [0] * n\n        stack = []\n        for\
        \ i in range(n):\n            if s[i] == '(':\n                stack.append(i)\n\
        \            elif s[i] == ')':\n                j = stack.pop()\n          \
        \      pair[i], pair[j] = j, i\n        res = []\n        i, d = 0, 1\n    \
        \    while i < n and i >= 0:\n            if s[i] in '()':\n               \
        \ i = pair[i]\n                d = -d\n            else:\n                res.append(s[i])\n\
        \            i += d\n        return \"\".join(res)"
      c: "char* reverseParentheses(char* s) {\n    int n = strlen(s);\n    int* pair\
        \ = (int*)malloc(n * sizeof(int));\n    int* stack = (int*)malloc(n * sizeof(int));\n\
        \    int top = -1;\n    for (int i = 0; i < n; i++) {\n        if (s[i] == '(')\
        \ {\n            stack[++top] = i;\n        } else if (s[i] == ')') {\n    \
        \        int j = stack[top--];\n            pair[i] = j;\n            pair[j]\
        \ = i;\n        }\n    }\n    char* res = (char*)malloc((n + 1) * sizeof(char));\n\
        \    int idx = 0;\n    int i = 0, d = 1;\n    while (i < n && i >= 0) {\n  \
        \      if (s[i] == '(' || s[i] == ')') {\n            i = pair[i];\n       \
        \     d = -d;\n        } else {\n            res[idx++] = s[i];\n        }\n\
        \        i += d;\n    }\n    res[idx] = '\\0';\n    free(pair);\n    free(stack);\n\
        \    return res;\n}"
      csharp: "using System.Collections.Generic;\nusing System.Text;\n\npublic class\
        \ Solution {\n    public string ReverseParentheses(string s) {\n        int\
        \ n = s.Length;\n        int[] pair = new int[n];\n        Stack<int> stack\
        \ = new Stack<int>();\n        for (int i = 0; i < n; i++) {\n            if\
        \ (s[i] == '(') {\n                stack.Push(i);\n            } else if (s[i]\
        \ == ')') {\n                int j = stack.Pop();\n                pair[i] =\
        \ j;\n                pair[j] = i;\n            }\n        }\n\n        StringBuilder\
        \ sb = new StringBuilder();\n        for (int i = 0, d = 1; i < n; i += d) {\n\
        \            if (s[i] == '(' || s[i] == ')') {\n                i = pair[i];\n\
        \                d = -d;\n            } else {\n                sb.Append(s[i]);\n\
        \            }\n        }\n        return sb.ToString();\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string}\n */\nvar reverseParentheses\
        \ = function(s) {\n    const n = s.length;\n    const pair = new Array(n);\n\
        \    const stack = [];\n    for (let i = 0; i < n; i++) {\n        if (s[i]\
        \ === '(') {\n            stack.push(i);\n        } else if (s[i] === ')') {\n\
        \            const j = stack.pop();\n            pair[i] = j;\n            pair[j]\
        \ = i;\n        }\n    }\n\n    let res = \"\";\n    for (let i = 0, d = 1;\
        \ i < n; i += d) {\n        if (s[i] === '(' || s[i] === ')') {\n          \
        \  i = pair[i];\n            d = -d;\n        } else {\n            res += s[i];\n\
        \        }\n    }\n    return res;\n};"
      typescript: "function reverseParentheses(s: string): string {\n    const n: number\
        \ = s.length;\n    const pair: number[] = new Array(n);\n    const stack: number[]\
        \ = [];\n    for (let i = 0; i < n; i++) {\n        if (s[i] === '(') {\n  \
        \          stack.push(i);\n        } else if (s[i] === ')') {\n            const\
        \ j = stack.pop()!;\n            pair[i] = j;\n            pair[j] = i;\n  \
        \      }\n    }\n\n    let res: string = \"\";\n    for (let i = 0, d = 1; i\
        \ < n; i += d) {\n        if (s[i] === '(' || s[i] === ')') {\n            i\
        \ = pair[i];\n            d = -d;\n        } else {\n            res += s[i];\n\
        \        }\n    }\n    return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String\n\
        \     */\n    function reverseParentheses($s) {\n        $n = strlen($s);\n\
        \        $pair = array_fill(0, $n, 0);\n        $stack = [];\n        for ($i\
        \ = 0; $i < $n; $i++) {\n            if ($s[$i] == '(') {\n                array_push($stack,\
        \ $i);\n            } else if ($s[$i] == ')') {\n                $j = array_pop($stack);\n\
        \                $pair[$i] = $j;\n                $pair[$j] = $i;\n        \
        \    }\n        }\n\n        $res = \"\";\n        for ($i = 0, $d = 1; $i <\
        \ $n; $i += $d) {\n            if ($s[$i] == '(' || $s[$i] == ')') {\n     \
        \           $i = $pair[$i];\n                $d = -$d;\n            } else {\n\
        \                $res .= $s[$i];\n            }\n        }\n        return $res;\n\
        \    }\n}"
      swift: "class Solution {\n    func reverseParentheses(_ s: String) -> String {\n\
        \        let sChars = Array(s)\n        let n = sChars.count\n        var pair\
        \ = Array(repeating: 0, count: n)\n        var stack = [Int]()\n\n        for\
        \ i in 0..<n {\n            if sChars[i] == \"(\" {\n                stack.append(i)\n\
        \            } else if sChars[i] == \")\" {\n                if let j = stack.popLast()\
        \ {\n                    pair[i] = j\n                    pair[j] = i\n    \
        \            }\n            }\n        }\n\n        var res = \"\"\n       \
        \ var i = 0\n        var d = 1\n        while i < n {\n            if sChars[i]\
        \ == \"(\" || sChars[i] == \")\" {\n                i = pair[i]\n          \
        \      d = -d\n            } else {\n                res.append(sChars[i])\n\
        \            }\n            i += d\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun reverseParentheses(s: String): String {\n \
        \       val n = s.length\n        val pair = IntArray(n)\n        val stack\
        \ = mutableListOf<Int>()\n        for (i in 0 until n) {\n            if (s[i]\
        \ == '(') {\n                stack.add(i)\n            } else if (s[i] == ')')\
        \ {\n                val j = stack.removeAt(stack.size - 1)\n              \
        \  pair[i] = j\n                pair[j] = i\n            }\n        }\n    \
        \    val res = StringBuilder()\n        var i = 0\n        var d = 1\n     \
        \   while (i < n) {\n            if (s[i] == '(' || s[i] == ')') {\n       \
        \         i = pair[i]\n                d = -d\n            } else {\n      \
        \          res.append(s[i])\n            }\n            i += d\n        }\n\
        \        return res.toString()\n    }\n}"
      dart: "class Solution {\n  String reverseParentheses(String s) {\n    int n =\
        \ s.length;\n    List<int> pair = List.filled(n, 0);\n    List<int> stack =\
        \ [];\n    for (int i = 0; i < n; i++) {\n      if (s[i] == '(') {\n       \
        \ stack.add(i);\n      } else if (s[i] == ')') {\n        int j = stack.removeLast();\n\
        \        pair[i] = j;\n        pair[j] = i;\n      }\n    }\n    StringBuffer\
        \ res = StringBuffer();\n    int i = 0;\n    int d = 1;\n    while (i < n &&\
        \ i >= 0) {\n      if (s[i] == '(' || s[i] == ')') {\n        i = pair[i];\n\
        \        d = -d;\n      } else {\n        res.write(s[i]);\n      }\n      i\
        \ += d;\n    }\n    return res.toString();\n  }\n}"
      go: "func reverseParentheses(s string) string {\n    n := len(s)\n    pair :=\
        \ make([]int, n)\n    stack := []int{}\n    for i, char := range s {\n     \
        \   if char == '(' {\n            stack = append(stack, i)\n        } else if\
        \ char == ')' {\n            j := stack[len(stack)-1]\n            stack = stack[:len(stack)-1]\n\
        \            pair[i] = j\n            pair[j] = i\n        }\n    }\n    var\
        \ res []byte\n    i, d := 0, 1\n    for i < n && i >= 0 {\n        if s[i] ==\
        \ '(' || s[i] == ')' {\n            i = pair[i]\n            d = -d\n      \
        \  } else {\n            res = append(res, s[i])\n        }\n        i += d\n\
        \    }\n    return string(res)\n}"
      ruby: "# @param {String} s\n# @return {String}\ndef reverse_parentheses(s)\n \
        \ n = s.length\n  pair = Array.new(n)\n  stack = []\n  n.times do |i|\n    if\
        \ s[i] == '('\n      stack.push(i)\n    elsif s[i] == ')'\n      j = stack.pop\n\
        \      pair[i] = j\n      pair[j] = i\n    end\n  end\n  res = \"\"\n  i = 0\n\
        \  d = 1\n  while i < n && i >= 0\n    if s[i] == '(' || s[i] == ')'\n     \
        \ i = pair[i]\n      d = -d\n    else\n      res << s[i]\n    end\n    i +=\
        \ d\n  end\n  res\nend"
      scala: "object Solution {\n    def reverseParentheses(s: String): String = {\n\
        \        val n = s.length\n        val pair = new Array[Int](n)\n        val\
        \ stack = scala.collection.mutable.Stack[Int]()\n        for (i <- 0 until n)\
        \ {\n            if (s(i) == '(') {\n                stack.push(i)\n       \
        \     } else if (s(i) == ')') {\n                val j = stack.pop()\n     \
        \           pair(i) = j\n                pair(j) = i\n            }\n      \
        \  }\n        val res = new StringBuilder()\n        var i = 0\n        var\
        \ d = 1\n        while (i < n && i >= 0) {\n            if (s(i) == '(' || s(i)\
        \ == ')') {\n                i = pair(i)\n                d = -d\n         \
        \   } else {\n                res.append(s(i))\n            }\n            i\
        \ += d\n        }\n        res.toString()\n    }\n}"
      rust: "impl Solution {\n    pub fn reverse_parentheses(s: String) -> String {\n\
        \        let n = s.len();\n        let s_bytes = s.as_bytes();\n        let\
        \ mut pair = vec![0; n];\n        let mut stack = Vec::new();\n        for i\
        \ in 0..n {\n            if s_bytes[i] == b'(' {\n                stack.push(i);\n\
        \            } else if s_bytes[i] == b')' {\n                let j = stack.pop().unwrap();\n\
        \                pair[i] = j;\n                pair[j] = i;\n            }\n\
        \        }\n        let mut res = String::with_capacity(n);\n        let mut\
        \ i: isize = 0;\n        let mut d: isize = 1;\n        let n_isize = n as isize;\n\
        \        while i >= 0 && i < n_isize {\n            let idx = i as usize;\n\
        \            if s_bytes[idx] == b'(' || s_bytes[idx] == b')' {\n           \
        \     i = pair[idx] as isize;\n                d = -d;\n            } else {\n\
        \                res.push(s_bytes[idx] as char);\n            }\n          \
        \  i += d;\n        }\n        res\n    }\n}"
      racket: "(define/contract (reverse-parentheses s)\n  (-> string? string?)\n  (let*\
        \ ([n (string-length s)]\n         [pair (make-vector n)]\n         [stack '()])\n\
        \    (for ([i (in-range n)])\n      (let ([c (string-ref s i)])\n        (cond\n\
        \          [(char=? c #\\() (set! stack (cons i stack))]\n          [(char=?\
        \ c #\\))\n           (let ([j (car stack)])\n             (set! stack (cdr\
        \ stack))\n             (vector-set! pair i j)\n             (vector-set! pair\
        \ j i))])))\n    (let loop ([i 0] [d 1] [res '()])\n      (if (and (>= i 0)\
        \ (< i n))\n          (let ([c (string-ref s i)])\n            (if (or (char=?\
        \ c #\\() (char=? c #\\)))\n                (let* ([new-d (- d)]\n         \
        \              [new-i (+ (vector-ref pair i) new-d)])\n                  (loop\
        \ new-i new-d res))\n                (loop (+ i d) d (cons c res))))\n     \
        \     (list->string (reverse res))))))"
      erlang: "-spec reverse_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().\n\
        reverse_parentheses(S) ->\n  N = byte_size(S),\n  PairArray = build_pairs(S,\
        \ 0, N, [], array:new(N)),\n  Result = traverse(S, 0, 1, PairArray, N, []),\n\
        \  list_to_binary(lists:reverse(Result)).\n\nbuild_pairs(_S, I, N, _Stack, Acc)\
        \ when I == N -> Acc;\nbuild_pairs(S, I, N, Stack, Acc) ->\n  case binary:at(S,\
        \ I) of\n    $( -> build_pairs(S, I + 1, N, [I | Stack], Acc);\n    $) ->\n\
        \      [J | Rest] = Stack,\n      Acc1 = array:set(I, J, Acc),\n      Acc2 =\
        \ array:set(J, I, Acc1),\n      build_pairs(S, I + 1, N, Rest, Acc2);\n    _\
        \ -> build_pairs(S, I + 1, N, Stack, Acc)\n  end.\n\ntraverse(_S, I, _D, _Pairs,\
        \ N, Acc) when I < 0; I >= N -> Acc;\ntraverse(S, I, D, Pairs, N, Acc) ->\n\
        \  Char = binary:at(S, I),\n  case Char of\n    $( -> traverse(S, array:get(I,\
        \ Pairs) - D, -D, Pairs, N, Acc);\n    $) -> traverse(S, array:get(I, Pairs)\
        \ - D, -D, Pairs, N, Acc);\n    _ -> traverse(S, I + D, D, Pairs, N, [Char |\
        \ Acc])\n  end."
      elixir: "defmodule Solution do\n  @spec reverse_parentheses(s :: String.t) ::\
        \ String.t\n  def reverse_parentheses(s) do\n    n = byte_size(s)\n    pairs\
        \ = build_pairs(s, n)\n    traverse(s, 0, 1, pairs, n, [])\n  end\n\n  defp\
        \ build_pairs(s, n) do\n    chars = String.to_charlist(s)\n    {_, pairs} =\
        \ Enum.reduce(Enum.with_index(chars), {[], %{}}, fn {char, i}, {stack, acc}\
        \ ->\n      case char do\n        ?( -> {[i | stack], acc}\n        ?) ->\n\
        \          [j | rest] = stack\n          {rest, acc |> Map.put(i, j) |> Map.put(j,\
        \ i)}\n        _ -> {stack, acc}\n      end\n    end)\n    pairs\n  end\n\n\
        \  defp traverse(s, i, d, pairs, n, acc) when i >= 0 and i < n do\n    char\
        \ = :binary.at(s, i)\n    case char do\n      c when c == ?( or c == ?) ->\n\
        \        new_d = -d\n        new_i = Map.get(pairs, i) + new_d\n        traverse(s,\
        \ new_i, new_d, pairs, n, acc)\n      _ ->\n        traverse(s, i + d, d, pairs,\
        \ n, [char | acc])\n    end\n  end\n\n  defp traverse(_s, _i, _d, _pairs, _n,\
        \ acc) do\n    acc |> Enum.reverse() |> List.to_string()\n  end\nend"
    approach: 'The problem can be solved efficiently using an O(N) traversal technique
      often called the wormhole or portal method. First, we identify matching pairs
      of parentheses by using a stack to store indices of opening brackets. We create
      an auxiliary array where each bracket''s index is mapped to its matching partner''s
      index. This allows us to treat parentheses as portals: whenever we encounter one
      during traversal, we jump to its matching partner and flip our traversal direction.'
    time_complexity: O(N) where N is the length of the string. We perform one linear
      pass to find matching parentheses using a stack and a second linear pass to construct
      the result string by jumping between portals.
    space_complexity: O(N) because we use an auxiliary array of size N to store the
      partner indices, a stack for matching parentheses, and a buffer to build the final
      output string.
    elapsed_time: 125.08882331848145
    model: gemini-3-flash-preview
    generated_at: '2026-09-27 02:54:00 '
---

## Problem #1190: Reverse Substrings Between Each Pair of Parentheses

**Difficulty:** Medium

**Topics:** String, Stack, Bracket Sequences

## Problem Description

<p>You are given a string <code>s</code> that consists of lower case English letters and brackets.</p>

<p>Reverse the strings in each pair of matching parentheses, starting from the innermost one.</p>

<p>Your result should <strong>not</strong> contain any brackets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(abcd)&quot;
<strong>Output:</strong> &quot;dcba&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(u(love)i)&quot;
<strong>Output:</strong> &quot;iloveu&quot;
<strong>Explanation:</strong> The substring &quot;love&quot; is reversed first, then the whole string is reversed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(ed(et(oc))el)&quot;
<strong>Output:</strong> &quot;leetcode&quot;
<strong>Explanation:</strong> First, we reverse the substring &quot;oc&quot;, then &quot;etco&quot;, and finally, the whole string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> only contains lower case English characters and parentheses.</li>
	<li>It is guaranteed that all parentheses are balanced.</li>
</ul>


## Hints

1. Find all brackets in the string.

2. Does the order of the reverse matter ?

3. The order does not matter.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved efficiently using an O(N) traversal technique often called the wormhole or portal method. First, we identify matching pairs of parentheses by using a stack to store indices of opening brackets. We create an auxiliary array where each bracket's index is mapped to its matching partner's index. This allows us to treat parentheses as portals: whenever we encounter one during traversal, we jump to its matching partner and flip our traversal direction.

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
    string reverseParentheses(string s) {
        int n = s.length();
        vector<int> pair(n);
        vector<int> stack;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '(') {
                stack.push_back(i);
            } else if (s[i] == ')') {
                int j = stack.back();
                stack.pop_back();
                pair[i] = j;
                pair[j] = i;
            }
        }
        string res = "";
        int i = 0, d = 1;
        while (i < n && i >= 0) {
            if (s[i] == '(' || s[i] == ')') {
                i = pair[i];
                d = -d;
            } else {
                res += s[i];
            }
            i += d;
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String reverseParentheses(String s) {
        int n = s.length();
        int[] pair = new int[n];
        int[] stack = new int[n];
        int top = -1;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                stack[++top] = i;
            } else if (s.charAt(i) == ')') {
                int j = stack[top--];
                pair[i] = j;
                pair[j] = i;
            }
        }
        StringBuilder res = new StringBuilder();
        int i = 0, d = 1;
        while (i < n && i >= 0) {
            char c = s.charAt(i);
            if (c == '(' || c == ')') {
                i = pair[i];
                d = -d;
            } else {
                res.append(c);
            }
            i += d;
        }
        return res.toString();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pair = [0] * n
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1
        while i < n and i >= 0:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1
        while i < n and i >= 0:
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* reverseParentheses(char* s) {
    int n = strlen(s);
    int* pair = (int*)malloc(n * sizeof(int));
    int* stack = (int*)malloc(n * sizeof(int));
    int top = -1;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            stack[++top] = i;
        } else if (s[i] == ')') {
            int j = stack[top--];
            pair[i] = j;
            pair[j] = i;
        }
    }
    char* res = (char*)malloc((n + 1) * sizeof(char));
    int idx = 0;
    int i = 0, d = 1;
    while (i < n && i >= 0) {
        if (s[i] == '(' || s[i] == ')') {
            i = pair[i];
            d = -d;
        } else {
            res[idx++] = s[i];
        }
        i += d;
    }
    res[idx] = '\0';
    free(pair);
    free(stack);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ReverseParentheses(string s) {
        int n = s.Length;
        int[] pair = new int[n];
        Stack<int> stack = new Stack<int>();
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                stack.Push(i);
            } else if (s[i] == ')') {
                int j = stack.Pop();
                pair[i] = j;
                pair[j] = i;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0, d = 1; i < n; i += d) {
            if (s[i] == '(' || s[i] == ')') {
                i = pair[i];
                d = -d;
            } else {
                sb.Append(s[i]);
            }
        }
        return sb.ToString();
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
 * @return {string}
 */
var reverseParentheses = function(s) {
    const n = s.length;
    const pair = new Array(n);
    const stack = [];
    for (let i = 0; i < n; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else if (s[i] === ')') {
            const j = stack.pop();
            pair[i] = j;
            pair[j] = i;
        }
    }

    let res = "";
    for (let i = 0, d = 1; i < n; i += d) {
        if (s[i] === '(' || s[i] === ')') {
            i = pair[i];
            d = -d;
        } else {
            res += s[i];
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function reverseParentheses(s: string): string {
    const n: number = s.length;
    const pair: number[] = new Array(n);
    const stack: number[] = [];
    for (let i = 0; i < n; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else if (s[i] === ')') {
            const j = stack.pop()!;
            pair[i] = j;
            pair[j] = i;
        }
    }

    let res: string = "";
    for (let i = 0, d = 1; i < n; i += d) {
        if (s[i] === '(' || s[i] === ')') {
            i = pair[i];
            d = -d;
        } else {
            res += s[i];
        }
    }
    return res;
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
     * @return String
     */
    function reverseParentheses($s) {
        $n = strlen($s);
        $pair = array_fill(0, $n, 0);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] == '(') {
                array_push($stack, $i);
            } else if ($s[$i] == ')') {
                $j = array_pop($stack);
                $pair[$i] = $j;
                $pair[$j] = $i;
            }
        }

        $res = "";
        for ($i = 0, $d = 1; $i < $n; $i += $d) {
            if ($s[$i] == '(' || $s[$i] == ')') {
                $i = $pair[$i];
                $d = -$d;
            } else {
                $res .= $s[$i];
            }
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func reverseParentheses(_ s: String) -> String {
        let sChars = Array(s)
        let n = sChars.count
        var pair = Array(repeating: 0, count: n)
        var stack = [Int]()

        for i in 0..<n {
            if sChars[i] == "(" {
                stack.append(i)
            } else if sChars[i] == ")" {
                if let j = stack.popLast() {
                    pair[i] = j
                    pair[j] = i
                }
            }
        }

        var res = ""
        var i = 0
        var d = 1
        while i < n {
            if sChars[i] == "(" || sChars[i] == ")" {
                i = pair[i]
                d = -d
            } else {
                res.append(sChars[i])
            }
            i += d
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun reverseParentheses(s: String): String {
        val n = s.length
        val pair = IntArray(n)
        val stack = mutableListOf<Int>()
        for (i in 0 until n) {
            if (s[i] == '(') {
                stack.add(i)
            } else if (s[i] == ')') {
                val j = stack.removeAt(stack.size - 1)
                pair[i] = j
                pair[j] = i
            }
        }
        val res = StringBuilder()
        var i = 0
        var d = 1
        while (i < n) {
            if (s[i] == '(' || s[i] == ')') {
                i = pair[i]
                d = -d
            } else {
                res.append(s[i])
            }
            i += d
        }
        return res.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String reverseParentheses(String s) {
    int n = s.length;
    List<int> pair = List.filled(n, 0);
    List<int> stack = [];
    for (int i = 0; i < n; i++) {
      if (s[i] == '(') {
        stack.add(i);
      } else if (s[i] == ')') {
        int j = stack.removeLast();
        pair[i] = j;
        pair[j] = i;
      }
    }
    StringBuffer res = StringBuffer();
    int i = 0;
    int d = 1;
    while (i < n && i >= 0) {
      if (s[i] == '(' || s[i] == ')') {
        i = pair[i];
        d = -d;
      } else {
        res.write(s[i]);
      }
      i += d;
    }
    return res.toString();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func reverseParentheses(s string) string {
    n := len(s)
    pair := make([]int, n)
    stack := []int{}
    for i, char := range s {
        if char == '(' {
            stack = append(stack, i)
        } else if char == ')' {
            j := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            pair[i] = j
            pair[j] = i
        }
    }
    var res []byte
    i, d := 0, 1
    for i < n && i >= 0 {
        if s[i] == '(' || s[i] == ')' {
            i = pair[i]
            d = -d
        } else {
            res = append(res, s[i])
        }
        i += d
    }
    return string(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {String}
def reverse_parentheses(s)
  n = s.length
  pair = Array.new(n)
  stack = []
  n.times do |i|
    if s[i] == '('
      stack.push(i)
    elsif s[i] == ')'
      j = stack.pop
      pair[i] = j
      pair[j] = i
    end
  end
  res = ""
  i = 0
  d = 1
  while i < n && i >= 0
    if s[i] == '(' || s[i] == ')'
      i = pair[i]
      d = -d
    else
      res << s[i]
    end
    i += d
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def reverseParentheses(s: String): String = {
        val n = s.length
        val pair = new Array[Int](n)
        val stack = scala.collection.mutable.Stack[Int]()
        for (i <- 0 until n) {
            if (s(i) == '(') {
                stack.push(i)
            } else if (s(i) == ')') {
                val j = stack.pop()
                pair(i) = j
                pair(j) = i
            }
        }
        val res = new StringBuilder()
        var i = 0
        var d = 1
        while (i < n && i >= 0) {
            if (s(i) == '(' || s(i) == ')') {
                i = pair(i)
                d = -d
            } else {
                res.append(s(i))
            }
            i += d
        }
        res.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let n = s.len();
        let s_bytes = s.as_bytes();
        let mut pair = vec![0; n];
        let mut stack = Vec::new();
        for i in 0..n {
            if s_bytes[i] == b'(' {
                stack.push(i);
            } else if s_bytes[i] == b')' {
                let j = stack.pop().unwrap();
                pair[i] = j;
                pair[j] = i;
            }
        }
        let mut res = String::with_capacity(n);
        let mut i: isize = 0;
        let mut d: isize = 1;
        let n_isize = n as isize;
        while i >= 0 && i < n_isize {
            let idx = i as usize;
            if s_bytes[idx] == b'(' || s_bytes[idx] == b')' {
                i = pair[idx] as isize;
                d = -d;
            } else {
                res.push(s_bytes[idx] as char);
            }
            i += d;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (reverse-parentheses s)
  (-> string? string?)
  (let* ([n (string-length s)]
         [pair (make-vector n)]
         [stack '()])
    (for ([i (in-range n)])
      (let ([c (string-ref s i)])
        (cond
          [(char=? c #\() (set! stack (cons i stack))]
          [(char=? c #\))
           (let ([j (car stack)])
             (set! stack (cdr stack))
             (vector-set! pair i j)
             (vector-set! pair j i))])))
    (let loop ([i 0] [d 1] [res '()])
      (if (and (>= i 0) (< i n))
          (let ([c (string-ref s i)])
            (if (or (char=? c #\() (char=? c #\)))
                (let* ([new-d (- d)]
                       [new-i (+ (vector-ref pair i) new-d)])
                  (loop new-i new-d res))
                (loop (+ i d) d (cons c res))))
          (list->string (reverse res))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec reverse_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_parentheses(S) ->
  N = byte_size(S),
  PairArray = build_pairs(S, 0, N, [], array:new(N)),
  Result = traverse(S, 0, 1, PairArray, N, []),
  list_to_binary(lists:reverse(Result)).

build_pairs(_S, I, N, _Stack, Acc) when I == N -> Acc;
build_pairs(S, I, N, Stack, Acc) ->
  case binary:at(S, I) of
    $( -> build_pairs(S, I + 1, N, [I | Stack], Acc);
    $) ->
      [J | Rest] = Stack,
      Acc1 = array:set(I, J, Acc),
      Acc2 = array:set(J, I, Acc1),
      build_pairs(S, I + 1, N, Rest, Acc2);
    _ -> build_pairs(S, I + 1, N, Stack, Acc)
  end.

traverse(_S, I, _D, _Pairs, N, Acc) when I < 0; I >= N -> Acc;
traverse(S, I, D, Pairs, N, Acc) ->
  Char = binary:at(S, I),
  case Char of
    $( -> traverse(S, array:get(I, Pairs) - D, -D, Pairs, N, Acc);
    $) -> traverse(S, array:get(I, Pairs) - D, -D, Pairs, N, Acc);
    _ -> traverse(S, I + D, D, Pairs, N, [Char | Acc])
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec reverse_parentheses(s :: String.t) :: String.t
  def reverse_parentheses(s) do
    n = byte_size(s)
    pairs = build_pairs(s, n)
    traverse(s, 0, 1, pairs, n, [])
  end

  defp build_pairs(s, n) do
    chars = String.to_charlist(s)
    {_, pairs} = Enum.reduce(Enum.with_index(chars), {[], %{}}, fn {char, i}, {stack, acc} ->
      case char do
        ?( -> {[i | stack], acc}
        ?) ->
          [j | rest] = stack
          {rest, acc |> Map.put(i, j) |> Map.put(j, i)}
        _ -> {stack, acc}
      end
    end)
    pairs
  end

  defp traverse(s, i, d, pairs, n, acc) when i >= 0 and i < n do
    char = :binary.at(s, i)
    case char do
      c when c == ?( or c == ?) ->
        new_d = -d
        new_i = Map.get(pairs, i) + new_d
        traverse(s, new_i, new_d, pairs, n, acc)
      _ ->
        traverse(s, i + d, d, pairs, n, [char | acc])
    end
  end

  defp traverse(_s, _i, _d, _pairs, _n, acc) do
    acc |> Enum.reverse() |> List.to_string()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the string. We perform one linear pass to find matching parentheses using a stack and a second linear pass to construct the result string by jumping between portals.
- **Space Complexity:** O(N) because we use an auxiliary array of size N to store the partner indices, a stack for matching parentheses, and a buffer to build the final output string.
