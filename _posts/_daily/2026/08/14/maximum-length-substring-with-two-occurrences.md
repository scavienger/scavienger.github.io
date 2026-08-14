---
layout: post
title: "Maximum Length Substring With Two Occurrences"
date: 2026-08-14 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Hash Table", "String", "Sliding Window"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximumLengthSubstring(string s) {\n\
        \        int counts[26] = {0};\n        int maxLen = 0;\n        int left =\
        \ 0;\n        for (int right = 0; right < s.length(); ++right) {\n         \
        \   int idx = s[right] - 'a';\n            counts[idx]++;\n            while\
        \ (counts[idx] > 2) {\n                counts[s[left] - 'a']--;\n          \
        \      left++;\n            }\n            int currentLen = right - left + 1;\n\
        \            if (currentLen > maxLen) {\n                maxLen = currentLen;\n\
        \            }\n        }\n        return maxLen;\n    }\n};"
      java: "class Solution {\n    public int maximumLengthSubstring(String s) {\n \
        \       int[] counts = new int[26];\n        int maxLen = 0;\n        int left\
        \ = 0;\n        int n = s.length();\n        for (int right = 0; right < n;\
        \ right++) {\n            int idx = s.charAt(right) - 'a';\n            counts[idx]++;\n\
        \            while (counts[idx] > 2) {\n                counts[s.charAt(left)\
        \ - 'a']--;\n                left++;\n            }\n            int currentLen\
        \ = right - left + 1;\n            if (currentLen > maxLen) {\n            \
        \    maxLen = currentLen;\n            }\n        }\n        return maxLen;\n\
        \    }\n}"
      python: "class Solution(object):\n    def maximumLengthSubstring(self, s):\n \
        \       \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n\
        \        counts = {}\n        max_len = 0\n        left = 0\n        for right\
        \ in range(len(s)):\n            char = s[right]\n            counts[char] =\
        \ counts.get(char, 0) + 1\n            while counts[char] > 2:\n           \
        \     counts[s[left]] -= 1\n                left += 1\n            current_len\
        \ = right - left + 1\n            if current_len > max_len:\n              \
        \  max_len = current_len\n        return max_len"
      python3: "class Solution:\n    def maximumLengthSubstring(self, s: str) -> int:\n\
        \        counts = [0] * 26\n        max_len = 0\n        left = 0\n        for\
        \ right in range(len(s)):\n            idx = ord(s[right]) - ord('a')\n    \
        \        counts[idx] += 1\n            while counts[idx] > 2:\n            \
        \    counts[ord(s[left]) - ord('a')] -= 1\n                left += 1\n     \
        \       current_len = right - left + 1\n            if current_len > max_len:\n\
        \                max_len = current_len\n        return max_len"
      c: "int maximumLengthSubstring(char* s) {\n    int counts[26];\n    for (int i\
        \ = 0; i < 26; i++) counts[i] = 0;\n    int maxLen = 0;\n    int left = 0;\n\
        \    int right = 0;\n    while (s[right] != '\\0') {\n        int idx = s[right]\
        \ - 'a';\n        counts[idx]++;\n        while (counts[idx] > 2) {\n      \
        \      counts[s[left] - 'a']--;\n            left++;\n        }\n        int\
        \ currentLen = right - left + 1;\n        if (currentLen > maxLen) {\n     \
        \       maxLen = currentLen;\n        }\n        right++;\n    }\n    return\
        \ maxLen;\n}"
      csharp: "public class Solution {\n    public int MaximumLengthSubstring(string\
        \ s) {\n        int[] counts = new int[26];\n        int maxLen = 0;\n     \
        \   int left = 0;\n        for (int right = 0; right < s.Length; right++) {\n\
        \            int idx = s[right] - 'a';\n            counts[idx]++;\n       \
        \     while (counts[idx] > 2) {\n                counts[s[left] - 'a']--;\n\
        \                left++;\n            }\n            int currentLen = right\
        \ - left + 1;\n            if (currentLen > maxLen) {\n                maxLen\
        \ = currentLen;\n            }\n        }\n        return maxLen;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar maximumLengthSubstring\
        \ = function(s) {\n    let counts = new Array(26).fill(0);\n    let maxLen =\
        \ 0;\n    let left = 0;\n    for (let right = 0; right < s.length; right++)\
        \ {\n        let charIdx = s.charCodeAt(right) - 97;\n        counts[charIdx]++;\n\
        \        while (counts[charIdx] > 2) {\n            let leftIdx = s.charCodeAt(left)\
        \ - 97;\n            counts[leftIdx]--;\n            left++;\n        }\n  \
        \      let currentLen = right - left + 1;\n        if (currentLen > maxLen)\
        \ {\n            maxLen = currentLen;\n        }\n    }\n    return maxLen;\n\
        };"
      typescript: "function maximumLengthSubstring(s: string): number {\n    let maxLen\
        \ = 0;\n    let left = 0;\n    const counts: { [key: string]: number } = {};\n\
        \n    for (let right = 0; right < s.length; right++) {\n        const char =\
        \ s[right];\n        counts[char] = (counts[char] || 0) + 1;\n\n        while\
        \ (counts[char] > 2) {\n            const leftChar = s[left];\n            counts[leftChar]--;\n\
        \            left++;\n        }\n\n        const currentLen = right - left +\
        \ 1;\n        if (currentLen > maxLen) {\n            maxLen = currentLen;\n\
        \        }\n    }\n\n    return maxLen;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function maximumLengthSubstring($s) {\n        $maxLen = 0;\n\
        \        $left = 0;\n        $counts = [];\n        $n = strlen($s);\n\n   \
        \     for ($right = 0; $right < $n; $right++) {\n            $char = $s[$right];\n\
        \            if (!isset($counts[$char])) {\n                $counts[$char] =\
        \ 0;\n            }\n            $counts[$char]++;\n\n            while ($counts[$char]\
        \ > 2) {\n                $leftChar = $s[$left];\n                $counts[$leftChar]--;\n\
        \                $left++;\n            }\n\n            $currentLen = $right\
        \ - $left + 1;\n            if ($currentLen > $maxLen) {\n                $maxLen\
        \ = $currentLen;\n            }\n        }\n\n        return $maxLen;\n    }\n\
        }"
      swift: "class Solution {\n    func maximumLengthSubstring(_ s: String) -> Int\
        \ {\n        let sChars = Array(s)\n        var maxLen = 0\n        var left\
        \ = 0\n        var counts = [Character: Int]()\n\n        for right in 0..<sChars.count\
        \ {\n            let char = sChars[right]\n            counts[char, default:\
        \ 0] += 1\n\n            while counts[char, default: 0] > 2 {\n            \
        \    let leftChar = sChars[left]\n                counts[leftChar, default:\
        \ 0] -= 1\n                left += 1\n            }\n\n            let currentLen\
        \ = right - left + 1\n            if currentLen > maxLen {\n               \
        \ maxLen = currentLen\n            }\n        }\n\n        return maxLen\n \
        \   }\n}"
      kotlin: "class Solution {\n    fun maximumLengthSubstring(s: String): Int {\n\
        \        var maxLen = 0\n        var left = 0\n        val counts = mutableMapOf<Char,\
        \ Int>()\n\n        for (right in s.indices) {\n            val char = s[right]\n\
        \            counts[char] = counts.getOrDefault(char, 0) + 1\n\n           \
        \ while (counts[char]!! > 2) {\n                val leftChar = s[left]\n   \
        \             counts[leftChar] = counts[leftChar]!! - 1\n                left++\n\
        \            }\n\n            val currentLen = right - left + 1\n          \
        \  if (currentLen > maxLen) {\n                maxLen = currentLen\n       \
        \     }\n        }\n\n        return maxLen\n    }\n}"
      dart: "class Solution {\n  int maximumLengthSubstring(String s) {\n    int maxLen\
        \ = 0;\n    int left = 0;\n    Map<String, int> counts = {};\n\n    for (int\
        \ right = 0; right < s.length; right++) {\n      String char = s[right];\n \
        \     counts[char] = (counts[char] ?? 0) + 1;\n\n      while (counts[char]!\
        \ > 2) {\n        String leftChar = s[left];\n        counts[leftChar] = counts[leftChar]!\
        \ - 1;\n        left++;\n      }\n\n      int currentLen = right - left + 1;\n\
        \      if (currentLen > maxLen) {\n        maxLen = currentLen;\n      }\n \
        \   }\n\n    return maxLen;\n  }\n}"
      go: "func maximumLengthSubstring(s string) int {\n    maxLen := 0\n    left :=\
        \ 0\n    counts := make(map[byte]int)\n\n    for right := 0; right < len(s);\
        \ right++ {\n        char := s[right]\n        counts[char]++\n\n        for\
        \ counts[char] > 2 {\n            leftChar := s[left]\n            counts[leftChar]--\n\
        \            left++\n        }\n\n        currentLen := right - left + 1\n \
        \       if currentLen > maxLen {\n            maxLen = currentLen\n        }\n\
        \    }\n\n    return maxLen\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef maximum_length_substring(s)\n\
        \  max_len = 0\n  n = s.length\n  (0...n).each do |i|\n    counts = Hash.new(0)\n\
        \    (i...n).each do |j|\n      char = s[j]\n      counts[char] += 1\n     \
        \ break if counts[char] > 2\n      len = j - i + 1\n      max_len = len if len\
        \ > max_len\n    end\n  end\n  max_len\nend"
      scala: "object Solution {\n    def maximumLengthSubstring(s: String): Int = {\n\
        \        var maxLen = 0\n        val n = s.length\n        for (i <- 0 until\
        \ n) {\n            val counts = new Array[Int](26)\n            var j = i\n\
        \            var possible = true\n            while (j < n && possible) {\n\
        \                val idx = s(j) - 'a'\n                counts(idx) += 1\n  \
        \              if (counts(idx) > 2) {\n                    possible = false\n\
        \                } else {\n                    val currentLen = j - i + 1\n\
        \                    if (currentLen > maxLen) {\n                        maxLen\
        \ = currentLen\n                    }\n                    j += 1\n        \
        \        }\n            }\n        }\n        maxLen\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_length_substring(s: String) -> i32\
        \ {\n        let s_bytes = s.as_bytes();\n        let n = s_bytes.len();\n \
        \       let mut max_len = 0;\n        for i in 0..n {\n            let mut counts\
        \ = [0; 26];\n            for j in i..n {\n                let idx = (s_bytes[j]\
        \ - b'a') as usize;\n                counts[idx] += 1;\n                if counts[idx]\
        \ > 2 {\n                    break;\n                }\n                let\
        \ current_len = (j - i + 1) as i32;\n                if current_len > max_len\
        \ {\n                    max_len = current_len;\n                }\n       \
        \     }\n        }\n        max_len\n    }\n}"
      racket: "(define/contract (maximum-length-substring s)\n  (-> string? exact-integer?)\n\
        \  (let ([n (string-length s)]\n        [max-len 0])\n    (for ([i (in-range\
        \ n)])\n      (let ([counts (make-hash)])\n        (let loop ([j i])\n     \
        \     (when (< j n)\n            (let* ([c (string-ref s j)]\n             \
        \      [count (+ 1 (hash-ref counts c 0))])\n              (if (<= count 2)\n\
        \                  (begin\n                    (hash-set! counts c count)\n\
        \                    (set! max-len (max max-len (+ 1 (- j i))))\n          \
        \          (loop (+ j 1)))\n                  'done))))))\n    max-len))"
      erlang: "-spec maximum_length_substring(S :: unicode:unicode_binary()) -> integer().\n\
        maximum_length_substring(S) ->\n  L = binary_to_list(S),\n  solve(L, 0).\n\n\
        solve([], Max) -> Max;\nsolve([_|T] = L, Max) ->\n  NewMax = check_substring(L,\
        \ #{}, 0, Max),\n  solve(T, NewMax).\n\ncheck_substring([], _, Len, Max) ->\
        \ erlang:max(Len, Max);\ncheck_substring([H|T], Map, Len, Max) ->\n  Count =\
        \ maps:get(H, Map, 0),\n  if\n    Count < 2 ->\n      NewLen = Len + 1,\n  \
        \    check_substring(T, Map#{H => Count + 1}, NewLen, erlang:max(NewLen, Max));\n\
        \    true ->\n      Max\n  end."
      elixir: "defmodule Solution do\n  @spec maximum_length_substring(s :: String.t)\
        \ :: integer\n  def maximum_length_substring(s) do\n    chars = String.to_charlist(s)\n\
        \    n = length(chars)\n    if n == 0 do\n      0\n    else\n      Enum.reduce(0..(n\
        \ - 1), 0, fn i, acc_max ->\n        substring_chars = Enum.slice(chars, i..(n\
        \ - 1))\n        local_max = find_max_for_start(substring_chars, %{}, 0)\n \
        \       max(acc_max, local_max)\n      end)\n    end\n  end\n\n  defp find_max_for_start([],\
        \ _counts, current_len), do: current_len\n  defp find_max_for_start([char |\
        \ rest], counts, current_len) do\n    count = Map.get(counts, char, 0)\n   \
        \ if count < 2 do\n      find_max_for_start(rest, Map.put(counts, char, count\
        \ + 1), current_len + 1)\n    else\n      current_len\n    end\n  end\nend"
    approach: 'To solve this problem efficiently, we utilize the sliding window (two-pointer)
      technique. We maintain a window defined by two pointers, ''left'' and ''right'',
      representing the current substring. As the ''right'' pointer iterates through
      the string, we increment the count of the character at that position using a frequency
      array of size 26 (to represent ''a'' through ''z''). This allows us to track how
      many times each character appears within the current window in constant time.


      Whenever the frequency of the character at the ''right'' pointer exceeds two,
      the window is no longer valid. To restore validity, we increment the ''left''
      pointer, shrinking the window from the left and decrementing the frequency of
      the character at each ''left'' position until the frequency of the character at
      the ''right'' pointer is reduced to two. Throughout this process, we maintain
      a variable to track the maximum window size ($right - left + 1$) encountered.
      This approach ensures every character is visited at most twice, resulting in a
      highly efficient linear scan.'
    time_complexity: O(n) where $n$ is the length of the string $s$. Each character
      is added to the window once by the 'right' pointer and removed at most once by
      the 'left' pointer, resulting in $2n$ total operations. Frequency lookups and
      updates are $O(1)$ due to the fixed size of the alphabet.
    space_complexity: O(1) (or O(Σ) where Σ is the alphabet size). We use a frequency
      array of size 26 to store counts for each lowercase English letter, which remains
      constant regardless of the input string length.
    elapsed_time: 97.49540638923645
    model: gemini-3-flash-preview
    generated_at: '2026-08-14 01:17:01 '
