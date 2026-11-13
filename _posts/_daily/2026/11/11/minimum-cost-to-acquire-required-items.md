---
layout: post
title: "Minimum Cost to Acquire Required Items"
date: 2026-11-11 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long minimumCost(int cost1, int cost2,\
        \ int costBoth, int need1, int need2) {\n        long long shared = min(need1,\
        \ need2);\n        long long total = shared * min(costBoth, cost1 + cost2);\n\
        \        total += (long long)(need1 - shared) * min(costBoth, cost1);\n    \
        \    total += (long long)(need2 - shared) * min(costBoth, cost2);\n        return\
        \ total;\n    }\n};"
      java: "class Solution {\n    public long minimumCost(int cost1, int cost2, int\
        \ costBoth, int need1, int need2) {\n        long shared = Math.min(need1, need2);\n\
        \        long total = shared * Math.min(costBoth, cost1 + cost2);\n        total\
        \ += (long) (need1 - shared) * Math.min(costBoth, cost1);\n        total +=\
        \ (long) (need2 - shared) * Math.min(costBoth, cost2);\n        return total;\n\
        \    }\n}"
      python: "class Solution(object):\n    def minimumCost(self, cost1, cost2, costBoth,\
        \ need1, need2):\n        \"\"\"\n        :type cost1: int\n        :type cost2:\
        \ int\n        :type costBoth: int\n        :type need1: int\n        :type\
        \ need2: int\n        :rtype: int\n        \"\"\"\n        shared = min(need1,\
        \ need2)\n        total = shared * min(costBoth, cost1 + cost2)\n        total\
        \ += (need1 - shared) * min(costBoth, cost1)\n        total += (need2 - shared)\
        \ * min(costBoth, cost2)\n        return total"
      python3: "class Solution:\n    def minimumCost(self, cost1: int, cost2: int, costBoth:\
        \ int, need1: int, need2: int) -> int:\n        shared = min(need1, need2)\n\
        \        total = shared * min(costBoth, cost1 + cost2)\n        total += (need1\
        \ - shared) * min(costBoth, cost1)\n        total += (need2 - shared) * min(costBoth,\
        \ cost2)\n        return total"
      c: "long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2)\
        \ {\n    long long shared = need1 < need2 ? need1 : need2;\n    int pairCost\
        \ = costBoth < cost1 + cost2 ? costBoth : cost1 + cost2;\n    int remaining1Cost\
        \ = costBoth < cost1 ? costBoth : cost1;\n    int remaining2Cost = costBoth\
        \ < cost2 ? costBoth : cost2;\n    long long total = shared * pairCost;\n  \
        \  total += (long long)(need1 - shared) * remaining1Cost;\n    total += (long\
        \ long)(need2 - shared) * remaining2Cost;\n    return total;\n}"
      csharp: "public class Solution {\n    public long MinimumCost(int cost1, int cost2,\
        \ int costBoth, int need1, int need2) {\n        long shared = Math.Min(need1,\
        \ need2);\n        long total = shared * Math.Min(costBoth, cost1 + cost2);\n\
        \        total += (need1 - shared) * Math.Min(costBoth, cost1);\n        total\
        \ += (need2 - shared) * Math.Min(costBoth, cost2);\n        return total;\n\
        \    }\n}"
      javascript: "/**\n * @param {number} cost1\n * @param {number} cost2\n * @param\
        \ {number} costBoth\n * @param {number} need1\n * @param {number} need2\n *\
        \ @return {number}\n */\nvar minimumCost = function(cost1, cost2, costBoth,\
        \ need1, need2) {\n    const shared = Math.min(need1, need2);\n    let total\
        \ = shared * Math.min(costBoth, cost1 + cost2);\n    total += (need1 - shared)\
        \ * Math.min(costBoth, cost1);\n    total += (need2 - shared) * Math.min(costBoth,\
        \ cost2);\n    return total;\n};"
      typescript: "function minimumCost(cost1: number, cost2: number, costBoth: number,\
        \ need1: number, need2: number): number {\n    const shared = Math.min(need1,\
        \ need2);\n    let total = shared * Math.min(costBoth, cost1 + cost2);\n   \
        \ total += (need1 - shared) * Math.min(costBoth, cost1);\n    total += (need2\
        \ - shared) * Math.min(costBoth, cost2);\n    return total;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $cost1\n     * @param\
        \ Integer $cost2\n     * @param Integer $costBoth\n     * @param Integer $need1\n\
        \     * @param Integer $need2\n     * @return Integer\n     */\n    function\
        \ minimumCost($cost1, $cost2, $costBoth, $need1, $need2) {\n        $shared\
        \ = min($need1, $need2);\n        $total = $shared * min($costBoth, $cost1 +\
        \ $cost2);\n        $total += ($need1 - $shared) * min($costBoth, $cost1);\n\
        \        $total += ($need2 - $shared) * min($costBoth, $cost2);\n        return\
        \ $total;\n    }\n}"
      swift: "class Solution {\n    func minimumCost(_ cost1: Int, _ cost2: Int, _ costBoth:\
        \ Int, _ need1: Int, _ need2: Int) -> Int {\n        let shared = min(need1,\
        \ need2)\n        var total = shared * min(costBoth, cost1 + cost2)\n      \
        \  total += (need1 - shared) * min(costBoth, cost1)\n        total += (need2\
        \ - shared) * min(costBoth, cost2)\n        return total\n    }\n}"
      kotlin: "class Solution {\n    fun minimumCost(cost1: Int, cost2: Int, costBoth:\
        \ Int, need1: Int, need2: Int): Long {\n        val shared = minOf(need1, need2)\n\
        \        var total = shared.toLong() * minOf(costBoth, cost1 + cost2).toLong()\n\
        \        total += (need1 - shared).toLong() * minOf(costBoth, cost1).toLong()\n\
        \        total += (need2 - shared).toLong() * minOf(costBoth, cost2).toLong()\n\
        \        return total\n    }\n}"
      dart: "class Solution {\n  int minimumCost(int cost1, int cost2, int costBoth,\
        \ int need1, int need2) {\n    final shared = need1 < need2 ? need1 : need2;\n\
        \    var total = shared * (costBoth < cost1 + cost2 ? costBoth : cost1 + cost2);\n\
        \    total += (need1 - shared) * (costBoth < cost1 ? costBoth : cost1);\n  \
        \  total += (need2 - shared) * (costBoth < cost2 ? costBoth : cost2);\n    return\
        \ total;\n  }\n}"
      go: "func minimumCost(cost1 int, cost2 int, costBoth int, need1 int, need2 int)\
        \ int64 {\n\tshared := need1\n\tif need2 < shared {\n\t\tshared = need2\n\t\
        }\n\tpairCost := cost1 + cost2\n\tif costBoth < pairCost {\n\t\tpairCost = costBoth\n\
        \t}\n\tcost1Only := cost1\n\tif costBoth < cost1Only {\n\t\tcost1Only = costBoth\n\
        \t}\n\tcost2Only := cost2\n\tif costBoth < cost2Only {\n\t\tcost2Only = costBoth\n\
        \t}\n\ttotal := int64(shared) * int64(pairCost)\n\ttotal += int64(need1-shared)\
        \ * int64(cost1Only)\n\ttotal += int64(need2-shared) * int64(cost2Only)\n\t\
        return total\n}"
      ruby: "# @param {Integer} cost1\n# @param {Integer} cost2\n# @param {Integer}\
        \ cost_both\n# @param {Integer} need1\n# @param {Integer} need2\n# @return {Integer}\n\
        def minimum_cost(cost1, cost2, cost_both, need1, need2)\n  shared = [need1,\
        \ need2].min\n  total = shared * [cost_both, cost1 + cost2].min\n  total +=\
        \ (need1 - shared) * [cost_both, cost1].min\n  total += (need2 - shared) * [cost_both,\
        \ cost2].min\n  total\nend"
      scala: "object Solution {\n    def minimumCost(cost1: Int, cost2: Int, costBoth:\
        \ Int, need1: Int, need2: Int): Long = {\n        val shared = math.min(need1,\
        \ need2)\n        var total = shared.toLong * math.min(costBoth, cost1 + cost2).toLong\n\
        \        total += (need1 - shared).toLong * math.min(costBoth, cost1).toLong\n\
        \        total += (need2 - shared).toLong * math.min(costBoth, cost2).toLong\n\
        \        total\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_cost(cost1: i32, cost2: i32, cost_both:\
        \ i32, need1: i32, need2: i32) -> i64 {\n        let shared = need1.min(need2)\
        \ as i64;\n        let total = shared * (cost_both.min(cost1 + cost2) as i64)\n\
        \            + (need1 as i64 - shared) * (cost_both.min(cost1) as i64)\n   \
        \         + (need2 as i64 - shared) * (cost_both.min(cost2) as i64);\n     \
        \   total\n    }\n}"
      racket: "(define/contract (minimum-cost cost1 cost2 costBoth need1 need2)\n  (->\
        \ exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?\
        \ exact-integer?)\n  (let* ([shared (min need1 need2)]\n         [total (* shared\
        \ (min costBoth (+ cost1 cost2)))])\n    (+ total\n       (* (- need1 shared)\
        \ (min costBoth cost1))\n       (* (- need2 shared) (min costBoth cost2)))))"
      erlang: "-spec minimum_cost(Cost1 :: integer(), Cost2 :: integer(), CostBoth ::\
        \ integer(), Need1 :: integer(), Need2 :: integer()) -> integer().\nminimum_cost(Cost1,\
        \ Cost2, CostBoth, Need1, Need2) ->\n    Shared = min(Need1, Need2),\n    Shared\
        \ * min(CostBoth, Cost1 + Cost2)\n        + (Need1 - Shared) * min(CostBoth,\
        \ Cost1)\n        + (Need2 - Shared) * min(CostBoth, Cost2)."
      elixir: "defmodule Solution do\n  @spec minimum_cost(cost1 :: integer, cost2 ::\
        \ integer, cost_both :: integer, need1 :: integer, need2 :: integer) :: integer\n\
        \  def minimum_cost(cost1, cost2, cost_both, need1, need2) do\n    shared =\
        \ min(need1, need2)\n\n    shared * min(cost_both, cost1 + cost2) +\n      (need1\
        \ - shared) * min(cost_both, cost1) +\n      (need2 - shared) * min(cost_both,\
        \ cost2)\n  end\nend"
    approach: 'Pair the overlapping requirements first. For min(need1, need2) units,
      each type 3 item costs costBoth, while one type 1 plus one type 2 item costs cost1
      + cost2, so use the cheaper option.


      Then satisfy whichever requirement remains. Each remaining unit can be covered
      by its specific item or a type 3 item, so use the cheaper of those costs. Use
      64-bit arithmetic for the total because the requirements can be large.'
    time_complexity: O(1), using a fixed number of arithmetic operations.
    space_complexity: O(1), using only a fixed number of variables.
    elapsed_time: 62.00395202636719
    model: gpt-6-luna
    generated_at: '2026-11-12 23:50:19 '
