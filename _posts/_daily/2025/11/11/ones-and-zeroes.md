---
layout: post
title: "Ones and Zeroes"
date: 2025-11-11 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "String", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/ones-and-zeroes/
---

## Problem #474: Ones and Zeroes

**Difficulty:** Medium

**Topics:** Array, String, Dynamic Programming

## Problem Description

<p>You are given an array of binary strings <code>strs</code> and two integers <code>m</code> and <code>n</code>.</p>

<p>Return <em>the size of the largest subset of <code>strs</code> such that there are <strong>at most</strong> </em><code>m</code><em> </em><code>0</code><em>&#39;s and </em><code>n</code><em> </em><code>1</code><em>&#39;s in the subset</em>.</p>

<p>A set <code>x</code> is a <strong>subset</strong> of a set <code>y</code> if all elements of <code>x</code> are also elements of <code>y</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;10&quot;,&quot;0001&quot;,&quot;111001&quot;,&quot;1&quot;,&quot;0&quot;], m = 5, n = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> The largest subset with at most 5 0&#39;s and 3 1&#39;s is {&quot;10&quot;, &quot;0001&quot;, &quot;1&quot;, &quot;0&quot;}, so the answer is 4.
Other valid but smaller subsets include {&quot;0001&quot;, &quot;1&quot;} and {&quot;10&quot;, &quot;1&quot;, &quot;0&quot;}.
{&quot;111001&quot;} is an invalid subset because it contains 4 1&#39;s, greater than the maximum of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;10&quot;,&quot;0&quot;,&quot;1&quot;], m = 1, n = 1
<strong>Output:</strong> 2
<b>Explanation:</b> The largest subset is {&quot;0&quot;, &quot;1&quot;}, so the answer is 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 600</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists only of digits <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:13:38 )</small>
</summary>

<div class="ai-solution-content">

### Approach

Failed to parse AI response

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash" checked>
  <div class="tab-labels">
    <label for="lang-python-gemini-2-5-flash">Python</label>
  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Failed to parse response
