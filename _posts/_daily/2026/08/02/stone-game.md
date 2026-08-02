---
layout: post
title: "Stone Game"
date: 2026-08-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Dynamic Programming", "Game Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/stone-game/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool stoneGame(vector<int>& piles) {\n  \
        \      return true;\n    }\n};"
      java: "class Solution {\n    public boolean stoneGame(int[] piles) {\n       \
        \ return true;\n    }\n}"
      python: "class Solution(object):\n    def stoneGame(self, piles):\n        \"\"\
        \"\n        :type piles: List[int]\n        :rtype: bool\n        \"\"\"\n \
        \       return True"
      python3: "class Solution:\n    def stoneGame(self, piles: List[int]) -> bool:\n\
        \        return True"
      c: "bool stoneGame(int* piles, int pilesSize) {\n    return true;\n}"
      csharp: "public class Solution {\n    public bool StoneGame(int[] piles) {\n \
        \       return true;\n    }\n}"
      javascript: "/**\n * @param {number[]} piles\n * @return {boolean}\n */\nvar stoneGame\
        \ = function(piles) {\n    return true;\n};"
      typescript: "function stoneGame(piles: number[]): boolean {\n    return true;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $piles\n     * @return\
        \ Boolean\n     */\n    function stoneGame($piles) {\n        return true;\n\
        \    }\n}"
      swift: "class Solution {\n    func stoneGame(_ piles: [Int]) -> Bool {\n     \
        \   return true;\n    }\n}"
      kotlin: "class Solution {\n    fun stoneGame(piles: IntArray): Boolean {\n   \
        \     return true\n    }\n}"
      dart: "class Solution {\n  bool stoneGame(List<int> piles) {\n    return true;\n\
        \  }\n}"
      go: "func stoneGame(piles []int) bool {\n    return true\n}"
      ruby: "# @param {Integer[]} piles\n# @return {Boolean}\ndef stone_game(piles)\n\
        \    return true\nend"
      scala: "object Solution {\n    def stoneGame(piles: Array[Int]): Boolean = {\n\
        \        true\n    }\n}"
      rust: "impl Solution {\n    pub fn stone_game(piles: Vec<i32>) -> bool {\n   \
        \     true\n    }\n}"
      racket: "(define/contract (stone-game piles)\n  (-> (listof exact-integer?) boolean?)\n\
        \  #t\n)"
      erlang: "-spec stone_game(Piles :: [integer()]) -> boolean().\nstone_game(Piles)\
        \ ->\n  true."
      elixir: "defmodule Solution do\n  @spec stone_game(piles :: [integer]) :: boolean\n\
        \  def stone_game(piles) do\n    true\n  end\nend"
    approach: 'The problem can be solved by recognizing a fundamental mathematical advantage
      for the first player. With an even number of piles, Alice can calculate the total
      number of stones in even-indexed positions (0, 2, 4, ...) and odd-indexed positions
      (1, 3, 5, ...). Since the total sum of stones is odd, these two sums cannot be
      equal. Alice can simply choose the parity (odd or even) that has the greater total
      and force a strategy to collect all piles of that parity.


      On her first move, Alice can pick the first pile (even index) or the last pile
      (odd index). If she picks the first pile, she leaves Bob with two piles that were
      originally at odd indices. No matter which one Bob picks, Alice will again have
      the option to pick an even-indexed pile. This parity-control strategy ensures
      Alice can always secure more stones than Bob, regardless of the values in the
      piles, resulting in a guaranteed win.'
    time_complexity: O(1). The solution runs in constant time because the outcome is
      mathematically predetermined to be true given the constraints of an even number
      of piles and an odd total stone count.
    space_complexity: O(1). The solution requires no extra space or auxiliary data structures
      to determine the result.
    elapsed_time: 152.78304624557495
    model: gemini-3-flash-preview
    generated_at: '2026-08-02 02:04:14 '
---

## Problem #877: Stone Game

**Difficulty:** Medium

**Topics:** Array, Math, Dynamic Programming, Game Theory

## Problem Description

<p>Alice and Bob play a game with piles of stones. There are an <strong>even</strong> number of piles arranged in a row, and each pile has a <strong>positive</strong> integer number of stones <code>piles[i]</code>.</p>

<p>The objective of the game is to end with the most stones. The <strong>total</strong> number of stones across all the piles is <strong>odd</strong>, so there are no ties.</p>

<p>Alice and Bob take turns, with <strong>Alice starting first</strong>. Each turn, a player takes the entire pile of stones either from the <strong>beginning</strong> or from the <strong>end</strong> of the row. This continues until there are no more piles left, at which point the person with the <strong>most stones wins</strong>.</p>

<p>Assuming Alice and Bob play optimally, return <code>true</code><em> if Alice wins the game, or </em><code>false</code><em> if Bob wins</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> piles = [5,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> piles = [3,7,2,3]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= piles.length &lt;= 500</code></li>
	<li><code>piles.length</code> is <strong>even</strong>.</li>
	<li><code>1 &lt;= piles[i] &lt;= 500</code></li>
	<li><code>sum(piles[i])</code> is <strong>odd</strong>.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by recognizing a fundamental mathematical advantage for the first player. With an even number of piles, Alice can calculate the total number of stones in even-indexed positions (0, 2, 4, ...) and odd-indexed positions (1, 3, 5, ...). Since the total sum of stones is odd, these two sums cannot be equal. Alice can simply choose the parity (odd or even) that has the greater total and force a strategy to collect all piles of that parity.

On her first move, Alice can pick the first pile (even index) or the last pile (odd index). If she picks the first pile, she leaves Bob with two piles that were originally at odd indices. No matter which one Bob picks, Alice will again have the option to pick an even-indexed pile. This parity-control strategy ensures Alice can always secure more stones than Bob, regardless of the values in the piles, resulting in a guaranteed win.

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
    bool stoneGame(vector<int>& piles) {
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean stoneGame(int[] piles) {
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool stoneGame(int* piles, int pilesSize) {
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool StoneGame(int[] piles) {
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} piles
 * @return {boolean}
 */
var stoneGame = function(piles) {
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function stoneGame(piles: number[]): boolean {
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $piles
     * @return Boolean
     */
    function stoneGame($piles) {
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func stoneGame(_ piles: [Int]) -> Bool {
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun stoneGame(piles: IntArray): Boolean {
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool stoneGame(List<int> piles) {
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func stoneGame(piles []int) bool {
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} piles
# @return {Boolean}
def stone_game(piles)
    return true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def stoneGame(piles: Array[Int]): Boolean = {
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn stone_game(piles: Vec<i32>) -> bool {
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (stone-game piles)
  (-> (listof exact-integer?) boolean?)
  #t
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec stone_game(Piles :: [integer()]) -> boolean().
stone_game(Piles) ->
  true.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec stone_game(piles :: [integer]) :: boolean
  def stone_game(piles) do
    true
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The solution runs in constant time because the outcome is mathematically predetermined to be true given the constraints of an even number of piles and an odd total stone count.
- **Space Complexity:** O(1). The solution requires no extra space or auxiliary data structures to determine the result.