---

## Problem #3789: Minimum Cost to Acquire Required Items

**Difficulty:** Medium

**Topics:** Math, Greedy

## Problem Description

<p>You are given five integers <code>cost1</code>, <code>cost2</code>, <code>costBoth</code>, <code>need1</code>, and <code>need2</code>.</p>

<p>There are three types of items available:</p>

<ul>
	<li>An item of <strong>type 1</strong> costs <code>cost1</code> and contributes 1 unit to the type 1 requirement only.</li>
	<li>An item of <strong>type 2</strong> costs <code>cost2</code> and contributes 1 unit to the type 2 requirement only.</li>
	<li>An item of <strong>type 3</strong> costs <code>costBoth</code> and contributes 1 unit to <strong>both</strong> type 1 and type 2 requirements.</li>
</ul>

<p>You must collect enough items so that the total contribution toward type 1 is <strong>at least</strong> <code>need1</code> and the total contribution toward type 2 is <strong>at least</strong> <code>need2</code>.</p>

<p>Return an integer representing the <strong>minimum</strong> possible total cost to achieve these requirements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>After buying three type 3 items, which cost <code>3 * 1 = 3</code>, the total contribution to type 1 is 3 (<code>&gt;= need1 = 3</code>) and to type 2 is 3 (<code>&gt;= need2 = 2</code>).<br data-end="229" data-start="226" />
Any other valid combination would cost more, so the minimum total cost is 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">22</span></p>

