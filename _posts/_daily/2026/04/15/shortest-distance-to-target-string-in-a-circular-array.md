---
layout: post
title: "Shortest Distance to Target String in a Circular Array"
date: 2026-04-15 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int closestTarget(vector<string>& words,\
        \ string target, int startIndex) {\n        int n = words.size();\n        int\
        \ minDistance = -1;\n        for (int i = 0; i < n; ++i) {\n            if (words[i]\
        \ == target) {\n                int directDist = abs(i - startIndex);\n    \
        \            int circularDist = min(directDist, n - directDist);\n         \
        \       if (minDistance == -1 || circularDist < minDistance) {\n           \
        \         minDistance = circularDist;\n                }\n            }\n  \
        \      }\n        return minDistance;\n    }\n};"
      java: "class Solution {\n    public int closestTarget(String[] words, String target,\
        \ int startIndex) {\n        int n = words.length;\n        int minDistance\
        \ = Integer.MAX_VALUE;\n        boolean found = false;\n        for (int i =\
        \ 0; i < n; i++) {\n            if (words[i].equals(target)) {\n           \
        \     int directDist = Math.abs(i - startIndex);\n                int circularDist\
        \ = Math.min(directDist, n - directDist);\n                minDistance = Math.min(minDistance,\
        \ circularDist);\n                found = true;\n            }\n        }\n\
        \        return found ? minDistance : -1;\n    }\n}"
      python: "class Solution(object):\n    def closestTarget(self, words, target, startIndex):\n\
        \        \"\"\"\n        :type words: List[str]\n        :type target: str\n\
        \        :type startIndex: int\n        :rtype: int\n        \"\"\"\n      \
        \  n = len(words)\n        min_dist = float('inf')\n        found = False\n\
        \        for i in range(n):\n            if words[i] == target:\n          \
        \      direct_dist = abs(i - startIndex)\n                circular_dist = min(direct_dist,\
        \ n - direct_dist)\n                min_dist = min(min_dist, circular_dist)\n\
        \                found = True\n        return min_dist if found else -1"
      python3: "class Solution:\n    def closestTarget(self, words: List[str], target:\
        \ str, startIndex: int) -> int:\n        n = len(words)\n        min_dist =\
        \ float('inf')\n        found = False\n        for i in range(n):\n        \
        \    if words[i] == target:\n                direct_dist = abs(i - startIndex)\n\
        \                circular_dist = min(direct_dist, n - direct_dist)\n       \
        \         min_dist = min(min_dist, circular_dist)\n                found = True\n\
        \        return min_dist if found else -1"
      c: "int closestTarget(char** words, int wordsSize, char* target, int startIndex)\
        \ {\n    int minDistance = -1;\n    for (int i = 0; i < wordsSize; i++) {\n\
        \        if (strcmp(words[i], target) == 0) {\n            int directDist =\
        \ abs(i - startIndex);\n            int circularDist = directDist < (wordsSize\
        \ - directDist) ? directDist : (wordsSize - directDist);\n            if (minDistance\
        \ == -1 || circularDist < minDistance) {\n                minDistance = circularDist;\n\
        \            }\n        }\n    }\n    return minDistance;\n}"
      csharp: "public class Solution {\n    public int ClosestTarget(string[] words,\
        \ string target, int startIndex) {\n        int n = words.Length;\n        int\
        \ minDistance = int.MaxValue;\n        bool found = false;\n        for (int\
        \ i = 0; i < n; i++) {\n            if (words[i] == target) {\n            \
        \    int directDist = Math.Abs(i - startIndex);\n                int circularDist\
        \ = Math.Min(directDist, n - directDist);\n                minDistance = Math.Min(minDistance,\
        \ circularDist);\n                found = true;\n            }\n        }\n\
        \        return found ? minDistance : -1;\n    }\n}"
      javascript: "/**\n * @param {string[]} words\n * @param {string} target\n * @param\
        \ {number} startIndex\n * @return {number}\n */\nvar closestTarget = function(words,\
        \ target, startIndex) {\n    let n = words.length;\n    let minDistance = Infinity;\n\
        \    let found = false;\n    for (let i = 0; i < n; i++) {\n        if (words[i]\
        \ === target) {\n            let directDist = Math.abs(i - startIndex);\n  \
        \          let circularDist = Math.min(directDist, n - directDist);\n      \
        \      minDistance = Math.min(minDistance, circularDist);\n            found\
        \ = true;\n        }\n    }\n    return found ? minDistance : -1;\n};"
      typescript: "function closestTarget(words: string[], target: string, startIndex:\
        \ number): number {\n    const n = words.length;\n    let ans = -1;\n    for\
        \ (let i = 0; i < n; i++) {\n        if (words[i] === target) {\n          \
        \  const diff = Math.abs(i - startIndex);\n            const dist = Math.min(diff,\
        \ n - diff);\n            if (ans === -1 || dist < ans) {\n                ans\
        \ = dist;\n            }\n        }\n    }\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param String[] $words\n     * @param\
        \ String $target\n     * @param Integer $startIndex\n     * @return Integer\n\
        \     */\n    function closestTarget($words, $target, $startIndex) {\n     \
        \   $n = count($words);\n        $ans = -1;\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            if ($words[$i] === $target) {\n                $diff = abs($i\
        \ - $startIndex);\n                $dist = min($diff, $n - $diff);\n       \
        \         if ($ans === -1 || $dist < $ans) {\n                    $ans = $dist;\n\
        \                }\n            }\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func closestTarget(_ words: [String], _ target:\
        \ String, _ startIndex: Int) -> Int {\n        let n = words.count\n       \
        \ var ans = -1\n        for i in 0..<n {\n            if words[i] == target\
        \ {\n                let diff = abs(i - startIndex)\n                let dist\
        \ = min(diff, n - diff)\n                if ans == -1 || dist < ans {\n    \
        \                ans = dist\n                }\n            }\n        }\n \
        \       return ans\n    }\n}"
      kotlin: "import kotlin.math.min\nimport kotlin.math.abs\n\nclass Solution {\n\
        \    fun closestTarget(words: Array<String>, target: String, startIndex: Int):\
        \ Int {\n        val n = words.size\n        var ans = -1\n        for (i in\
        \ 0 until n) {\n            if (words[i] == target) {\n                val diff\
        \ = abs(i - startIndex)\n                val dist = min(diff, n - diff)\n  \
        \              if (ans == -1 || dist < ans) {\n                    ans = dist\n\
        \                }\n            }\n        }\n        return ans\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int closestTarget(List<String>\
        \ words, String target, int startIndex) {\n    int n = words.length;\n    int\
        \ ans = -1;\n    for (int i = 0; i < n; i++) {\n      if (words[i] == target)\
        \ {\n        int diff = (i - startIndex).abs();\n        int dist = min(diff,\
        \ n - diff);\n        if (ans == -1 || dist < ans) {\n          ans = dist;\n\
        \        }\n      }\n    }\n    return ans;\n  }\n}"
      go: "func closestTarget(words []string, target string, startIndex int) int {\n\
        \    n := len(words)\n    ans := -1\n    for i := 0; i < n; i++ {\n        if\
        \ words[i] == target {\n            diff := i - startIndex\n            if diff\
        \ < 0 {\n                diff = -diff\n            }\n            dist := diff\n\
        \            if n-diff < dist {\n                dist = n - diff\n         \
        \   }\n            if ans == -1 || dist < ans {\n                ans = dist\n\
        \            }\n        }\n    }\n    return ans\n}"
      ruby: "def closest_target(words, target, start_index)\n  n = words.length\n  distances\
        \ = words.each_with_index.map do |word, i|\n    if word == target\n      dist\
        \ = (i - start_index).abs\n      [dist, n - dist].min\n    end\n  end.compact\n\
        \n  distances.empty? ? -1 : distances.min\nend"
      scala: "object Solution {\n  def closestTarget(words: Array[String], target: String,\
        \ startIndex: Int): Int = {\n    val n = words.length\n    val distances = for\
        \ {\n      (word, i) <- words.zipWithIndex\n      if word == target\n      dist\
        \ = Math.abs(i - startIndex)\n    } yield Math.min(dist, n - dist)\n\n    if\
        \ (distances.isEmpty) -1 else distances.min\n  }\n}"
      rust: "impl Solution {\n    pub fn closest_target(words: Vec<String>, target:\
        \ String, start_index: i32) -> i32 {\n        let n = words.len() as i32;\n\
        \        let mut min_dist = -1;\n\n        for (i, word) in words.iter().enumerate()\
        \ {\n            if word == &target {\n                let dist = (i as i32\
        \ - start_index).abs();\n                let shortest = dist.min(n - dist);\n\
        \                if min_dist == -1 || shortest < min_dist {\n              \
        \      min_dist = shortest;\n                }\n            }\n        }\n\n\
        \        min_dist\n    }\n}"
      racket: "(define/contract (closest-target words target startIndex)\n  (-> (listof\
        \ string?) string? exact-integer? exact-integer?)\n  (let* ([n (length words)]\n\
        \         [results (for/list ([i (in-range n)]\n                           \
        \  [word (in-list words)]\n                             #:when (string=? word\
        \ target))\n                    (let ([dist (abs (- i startIndex))])\n     \
        \                 (min dist (- n dist))))])\n    (if (null? results)\n     \
        \   -1\n        (apply min results))))"
      erlang: "closest_target(Words, Target, StartIndex) ->\n  N = length(Words),\n\
        \  Distances = [begin\n                 Dist = abs(Idx - StartIndex),\n    \
        \             min(Dist, N - Dist)\n               end || {Idx, Word} <- lists:zip(lists:seq(0,\
        \ N - 1), Words), Word =:= Target],\n  case Distances of\n    [] -> -1;\n  \
        \  _ -> lists:min(Distances)\n  end."
      elixir: "defmodule Solution do\n  @spec closest_target(words :: [String.t], target\
        \ :: String.t, start_index :: integer) :: integer\n  def closest_target(words,\
        \ target, start_index) do\n    n = length(words)\n    distances = words\n  \
        \  |> Enum.with_index()\n    |> Enum.filter(fn {word, _i} -> word == target\
        \ end)\n    |> Enum.map(fn {_word, i} ->\n      dist = abs(i - start_index)\n\
        \      min(dist, n - dist)\n    end)\n\n    if distances == [] do\n      -1\n\
        \    else\n      Enum.min(distances)\n    end\n  end\nend"
    approach: 'To find the shortest distance in a circular array of length $n$ between
      a starting index and a target string, we consider both clockwise and counter-clockwise
      movement. For any index $i$ where the word matches the target, the direct distance
      is calculated as the absolute difference $|i - startIndex|$. Because the array
      is circular, the alternative distance wrapping around the boundary is $n - |i
      - startIndex|$. The shortest path to that specific index is the minimum of these
      two values.


      We iterate through every index of the words array and check if the string matches
      the target. If it does, we compute the circular distance using the logic mentioned
      above and update a global minimum variable. If the target is never found after
      checking all indices, we return -1. Otherwise, the global minimum represents the
      shortest possible path to reach any instance of the target string starting from
      the given index.'
    time_complexity: O(n * m) where $n$ is the number of elements in the words array
      and $m$ is the maximum length of a string. We perform a single linear scan of
      the array, and each string comparison takes $O(m)$ time.
    space_complexity: O(1) as we only use a few integer variables to track the minimum
      distance and the current index during the iteration, regardless of the input size.
    elapsed_time: 106.98412418365479
    model: gemini-3-flash-preview
    generated_at: '2026-04-15 01:52:19 '
