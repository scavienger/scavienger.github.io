---
layout: post
title: "Minimum Cost of Buying Candies With Discount"
date: 2026-06-01 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumCost(vector<int>& cost) {\n  \
        \      sort(cost.begin(), cost.end(), greater<int>());\n        int totalCost\
        \ = 0;\n        for (int i = 0; i < cost.size(); ++i) {\n            if ((i\
        \ + 1) % 3 != 0) {\n                totalCost += cost[i];\n            }\n \
        \       }\n        return totalCost;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minimumCost(int[]\
        \ cost) {\n        Arrays.sort(cost);\n        int totalCost = 0;\n        int\
        \ count = 0;\n        for (int i = cost.length - 1; i >= 0; i--) {\n       \
        \     count++;\n            if (count % 3 != 0) {\n                totalCost\
        \ += cost[i];\n            }\n        }\n        return totalCost;\n    }\n}"
      python: "class Solution(object):\n    def minimumCost(self, cost):\n        \"\
        \"\"\n        :type cost: List[int]\n        :rtype: int\n        \"\"\"\n \
        \       cost.sort(reverse=True)\n        total_cost = 0\n        for i in range(len(cost)):\n\
        \            if (i + 1) % 3 != 0:\n                total_cost += cost[i]\n \
        \       return total_cost"
      python3: "class Solution:\n    def minimumCost(self, cost: List[int]) -> int:\n\
        \        cost.sort(reverse=True)\n        total_cost = 0\n        for i in range(len(cost)):\n\
        \            if (i + 1) % 3 != 0:\n                total_cost += cost[i]\n \
        \       return total_cost"
      c: "int compare(const void *a, const void *b) {\n    return (*(int*)b - *(int*)a);\n\
        }\n\nint minimumCost(int* cost, int costSize) {\n    qsort(cost, costSize, sizeof(int),\
        \ compare);\n    int totalCost = 0;\n    for (int i = 0; i < costSize; i++)\
        \ {\n        if ((i + 1) % 3 != 0) {\n            totalCost += cost[i];\n  \
        \      }\n    }\n    return totalCost;\n}"
      csharp: "public class Solution {\n    public int MinimumCost(int[] cost) {\n \
        \       Array.Sort(cost);\n        Array.Reverse(cost);\n        int totalCost\
        \ = 0;\n        for (int i = 0; i < cost.Length; i++) {\n            if ((i\
        \ + 1) % 3 != 0) {\n                totalCost += cost[i];\n            }\n \
        \       }\n        return totalCost;\n    }\n}"
      javascript: "/**\n * @param {number[]} cost\n * @return {number}\n */\nvar minimumCost\
        \ = function(cost) {\n    cost.sort((a, b) => b - a);\n    let totalCost = 0;\n\
        \    for (let i = 0; i < cost.length; i++) {\n        if ((i + 1) % 3 !== 0)\
        \ {\n            totalCost += cost[i];\n        }\n    }\n    return totalCost;\n\
        };"
      typescript: "function minimumCost(cost: number[]): number {\n    cost.sort((a,\
        \ b) => b - a);\n    let total = 0;\n    for (let i = 0; i < cost.length; i++)\
        \ {\n        if ((i + 1) % 3 !== 0) {\n            total += cost[i];\n     \
        \   }\n    }\n    return total;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $cost\n     * @return\
        \ Integer\n     */\n    function minimumCost($cost) {\n        rsort($cost);\n\
        \        $total = 0;\n        $n = count($cost);\n        for ($i = 0; $i <\
        \ $n; $i++) {\n            if (($i + 1) % 3 !== 0) {\n                $total\
        \ += $cost[$i];\n            }\n        }\n        return $total;\n    }\n}"
      swift: "class Solution {\n    func minimumCost(_ cost: [Int]) -> Int {\n     \
        \   let sortedCost = cost.sorted(by: >)\n        var total = 0\n        for\
        \ i in 0..<sortedCost.count {\n            if (i + 1) % 3 != 0 {\n         \
        \       total += sortedCost[i]\n            }\n        }\n        return total\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minimumCost(cost: IntArray): Int {\n      \
        \  cost.sortDescending()\n        var total = 0\n        for (i in cost.indices)\
        \ {\n            if ((i + 1) % 3 != 0) {\n                total += cost[i]\n\
        \            }\n        }\n        return total\n    }\n}"
      dart: "class Solution {\n  int minimumCost(List<int> cost) {\n    cost.sort((a,\
        \ b) => b.compareTo(a));\n    int total = 0;\n    for (int i = 0; i < cost.length;\
        \ i++) {\n      if ((i + 1) % 3 != 0) {\n        total += cost[i];\n      }\n\
        \    }\n    return total;\n  }\n}"
      go: "import \"sort\"\n\nfunc minimumCost(cost []int) int {\n    sort.Slice(cost,\
        \ func(i, j int) bool {\n        return cost[i] > cost[j]\n    })\n    total\
        \ := 0\n    for i := 0; i < len(cost); i++ {\n        if (i+1)%3 != 0 {\n  \
        \          total += cost[i]\n        }\n    }\n    return total\n}"
      ruby: "# @param {Integer[]} cost\n# @return {Integer}\ndef minimum_cost(cost)\n\
        \  total = 0\n  sorted_cost = cost.sort.reverse\n  sorted_cost.each_with_index\
        \ do |c, i|\n    total += c if (i + 1) % 3 != 0\n  end\n  total\nend"
      scala: "object Solution {\n    def minimumCost(cost: Array[Int]): Int = {\n  \
        \      val sortedCost = cost.sorted(Ordering.Int.reverse)\n        var total\
        \ = 0\n        for (i <- sortedCost.indices) {\n            if ((i + 1) % 3\
        \ != 0) {\n                total += sortedCost(i)\n            }\n        }\n\
        \        total\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_cost(cost: Vec<i32>) -> i32 {\n   \
        \     let mut cost = cost;\n        cost.sort_unstable_by(|a, b| b.cmp(a));\n\
        \        let mut total = 0;\n        for (i, &c) in cost.iter().enumerate()\
        \ {\n            if (i + 1) % 3 != 0 {\n                total += c;\n      \
        \      }\n        }\n        total\n    }\n}"
      racket: "(define/contract (minimum-cost cost)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (for/sum ([c (sort cost >)]\n            [i (in-naturals 1)])\n    (if (zero?\
        \ (remainder i 3)) 0 c)))"
      erlang: "-spec minimum_cost(Cost :: [integer()]) -> integer().\nminimum_cost(Cost)\
        \ ->\n  Sorted = lists:reverse(lists:sort(Cost)),\n  calculate(Sorted).\n\n\
        calculate([]) -> 0;\ncalculate([A]) -> A;\ncalculate([A, B]) -> A + B;\ncalculate([A,\
        \ B, _C | Rest]) -> A + B + calculate(Rest)."
      elixir: "defmodule Solution do\n  @spec minimum_cost(cost :: [integer]) :: integer\n\
        \  def minimum_cost(cost) do\n    cost\n    |> Enum.sort(:desc)\n    |> Enum.chunk_every(3)\n\
        \    |> Enum.map(fn\n      [a, b, _] -> a + b\n      other -> Enum.sum(other)\n\
        \    end)\n    |> Enum.sum()\n  end\nend"
    approach: 'To minimize the total cost, we should aim to maximize the value of the
      candies we get for free. Since we can get a third candy for free if its cost is
      less than or equal to the minimum of the two candies we buy, the optimal strategy
      is a greedy one: sort the candies in descending order of cost and group them in
      threes. In each group of three candies $(c_1, c_2, c_3)$ where $c_1 \ge c_2 \ge
      c_3$, we pay for the two most expensive ones ($c_1$ and $c_2$) and receive the
      third ($c_3$) for free.


      By following this pattern, we ensure that every third candy we ''skip'' (the one
      at index $i$ where $(i+1) \% 3 == 0$) is as expensive as possible relative to
      the remaining candies. After sorting the costs in non-increasing order, we iterate
      through the list and add the cost of every candy to the total sum, except for
      every third candy (indices 2, 5, 8, etc.), which represents the discount applied
      to the most valuable set possible.'
    time_complexity: O(n log n) where n is the number of candies. This complexity is
      dominated by the sorting step. The subsequent single pass through the array to
      calculate the sum takes O(n) time.
    space_complexity: O(1) or O(n) depending on the language and the sorting implementation.
      In C++, std::sort typically uses O(log n) extra space for recursion, while in
      Python, Timsort uses O(n) auxiliary space.
    elapsed_time: 37.690678119659424
    model: gemini-3-flash-preview
    generated_at: '2026-06-01 02:54:14 '