<p><strong>Explanation:</strong></p>

<p>We buy <code>need1 = 2</code> items of type 1 and <code>need2 = 3</code> items of type 2: <code>2 * 5 + 3 * 4 = 10 + 12 = 22</code>.<br />
Any other valid combination would cost more, so the minimum total cost is 22.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Since no items are required (<code>need1 = need2 = 0</code>), we buy nothing and pay 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= cost1, cost2, costBoth &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= need1, need2 &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. First, use `min(costBoth, cost1 + cost2)` for `min(need1, need2)`.

2. For the remaining type 1 requirement `rem1`, use cost `min(costBoth, cost1)` for the rest.

3. Do the same for type 2, using cost `min(costBoth, cost2)`.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Pair the overlapping requirements first. For min(need1, need2) units, each type 3 item costs costBoth, while one type 1 plus one type 2 item costs cost1 + cost2, so use the cheaper option.

Then satisfy whichever requirement remains. Each remaining unit can be covered by its specific item or a type 3 item, so use the cheaper of those costs. Use 64-bit arithmetic for the total because the requirements can be large.

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
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long long shared = min(need1, need2);
        long long total = shared * min(costBoth, cost1 + cost2);
        total += (long long)(need1 - shared) * min(costBoth, cost1);
        total += (long long)(need2 - shared) * min(costBoth, cost2);
        return total;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long shared = Math.min(need1, need2);
        long total = shared * Math.min(costBoth, cost1 + cost2);
        total += (long) (need1 - shared) * Math.min(costBoth, cost1);
        total += (long) (need2 - shared) * Math.min(costBoth, cost2);
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        shared = min(need1, need2)
        total = shared * min(costBoth, cost1 + cost2)
        total += (need1 - shared) * min(costBoth, cost1)
        total += (need2 - shared) * min(costBoth, cost2)
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        shared = min(need1, need2)
        total = shared * min(costBoth, cost1 + cost2)
        total += (need1 - shared) * min(costBoth, cost1)
        total += (need2 - shared) * min(costBoth, cost2)
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
    long long shared = need1 < need2 ? need1 : need2;
    int pairCost = costBoth < cost1 + cost2 ? costBoth : cost1 + cost2;
    int remaining1Cost = costBoth < cost1 ? costBoth : cost1;
    int remaining2Cost = costBoth < cost2 ? costBoth : cost2;
    long long total = shared * pairCost;
    total += (long long)(need1 - shared) * remaining1Cost;
    total += (long long)(need2 - shared) * remaining2Cost;
    return total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MinimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long shared = Math.Min(need1, need2);
        long total = shared * Math.Min(costBoth, cost1 + cost2);
        total += (need1 - shared) * Math.Min(costBoth, cost1);
        total += (need2 - shared) * Math.Min(costBoth, cost2);
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} cost1
 * @param {number} cost2
 * @param {number} costBoth
 * @param {number} need1
 * @param {number} need2
 * @return {number}
 */