# Check logs for full output.
# Full Response:
'''
{
  "approach": "This problem is a variation of the 0/1 Knapsack problem with two constraints (zeros and ones). We use a 2D dynamic programming table `dp[i][j]` to store the maximum number of strings that can be formed using at most `i` zeros and `j` ones. For each string, we iterate the DP table backwards to update states, considering whether to include the current string or not.",
  "time_complexity": "O(L * m * n)",
  "space_complexity": "O(m * n)",
  "solutions": {
    "cpp": "class Solution {\npublic:\n    int findMaxForm(std::vector<std::string>& strs, int m, int n) {\n        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));\n\n        for (const std::string& s : strs) {\n            int zeros = 0;\n            int ones = 0;\n            for (char c : s) {\n                if (c == '0') {\n                    zeros++;\n                } else {\n                    ones++;\n                }\n            }\n\n            for (int i = m; i >= zeros; --i) {\n                for (int j = n; j >= ones; --j) {\n                    dp[i][j] = std::max(dp[i][j], 1 + dp[i - zeros][j - ones]);\n                }\n            }\n        }\n\n        return dp[m][n];\n    }\n};\n",
    "java": "import java.util.Arrays;\n\nclass Solution {\n    public int findMaxForm(String[] strs, int m, int n) {\n        int[][] dp = new int[m + 1][n + 1];\n\n        for (String s : strs) {\n            int zeros = 0;\n            int ones = 0;\n            for (char c : s.toCharArray()) {\n                if (c == '0') {\n                    zeros++;\n                } else {\n                    ones++;\n                }\n            }\n\n            for (int i = m; i >= zeros; i--) {\n                for (int j = n; j >= ones; j--) {\n                    dp[i][j] = Math.max(dp[i][j], 1 + dp[i - zeros][j - ones]);\n                }\n            }\n        }\n\n        return dp[m][n];\n    }\n}\n",
    "python": "class Solution:\n    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:\n        dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n        for s in strs:\n            zeros = s.count('0')\n            ones = s.count('1')\n\n            for i in range(m, zeros - 1, -1):\n                for j in range(n, ones - 1, -1):\n                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])\n        \n        return dp[m][n]\n",
    "python3": "class Solution:\n    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:\n        dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n        for s in strs:\n            zeros = s.count('0')\n            ones = s.count('1')\n\n            for i in range(m, zeros - 1, -1):\n                for j in range(n, ones - 1, -1):\n                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])\n        \n        return dp[m][n]\n",
    "c": "#include <stdlib.h>\n#include <string.h>\n#include <stdio.h>\n\n// Helper function for max\nint max(int a, int b) {\n    return a > b ? a : b;\n}\n\nint findMaxForm(char **strs, int strsSize, int m, int n) {\n    // dp table initialization\n    int **dp = (int **)malloc((m + 1) * sizeof(int *));\n    for (int i = 0; i <= m; i++) {\n        dp[i] = (int *)malloc((n + 1) * sizeof(int));\n        for (int j = 0; j <= n; j++) {\n            dp[i][j] = 0;\n        }\n    }\n\n    for (int k = 0; k < strsSize; k++) {\n        char *s = strs[k];\n        int zeros = 0;\n        int ones = 0;\n        for (int i = 0; s[i] != '\\0'; i++) {\n            if (s[i] == '0') {\n                zeros++;\n            } else {\n                ones++;\n            }\n        }\n\n        for (int i = m; i >= zeros; i--) {\n            for (int j = n; j >= ones; j--) {\n                dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones]);\n            }\n        }\n    }\n\n    int result = dp[m][n];\n\n    // Free allocated memory\n    for (int i = 0; i <= m; i++) {\n        free(dp[i]);\n    }\n    free(dp);\n\n    return result;\n}\n",
    "csharp": "using System;\nusing System.Collections.Generic;\n\npublic class Solution {\n    public int FindMaxForm(string[] strs, int m, int n) {\n        int[,] dp = new int[m + 1, n + 1];\n\n        foreach (string s in strs) {\n            int zeros = 0;\n            int ones = 0;\n            foreach (char c in s) {\n                if (c == '0') {\n                    zeros++;\n                } else {\n                    ones++;\n                }\n            }\n\n            for (int i = m; i >= zeros; i--) {\n                for (int j = n; j >= ones; j--) {\n                    dp[i, j] = Math.Max(dp[i, j], 1 + dp[i - zeros, j - ones]);\n                }\n            }\n        }\n\n        return dp[m, n];\n    }\n}\n",
    "javascript": "/**\n * @param {string[]} strs\n * @param {number} m\n * @param {number} n\n * @return {number}\n */\nvar findMaxForm = function(strs, m, n) {\n    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));\n\n    for (const s of strs) {\n        let zeros = 0;\n        let ones = 0;\n        for (const char of s) {\n            if (char === '0') {\n                zeros++;\n            } else {\n                ones++;\n            }\n        }\n\n        for (let i = m; i >= zeros; i--) {\n            for (let j = n; j >= ones; j--) {\n                dp[i][j] = Math.max(dp[i][j], 1 + dp[i - zeros][j - ones]);\n            }\n        }\n    }\n\n    return dp[m][n];\n};\n",
    "typescript": "function findMaxForm(strs: string[], m: number, n: number): number {\n    const dp: number[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));\n\n    for (const s of strs) {\n        let zeros = 0;\n        let ones = 0;\n        for (const char of s) {\n            if (char === '0') {\n                zeros++;\n            } else {\n                ones++;\n            }\n        }\n\n        for (let i = m; i >= zeros; i--) {\n            for (let j = n; j >= ones; j--) {\n                dp[i][j] = Math.max(dp[i][j], 1 + dp[i - zeros][j - ones]);\n            }\n        }\n    }\n\n    return dp[m][n];\n}\n",
    "php": "<?php\nclass Solution {\n\n    /**\n     * @param String[] $strs\n     * @param Integer $m\n     * @param Integer $n\n     * @return Integer\n     */\n    function findMaxForm($strs, $m, $n) {\n        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));\n\n        foreach ($strs as $s) {\n            $zeros = 0;\n            $ones = 0;\n            for ($i = 0; $i < strlen($s); $i++) {\n                if ($s[$i] == '0') {\n                    $zeros++;\n                } else {\n                    $ones++;\n                }\n            }\n\n            for ($i = $m; $i >= $zeros; $i--) {\n                for ($j = $n; $j >= $ones; $j--) {\n                    $dp[$i][$j] = max($dp[$i][$j], 1 + $dp[$i - $zeros][$j - $ones]);\n                }\n            }\n        }\n\n        return $dp[$m][$n];\n    }\n}\n?>\n",
    "swift": "import Foundation\n\nclass Solution {\n    func findMaxForm(_ strs: [String], _ m: Int, _ n: Int) -> Int {\n        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)\n\n        for s in strs {\n            var zeros = 0\n            var ones = 0\n            for char in s {\n                if char == \"0\" {\n                    zeros += 1\n                } else {\n                    ones += 1\n                }\n            }\n\n            for i in (zeros...m).reversed() {\n                for j in (ones...n).reversed() {\n                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])\n                }\n            }\n        }\n\n        return dp[m][n]\n    }\n}\n",
    "kotlin": "class Solution {\n    fun findMaxForm(strs:
'''
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:13:39 )</small>
</summary>

<div class="ai-solution-content">

### Approach

No approach provided

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
// Generation failed for C++
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
