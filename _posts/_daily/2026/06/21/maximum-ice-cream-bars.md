---
layout: post
title: "Maximum Ice Cream Bars"
date: 2026-06-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting", "Counting Sort"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-ice-cream-bars/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxIceCream(vector<int>& costs, int coins)\
        \ {\n        int max_cost = 0;\n        for (int cost : costs) {\n         \
        \   if (cost > max_cost) max_cost = cost;\n        }\n\n        vector<int>\
        \ freq(max_cost + 1, 0);\n        for (int cost : costs) {\n            freq[cost]++;\n\
        \        }\n\n        int count = 0;\n        for (int i = 1; i <= max_cost;\
        \ ++i) {\n            if (freq[i] == 0) continue;\n            if (coins < i)\
        \ break;\n\n            int can_buy = coins / i;\n            if (can_buy >\
        \ freq[i]) can_buy = freq[i];\n\n            count += can_buy;\n           \
        \ coins -= can_buy * i;\n        }\n\n        return count;\n    }\n};"
      java: "class Solution {\n    public int maxIceCream(int[] costs, int coins) {\n\
        \        int maxCost = 0;\n        for (int cost : costs) {\n            if\
        \ (cost > maxCost) maxCost = cost;\n        }\n\n        int[] freq = new int[maxCost\
        \ + 1];\n        for (int cost : costs) {\n            freq[cost]++;\n     \
        \   }\n\n        int count = 0;\n        for (int i = 1; i <= maxCost; i++)\
        \ {\n            if (freq[i] == 0) continue;\n            if (coins < i) break;\n\
        \n            int canBuy = Math.min(freq[i], coins / i);\n            count\
        \ += canBuy;\n            coins -= canBuy * i;\n        }\n\n        return\
        \ count;\n    }\n}"
      python: "class Solution(object):\n    def maxIceCream(self, costs, coins):\n \
        \       \"\"\"\n        :type costs: List[int]\n        :type coins: int\n \
        \       :rtype: int\n        \"\"\"\n        if not costs:\n            return\
        \ 0\n\n        max_cost = 0\n        for cost in costs:\n            if cost\
        \ > max_cost:\n                max_cost = cost\n\n        freq = [0] * (max_cost\
        \ + 1)\n        for cost in costs:\n            freq[cost] += 1\n\n        count\
        \ = 0\n        for i in range(1, max_cost + 1):\n            if freq[i] == 0:\n\
        \                continue\n            if coins < i:\n                break\n\
        \n            can_buy = min(freq[i], coins // i)\n            count += can_buy\n\
        \            coins -= can_buy * i\n\n        return count"
      python3: "class Solution:\n    def maxIceCream(self, costs: List[int], coins:\
        \ int) -> int:\n        if not costs:\n            return 0\n\n        max_cost\
        \ = max(costs)\n        freq = [0] * (max_cost + 1)\n\n        for cost in costs:\n\
        \            freq[cost] += 1\n\n        count = 0\n        for i in range(1,\
        \ max_cost + 1):\n            if freq[i] == 0:\n                continue\n \
        \           if coins < i:\n                break\n\n            can_buy = min(freq[i],\
        \ coins // i)\n            count += can_buy\n            coins -= can_buy *\
        \ i\n\n        return count"
      c: "int maxIceCream(int* costs, int costsSize, int coins) {\n    int max_cost\
        \ = 0;\n    for (int i = 0; i < costsSize; i++) {\n        if (costs[i] > max_cost)\
        \ {\n            max_cost = costs[i];\n        }\n    }\n\n    int* freq = (int*)calloc(max_cost\
        \ + 1, sizeof(int));\n    if (!freq) return 0;\n\n    for (int i = 0; i < costsSize;\
        \ i++) {\n        freq[costs[i]]++;\n    }\n\n    int total_bars = 0;\n    for\
        \ (int i = 1; i <= max_cost; i++) {\n        if (freq[i] == 0) continue;\n \
        \       if (coins < i) break;\n\n        int can_buy = coins / i;\n        if\
        \ (can_buy > freq[i]) {\n            can_buy = freq[i];\n        }\n\n     \
        \   total_bars += can_buy;\n        coins -= can_buy * i;\n    }\n\n    free(freq);\n\
        \    return total_bars;\n}"
      csharp: "public class Solution {\n    public int MaxIceCream(int[] costs, int\
        \ coins) {\n        int max = 0;\n        foreach (int cost in costs) {\n  \
        \          if (cost > max) max = cost;\n        }\n\n        int[] frequency\
        \ = new int[max + 1];\n        foreach (int cost in costs) {\n            frequency[cost]++;\n\
        \        }\n\n        int count = 0;\n        for (int i = 1; i <= max; i++)\
        \ {\n            if (frequency[i] == 0) continue;\n            if (coins < i)\
        \ break;\n\n            long canBuy = Math.Min((long)frequency[i], (long)coins\
        \ / i);\n            count += (int)canBuy;\n            coins -= (int)canBuy\
        \ * i;\n        }\n\n        return count;\n    }\n}"
      javascript: "/**\n * @param {number[]} costs\n * @param {number} coins\n * @return\
        \ {number}\n */\nvar maxIceCream = function(costs, coins) {\n    let max = 0;\n\
        \    for (let i = 0; i < costs.length; i++) {\n        if (costs[i] > max) max\
        \ = costs[i];\n    }\n\n    let frequency = new Int32Array(max + 1);\n    for\
        \ (let i = 0; i < costs.length; i++) {\n        frequency[costs[i]]++;\n   \
        \ }\n\n    let count = 0;\n    for (let i = 1; i <= max; i++) {\n        if\
        \ (frequency[i] === 0) continue;\n        if (coins < i) break;\n\n        let\
        \ canBuy = Math.min(frequency[i], Math.floor(coins / i));\n        count +=\
        \ canBuy;\n        coins -= canBuy * i;\n    }\n\n    return count;\n};"
      typescript: "function maxIceCream(costs: number[], coins: number): number {\n\
        \    let max = 0;\n    for (let i = 0; i < costs.length; i++) {\n        if\
        \ (costs[i] > max) max = costs[i];\n    }\n\n    let frequency = new Int32Array(max\
        \ + 1);\n    for (let i = 0; i < costs.length; i++) {\n        frequency[costs[i]]++;\n\
        \    }\n\n    let count = 0;\n    for (let i = 1; i <= max; i++) {\n       \
        \ if (frequency[i] === 0) continue;\n        if (coins < i) break;\n\n     \
        \   let canBuy = Math.min(frequency[i], Math.floor(coins / i));\n        count\
        \ += canBuy;\n        coins -= canBuy * i;\n    }\n\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $costs\n     * @param\
        \ Integer $coins\n     * @return Integer\n     */\n    function maxIceCream($costs,\
        \ $coins) {\n        $max = 0;\n        foreach ($costs as $cost) {\n      \
        \      if ($cost > $max) $max = $cost;\n        }\n\n        $frequency = array_fill(0,\
        \ $max + 1, 0);\n        foreach ($costs as $cost) {\n            $frequency[$cost]++;\n\
        \        }\n\n        $count = 0;\n        for ($i = 1; $i <= $max; $i++) {\n\
        \            if ($frequency[$i] === 0) continue;\n            if ($coins < $i)\
        \ break;\n\n            $canBuy = min($frequency[$i], (int)($coins / $i));\n\
        \            $count += $canBuy;\n            $coins -= $canBuy * $i;\n     \
        \   }\n\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func maxIceCream(_ costs: [Int], _ coins: Int) ->\
        \ Int {\n        guard let maxCost = costs.max() else { return 0 }\n\n     \
        \   var frequency = Array(repeating: 0, count: maxCost + 1)\n        for cost\
        \ in costs {\n            frequency[cost] += 1\n        }\n\n        var count\
        \ = 0\n        var remainingCoins = coins\n\n        for i in 1...maxCost {\n\
        \            if frequency[i] == 0 { continue }\n            if remainingCoins\
        \ < i { break }\n\n            let canBuy = min(frequency[i], remainingCoins\
        \ / i)\n            count += canBuy\n            remainingCoins -= canBuy *\
        \ i\n        }\n\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun maxIceCream(costs: IntArray, coins: Int): Int\
        \ {\n        var maxCost = 0\n        for (cost in costs) {\n            if\
        \ (cost > maxCost) maxCost = cost\n        }\n\n        val count = IntArray(maxCost\
        \ + 1)\n        for (cost in costs) {\n            count[cost]++\n        }\n\
        \n        var totalIceCreams = 0\n        var remainingCoins = coins\n\n   \
        \     for (price in 1..maxCost) {\n            if (count[price] == 0) continue\n\
        \            if (remainingCoins < price) break\n\n            val canBuy = remainingCoins\
        \ / price\n            val num = if (count[price] < canBuy) count[price] else\
        \ canBuy\n\n            totalIceCreams += num\n            remainingCoins -=\
        \ num * price\n        }\n\n        return totalIceCreams\n    }\n}"
      dart: "class Solution {\n  int maxIceCream(List<int> costs, int coins) {\n   \
        \ int maxCost = 0;\n    for (var cost in costs) {\n      if (cost > maxCost)\
        \ maxCost = cost;\n    }\n\n    List<int> count = List<int>.filled(maxCost +\
        \ 1, 0);\n    for (var cost in costs) {\n      count[cost]++;\n    }\n\n   \
        \ int totalIceCreams = 0;\n    int remainingCoins = coins;\n\n    for (int price\
        \ = 1; price <= maxCost; price++) {\n      if (count[price] == 0) continue;\n\
        \      if (remainingCoins < price) break;\n\n      int canBuy = remainingCoins\
        \ ~/ price;\n      int num = count[price] < canBuy ? count[price] : canBuy;\n\
        \n      totalIceCreams += num;\n      remainingCoins -= num * price;\n    }\n\
        \n    return totalIceCreams;\n  }\n}"
      go: "func maxIceCream(costs []int, coins int) int {\n    maxCost := 0\n    for\
        \ _, cost := range costs {\n        if cost > maxCost {\n            maxCost\
        \ = cost\n        }\n    }\n\n    count := make([]int, maxCost+1)\n    for _,\
        \ cost := range costs {\n        count[cost]++\n    }\n\n    totalIceCreams\
        \ := 0\n    remainingCoins := coins\n\n    for price := 1; price <= maxCost;\
        \ price++ {\n        if count[price] == 0 {\n            continue\n        }\n\
        \        if remainingCoins < price {\n            break\n        }\n\n     \
        \   canBuy := remainingCoins / price\n        num := count[price]\n        if\
        \ canBuy < num {\n            num = canBuy\n        }\n\n        totalIceCreams\
        \ += num\n        remainingCoins -= num * price\n    }\n\n    return totalIceCreams\n\
        }"
      ruby: "def max_ice_cream(costs, coins)\n  max_cost = costs.max\n  count = Array.new(max_cost\
        \ + 1, 0)\n  costs.each { |cost| count[cost] += 1 }\n\n  total_ice_creams =\
        \ 0\n  remaining_coins = coins\n\n  (1..max_cost).each do |price|\n    next\
        \ if count[price] == 0\n    break if remaining_coins < price\n\n    num = [count[price],\
        \ remaining_coins / price].min\n    total_ice_creams += num\n    remaining_coins\
        \ -= num * price\n  end\n\n  total_ice_creams\nend"
      scala: "object Solution {\n    def maxIceCream(costs: Array[Int], coins: Int):\
        \ Int = {\n        var maxCost = 0\n        var i = 0\n        while (i < costs.length)\
        \ {\n            if (costs(i) > maxCost) maxCost = costs(i)\n            i +=\
        \ 1\n        }\n\n        val count = new Array[Int](maxCost + 1)\n        i\
        \ = 0\n        while (i < costs.length) {\n            count(costs(i)) += 1\n\
        \            i += 1\n        }\n\n        var totalIceCreams = 0\n        var\
        \ remainingCoins = coins\n        var price = 1\n\n        while (price <= maxCost\
        \ && remainingCoins >= price) {\n            if (count(price) > 0) {\n     \
        \           val canBuy = remainingCoins / price\n                val num = if\
        \ (count(price) < canBuy) count(price) else canBuy\n                totalIceCreams\
        \ += num\n                remainingCoins -= num * price\n            }\n   \
        \         price += 1\n        }\n\n        totalIceCreams\n    }\n}"
      rust: "impl Solution {\n    pub fn max_ice_cream(costs: Vec<i32>, coins: i32)\
        \ -> i32 {\n        let mut max_cost = 0;\n        for &cost in costs.iter()\
        \ {\n            if cost > max_cost {\n                max_cost = cost;\n  \
        \          }\n        }\n\n        let mut counts = vec![0; (max_cost + 1) as\
        \ usize];\n        for &cost in costs.iter() {\n            counts[cost as usize]\
        \ += 1;\n        }\n\n        let mut total_bars = 0;\n        let mut remaining_coins\
        \ = coins;\n\n        for cost in 1..=max_cost {\n            let count = counts[cost\
        \ as usize];\n            if count > 0 {\n                if remaining_coins\
        \ >= cost {\n                    let can_buy = std::cmp::min(count, remaining_coins\
        \ / cost);\n                    total_bars += can_buy;\n                   \
        \ remaining_coins -= can_buy * cost;\n                } else {\n           \
        \         break;\n                }\n            }\n        }\n\n        total_bars\n\
        \    }\n}"
      racket: "(define/contract (max-ice-cream costs coins)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([max-val (foldl max (car costs) (cdr\
        \ costs))]\n         [counts (make-vector (+ max-val 1) 0)])\n    (for-each\
        \ (lambda (cost)\n                (vector-set! counts cost (+ (vector-ref counts\
        \ cost) 1)))\n              costs)\n    (let loop ([cost 1] [remaining coins]\
        \ [total 0])\n      (cond\n        [(> cost max-val) total]\n        [(< remaining\
        \ cost) total]\n        [else\n         (let ([count (vector-ref counts cost)])\n\
        \           (if (> count 0)\n               (let ([can-buy (min count (quotient\
        \ remaining cost))])\n                 (loop (+ cost 1) (- remaining (* can-buy\
        \ cost)) (+ total can-buy)))\n               (loop (+ cost 1) remaining total)))]))))"
      erlang: "-spec max_ice_cream(Costs :: [integer()], Coins :: integer()) -> integer().\n\
        max_ice_cream(Costs, Coins) ->\n    Max = lists:max(Costs),\n    Counts = lists:foldl(fun(C,\
        \ Acc) ->\n        maps:put(C, maps:get(C, Acc, 0) + 1, Acc)\n    end, #{},\
        \ Costs),\n    solve(1, Max, Coins, 0, Counts).\n\nsolve(Cost, Max, Remaining,\
        \ Total, Counts) when Cost =< Max, Remaining >= Cost ->\n    Count = maps:get(Cost,\
        \ Counts, 0),\n    if\n        Count > 0 ->\n            CanBuy = min(Count,\
        \ Remaining div Cost),\n            solve(Cost + 1, Max, Remaining - (CanBuy\
        \ * Cost), Total + CanBuy, Counts);\n        true ->\n            solve(Cost\
        \ + 1, Max, Remaining, Total, Counts)\n    end;\nsolve(_, _, _, Total, _) ->\n\
        \    Total."
      elixir: "defmodule Solution do\n  @spec max_ice_cream(costs :: [integer], coins\
        \ :: integer) :: integer\n  def max_ice_cream(costs, coins) do\n    max_val\
        \ = Enum.reduce(costs, 0, &max/2)\n    counts = Enum.reduce(costs, %{}, fn cost,\
        \ acc ->\n      Map.update(acc, cost, 1, &(&1 + 1))\n    end)\n\n    {_, total}\
        \ = Enum.reduce_while(1..max_val, {coins, 0}, fn cost, {remaining, total_bars}\
        \ ->\n      if remaining < cost do\n        {:halt, {remaining, total_bars}}\n\
        \      else\n        count = Map.get(counts, cost, 0)\n        if count > 0\
        \ do\n          can_buy = min(count, div(remaining, cost))\n          {:cont,\
        \ {remaining - (can_buy * cost), total_bars + can_buy}}\n        else\n    \
        \      {:cont, {remaining, total_bars}}\n        end\n      end\n    end)\n\n\
        \    total\n  end\nend"
    approach: 'To maximize the total number of ice cream bars purchased, we employ a
      greedy strategy by prioritizing the cheapest items first. Given the constraints
      where the cost of each bar is bounded by $10^5$, we can utilize the counting sort
      technique to efficiently organize the costs. We first identify the maximum price
      in the costs array and then build a frequency array where each index represents
      a specific price and the value at that index denotes the number of bars available
      at that price.


      Next, we iterate through the frequency array from the lowest price to the highest.
      For each price $i$, we determine how many bars we can afford by calculating the
      minimum of the available bars ($freq[i]$) and the total bars our current budget
      allows ($coins / i$). We update our total count and subtract the expenditure from
      our remaining coins. This process continues until we either exhaust our budget
      or process all available bars, ensuring we obtain the maximum count in $O(N +
      M)$ time.'
    time_complexity: O(N + M) where $N$ is the number of ice cream bars and $M$ is the
      maximum cost in the input array. We traverse the input array once to build the
      frequency map and then iterate through the range of costs up to $M$.
    space_complexity: O(M) where $M$ is the maximum cost in the input array. This space
      is required to store the frequency array used for the counting sort logic.
    elapsed_time: 136.91311407089233
    model: gemini-3-flash-preview
    generated_at: '2026-06-21 02:58:41 '