---

## Problem #2144: Minimum Cost of Buying Candies With Discount

**Difficulty:** Easy

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>A shop is selling candies at a discount. For <strong>every two</strong> candies sold, the shop gives a <strong>third</strong> candy for <strong>free</strong>.</p>

<p>The customer can choose <strong>any</strong> candy to take away for free as long as the cost of the chosen candy is less than or equal to the <strong>minimum</strong> cost of the two candies bought.</p>

<ul>
	<li>For example, if there are <code>4</code> candies with costs <code>1</code>, <code>2</code>, <code>3</code>, and <code>4</code>, and the customer buys candies with costs <code>2</code> and <code>3</code>, they&nbsp;can take the candy with cost <code>1</code> for free, but not the candy with cost <code>4</code>.</li>
</ul>

<p>Given a <strong>0-indexed</strong> integer array <code>cost</code>, where <code>cost[i]</code> denotes the cost of the <code>i<sup>th</sup></code> candy, return <em>the <strong>minimum cost</strong> of buying <strong>all</strong> the candies</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> cost = [1,2,3]
<strong>Output:</strong> 5
<strong>Explanation:</strong> We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
The total cost of buying all candies is 2 + 3 = 5. This is the <strong>only</strong> way we can buy the candies.
Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> cost = [6,5,7,9,2,2]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The way in which we can get the minimum cost is described below:
- Buy candies with costs 9 and 7
- Take the candy with cost 6 for free
- We buy candies with costs 5 and 2
- Take the last remaining candy with cost 2 for free
Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> cost = [5,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free.
Hence, the minimum cost to buy all candies is 5 + 5 = 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= cost.length &lt;= 100</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 100</code></li>
</ul>


## Hints

1. If we consider costs from high to low, what is the maximum cost of a single candy that we can get for free?

2. How can we generalize this approach to maximize the costs of the candies we get for free?

3. Can “sorting” the array help us find the minimum cost?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To minimize the total cost, we should aim to maximize the value of the candies we get for free. Since we can get a third candy for free if its cost is less than or equal to the minimum of the two candies we buy, the optimal strategy is a greedy one: sort the candies in descending order of cost and group them in threes. In each group of three candies $(c_1, c_2, c_3)$ where $c_1 \ge c_2 \ge c_3$, we pay for the two most expensive ones ($c_1$ and $c_2$) and receive the third ($c_3$) for free.

By following this pattern, we ensure that every third candy we 'skip' (the one at index $i$ where $(i+1) \% 3 == 0$) is as expensive as possible relative to the remaining candies. After sorting the costs in non-increasing order, we iterate through the list and add the cost of every candy to the total sum, except for every third candy (indices 2, 5, 8, etc.), which represents the discount applied to the most valuable set possible.

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
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(), cost.end(), greater<int>());
        int totalCost = 0;
        for (int i = 0; i < cost.size(); ++i) {
            if ((i + 1) % 3 != 0) {
                totalCost += cost[i];
            }
        }
        return totalCost;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int totalCost = 0;
        int count = 0;
        for (int i = cost.length - 1; i >= 0; i--) {
            count++;
            if (count % 3 != 0) {
                totalCost += cost[i];
            }
        }
        return totalCost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        total_cost = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
        return total_cost
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total_cost = 0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
        return total_cost
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

