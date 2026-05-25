---
layout: post
title: "Jump Game VII"
date: 2026-05-25 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Dynamic Programming", "Sliding Window", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/jump-game-vii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool canReach(string s, int minJump, int\
        \ maxJump) {\n        int n = s.length();\n        if (s[n - 1] == '1') return\
        \ false;\n        vector<bool> dp(n, false);\n        dp[0] = true;\n      \
        \  int reachable_count = 0;\n        for (int j = 1; j < n; ++j) {\n       \
        \     if (j >= minJump) {\n                if (dp[j - minJump]) reachable_count++;\n\
        \            }\n            if (j > maxJump) {\n                if (dp[j - maxJump\
        \ - 1]) reachable_count--;\n            }\n            if (s[j] == '0' && reachable_count\
        \ > 0) {\n                dp[j] = true;\n            }\n        }\n        return\
        \ dp[n - 1];\n    }\n};"
      java: "class Solution {\n    public boolean canReach(String s, int minJump, int\
        \ maxJump) {\n        int n = s.length();\n        if (s.charAt(n - 1) == '1')\
        \ return false;\n        boolean[] dp = new boolean[n];\n        dp[0] = true;\n\
        \        int reachableCount = 0;\n        for (int j = 1; j < n; j++) {\n  \
        \          if (j >= minJump) {\n                if (dp[j - minJump]) {\n   \
        \                 reachableCount++;\n                }\n            }\n    \
        \        if (j > maxJump) {\n                if (dp[j - maxJump - 1]) {\n  \
        \                  reachableCount--;\n                }\n            }\n   \
        \         if (s.charAt(j) == '0' && reachableCount > 0) {\n                dp[j]\
        \ = true;\n            }\n        }\n        return dp[n - 1];\n    }\n}"
      python: "class Solution(object):\n    def canReach(self, s, minJump, maxJump):\n\
        \        \"\"\"\n        :type s: str\n        :type minJump: int\n        :type\
        \ maxJump: int\n        :rtype: bool\n        \"\"\"\n        n = len(s)\n \
        \       if s[n - 1] == '1':\n            return False\n        dp = [False]\
        \ * n\n        dp[0] = True\n        reachable_count = 0\n        for j in range(1,\
        \ n):\n            if j >= minJump:\n                if dp[j - minJump]:\n \
        \                   reachable_count += 1\n            if j > maxJump:\n    \
        \            if dp[j - maxJump - 1]:\n                    reachable_count -=\
        \ 1\n            if s[j] == '0' and reachable_count > 0:\n                dp[j]\
        \ = True\n        return dp[n - 1]"
      python3: "class Solution:\n    def canReach(self, s: str, minJump: int, maxJump:\
        \ int) -> bool:\n        n = len(s)\n        if s[n - 1] == '1':\n         \
        \   return False\n        dp = [False] * n\n        dp[0] = True\n        reachable_count\
        \ = 0\n        for j in range(1, n):\n            if j >= minJump:\n       \
        \         if dp[j - minJump]:\n                    reachable_count += 1\n  \
        \          if j > maxJump:\n                if dp[j - maxJump - 1]:\n      \
        \              reachable_count -= 1\n            if s[j] == '0' and reachable_count\
        \ > 0:\n                dp[j] = True\n        return dp[n - 1]"
      c: "#include <stdbool.h>\n#include <string.h>\n#include <stdlib.h>\n\nbool canReach(char*\
        \ s, int minJump, int maxJump) {\n    int n = (int)strlen(s);\n    if (s[n -\
        \ 1] == '1') return false;\n    bool* dp = (bool*)calloc(n, sizeof(bool));\n\
        \    if (!dp) return false;\n    dp[0] = true;\n    int reachable_count = 0;\n\
        \    for (int j = 1; j < n; j++) {\n        if (j >= minJump) {\n          \
        \  if (dp[j - minJump]) {\n                reachable_count++;\n            }\n\
        \        }\n        if (j > maxJump) {\n            if (dp[j - maxJump - 1])\
        \ {\n                reachable_count--;\n            }\n        }\n        if\
        \ (s[j] == '0' && reachable_count > 0) {\n            dp[j] = true;\n      \
        \  }\n    }\n    bool result = dp[n - 1];\n    free(dp);\n    return result;\n\
        }"
      csharp: "public class Solution {\n    public bool CanReach(string s, int minJump,\
        \ int maxJump) {\n        int n = s.Length;\n        if (s[n - 1] == '1') return\
        \ false;\n\n        bool[] dp = new bool[n];\n        dp[0] = true;\n      \
        \  int reachableCount = 0;\n\n        for (int i = 1; i < n; i++) {\n      \
        \      if (i >= minJump && dp[i - minJump]) {\n                reachableCount++;\n\
        \            }\n            if (i > maxJump && dp[i - maxJump - 1]) {\n    \
        \            reachableCount--;\n            }\n            if (reachableCount\
        \ > 0 && s[i] == '0') {\n                dp[i] = true;\n            }\n    \
        \    }\n\n        return dp[n - 1];\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {number} minJump\n * @param\
        \ {number} maxJump\n * @return {boolean}\n */\nvar canReach = function(s, minJump,\
        \ maxJump) {\n    const n = s.length;\n    if (s[n - 1] === '1') return false;\n\
        \n    const dp = new Uint8Array(n);\n    dp[0] = 1;\n    let reachableCount\
        \ = 0;\n\n    for (let i = 1; i < n; i++) {\n        if (i >= minJump && dp[i\
        \ - minJump]) {\n            reachableCount++;\n        }\n        if (i > maxJump\
        \ && dp[i - maxJump - 1]) {\n            reachableCount--;\n        }\n    \
        \    if (reachableCount > 0 && s[i] === '0') {\n            dp[i] = 1;\n   \
        \     }\n    }\n\n    return dp[n - 1] === 1;\n};"
      typescript: "function canReach(s: string, minJump: number, maxJump: number): boolean\
        \ {\n    const n = s.length;\n    if (s[n - 1] === '1') return false;\n\n  \
        \  const dp: boolean[] = new Array(n).fill(false);\n    dp[0] = true;\n    let\
        \ reachableCount = 0;\n\n    for (let i = 1; i < n; i++) {\n        if (i >=\
        \ minJump && dp[i - minJump]) {\n            reachableCount++;\n        }\n\
        \        if (i > maxJump && dp[i - maxJump - 1]) {\n            reachableCount--;\n\
        \        }\n        if (reachableCount > 0 && s[i] === '0') {\n            dp[i]\
        \ = true;\n        }\n    }\n\n    return dp[n - 1];\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $minJump\n     * @param Integer $maxJump\n     * @return Boolean\n     */\n\
        \    function canReach($s, $minJump, $maxJump) {\n        $n = strlen($s);\n\
        \        if ($s[$n - 1] === '1') {\n            return false;\n        }\n\n\
        \        $dp = array_fill(0, $n, false);\n        $dp[0] = true;\n        $reachableCount\
        \ = 0;\n\n        for ($i = 1; $i < $n; $i++) {\n            if ($i >= $minJump\
        \ && $dp[$i - $minJump]) {\n                $reachableCount++;\n           \
        \ }\n            if ($i > $maxJump && $dp[$i - $maxJump - 1]) {\n          \
        \      $reachableCount--;\n            }\n            if ($reachableCount >\
        \ 0 && $s[$i] === '0') {\n                $dp[$i] = true;\n            }\n \
        \       }\n\n        return $dp[$n - 1];\n    }\n}"
      swift: "class Solution {\n    func canReach(_ s: String, _ minJump: Int, _ maxJump:\
        \ Int) -> Bool {\n        let n = s.count\n        let chars = Array(s)\n  \
        \      if chars[n - 1] == \"1\" {\n            return false\n        }\n\n \
        \       var dp = [Bool](repeating: false, count: n)\n        dp[0] = true\n\
        \        var reachableCount = 0\n\n        for i in 1..<n {\n            if\
        \ i >= minJump && dp[i - minJump] {\n                reachableCount += 1\n \
        \           }\n            if i > maxJump && dp[i - maxJump - 1] {\n       \
        \         reachableCount -= 1\n            }\n            if reachableCount\
        \ > 0 && chars[i] == \"0\" {\n                dp[i] = true\n            }\n\
        \        }\n\n        return dp[n - 1]\n    }\n}"
      kotlin: "class Solution {\n    fun canReach(s: String, minJump: Int, maxJump:\
        \ Int): Boolean {\n        val n = s.length\n        if (s[n - 1] == '1') return\
        \ false\n        val dp = BooleanArray(n)\n        dp[0] = true\n        var\
        \ reachableCount = 0\n        for (i in 1 until n) {\n            if (i >= minJump)\
        \ {\n                if (dp[i - minJump]) {\n                    reachableCount++\n\
        \                }\n            }\n            if (i > maxJump) {\n        \
        \        if (dp[i - maxJump - 1]) {\n                    reachableCount--\n\
        \                }\n            }\n            if (reachableCount > 0 && s[i]\
        \ == '0') {\n                dp[i] = true\n            }\n        }\n      \
        \  return dp[n - 1]\n    }\n}"
      dart: "class Solution {\n  bool canReach(String s, int minJump, int maxJump) {\n\
        \    int n = s.length;\n    if (s[n - 1] == '1') return false;\n    List<bool>\
        \ dp = List.filled(n, false);\n    dp[0] = true;\n    int reachableCount = 0;\n\
        \    for (int i = 1; i < n; i++) {\n      if (i >= minJump) {\n        if (dp[i\
        \ - minJump]) {\n          reachableCount++;\n        }\n      }\n      if (i\
        \ > maxJump) {\n        if (dp[i - maxJump - 1]) {\n          reachableCount--;\n\
        \        }\n      }\n      if (reachableCount > 0 && s[i] == '0') {\n      \
        \  dp[i] = true;\n      }\n    }\n    return dp[n - 1];\n  }\n}"
      go: "func canReach(s string, minJump int, maxJump int) bool {\n    n := len(s)\n\
        \    if s[n-1] == '1' {\n        return false\n    }\n    dp := make([]bool,\
        \ n)\n    dp[0] = true\n    reachableCount := 0\n    for i := 1; i < n; i++\
        \ {\n        if i >= minJump {\n            if dp[i-minJump] {\n           \
        \     reachableCount++\n            }\n        }\n        if i > maxJump {\n\
        \            if dp[i-maxJump-1] {\n                reachableCount--\n      \
        \      }\n        }\n        if reachableCount > 0 && s[i] == '0' {\n      \
        \      dp[i] = true\n        }\n    }\n    return dp[n-1]\n}"
      ruby: "# @param {String} s\n# @param {Integer} min_jump\n# @param {Integer} max_jump\n\
        # @return {Boolean}\ndef can_reach(s, min_jump, max_jump)\n    n = s.length\n\
        \    return false if s[n - 1] == '1'\n    dp = Array.new(n, false)\n    dp[0]\
        \ = true\n    reachable_count = 0\n    (1...n).each do |i|\n        if i >=\
        \ min_jump\n            reachable_count += 1 if dp[i - min_jump]\n        end\n\
        \        if i > max_jump\n            reachable_count -= 1 if dp[i - max_jump\
        \ - 1]\n        end\n        if reachable_count > 0 && s[i] == '0'\n       \
        \     dp[i] = true\n        end\n    end\n    dp[n - 1]\nend"
      scala: "object Solution {\n    def canReach(s: String, minJump: Int, maxJump:\
        \ Int): Boolean = {\n        val n = s.length\n        if (s(n - 1) == '1')\
        \ return false\n        val dp = new Array[Boolean](n)\n        dp(0) = true\n\
        \        var reachableCount = 0\n        for (i <- 1 until n) {\n          \
        \  if (i >= minJump) {\n                if (dp(i - minJump)) {\n           \
        \         reachableCount += 1\n                }\n            }\n          \
        \  if (i > maxJump) {\n                if (dp(i - maxJump - 1)) {\n        \
        \            reachableCount -= 1\n                }\n            }\n       \
        \     if (reachableCount > 0 && s(i) == '0') {\n                dp(i) = true\n\
        \            }\n        }\n        dp(n - 1)\n    }\n}"
      rust: "impl Solution {\n    pub fn can_reach(s: String, min_jump: i32, max_jump:\
        \ i32) -> bool {\n        let n = s.len();\n        let s_bytes = s.as_bytes();\n\
        \        let min_jump = min_jump as usize;\n        let max_jump = max_jump\
        \ as usize;\n\n        if s_bytes[n - 1] != b'0' {\n            return false;\n\
        \        }\n\n        let mut dp = vec![false; n];\n        dp[0] = true;\n\
        \        let mut reachable_count = 0;\n\n        for i in 1..n {\n         \
        \   if i >= min_jump {\n                if dp[i - min_jump] {\n            \
        \        reachable_count += 1;\n                }\n            }\n         \
        \   if i > max_jump {\n                if dp[i - max_jump - 1] {\n         \
        \           reachable_count -= 1;\n                }\n            }\n      \
        \      if s_bytes[i] == b'0' && reachable_count > 0 {\n                dp[i]\
        \ = true;\n            }\n        }\n\n        dp[n - 1]\n    }\n}"
      racket: "(define/contract (can-reach s minJump maxJump)\n  (-> string? exact-integer?\
        \ exact-integer? boolean?)\n  (let* ([n (string-length s)]\n         [s-bytes\
        \ (string->bytes/utf-8 s)]\n         [dp (make-vector n #f)])\n    (if (not\
        \ (= (bytes-ref s-bytes (- n 1)) 48))\n        #f\n        (begin\n        \
        \  (vector-set! dp 0 #t)\n          (let loop ([i 1] [rc 0])\n            (if\
        \ (= i n)\n                (vector-ref dp (- n 1))\n                (let* ([rc1\
        \ (if (>= i minJump)\n                                (if (vector-ref dp (-\
        \ i minJump))\n                                    (+ rc 1)\n              \
        \                      rc)\n                                rc)]\n         \
        \              [rc2 (if (> i maxJump)\n                                (if (vector-ref\
        \ dp (- i maxJump 1))\n                                    (- rc1 1)\n     \
        \                               rc1)\n                                rc1)])\n\
        \                  (when (and (= (bytes-ref s-bytes i) 48) (> rc2 0))\n    \
        \                (vector-set! dp i #t))\n                  (loop (+ i 1) rc2))))))))"
      erlang: "-spec can_reach(S :: unicode:unicode_binary(), MinJump :: integer(),\
        \ MaxJump :: integer()) -> boolean().\ncan_reach(S, MinJump, MaxJump) ->\n \
        \ N = byte_size(S),\n  case binary:at(S, N - 1) of\n    $1 -> false;\n    $0\
        \ ->\n      Dp = array:new(N, {default, false}),\n      Dp1 = array:set(0, true,\
        \ Dp),\n      loop(1, 0, Dp1, S, N, MinJump, MaxJump)\n  end.\n\nloop(I, RC,\
        \ Dp, S, N, MinJump, MaxJump) when I < N ->\n  RC1 = if \n          I >= MinJump\
        \ ->\n            case array:get(I - MinJump, Dp) of\n              true ->\
        \ RC + 1;\n              false -> RC\n            end;\n          true -> RC\n\
        \        end,\n  RC2 = if \n          I > MaxJump ->\n            case array:get(I\
        \ - MaxJump - 1, Dp) of\n              true -> RC1 - 1;\n              false\
        \ -> RC1\n            end;\n          true -> RC1\n        end,\n  NewDp = if\
        \ \n            (RC2 > 0) andalso (binary:at(S, I) == $0) ->\n             \
        \ array:set(I, true, Dp);\n            true -> Dp\n          end,\n  loop(I\
        \ + 1, RC2, NewDp, S, N, MinJump, MaxJump);\nloop(N, _RC, Dp, _S, N, _MinJump,\
        \ _MaxJump) ->\n  array:get(N - 1, Dp)."
      elixir: "defmodule Solution do\n  @spec can_reach(s :: String.t, min_jump :: integer,\
        \ max_jump :: integer) :: boolean\n  def can_reach(s, min_jump, max_jump) do\n\
        \    n = byte_size(s)\n    if :binary.at(s, n - 1) == ?1 do\n      false\n \
        \   else\n      dp = :array.new(n, default: false)\n      dp = :array.set(0,\
        \ true, dp)\n      iterate(1, 0, dp, s, n, min_jump, max_jump)\n    end\n  end\n\
        \n  defp iterate(i, rc, dp, s, n, min_jump, max_jump) when i < n do\n    rc1\
        \ = if i >= min_jump do\n      if :array.get(i - min_jump, dp), do: rc + 1,\
        \ else: rc\n    else\n      rc\n    end\n\n    rc2 = if i > max_jump do\n  \
        \    if :array.get(i - max_jump - 1, dp), do: rc1 - 1, else: rc1\n    else\n\
        \      rc1\n    end\n\n    new_dp = if rc2 > 0 and :binary.at(s, i) == ?0 do\n\
        \      :array.set(i, true, dp)\n    else\n      dp\n    end\n\n    iterate(i\
        \ + 1, rc2, new_dp, s, n, min_jump, max_jump)\n  end\n\n  defp iterate(n, _rc,\
        \ dp, _s, n, _min_jump, _max_jump) do\n    :array.get(n - 1, dp)\n  end\nend"
    approach: 'We solve the problem using dynamic programming with a sliding window
      optimization. Let `dp[i]` be a boolean value indicating whether the $i$-th index
      of the binary string `s` is reachable from index 0. By definition, `dp[0]` is
      true. For any index $j > 0$, it is reachable if $s[j]$ is ''0'' and there exists
      at least one reachable index $i$ in the range $[j - maxJump, j - minJump]$. A
      naive check for each $j$ would result in $O(N \cdot (maxJump - minJump))$ complexity,
      which is too slow given the constraints.


      To optimize this, we maintain a running count, `reachable_count`, of reachable
      indices within the current valid jump window $[j - maxJump, j - minJump]$. As
      we iterate through the string from $j = 1$ to $n-1$, we update the window: when
      $j$ increases, the index $j - minJump$ enters the consideration set and the index
      $j - maxJump - 1$ leaves it. If the entering index was reachable, we increment
      the counter; if the exiting index was reachable, we decrement it. This allows
      us to determine if any index in the valid range is reachable in $O(1)$ time for
      each $j$, leading to a total time complexity of $O(N)$.'
    time_complexity: O(n) where n is the length of the string s. We iterate through
      the string exactly once, performing a constant number of operations (additions,
      subtractions, and comparisons) at each step to maintain the sliding window counter.
    space_complexity: O(n) because we use a boolean dynamic programming array of size
      n to store the reachability status for each character in the input string s.
    elapsed_time: 193.59639191627502
    model: gemini-3-flash-preview
    generated_at: '2026-05-25 02:46:57 '
