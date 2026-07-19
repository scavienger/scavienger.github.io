---
layout: post
title: "Smallest Subsequence of Distinct Characters"
date: 2026-07-19 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Stack", "Greedy", "Monotonic Stack"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
ai_solutions:
  - solutions:
      cpp: "#include <string>\n#include <vector>\n\nusing namespace std; \n\nclass Solution\
        \ {\npublic:\n    string smallestSubsequence(string s) {\n        int last[26]\
        \ = {0};\n        for (int i = 0; i < s.length(); i++) {\n            last[s[i]\
        \ - 'a'] = i;\n        }\n\n        string res = \"\";\n        bool seen[26]\
        \ = {false};\n\n        for (int i = 0; i < s.length(); i++) {\n           \
        \ int c = s[i] - 'a';\n            if (seen[c]) continue;\n\n            while\
        \ (!res.empty() && res.back() > s[i] && last[res.back() - 'a'] > i) {\n    \
        \            seen[res.back() - 'a'] = false;\n                res.pop_back();\n\
        \            }\n\n            res.push_back(s[i]);\n            seen[c] = true;\n\
        \        }\n\n        return res;\n    }\n};"
      java: "import java.util.Stack;\n\nclass Solution {\n    public String smallestSubsequence(String\
        \ s) {\n        int[] lastIdx = new int[26];\n        for (int i = 0; i < s.length();\
        \ i++) {\n            lastIdx[s.charAt(i) - 'a'] = i;\n        }\n\n       \
        \ boolean[] seen = new boolean[26];\n        Stack<Character> stack = new Stack<>();\n\
        \n        for (int i = 0; i < s.length(); i++) {\n            char curr = s.charAt(i);\n\
        \            if (seen[curr - 'a']) continue;\n\n            while (!stack.isEmpty()\
        \ && stack.peek() > curr && lastIdx[stack.peek() - 'a'] > i) {\n           \
        \     seen[stack.pop() - 'a'] = false;\n            }\n\n            stack.push(curr);\n\
        \            seen[curr - 'a'] = true;\n        }\n\n        StringBuilder sb\
        \ = new StringBuilder();\n        for (char c : stack) {\n            sb.append(c);\n\
        \        }\n\n        return sb.toString();\n    }\n}"
      python: "class Solution(object):\n    def smallestSubsequence(self, s):\n    \
        \    \"\"\"\n        :type s: str\n        :rtype: str\n        \"\"\"\n   \
        \     last_occurrence = {c: i for i, c in enumerate(s)}\n        stack = []\n\
        \        visited = set()\n\n        for i, char in enumerate(s):\n         \
        \   if char not in visited:\n                while stack and char < stack[-1]\
        \ and last_occurrence[stack[-1]] > i:\n                    visited.remove(stack.pop())\n\
        \                stack.append(char)\n                visited.add(char)\n\n \
        \       return \"\".join(stack)"
      python3: "class Solution:\n    def smallestSubsequence(self, s: str) -> str:\n\
        \        last_occurrence = {char: i for i, char in enumerate(s)}\n        stack\
        \ = []\n        visited = set()\n\n        for i, char in enumerate(s):\n  \
        \          if char not in visited:\n                while stack and char < stack[-1]\
        \ and last_occurrence[stack[-1]] > i:\n                    visited.remove(stack.pop())\n\
        \                stack.append(char)\n                visited.add(char)\n\n \
        \       return \"\".join(stack)"
      c: "#include <stdlib.h>\n#include <string.h>\n\nchar* smallestSubsequence(char*\
        \ s) {\n    int last[26] = {0};\n    int n = 0;\n    while (s[n]) {\n      \
        \  last[s[n] - 'a'] = n;\n        n++;\n    }\n\n    int seen[26] = {0};\n \
        \   char* stack = (char*)malloc(27 * sizeof(char));\n    int top = -1;\n\n \
        \   for (int i = 0; i < n; i++) {\n        int c = s[i] - 'a';\n        if (seen[c])\
        \ continue;\n\n        while (top >= 0 && stack[top] > s[i] && last[stack[top]\
        \ - 'a'] > i) {\n            seen[stack[top] - 'a'] = 0;\n            top--;\n\
        \        }\n\n        stack[++top] = s[i];\n        seen[c] = 1;\n    }\n\n\
        \    stack[++top] = '\\0';\n    return stack;\n}"
      csharp: "public class Solution {\n    public string SmallestSubsequence(string\
        \ s) {\n        int[] lastPos = new int[26];\n        for (int i = 0; i < s.Length;\
        \ i++) {\n            lastPos[s[i] - 'a'] = i;\n        }\n        char[] stack\
        \ = new char[26];\n        int top = -1;\n        bool[] seen = new bool[26];\n\
        \        for (int i = 0; i < s.Length; i++) {\n            char c = s[i];\n\
        \            int idx = c - 'a';\n            if (seen[idx]) continue;\n    \
        \        while (top >= 0 && stack[top] > c && lastPos[stack[top] - 'a'] > i)\
        \ {\n                seen[stack[top] - 'a'] = false;\n                top--;\n\
        \            }\n            stack[++top] = c;\n            seen[idx] = true;\n\
        \        }\n        return new string(stack, 0, top + 1);\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string}\n */\nvar smallestSubsequence\
        \ = function(s) {\n    let lastIdx = new Array(26).fill(0);\n    for (let i\
        \ = 0; i < s.length; i++) {\n        lastIdx[s.charCodeAt(i) - 97] = i;\n  \
        \  }\n    let stack = [];\n    let seen = new Array(26).fill(false);\n    for\
        \ (let i = 0; i < s.length; i++) {\n        let char = s[i];\n        let code\
        \ = char.charCodeAt(0) - 97;\n        if (seen[code]) continue;\n        while\
        \ (stack.length > 0 && stack[stack.length - 1] > char && lastIdx[stack[stack.length\
        \ - 1].charCodeAt(0) - 97] > i) {\n            let poppedChar = stack.pop();\n\
        \            seen[poppedChar.charCodeAt(0) - 97] = false;\n        }\n     \
        \   stack.push(char);\n        seen[code] = true;\n    }\n    return stack.join('');\n\
        };"
      typescript: "function smallestSubsequence(s: string): string {\n    const lastIdx:\
        \ number[] = new Array(26).fill(0);\n    for (let i = 0; i < s.length; i++)\
        \ {\n        lastIdx[s.charCodeAt(i) - 97] = i;\n    }\n    const stack: string[]\
        \ = [];\n    const seen: boolean[] = new Array(26).fill(false);\n    for (let\
        \ i = 0; i < s.length; i++) {\n        const char = s[i];\n        const code\
        \ = char.charCodeAt(0) - 97;\n        if (seen[code]) continue;\n        while\
        \ (stack.length > 0 && stack[stack.length - 1] > char && lastIdx[stack[stack.length\
        \ - 1].charCodeAt(0) - 97] > i) {\n            const poppedChar = stack.pop()!;\n\
        \            seen[poppedChar.charCodeAt(0) - 97] = false;\n        }\n     \
        \   stack.push(char);\n        seen[code] = true;\n    }\n    return stack.join('');\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String\n\
        \     */\n    function smallestSubsequence($s) {\n        $lastPos = [];\n \
        \       $n = strlen($s);\n        for ($i = 0; $i < $n; $i++) {\n          \
        \  $lastPos[$s[$i]] = $i;\n        }\n        $stack = [];\n        $seen =\
        \ [];\n        for ($i = 0; $i < $n; $i++) {\n            $c = $s[$i];\n   \
        \         if (isset($seen[$c]) && $seen[$c]) continue;\n            while (!empty($stack)\
        \ && end($stack) > $c && $lastPos[end($stack)] > $i) {\n                $top\
        \ = array_pop($stack);\n                $seen[$top] = false;\n            }\n\
        \            $stack[] = $c;\n            $seen[$c] = true;\n        }\n    \
        \    return implode('', $stack);\n    }\n}"
      swift: "class Solution {\n    func smallestSubsequence(_ s: String) -> String\
        \ {\n        var lastIdx = [Character: Int]()\n        let chars = Array(s)\n\
        \        for i in 0..<chars.count {\n            lastIdx[chars[i]] = i\n   \
        \     }\n        var stack = [Character]()\n        var seen = Set<Character>()\n\
        \        for i in 0..<chars.count {\n            let char = chars[i]\n     \
        \       if seen.contains(char) { continue }\n            while let last = stack.last,\
        \ last > char, let pos = lastIdx[last], pos > i {\n                let removed\
        \ = stack.removeLast()\n                seen.remove(removed)\n            }\n\
        \            stack.append(char)\n            seen.insert(char)\n        }\n\
        \        return String(stack)\n    }\n}"
      kotlin: "class Solution {\n    fun smallestSubsequence(s: String): String {\n\
        \        val lastIndex = IntArray(26)\n        for (i in 0 until s.length) {\n\
        \            lastIndex[s[i] - 'a'] = i\n        }\n        val stack = StringBuilder()\n\
        \        val seen = BooleanArray(26)\n        for (i in 0 until s.length) {\n\
        \            val c = s[i]\n            if (seen[c - 'a']) continue\n       \
        \     while (stack.length > 0 && stack[stack.length - 1] > c && lastIndex[stack[stack.length\
        \ - 1] - 'a'] > i) {\n                seen[stack[stack.length - 1] - 'a'] =\
        \ false\n                stack.deleteCharAt(stack.length - 1)\n            }\n\
        \            stack.append(c)\n            seen[c - 'a'] = true\n        }\n\
        \        return stack.toString()\n    }\n}"
      dart: "class Solution {\n  String smallestSubsequence(String s) {\n    List<int>\
        \ lastIndex = List.filled(26, 0);\n    for (int i = 0; i < s.length; i++) {\n\
        \      lastIndex[s.codeUnitAt(i) - 97] = i;\n    }\n    List<String> stack =\
        \ [];\n    List<bool> seen = List.filled(26, false);\n    for (int i = 0; i\
        \ < s.length; i++) {\n      String char = s[i];\n      int charIdx = s.codeUnitAt(i)\
        \ - 97;\n      if (seen[charIdx]) continue;\n      while (stack.isNotEmpty &&\n\
        \          stack.last.compareTo(char) > 0 &&\n          lastIndex[stack.last.codeUnitAt(0)\
        \ - 97] > i) {\n        seen[stack.last.codeUnitAt(0) - 97] = false;\n     \
        \   stack.removeLast();\n      }\n      stack.add(char);\n      seen[charIdx]\
        \ = true;\n    }\n    return stack.join('');\n  }\n}"
      go: "func smallestSubsequence(s string) string {\n    lastIndex := [26]int{}\n\
        \    for i := 0; i < len(s); i++ {\n        lastIndex[s[i]-'a'] = i\n    }\n\
        \    seen := [26]bool{}\n    stack := []byte{}\n    for i := 0; i < len(s);\
        \ i++ {\n        char := s[i]\n        if !seen[char-'a'] {\n            for\
        \ len(stack) > 0 && stack[len(stack)-1] > char && lastIndex[stack[len(stack)-1]-'a']\
        \ > i {\n                seen[stack[len(stack)-1]-'a'] = false\n           \
        \     stack = stack[:len(stack)-1]\n            }\n            stack = append(stack,\
        \ char)\n            seen[char-'a'] = true\n        }\n    }\n    return string(stack)\n\
        }"
      ruby: "# @param {String} s\n# @return {String}\ndef smallest_subsequence(s)\n\
        \  last_index = {}\n  s.each_char.with_index { |char, i| last_index[char] =\
        \ i }\n  stack = []\n  seen = {}\n  s.each_char.with_index do |char, i|\n  \
        \  if !seen[char]\n      while !stack.empty? && stack[-1] > char && last_index[stack[-1]]\
        \ > i\n        seen.delete(stack.pop)\n      end\n      stack.push(char)\n \
        \     seen[char] = true\n    end\n  end\n  stack.join\nend"
      scala: "object Solution {\n    def smallestSubsequence(s: String): String = {\n\
        \        val lastIndex = Array.fill(26)(0)\n        for (i <- 0 until s.length)\
        \ {\n            lastIndex(s(i) - 'a') = i\n        }\n        val stack = new\
        \ scala.collection.mutable.ListBuffer[Char]()\n        val seen = Array.fill(26)(false)\n\
        \        for (i <- 0 until s.length) {\n            val c = s(i)\n         \
        \   if (!seen(c - 'a')) {\n                while (stack.nonEmpty && stack.last\
        \ > c && lastIndex(stack.last - 'a') > i) {\n                    val lastChar\
        \ = stack.remove(stack.length - 1)\n                    seen(lastChar - 'a')\
        \ = false\n                }\n                stack.append(c)\n            \
        \    seen(c - 'a') = true\n            }\n        }\n        stack.mkString\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn smallest_subsequence(s: String) -> String {\n\
        \        let mut last_occurrence = [0; 26];\n        let bytes = s.as_bytes();\n\
        \        for (i, &b) in bytes.iter().enumerate() {\n            last_occurrence[(b\
        \ - b'a') as usize] = i;\n        }\n        let mut stack: Vec<u8> = Vec::new();\n\
        \        let mut visited = [false; 26];\n        for (i, &b) in bytes.iter().enumerate()\
        \ {\n            let idx = (b - b'a') as usize;\n            if !visited[idx]\
        \ {\n                while let Some(&top_b) = stack.last() {\n             \
        \       let top_idx = (top_b - b'a') as usize;\n                    if top_b\
        \ > b && last_occurrence[top_idx] > i {\n                        visited[top_idx]\
        \ = false;\n                        stack.pop();\n                    } else\
        \ {\n                        break;\n                    }\n               \
        \ }\n                stack.push(b);\n                visited[idx] = true;\n\
        \            }\n        }\n        String::from_utf8(stack).unwrap()\n    }\n\
        }"
      racket: "(define/contract (smallest-subsequence s)\n  (-> string? string?)\n \
        \ (let* ([chars (string->list s)]\n         [last-idx (make-hasheqv)]\n    \
        \     [n (length chars)])\n    (for ([c chars] [i (in-range n)])\n      (hash-set!\
        \ last-idx c i))\n    (let loop ([i 0] [curr chars] [stack '()] [seen (set)])\n\
        \      (if (null? curr)\n          (list->string (reverse stack))\n        \
        \  (let ([c (car curr)])\n            (if (set-member? seen c)\n           \
        \     (loop (+ i 1) (cdr curr) stack seen)\n                (let pop-loop ([stk\
        \ stack] [sn seen])\n                  (if (and (not (null? stk))\n        \
        \                   (char>? (car stk) c)\n                           (> (hash-ref\
        \ last-idx (car stk)) i))\n                      (pop-loop (cdr stk) (set-remove\
        \ sn (car stk)))\n                      (loop (+ i 1) (cdr curr) (cons c stk)\
        \ (set-add sn c))))))))))"
      erlang: "-spec smallest_subsequence(S :: unicode:unicode_binary()) -> unicode:unicode_binary().\n\
        smallest_subsequence(S) ->\n  List = binary_to_list(S),\n  Indices = lists:seq(0,\
        \ length(List) - 1),\n  Zipped = lists:zip(List, Indices),\n  LastIdxMap = maps:from_list(Zipped),\n\
        \  FinalStack = process_chars(List, 0, [], sets:new(), LastIdxMap),\n  unicode:characters_to_binary(lists:reverse(FinalStack)).\n\
        \nprocess_chars([], _Idx, Stack, _Seen, _LastIdxMap) ->\n  Stack;\nprocess_chars([Char\
        \ | Rest], Idx, Stack, Seen, LastIdxMap) ->\n  case sets:is_element(Char, Seen)\
        \ of\n    true ->\n      process_chars(Rest, Idx + 1, Stack, Seen, LastIdxMap);\n\
        \    false ->\n      {NewStack, NewSeen} = pop_stack(Char, Idx, Stack, Seen,\
        \ LastIdxMap),\n      process_chars(Rest, Idx + 1, [Char | NewStack], sets:add_element(Char,\
        \ NewSeen), LastIdxMap)\n  end.\n\npop_stack(_Char, _Idx, [], Seen, _LastIdxMap)\
        \ ->\n  {[], Seen};\npop_stack(Char, Idx, [Top | RestStack] = Stack, Seen, LastIdxMap)\
        \ ->\n  TopLastIdx = maps:get(Top, LastIdxMap),\n  case (Top > Char) andalso\
        \ (TopLastIdx > Idx) of\n    true ->\n      pop_stack(Char, Idx, RestStack,\
        \ sets:del_element(Top, Seen), LastIdxMap);\n    false ->\n      {Stack, Seen}\n\
        \  end."
      elixir: "defmodule Solution do\n  @spec smallest_subsequence(s :: String.t) ::\
        \ String.t\n  def smallest_subsequence(s) do\n    chars = String.to_charlist(s)\n\
        \    last_idx = chars\n               |> Enum.with_index()\n               |>\
        \ Enum.reduce(%{}, fn {c, i}, acc -> Map.put(acc, c, i) end)\n\n    stack =\
        \ process(chars, 0, [], MapSet.new(), last_idx)\n    List.to_string(Enum.reverse(stack))\n\
        \  end\n\n  defp process([], _idx, stack, _seen, _last_idx), do: stack\n  defp\
        \ process([char | rest], idx, stack, seen, last_idx) do\n    if MapSet.member?(seen,\
        \ char) do\n      process(rest, idx + 1, stack, seen, last_idx)\n    else\n\
        \      {new_stack, new_seen} = pop_stack(char, idx, stack, seen, last_idx)\n\
        \      process(rest, idx + 1, [char | new_stack], MapSet.put(new_seen, char),\
        \ last_idx)\n    end\n  end\n\n  defp pop_stack(_char, _idx, [], seen, _last_idx),\
        \ do: {[], seen}\n  defp pop_stack(char, idx, [top | rest] = stack, seen, last_idx)\
        \ do\n    if top > char and Map.get(last_idx, top) > idx do\n      pop_stack(char,\
        \ idx, rest, MapSet.delete(seen, top), last_idx)\n    else\n      {stack, seen}\n\
        \    end\n  end\nend"
    approach: 'The problem is solved using a monotonic stack combined with a greedy
      approach. We first iterate through the input string to record the last occurrence
      index of each distinct character. This information is crucial because it allows
      us to decide whether a character can be removed from our current stack and safely
      re-added later without permanently losing it from the final subsequence.


      As we iterate through the string a second time, we build the resulting subsequence
      by maintaining a stack of characters. For each character in the string, if it
      is already in our stack, we skip it. Otherwise, we compare it with the character
      at the top of the stack. If the top character is lexicographically larger than
      the current character and the top character appears again later in the string
      (based on our precomputed indices), we pop the top character and mark it as not
      seen. We repeat this process before pushing the current character onto the stack
      and marking it as seen, ensuring the lexicographically smallest result.'
    time_complexity: O(N), where N is the length of the input string s. We perform one
      pass to map characters to their last indices and another pass to iterate through
      the string to build the stack. Since each character is pushed and popped from
      the stack at most once, and the operations inside the loop are O(1), the overall
      time complexity is linear.
    space_complexity: O(1), as the extra space used for the stack, the last-occurrence
      array, and the existence tracking (seen array or set) is bounded by the size of
      the alphabet, which is 26 for lowercase English letters. This constant bound means
      the space complexity does not scale with the length of the input string.
    elapsed_time: 170.60576128959656
    model: gemini-3-flash-preview
    generated_at: '2026-07-19 02:00:10 '
