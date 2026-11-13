---
layout: post
title: "Minimum Time to Make Rope Colorful"
date: 2025-11-03 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "String", "Dynamic Programming", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minCost(string colors, vector<int>& neededTime)\
        \ {\n        int total = 0;\n        int runSum = neededTime[0];\n        int\
        \ runMax = neededTime[0];\n\n        for (int i = 1; i < colors.size(); ++i)\
        \ {\n            if (colors[i] == colors[i - 1]) {\n                runSum +=\
        \ neededTime[i];\n                runMax = max(runMax, neededTime[i]);\n   \
        \         } else {\n                total += runSum - runMax;\n            \
        \    runSum = neededTime[i];\n                runMax = neededTime[i];\n    \
        \        }\n        }\n\n        return total + runSum - runMax;\n    }\n};"
      java: "class Solution {\n    public int minCost(String colors, int[] neededTime)\
        \ {\n        int total = 0;\n        int runSum = neededTime[0];\n        int\
        \ runMax = neededTime[0];\n\n        for (int i = 1; i < colors.length(); i++)\
        \ {\n            if (colors.charAt(i) == colors.charAt(i - 1)) {\n         \
        \       runSum += neededTime[i];\n                runMax = Math.max(runMax,\
        \ neededTime[i]);\n            } else {\n                total += runSum - runMax;\n\
        \                runSum = neededTime[i];\n                runMax = neededTime[i];\n\
        \            }\n        }\n\n        return total + runSum - runMax;\n    }\n\
        }"
      python: "class Solution(object):\n    def minCost(self, colors, neededTime):\n\
        \        \"\"\"\n        :type colors: str\n        :type neededTime: List[int]\n\
        \        :rtype: int\n        \"\"\"\n        total = 0\n        run_sum = neededTime[0]\n\
        \        run_max = neededTime[0]\n\n        for i in range(1, len(colors)):\n\
        \            if colors[i] == colors[i - 1]:\n                run_sum += neededTime[i]\n\
        \                run_max = max(run_max, neededTime[i])\n            else:\n\
        \                total += run_sum - run_max\n                run_sum = neededTime[i]\n\
        \                run_max = neededTime[i]\n\n        return total + run_sum -\
        \ run_max"
      python3: "class Solution:\n    def minCost(self, colors: str, neededTime: list[int])\
        \ -> int:\n        total = 0\n        run_sum = neededTime[0]\n        run_max\
        \ = neededTime[0]\n\n        for i in range(1, len(colors)):\n            if\
        \ colors[i] == colors[i - 1]:\n                run_sum += neededTime[i]\n  \
        \              run_max = max(run_max, neededTime[i])\n            else:\n  \
        \              total += run_sum - run_max\n                run_sum = neededTime[i]\n\
        \                run_max = neededTime[i]\n\n        return total + run_sum -\
        \ run_max"
      c: "int minCost(char* colors, int* neededTime, int neededTimeSize) {\n    int\
        \ total = 0;\n    int runSum = neededTime[0];\n    int runMax = neededTime[0];\n\
        \n    for (int i = 1; i < neededTimeSize; ++i) {\n        if (colors[i] == colors[i\
        \ - 1]) {\n            runSum += neededTime[i];\n            if (neededTime[i]\
        \ > runMax) {\n                runMax = neededTime[i];\n            }\n    \
        \    } else {\n            total += runSum - runMax;\n            runSum = neededTime[i];\n\
        \            runMax = neededTime[i];\n        }\n    }\n\n    return total +\
        \ runSum - runMax;\n}"
      csharp: "public class Solution {\n    public int MinCost(string colors, int[]\
        \ neededTime) {\n        int total = 0;\n        int runSum = neededTime[0];\n\
        \        int runMax = neededTime[0];\n\n        for (int i = 1; i < colors.Length;\
        \ i++) {\n            if (colors[i] == colors[i - 1]) {\n                runSum\
        \ += neededTime[i];\n                runMax = Math.Max(runMax, neededTime[i]);\n\
        \            } else {\n                total += runSum - runMax;\n         \
        \       runSum = neededTime[i];\n                runMax = neededTime[i];\n \
        \           }\n        }\n\n        return total + runSum - runMax;\n    }\n\
        }"
      javascript: "/**\n * @param {string} colors\n * @param {number[]} neededTime\n\
        \ * @return {number}\n */\nvar minCost = function(colors, neededTime) {\n  \
        \  let total = 0;\n    let runSum = neededTime[0];\n    let runMax = neededTime[0];\n\
        \n    for (let i = 1; i < colors.length; i++) {\n        if (colors[i] === colors[i\
        \ - 1]) {\n            runSum += neededTime[i];\n            runMax = Math.max(runMax,\
        \ neededTime[i]);\n        } else {\n            total += runSum - runMax;\n\
        \            runSum = neededTime[i];\n            runMax = neededTime[i];\n\
        \        }\n    }\n\n    return total + runSum - runMax;\n};"
      typescript: "function minCost(colors: string, neededTime: number[]): number {\n\
        \    let total = 0;\n    let runSum = neededTime[0];\n    let runMax = neededTime[0];\n\
        \n    for (let i = 1; i < colors.length; i++) {\n        if (colors[i] === colors[i\
        \ - 1]) {\n            runSum += neededTime[i];\n            runMax = Math.max(runMax,\
        \ neededTime[i]);\n        } else {\n            total += runSum - runMax;\n\
        \            runSum = neededTime[i];\n            runMax = neededTime[i];\n\
        \        }\n    }\n\n    return total + runSum - runMax;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $colors\n     * @param\
        \ Integer[] $neededTime\n     * @return Integer\n     */\n    function minCost($colors,\
        \ $neededTime) {\n        $total = 0;\n        $runSum = $neededTime[0];\n \
        \       $runMax = $neededTime[0];\n        $length = strlen($colors);\n\n  \
        \      for ($i = 1; $i < $length; $i++) {\n            if ($colors[$i] === $colors[$i\
        \ - 1]) {\n                $runSum += $neededTime[$i];\n                $runMax\
        \ = max($runMax, $neededTime[$i]);\n            } else {\n                $total\
        \ += $runSum - $runMax;\n                $runSum = $neededTime[$i];\n      \
        \          $runMax = $neededTime[$i];\n            }\n        }\n\n        return\
        \ $total + $runSum - $runMax;\n    }\n}"
      swift: "class Solution {\n    func minCost(_ colors: String, _ neededTime: [Int])\
        \ -> Int {\n        let chars = Array(colors)\n        var total = 0\n     \
        \   var runSum = neededTime[0]\n        var runMax = neededTime[0]\n\n     \
        \   for i in 1..<chars.count {\n            if chars[i] == chars[i - 1] {\n\
        \                runSum += neededTime[i]\n                runMax = max(runMax,\
        \ neededTime[i])\n            } else {\n                total += runSum - runMax\n\
        \                runSum = neededTime[i]\n                runMax = neededTime[i]\n\
        \            }\n        }\n\n        return total + runSum - runMax\n    }\n\
        }"
      kotlin: "class Solution {\n    fun minCost(colors: String, neededTime: IntArray):\
        \ Int {\n        var total = 0\n        var runSum = neededTime[0]\n       \
        \ var runMax = neededTime[0]\n\n        for (i in 1 until colors.length) {\n\
        \            if (colors[i] == colors[i - 1]) {\n                runSum += neededTime[i]\n\
        \                runMax = maxOf(runMax, neededTime[i])\n            } else {\n\
        \                total += runSum - runMax\n                runSum = neededTime[i]\n\
        \                runMax = neededTime[i]\n            }\n        }\n\n      \
        \  return total + runSum - runMax\n    }\n}"
      dart: "class Solution {\n  int minCost(String colors, List<int> neededTime) {\n\
        \    var total = 0;\n    var runSum = neededTime[0];\n    var runMax = neededTime[0];\n\
        \n    for (var i = 1; i < colors.length; i++) {\n      if (colors[i] == colors[i\
        \ - 1]) {\n        runSum += neededTime[i];\n        runMax = runMax > neededTime[i]\
        \ ? runMax : neededTime[i];\n      } else {\n        total += runSum - runMax;\n\
        \        runSum = neededTime[i];\n        runMax = neededTime[i];\n      }\n\
        \    }\n\n    return total + runSum - runMax;\n  }\n}"
      go: "func minCost(colors string, neededTime []int) int {\n\ttotal := 0\n\trunSum\
        \ := neededTime[0]\n\trunMax := neededTime[0]\n\n\tfor i := 1; i < len(colors);\
        \ i++ {\n\t\tif colors[i] == colors[i-1] {\n\t\t\trunSum += neededTime[i]\n\t\
        \t\tif neededTime[i] > runMax {\n\t\t\t\trunMax = neededTime[i]\n\t\t\t}\n\t\
        \t} else {\n\t\t\ttotal += runSum - runMax\n\t\t\trunSum = neededTime[i]\n\t\
        \t\trunMax = neededTime[i]\n\t\t}\n\t}\n\n\treturn total + runSum - runMax\n\
        }"
      ruby: "# @param {String} colors\n# @param {Integer[]} needed_time\n# @return {Integer}\n\
        def min_cost(colors, needed_time)\n  total = 0\n  run_sum = needed_time[0]\n\
        \  run_max = needed_time[0]\n\n  (1...colors.length).each do |i|\n    if colors[i]\
        \ == colors[i - 1]\n      run_sum += needed_time[i]\n      run_max = [run_max,\
        \ needed_time[i]].max\n    else\n      total += run_sum - run_max\n      run_sum\
        \ = needed_time[i]\n      run_max = needed_time[i]\n    end\n  end\n\n  total\
        \ + run_sum - run_max\nend"
      scala: "object Solution {\n    def minCost(colors: String, neededTime: Array[Int]):\
        \ Int = {\n        var total = 0\n        var runSum = neededTime(0)\n     \
        \   var runMax = neededTime(0)\n\n        for (i <- 1 until colors.length) {\n\
        \            if (colors(i) == colors(i - 1)) {\n                runSum += neededTime(i)\n\
        \                runMax = runMax.max(neededTime(i))\n            } else {\n\
        \                total += runSum - runMax\n                runSum = neededTime(i)\n\
        \                runMax = neededTime(i)\n            }\n        }\n\n      \
        \  total + runSum - runMax\n    }\n}"
      rust: "impl Solution {\n    pub fn min_cost(colors: String, needed_time: Vec<i32>)\
        \ -> i32 {\n        let colors = colors.as_bytes();\n        let mut total =\
        \ 0;\n        let mut run_sum = needed_time[0];\n        let mut run_max = needed_time[0];\n\
        \n        for i in 1..colors.len() {\n            if colors[i] == colors[i -\
        \ 1] {\n                run_sum += needed_time[i];\n                run_max\
        \ = run_max.max(needed_time[i]);\n            } else {\n                total\
        \ += run_sum - run_max;\n                run_sum = needed_time[i];\n       \
        \         run_max = needed_time[i];\n            }\n        }\n\n        total\
        \ + run_sum - run_max\n    }\n}"
      racket: "(define/contract (min-cost colors neededTime)\n  (-> string? (listof\
        \ exact-integer?) exact-integer?)\n  (define n (string-length colors))\n  (define\
        \ total 0)\n  (define run-sum (first neededTime))\n  (define run-max (first\
        \ neededTime))\n  (for ([i (in-range 1 n)])\n    (if (char=? (string-ref colors\
        \ i) (string-ref colors (sub1 i)))\n        (begin\n          (set! run-sum\
        \ (+ run-sum (list-ref neededTime i)))\n          (set! run-max (max run-max\
        \ (list-ref neededTime i))))\n        (begin\n          (set! total (+ total\
        \ (- run-sum run-max)))\n          (set! run-sum (list-ref neededTime i))\n\
        \          (set! run-max (list-ref neededTime i)))))\n  (+ total (- run-sum\
        \ run-max)))"
      erlang: "-spec min_cost(Colors :: unicode:unicode_binary(), NeededTime :: [integer()])\
        \ -> integer().\nmin_cost(Colors, NeededTime) ->\n  [First | Rest] = binary_to_list(Colors),\n\
        \  [FirstTime | RestTimes] = NeededTime,\n  {Total, _, RunSum, RunMax} = lists:foldl(\n\
        \    fun({Color, Time}, {Acc, PrevColor, Sum, MaxTime}) ->\n      case Color\
        \ =:= PrevColor of\n        true -> {Acc, Color, Sum + Time, max(MaxTime, Time)};\n\
        \        false -> {Acc + Sum - MaxTime, Color, Time, Time}\n      end\n    end,\n\
        \    {0, First, FirstTime, FirstTime},\n    lists:zip(Rest, RestTimes)\n  ),\n\
        \  Total + RunSum - RunMax."
      elixir: "defmodule Solution do\n  @spec min_cost(colors :: String.t, needed_time\
        \ :: [integer]) :: integer\n  def min_cost(colors, needed_time) do\n    [first_time\
        \ | rest_times] = needed_time\n    [first_color | rest_colors] = String.to_charlist(colors)\n\
        \n    {total, _, run_sum, run_max} =\n      Enum.zip(rest_colors, rest_times)\n\
        \      |> Enum.reduce({0, first_color, first_time, first_time}, fn {color, time},\
        \ {total, prev_color, run_sum, run_max} ->\n        if color == prev_color do\n\
        \          {total, color, run_sum + time, max(run_max, time)}\n        else\n\
        \          {total + run_sum - run_max, color, time, time}\n        end\n   \
        \   end)\n\n    total + run_sum - run_max\n  end\nend"
    approach: 'Scan the balloons from left to right and group each maximal consecutive
      run of the same color. In every run, at least all but one balloon must be removed
      to avoid equal adjacent colors.


      For each run, add the removal times of all balloons except the one with the greatest
      removal time. Summing these costs across the runs gives the minimum time.'
    time_complexity: O(n), where n is the number of balloons, since each balloon is
      processed once.
    space_complexity: O(1), using only a few variables beyond the input.
    elapsed_time: 73.42002320289612
    model: gpt-6-luna
    generated_at: '2026-11-13 00:18:10 '
