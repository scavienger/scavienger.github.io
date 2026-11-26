---
layout: post
title: "Stone Removal Game"
date: 2026-11-26 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/stone-removal-game/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool canAliceWin(int n) {\n        int stonesToRemove\
        \ = 10;\n        bool aliceTurn = true;\n        while (n >= stonesToRemove)\
        \ {\n            n -= stonesToRemove;\n            stonesToRemove--;\n     \
        \       aliceTurn = !aliceTurn;\n        }\n        return !aliceTurn;\n   \
        \ }\n};"
      java: "class Solution {\n    public boolean canAliceWin(int n) {\n        int\
        \ stonesToRemove = 10;\n        boolean aliceTurn = true;\n        while (n\
        \ >= stonesToRemove) {\n            n -= stonesToRemove;\n            stonesToRemove--;\n\
        \            aliceTurn = !aliceTurn;\n        }\n        return !aliceTurn;\n\
        \    }\n}"
      python: "class Solution(object):\n    def canAliceWin(self, n):\n        \"\"\"\
        \n        :type n: int\n        :rtype: bool\n        \"\"\"\n        stones_to_remove\
        \ = 10\n        alice_turn = True\n        while n >= stones_to_remove:\n  \
        \          n -= stones_to_remove\n            stones_to_remove -= 1\n      \
        \      alice_turn = not alice_turn\n        return not alice_turn"
      python3: "class Solution:\n    def canAliceWin(self, n: int) -> bool:\n      \
        \  stones_to_remove = 10\n        alice_turn = True\n        while n >= stones_to_remove:\n\
        \            n -= stones_to_remove\n            stones_to_remove -= 1\n    \
        \        alice_turn = not alice_turn\n        return not alice_turn"
      c: "#include <stdbool.h>\n\nbool canAliceWin(int n) {\n    int stonesToRemove\
        \ = 10;\n    bool aliceTurn = true;\n    while (n >= stonesToRemove) {\n   \
        \     n -= stonesToRemove;\n        stonesToRemove--;\n        aliceTurn = !aliceTurn;\n\
        \    }\n    return !aliceTurn;\n}"
      csharp: "public class Solution {\n    public bool CanAliceWin(int n) {\n     \
        \   int stonesToRemove = 10;\n        bool aliceTurn = true;\n        while\
        \ (n >= stonesToRemove) {\n            n -= stonesToRemove;\n            stonesToRemove--;\n\
        \            aliceTurn = !aliceTurn;\n        }\n        return !aliceTurn;\n\
        \    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {boolean}\n */\nvar canAliceWin\
        \ = function(n) {\n    let stonesToRemove = 10;\n    let aliceTurn = true;\n\
        \    while (n >= stonesToRemove) {\n        n -= stonesToRemove;\n        stonesToRemove--;\n\
        \        aliceTurn = !aliceTurn;\n    }\n    return !aliceTurn;\n};"
      typescript: "function canAliceWin(n: number): boolean {\n    let stonesToRemove:\
        \ number = 10;\n    let aliceTurn: boolean = true;\n    while (n >= stonesToRemove)\
        \ {\n        n -= stonesToRemove;\n        stonesToRemove -= 1;\n        aliceTurn\
        \ = !aliceTurn;\n    }\n    return !aliceTurn;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Boolean\n\
        \     */\n    function canAliceWin($n) {\n        $stonesToRemove = 10;\n  \
        \      $aliceTurn = true;\n        while ($n >= $stonesToRemove) {\n       \
        \     $n -= $stonesToRemove;\n            $stonesToRemove -= 1;\n          \
        \  $aliceTurn = !$aliceTurn;\n        }\n        return !$aliceTurn;\n    }\n\
        }"
      swift: "class Solution {\n    func canAliceWin(_ n: Int) -> Bool {\n        var\
        \ currentN = n\n        var stonesToRemove = 10\n        var aliceTurn = true\n\
        \        while currentN >= stonesToRemove {\n            currentN -= stonesToRemove\n\
        \            stonesToRemove -= 1\n            aliceTurn = !aliceTurn\n     \
        \   }\n        return !aliceTurn\n    }\n}"
      kotlin: "class Solution {\n    fun canAliceWin(n: Int): Boolean {\n        var\
        \ currentN = n\n        var stonesToRemove = 10\n        var aliceTurn = true\n\
        \        while (currentN >= stonesToRemove) {\n            currentN -= stonesToRemove\n\
        \            stonesToRemove -= 1\n            aliceTurn = !aliceTurn\n     \
        \   }\n        return !aliceTurn\n    }\n}"
      dart: "class Solution {\n  bool canAliceWin(int n) {\n    int stonesToRemove =\
        \ 10;\n    bool aliceTurn = true;\n    while (n >= stonesToRemove) {\n     \
        \ n -= stonesToRemove;\n      stonesToRemove -= 1;\n      aliceTurn = !aliceTurn;\n\
        \    }\n    return !aliceTurn;\n  }\n}"
      go: "func canAliceWin(n int) bool {\n    stonesToRemove := 10\n    aliceTurn :=\
        \ true\n    for n >= stonesToRemove {\n        n -= stonesToRemove\n       \
        \ stonesToRemove -= 1\n        aliceTurn = !aliceTurn\n    }\n    return !aliceTurn\n\
        }"
      ruby: "def can_alice_win(n)\n  stones_to_remove = 10\n  alice_turn = true\n  while\
        \ n >= stones_to_remove\n    n -= stones_to_remove\n    stones_to_remove -=\
        \ 1\n    alice_turn = !alice_turn\n  end\n  !alice_turn\nend"
      scala: "object Solution {\n    def canAliceWin(n: Int): Boolean = {\n        var\
        \ currN = n\n        var stonesToRemove = 10\n        var aliceTurn = true\n\
        \        while (currN >= stonesToRemove) {\n            currN -= stonesToRemove\n\
        \            stonesToRemove -= 1\n            aliceTurn = !aliceTurn\n     \
        \   }\n        !aliceTurn\n    }\n}"
      rust: "impl Solution {\n    pub fn can_alice_win(n: i32) -> bool {\n        let\
        \ mut n = n;\n        let mut stones_to_remove = 10;\n        let mut alice_turn\
        \ = true;\n        while n >= stones_to_remove {\n            n -= stones_to_remove;\n\
        \            stones_to_remove -= 1;\n            alice_turn = !alice_turn;\n\
        \        }\n        !alice_turn\n    }\n}"
      racket: "(define/contract (can-alice-win n)\n  (-> exact-integer? boolean?)\n\
        \  (let loop ([curr-n n]\n             [stones-to-remove 10]\n             [alice-turn\
        \ #t])\n    (if (>= curr-n stones-to-remove)\n        (loop (- curr-n stones-to-remove)\n\
        \              (- stones-to-remove 1)\n              (not alice-turn))\n   \
        \     (not alice-turn))))"
      erlang: "-spec can_alice_win(N :: integer()) -> boolean().\ncan_alice_win(N) ->\n\
        \  can_alice_win_helper(N, 10, true).\n\ncan_alice_win_helper(N, StonesToRemove,\
        \ AliceTurn) when N >= StonesToRemove ->\n  can_alice_win_helper(N - StonesToRemove,\
        \ StonesToRemove - 1, not AliceTurn);\ncan_alice_win_helper(_N, _StonesToRemove,\
        \ AliceTurn) ->\n  not AliceTurn."
      elixir: "defmodule Solution do\n  @spec can_alice_win(n :: integer) :: boolean\n\
        \  def can_alice_win(n) do\n    can_alice_win_helper(n, 10, true)\n  end\n\n\
        \  defp can_alice_win_helper(n, stones_to_remove, alice_turn) when n >= stones_to_remove\
        \ do\n    can_alice_win_helper(n - stones_to_remove, stones_to_remove - 1, not\
        \ alice_turn)\n  end\n\n  defp can_alice_win_helper(_n, _stones_to_remove, alice_turn)\
        \ do\n    not alice_turn\n  end\nend"
    approach: 'The game is a turn-based simulation where Alice and Bob remove a decreasing
      number of stones from a pile. Starting with Alice removing 10 stones, each subsequent
      move requires exactly one stone fewer than the previous opponent''s turn. We can
      model this using a simulation loop that continues as long as the current player
      can remove the required number of stones from the remaining pile.


      In each iteration, we check if the pile size is at least equal to the current
      removal requirement. If it is, we subtract that amount from the pile, decrement
      the removal requirement for the next turn, and toggle a turn-tracking boolean
      flag. If a player cannot meet the requirement, the loop terminates. The winner
      is determined by which player''s turn it was when the loop ended; if it was Alice''s
      turn and she couldn''t move, she loses, and if it was Bob''s turn and he couldn''t
      move, he loses (meaning Alice wins).'
    time_complexity: O(1). The simulation involves a maximum of 10 turns because the
      removal requirement starts at 10 and decreases by 1 each turn. Even as $n$ increases,
      the sum of stones removed in a full game is at most 55, and since $n$ is capped
      at 50, the loop will always terminate in a small constant number of iterations.
    space_complexity: O(1). The algorithm uses a constant amount of extra space for
      tracking the remaining stones, the current removal requirement, and the turn indicator.
      No complex data structures or recursive calls are utilized, so the memory usage
      is independent of the input size $n$.
    elapsed_time: 94.7673237323761
    model: gemini-3-flash-preview
    generated_at: '2026-11-26 06:14:18 '
