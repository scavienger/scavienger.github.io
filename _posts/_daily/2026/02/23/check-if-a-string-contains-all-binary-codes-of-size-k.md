---
layout: post
title: "Check If a String Contains All Binary Codes of Size K"
date: 2026-02-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Bit Manipulation", "Rolling Hash", "Hash Function"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool hasAllCodes(string s, int k) {\n   \
        \     int n = s.length();\n        int total = 1 << k;\n        if (n < k ||\
        \ n - k + 1 < total) return false;\n\n        vector<bool> seen(total, false);\n\
        \        int current = 0;\n        int mask = total - 1;\n        int count\
        \ = 0;\n\n        for (int i = 0; i < n; ++i) {\n            current = ((current\
        \ << 1) & mask) | (s[i] - '0');\n            if (i >= k - 1) {\n           \
        \     if (!seen[current]) {\n                    seen[current] = true;\n   \
        \                 count++;\n                    if (count == total) return true;\n\
        \                }\n            }\n        }\n        return false;\n    }\n\
        };"
      java: "class Solution {\n    public boolean hasAllCodes(String s, int k) {\n \
        \       int n = s.length();\n        int total = 1 << k;\n        if (n < k\
        \ || n - k + 1 < total) return false;\n\n        boolean[] seen = new boolean[total];\n\
        \        int current = 0;\n        int mask = total - 1;\n        int count\
        \ = 0;\n\n        for (int i = 0; i < n; i++) {\n            current = ((current\
        \ << 1) & mask) | (s.charAt(i) - '0');\n            if (i >= k - 1) {\n    \
        \            if (!seen[current]) {\n                    seen[current] = true;\n\
        \                    count++;\n                    if (count == total) return\
        \ true;\n                }\n            }\n        }\n        return false;\n\
        \    }\n}"
      python: "class Solution(object):\n    def hasAllCodes(self, s, k):\n        \"\
        \"\"\n        :type s: str\n        :type k: int\n        :rtype: bool\n   \
        \     \"\"\"\n        total = 1 << k\n        if len(s) - k + 1 < total:\n \
        \           return False\n\n        seen = set()\n        for i in range(len(s)\
        \ - k + 1):\n            seen.add(s[i:i+k])\n            if len(seen) == total:\n\
        \                return True\n        return False"
      python3: "class Solution:\n    def hasAllCodes(self, s: str, k: int) -> bool:\n\
        \        total = 1 << k\n        if len(s) - k + 1 < total:\n            return\
        \ False\n\n        seen = set()\n        for i in range(len(s) - k + 1):\n \
        \           seen.add(s[i:i+k])\n            if len(seen) == total:\n       \
        \         return True\n        return False"
      c: "#include <stdbool.h>\n#include <string.h>\n#include <stdlib.h>\n\nbool hasAllCodes(char*\
        \ s, int k) {\n    int n = strlen(s);\n    if (k > 20) return false;\n    int\
        \ total = 1 << k;\n    if (n < k || n - k + 1 < total) return false;\n\n   \
        \ bool* seen = (bool*)calloc(total, sizeof(bool));\n    if (!seen) return false;\n\
        \n    int current = 0;\n    int mask = total - 1;\n    int count = 0;\n\n  \
        \  for (int i = 0; i < n; i++) {\n        current = ((current << 1) & mask)\
        \ | (s[i] - '0');\n        if (i >= k - 1) {\n            if (!seen[current])\
        \ {\n                seen[current] = true;\n                count++;\n     \
        \           if (count == total) {\n                    free(seen);\n       \
        \             return true;\n                }\n            }\n        }\n  \
        \  }\n\n    free(seen);\n    return false;\n}"
      csharp: "public class Solution {\n    public bool HasAllCodes(string s, int k)\
        \ {\n        int n = s.Length;\n        int total = 1 << k;\n        if (n <\
        \ k || n - k + 1 < total) return false;\n\n        bool[] seen = new bool[total];\n\
        \        int current = 0;\n        int mask = total - 1;\n        int count\
        \ = 0;\n\n        for (int i = 0; i < n; i++) {\n            current = ((current\
        \ << 1) & mask) | (s[i] - '0');\n            if (i >= k - 1) {\n           \
        \     if (!seen[current]) {\n                    seen[current] = true;\n   \
        \                 count++;\n                    if (count == total) return true;\n\
        \                }\n            }\n        }\n        return false;\n    }\n\
        }"
      javascript: "/**\n * @param {string} s\n * @param {number} k\n * @return {boolean}\n\
        \ */\nvar hasAllCodes = function(s, k) {\n    const total = 1 << k;\n    if\
        \ (s.length - k + 1 < total) return false;\n\n    const seen = new Set();\n\
        \    for (let i = 0; i <= s.length - k; i++) {\n        seen.add(s.substring(i,\
        \ i + k));\n        if (seen.size === total) return true;\n    }\n    return\
        \ false;\n};"
      typescript: "function hasAllCodes(s: string, k: number): boolean {\n    const\
        \ total = 1 << k;\n    const n = s.length;\n    if (n < total + k - 1) return\
        \ false;\n\n    const seen = new Uint8Array(total);\n    let count = 0;\n  \
        \  let currentVal = 0;\n    const mask = total - 1;\n\n    for (let i = 0; i\
        \ < n; i++) {\n        currentVal = ((currentVal << 1) & mask) | (s[i] === '1'\
        \ ? 1 : 0);\n        if (i >= k - 1) {\n            if (seen[currentVal] ===\
        \ 0) {\n                seen[currentVal] = 1;\n                count++;\n  \
        \              if (count === total) return true;\n            }\n        }\n\
        \    }\n    return count === total;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return Boolean\n     */\n    function hasAllCodes($s, $k) {\n\
        \        $total = 1 << $k;\n        $n = strlen($s);\n        if ($n < $total\
        \ + $k - 1) return false;\n\n        $seen = array_fill(0, $total, false);\n\
        \        $count = 0;\n        $currentVal = 0;\n        $mask = $total - 1;\n\
        \n        for ($i = 0; $i < $n; $i++) {\n            $currentVal = (($currentVal\
        \ << 1) & $mask) | ($s[$i] === '1' ? 1 : 0);\n            if ($i >= $k - 1)\
        \ {\n                if (!$seen[$currentVal]) {\n                    $seen[$currentVal]\
        \ = true;\n                    $count++;\n                    if ($count ==\
        \ $total) return true;\n                }\n            }\n        }\n      \
        \  return $count == $total;\n    }\n}"
      swift: "class Solution {\n    func hasAllCodes(_ s: String, _ k: Int) -> Bool\
        \ {\n        let utf8 = Array(s.utf8)\n        let n = utf8.count\n        let\
        \ total = 1 << k\n        if n < total + k - 1 { return false }\n\n        var\
        \ seen = Array(repeating: false, count: total)\n        var count = 0\n    \
        \    var currentVal = 0\n        let mask = total - 1\n\n        for i in 0..<n\
        \ {\n            currentVal = ((currentVal << 1) & mask) | Int(utf8[i] & 1)\n\
        \            if i >= k - 1 {\n                if !seen[currentVal] {\n     \
        \               seen[currentVal] = true\n                    count += 1\n  \
        \                  if count == total { return true }\n                }\n  \
        \          }\n        }\n        return count == total\n    }\n}"
      kotlin: "class Solution {\n    fun hasAllCodes(s: String, k: Int): Boolean {\n\
        \        val total = 1 shl k\n        val n = s.length\n        if (n < total\
        \ + k - 1) return false\n\n        val seen = BooleanArray(total)\n        var\
        \ count = 0\n        var currentVal = 0\n        val mask = total - 1\n\n  \
        \      for (i in 0 until n) {\n            currentVal = ((currentVal shl 1)\
        \ and mask) or (if (s[i] == '1') 1 else 0)\n            if (i >= k - 1) {\n\
        \                if (!seen[currentVal]) {\n                    seen[currentVal]\
        \ = true\n                    count++\n                    if (count == total)\
        \ return true\n                }\n            }\n        }\n        return count\
        \ == total\n    }\n}"
      dart: "class Solution {\n  bool hasAllCodes(String s, int k) {\n    int total\
        \ = 1 << k;\n    int n = s.length;\n    if (n < total + k - 1) return false;\n\
        \n    List<bool> seen = List.filled(total, false);\n    int count = 0;\n   \
        \ int currentVal = 0;\n    int mask = total - 1;\n\n    for (int i = 0; i <\
        \ n; i++) {\n      currentVal = ((currentVal << 1) & mask) | (s.codeUnitAt(i)\
        \ & 1);\n      if (i >= k - 1) {\n        if (!seen[currentVal]) {\n       \
        \   seen[currentVal] = true;\n          count++;\n          if (count == total)\
        \ return true;\n        }\n      }\n    }\n    return count == total;\n  }\n\
        }"
      go: "func hasAllCodes(s string, k int) bool {\n    total := 1 << uint(k)\n   \
        \ n := len(s)\n    if n < total+k-1 {\n        return false\n    }\n\n    seen\
        \ := make([]bool, total)\n    count := 0\n    currentVal := 0\n    mask := total\
        \ - 1\n\n    for i := 0; i < n; i++ {\n        currentVal = ((currentVal <<\
        \ 1) & mask) | int(s[i]&1)\n        if i >= k-1 {\n            if !seen[currentVal]\
        \ {\n                seen[currentVal] = true\n                count++\n    \
        \            if count == total {\n                    return true\n        \
        \        }\n            }\n        }\n    }\n    return count == total\n}"
      ruby: "def has_all_codes(s, k)\n  required = 1 << k\n  return false if s.length\
        \ < required + k - 1\n  seen = {}\n  (0..s.length - k).each do |i|\n    sub\
        \ = s[i, k]\n    unless seen.has_key?(sub)\n      seen[sub] = true\n      return\
        \ true if seen.size == required\n    end\n  end\n  false\nend"
      scala: "object Solution {\n  def hasAllCodes(s: String, k: Int): Boolean = {\n\
        \    val required = 1 << k\n    if (s.length < required + k - 1) return false\n\
        \    val seen = new java.util.BitSet(required)\n    val mask = required - 1\n\
        \    var curr = 0\n    var count = 0\n    for (i <- 0 until s.length) {\n  \
        \    curr = ((curr << 1) | (s(i) - '0')) & mask\n      if (i >= k - 1) {\n \
        \       if (!seen.get(curr)) {\n          seen.set(curr)\n          count +=\
        \ 1\n          if (count == required) return true\n        }\n      }\n    }\n\
        \    false\n  }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn has_all_codes(s:\
        \ String, k: i32) -> bool {\n        let k = k as usize;\n        let required\
        \ = 1 << k;\n        if s.len() < required + k - 1 {\n            return false;\n\
        \        }\n        let mut seen = HashSet::with_capacity(required);\n     \
        \   let bytes = s.as_bytes();\n        for window in bytes.windows(k) {\n  \
        \          seen.insert(window);\n            if seen.len() == required {\n \
        \               return true;\n            }\n        }\n        false\n    }\n\
        }"
      racket: "(define/contract (has-all-codes s k)\n  (-> string? exact-integer? boolean?)\n\
        \  (let* ([len (string-length s)]\n         [required (arithmetic-shift 1 k)])\n\
        \    (if (< len (+ required k -1))\n        #f\n        (let ([seen (make-bytes\
        \ required 0)]\n              [mask (sub1 required)])\n          (let loop ([i\
        \ 0] [curr 0] [count 0])\n            (if (= i len)\n                (= count\
        \ required)\n                (let* ([bit (if (char=? (string-ref s i) #\\1)\
        \ 1 0)]\n                       [next-val (bitwise-and (bitwise-ior (arithmetic-shift\
        \ curr 1) bit) mask)])\n                  (if (>= i (sub1 k))\n            \
        \          (if (= (bytes-ref seen next-val) 0)\n                          (begin\n\
        \                            (bytes-set! seen next-val 1)\n                \
        \            (if (= (add1 count) required)\n                               \
        \ #t\n                                (loop (add1 i) next-val (add1 count))))\n\
        \                          (loop (add1 i) next-val count))\n               \
        \       (loop (add1 i) next-val count)))))))))"
      erlang: "has_all_codes(S, K) ->\n  Required = 1 bsl K,\n  SLen = byte_size(S),\n\
        \  case SLen < Required + K - 1 of\n    true -> false;\n    false -> check(S,\
        \ K, SLen, 0, #{}, Required)\n  end.\n\ncheck(_S, _K, SLen, I, Acc, Required)\
        \ when I > SLen - K ->\n  maps:size(Acc) == Required;\ncheck(S, K, SLen, I,\
        \ Acc, Required) ->\n  Sub = binary:part(S, I, K),\n  case maps:is_key(Sub,\
        \ Acc) of\n    true -> check(S, K, SLen, I + 1, Acc, Required);\n    false ->\n\
        \      NewAcc = Acc#{Sub => true},\n      case maps:size(NewAcc) of\n      \
        \  Required -> true;\n        _ -> check(S, K, SLen, I + 1, NewAcc, Required)\n\
        \      end\n  end."
      elixir: "defmodule Solution do\n  @spec has_all_codes(s :: String.t, k :: integer)\
        \ :: boolean\n  def has_all_codes(s, k) do\n    required = Bitwise.bsl(1, k)\n\
        \    s_len = byte_size(s)\n    if s_len < required + k - 1 do\n      false\n\
        \    else\n      check(s, k, s_len, 0, MapSet.new(), required)\n    end\n  end\n\
        \n  defp check(s, k, s_len, i, acc, required) do\n    if i > s_len - k do\n\
        \      MapSet.size(acc) == required\n    else\n      sub = binary_part(s, i,\
        \ k)\n      if MapSet.member?(acc, sub) do\n        check(s, k, s_len, i + 1,\
        \ acc, required)\n      else\n        new_acc = MapSet.put(acc, sub)\n     \
        \   if MapSet.size(new_acc) == required do\n          true\n        else\n \
        \         check(s, k, s_len, i + 1, new_acc, required)\n        end\n      end\n\
        \    end\n  end\nend"
    approach: 'The problem asks whether all $2^k$ possible binary strings of length
      $k$ appear as substrings in the given string $s$. A binary string of length $k$
      can be viewed as an integer in the range $[0, 2^k - 1]$. The key intuition is
      that there are exactly $2^k$ distinct codes, and if the total number of unique
      substrings of length $k$ found in $s$ equals $2^k$, then the condition is satisfied.
      Since the maximum length of $s$ is $5 \cdot 10^5$ and $k$ is up to $20$, we can
      efficiently track these substrings using either a hash set or a boolean array.


      To optimize, we use a sliding window with bit manipulation. As we slide across
      $s$ one character at a time, we maintain the numerical value of the current $k$-length
      window. By shifting the current value left, applying a bitmask to keep only the
      last $k$ bits, and adding the new character''s value, we update the window in
      $O(1)$ time. This avoids the overhead of repeated string slicing. We use a boolean
      array (or a set) to mark each numerical value as ''seen'' and decrement a counter
      starting from $2^k$. If the counter reaches zero, we return true early. Additionally,
      if the number of possible windows in $s$ ($s.length - k + 1$) is less than $2^k$,
      we can immediately return false.'
    time_complexity: O(N), where N is the length of the string $s$. We iterate through
      the string once, performing constant-time bitwise operations and array lookups
      at each step. Calculating the string length takes $O(N)$, and the final check
      or the early exit also fits within this linear bound.
    space_complexity: O(\min(N, 2^k)), where $2^k$ is the total number of possible binary
      codes. We need to store up to $2^k$ markers to track which codes have been encountered.
      In the worst case where $k=20$, this requires approximately 1MB of memory for
      a boolean array, which is well within standard limits.
    elapsed_time: 366.7910180091858
    model: gemini-3-flash-preview
    generated_at: '2026-02-23 01:30:47 '