---

## Problem #2515: Shortest Distance to Target String in a Circular Array

**Difficulty:** Easy

**Topics:** Array, String

## Problem Description

<p>You are given a <strong>0-indexed</strong> <strong>circular</strong> string array <code>words</code> and a string <code>target</code>. A <strong>circular array</strong> means that the array&#39;s end connects to the array&#39;s beginning.</p>

<ul>
	<li>Formally, the next element of <code>words[i]</code> is <code>words[(i + 1) % n]</code> and the previous element of <code>words[i]</code> is <code>words[(i - 1 + n) % n]</code>, where <code>n</code> is the length of <code>words</code>.</li>
</ul>

<p>Starting from <code>startIndex</code>, you can move to either the next word or the previous word with <code>1</code> step at a time.</p>

<p>Return <em>the <strong>shortest</strong> distance needed to reach the string</em> <code>target</code>. If the string <code>target</code> does not exist in <code>words</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;hello&quot;,&quot;i&quot;,&quot;am&quot;,&quot;leetcode&quot;,&quot;hello&quot;], target = &quot;hello&quot;, startIndex = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> We start from index 1 and can reach &quot;hello&quot; by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach &quot;hello&quot; is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;b&quot;,&quot;leetcode&quot;], target = &quot;leetcode&quot;, startIndex = 0
<strong>Output:</strong> 1
<strong>Explanation:</strong> We start from index 0 and can reach &quot;leetcode&quot; by
- moving 2 units to the right to reach index 2.
- moving 1 unit to the left to reach index 2.
The shortest distance to reach &quot;leetcode&quot; is 1.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;i&quot;,&quot;eat&quot;,&quot;leetcode&quot;], target = &quot;ate&quot;, startIndex = 0
<strong>Output:</strong> -1
<strong>Explanation:</strong> Since &quot;ate&quot; does not exist in <code>words</code>, we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> and <code>target</code> consist of only lowercase English letters.</li>
	<li><code>0 &lt;= startIndex &lt; words.length</code></li>
