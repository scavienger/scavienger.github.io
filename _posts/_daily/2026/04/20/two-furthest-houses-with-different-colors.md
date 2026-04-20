---
layout: post
title: "Two Furthest Houses With Different Colors"
date: 2026-04-20 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Greedy"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/two-furthest-houses-with-different-colors/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxDistance(vector<int>& colors) {\n\
        \        int n = colors.size();\n        int i = 0, j = n - 1;\n        while\
        \ (colors[j] == colors[0]) {\n            j--;\n        }\n        while (colors[i]\
        \ == colors[n - 1]) {\n            i++;\n        }\n        return j > (n -\
        \ 1 - i) ? j : (n - 1 - i);\n    }\n};"
      java: "class Solution {\n    public int maxDistance(int[] colors) {\n        int\
        \ n = colors.length;\n        int i = 0, j = n - 1;\n        while (colors[j]\
        \ == colors[0]) {\n            j--;\n        }\n        while (colors[i] ==\
        \ colors[n - 1]) {\n            i++;\n        }\n        return Math.max(j,\
        \ n - 1 - i);\n    }\n}"
      python: "class Solution(object):\n    def maxDistance(self, colors):\n       \
        \ \"\"\"\n        :type colors: List[int]\n        :rtype: int\n        \"\"\
        \"\n        n = len(colors)\n        i = 0\n        j = n - 1\n        while\
        \ colors[j] == colors[0]:\n            j -= 1\n        while colors[i] == colors[n\
        \ - 1]:\n            i += 1\n        return max(j, n - 1 - i)"
      python3: "class Solution:\n    def maxDistance(self, colors: List[int]) -> int:\n\
        \        n = len(colors)\n        i = 0\n        j = n - 1\n        while colors[j]\
        \ == colors[0]:\n            j -= 1\n        while colors[i] == colors[n - 1]:\n\
        \            i += 1\n        return max(j, n - 1 - i)"
      c: "int maxDistance(int* colors, int colorsSize) {\n    int i = 0, j = colorsSize\
        \ - 1;\n    while (colors[j] == colors[0]) {\n        j--;\n    }\n    while\
        \ (colors[i] == colors[colorsSize - 1]) {\n        i++;\n    }\n    int dist1\
        \ = j;\n    int dist2 = colorsSize - 1 - i;\n    return dist1 > dist2 ? dist1\
        \ : dist2;\n}"
      csharp: "public class Solution {\n    public int MaxDistance(int[] colors) {\n\
        \        int n = colors.Length;\n        int i = 0, j = n - 1;\n        while\
        \ (colors[j] == colors[0]) {\n            j--;\n        }\n        while (colors[i]\
        \ == colors[n - 1]) {\n            i++;\n        }\n        return Math.Max(j,\
        \ n - 1 - i);\n    }\n}"
      javascript: "/**\n * @param {number[]} colors\n * @return {number}\n */\nvar maxDistance\
        \ = function(colors) {\n    let n = colors.length;\n    let i = 0;\n    let\
        \ j = n - 1;\n    while (colors[j] === colors[0]) {\n        j--;\n    }\n \
        \   while (colors[i] === colors[n - 1]) {\n        i++;\n    }\n    return Math.max(j,\
        \ n - 1 - i);\n};"
      typescript: "function maxDistance(colors: number[]): number {\n    let n = colors.length;\n\
        \    let maxDist = 0;\n    for (let i = n - 1; i >= 0; i--) {\n        if (colors[i]\
        \ !== colors[0]) {\n            maxDist = Math.max(maxDist, i);\n          \
        \  break;\n        }\n    }\n    for (let i = 0; i < n; i++) {\n        if (colors[i]\
        \ !== colors[n - 1]) {\n            maxDist = Math.max(maxDist, n - 1 - i);\n\
        \            break;\n        }\n    }\n    return maxDist;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $colors\n     * @return\
        \ Integer\n     */\n    function maxDistance($colors) {\n        $n = count($colors);\n\
        \        $maxDist = 0;\n        for ($i = $n - 1; $i >= 0; $i--) {\n       \
        \     if ($colors[$i] !== $colors[0]) {\n                $maxDist = max($maxDist,\
        \ $i);\n                break;\n            }\n        }\n        for ($i =\
        \ 0; $i < $n; $i++) {\n            if ($colors[$i] !== $colors[$n - 1]) {\n\
        \                $maxDist = max($maxDist, $n - 1 - $i);\n                break;\n\
        \            }\n        }\n        return $maxDist;\n    }\n}"
      swift: "class Solution {\n    func maxDistance(_ colors: [Int]) -> Int {\n   \
        \     let n = colors.count\n        var maxDist = 0\n        for i in (0..<n).reversed()\
        \ {\n            if colors[i] != colors[0] {\n                maxDist = max(maxDist,\
        \ i)\n                break\n            }\n        }\n        for i in 0..<n\
        \ {\n            if colors[i] != colors[n - 1] {\n                maxDist =\
        \ max(maxDist, n - 1 - i)\n                break\n            }\n        }\n\
        \        return maxDist\n    }\n}"
      kotlin: "class Solution {\n    fun maxDistance(colors: IntArray): Int {\n    \
        \    val n = colors.size\n        var maxDist = 0\n        for (i in n - 1 downTo\
        \ 0) {\n            if (colors[i] != colors[0]) {\n                maxDist =\
        \ Math.max(maxDist, i)\n                break\n            }\n        }\n  \
        \      for (i in 0 until n) {\n            if (colors[i] != colors[n - 1]) {\n\
        \                maxDist = Math.max(maxDist, n - 1 - i)\n                break\n\
        \            }\n        }\n        return maxDist\n    }\n}"
      dart: "class Solution {\n  int maxDistance(List<int> colors) {\n    int n = colors.length;\n\
        \    int maxDist = 0;\n    for (int i = n - 1; i >= 0; i--) {\n      if (colors[i]\
        \ != colors[0]) {\n        if (i > maxDist) {\n          maxDist = i;\n    \
        \    }\n        break;\n      }\n    }\n    for (int i = 0; i < n; i++) {\n\
        \      if (colors[i] != colors[n - 1]) {\n        int dist = n - 1 - i;\n  \
        \      if (dist > maxDist) {\n          maxDist = dist;\n        }\n       \
        \ break;\n      }\n    }\n    return maxDist;\n  }\n}"
      go: "func maxDistance(colors []int) int {\n    n := len(colors)\n    maxDist :=\
        \ 0\n    for i := n - 1; i >= 0; i-- {\n        if colors[i] != colors[0] {\n\
        \            if i > maxDist {\n                maxDist = i\n            }\n\
        \            break\n        }\n    }\n    for i := 0; i < n; i++ {\n       \
        \ if colors[i] != colors[n-1] {\n            dist := n - 1 - i\n           \
        \ if dist > maxDist {\n                maxDist = dist\n            }\n     \
        \       break\n        }\n    }\n    return maxDist\n}"
      ruby: "# @param {Integer[]} colors\n# @return {Integer}\ndef max_distance(colors)\n\
        \  n = colors.length\n  j = n - 1\n  while colors[j] == colors[0]\n    j -=\
        \ 1\n  end\n  i = 0\n  while colors[i] == colors[n - 1]\n    i += 1\n  end\n\
        \  dist1 = j\n  dist2 = n - 1 - i\n  dist1 > dist2 ? dist1 : dist2\nend"
      scala: "object Solution {\n    def maxDistance(colors: Array[Int]): Int = {\n\
        \        val n = colors.length\n        var j = n - 1\n        while (colors(j)\
        \ == colors(0)) {\n            j -= 1\n        }\n        var i = 0\n      \
        \  while (colors(i) == colors(n - 1)) {\n            i += 1\n        }\n   \
        \     math.max(j, n - 1 - i)\n    }\n}"
      rust: "impl Solution {\n    pub fn max_distance(colors: Vec<i32>) -> i32 {\n \
        \       let n = colors.len();\n        let mut j = n - 1;\n        while colors[j]\
        \ == colors[0] {\n            j -= 1;\n        }\n        let mut i = 0;\n \
        \       while colors[i] == colors[n - 1] {\n            i += 1;\n        }\n\
        \        std::cmp::max(j as i32, (n - 1 - i) as i32)\n    }\n}"
      racket: "(define/contract (max-distance colors)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([n (length colors)]\n         [colors-vec (list->vector\
        \ colors)]\n         [c0 (vector-ref colors-vec 0)]\n         [cn-1 (vector-ref\
        \ colors-vec (- n 1))])\n    (let loop-j ([j (- n 1)])\n      (if (not (= (vector-ref\
        \ colors-vec j) c0))\n          (let loop-i ([i 0])\n            (if (not (=\
        \ (vector-ref colors-vec i) cn-1))\n                (max j (- n 1 i))\n    \
        \            (loop-i (+ i 1))))\n          (loop-j (- j 1))))))"
      erlang: "-spec max_distance(Colors :: [integer()]) -> integer().\nmax_distance(Colors)\
        \ ->\n  N = length(Colors),\n  ColorsTuple = list_to_tuple(Colors),\n  C0 =\
        \ element(1, ColorsTuple),\n  CNm1 = element(N, ColorsTuple),\n  J = find_j(ColorsTuple,\
        \ C0, N),\n  I = find_i(ColorsTuple, CNm1, 1),\n  MaxJ = J - 1,\n  MaxI = N\
        \ - I,\n  if MaxJ > MaxI -> MaxJ;\n     true -> MaxI\n  end.\n\nfind_j(Tuple,\
        \ C, Index) ->\n  case element(Index, Tuple) of\n    C -> find_j(Tuple, C, Index\
        \ - 1);\n    _ -> Index\n  end.\n\nfind_i(Tuple, C, Index) ->\n  case element(Index,\
        \ Tuple) of\n    C -> find_i(Tuple, C, Index + 1);\n    _ -> Index\n  end."
      elixir: "defmodule Solution do\n  @spec max_distance(colors :: [integer]) :: integer\n\
        \  def max_distance(colors) do\n    n = length(colors)\n    colors_tuple = List.to_tuple(colors)\n\
        \    c0 = elem(colors_tuple, 0)\n    cn_m1 = elem(colors_tuple, n - 1)\n   \
        \ j = find_j(colors_tuple, c0, n - 1)\n    i = find_i(colors_tuple, cn_m1, 0)\n\
        \    max(j, n - 1 - i)\n  end\n\n  defp find_j(tuple, c, index) do\n    if elem(tuple,\
        \ index) == c do\n      find_j(tuple, c, index - 1)\n    else\n      index\n\
        \    end\n  end\n\n  defp find_i(tuple, c, index) do\n    if elem(tuple, index)\
        \ == c do\n      find_i(tuple, c, index + 1)\n    else\n      index\n    end\n\
        \  end\nend"
    approach: 'The maximum distance between two houses with different colors must involve
      at least one of the endpoints of the street. To prove this greedily, consider
      any pair of indices (i, j) where colors[i] is not equal to colors[j]. If i is
      not 0 and j is not n-1, then the distance abs(i - j) can potentially be increased
      by replacing either i with 0 or j with n-1, as long as the color of the new endpoint
      is different from the other house. Thus, we only need to check the distance from
      the first house to the last house with a different color, and from the last house
      to the first house with a different color.


      We implement this by performing two scans. First, we start from the right end
      of the array and move inward until we find a house with a color different from
      the first house (index 0). Second, we start from the left end of the array and
      move inward until we find a house with a color different from the last house (index
      n-1). The result is the maximum of these two distances. This greedy approach ensures
      we find the global maximum distance while only visiting each house a constant
      number of times.'
    time_complexity: O(n) where n is the number of houses. We perform at most two linear
      passes over the colors array to find the first house from each end that differs
      in color from the opposite endpoint.
    space_complexity: O(1) because we only store a few integer variables to track indices
      and the maximum distance, regardless of the input size.
    elapsed_time: 47.02527666091919
    model: gemini-3-flash-preview
    generated_at: '2026-04-20 02:00:36 '