---

## Problem #1871: Jump Game VII

**Difficulty:** Medium

**Topics:** String, Dynamic Programming, Sliding Window, Prefix Sum

## Problem Description

<p>You are given a <strong>0-indexed</strong> binary string <code>s</code> and two integers <code>minJump</code> and <code>maxJump</code>. In the beginning, you are standing at index <code>0</code>, which is equal to <code>&#39;0&#39;</code>. You can move from index <code>i</code> to index <code>j</code> if the following conditions are fulfilled:</p>

<ul>
	<li><code>i + minJump &lt;= j &lt;= min(i + maxJump, s.length - 1)</code>, and</li>
	<li><code>s[j] == &#39;0&#39;</code>.</li>
</ul>

<p>Return <code>true</code><i> if you can reach index </i><code>s.length - 1</code><i> in </i><code>s</code><em>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;<u>0</u>11<u>0</u>1<u>0</u>&quot;, minJump = 2, maxJump = 3
<strong>Output:</strong> true
<strong>Explanation:</strong>
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;01101110&quot;, minJump = 2, maxJump = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>s[0] == &#39;0&#39;</code></li>
	<li><code>1 &lt;= minJump &lt;= maxJump &lt; s.length</code></li>
</ul>


## Hints

1. Consider for each reachable index i the interval [i + a, i + b].