---

## Problem #1578: Minimum Time to Make Rope Colorful

**Difficulty:** Medium

**Topics:** Array, String, Dynamic Programming, Greedy

## Problem Description

<p>Alice has <code>n</code> balloons arranged on a rope. You are given a <strong>0-indexed</strong> string <code>colors</code> where <code>colors[i]</code> is the color of the <code>i<sup>th</sup></code> balloon.</p>

<p>Alice wants the rope to be <strong>colorful</strong>. She does not want <strong>two consecutive balloons</strong> to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it <strong>colorful</strong>. You are given a <strong>0-indexed</strong> integer array <code>neededTime</code> where <code>neededTime[i]</code> is the time (in seconds) that Bob needs to remove the <code>i<sup>th</sup></code> balloon from the rope.</p>

<p>Return <em>the <strong>minimum time</strong> Bob needs to make the rope <strong>colorful</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;abaac&quot;, neededTime = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> In the above image, &#39;a&#39; is blue, &#39;b&#39; is red, and &#39;c&#39; is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg" style="width: 244px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;abc&quot;, neededTime = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The rope is already colorful. Bob does not need to remove any balloons from the rope.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;aabaa&quot;, neededTime = [1,2,3,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == colors.length == neededTime.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= neededTime[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>colors</code> contains only lowercase English letters.</li>
</ul>