</ul>


## Hints

1. You have two options, either move straight to the left or move straight to the right.

2. Find the first target word and record the distance.

3. Choose the one with the minimum distance.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the shortest distance in a circular array of length $n$ between a starting index and a target string, we consider both clockwise and counter-clockwise movement. For any index $i$ where the word matches the target, the direct distance is calculated as the absolute difference $|i - startIndex|$. Because the array is circular, the alternative distance wrapping around the boundary is $n - |i - startIndex|$. The shortest path to that specific index is the minimum of these two values.

We iterate through every index of the words array and check if the string matches the target. If it does, we compute the circular distance using the logic mentioned above and update a global minimum variable. If the target is never found after checking all indices, we return -1. Otherwise, the global minimum represents the shortest possible path to reach any instance of the target string starting from the given index.

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
    int closestTarget(vector<string>& words, string target, int startIndex) {
        int n = words.size();
        int minDistance = -1;
        for (int i = 0; i < n; ++i) {
            if (words[i] == target) {
                int directDist = abs(i - startIndex);
                int circularDist = min(directDist, n - directDist);
                if (minDistance == -1 || circularDist < minDistance) {
                    minDistance = circularDist;
                }
            }
        }
        return minDistance;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {
        int n = words.length;
        int minDistance = Integer.MAX_VALUE;
        boolean found = false;
        for (int i = 0; i < n; i++) {
            if (words[i].equals(target)) {
                int directDist = Math.abs(i - startIndex);
                int circularDist = Math.min(directDist, n - directDist);
                minDistance = Math.min(minDistance, circularDist);
                found = true;
            }
        }
        return found ? minDistance : -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        min_dist = float('inf')
        found = False
        for i in range(n):
            if words[i] == target:
                direct_dist = abs(i - startIndex)
                circular_dist = min(direct_dist, n - direct_dist)
                min_dist = min(min_dist, circular_dist)
                found = True
        return min_dist if found else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')
        found = False
        for i in range(n):
            if words[i] == target:
                direct_dist = abs(i - startIndex)
                circular_dist = min(direct_dist, n - direct_dist)
                min_dist = min(min_dist, circular_dist)
                found = True
        return min_dist if found else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int closestTarget(char** words, int wordsSize, char* target, int startIndex) {
    int minDistance = -1;
    for (int i = 0; i < wordsSize; i++) {
        if (strcmp(words[i], target) == 0) {
            int directDist = abs(i - startIndex);
            int circularDist = directDist < (wordsSize - directDist) ? directDist : (wordsSize - directDist);
            if (minDistance == -1 || circularDist < minDistance) {
                minDistance = circularDist;
            }
        }
    }
    return minDistance;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int ClosestTarget(string[] words, string target, int startIndex) {
        int n = words.Length;
        int minDistance = int.MaxValue;
        bool found = false;
        for (int i = 0; i < n; i++) {
            if (words[i] == target) {
                int directDist = Math.Abs(i - startIndex);
                int circularDist = Math.Min(directDist, n - directDist);
                minDistance = Math.Min(minDistance, circularDist);
                found = true;
            }
        }
        return found ? minDistance : -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} words
 * @param {string} target
 * @param {number} startIndex
 * @return {number}
 */
var closestTarget = function(words, target, startIndex) {
    let n = words.length;
    let minDistance = Infinity;
    let found = false;
    for (let i = 0; i < n; i++) {
        if (words[i] === target) {
            let directDist = Math.abs(i - startIndex);
            let circularDist = Math.min(directDist, n - directDist);
            minDistance = Math.min(minDistance, circularDist);
            found = true;
        }
    }
    return found ? minDistance : -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function closestTarget(words: string[], target: string, startIndex: number): number {
    const n = words.length;
    let ans = -1;
    for (let i = 0; i < n; i++) {
        if (words[i] === target) {
            const diff = Math.abs(i - startIndex);
            const dist = Math.min(diff, n - diff);
            if (ans === -1 || dist < ans) {
                ans = dist;
            }
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $words
     * @param String $target
     * @param Integer $startIndex
     * @return Integer
     */
    function closestTarget($words, $target, $startIndex) {
        $n = count($words);
        $ans = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($words[$i] === $target) {
                $diff = abs($i - $startIndex);
                $dist = min($diff, $n - $diff);
                if ($ans === -1 || $dist < $ans) {
                    $ans = $dist;
                }
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
    func closestTarget(_ words: [String], _ target: String, _ startIndex: Int) -> Int {
        let n = words.count
        var ans = -1
        for i in 0..<n {
            if words[i] == target {
                let diff = abs(i - startIndex)
                let dist = min(diff, n - diff)
                if ans == -1 || dist < ans {
                    ans = dist
                }
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
import kotlin.math.min
import kotlin.math.abs

class Solution {
    fun closestTarget(words: Array<String>, target: String, startIndex: Int): Int {
        val n = words.size
        var ans = -1
        for (i in 0 until n) {
            if (words[i] == target) {
                val diff = abs(i - startIndex)
                val dist = min(diff, n - diff)
                if (ans == -1 || dist < ans) {
                    ans = dist
                }
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
import 'dart:math';

class Solution {
  int closestTarget(List<String> words, String target, int startIndex) {
    int n = words.length;
    int ans = -1;
    for (int i = 0; i < n; i++) {
      if (words[i] == target) {
        int diff = (i - startIndex).abs();
        int dist = min(diff, n - diff);
        if (ans == -1 || dist < ans) {
          ans = dist;
        }
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
func closestTarget(words []string, target string, startIndex int) int {
    n := len(words)
    ans := -1
    for i := 0; i < n; i++ {
        if words[i] == target {
            diff := i - startIndex
            if diff < 0 {
                diff = -diff
            }
            dist := diff
            if n-diff < dist {
                dist = n - diff
            }
            if ans == -1 || dist < ans {
                ans = dist
            }
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
def closest_target(words, target, start_index)
  n = words.length
  distances = words.each_with_index.map do |word, i|
    if word == target
      dist = (i - start_index).abs
      [dist, n - dist].min
    end
  end.compact

  distances.empty? ? -1 : distances.min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def closestTarget(words: Array[String], target: String, startIndex: Int): Int = {
    val n = words.length
    val distances = for {
      (word, i) <- words.zipWithIndex
      if word == target
      dist = Math.abs(i - startIndex)
    } yield Math.min(dist, n - dist)

    if (distances.isEmpty) -1 else distances.min
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn closest_target(words: Vec<String>, target: String, start_index: i32) -> i32 {
        let n = words.len() as i32;
        let mut min_dist = -1;

        for (i, word) in words.iter().enumerate() {
            if word == &target {
                let dist = (i as i32 - start_index).abs();
                let shortest = dist.min(n - dist);
                if min_dist == -1 || shortest < min_dist {
                    min_dist = shortest;
                }
            }
        }

        min_dist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (closest-target words target startIndex)
  (-> (listof string?) string? exact-integer? exact-integer?)
  (let* ([n (length words)]
         [results (for/list ([i (in-range n)]
                             [word (in-list words)]
                             #:when (string=? word target))
                    (let ([dist (abs (- i startIndex))])
                      (min dist (- n dist))))])
    (if (null? results)
        -1
        (apply min results))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
closest_target(Words, Target, StartIndex) ->
  N = length(Words),
  Distances = [begin
                 Dist = abs(Idx - StartIndex),
                 min(Dist, N - Dist)
               end || {Idx, Word} <- lists:zip(lists:seq(0, N - 1), Words), Word =:= Target],
  case Distances of
    [] -> -1;
    _ -> lists:min(Distances)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec closest_target(words :: [String.t], target :: String.t, start_index :: integer) :: integer
  def closest_target(words, target, start_index) do
    n = length(words)
    distances = words
    |> Enum.with_index()
    |> Enum.filter(fn {word, _i} -> word == target end)
    |> Enum.map(fn {_word, i} ->
      dist = abs(i - start_index)
      min(dist, n - dist)
    end)

    if distances == [] do
      -1
    else
      Enum.min(distances)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * m) where $n$ is the number of elements in the words array and $m$ is the maximum length of a string. We perform a single linear scan of the array, and each string comparison takes $O(m)$ time.
- **Space Complexity:** O(1) as we only use a few integer variables to track the minimum distance and the current index during the iteration, regardless of the input size.
