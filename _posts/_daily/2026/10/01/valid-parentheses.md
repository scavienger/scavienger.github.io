---
layout: post
title: "Valid Parentheses"
date: 2026-10-01 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "Stack", "Bracket Sequences"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/valid-parentheses/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool isValid(string s) {\n        std::stack<char>\
        \ st;\n        for (char c : s) {\n            if (c == '(' || c == '{' || c\
        \ == '[') {\n                st.push(c);\n            } else {\n           \
        \     if (st.empty()) return false;\n                if (c == ')' && st.top()\
        \ != '(') return false;\n                if (c == '}' && st.top() != '{') return\
        \ false;\n                if (c == ']' && st.top() != '[') return false;\n \
        \               st.pop();\n            }\n        }\n        return st.empty();\n\
        \    }\n};"
      java: "class Solution {\n    public boolean isValid(String s) {\n        java.util.Stack<Character>\
        \ stack = new java.util.Stack<>();\n        for (char c : s.toCharArray()) {\n\
        \            if (c == '(' || c == '{' || c == '[') {\n                stack.push(c);\n\
        \            } else {\n                if (stack.isEmpty()) return false;\n\
        \                char top = stack.pop();\n                if (c == ')' && top\
        \ != '(') return false;\n                if (c == '}' && top != '{') return\
        \ false;\n                if (c == ']' && top != '[') return false;\n      \
        \      }\n        }\n        return stack.isEmpty();\n    }\n}"
      python: "class Solution(object):\n    def isValid(self, s):\n        \"\"\"\n\
        \        :type s: str\n        :rtype: bool\n        \"\"\"\n        stack =\
        \ []\n        mapping = {\")\": \"(\", \"}\": \"{\", \"]\": \"[\"}\n       \
        \ for char in s:\n            if char in mapping:\n                top_element\
        \ = stack.pop() if stack else '#'\n                if mapping[char] != top_element:\n\
        \                    return False\n            else:\n                stack.append(char)\n\
        \        return not stack"
      python3: "class Solution:\n    def isValid(self, s: str) -> bool:\n        stack\
        \ = []\n        mapping = {\")\": \"(\", \"}\": \"{\", \"]\": \"[\"}\n     \
        \   for char in s:\n            if char in mapping:\n                top_element\
        \ = stack.pop() if stack else '#'\n                if mapping[char] != top_element:\n\
        \                    return False\n            else:\n                stack.append(char)\n\
        \        return not stack"
      c: "bool isValid(char* s) {\n    int n = 0;\n    while (s[n]) n++;\n    char stack[n\
        \ + 1];\n    int top = -1;\n    for (int i = 0; i < n; i++) {\n        if (s[i]\
        \ == '(' || s[i] == '{' || s[i] == '[') {\n            stack[++top] = s[i];\n\
        \        } else {\n            if (top == -1) return false;\n            if\
        \ ((s[i] == ')' && stack[top] != '(') ||\n                (s[i] == '}' && stack[top]\
        \ != '{') ||\n                (s[i] == ']' && stack[top] != '[')) {\n      \
        \          return false;\n            }\n            top--;\n        }\n   \
        \ }\n    return top == -1;\n}"
      csharp: "public class Solution {\n    public bool IsValid(string s) {\n      \
        \  System.Collections.Generic.Stack<char> stack = new System.Collections.Generic.Stack<char>();\n\
        \        foreach (char c in s) {\n            if (c == '(' || c == '{' || c\
        \ == '[') {\n                stack.Push(c);\n            } else {\n        \
        \        if (stack.Count == 0) return false;\n                char top = stack.Pop();\n\
        \                if (c == ')' && top != '(') return false;\n               \
        \ if (c == '}' && top != '{') return false;\n                if (c == ']' &&\
        \ top != '[') return false;\n            }\n        }\n        return stack.Count\
        \ == 0;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {boolean}\n */\nvar isValid\
        \ = function(s) {\n    const stack = [];\n    const mapping = {\n        ')':\
        \ '(',\n        '}': '{',\n        ']': '['\n    };\n    for (let i = 0; i <\
        \ s.length; i++) {\n        const char = s[i];\n        if (mapping[char]) {\n\
        \            const topElement = stack.length === 0 ? '#' : stack.pop();\n  \
        \          if (mapping[char] !== topElement) {\n                return false;\n\
        \            }\n        } else {\n            stack.push(char);\n        }\n\
        \    }\n    return stack.length === 0;\n};"
      typescript: "function isValid(s: string): boolean {\n    const stack: string[]\
        \ = [];\n    const mapping: { [key: string]: string } = {\n        ')': '(',\n\
        \        '}': '{',\n        ']': '['\n    };\n\n    for (let i = 0; i < s.length;\
        \ i++) {\n        const char = s[i];\n        if (mapping[char]) {\n       \
        \     const topElement = stack.length === 0 ? '#' : stack.pop();\n         \
        \   if (topElement !== mapping[char]) {\n                return false;\n   \
        \         }\n        } else {\n            stack.push(char);\n        }\n  \
        \  }\n\n    return stack.length === 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Boolean\n\
        \     */\n    function isValid($s) {\n        $stack = [];\n        $mapping\
        \ = [\n            ')' => '(',\n            '}' => '{',\n            ']' =>\
        \ '['\n        ];\n\n        $len = strlen($s);\n        for ($i = 0; $i < $len;\
        \ $i++) {\n            $char = $s[$i];\n            if (isset($mapping[$char]))\
        \ {\n                if (empty($stack) || array_pop($stack) !== $mapping[$char])\
        \ {\n                    return false;\n                }\n            } else\
        \ {\n                array_push($stack, $char);\n            }\n        }\n\n\
        \        return empty($stack);\n    }\n}"
      swift: "class Solution {\n    func isValid(_ s: String) -> Bool {\n        var\
        \ stack = [Character]()\n        let mapping: [Character: Character] = [\n \
        \           \")\": \"(\",\n            \"}\": \"{\",\n            \"]\": \"\
        [\"\n        ]\n\n        for char in s {\n            if let openingBracket\
        \ = mapping[char] {\n                if stack.isEmpty || stack.removeLast()\
        \ != openingBracket {\n                    return false\n                }\n\
        \            } else {\n                stack.append(char)\n            }\n \
        \       }\n\n        return stack.isEmpty\n    }\n}"
      kotlin: "class Solution {\n    fun isValid(s: String): Boolean {\n        val\
        \ stack = java.util.Stack<Char>()\n        val mapping = mapOf(')' to '(', '}'\
        \ to '{', ']' to '[')\n\n        for (char in s) {\n            if (mapping.containsKey(char))\
        \ {\n                if (stack.isEmpty() || stack.pop() != mapping[char]) {\n\
        \                    return false\n                }\n            } else {\n\
        \                stack.push(char)\n            }\n        }\n\n        return\
        \ stack.isEmpty()\n    }\n}"
      dart: "class Solution {\n  bool isValid(String s) {\n    List<String> stack =\
        \ [];\n    Map<String, String> mapping = {\n      ')': '(',\n      '}': '{',\n\
        \      ']': '[',\n    };\n\n    for (int i = 0; i < s.length; i++) {\n     \
        \ String char = s[i];\n      if (mapping.containsKey(char)) {\n        if (stack.isEmpty\
        \ || stack.removeLast() != mapping[char]) {\n          return false;\n     \
        \   }\n      } else {\n        stack.add(char);\n      }\n    }\n\n    return\
        \ stack.isEmpty;\n  }\n}"
      go: "func isValid(s string) bool {\n    stack := []rune{}\n    mapping := map[rune]rune{\n\
        \        ')': '(',\n        '}': '{',\n        ']': '[',\n    }\n\n    for _,\
        \ char := range s {\n        if opening, ok := mapping[char]; ok {\n       \
        \     if len(stack) == 0 || stack[len(stack)-1] != opening {\n             \
        \   return false\n            }\n            stack = stack[:len(stack)-1]\n\
        \        } else {\n            stack = append(stack, char)\n        }\n    }\n\
        \n    return len(stack) == 0\n}"
      ruby: "# @param {String} s\n# @return {Boolean}\ndef is_valid(s)\n  stack = []\n\
        \  pairs = { ')' => '(', ']' => '[', '}' => '{' }\n  s.each_char do |c|\n  \
        \  if pairs.key?(c)\n      return false if stack.pop != pairs[c]\n    else\n\
        \      stack.push(c)\n    end\n  end\n  stack.empty?\nend"
      scala: "object Solution {\n    def isValid(s: String): Boolean = {\n        val\
        \ pairs = Map(')' -> '(', '}' -> '{', ']' -> '[')\n        def solve(chars:\
        \ List[Char], stack: List[Char]): Boolean = chars match {\n            case\
        \ Nil => stack.isEmpty\n            case c :: rest =>\n                if (pairs.contains(c))\
        \ {\n                    if (stack.nonEmpty && stack.head == pairs(c)) solve(rest,\
        \ stack.tail)\n                    else false\n                } else {\n  \
        \                  solve(rest, c :: stack)\n                }\n        }\n \
        \       solve(s.toList, Nil)\n    }\n}"
      rust: "impl Solution {\n    pub fn is_valid(s: String) -> bool {\n        let\
        \ mut stack = Vec::new();\n        for c in s.chars() {\n            match c\
        \ {\n                '(' | '[' | '{' => stack.push(c),\n                ')'\
        \ => if stack.pop() != Some('(') { return false; },\n                ']' =>\
        \ if stack.pop() != Some('[') { return false; },\n                '}' => if\
        \ stack.pop() != Some('{') { return false; },\n                _ => return false,\n\
        \            }\n        }\n        stack.is_empty()\n    }\n}"
      racket: "(define/contract (is-valid s)\n  (-> string? boolean?)\n  (let loop ([chars\
        \ (string->list s)]\n             [stack '()])\n    (if (null? chars)\n    \
        \    (null? stack)\n        (let ([c (car chars)]\n              [rest (cdr\
        \ chars)])\n          (cond\n            [(char=? c #\\() (loop rest (cons #\\\
        ( stack))]\n            [(char=? c #\\[) (loop rest (cons #\\[ stack))]\n  \
        \          [(char=? c #\\{) (loop rest (cons #\\{ stack))]\n            [(and\
        \ (not (null? stack)) (char=? c #\\)) (char=? (car stack) #\\()) (loop rest\
        \ (cdr stack))]\n            [(and (not (null? stack)) (char=? c #\\]) (char=?\
        \ (car stack) #\\[)) (loop rest (cdr stack))]\n            [(and (not (null?\
        \ stack)) (char=? c #\\}) (char=? (car stack) #\\{)) (loop rest (cdr stack))]\n\
        \            [else #f])))))"
      erlang: "-spec is_valid(S :: unicode:unicode_binary()) -> boolean().\nis_valid(S)\
        \ ->\n  is_valid_helper(binary_to_list(S), []).\n\nis_valid_helper([], []) ->\
        \ true;\nis_valid_helper([], _) -> false;\nis_valid_helper([$( | Rest], Stack)\
        \ -> is_valid_helper(Rest, [$( | Stack]);\nis_valid_helper([$[ | Rest], Stack)\
        \ -> is_valid_helper(Rest, [$[ | Stack]);\nis_valid_helper([${ | Rest], Stack)\
        \ -> is_valid_helper(Rest, [${ | Stack]);\nis_valid_helper([$) | Rest], [$(\
        \ | Stack]) -> is_valid_helper(Rest, Stack);\nis_valid_helper([$] | Rest], [$[\
        \ | Stack]) -> is_valid_helper(Rest, Stack);\nis_valid_helper([$} | Rest], [${\
        \ | Stack]) -> is_valid_helper(Rest, Stack);\nis_valid_helper(_, _) -> false."
      elixir: "defmodule Solution do\n  @spec is_valid(s :: String.t) :: boolean\n \
        \ def is_valid(s) do\n    check(String.graphemes(s), [])\n  end\n\n  defp check([],\
        \ []), do: true\n  defp check([], _), do: false\n  defp check([c | rest], stack)\
        \ when c in [\"(\", \"[\", \"{\"] do\n    check(rest, [c | stack])\n  end\n\
        \  defp check([\")\" | rest], [\"(\" | stack]), do: check(rest, stack)\n  defp\
        \ check([\"]\" | rest], [\"[\" | stack]), do: check(rest, stack)\n  defp check([\"\
        }\" | rest], [\"{\" | stack]), do: check(rest, stack)\n  defp check(_, _), do:\
        \ false\nend"
    approach: 'The algorithm utilizes a stack data structure to track opening brackets
      as the string is traversed from left to right. When an opening bracket (''('',
      ''{'', or ''['') is encountered, it is pushed onto the stack, ensuring that the
      most recently opened bracket is always at the top. This LIFO (Last-In-First-Out)
      behavior is essential because the last bracket opened must be the first one closed
      to satisfy a valid nested sequence.


      When a closing bracket is encountered, the algorithm checks the top of the stack
      to see if it matches the current bracket''s type. If the stack is empty or the
      top element does not correspond to the closing bracket, the sequence is immediately
      deemed invalid. If it does match, the opening bracket is popped from the stack.
      Once the entire string is processed, the sequence is valid only if the stack is
      empty, meaning all opened brackets were successfully matched and closed.'
    time_complexity: O(n), where n is the length of the string s. The algorithm performs
      a single pass through the input string, and every character involves a constant
      time stack operation (either push or pop) and a lookup.
    space_complexity: O(n), where n is the length of the string s. In the worst-case
      scenario, such as a string consisting entirely of opening brackets, the stack
      will store all n characters.
    elapsed_time: 117.87984824180603
    model: gemini-3-flash-preview
    generated_at: '2026-10-01 03:26:31 '
---

## Problem #20: Valid Parentheses

**Difficulty:** Easy

**Topics:** String, Stack, Bracket Sequences

## Problem Description

<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()[]{}&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(]&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;([])&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;([)]&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>


## Hints

1. Use a stack of characters.

2. When you encounter an opening bracket, push it to the top of the stack.

3. When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm utilizes a stack data structure to track opening brackets as the string is traversed from left to right. When an opening bracket ('(', '{', or '[') is encountered, it is pushed onto the stack, ensuring that the most recently opened bracket is always at the top. This LIFO (Last-In-First-Out) behavior is essential because the last bracket opened must be the first one closed to satisfy a valid nested sequence.

When a closing bracket is encountered, the algorithm checks the top of the stack to see if it matches the current bracket's type. If the stack is empty or the top element does not correspond to the closing bracket, the sequence is immediately deemed invalid. If it does match, the opening bracket is popped from the stack. Once the entire string is processed, the sequence is valid only if the stack is empty, meaning all opened brackets were successfully matched and closed.

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
    bool isValid(string s) {
        std::stack<char> st;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else {
                if (st.empty()) return false;
                if (c == ')' && st.top() != '(') return false;
                if (c == '}' && st.top() != '{') return false;
                if (c == ']' && st.top() != '[') return false;
                st.pop();
            }
        }
        return st.empty();
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean isValid(String s) {
        java.util.Stack<Character> stack = new java.util.Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        return stack.isEmpty();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool isValid(char* s) {
    int n = 0;
    while (s[n]) n++;
    char stack[n + 1];
    int top = -1;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[++top] = s[i];
        } else {
            if (top == -1) return false;
            if ((s[i] == ')' && stack[top] != '(') ||
                (s[i] == '}' && stack[top] != '{') ||
                (s[i] == ']' && stack[top] != '[')) {
                return false;
            }
            top--;
        }
    }
    return top == -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool IsValid(string s) {
        System.Collections.Generic.Stack<char> stack = new System.Collections.Generic.Stack<char>();
        foreach (char c in s) {
            if (c == '(' || c == '{' || c == '[') {
                stack.Push(c);
            } else {
                if (stack.Count == 0) return false;
                char top = stack.Pop();
                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
        }
        return stack.Count == 0;
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
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    const mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (mapping[char]) {
            const topElement = stack.length === 0 ? '#' : stack.pop();
            if (mapping[char] !== topElement) {
                return false;
            }
        } else {
            stack.push(char);
        }
    }
    return stack.length === 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isValid(s: string): boolean {
    const stack: string[] = [];
    const mapping: { [key: string]: string } = {
        ')': '(',
        '}': '{',
        ']': '['
    };

    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (mapping[char]) {
            const topElement = stack.length === 0 ? '#' : stack.pop();
            if (topElement !== mapping[char]) {
                return false;
            }
        } else {
            stack.push(char);
        }
    }

    return stack.length === 0;
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
     * @return Boolean
     */
    function isValid($s) {
        $stack = [];
        $mapping = [
            ')' => '(',
            '}' => '{',
            ']' => '['
        ];

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $char = $s[$i];
            if (isset($mapping[$char])) {
                if (empty($stack) || array_pop($stack) !== $mapping[$char]) {
                    return false;
                }
            } else {
                array_push($stack, $char);
            }
        }

        return empty($stack);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func isValid(_ s: String) -> Bool {
        var stack = [Character]()
        let mapping: [Character: Character] = [
            ")": "(",
            "}": "{",
            "]": "["
        ]

        for char in s {
            if let openingBracket = mapping[char] {
                if stack.isEmpty || stack.removeLast() != openingBracket {
                    return false
                }
            } else {
                stack.append(char)
            }
        }

        return stack.isEmpty
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun isValid(s: String): Boolean {
        val stack = java.util.Stack<Char>()
        val mapping = mapOf(')' to '(', '}' to '{', ']' to '[')

        for (char in s) {
            if (mapping.containsKey(char)) {
                if (stack.isEmpty() || stack.pop() != mapping[char]) {
                    return false
                }
            } else {
                stack.push(char)
            }
        }

        return stack.isEmpty()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool isValid(String s) {
    List<String> stack = [];
    Map<String, String> mapping = {
      ')': '(',
      '}': '{',
      ']': '[',
    };

    for (int i = 0; i < s.length; i++) {
      String char = s[i];
      if (mapping.containsKey(char)) {
        if (stack.isEmpty || stack.removeLast() != mapping[char]) {
          return false;
        }
      } else {
        stack.add(char);
      }
    }

    return stack.isEmpty;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isValid(s string) bool {
    stack := []rune{}
    mapping := map[rune]rune{
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for _, char := range s {
        if opening, ok := mapping[char]; ok {
            if len(stack) == 0 || stack[len(stack)-1] != opening {
                return false
            }
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, char)
        }
    }

    return len(stack) == 0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Boolean}
def is_valid(s)
  stack = []
  pairs = { ')' => '(', ']' => '[', '}' => '{' }
  s.each_char do |c|
    if pairs.key?(c)
      return false if stack.pop != pairs[c]
    else
      stack.push(c)
    end
  end
  stack.empty?
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def isValid(s: String): Boolean = {
        val pairs = Map(')' -> '(', '}' -> '{', ']' -> '[')
        def solve(chars: List[Char], stack: List[Char]): Boolean = chars match {
            case Nil => stack.isEmpty
            case c :: rest =>
                if (pairs.contains(c)) {
                    if (stack.nonEmpty && stack.head == pairs(c)) solve(rest, stack.tail)
                    else false
                } else {
                    solve(rest, c :: stack)
                }
        }
        solve(s.toList, Nil)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        for c in s.chars() {
            match c {
                '(' | '[' | '{' => stack.push(c),
                ')' => if stack.pop() != Some('(') { return false; },
                ']' => if stack.pop() != Some('[') { return false; },
                '}' => if stack.pop() != Some('{') { return false; },
                _ => return false,
            }
        }
        stack.is_empty()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (is-valid s)
  (-> string? boolean?)
  (let loop ([chars (string->list s)]
             [stack '()])
    (if (null? chars)
        (null? stack)
        (let ([c (car chars)]
              [rest (cdr chars)])
          (cond
            [(char=? c #\() (loop rest (cons #\( stack))]
            [(char=? c #\[) (loop rest (cons #\[ stack))]
            [(char=? c #\{) (loop rest (cons #\{ stack))]
            [(and (not (null? stack)) (char=? c #\)) (char=? (car stack) #\()) (loop rest (cdr stack))]
            [(and (not (null? stack)) (char=? c #\]) (char=? (car stack) #\[)) (loop rest (cdr stack))]
            [(and (not (null? stack)) (char=? c #\}) (char=? (car stack) #\{)) (loop rest (cdr stack))]
            [else #f])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec is_valid(S :: unicode:unicode_binary()) -> boolean().
is_valid(S) ->
  is_valid_helper(binary_to_list(S), []).

is_valid_helper([], []) -> true;
is_valid_helper([], _) -> false;
is_valid_helper([$( | Rest], Stack) -> is_valid_helper(Rest, [$( | Stack]);
is_valid_helper([$[ | Rest], Stack) -> is_valid_helper(Rest, [$[ | Stack]);
is_valid_helper([${ | Rest], Stack) -> is_valid_helper(Rest, [${ | Stack]);
is_valid_helper([$) | Rest], [$( | Stack]) -> is_valid_helper(Rest, Stack);
is_valid_helper([$] | Rest], [$[ | Stack]) -> is_valid_helper(Rest, Stack);
is_valid_helper([$} | Rest], [${ | Stack]) -> is_valid_helper(Rest, Stack);
is_valid_helper(_, _) -> false.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec is_valid(s :: String.t) :: boolean
  def is_valid(s) do
    check(String.graphemes(s), [])
  end

  defp check([], []), do: true
  defp check([], _), do: false
  defp check([c | rest], stack) when c in ["(", "[", "{"] do
    check(rest, [c | stack])
  end
  defp check([")" | rest], ["(" | stack]), do: check(rest, stack)
  defp check(["]" | rest], ["[" | stack]), do: check(rest, stack)
  defp check(["}" | rest], ["{" | stack]), do: check(rest, stack)
  defp check(_, _), do: false
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string s. The algorithm performs a single pass through the input string, and every character involves a constant time stack operation (either push or pop) and a lookup.
- **Space Complexity:** O(n), where n is the length of the string s. In the worst-case scenario, such as a string consisting entirely of opening brackets, the stack will store all n characters.