2. Use partial sums to mark the intervals as reachable.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We solve the problem using dynamic programming with a sliding window optimization. Let `dp[i]` be a boolean value indicating whether the $i$-th index of the binary string `s` is reachable from index 0. By definition, `dp[0]` is true. For any index $j > 0$, it is reachable if $s[j]$ is '0' and there exists at least one reachable index $i$ in the range $[j - maxJump, j - minJump]$. A naive check for each $j$ would result in $O(N \cdot (maxJump - minJump))$ complexity, which is too slow given the constraints.

To optimize this, we maintain a running count, `reachable_count`, of reachable indices within the current valid jump window $[j - maxJump, j - minJump]$. As we iterate through the string from $j = 1$ to $n-1$, we update the window: when $j$ increases, the index $j - minJump$ enters the consideration set and the index $j - maxJump - 1$ leaves it. If the entering index was reachable, we increment the counter; if the exiting index was reachable, we decrement it. This allows us to determine if any index in the valid range is reachable in $O(1)$ time for each $j$, leading to a total time complexity of $O(N)$.

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
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.length();
        if (s[n - 1] == '1') return false;
        vector<bool> dp(n, false);
        dp[0] = true;
        int reachable_count = 0;
        for (int j = 1; j < n; ++j) {
            if (j >= minJump) {
                if (dp[j - minJump]) reachable_count++;
            }
            if (j > maxJump) {
                if (dp[j - maxJump - 1]) reachable_count--;
            }
            if (s[j] == '0' && reachable_count > 0) {
                dp[j] = true;
            }
        }
        return dp[n - 1];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length();
        if (s.charAt(n - 1) == '1') return false;
        boolean[] dp = new boolean[n];
        dp[0] = true;
        int reachableCount = 0;
        for (int j = 1; j < n; j++) {
            if (j >= minJump) {
                if (dp[j - minJump]) {
                    reachableCount++;
                }
            }
            if (j > maxJump) {
                if (dp[j - maxJump - 1]) {
                    reachableCount--;
                }
            }
            if (s.charAt(j) == '0' && reachableCount > 0) {
                dp[j] = true;
            }
        }
        return dp[n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[n - 1] == '1':
            return False
        dp = [False] * n
        dp[0] = True
        reachable_count = 0
        for j in range(1, n):
            if j >= minJump:
                if dp[j - minJump]:
                    reachable_count += 1
            if j > maxJump:
                if dp[j - maxJump - 1]:
                    reachable_count -= 1
            if s[j] == '0' and reachable_count > 0:
                dp[j] = True
        return dp[n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
        dp = [False] * n
        dp[0] = True
        reachable_count = 0
        for j in range(1, n):
            if j >= minJump:
                if dp[j - minJump]:
                    reachable_count += 1
            if j > maxJump:
                if dp[j - maxJump - 1]:
                    reachable_count -= 1
            if s[j] == '0' and reachable_count > 0:
                dp[j] = True
        return dp[n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool canReach(char* s, int minJump, int maxJump) {
    int n = (int)strlen(s);
    if (s[n - 1] == '1') return false;
    bool* dp = (bool*)calloc(n, sizeof(bool));
    if (!dp) return false;
    dp[0] = true;
    int reachable_count = 0;
    for (int j = 1; j < n; j++) {
        if (j >= minJump) {
            if (dp[j - minJump]) {
                reachable_count++;
            }
        }
        if (j > maxJump) {
            if (dp[j - maxJump - 1]) {
                reachable_count--;
            }
        }
        if (s[j] == '0' && reachable_count > 0) {
            dp[j] = true;
        }
    }
    bool result = dp[n - 1];
    free(dp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CanReach(string s, int minJump, int maxJump) {
        int n = s.Length;
        if (s[n - 1] == '1') return false;

        bool[] dp = new bool[n];
        dp[0] = true;
        int reachableCount = 0;

        for (int i = 1; i < n; i++) {
            if (i >= minJump && dp[i - minJump]) {
                reachableCount++;
            }
            if (i > maxJump && dp[i - maxJump - 1]) {
                reachableCount--;
            }
            if (reachableCount > 0 && s[i] == '0') {
                dp[i] = true;
            }
        }

        return dp[n - 1];
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
 * @param {number} minJump
 * @param {number} maxJump
 * @return {boolean}
 */
var canReach = function(s, minJump, maxJump) {
    const n = s.length;
    if (s[n - 1] === '1') return false;

    const dp = new Uint8Array(n);
    dp[0] = 1;
    let reachableCount = 0;

    for (let i = 1; i < n; i++) {
        if (i >= minJump && dp[i - minJump]) {
            reachableCount++;
        }
        if (i > maxJump && dp[i - maxJump - 1]) {
            reachableCount--;
        }
        if (reachableCount > 0 && s[i] === '0') {
            dp[i] = 1;
        }
    }

    return dp[n - 1] === 1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function canReach(s: string, minJump: number, maxJump: number): boolean {
    const n = s.length;
    if (s[n - 1] === '1') return false;

    const dp: boolean[] = new Array(n).fill(false);
    dp[0] = true;
    let reachableCount = 0;

    for (let i = 1; i < n; i++) {
        if (i >= minJump && dp[i - minJump]) {
            reachableCount++;
        }
        if (i > maxJump && dp[i - maxJump - 1]) {
            reachableCount--;
        }
        if (reachableCount > 0 && s[i] === '0') {
            dp[i] = true;
        }
    }

    return dp[n - 1];
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
     * @param Integer $minJump
     * @param Integer $maxJump
     * @return Boolean
     */
    function canReach($s, $minJump, $maxJump) {
        $n = strlen($s);
        if ($s[$n - 1] === '1') {
            return false;
        }

        $dp = array_fill(0, $n, false);
        $dp[0] = true;
        $reachableCount = 0;

        for ($i = 1; $i < $n; $i++) {
            if ($i >= $minJump && $dp[$i - $minJump]) {
                $reachableCount++;
            }
            if ($i > $maxJump && $dp[$i - $maxJump - 1]) {
                $reachableCount--;
            }
            if ($reachableCount > 0 && $s[$i] === '0') {
                $dp[$i] = true;
            }
        }

        return $dp[$n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func canReach(_ s: String, _ minJump: Int, _ maxJump: Int) -> Bool {
        let n = s.count
        let chars = Array(s)
        if chars[n - 1] == "1" {
            return false
        }

        var dp = [Bool](repeating: false, count: n)
        dp[0] = true
        var reachableCount = 0

        for i in 1..<n {
            if i >= minJump && dp[i - minJump] {
                reachableCount += 1
            }
            if i > maxJump && dp[i - maxJump - 1] {
                reachableCount -= 1
            }
            if reachableCount > 0 && chars[i] == "0" {
                dp[i] = true
            }
        }

        return dp[n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun canReach(s: String, minJump: Int, maxJump: Int): Boolean {
        val n = s.length
        if (s[n - 1] == '1') return false
        val dp = BooleanArray(n)
        dp[0] = true
        var reachableCount = 0
        for (i in 1 until n) {
            if (i >= minJump) {
                if (dp[i - minJump]) {
                    reachableCount++
                }
            }
            if (i > maxJump) {
                if (dp[i - maxJump - 1]) {
                    reachableCount--
                }
            }
            if (reachableCount > 0 && s[i] == '0') {
                dp[i] = true
            }
        }
        return dp[n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool canReach(String s, int minJump, int maxJump) {
    int n = s.length;
    if (s[n - 1] == '1') return false;
    List<bool> dp = List.filled(n, false);
    dp[0] = true;
    int reachableCount = 0;
    for (int i = 1; i < n; i++) {
      if (i >= minJump) {
        if (dp[i - minJump]) {
          reachableCount++;
        }
      }
      if (i > maxJump) {
        if (dp[i - maxJump - 1]) {
          reachableCount--;
        }
      }
      if (reachableCount > 0 && s[i] == '0') {
        dp[i] = true;
      }
    }
    return dp[n - 1];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func canReach(s string, minJump int, maxJump int) bool {
    n := len(s)
    if s[n-1] == '1' {
        return false
    }
    dp := make([]bool, n)
    dp[0] = true
    reachableCount := 0
    for i := 1; i < n; i++ {
        if i >= minJump {
            if dp[i-minJump] {
                reachableCount++
            }
        }
        if i > maxJump {
            if dp[i-maxJump-1] {
                reachableCount--
            }
        }
        if reachableCount > 0 && s[i] == '0' {
            dp[i] = true
        }
    }
    return dp[n-1]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer} min_jump
# @param {Integer} max_jump
# @return {Boolean}
def can_reach(s, min_jump, max_jump)
    n = s.length
    return false if s[n - 1] == '1'
    dp = Array.new(n, false)
    dp[0] = true
    reachable_count = 0
    (1...n).each do |i|
        if i >= min_jump
            reachable_count += 1 if dp[i - min_jump]
        end
        if i > max_jump
            reachable_count -= 1 if dp[i - max_jump - 1]
        end
        if reachable_count > 0 && s[i] == '0'
            dp[i] = true
        end
    end
    dp[n - 1]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def canReach(s: String, minJump: Int, maxJump: Int): Boolean = {
        val n = s.length
        if (s(n - 1) == '1') return false
        val dp = new Array[Boolean](n)
        dp(0) = true
        var reachableCount = 0
        for (i <- 1 until n) {
            if (i >= minJump) {
                if (dp(i - minJump)) {
                    reachableCount += 1
                }
            }
            if (i > maxJump) {
                if (dp(i - maxJump - 1)) {
                    reachableCount -= 1
                }
            }
            if (reachableCount > 0 && s(i) == '0') {
                dp(i) = true
            }
        }
        dp(n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
        let n = s.len();
        let s_bytes = s.as_bytes();
        let min_jump = min_jump as usize;
        let max_jump = max_jump as usize;

        if s_bytes[n - 1] != b'0' {
            return false;
        }

        let mut dp = vec![false; n];
        dp[0] = true;
        let mut reachable_count = 0;

        for i in 1..n {
            if i >= min_jump {
                if dp[i - min_jump] {
                    reachable_count += 1;
                }
            }
            if i > max_jump {
                if dp[i - max_jump - 1] {
                    reachable_count -= 1;
                }
            }
            if s_bytes[i] == b'0' && reachable_count > 0 {
                dp[i] = true;
            }
        }

        dp[n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (can-reach s minJump maxJump)
  (-> string? exact-integer? exact-integer? boolean?)
  (let* ([n (string-length s)]
         [s-bytes (string->bytes/utf-8 s)]
         [dp (make-vector n #f)])
    (if (not (= (bytes-ref s-bytes (- n 1)) 48))
        #f
        (begin
          (vector-set! dp 0 #t)
          (let loop ([i 1] [rc 0])
            (if (= i n)
                (vector-ref dp (- n 1))
                (let* ([rc1 (if (>= i minJump)
                                (if (vector-ref dp (- i minJump))
                                    (+ rc 1)
                                    rc)
                                rc)]
                       [rc2 (if (> i maxJump)
                                (if (vector-ref dp (- i maxJump 1))
                                    (- rc1 1)
                                    rc1)
                                rc1)])
                  (when (and (= (bytes-ref s-bytes i) 48) (> rc2 0))
                    (vector-set! dp i #t))
                  (loop (+ i 1) rc2))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec can_reach(S :: unicode:unicode_binary(), MinJump :: integer(), MaxJump :: integer()) -> boolean().
can_reach(S, MinJump, MaxJump) ->
  N = byte_size(S),
  case binary:at(S, N - 1) of
    $1 -> false;
    $0 ->
      Dp = array:new(N, {default, false}),
      Dp1 = array:set(0, true, Dp),
      loop(1, 0, Dp1, S, N, MinJump, MaxJump)
  end.

loop(I, RC, Dp, S, N, MinJump, MaxJump) when I < N ->
  RC1 = if 
          I >= MinJump ->
            case array:get(I - MinJump, Dp) of
              true -> RC + 1;
              false -> RC
            end;
          true -> RC
        end,
  RC2 = if 
          I > MaxJump ->
            case array:get(I - MaxJump - 1, Dp) of
              true -> RC1 - 1;
              false -> RC1
            end;
          true -> RC1
        end,
  NewDp = if 
            (RC2 > 0) andalso (binary:at(S, I) == $0) ->
              array:set(I, true, Dp);
            true -> Dp
          end,
  loop(I + 1, RC2, NewDp, S, N, MinJump, MaxJump);
loop(N, _RC, Dp, _S, N, _MinJump, _MaxJump) ->
  array:get(N - 1, Dp).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec can_reach(s :: String.t, min_jump :: integer, max_jump :: integer) :: boolean
  def can_reach(s, min_jump, max_jump) do
    n = byte_size(s)
    if :binary.at(s, n - 1) == ?1 do
      false
    else
      dp = :array.new(n, default: false)
      dp = :array.set(0, true, dp)
      iterate(1, 0, dp, s, n, min_jump, max_jump)
    end
  end

  defp iterate(i, rc, dp, s, n, min_jump, max_jump) when i < n do
    rc1 = if i >= min_jump do
      if :array.get(i - min_jump, dp), do: rc + 1, else: rc
    else
      rc
    end

    rc2 = if i > max_jump do
      if :array.get(i - max_jump - 1, dp), do: rc1 - 1, else: rc1
    else
      rc1
    end

    new_dp = if rc2 > 0 and :binary.at(s, i) == ?0 do
      :array.set(i, true, dp)
    else
      dp
    end

    iterate(i + 1, rc2, new_dp, s, n, min_jump, max_jump)
  end

  defp iterate(n, _rc, dp, _s, n, _min_jump, _max_jump) do
    :array.get(n - 1, dp)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string s. We iterate through the string exactly once, performing a constant number of operations (additions, subtractions, and comparisons) at each step to maintain the sliding window counter.
- **Space Complexity:** O(n) because we use a boolean dynamic programming array of size n to store the reachability status for each character in the input string s.
