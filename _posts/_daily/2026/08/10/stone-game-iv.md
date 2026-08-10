---
layout: post
title: "Stone Game IV"
date: 2026-08-10 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Math", "Dynamic Programming", "Minimax", "Game Theory", "Nim Game", "Sprague–Grundy Theorem", "Zero-Sum Game"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/stone-game-iv/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool winnerSquareGame(int n) {\n        vector<bool>\
        \ dp(n + 1, false);\n        for (int i = 1; i <= n; ++i) {\n            for\
        \ (int k = 1; k * k <= i; ++k) {\n                if (!dp[i - k * k]) {\n  \
        \                  dp[i] = true;\n                    break;\n             \
        \   }\n            }\n        }\n        return dp[n];\n    }\n};"
      java: "class Solution {\n    public boolean winnerSquareGame(int n) {\n      \
        \  boolean[] dp = new boolean[n + 1];\n        for (int i = 1; i <= n; i++)\
        \ {\n            for (int k = 1; k * k <= i; k++) {\n                if (!dp[i\
        \ - k * k]) {\n                    dp[i] = true;\n                    break;\n\
        \                }\n            }\n        }\n        return dp[n];\n    }\n\
        }"
      python: "class Solution(object):\n    def winnerSquareGame(self, n):\n       \
        \ \"\"\"\n        :type n: int\n        :rtype: bool\n        \"\"\"\n     \
        \   dp = [False] * (n + 1)\n        for i in range(1, n + 1):\n            k\
        \ = 1\n            while k * k <= i:\n                if not dp[i - k * k]:\n\
        \                    dp[i] = True\n                    break\n             \
        \   k += 1\n        return dp[n]"
      python3: "class Solution:\n    def winnerSquareGame(self, n: int) -> bool:\n \
        \       dp = [False] * (n + 1)\n        squares = [k * k for k in range(1, int(n**0.5)\
        \ + 1)]\n        for i in range(n + 1):\n            if dp[i]:\n           \
        \     continue\n            for sq in squares:\n                if i + sq >\
        \ n:\n                    break\n                dp[i + sq] = True\n       \
        \ return dp[n]"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n\nbool winnerSquareGame(int n)\
        \ {\n    bool *dp = (bool *)calloc(n + 1, sizeof(bool));\n    if (!dp) return\
        \ false;\n    for (int i = 0; i <= n; i++) {\n        if (dp[i]) continue;\n\
        \        for (int k = 1; ; k++) {\n            int sq = k * k;\n           \
        \ if (i + sq > n) break;\n            dp[i + sq] = true;\n        }\n    }\n\
        \    bool result = dp[n];\n    free(dp);\n    return result;\n}"
      csharp: "public class Solution {\n    public bool WinnerSquareGame(int n) {\n\
        \        bool[] dp = new bool[n + 1];\n        for (int i = 0; i <= n; i++)\
        \ {\n            if (dp[i]) continue;\n            for (int k = 1; ; k++) {\n\
        \                int sq = k * k;\n                if (i + sq > n) break;\n \
        \               dp[i + sq] = true;\n            }\n        }\n        return\
        \ dp[n];\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {boolean}\n */\nvar winnerSquareGame\
        \ = function(n) {\n    const dp = new Uint8Array(n + 1);\n    for (let i = 0;\
        \ i <= n; i++) {\n        if (dp[i]) continue;\n        for (let k = 1; ; k++)\
        \ {\n            const sq = k * k;\n            if (i + sq > n) break;\n   \
        \         dp[i + sq] = 1;\n        }\n    }\n    return dp[n] === 1;\n};"
      typescript: "function winnerSquareGame(n: number): boolean {\n    const dp: boolean[]\
        \ = new Array(n + 1).fill(false);\n    for (let i = 1; i <= n; i++) {\n    \
        \    for (let k = 1; k * k <= i; k++) {\n            if (!dp[i - k * k]) {\n\
        \                dp[i] = true;\n                break;\n            }\n    \
        \    }\n    }\n    return dp[n];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Boolean\n\
        \     */\n    function winnerSquareGame($n) {\n        $dp = array_fill(0, $n\
        \ + 1, false);\n        for (\\$i = 1; \\$i <= $n; \\$i++) {\n            for\
        \ (\\$k = 1; \\$k * \\$k <= \\$i; \\$k++) {\n                if (!\\$dp[\\$i\
        \ - \\$k * \\$k]) {\n                    \\$dp[\\$i] = true;\n             \
        \       break;\n                }\n            }\n        }\n        return\
        \ \\$dp[\\$n];\n    }\n}"
      swift: "class Solution {\n    func winnerSquareGame(_ n: Int) -> Bool {\n    \
        \    var dp = [Bool](repeating: false, count: n + 1)\n        for i in 1...n\
        \ {\n            var k = 1\n            while k * k <= i {\n               \
        \ if !dp[i - k * k] {\n                    dp[i] = true\n                  \
        \  break\n                }\n                k += 1\n            }\n       \
        \ }\n        return dp[n]\n    }\n}"
      kotlin: "class Solution {\n    fun winnerSquareGame(n: Int): Boolean {\n     \
        \   val dp = BooleanArray(n + 1)\n        for (i in 1..n) {\n            var\
        \ k = 1\n            while (k * k <= i) {\n                if (!dp[i - k * k])\
        \ {\n                    dp[i] = true\n                    break\n         \
        \       }\n                k++\n            }\n        }\n        return dp[n]\n\
        \    }\n}"
      dart: "class Solution {\n  bool winnerSquareGame(int n) {\n    List<bool> dp =\
        \ List.filled(n + 1, false);\n    for (int i = 1; i <= n; i++) {\n      for\
        \ (int k = 1; k * k <= i; k++) {\n        if (!dp[i - k * k]) {\n          dp[i]\
        \ = true;\n          break;\n        }\n      }\n    }\n    return dp[n];\n\
        \  }\n}"
      go: "func winnerSquareGame(n int) bool {\n    dp := make([]bool, n+1)\n    for\
        \ i := 1; i <= n; i++ {\n        for k := 1; k*k <= i; k++ {\n            if\
        \ !dp[i-k*k] {\n                dp[i] = true\n                break\n      \
        \      }\n        }\n    }\n    return dp[n]\n}"
      ruby: "# @param {Integer} n\n# @return {Boolean}\ndef winner_square_game(n)\n\
        \  dp = Array.new(n + 1, false)\n  (1..n).each do |i|\n    k = 1\n    while\
        \ k * k <= i\n      if !dp[i - k * k]\n        dp[i] = true\n        break\n\
        \      end\n      k += 1\n    end\n  end\n  dp[n]\nend"
      scala: "object Solution {\n    def winnerSquareGame(n: Int): Boolean = {\n   \
        \     val dp = new Array[Boolean](n + 1)\n        for (i <- 1 to n) {\n    \
        \        var k = 1\n            var found = false\n            while (k * k\
        \ <= i && !found) {\n                if (!dp(i - k * k)) {\n               \
        \     found = true\n                }\n                k += 1\n            }\n\
        \            dp(i) = found\n        }\n        dp(n)\n    }\n}"
      rust: "impl Solution {\n    pub fn winner_square_game(n: i32) -> bool {\n    \
        \    let n = n as usize;\n        let mut dp = vec![false; n + 1];\n       \
        \ for i in 0..=n {\n            if !dp[i] {\n                let mut k = 1;\n\
        \                while i + k * k <= n {\n                    dp[i + k * k] =\
        \ true;\n                    k += 1;\n                }\n            }\n   \
        \     }\n        dp[n]\n    }\n}"
      racket: "(define/contract (winner-square-game n)\n  (-> exact-integer? boolean?)\n\
        \  (let ([dp (make-vector (+ n 1) #f)])\n    (for ([i (in-range (+ n 1))])\n\
        \      (when (not (vector-ref dp i))\n        (let loop ([k 1])\n          (let\
        \ ([next (+ i (* k k))])\n            (when (<= next n)\n              (vector-set!\
        \ dp next #t)\n              (loop (+ k 1)))))))\n    (vector-ref dp n)))"
      erlang: "-spec winner_square_game(N :: integer()) -> boolean().\nwinner_square_game(N)\
        \ ->\n  Dp = ets:new(dp_table, [set, private]),\n  solve(0, N, Dp),\n  Result\
        \ = ets:member(Dp, N),\n  ets:delete(Dp),\n  Result.\n\nsolve(I, N, Dp) when\
        \ I > N -> ok;\nsolve(I, N, Dp) ->\n  case ets:member(Dp, I) of\n    true ->\
        \ solve(I + 1, N, Dp);\n    false ->\n      mark_winning(I, 1, N, Dp),\n   \
        \   solve(I + 1, N, Dp)\n  end.\n\nmark_winning(I, K, N, Dp) ->\n  Next = I\
        \ + K * K,\n  if\n    Next > N -> ok;\n    true ->\n      ets:insert(Dp, {Next,\
        \ true}),\n      mark_winning(I, K + 1, N, Dp)\n  end."
      elixir: "defmodule Solution do\n  @spec winner_square_game(n :: integer) :: boolean\n\
        \  def winner_square_game(n) do\n    dp = :ets.new(:dp_table, [:set, :private])\n\
        \    solve(0, n, dp)\n    result = :ets.member(dp, n)\n    :ets.delete(dp)\n\
        \    result\n  end\n\n  defp solve(i, n, dp) when i > n, do: :ok\n  defp solve(i,\
        \ n, dp) do\n    unless :ets.member(dp, i) do\n      mark_winning(i, 1, n, dp)\n\
        \    end\n    solve(i + 1, n, dp)\n  end\n\n  defp mark_winning(i, k, n, dp)\
        \ do\n    next = i + k * k\n    if next <= n do\n      :ets.insert(dp, {next,\
        \ true})\n      mark_winning(i, k + 1, n, dp)\n    end\n  end\nend"
    approach: 'The problem can be solved using dynamic programming by identifying whether
      each number of stones from 1 to n represents a winning or losing state. A state
      i is defined as winning (true) if there is at least one move that leads the opponent
      into a losing state (false). Specifically, if there exists an integer k such that
      k^2 <= i and dp[i - k^2] is false, then the current player can make that move
      to win, making dp[i] true.


      We initialize a boolean array dp of size n + 1, where dp[0] is false because a
      player starting with zero stones has no valid moves and loses. We then iterate
      through each number of stones i from 1 to n. For each i, we test all possible
      square numbers k^2 <= i; if we find any k such that dp[i - k^2] is false, we mark
      dp[i] as true and break the inner loop early. The final result is stored in dp[n].'
    time_complexity: O(n\sqrt{n}) because we iterate from 1 to n, and for each integer
      i, we check up to \sqrt{i} square numbers. The sum of square roots from 1 to n
      is approximately the integral of sqrt(x) from 0 to n, which results in a complexity
      of roughly (2/3)n^{1.5}.
    space_complexity: O(n) since we use a boolean array of size n + 1 to store the winning
      or losing status for every possible number of stones up to n.
    elapsed_time: 592.7802579402924
    model: gemini-3-flash-preview
    generated_at: '2026-08-10 01:17:54 '