int minimumCost(int* cost, int costSize) {
    qsort(cost, costSize, sizeof(int), compare);
    int totalCost = 0;
    for (int i = 0; i < costSize; i++) {
        if ((i + 1) % 3 != 0) {
            totalCost += cost[i];
        }
    }
    return totalCost;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumCost(int[] cost) {
        Array.Sort(cost);
        Array.Reverse(cost);
        int totalCost = 0;
        for (int i = 0; i < cost.Length; i++) {
            if ((i + 1) % 3 != 0) {
                totalCost += cost[i];
            }
        }
        return totalCost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(cost) {
    cost.sort((a, b) => b - a);
    let totalCost = 0;
    for (let i = 0; i < cost.length; i++) {
        if ((i + 1) % 3 !== 0) {
            totalCost += cost[i];
        }
    }
    return totalCost;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumCost(cost: number[]): number {
    cost.sort((a, b) => b - a);
    let total = 0;
    for (let i = 0; i < cost.length; i++) {
        if ((i + 1) % 3 !== 0) {
            total += cost[i];
        }
    }
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
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($cost) {
        rsort($cost);
        $total = 0;
        $n = count($cost);
        for ($i = 0; $i < $n; $i++) {
            if (($i + 1) % 3 !== 0) {
                $total += $cost[$i];
            }
        }
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
    func minimumCost(_ cost: [Int]) -> Int {
        let sortedCost = cost.sorted(by: >)
        var total = 0
        for i in 0..<sortedCost.count {
            if (i + 1) % 3 != 0 {
                total += sortedCost[i]
            }
        }
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
    fun minimumCost(cost: IntArray): Int {
        cost.sortDescending()
        var total = 0
        for (i in cost.indices) {
            if ((i + 1) % 3 != 0) {
                total += cost[i]
            }
        }
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
  int minimumCost(List<int> cost) {
    cost.sort((a, b) => b.compareTo(a));
    int total = 0;
    for (int i = 0; i < cost.length; i++) {
      if ((i + 1) % 3 != 0) {
        total += cost[i];
      }
    }
    return total;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minimumCost(cost []int) int {
    sort.Slice(cost, func(i, j int) bool {
        return cost[i] > cost[j]
    })
    total := 0
    for i := 0; i < len(cost); i++ {
        if (i+1)%3 != 0 {
            total += cost[i]
        }
    }
    return total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(cost)
  total = 0
  sorted_cost = cost.sort.reverse
  sorted_cost.each_with_index do |c, i|
    total += c if (i + 1) % 3 != 0
  end
  total
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumCost(cost: Array[Int]): Int = {
        val sortedCost = cost.sorted(Ordering.Int.reverse)
        var total = 0
        for (i <- sortedCost.indices) {
            if ((i + 1) % 3 != 0) {
                total += sortedCost(i)
            }
        }
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
    pub fn minimum_cost(cost: Vec<i32>) -> i32 {
        let mut cost = cost;
        cost.sort_unstable_by(|a, b| b.cmp(a));
        let mut total = 0;
        for (i, &c) in cost.iter().enumerate() {
            if (i + 1) % 3 != 0 {
                total += c;
            }
        }
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-cost cost)
  (-> (listof exact-integer?) exact-integer?)
  (for/sum ([c (sort cost >)]
            [i (in-naturals 1)])
    (if (zero? (remainder i 3)) 0 c)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_cost(Cost :: [integer()]) -> integer().
minimum_cost(Cost) ->
  Sorted = lists:reverse(lists:sort(Cost)),
  calculate(Sorted).

calculate([]) -> 0;
calculate([A]) -> A;
calculate([A, B]) -> A + B;
calculate([A, B, _C | Rest]) -> A + B + calculate(Rest).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_cost(cost :: [integer]) :: integer
  def minimum_cost(cost) do
    cost
    |> Enum.sort(:desc)
    |> Enum.chunk_every(3)
    |> Enum.map(fn
      [a, b, _] -> a + b
      other -> Enum.sum(other)
    end)
    |> Enum.sum()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) where n is the number of candies. This complexity is dominated by the sorting step. The subsequent single pass through the array to calculate the sum takes O(n) time.
- **Space Complexity:** O(1) or O(n) depending on the language and the sorting implementation. In C++, std::sort typically uses O(log n) extra space for recursion, while in Python, Timsort uses O(n) auxiliary space.