## Hints

1. Maintain the running sum and max value for repeated letters.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Scan the balloons from left to right and group each maximal consecutive run of the same color. In every run, at least all but one balloon must be removed to avoid equal adjacent colors.

For each run, add the removal times of all balloons except the one with the greatest removal time. Summing these costs across the runs gives the minimum time.

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
    int minCost(string colors, vector<int>& neededTime) {
        int total = 0;
        int runSum = neededTime[0];
        int runMax = neededTime[0];

        for (int i = 1; i < colors.size(); ++i) {
            if (colors[i] == colors[i - 1]) {
                runSum += neededTime[i];
                runMax = max(runMax, neededTime[i]);
            } else {
                total += runSum - runMax;
                runSum = neededTime[i];
                runMax = neededTime[i];
            }
        }

        return total + runSum - runMax;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minCost(String colors, int[] neededTime) {
        int total = 0;
        int runSum = neededTime[0];
        int runMax = neededTime[0];

        for (int i = 1; i < colors.length(); i++) {
            if (colors.charAt(i) == colors.charAt(i - 1)) {
                runSum += neededTime[i];
                runMax = Math.max(runMax, neededTime[i]);
            } else {
                total += runSum - runMax;
                runSum = neededTime[i];
                runMax = neededTime[i];
            }
        }

        return total + runSum - runMax;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total = 0
        run_sum = neededTime[0]
        run_max = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                run_sum += neededTime[i]
                run_max = max(run_max, neededTime[i])
            else:
                total += run_sum - run_max
                run_sum = neededTime[i]
                run_max = neededTime[i]

        return total + run_sum - run_max
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total = 0
        run_sum = neededTime[0]
        run_max = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                run_sum += neededTime[i]
                run_max = max(run_max, neededTime[i])
            else:
                total += run_sum - run_max
                run_sum = neededTime[i]
                run_max = neededTime[i]

        return total + run_sum - run_max
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minCost(char* colors, int* neededTime, int neededTimeSize) {
    int total = 0;
    int runSum = neededTime[0];
    int runMax = neededTime[0];

    for (int i = 1; i < neededTimeSize; ++i) {
        if (colors[i] == colors[i - 1]) {
            runSum += neededTime[i];
            if (neededTime[i] > runMax) {
                runMax = neededTime[i];
            }
        } else {
            total += runSum - runMax;
            runSum = neededTime[i];
            runMax = neededTime[i];
        }
    }

    return total + runSum - runMax;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int total = 0;
        int runSum = neededTime[0];
        int runMax = neededTime[0];

        for (int i = 1; i < colors.Length; i++) {
            if (colors[i] == colors[i - 1]) {
                runSum += neededTime[i];
                runMax = Math.Max(runMax, neededTime[i]);
            } else {
                total += runSum - runMax;
                runSum = neededTime[i];
                runMax = neededTime[i];
            }
        }

        return total + runSum - runMax;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    let total = 0;
    let runSum = neededTime[0];
    let runMax = neededTime[0];

    for (let i = 1; i < colors.length; i++) {
        if (colors[i] === colors[i - 1]) {
            runSum += neededTime[i];
            runMax = Math.max(runMax, neededTime[i]);
        } else {
            total += runSum - runMax;
            runSum = neededTime[i];
            runMax = neededTime[i];
        }
    }

    return total + runSum - runMax;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minCost(colors: string, neededTime: number[]): number {
    let total = 0;
    let runSum = neededTime[0];
    let runMax = neededTime[0];

    for (let i = 1; i < colors.length; i++) {
        if (colors[i] === colors[i - 1]) {
            runSum += neededTime[i];
            runMax = Math.max(runMax, neededTime[i]);
        } else {
            total += runSum - runMax;
            runSum = neededTime[i];
            runMax = neededTime[i];
        }
    }

    return total + runSum - runMax;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        $total = 0;
        $runSum = $neededTime[0];
        $runMax = $neededTime[0];
        $length = strlen($colors);

        for ($i = 1; $i < $length; $i++) {
            if ($colors[$i] === $colors[$i - 1]) {
                $runSum += $neededTime[$i];
                $runMax = max($runMax, $neededTime[$i]);
            } else {
                $total += $runSum - $runMax;
                $runSum = $neededTime[$i];
                $runMax = $neededTime[$i];
            }
        }

        return $total + $runSum - $runMax;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
        let chars = Array(colors)
        var total = 0
        var runSum = neededTime[0]
        var runMax = neededTime[0]

        for i in 1..<chars.count {
            if chars[i] == chars[i - 1] {
                runSum += neededTime[i]
                runMax = max(runMax, neededTime[i])
            } else {
                total += runSum - runMax
                runSum = neededTime[i]
                runMax = neededTime[i]
            }
        }

        return total + runSum - runMax
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        var total = 0
        var runSum = neededTime[0]
        var runMax = neededTime[0]

        for (i in 1 until colors.length) {
            if (colors[i] == colors[i - 1]) {
                runSum += neededTime[i]
                runMax = maxOf(runMax, neededTime[i])
            } else {
                total += runSum - runMax
                runSum = neededTime[i]
                runMax = neededTime[i]
            }
        }

        return total + runSum - runMax
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minCost(String colors, List<int> neededTime) {
    var total = 0;
    var runSum = neededTime[0];
    var runMax = neededTime[0];

    for (var i = 1; i < colors.length; i++) {
      if (colors[i] == colors[i - 1]) {
        runSum += neededTime[i];
        runMax = runMax > neededTime[i] ? runMax : neededTime[i];
      } else {
        total += runSum - runMax;
        runSum = neededTime[i];
        runMax = neededTime[i];
      }
    }

    return total + runSum - runMax;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minCost(colors string, neededTime []int) int {
	total := 0
	runSum := neededTime[0]
	runMax := neededTime[0]

	for i := 1; i < len(colors); i++ {
		if colors[i] == colors[i-1] {
			runSum += neededTime[i]
			if neededTime[i] > runMax {
				runMax = neededTime[i]
			}
		} else {
			total += runSum - runMax
			runSum = neededTime[i]
			runMax = neededTime[i]
		}
	}

	return total + runSum - runMax
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} colors
# @param {Integer[]} needed_time
# @return {Integer}
def min_cost(colors, needed_time)
  total = 0
  run_sum = needed_time[0]
  run_max = needed_time[0]

  (1...colors.length).each do |i|
    if colors[i] == colors[i - 1]
      run_sum += needed_time[i]
      run_max = [run_max, needed_time[i]].max
    else
      total += run_sum - run_max
      run_sum = needed_time[i]
      run_max = needed_time[i]
    end
  end

  total + run_sum - run_max
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minCost(colors: String, neededTime: Array[Int]): Int = {
        var total = 0
        var runSum = neededTime(0)
        var runMax = neededTime(0)

        for (i <- 1 until colors.length) {
            if (colors(i) == colors(i - 1)) {
                runSum += neededTime(i)
                runMax = runMax.max(neededTime(i))
            } else {
                total += runSum - runMax
                runSum = neededTime(i)
                runMax = neededTime(i)
            }
        }

        total + runSum - runMax
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let colors = colors.as_bytes();
        let mut total = 0;
        let mut run_sum = needed_time[0];
        let mut run_max = needed_time[0];

        for i in 1..colors.len() {
            if colors[i] == colors[i - 1] {
                run_sum += needed_time[i];
                run_max = run_max.max(needed_time[i]);
            } else {
                total += run_sum - run_max;
                run_sum = needed_time[i];
                run_max = needed_time[i];
            }
        }

        total + run_sum - run_max
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-cost colors neededTime)
  (-> string? (listof exact-integer?) exact-integer?)
  (define n (string-length colors))
  (define total 0)
  (define run-sum (first neededTime))
  (define run-max (first neededTime))
  (for ([i (in-range 1 n)])
    (if (char=? (string-ref colors i) (string-ref colors (sub1 i)))
        (begin
          (set! run-sum (+ run-sum (list-ref neededTime i)))
          (set! run-max (max run-max (list-ref neededTime i))))
        (begin
          (set! total (+ total (- run-sum run-max)))
          (set! run-sum (list-ref neededTime i))
          (set! run-max (list-ref neededTime i)))))
  (+ total (- run-sum run-max)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_cost(Colors :: unicode:unicode_binary(), NeededTime :: [integer()]) -> integer().
min_cost(Colors, NeededTime) ->
  [First | Rest] = binary_to_list(Colors),
  [FirstTime | RestTimes] = NeededTime,
  {Total, _, RunSum, RunMax} = lists:foldl(
    fun({Color, Time}, {Acc, PrevColor, Sum, MaxTime}) ->
      case Color =:= PrevColor of
        true -> {Acc, Color, Sum + Time, max(MaxTime, Time)};
        false -> {Acc + Sum - MaxTime, Color, Time, Time}
      end
    end,
    {0, First, FirstTime, FirstTime},
    lists:zip(Rest, RestTimes)
  ),
  Total + RunSum - RunMax.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_cost(colors :: String.t, needed_time :: [integer]) :: integer
  def min_cost(colors, needed_time) do
    [first_time | rest_times] = needed_time
    [first_color | rest_colors] = String.to_charlist(colors)

    {total, _, run_sum, run_max} =
      Enum.zip(rest_colors, rest_times)
      |> Enum.reduce({0, first_color, first_time, first_time}, fn {color, time}, {total, prev_color, run_sum, run_max} ->
        if color == prev_color do
          {total, color, run_sum + time, max(run_max, time)}
        else
          {total + run_sum - run_max, color, time, time}
        end
      end)

    total + run_sum - run_max
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the number of balloons, since each balloon is processed once.
- **Space Complexity:** O(1), using only a few variables beyond the input.