---

## Problem #1833: Maximum Ice Cream Bars

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting, Counting Sort

## Problem Description

<p>It is a sweltering summer day, and a boy wants to buy some ice cream bars.</p>

<p>At the store, there are <code>n</code> ice cream bars. You are given an array <code>costs</code> of length <code>n</code>, where <code>costs[i]</code> is the price of the <code>i<sup>th</sup></code> ice cream bar in coins. The boy initially has <code>coins</code> coins to spend, and he wants to buy as many ice cream bars as possible.&nbsp;</p>

<p><strong>Note:</strong> The boy can buy the ice cream bars in any order.</p>

<p>Return <em>the <strong>maximum</strong> number of ice cream bars the boy can buy with </em><code>coins</code><em> coins.</em></p>

<p>You must solve the problem by counting sort.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> costs = [1,3,2,4,1], coins = 7
<strong>Output:</strong> 4
<strong>Explanation: </strong>The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> costs = [10,6,8,7,7,8], coins = 5
<strong>Output:</strong> 0
<strong>Explanation: </strong>The boy cannot afford any of the ice cream bars.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> costs = [1,6,3,1,2,5], coins = 20
<strong>Output:</strong> 6
<strong>Explanation: </strong>The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>costs.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= costs[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= coins &lt;= 10<sup>8</sup></code></li>
</ul>


## Hints

1. It is always optimal to buy the least expensive ice cream bar first.

2. Sort the prices so that the cheapest ice cream bar comes first.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To maximize the total number of ice cream bars purchased, we employ a greedy strategy by prioritizing the cheapest items first. Given the constraints where the cost of each bar is bounded by $10^5$, we can utilize the counting sort technique to efficiently organize the costs. We first identify the maximum price in the costs array and then build a frequency array where each index represents a specific price and the value at that index denotes the number of bars available at that price.

Next, we iterate through the frequency array from the lowest price to the highest. For each price $i$, we determine how many bars we can afford by calculating the minimum of the available bars ($freq[i]$) and the total bars our current budget allows ($coins / i$). We update our total count and subtract the expenditure from our remaining coins. This process continues until we either exhaust our budget or process all available bars, ensuring we obtain the maximum count in $O(N + M)$ time.

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
    int maxIceCream(vector<int>& costs, int coins) {
        int max_cost = 0;
        for (int cost : costs) {
            if (cost > max_cost) max_cost = cost;
        }

        vector<int> freq(max_cost + 1, 0);
        for (int cost : costs) {
            freq[cost]++;
        }

        int count = 0;
        for (int i = 1; i <= max_cost; ++i) {
            if (freq[i] == 0) continue;
            if (coins < i) break;

            int can_buy = coins / i;
            if (can_buy > freq[i]) can_buy = freq[i];

            count += can_buy;
            coins -= can_buy * i;
        }

        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int maxCost = 0;
        for (int cost : costs) {
            if (cost > maxCost) maxCost = cost;
        }

        int[] freq = new int[maxCost + 1];
        for (int cost : costs) {
            freq[cost]++;
        }

        int count = 0;
        for (int i = 1; i <= maxCost; i++) {
            if (freq[i] == 0) continue;
            if (coins < i) break;

            int canBuy = Math.min(freq[i], coins / i);
            count += canBuy;
            coins -= canBuy * i;
        }

        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if not costs:
            return 0

        max_cost = 0
        for cost in costs:
            if cost > max_cost:
                max_cost = cost

        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1

        count = 0
        for i in range(1, max_cost + 1):
            if freq[i] == 0:
                continue
            if coins < i:
                break

            can_buy = min(freq[i], coins // i)
            count += can_buy
            coins -= can_buy * i

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0

        max_cost = max(costs)
        freq = [0] * (max_cost + 1)

        for cost in costs:
            freq[cost] += 1

        count = 0
        for i in range(1, max_cost + 1):
            if freq[i] == 0:
                continue
            if coins < i:
                break

            can_buy = min(freq[i], coins // i)
            count += can_buy
            coins -= can_buy * i

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxIceCream(int* costs, int costsSize, int coins) {
    int max_cost = 0;
    for (int i = 0; i < costsSize; i++) {
        if (costs[i] > max_cost) {
            max_cost = costs[i];
        }
    }

    int* freq = (int*)calloc(max_cost + 1, sizeof(int));
    if (!freq) return 0;

    for (int i = 0; i < costsSize; i++) {
        freq[costs[i]]++;
    }

    int total_bars = 0;
    for (int i = 1; i <= max_cost; i++) {
        if (freq[i] == 0) continue;
        if (coins < i) break;

        int can_buy = coins / i;
        if (can_buy > freq[i]) {
            can_buy = freq[i];
        }

        total_bars += can_buy;
        coins -= can_buy * i;
    }

    free(freq);
    return total_bars;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxIceCream(int[] costs, int coins) {
        int max = 0;
        foreach (int cost in costs) {
            if (cost > max) max = cost;
        }

        int[] frequency = new int[max + 1];
        foreach (int cost in costs) {
            frequency[cost]++;
        }

        int count = 0;
        for (int i = 1; i <= max; i++) {
            if (frequency[i] == 0) continue;
            if (coins < i) break;

            long canBuy = Math.Min((long)frequency[i], (long)coins / i);
            count += (int)canBuy;
            coins -= (int)canBuy * i;
        }

        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function(costs, coins) {
    let max = 0;
    for (let i = 0; i < costs.length; i++) {
        if (costs[i] > max) max = costs[i];
    }

    let frequency = new Int32Array(max + 1);
    for (let i = 0; i < costs.length; i++) {
        frequency[costs[i]]++;
    }

    let count = 0;
    for (let i = 1; i <= max; i++) {
        if (frequency[i] === 0) continue;
        if (coins < i) break;

        let canBuy = Math.min(frequency[i], Math.floor(coins / i));
        count += canBuy;
        coins -= canBuy * i;
    }

    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxIceCream(costs: number[], coins: number): number {
    let max = 0;
    for (let i = 0; i < costs.length; i++) {
        if (costs[i] > max) max = costs[i];
    }

    let frequency = new Int32Array(max + 1);
    for (let i = 0; i < costs.length; i++) {
        frequency[costs[i]]++;
    }

    let count = 0;
    for (let i = 1; i <= max; i++) {
        if (frequency[i] === 0) continue;
        if (coins < i) break;

        let canBuy = Math.min(frequency[i], Math.floor(coins / i));
        count += canBuy;
        coins -= canBuy * i;
    }

    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $costs
     * @param Integer $coins
     * @return Integer
     */
    function maxIceCream($costs, $coins) {
        $max = 0;
        foreach ($costs as $cost) {
            if ($cost > $max) $max = $cost;
        }

        $frequency = array_fill(0, $max + 1, 0);
        foreach ($costs as $cost) {
            $frequency[$cost]++;
        }

        $count = 0;
        for ($i = 1; $i <= $max; $i++) {
            if ($frequency[$i] === 0) continue;
            if ($coins < $i) break;

            $canBuy = min($frequency[$i], (int)($coins / $i));
            $count += $canBuy;
            $coins -= $canBuy * $i;
        }

        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxIceCream(_ costs: [Int], _ coins: Int) -> Int {
        guard let maxCost = costs.max() else { return 0 }

        var frequency = Array(repeating: 0, count: maxCost + 1)
        for cost in costs {
            frequency[cost] += 1
        }

        var count = 0
        var remainingCoins = coins

        for i in 1...maxCost {
            if frequency[i] == 0 { continue }
            if remainingCoins < i { break }

            let canBuy = min(frequency[i], remainingCoins / i)
            count += canBuy
            remainingCoins -= canBuy * i
        }

        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxIceCream(costs: IntArray, coins: Int): Int {
        var maxCost = 0
        for (cost in costs) {
            if (cost > maxCost) maxCost = cost
        }

        val count = IntArray(maxCost + 1)
        for (cost in costs) {
            count[cost]++
        }

        var totalIceCreams = 0
        var remainingCoins = coins

        for (price in 1..maxCost) {
            if (count[price] == 0) continue
            if (remainingCoins < price) break

            val canBuy = remainingCoins / price
            val num = if (count[price] < canBuy) count[price] else canBuy

            totalIceCreams += num
            remainingCoins -= num * price
        }

        return totalIceCreams
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxIceCream(List<int> costs, int coins) {
    int maxCost = 0;
    for (var cost in costs) {
      if (cost > maxCost) maxCost = cost;
    }

    List<int> count = List<int>.filled(maxCost + 1, 0);
    for (var cost in costs) {
      count[cost]++;
    }

    int totalIceCreams = 0;
    int remainingCoins = coins;

    for (int price = 1; price <= maxCost; price++) {
      if (count[price] == 0) continue;
      if (remainingCoins < price) break;

      int canBuy = remainingCoins ~/ price;
      int num = count[price] < canBuy ? count[price] : canBuy;

      totalIceCreams += num;
      remainingCoins -= num * price;
    }

    return totalIceCreams;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxIceCream(costs []int, coins int) int {
    maxCost := 0
    for _, cost := range costs {
        if cost > maxCost {
            maxCost = cost
        }
    }

    count := make([]int, maxCost+1)
    for _, cost := range costs {
        count[cost]++
    }

    totalIceCreams := 0
    remainingCoins := coins

    for price := 1; price <= maxCost; price++ {
        if count[price] == 0 {
            continue
        }
        if remainingCoins < price {
            break
        }

        canBuy := remainingCoins / price
        num := count[price]
        if canBuy < num {
            num = canBuy
        }

        totalIceCreams += num
        remainingCoins -= num * price
    }

    return totalIceCreams
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_ice_cream(costs, coins)
  max_cost = costs.max
  count = Array.new(max_cost + 1, 0)
  costs.each { |cost| count[cost] += 1 }

  total_ice_creams = 0
  remaining_coins = coins

  (1..max_cost).each do |price|
    next if count[price] == 0
    break if remaining_coins < price

    num = [count[price], remaining_coins / price].min
    total_ice_creams += num
    remaining_coins -= num * price
  end

  total_ice_creams
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxIceCream(costs: Array[Int], coins: Int): Int = {
        var maxCost = 0
        var i = 0
        while (i < costs.length) {
            if (costs(i) > maxCost) maxCost = costs(i)
            i += 1
        }

        val count = new Array[Int](maxCost + 1)
        i = 0
        while (i < costs.length) {
            count(costs(i)) += 1
            i += 1
        }

        var totalIceCreams = 0
        var remainingCoins = coins
        var price = 1

        while (price <= maxCost && remainingCoins >= price) {
            if (count(price) > 0) {
                val canBuy = remainingCoins / price
                val num = if (count(price) < canBuy) count(price) else canBuy
                totalIceCreams += num
                remainingCoins -= num * price
            }
            price += 1
        }

        totalIceCreams
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_ice_cream(costs: Vec<i32>, coins: i32) -> i32 {
        let mut max_cost = 0;
        for &cost in costs.iter() {
            if cost > max_cost {
                max_cost = cost;
            }
        }

        let mut counts = vec![0; (max_cost + 1) as usize];
        for &cost in costs.iter() {
            counts[cost as usize] += 1;
        }

        let mut total_bars = 0;
        let mut remaining_coins = coins;

        for cost in 1..=max_cost {
            let count = counts[cost as usize];
            if count > 0 {
                if remaining_coins >= cost {
                    let can_buy = std::cmp::min(count, remaining_coins / cost);
                    total_bars += can_buy;
                    remaining_coins -= can_buy * cost;
                } else {
                    break;
                }
            }
        }

        total_bars
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-ice-cream costs coins)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([max-val (foldl max (car costs) (cdr costs))]
         [counts (make-vector (+ max-val 1) 0)])
    (for-each (lambda (cost)
                (vector-set! counts cost (+ (vector-ref counts cost) 1)))
              costs)
    (let loop ([cost 1] [remaining coins] [total 0])
      (cond
        [(> cost max-val) total]
        [(< remaining cost) total]
        [else
         (let ([count (vector-ref counts cost)])
           (if (> count 0)
               (let ([can-buy (min count (quotient remaining cost))])
                 (loop (+ cost 1) (- remaining (* can-buy cost)) (+ total can-buy)))
               (loop (+ cost 1) remaining total)))]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_ice_cream(Costs :: [integer()], Coins :: integer()) -> integer().
max_ice_cream(Costs, Coins) ->
    Max = lists:max(Costs),
    Counts = lists:foldl(fun(C, Acc) ->
        maps:put(C, maps:get(C, Acc, 0) + 1, Acc)
    end, #{}, Costs),
    solve(1, Max, Coins, 0, Counts).

solve(Cost, Max, Remaining, Total, Counts) when Cost =< Max, Remaining >= Cost ->
    Count = maps:get(Cost, Counts, 0),
    if
        Count > 0 ->
            CanBuy = min(Count, Remaining div Cost),
            solve(Cost + 1, Max, Remaining - (CanBuy * Cost), Total + CanBuy, Counts);
        true ->
            solve(Cost + 1, Max, Remaining, Total, Counts)
    end;
solve(_, _, _, Total, _) ->
    Total.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_ice_cream(costs :: [integer], coins :: integer) :: integer
  def max_ice_cream(costs, coins) do
    max_val = Enum.reduce(costs, 0, &max/2)
    counts = Enum.reduce(costs, %{}, fn cost, acc ->
      Map.update(acc, cost, 1, &(&1 + 1))
    end)

    {_, total} = Enum.reduce_while(1..max_val, {coins, 0}, fn cost, {remaining, total_bars} ->
      if remaining < cost do
        {:halt, {remaining, total_bars}}
      else
        count = Map.get(counts, cost, 0)
        if count > 0 do
          can_buy = min(count, div(remaining, cost))
          {:cont, {remaining - (can_buy * cost), total_bars + can_buy}}
        else
          {:cont, {remaining, total_bars}}
        end
      end
    end)

    total
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + M) where $N$ is the number of ice cream bars and $M$ is the maximum cost in the input array. We traverse the input array once to build the frequency map and then iterate through the range of costs up to $M$.
- **Space Complexity:** O(M) where $M$ is the maximum cost in the input array. This space is required to store the frequency array used for the counting sort logic.