---

## Problem #1081: Smallest Subsequence of Distinct Characters

**Difficulty:** Medium

**Topics:** String, Stack, Greedy, Monotonic Stack

## Problem Description

<p>Given a string <code>s</code>, return <em>the </em><span data-keyword="lexicographically-smaller-string"><em>lexicographically smallest</em></span> <span data-keyword="subsequence-string"><em>subsequence</em></span><em> of</em> <code>s</code> <em>that contains all the distinct characters of</em> <code>s</code> <em>exactly once</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bcabc&quot;
<strong>Output:</strong> &quot;abc&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbacdcbc&quot;
<strong>Output:</strong> &quot;acdb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Note:</strong> This question is the same as 316: <a href="https://leetcode.com/problems/remove-duplicate-letters/" target="_blank">https://leetcode.com/problems/remove-duplicate-letters/</a>

## Hints

1. Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using a monotonic stack combined with a greedy approach. We first iterate through the input string to record the last occurrence index of each distinct character. This information is crucial because it allows us to decide whether a character can be removed from our current stack and safely re-added later without permanently losing it from the final subsequence.

As we iterate through the string a second time, we build the resulting subsequence by maintaining a stack of characters. For each character in the string, if it is already in our stack, we skip it. Otherwise, we compare it with the character at the top of the stack. If the top character is lexicographically larger than the current character and the top character appears again later in the string (based on our precomputed indices), we pop the top character and mark it as not seen. We repeat this process before pushing the current character onto the stack and marking it as seen, ensuring the lexicographically smallest result.

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
#include <string>
#include <vector>