---

## Problem #3090: Maximum Length Substring With Two Occurrences

**Difficulty:** Easy

**Topics:** Hash Table, String, Sliding Window

## Problem Description

Given a string <code>s</code>, return the <strong>maximum</strong> length of a <span data-keyword="substring">substring</span>&nbsp;such that it contains <em>at most two occurrences</em> of each character.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;bcbbbcba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>
The following substring has a length of 4 and contains at most two occurrences of each character: <code>&quot;bcbb<u>bcba</u>&quot;</code>.</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aaaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>
The following substring has a length of 2 and contains at most two occurrences of each character: <code>&quot;<u>aa</u>aa&quot;</code>.</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


## Hints

1. We can try all substrings by brute-force since the constraints are very small.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we utilize the sliding window (two-pointer) technique. We maintain a window defined by two pointers, 'left' and 'right', representing the current substring. As the 'right' pointer iterates through the string, we increment the count of the character at that position using a frequency array of size 26 (to represent 'a' through 'z'). This allows us to track how many times each character appears within the current window in constant time.

Whenever the frequency of the character at the 'right' pointer exceeds two, the window is no longer valid. To restore validity, we increment the 'left' pointer, shrinking the window from the left and decrementing the frequency of the character at each 'left' position until the frequency of the character at the 'right' pointer is reduced to two. Throughout this process, we maintain a variable to track the maximum window size ($right - left + 1$) encountered. This approach ensures every character is visited at most twice, resulting in a highly efficient linear scan.

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
    int maximumLengthSubstring(string s) {
        int counts[26] = {0};
        int maxLen = 0;
        int left = 0;
        for (int right = 0; right < s.length(); ++right) {
            int idx = s[right] - 'a';
            counts[idx]++;
            while (counts[idx] > 2) {
                counts[s[left] - 'a']--;
                left++;
            }
            int currentLen = right - left + 1;
            if (currentLen > maxLen) {
                maxLen = currentLen;
            }
        }
        return maxLen;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximumLengthSubstring(String s) {
        int[] counts = new int[26];
        int maxLen = 0;
        int left = 0;
        int n = s.length();
        for (int right = 0; right < n; right++) {
            int idx = s.charAt(right) - 'a';
            counts[idx]++;
            while (counts[idx] > 2) {
                counts[s.charAt(left) - 'a']--;
                left++;
            }
            int currentLen = right - left + 1;
            if (currentLen > maxLen) {
                maxLen = currentLen;
            }
        }
        return maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            while counts[char] > 2:
                counts[s[left]] -= 1
                left += 1
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = [0] * 26
        max_len = 0
        left = 0
        for right in range(len(s)):
            idx = ord(s[right]) - ord('a')
            counts[idx] += 1
            while counts[idx] > 2:
                counts[ord(s[left]) - ord('a')] -= 1
                left += 1
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maximumLengthSubstring(char* s) {
    int counts[26];
    for (int i = 0; i < 26; i++) counts[i] = 0;
    int maxLen = 0;
    int left = 0;
    int right = 0;
    while (s[right] != '\0') {
        int idx = s[right] - 'a';
        counts[idx]++;
        while (counts[idx] > 2) {
            counts[s[left] - 'a']--;
            left++;
        }
        int currentLen = right - left + 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
        }
        right++;
    }
    return maxLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximumLengthSubstring(string s) {
        int[] counts = new int[26];
        int maxLen = 0;
        int left = 0;
        for (int right = 0; right < s.Length; right++) {
            int idx = s[right] - 'a';
            counts[idx]++;
            while (counts[idx] > 2) {
                counts[s[left] - 'a']--;
                left++;
            }
            int currentLen = right - left + 1;
            if (currentLen > maxLen) {
                maxLen = currentLen;
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
var maximumLengthSubstring = function(s) {
    let counts = new Array(26).fill(0);
    let maxLen = 0;
    let left = 0;
    for (let right = 0; right < s.length; right++) {
        let charIdx = s.charCodeAt(right) - 97;
        counts[charIdx]++;
        while (counts[charIdx] > 2) {
            let leftIdx = s.charCodeAt(left) - 97;
            counts[leftIdx]--;
            left++;
        }
        let currentLen = right - left + 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
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
function maximumLengthSubstring(s: string): number {
    let maxLen = 0;
    let left = 0;
    const counts: { [key: string]: number } = {};

    for (let right = 0; right < s.length; right++) {
        const char = s[right];
        counts[char] = (counts[char] || 0) + 1;

        while (counts[char] > 2) {
            const leftChar = s[left];
            counts[leftChar]--;
            left++;
        }

        const currentLen = right - left + 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
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
    function maximumLengthSubstring($s) {
        $maxLen = 0;
        $left = 0;
        $counts = [];
        $n = strlen($s);

        for ($right = 0; $right < $n; $right++) {
            $char = $s[$right];
            if (!isset($counts[$char])) {
                $counts[$char] = 0;
            }
            $counts[$char]++;

            while ($counts[$char] > 2) {
                $leftChar = $s[$left];
                $counts[$leftChar]--;
                $left++;
            }

            $currentLen = $right - $left + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
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
    func maximumLengthSubstring(_ s: String) -> Int {
        let sChars = Array(s)
        var maxLen = 0
        var left = 0
        var counts = [Character: Int]()

        for right in 0..<sChars.count {
            let char = sChars[right]
            counts[char, default: 0] += 1

            while counts[char, default: 0] > 2 {
                let leftChar = sChars[left]
                counts[leftChar, default: 0] -= 1
                left += 1
            }

            let currentLen = right - left + 1
            if currentLen > maxLen {
                maxLen = currentLen
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
    fun maximumLengthSubstring(s: String): Int {
        var maxLen = 0
        var left = 0
        val counts = mutableMapOf<Char, Int>()

        for (right in s.indices) {
            val char = s[right]
            counts[char] = counts.getOrDefault(char, 0) + 1

            while (counts[char]!! > 2) {
                val leftChar = s[left]
                counts[leftChar] = counts[leftChar]!! - 1
                left++
            }

            val currentLen = right - left + 1
            if (currentLen > maxLen) {
                maxLen = currentLen
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
  int maximumLengthSubstring(String s) {
    int maxLen = 0;
    int left = 0;
    Map<String, int> counts = {};

    for (int right = 0; right < s.length; right++) {
      String char = s[right];
      counts[char] = (counts[char] ?? 0) + 1;

      while (counts[char]! > 2) {
        String leftChar = s[left];
        counts[leftChar] = counts[leftChar]! - 1;
        left++;
      }

      int currentLen = right - left + 1;
      if (currentLen > maxLen) {
        maxLen = currentLen;
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
func maximumLengthSubstring(s string) int {
    maxLen := 0
    left := 0
    counts := make(map[byte]int)

    for right := 0; right < len(s); right++ {
        char := s[right]
        counts[char]++

        for counts[char] > 2 {
            leftChar := s[left]
            counts[leftChar]--
            left++
        }

        currentLen := right - left + 1
        if currentLen > maxLen {
            maxLen = currentLen
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
def maximum_length_substring(s)
  max_len = 0
  n = s.length
  (0...n).each do |i|
    counts = Hash.new(0)
    (i...n).each do |j|
      char = s[j]
      counts[char] += 1
      break if counts[char] > 2
      len = j - i + 1
      max_len = len if len > max_len
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
    def maximumLengthSubstring(s: String): Int = {
        var maxLen = 0
        val n = s.length
        for (i <- 0 until n) {
            val counts = new Array[Int](26)
            var j = i
            var possible = true
            while (j < n && possible) {
                val idx = s(j) - 'a'
                counts(idx) += 1
                if (counts(idx) > 2) {
                    possible = false
                } else {
                    val currentLen = j - i + 1
                    if (currentLen > maxLen) {
                        maxLen = currentLen
                    }
                    j += 1
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
    pub fn maximum_length_substring(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let n = s_bytes.len();
        let mut max_len = 0;
        for i in 0..n {
            let mut counts = [0; 26];
            for j in i..n {
                let idx = (s_bytes[j] - b'a') as usize;
                counts[idx] += 1;
                if counts[idx] > 2 {
                    break;
                }
                let current_len = (j - i + 1) as i32;
                if current_len > max_len {
                    max_len = current_len;
                }
            }
        }
        max_len
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-length-substring s)
  (-> string? exact-integer?)
  (let ([n (string-length s)]
        [max-len 0])
    (for ([i (in-range n)])
      (let ([counts (make-hash)])
        (let loop ([j i])
          (when (< j n)
            (let* ([c (string-ref s j)]
                   [count (+ 1 (hash-ref counts c 0))])
              (if (<= count 2)
                  (begin
                    (hash-set! counts c count)
                    (set! max-len (max max-len (+ 1 (- j i))))
                    (loop (+ j 1)))
                  'done))))))
    max-len))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_length_substring(S :: unicode:unicode_binary()) -> integer().
maximum_length_substring(S) ->
  L = binary_to_list(S),
  solve(L, 0).

solve([], Max) -> Max;
solve([_|T] = L, Max) ->
  NewMax = check_substring(L, #{}, 0, Max),
  solve(T, NewMax).

check_substring([], _, Len, Max) -> erlang:max(Len, Max);
check_substring([H|T], Map, Len, Max) ->
  Count = maps:get(H, Map, 0),
  if
    Count < 2 ->
      NewLen = Len + 1,
      check_substring(T, Map#{H => Count + 1}, NewLen, erlang:max(NewLen, Max));
    true ->
      Max
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_length_substring(s :: String.t) :: integer
  def maximum_length_substring(s) do
    chars = String.to_charlist(s)
    n = length(chars)
    if n == 0 do
      0
    else
      Enum.reduce(0..(n - 1), 0, fn i, acc_max ->
        substring_chars = Enum.slice(chars, i..(n - 1))
        local_max = find_max_for_start(substring_chars, %{}, 0)
        max(acc_max, local_max)
      end)
    end
  end

  defp find_max_for_start([], _counts, current_len), do: current_len
  defp find_max_for_start([char | rest], counts, current_len) do
    count = Map.get(counts, char, 0)
    if count < 2 do
      find_max_for_start(rest, Map.put(counts, char, count + 1), current_len + 1)
    else
      current_len
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where $n$ is the length of the string $s$. Each character is added to the window once by the 'right' pointer and removed at most once by the 'left' pointer, resulting in $2n$ total operations. Frequency lookups and updates are $O(1)$ due to the fixed size of the alphabet.
- **Space Complexity:** O(1) (or O(Σ) where Σ is the alphabet size). We use a frequency array of size 26 to store counts for each lowercase English letter, which remains constant regardless of the input string length.