---

## Problem #1510: Stone Game IV

**Difficulty:** Hard

**Topics:** Math, Dynamic Programming, Minimax, Game Theory, Nim Game, Sprague–Grundy Theorem, Zero-Sum Game

## Problem Description

<p>Alice and Bob take turns playing a game, with Alice starting first.</p>

<p>Initially, there are <code>n</code> stones in a pile. On each player&#39;s turn, that player makes a <em>move</em> consisting of removing <strong>any</strong> non-zero <strong>square number</strong> of stones in the pile.</p>

<p>Also, if a player cannot make a move, he/she loses the game.</p>

<p>Given a positive integer <code>n</code>, return <code>true</code> if and only if Alice wins the game otherwise return <code>false</code>, assuming both players play optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>Alice can remove 1 stone winning the game because Bob doesn&#39;t have any moves.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -&gt; 1 -&gt; 0).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> n is already a perfect square, Alice can win with one move, removing 4 stones (4 -&gt; 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Use dynamic programming to keep track of winning and losing states. Given some number of stones, Alice can win if she can force Bob onto a losing state.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved using dynamic programming by identifying whether each number of stones from 1 to n represents a winning or losing state. A state i is defined as winning (true) if there is at least one move that leads the opponent into a losing state (false). Specifically, if there exists an integer k such that k^2 <= i and dp[i - k^2] is false, then the current player can make that move to win, making dp[i] true.