var minimumCost = function(cost1, cost2, costBoth, need1, need2) {
    const shared = Math.min(need1, need2);
    let total = shared * Math.min(costBoth, cost1 + cost2);
    total += (need1 - shared) * Math.min(costBoth, cost1);
    total += (need2 - shared) * Math.min(costBoth, cost2);
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumCost(cost1: number, cost2: number, costBoth: number, need1: number, need2: number): number {
    const shared = Math.min(need1, need2);
    let total = shared * Math.min(costBoth, cost1 + cost2);
    total += (need1 - shared) * Math.min(costBoth, cost1);
    total += (need2 - shared) * Math.min(costBoth, cost2);
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $cost1
     * @param Integer $cost2
     * @param Integer $costBoth
     * @param Integer $need1
     * @param Integer $need2
     * @return Integer
     */
    function minimumCost($cost1, $cost2, $costBoth, $need1, $need2) {
        $shared = min($need1, $need2);
        $total = $shared * min($costBoth, $cost1 + $cost2);
        $total += ($need1 - $shared) * min($costBoth, $cost1);
        $total += ($need2 - $shared) * min($costBoth, $cost2);
        return $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumCost(_ cost1: Int, _ cost2: Int, _ costBoth: Int, _ need1: Int, _ need2: Int) -> Int {
        let shared = min(need1, need2)
        var total = shared * min(costBoth, cost1 + cost2)
        total += (need1 - shared) * min(costBoth, cost1)
        total += (need2 - shared) * min(costBoth, cost2)
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumCost(cost1: Int, cost2: Int, costBoth: Int, need1: Int, need2: Int): Long {
        val shared = minOf(need1, need2)
        var total = shared.toLong() * minOf(costBoth, cost1 + cost2).toLong()
        total += (need1 - shared).toLong() * minOf(costBoth, cost1).toLong()
        total += (need2 - shared).toLong() * minOf(costBoth, cost2).toLong()
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
    final shared = need1 < need2 ? need1 : need2;
    var total = shared * (costBoth < cost1 + cost2 ? costBoth : cost1 + cost2);
    total += (need1 - shared) * (costBoth < cost1 ? costBoth : cost1);
    total += (need2 - shared) * (costBoth < cost2 ? costBoth : cost2);
    return total;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumCost(cost1 int, cost2 int, costBoth int, need1 int, need2 int) int64 {
	shared := need1
	if need2 < shared {
		shared = need2
	}
	pairCost := cost1 + cost2
	if costBoth < pairCost {
		pairCost = costBoth
	}
	cost1Only := cost1
	if costBoth < cost1Only {
		cost1Only = costBoth
	}
	cost2Only := cost2
	if costBoth < cost2Only {
		cost2Only = costBoth
	}
	total := int64(shared) * int64(pairCost)
	total += int64(need1-shared) * int64(cost1Only)
	total += int64(need2-shared) * int64(cost2Only)
	return total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} cost1
# @param {Integer} cost2
# @param {Integer} cost_both
# @param {Integer} need1
# @param {Integer} need2
# @return {Integer}
def minimum_cost(cost1, cost2, cost_both, need1, need2)
  shared = [need1, need2].min
  total = shared * [cost_both, cost1 + cost2].min
  total += (need1 - shared) * [cost_both, cost1].min
  total += (need2 - shared) * [cost_both, cost2].min
  total
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumCost(cost1: Int, cost2: Int, costBoth: Int, need1: Int, need2: Int): Long = {
        val shared = math.min(need1, need2)
        var total = shared.toLong * math.min(costBoth, cost1 + cost2).toLong
        total += (need1 - shared).toLong * math.min(costBoth, cost1).toLong
        total += (need2 - shared).toLong * math.min(costBoth, cost2).toLong
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_cost(cost1: i32, cost2: i32, cost_both: i32, need1: i32, need2: i32) -> i64 {
        let shared = need1.min(need2) as i64;
        let total = shared * (cost_both.min(cost1 + cost2) as i64)
            + (need1 as i64 - shared) * (cost_both.min(cost1) as i64)
            + (need2 as i64 - shared) * (cost_both.min(cost2) as i64);
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-cost cost1 cost2 costBoth need1 need2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([shared (min need1 need2)]
         [total (* shared (min costBoth (+ cost1 cost2)))])
    (+ total
       (* (- need1 shared) (min costBoth cost1))
       (* (- need2 shared) (min costBoth cost2)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_cost(Cost1 :: integer(), Cost2 :: integer(), CostBoth :: integer(), Need1 :: integer(), Need2 :: integer()) -> integer().
minimum_cost(Cost1, Cost2, CostBoth, Need1, Need2) ->
    Shared = min(Need1, Need2),
    Shared * min(CostBoth, Cost1 + Cost2)
        + (Need1 - Shared) * min(CostBoth, Cost1)
        + (Need2 - Shared) * min(CostBoth, Cost2).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_cost(cost1 :: integer, cost2 :: integer, cost_both :: integer, need1 :: integer, need2 :: integer) :: integer
  def minimum_cost(cost1, cost2, cost_both, need1, need2) do
    shared = min(need1, need2)

    shared * min(cost_both, cost1 + cost2) +
      (need1 - shared) * min(cost_both, cost1) +
      (need2 - shared) * min(cost_both, cost2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1), using a fixed number of arithmetic operations.
- **Space Complexity:** O(1), using only a fixed number of variables.