---

## Problem #1461: Check If a String Contains All Binary Codes of Size K

**Difficulty:** Medium

**Topics:** Hash Table, String, Bit Manipulation, Rolling Hash, Hash Function

## Problem Description

<p>Given a binary string <code>s</code> and an integer <code>k</code>, return <code>true</code> <em>if every binary code of length</em> <code>k</code> <em>is a substring of</em> <code>s</code>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;00110110&quot;, k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> The binary codes of length 2 are &quot;00&quot;, &quot;01&quot;, &quot;10&quot; and &quot;11&quot;. They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0110&quot;, k = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> The binary codes of length 1 are &quot;0&quot; and &quot;1&quot;, it is clear that both exist as a substring. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0110&quot;, k = 2
<strong>Output:</strong> false
<strong>Explanation:</strong> The binary code &quot;00&quot; is of length 2 and does not exist in the array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= k &lt;= 20</code></li>
</ul>


## Hints

1. We need only to check all sub-strings of length k.

2. The number of distinct sub-strings should be exactly 2^k.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether all $2^k$ possible binary strings of length $k$ appear as substrings in the given string $s$. A binary string of length $k$ can be viewed as an integer in the range $[0, 2^k - 1]$. The key intuition is that there are exactly $2^k$ distinct codes, and if the total number of unique substrings of length $k$ found in $s$ equals $2^k$, then the condition is satisfied. Since the maximum length of $s$ is $5 \cdot 10^5$ and $k$ is up to $20$, we can efficiently track these substrings using either a hash set or a boolean array.