---

## Problem #2078: Two Furthest Houses With Different Colors

**Difficulty:** Easy

**Topics:** Array, Greedy

## Problem Description

<p>There are <code>n</code> houses evenly lined up on the street, and each house is beautifully painted. You are given a <strong>0-indexed</strong> integer array <code>colors</code> of length <code>n</code>, where <code>colors[i]</code> represents the color of the <code>i<sup>th</sup></code> house.</p>

<p>Return <em>the <strong>maximum</strong> distance between <strong>two</strong> houses with <strong>different</strong> colors</em>.</p>

<p>The distance between the <code>i<sup>th</sup></code> and <code>j<sup>th</sup></code> houses is <code>abs(i - j)</code>, where <code>abs(x)</code> is the <strong>absolute value</strong> of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg1.png" style="width: 610px; height: 84px;" />
<pre>
<strong>Input:</strong> colors = [<u><strong>1</strong></u>,1,1,<strong><u>6</u></strong>,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> In the above image, color 1 is blue, and color 6 is red.
The furthest two houses with different colors are house 0 and house 3.
House 0 has color 1, and house 3 has color 6. The distance between them is abs(0 - 3) = 3.
Note that houses 3 and 6 can also produce the optimal answer.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg2.png" style="width: 426px; height: 84px;" />
<pre>
<strong>Input:</strong> colors = [<u><strong>1</strong></u>,8,3,8,<u><strong>3</strong></u>]
<strong>Output:</strong> 4
<strong>Explanation:</strong> In the above image, color 1 is blue, color 8 is yellow, and color 3 is green.
The furthest two houses with different colors are house 0 and house 4.
House 0 has color 1, and house 4 has color 3. The distance between them is abs(0 - 4) = 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> colors = [<u><strong>0</strong></u>,<strong><u>1</u></strong>]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The furthest two houses with different colors are house 0 and house 1.
House 0 has color 0, and house 1 has color 1. The distance between them is abs(0 - 1) = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n ==&nbsp;colors.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= colors[i] &lt;= 100</code></li>
	<li>Test data are generated such that <strong>at least</strong> two houses have different colors.</li>
</ul>


## Hints

1. The constraints are small. Can you try the combination of every two houses?

2. Greedily, the maximum distance will come from either the pair of the leftmost house and possibly some house on the right with a different color, or the pair of the rightmost house and possibly some house on the left with a different color.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The maximum distance between two houses with different colors must involve at least one of the endpoints of the street. To prove this greedily, consider any pair of indices (i, j) where colors[i] is not equal to colors[j]. If i is not 0 and j is not n-1, then the distance abs(i - j) can potentially be increased by replacing either i with 0 or j with n-1, as long as the color of the new endpoint is different from the other house. Thus, we only need to check the distance from the first house to the last house with a different color, and from the last house to the first house with a different color.

We implement this by performing two scans. First, we start from the right end of the array and move inward until we find a house with a color different from the first house (index 0). Second, we start from the left end of the array and move inward until we find a house with a color different from the last house (index n-1). The result is the maximum of these two distances. This greedy approach ensures we find the global maximum distance while only visiting each house a constant number of times.

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
    int maxDistance(vector<int>& colors) {
        int n = colors.size();
        int i = 0, j = n - 1;
        while (colors[j] == colors[0]) {
            j--;
        }
        while (colors[i] == colors[n - 1]) {
            i++;
        }
        return j > (n - 1 - i) ? j : (n - 1 - i);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxDistance(int[] colors) {
        int n = colors.length;
        int i = 0, j = n - 1;
        while (colors[j] == colors[0]) {
            j--;
        }
        while (colors[i] == colors[n - 1]) {
            i++;
        }
        return Math.max(j, n - 1 - i);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        i = 0
        j = n - 1
        while colors[j] == colors[0]:
            j -= 1
        while colors[i] == colors[n - 1]:
            i += 1
        return max(j, n - 1 - i)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = 0
        j = n - 1
        while colors[j] == colors[0]:
            j -= 1
        while colors[i] == colors[n - 1]:
            i += 1
        return max(j, n - 1 - i)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxDistance(int* colors, int colorsSize) {
    int i = 0, j = colorsSize - 1;
    while (colors[j] == colors[0]) {
        j--;
    }
    while (colors[i] == colors[colorsSize - 1]) {
        i++;
    }
    int dist1 = j;
    int dist2 = colorsSize - 1 - i;
    return dist1 > dist2 ? dist1 : dist2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxDistance(int[] colors) {
        int n = colors.Length;
        int i = 0, j = n - 1;
        while (colors[j] == colors[0]) {
            j--;
        }
        while (colors[i] == colors[n - 1]) {
            i++;
        }
        return Math.Max(j, n - 1 - i);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} colors
 * @return {number}
 */
var maxDistance = function(colors) {
    let n = colors.length;
    let i = 0;
    let j = n - 1;
    while (colors[j] === colors[0]) {
        j--;
    }
    while (colors[i] === colors[n - 1]) {
        i++;
    }
    return Math.max(j, n - 1 - i);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxDistance(colors: number[]): number {
    let n = colors.length;
    let maxDist = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (colors[i] !== colors[0]) {
            maxDist = Math.max(maxDist, i);
            break;
        }
    }
    for (let i = 0; i < n; i++) {
        if (colors[i] !== colors[n - 1]) {
            maxDist = Math.max(maxDist, n - 1 - i);
            break;
        }
    }
    return maxDist;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $colors
     * @return Integer
     */
    function maxDistance($colors) {
        $n = count($colors);
        $maxDist = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($colors[$i] !== $colors[0]) {
                $maxDist = max($maxDist, $i);
                break;
            }
        }
        for ($i = 0; $i < $n; $i++) {
            if ($colors[$i] !== $colors[$n - 1]) {
                $maxDist = max($maxDist, $n - 1 - $i);
                break;
            }
        }
        return $maxDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxDistance(_ colors: [Int]) -> Int {
        let n = colors.count
        var maxDist = 0
        for i in (0..<n).reversed() {
            if colors[i] != colors[0] {
                maxDist = max(maxDist, i)
                break
            }
        }
        for i in 0..<n {
            if colors[i] != colors[n - 1] {
                maxDist = max(maxDist, n - 1 - i)
                break
            }
        }
        return maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxDistance(colors: IntArray): Int {
        val n = colors.size
        var maxDist = 0
        for (i in n - 1 downTo 0) {
            if (colors[i] != colors[0]) {
                maxDist = Math.max(maxDist, i)
                break
            }
        }
        for (i in 0 until n) {
            if (colors[i] != colors[n - 1]) {
                maxDist = Math.max(maxDist, n - 1 - i)
                break
            }
        }
        return maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxDistance(List<int> colors) {
    int n = colors.length;
    int maxDist = 0;
    for (int i = n - 1; i >= 0; i--) {
      if (colors[i] != colors[0]) {
        if (i > maxDist) {
          maxDist = i;
        }
        break;
      }
    }
    for (int i = 0; i < n; i++) {
      if (colors[i] != colors[n - 1]) {
        int dist = n - 1 - i;
        if (dist > maxDist) {
          maxDist = dist;
        }
        break;
      }
    }
    return maxDist;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxDistance(colors []int) int {
    n := len(colors)
    maxDist := 0
    for i := n - 1; i >= 0; i-- {
        if colors[i] != colors[0] {
            if i > maxDist {
                maxDist = i
            }
            break
        }
    }
    for i := 0; i < n; i++ {
        if colors[i] != colors[n-1] {
            dist := n - 1 - i
            if dist > maxDist {
                maxDist = dist
            }
            break
        }
    }
    return maxDist
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} colors
# @return {Integer}
def max_distance(colors)
  n = colors.length
  j = n - 1
  while colors[j] == colors[0]
    j -= 1
  end
  i = 0
  while colors[i] == colors[n - 1]
    i += 1
  end
  dist1 = j
  dist2 = n - 1 - i
  dist1 > dist2 ? dist1 : dist2
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxDistance(colors: Array[Int]): Int = {
        val n = colors.length
        var j = n - 1
        while (colors(j) == colors(0)) {
            j -= 1
        }
        var i = 0
        while (colors(i) == colors(n - 1)) {
            i += 1
        }
        math.max(j, n - 1 - i)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_distance(colors: Vec<i32>) -> i32 {
        let n = colors.len();
        let mut j = n - 1;
        while colors[j] == colors[0] {
            j -= 1;
        }
        let mut i = 0;
        while colors[i] == colors[n - 1] {
            i += 1;
        }
        std::cmp::max(j as i32, (n - 1 - i) as i32)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-distance colors)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length colors)]
         [colors-vec (list->vector colors)]
         [c0 (vector-ref colors-vec 0)]
         [cn-1 (vector-ref colors-vec (- n 1))])
    (let loop-j ([j (- n 1)])
      (if (not (= (vector-ref colors-vec j) c0))
          (let loop-i ([i 0])
            (if (not (= (vector-ref colors-vec i) cn-1))
                (max j (- n 1 i))
                (loop-i (+ i 1))))
          (loop-j (- j 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_distance(Colors :: [integer()]) -> integer().
max_distance(Colors) ->
  N = length(Colors),
  ColorsTuple = list_to_tuple(Colors),
  C0 = element(1, ColorsTuple),
  CNm1 = element(N, ColorsTuple),
  J = find_j(ColorsTuple, C0, N),
  I = find_i(ColorsTuple, CNm1, 1),
  MaxJ = J - 1,
  MaxI = N - I,
  if MaxJ > MaxI -> MaxJ;
     true -> MaxI
  end.

find_j(Tuple, C, Index) ->
  case element(Index, Tuple) of
    C -> find_j(Tuple, C, Index - 1);
    _ -> Index
  end.

find_i(Tuple, C, Index) ->
  case element(Index, Tuple) of
    C -> find_i(Tuple, C, Index + 1);
    _ -> Index
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_distance(colors :: [integer]) :: integer
  def max_distance(colors) do
    n = length(colors)
    colors_tuple = List.to_tuple(colors)
    c0 = elem(colors_tuple, 0)
    cn_m1 = elem(colors_tuple, n - 1)
    j = find_j(colors_tuple, c0, n - 1)
    i = find_i(colors_tuple, cn_m1, 0)
    max(j, n - 1 - i)
  end

  defp find_j(tuple, c, index) do
    if elem(tuple, index) == c do
      find_j(tuple, c, index - 1)
    else
      index
    end
  end

  defp find_i(tuple, c, index) do
    if elem(tuple, index) == c do
      find_i(tuple, c, index + 1)
    else
      index
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of houses. We perform at most two linear passes over the colors array to find the first house from each end that differs in color from the opposite endpoint.
- **Space Complexity:** O(1) because we only store a few integer variables to track indices and the maximum distance, regardless of the input size.