---

## Problem #3360: Stone Removal Game

**Difficulty:** Easy

**Topics:** Math, Simulation

## Problem Description

<p>Alice and Bob are playing a game where they take turns removing stones from a pile, with <em>Alice going first</em>.</p>

<ul>
	<li>Alice starts by removing <strong>exactly</strong> 10 stones on her first turn.</li>
	<li>For each subsequent turn, each player removes <strong>exactly</strong> 1 fewer<strong> </strong>stone<strong> </strong>than the previous opponent.</li>
</ul>

<p>The player who cannot make a move loses the game.</p>

<p>Given a positive integer <code>n</code>, return <code>true</code> if Alice wins the game and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 12</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Alice removes 10 stones on her first turn, leaving 2 stones for Bob.</li>
	<li>Bob cannot remove 9 stones, so Alice wins.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Alice cannot remove 10 stones, so Alice loses.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
</ul>


## Hints

1. The constraints are small enough that a brute-force solution is feasible.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The game is a turn-based simulation where Alice and Bob remove a decreasing number of stones from a pile. Starting with Alice removing 10 stones, each subsequent move requires exactly one stone fewer than the previous opponent's turn. We can model this using a simulation loop that continues as long as the current player can remove the required number of stones from the remaining pile.

In each iteration, we check if the pile size is at least equal to the current removal requirement. If it is, we subtract that amount from the pile, decrement the removal requirement for the next turn, and toggle a turn-tracking boolean flag. If a player cannot meet the requirement, the loop terminates. The winner is determined by which player's turn it was when the loop ended; if it was Alice's turn and she couldn't move, she loses, and if it was Bob's turn and he couldn't move, he loses (meaning Alice wins).

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
    bool canAliceWin(int n) {
        int stonesToRemove = 10;
        bool aliceTurn = true;
        while (n >= stonesToRemove) {
            n -= stonesToRemove;
            stonesToRemove--;
            aliceTurn = !aliceTurn;
        }
        return !aliceTurn;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean canAliceWin(int n) {
        int stonesToRemove = 10;
        boolean aliceTurn = true;
        while (n >= stonesToRemove) {
            n -= stonesToRemove;
            stonesToRemove--;
            aliceTurn = !aliceTurn;
        }
        return !aliceTurn;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stones_to_remove = 10
        alice_turn = True
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn
        return not alice_turn
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        alice_turn = True
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn
        return not alice_turn
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>

bool canAliceWin(int n) {
    int stonesToRemove = 10;
    bool aliceTurn = true;
    while (n >= stonesToRemove) {
        n -= stonesToRemove;
        stonesToRemove--;
        aliceTurn = !aliceTurn;
    }
    return !aliceTurn;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CanAliceWin(int n) {
        int stonesToRemove = 10;
        bool aliceTurn = true;
        while (n >= stonesToRemove) {
            n -= stonesToRemove;
            stonesToRemove--;
            aliceTurn = !aliceTurn;
        }
        return !aliceTurn;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @return {boolean}
 */
var canAliceWin = function(n) {
    let stonesToRemove = 10;
    let aliceTurn = true;
    while (n >= stonesToRemove) {
        n -= stonesToRemove;
        stonesToRemove--;
        aliceTurn = !aliceTurn;
    }
    return !aliceTurn;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function canAliceWin(n: number): boolean {
    let stonesToRemove: number = 10;
    let aliceTurn: boolean = true;
    while (n >= stonesToRemove) {
        n -= stonesToRemove;
        stonesToRemove -= 1;
        aliceTurn = !aliceTurn;
    }
    return !aliceTurn;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function canAliceWin($n) {
        $stonesToRemove = 10;
        $aliceTurn = true;
        while ($n >= $stonesToRemove) {
            $n -= $stonesToRemove;
            $stonesToRemove -= 1;
            $aliceTurn = !$aliceTurn;
        }
        return !$aliceTurn;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func canAliceWin(_ n: Int) -> Bool {
        var currentN = n
        var stonesToRemove = 10
        var aliceTurn = true
        while currentN >= stonesToRemove {
            currentN -= stonesToRemove
            stonesToRemove -= 1
            aliceTurn = !aliceTurn
        }
        return !aliceTurn
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun canAliceWin(n: Int): Boolean {
        var currentN = n
        var stonesToRemove = 10
        var aliceTurn = true
        while (currentN >= stonesToRemove) {
            currentN -= stonesToRemove
            stonesToRemove -= 1
            aliceTurn = !aliceTurn
        }
        return !aliceTurn
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool canAliceWin(int n) {
    int stonesToRemove = 10;
    bool aliceTurn = true;
    while (n >= stonesToRemove) {
      n -= stonesToRemove;
      stonesToRemove -= 1;
      aliceTurn = !aliceTurn;
    }
    return !aliceTurn;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func canAliceWin(n int) bool {
    stonesToRemove := 10
    aliceTurn := true
    for n >= stonesToRemove {
        n -= stonesToRemove
        stonesToRemove -= 1
        aliceTurn = !aliceTurn
    }
    return !aliceTurn
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def can_alice_win(n)
  stones_to_remove = 10
  alice_turn = true
  while n >= stones_to_remove
    n -= stones_to_remove
    stones_to_remove -= 1
    alice_turn = !alice_turn
  end
  !alice_turn
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def canAliceWin(n: Int): Boolean = {
        var currN = n
        var stonesToRemove = 10
        var aliceTurn = true
        while (currN >= stonesToRemove) {
            currN -= stonesToRemove
            stonesToRemove -= 1
            aliceTurn = !aliceTurn
        }
        !aliceTurn
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn can_alice_win(n: i32) -> bool {
        let mut n = n;
        let mut stones_to_remove = 10;
        let mut alice_turn = true;
        while n >= stones_to_remove {
            n -= stones_to_remove;
            stones_to_remove -= 1;
            alice_turn = !alice_turn;
        }
        !alice_turn
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (can-alice-win n)
  (-> exact-integer? boolean?)
  (let loop ([curr-n n]
             [stones-to-remove 10]
             [alice-turn #t])
    (if (>= curr-n stones-to-remove)
        (loop (- curr-n stones-to-remove)
              (- stones-to-remove 1)
              (not alice-turn))
        (not alice-turn))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec can_alice_win(N :: integer()) -> boolean().
can_alice_win(N) ->
  can_alice_win_helper(N, 10, true).

can_alice_win_helper(N, StonesToRemove, AliceTurn) when N >= StonesToRemove ->
  can_alice_win_helper(N - StonesToRemove, StonesToRemove - 1, not AliceTurn);
can_alice_win_helper(_N, _StonesToRemove, AliceTurn) ->
  not AliceTurn.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec can_alice_win(n :: integer) :: boolean
  def can_alice_win(n) do
    can_alice_win_helper(n, 10, true)
  end

  defp can_alice_win_helper(n, stones_to_remove, alice_turn) when n >= stones_to_remove do
    can_alice_win_helper(n - stones_to_remove, stones_to_remove - 1, not alice_turn)
  end

  defp can_alice_win_helper(_n, _stones_to_remove, alice_turn) do
    not alice_turn
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The simulation involves a maximum of 10 turns because the removal requirement starts at 10 and decreases by 1 each turn. Even as $n$ increases, the sum of stones removed in a full game is at most 55, and since $n$ is capped at 50, the loop will always terminate in a small constant number of iterations.
- **Space Complexity:** O(1). The algorithm uses a constant amount of extra space for tracking the remaining stones, the current removal requirement, and the turn indicator. No complex data structures or recursive calls are utilized, so the memory usage is independent of the input size $n$.