To optimize, we use a sliding window with bit manipulation. As we slide across $s$ one character at a time, we maintain the numerical value of the current $k$-length window. By shifting the current value left, applying a bitmask to keep only the last $k$ bits, and adding the new character's value, we update the window in $O(1)$ time. This avoids the overhead of repeated string slicing. We use a boolean array (or a set) to mark each numerical value as 'seen' and decrement a counter starting from $2^k$. If the counter reaches zero, we return true early. Additionally, if the number of possible windows in $s$ ($s.length - k + 1$) is less than $2^k$, we can immediately return false.

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
    bool hasAllCodes(string s, int k) {
        int n = s.length();
        int total = 1 << k;
        if (n < k || n - k + 1 < total) return false;

        vector<bool> seen(total, false);
        int current = 0;
        int mask = total - 1;
        int count = 0;

        for (int i = 0; i < n; ++i) {
            current = ((current << 1) & mask) | (s[i] - '0');
            if (i >= k - 1) {
                if (!seen[current]) {
                    seen[current] = true;
                    count++;
                    if (count == total) return true;
                }
            }
        }
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean hasAllCodes(String s, int k) {
        int n = s.length();
        int total = 1 << k;
        if (n < k || n - k + 1 < total) return false;

        boolean[] seen = new boolean[total];
        int current = 0;
        int mask = total - 1;
        int count = 0;

        for (int i = 0; i < n; i++) {
            current = ((current << 1) & mask) | (s.charAt(i) - '0');
            if (i >= k - 1) {
                if (!seen[current]) {
                    seen[current] = true;
                    count++;
                    if (count == total) return true;
                }
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        total = 1 << k
        if len(s) - k + 1 < total:
            return False

        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            if len(seen) == total:
                return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total = 1 << k
        if len(s) - k + 1 < total:
            return False

        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            if len(seen) == total:
                return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool hasAllCodes(char* s, int k) {
    int n = strlen(s);
    if (k > 20) return false;
    int total = 1 << k;
    if (n < k || n - k + 1 < total) return false;

    bool* seen = (bool*)calloc(total, sizeof(bool));
    if (!seen) return false;

    int current = 0;
    int mask = total - 1;
    int count = 0;

    for (int i = 0; i < n; i++) {
        current = ((current << 1) & mask) | (s[i] - '0');
        if (i >= k - 1) {
            if (!seen[current]) {
                seen[current] = true;
                count++;
                if (count == total) {
                    free(seen);
                    return true;
                }
            }
        }
    }

    free(seen);
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool HasAllCodes(string s, int k) {
        int n = s.Length;
        int total = 1 << k;
        if (n < k || n - k + 1 < total) return false;

        bool[] seen = new bool[total];
        int current = 0;
        int mask = total - 1;
        int count = 0;

        for (int i = 0; i < n; i++) {
            current = ((current << 1) & mask) | (s[i] - '0');
            if (i >= k - 1) {
                if (!seen[current]) {
                    seen[current] = true;
                    count++;
                    if (count == total) return true;
                }
            }
        }
        return false;
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
 * @param {number} k
 * @return {boolean}
 */
var hasAllCodes = function(s, k) {
    const total = 1 << k;
    if (s.length - k + 1 < total) return false;

    const seen = new Set();
    for (let i = 0; i <= s.length - k; i++) {
        seen.add(s.substring(i, i + k));
        if (seen.size === total) return true;
    }
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function hasAllCodes(s: string, k: number): boolean {
    const total = 1 << k;
    const n = s.length;
    if (n < total + k - 1) return false;

    const seen = new Uint8Array(total);
    let count = 0;
    let currentVal = 0;
    const mask = total - 1;

    for (let i = 0; i < n; i++) {
        currentVal = ((currentVal << 1) & mask) | (s[i] === '1' ? 1 : 0);
        if (i >= k - 1) {
            if (seen[currentVal] === 0) {
                seen[currentVal] = 1;
                count++;
                if (count === total) return true;
            }
        }
    }
    return count === total;
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
     * @param Integer $k
     * @return Boolean
     */
    function hasAllCodes($s, $k) {
        $total = 1 << $k;
        $n = strlen($s);
        if ($n < $total + $k - 1) return false;

        $seen = array_fill(0, $total, false);
        $count = 0;
        $currentVal = 0;
        $mask = $total - 1;

        for ($i = 0; $i < $n; $i++) {
            $currentVal = (($currentVal << 1) & $mask) | ($s[$i] === '1' ? 1 : 0);
            if ($i >= $k - 1) {
                if (!$seen[$currentVal]) {
                    $seen[$currentVal] = true;
                    $count++;
                    if ($count == $total) return true;
                }
            }
        }
        return $count == $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func hasAllCodes(_ s: String, _ k: Int) -> Bool {
        let utf8 = Array(s.utf8)
        let n = utf8.count
        let total = 1 << k
        if n < total + k - 1 { return false }

        var seen = Array(repeating: false, count: total)
        var count = 0
        var currentVal = 0
        let mask = total - 1

        for i in 0..<n {
            currentVal = ((currentVal << 1) & mask) | Int(utf8[i] & 1)
            if i >= k - 1 {
                if !seen[currentVal] {
                    seen[currentVal] = true
                    count += 1
                    if count == total { return true }
                }
            }
        }
        return count == total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun hasAllCodes(s: String, k: Int): Boolean {
        val total = 1 shl k
        val n = s.length
        if (n < total + k - 1) return false

        val seen = BooleanArray(total)
        var count = 0
        var currentVal = 0
        val mask = total - 1

        for (i in 0 until n) {
            currentVal = ((currentVal shl 1) and mask) or (if (s[i] == '1') 1 else 0)
            if (i >= k - 1) {
                if (!seen[currentVal]) {
                    seen[currentVal] = true
                    count++
                    if (count == total) return true
                }
            }
        }
        return count == total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool hasAllCodes(String s, int k) {
    int total = 1 << k;
    int n = s.length;
    if (n < total + k - 1) return false;

    List<bool> seen = List.filled(total, false);
    int count = 0;
    int currentVal = 0;
    int mask = total - 1;

    for (int i = 0; i < n; i++) {
      currentVal = ((currentVal << 1) & mask) | (s.codeUnitAt(i) & 1);
      if (i >= k - 1) {
        if (!seen[currentVal]) {
          seen[currentVal] = true;
          count++;
          if (count == total) return true;
        }
      }
    }
    return count == total;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func hasAllCodes(s string, k int) bool {
    total := 1 << uint(k)
    n := len(s)
    if n < total+k-1 {
        return false
    }

    seen := make([]bool, total)
    count := 0
    currentVal := 0
    mask := total - 1

    for i := 0; i < n; i++ {
        currentVal = ((currentVal << 1) & mask) | int(s[i]&1)
        if i >= k-1 {
            if !seen[currentVal] {
                seen[currentVal] = true
                count++
                if count == total {
                    return true
                }
            }
        }
    }
    return count == total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def has_all_codes(s, k)
  required = 1 << k
  return false if s.length < required + k - 1
  seen = {}
  (0..s.length - k).each do |i|
    sub = s[i, k]
    unless seen.has_key?(sub)
      seen[sub] = true
      return true if seen.size == required
    end
  end
  false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def hasAllCodes(s: String, k: Int): Boolean = {
    val required = 1 << k
    if (s.length < required + k - 1) return false
    val seen = new java.util.BitSet(required)
    val mask = required - 1
    var curr = 0
    var count = 0
    for (i <- 0 until s.length) {
      curr = ((curr << 1) | (s(i) - '0')) & mask
      if (i >= k - 1) {
        if (!seen.get(curr)) {
          seen.set(curr)
          count += 1
          if (count == required) return true
        }
      }
    }
    false
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        let k = k as usize;
        let required = 1 << k;
        if s.len() < required + k - 1 {
            return false;
        }
        let mut seen = HashSet::with_capacity(required);
        let bytes = s.as_bytes();
        for window in bytes.windows(k) {
            seen.insert(window);
            if seen.len() == required {
                return true;
            }
        }
        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (has-all-codes s k)
  (-> string? exact-integer? boolean?)
  (let* ([len (string-length s)]
         [required (arithmetic-shift 1 k)])
    (if (< len (+ required k -1))
        #f
        (let ([seen (make-bytes required 0)]
              [mask (sub1 required)])
          (let loop ([i 0] [curr 0] [count 0])
            (if (= i len)
                (= count required)
                (let* ([bit (if (char=? (string-ref s i) #\1) 1 0)]
                       [next-val (bitwise-and (bitwise-ior (arithmetic-shift curr 1) bit) mask)])
                  (if (>= i (sub1 k))
                      (if (= (bytes-ref seen next-val) 0)
                          (begin
                            (bytes-set! seen next-val 1)
                            (if (= (add1 count) required)
                                #t
                                (loop (add1 i) next-val (add1 count))))
                          (loop (add1 i) next-val count))
                      (loop (add1 i) next-val count)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
has_all_codes(S, K) ->
  Required = 1 bsl K,
  SLen = byte_size(S),
  case SLen < Required + K - 1 of
    true -> false;
    false -> check(S, K, SLen, 0, #{}, Required)
  end.

check(_S, _K, SLen, I, Acc, Required) when I > SLen - K ->
  maps:size(Acc) == Required;
check(S, K, SLen, I, Acc, Required) ->
  Sub = binary:part(S, I, K),
  case maps:is_key(Sub, Acc) of
    true -> check(S, K, SLen, I + 1, Acc, Required);
    false ->
      NewAcc = Acc#{Sub => true},
      case maps:size(NewAcc) of
        Required -> true;
        _ -> check(S, K, SLen, I + 1, NewAcc, Required)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec has_all_codes(s :: String.t, k :: integer) :: boolean
  def has_all_codes(s, k) do
    required = Bitwise.bsl(1, k)
    s_len = byte_size(s)
    if s_len < required + k - 1 do
      false
    else
      check(s, k, s_len, 0, MapSet.new(), required)
    end
  end

  defp check(s, k, s_len, i, acc, required) do
    if i > s_len - k do
      MapSet.size(acc) == required
    else
      sub = binary_part(s, i, k)
      if MapSet.member?(acc, sub) do
        check(s, k, s_len, i + 1, acc, required)
      else
        new_acc = MapSet.put(acc, sub)
        if MapSet.size(new_acc) == required do
          true
        else
          check(s, k, s_len, i + 1, new_acc, required)
        end
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the string $s$. We iterate through the string once, performing constant-time bitwise operations and array lookups at each step. Calculating the string length takes $O(N)$, and the final check or the early exit also fits within this linear bound.
- **Space Complexity:** O(\min(N, 2^k)), where $2^k$ is the total number of possible binary codes. We need to store up to $2^k$ markers to track which codes have been encountered. In the worst case where $k=20$, this requires approximately 1MB of memory for a boolean array, which is well within standard limits.