We initialize a boolean array dp of size n + 1, where dp[0] is false because a player starting with zero stones has no valid moves and loses. We then iterate through each number of stones i from 1 to n. For each i, we test all possible square numbers k^2 <= i; if we find any k such that dp[i - k^2] is false, we mark dp[i] as true and break the inner loop early. The final result is stored in dp[n].

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
    bool winnerSquareGame(int n) {
        vector<bool> dp(n + 1, false);
        for (int i = 1; i <= n; ++i) {
            for (int k = 1; k * k <= i; ++k) {
                if (!dp[i - k * k]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean winnerSquareGame(int n) {
        boolean[] dp = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            for (int k = 1; k * k <= i; k++) {
                if (!dp[i - k * k]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        squares = [k * k for k in range(1, int(n**0.5) + 1)]
        for i in range(n + 1):
            if dp[i]:
                continue
            for sq in squares:
                if i + sq > n:
                    break
                dp[i + sq] = True
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

bool winnerSquareGame(int n) {
    bool *dp = (bool *)calloc(n + 1, sizeof(bool));
    if (!dp) return false;
    for (int i = 0; i <= n; i++) {
        if (dp[i]) continue;
        for (int k = 1; ; k++) {
            int sq = k * k;
            if (i + sq > n) break;
            dp[i + sq] = true;
        }
    }
    bool result = dp[n];
    free(dp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool WinnerSquareGame(int n) {
        bool[] dp = new bool[n + 1];
        for (int i = 0; i <= n; i++) {
            if (dp[i]) continue;
            for (int k = 1; ; k++) {
                int sq = k * k;
                if (i + sq > n) break;
                dp[i + sq] = true;
            }
        }
        return dp[n];
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
var winnerSquareGame = function(n) {
    const dp = new Uint8Array(n + 1);
    for (let i = 0; i <= n; i++) {
        if (dp[i]) continue;
        for (let k = 1; ; k++) {
            const sq = k * k;
            if (i + sq > n) break;
            dp[i + sq] = 1;
        }
    }
    return dp[n] === 1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function winnerSquareGame(n: number): boolean {
    const dp: boolean[] = new Array(n + 1).fill(false);
    for (let i = 1; i <= n; i++) {
        for (let k = 1; k * k <= i; k++) {
            if (!dp[i - k * k]) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
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
    function winnerSquareGame($n) {
        $dp = array_fill(0, $n + 1, false);
        for (\$i = 1; \$i <= $n; \$i++) {
            for (\$k = 1; \$k * \$k <= \$i; \$k++) {
                if (!\$dp[\$i - \$k * \$k]) {
                    \$dp[\$i] = true;
                    break;
                }
            }
        }
        return \$dp[\$n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func winnerSquareGame(_ n: Int) -> Bool {
        var dp = [Bool](repeating: false, count: n + 1)
        for i in 1...n {
            var k = 1
            while k * k <= i {
                if !dp[i - k * k] {
                    dp[i] = true
                    break
                }
                k += 1
            }
        }
        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun winnerSquareGame(n: Int): Boolean {
        val dp = BooleanArray(n + 1)
        for (i in 1..n) {
            var k = 1
            while (k * k <= i) {
                if (!dp[i - k * k]) {
                    dp[i] = true
                    break
                }
                k++
            }
        }
        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool winnerSquareGame(int n) {
    List<bool> dp = List.filled(n + 1, false);
    for (int i = 1; i <= n; i++) {
      for (int k = 1; k * k <= i; k++) {
        if (!dp[i - k * k]) {
          dp[i] = true;
          break;
        }
      }
    }
    return dp[n];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func winnerSquareGame(n int) bool {
    dp := make([]bool, n+1)
    for i := 1; i <= n; i++ {
        for k := 1; k*k <= i; k++ {
            if !dp[i-k*k] {
                dp[i] = true
                break
            }
        }
    }
    return dp[n]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Boolean}
def winner_square_game(n)
  dp = Array.new(n + 1, false)
  (1..n).each do |i|
    k = 1
    while k * k <= i
      if !dp[i - k * k]
        dp[i] = true
        break
      end
      k += 1
    end
  end
  dp[n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def winnerSquareGame(n: Int): Boolean = {
        val dp = new Array[Boolean](n + 1)
        for (i <- 1 to n) {
            var k = 1
            var found = false
            while (k * k <= i && !found) {
                if (!dp(i - k * k)) {
                    found = true
                }
                k += 1
            }
            dp(i) = found
        }
        dp(n)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn winner_square_game(n: i32) -> bool {
        let n = n as usize;
        let mut dp = vec![false; n + 1];
        for i in 0..=n {
            if !dp[i] {
                let mut k = 1;
                while i + k * k <= n {
                    dp[i + k * k] = true;
                    k += 1;
                }
            }
        }
        dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (winner-square-game n)
  (-> exact-integer? boolean?)
  (let ([dp (make-vector (+ n 1) #f)])
    (for ([i (in-range (+ n 1))])
      (when (not (vector-ref dp i))
        (let loop ([k 1])
          (let ([next (+ i (* k k))])
            (when (<= next n)
              (vector-set! dp next #t)
              (loop (+ k 1)))))))
    (vector-ref dp n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec winner_square_game(N :: integer()) -> boolean().
winner_square_game(N) ->
  Dp = ets:new(dp_table, [set, private]),
  solve(0, N, Dp),
  Result = ets:member(Dp, N),
  ets:delete(Dp),
  Result.

solve(I, N, Dp) when I > N -> ok;
solve(I, N, Dp) ->
  case ets:member(Dp, I) of
    true -> solve(I + 1, N, Dp);
    false ->
      mark_winning(I, 1, N, Dp),
      solve(I + 1, N, Dp)
  end.

mark_winning(I, K, N, Dp) ->
  Next = I + K * K,
  if
    Next > N -> ok;
    true ->
      ets:insert(Dp, {Next, true}),
      mark_winning(I, K + 1, N, Dp)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec winner_square_game(n :: integer) :: boolean
  def winner_square_game(n) do
    dp = :ets.new(:dp_table, [:set, :private])
    solve(0, n, dp)
    result = :ets.member(dp, n)
    :ets.delete(dp)
    result
  end

  defp solve(i, n, dp) when i > n, do: :ok
  defp solve(i, n, dp) do
    unless :ets.member(dp, i) do
      mark_winning(i, 1, n, dp)
    end
    solve(i + 1, n, dp)
  end

  defp mark_winning(i, k, n, dp) do
    next = i + k * k
    if next <= n do
      :ets.insert(dp, {next, true})
      mark_winning(i, k + 1, n, dp)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n\sqrt{n}) because we iterate from 1 to n, and for each integer i, we check up to \sqrt{i} square numbers. The sum of square roots from 1 to n is approximately the integral of sqrt(x) from 0 to n, which results in a complexity of roughly (2/3)n^{1.5}.
- **Space Complexity:** O(n) since we use a boolean array of size n + 1 to store the winning or losing status for every possible number of stones up to n.