using namespace std; 

class Solution {
public:
    string smallestSubsequence(string s) {
        int last[26] = {0};
        for (int i = 0; i < s.length(); i++) {
            last[s[i] - 'a'] = i;
        }

        string res = "";
        bool seen[26] = {false};

        for (int i = 0; i < s.length(); i++) {
            int c = s[i] - 'a';
            if (seen[c]) continue;

            while (!res.empty() && res.back() > s[i] && last[res.back() - 'a'] > i) {
                seen[res.back() - 'a'] = false;
                res.pop_back();
            }

            res.push_back(s[i]);
            seen[c] = true;
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
import java.util.Stack;

class Solution {
    public String smallestSubsequence(String s) {
        int[] lastIdx = new int[26];
        for (int i = 0; i < s.length(); i++) {
            lastIdx[s.charAt(i) - 'a'] = i;
        }

        boolean[] seen = new boolean[26];
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (seen[curr - 'a']) continue;

            while (!stack.isEmpty() && stack.peek() > curr && lastIdx[stack.peek() - 'a'] > i) {
                seen[stack.pop() - 'a'] = false;
            }

            stack.push(curr);
            seen[curr - 'a'] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }

        return sb.toString();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        visited = set()

        for i, char in enumerate(s):
            if char not in visited:
                while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)

        return "".join(stack)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        visited = set()

        for i, char in enumerate(s):
            if char not in visited:
                while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)

        return "".join(stack)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

char* smallestSubsequence(char* s) {
    int last[26] = {0};
    int n = 0;
    while (s[n]) {
        last[s[n] - 'a'] = n;
        n++;
    }

    int seen[26] = {0};
    char* stack = (char*)malloc(27 * sizeof(char));
    int top = -1;

    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        if (seen[c]) continue;

        while (top >= 0 && stack[top] > s[i] && last[stack[top] - 'a'] > i) {
            seen[stack[top] - 'a'] = 0;
            top--;
        }

        stack[++top] = s[i];
        seen[c] = 1;
    }

    stack[++top] = '\0';
    return stack;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string SmallestSubsequence(string s) {
        int[] lastPos = new int[26];
        for (int i = 0; i < s.Length; i++) {
            lastPos[s[i] - 'a'] = i;
        }
        char[] stack = new char[26];
        int top = -1;
        bool[] seen = new bool[26];
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            int idx = c - 'a';
            if (seen[idx]) continue;
            while (top >= 0 && stack[top] > c && lastPos[stack[top] - 'a'] > i) {
                seen[stack[top] - 'a'] = false;
                top--;
            }
            stack[++top] = c;
            seen[idx] = true;
        }
        return new string(stack, 0, top + 1);
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
var smallestSubsequence = function(s) {
    let lastIdx = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        lastIdx[s.charCodeAt(i) - 97] = i;
    }
    let stack = [];
    let seen = new Array(26).fill(false);
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        let code = char.charCodeAt(0) - 97;
        if (seen[code]) continue;
        while (stack.length > 0 && stack[stack.length - 1] > char && lastIdx[stack[stack.length - 1].charCodeAt(0) - 97] > i) {
            let poppedChar = stack.pop();
            seen[poppedChar.charCodeAt(0) - 97] = false;
        }
        stack.push(char);
        seen[code] = true;
    }
    return stack.join('');
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function smallestSubsequence(s: string): string {
    const lastIdx: number[] = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        lastIdx[s.charCodeAt(i) - 97] = i;
    }
    const stack: string[] = [];
    const seen: boolean[] = new Array(26).fill(false);
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        const code = char.charCodeAt(0) - 97;
        if (seen[code]) continue;
        while (stack.length > 0 && stack[stack.length - 1] > char && lastIdx[stack[stack.length - 1].charCodeAt(0) - 97] > i) {
            const poppedChar = stack.pop()!;
            seen[poppedChar.charCodeAt(0) - 97] = false;
        }
        stack.push(char);
        seen[code] = true;
    }
    return stack.join('');
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
    function smallestSubsequence($s) {
        $lastPos = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $lastPos[$s[$i]] = $i;
        }
        $stack = [];
        $seen = [];
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (isset($seen[$c]) && $seen[$c]) continue;
            while (!empty($stack) && end($stack) > $c && $lastPos[end($stack)] > $i) {
                $top = array_pop($stack);
                $seen[$top] = false;
            }
            $stack[] = $c;
            $seen[$c] = true;
        }
        return implode('', $stack);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func smallestSubsequence(_ s: String) -> String {
        var lastIdx = [Character: Int]()
        let chars = Array(s)
        for i in 0..<chars.count {
            lastIdx[chars[i]] = i
        }
        var stack = [Character]()
        var seen = Set<Character>()
        for i in 0..<chars.count {
            let char = chars[i]
            if seen.contains(char) { continue }
            while let last = stack.last, last > char, let pos = lastIdx[last], pos > i {
                let removed = stack.removeLast()
                seen.remove(removed)
            }
            stack.append(char)
            seen.insert(char)
        }
        return String(stack)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun smallestSubsequence(s: String): String {
        val lastIndex = IntArray(26)
        for (i in 0 until s.length) {
            lastIndex[s[i] - 'a'] = i
        }
        val stack = StringBuilder()
        val seen = BooleanArray(26)
        for (i in 0 until s.length) {
            val c = s[i]
            if (seen[c - 'a']) continue
            while (stack.length > 0 && stack[stack.length - 1] > c && lastIndex[stack[stack.length - 1] - 'a'] > i) {
                seen[stack[stack.length - 1] - 'a'] = false
                stack.deleteCharAt(stack.length - 1)
            }
            stack.append(c)
            seen[c - 'a'] = true
        }
        return stack.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String smallestSubsequence(String s) {
    List<int> lastIndex = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      lastIndex[s.codeUnitAt(i) - 97] = i;
    }
    List<String> stack = [];
    List<bool> seen = List.filled(26, false);
    for (int i = 0; i < s.length; i++) {
      String char = s[i];
      int charIdx = s.codeUnitAt(i) - 97;
      if (seen[charIdx]) continue;
      while (stack.isNotEmpty &&
          stack.last.compareTo(char) > 0 &&
          lastIndex[stack.last.codeUnitAt(0) - 97] > i) {
        seen[stack.last.codeUnitAt(0) - 97] = false;
        stack.removeLast();
      }
      stack.add(char);
      seen[charIdx] = true;
    }
    return stack.join('');
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func smallestSubsequence(s string) string {
    lastIndex := [26]int{}
    for i := 0; i < len(s); i++ {
        lastIndex[s[i]-'a'] = i
    }
    seen := [26]bool{}
    stack := []byte{}
    for i := 0; i < len(s); i++ {
        char := s[i]
        if !seen[char-'a'] {
            for len(stack) > 0 && stack[len(stack)-1] > char && lastIndex[stack[len(stack)-1]-'a'] > i {
                seen[stack[len(stack)-1]-'a'] = false
                stack = stack[:len(stack)-1]
            }
            stack = append(stack, char)
            seen[char-'a'] = true
        }
    }
    return string(stack)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {String}
def smallest_subsequence(s)
  last_index = {}
  s.each_char.with_index { |char, i| last_index[char] = i }
  stack = []
  seen = {}
  s.each_char.with_index do |char, i|
    if !seen[char]
      while !stack.empty? && stack[-1] > char && last_index[stack[-1]] > i
        seen.delete(stack.pop)
      end
      stack.push(char)
      seen[char] = true
    end
  end
  stack.join
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def smallestSubsequence(s: String): String = {
        val lastIndex = Array.fill(26)(0)
        for (i <- 0 until s.length) {
            lastIndex(s(i) - 'a') = i
        }
        val stack = new scala.collection.mutable.ListBuffer[Char]()
        val seen = Array.fill(26)(false)
        for (i <- 0 until s.length) {
            val c = s(i)
            if (!seen(c - 'a')) {
                while (stack.nonEmpty && stack.last > c && lastIndex(stack.last - 'a') > i) {
                    val lastChar = stack.remove(stack.length - 1)
                    seen(lastChar - 'a') = false
                }
                stack.append(c)
                seen(c - 'a') = true
            }
        }
        stack.mkString
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn smallest_subsequence(s: String) -> String {
        let mut last_occurrence = [0; 26];
        let bytes = s.as_bytes();
        for (i, &b) in bytes.iter().enumerate() {
            last_occurrence[(b - b'a') as usize] = i;
        }
        let mut stack: Vec<u8> = Vec::new();
        let mut visited = [false; 26];
        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            if !visited[idx] {
                while let Some(&top_b) = stack.last() {
                    let top_idx = (top_b - b'a') as usize;
                    if top_b > b && last_occurrence[top_idx] > i {
                        visited[top_idx] = false;
                        stack.pop();
                    } else {
                        break;
                    }
                }
                stack.push(b);
                visited[idx] = true;
            }
        }
        String::from_utf8(stack).unwrap()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-subsequence s)
  (-> string? string?)
  (let* ([chars (string->list s)]
         [last-idx (make-hasheqv)]
         [n (length chars)])
    (for ([c chars] [i (in-range n)])
      (hash-set! last-idx c i))
    (let loop ([i 0] [curr chars] [stack '()] [seen (set)])
      (if (null? curr)
          (list->string (reverse stack))
          (let ([c (car curr)])
            (if (set-member? seen c)
                (loop (+ i 1) (cdr curr) stack seen)
                (let pop-loop ([stk stack] [sn seen])
                  (if (and (not (null? stk))
                           (char>? (car stk) c)
                           (> (hash-ref last-idx (car stk)) i))
                      (pop-loop (cdr stk) (set-remove sn (car stk)))
                      (loop (+ i 1) (cdr curr) (cons c stk) (set-add sn c))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_subsequence(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_subsequence(S) ->
  List = binary_to_list(S),
  Indices = lists:seq(0, length(List) - 1),
  Zipped = lists:zip(List, Indices),
  LastIdxMap = maps:from_list(Zipped),
  FinalStack = process_chars(List, 0, [], sets:new(), LastIdxMap),
  unicode:characters_to_binary(lists:reverse(FinalStack)).

process_chars([], _Idx, Stack, _Seen, _LastIdxMap) ->
  Stack;
process_chars([Char | Rest], Idx, Stack, Seen, LastIdxMap) ->
  case sets:is_element(Char, Seen) of
    true ->
      process_chars(Rest, Idx + 1, Stack, Seen, LastIdxMap);
    false ->
      {NewStack, NewSeen} = pop_stack(Char, Idx, Stack, Seen, LastIdxMap),
      process_chars(Rest, Idx + 1, [Char | NewStack], sets:add_element(Char, NewSeen), LastIdxMap)
  end.

pop_stack(_Char, _Idx, [], Seen, _LastIdxMap) ->
  {[], Seen};
pop_stack(Char, Idx, [Top | RestStack] = Stack, Seen, LastIdxMap) ->
  TopLastIdx = maps:get(Top, LastIdxMap),
  case (Top > Char) andalso (TopLastIdx > Idx) of
    true ->
      pop_stack(Char, Idx, RestStack, sets:del_element(Top, Seen), LastIdxMap);
    false ->
      {Stack, Seen}
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_subsequence(s :: String.t) :: String.t
  def smallest_subsequence(s) do
    chars = String.to_charlist(s)
    last_idx = chars
               |> Enum.with_index()
               |> Enum.reduce(%{}, fn {c, i}, acc -> Map.put(acc, c, i) end)

    stack = process(chars, 0, [], MapSet.new(), last_idx)
    List.to_string(Enum.reverse(stack))
  end

  defp process([], _idx, stack, _seen, _last_idx), do: stack
  defp process([char | rest], idx, stack, seen, last_idx) do
    if MapSet.member?(seen, char) do
      process(rest, idx + 1, stack, seen, last_idx)
    else
      {new_stack, new_seen} = pop_stack(char, idx, stack, seen, last_idx)
      process(rest, idx + 1, [char | new_stack], MapSet.put(new_seen, char), last_idx)
    end
  end

  defp pop_stack(_char, _idx, [], seen, _last_idx), do: {[], seen}
  defp pop_stack(char, idx, [top | rest] = stack, seen, last_idx) do
    if top > char and Map.get(last_idx, top) > idx do
      pop_stack(char, idx, rest, MapSet.delete(seen, top), last_idx)
    else
      {stack, seen}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the input string s. We perform one pass to map characters to their last indices and another pass to iterate through the string to build the stack. Since each character is pushed and popped from the stack at most once, and the operations inside the loop are O(1), the overall time complexity is linear.
- **Space Complexity:** O(1), as the extra space used for the stack, the last-occurrence array, and the existence tracking (seen array or set) is bounded by the size of the alphabet, which is 26 for lowercase English letters. This constant bound means the space complexity does not scale with the length of the input string.
