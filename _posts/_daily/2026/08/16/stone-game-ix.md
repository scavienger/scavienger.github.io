---
layout: post
title: "Stone Game IX"
date: 2026-08-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Greedy", "Minimax", "Counting", "Game Theory", "Nim Game", "Zero-Sum Game"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/stone-game-ix/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool stoneGameIX(vector<int>& stones) {\n\
        \        int cnt[3] = {0, 0, 0};\n        for (int s : stones) {\n         \
        \   cnt[s % 3]++;\n        }\n        if (cnt[0] % 2 == 0) {\n            return\
        \ cnt[1] > 0 && cnt[2] > 0;\n        }\n        return (cnt[1] - cnt[2] > 2)\
        \ || (cnt[2] - cnt[1] > 2);\n    }\n};"
      java: "class Solution {\n    public boolean stoneGameIX(int[] stones) {\n    \
        \    int[] cnt = new int[3];\n        for (int s : stones) {\n            cnt[s\
        \ % 3]++;\n        }\n        if (cnt[0] % 2 == 0) {\n            return cnt[1]\
        \ > 0 && cnt[2] > 0;\n        }\n        return Math.abs(cnt[1] - cnt[2]) >\
        \ 2;\n    }\n}"
      python: "class Solution(object):\n    def stoneGameIX(self, stones):\n       \
        \ \"\"\"\n        :type stones: List[int]\n        :rtype: bool\n        \"\"\
        \"\n        cnt = [0, 0, 0]\n        for s in stones:\n            cnt[s % 3]\
        \ += 1\n        if cnt[0] % 2 == 0:\n            return cnt[1] > 0 and cnt[2]\
        \ > 0\n        return abs(cnt[1] - cnt[2]) > 2"
      python3: "class Solution:\n    def stoneGameIX(self, stones: List[int]) -> bool:\n\
        \        cnt = [0, 0, 0]\n        for s in stones:\n            cnt[s % 3] +=\
        \ 1\n        if cnt[0] % 2 == 0:\n            return cnt[1] > 0 and cnt[2] >\
        \ 0\n        return abs(cnt[1] - cnt[2]) > 2"
      c: "bool stoneGameIX(int* stones, int stonesSize) {\n    int cnt[3] = {0, 0, 0};\n\
        \    for (int i = 0; i < stonesSize; i++) {\n        cnt[stones[i] % 3]++;\n\
        \    }\n    if (cnt[0] % 2 == 0) {\n        return cnt[1] > 0 && cnt[2] > 0;\n\
        \    } else {\n        return (cnt[1] - cnt[2] > 2) || (cnt[2] - cnt[1] > 2);\n\
        \    }\n}"
      csharp: "using System;\n\npublic class Solution {\n    public bool StoneGameIX(int[]\
        \ stones) {\n        int[] counts = new int[3];\n        foreach (int s in stones)\
        \ {\n            counts[s % 3]++;\n        }\n\n        if (counts[0] % 2 ==\
        \ 0) {\n            return counts[1] > 0 && counts[2] > 0;\n        }\n\n  \
        \      return Math.Abs(counts[1] - counts[2]) > 2;\n    }\n}"
      javascript: "/**\n * @param {number[]} stones\n * @return {boolean}\n */\nvar\
        \ stoneGameIX = function(stones) {\n    let counts = [0, 0, 0];\n    for (let\
        \ s of stones) {\n        counts[s % 3]++;\n    }\n\n    if (counts[0] % 2 ===\
        \ 0) {\n        return counts[1] > 0 && counts[2] > 0;\n    }\n\n    return\
        \ Math.abs(counts[1] - counts[2]) > 2;\n};"
      typescript: "function stoneGameIX(stones: number[]): boolean {\n    let counts:\
        \ [number, number, number] = [0, 0, 0];\n    for (let s of stones) {\n     \
        \   counts[s % 3]++;\n    }\n\n    if (counts[0] % 2 === 0) {\n        return\
        \ counts[1] > 0 && counts[2] > 0;\n    }\n\n    return Math.abs(counts[1] -\
        \ counts[2]) > 2;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $stones\n     * @return\
        \ Boolean\n     */\n    function stoneGameIX($stones) {\n        $counts = [0,\
        \ 0, 0];\n        foreach ($stones as $s) {\n            $counts[$s % 3]++;\n\
        \        }\n\n        if ($counts[0] % 2 == 0) {\n            return $counts[1]\
        \ > 0 && $counts[2] > 0;\n        }\n\n        return abs($counts[1] - $counts[2])\
        \ > 2;\n    }\n}"
      swift: "class Solution {\n    func stoneGameIX(_ stones: [Int]) -> Bool {\n  \
        \      var counts = [0, 0, 0]\n        for s in stones {\n            counts[s\
        \ % 3] += 1\n        }\n\n        if counts[0] % 2 == 0 {\n            return\
        \ counts[1] > 0 && counts[2] > 0\n        }\n\n        return abs(counts[1]\
        \ - counts[2]) > 2\n    }\n}"
      kotlin: "class Solution {\n    fun stoneGameIX(stones: IntArray): Boolean {\n\
        \        var cnt0 = 0\n        var cnt1 = 0\n        var cnt2 = 0\n        for\
        \ (s in stones) {\n            val rem = s % 3\n            if (rem == 0) {\n\
        \                cnt0++\n            } else if (rem == 1) {\n              \
        \  cnt1++\n            } else {\n                cnt2++\n            }\n   \
        \     }\n        return if (cnt0 % 2 == 0) {\n            cnt1 > 0 && cnt2 >\
        \ 0\n        } else {\n            Math.abs(cnt1 - cnt2) > 2\n        }\n  \
        \  }\n}"
      dart: "class Solution {\n  bool stoneGameIX(List<int> stones) {\n    int cnt0\
        \ = 0;\n    int cnt1 = 0;\n    int cnt2 = 0;\n    for (int s in stones) {\n\
        \      int rem = s % 3;\n      if (rem == 0) {\n        cnt0++;\n      } else\
        \ if (rem == 1) {\n        cnt1++;\n      } else {\n        cnt2++;\n      }\n\
        \    }\n    if (cnt0 % 2 == 0) {\n      return cnt1 > 0 && cnt2 > 0;\n    }\
        \ else {\n      return (cnt1 - cnt2).abs() > 2;\n    }\n  }\n}"
      go: "func stoneGameIX(stones []int) bool {\n\tcnt0, cnt1, cnt2 := 0, 0, 0\n\t\
        for _, s := range stones {\n\t\trem := s % 3\n\t\tif rem == 0 {\n\t\t\tcnt0++\n\
        \t\t} else if rem == 1 {\n\t\t\tcnt1++\n\t\t} else {\n\t\t\tcnt2++\n\t\t}\n\t\
        }\n\tif cnt0%2 == 0 {\n\t\treturn cnt1 > 0 && cnt2 > 0\n\t}\n\tdiff := cnt1\
        \ - cnt2\n\tif diff < 0 {\n\t\tdiff = -diff\n\t}\n\treturn diff > 2\n}"
      ruby: "# @param {Integer[]} stones\n# @return {Boolean}\ndef stone_game_ix(stones)\n\
        \  cnt0 = 0\n  cnt1 = 0\n  cnt2 = 0\n  stones.each do |s|\n    rem = s % 3\n\
        \    if rem == 0\n      cnt0 += 1\n    elsif rem == 1\n      cnt1 += 1\n   \
        \ else\n      cnt2 += 1\n    end\n  end\n  if cnt0 % 2 == 0\n    cnt1 > 0 &&\
        \ cnt2 > 0\n  else\n    (cnt1 - cnt2).abs > 2\n  end\nend"
      scala: "object Solution {\n    def stoneGameIX(stones: Array[Int]): Boolean =\
        \ {\n        var cnt0 = 0\n        var cnt1 = 0\n        var cnt2 = 0\n    \
        \    for (s <- stones) {\n            val rem = s % 3\n            if (rem ==\
        \ 0) {\n                cnt0 += 1\n            } else if (rem == 1) {\n    \
        \            cnt1 += 1\n            } else {\n                cnt2 += 1\n  \
        \          }\n        }\n        if (cnt0 % 2 == 0) {\n            cnt1 > 0\
        \ && cnt2 > 0\n        } else {\n            math.abs(cnt1 - cnt2) > 2\n   \
        \     }\n    }\n}"
      rust: "impl Solution {\n    pub fn stone_game_ix(stones: Vec<i32>) -> bool {\n\
        \        let mut counts = [0i32; 3];\n        for &s in &stones {\n        \
        \    counts[(s % 3) as usize] += 1;\n        }\n\n        let c0 = counts[0];\n\
        \        let c1 = counts[1];\n        let c2 = counts[2];\n\n        if c0 %\
        \ 2 == 0 {\n            c1 > 0 && c2 > 0\n        } else {\n            (c1\
        \ - c2).abs() > 2\n        }\n    }\n}"
      racket: "(define/contract (stone-game-ix stones)\n  (-> (listof exact-integer?)\
        \ boolean?)\n  (let-values ([(c0 c1 c2) (for/fold ([c0 0] [c1 0] [c2 0]) ([s\
        \ stones])\n                             (let ([m (modulo s 3)])\n         \
        \                      (cond\n                                 [(= m 0) (values\
        \ (+ c0 1) c1 c2)]\n                                 [(= m 1) (values c0 (+\
        \ c1 1) c2)]\n                                 [(= m 2) (values c0 c1 (+ c2\
        \ 1))]))])\n    (if (even? c0)\n        (and (> c1 0) (> c2 0))\n        (>\
        \ (abs (- c1 c2)) 2))))"
      erlang: "-spec stone_game_ix(Stones :: [integer()]) -> boolean().\nstone_game_ix(Stones)\
        \ ->\n    {C0, C1, C2} = lists:foldl(fun(S, {Acc0, Acc1, Acc2}) ->\n       \
        \ case S rem 3 of\n            0 -> {Acc0 + 1, Acc1, Acc2};\n            1 ->\
        \ {Acc0, Acc1 + 1, Acc2};\n            2 -> {Acc0, Acc1, Acc2 + 1}\n       \
        \ end\n    end, {0, 0, 0}, Stones),\n    case C0 rem 2 of\n        0 -> (C1\
        \ > 0) and (C2 > 0);\n        1 -> abs(C1 - C2) > 2\n    end."
      elixir: "defmodule Solution do\n  @spec stone_game_ix(stones :: [integer]) ::\
        \ boolean\n  def stone_game_ix(stones) do\n    {c0, c1, c2} = Enum.reduce(stones,\
        \ {0, 0, 0}, fn s, {acc0, acc1, acc2} ->\n      case rem(s, 3) do\n        0\
        \ -> {acc0 + 1, acc1, acc2}\n        1 -> {acc0, acc1 + 1, acc2}\n        2\
        \ -> {acc0, acc1, acc2 + 1}\n      end\n    end)\n    if rem(c0, 2) == 0 do\n\
        \      c1 > 0 and c2 > 0\n    else\n      abs(c1 - c2) > 2\n    end\n  end\n\
        end"
    approach: 'The problem can be solved by counting the stones based on their remainders
      when divided by 3. Let $cnt_0, cnt_1$, and $cnt_2$ be the counts of stones with
      remainders 0, 1, and 2, respectively. Stones with remainder 0 are turn-flippers:
      they don''t change the current sum modulo 3, but they change whose turn it is.
      Alice starts first and cannot pick a stone with remainder 0 because the initial
      sum is 0, making it divisible by 3 and resulting in an immediate loss. Thus, she
      must begin with a stone of remainder 1 or 2.


      The game''s outcome depends on the parity of $cnt_0$. If $cnt_0$ is even, the
      zero-remainder stones effectively cancel each other out, and Alice wins if she
      can start with a 1 or 2 and force Bob into a situation where all available moves
      lead to a sum divisible by 3. This occurs if both $cnt_1 > 0$ and $cnt_2 > 0$.
      If $cnt_0$ is odd, it acts as a single turn-skip that can be used once. In this
      scenario, Alice wins only if the difference between the number of stones of remainder
      1 and remainder 2 is large enough to survive the turn-skip and force Bob into
      a loss, which mathematically simplifies to $|cnt_1 - cnt_2| > 2$.'
    time_complexity: 'O(n) with one-paragraph explanation: We iterate through the stones
      array exactly once to count the occurrences of each remainder modulo 3, where
      n is the number of stones in the input array.'
    space_complexity: 'O(1) with one-paragraph explanation: We use a fixed-size array
      of length 3 (or three integer variables) to store the counts of the remainders,
      which does not grow with the input size.'
    elapsed_time: 335.2713940143585
    model: gemini-3-flash-preview
    generated_at: '2026-08-16 00:56:35 '
---

## Problem #2029: Stone Game IX

**Difficulty:** Medium

**Topics:** Array, Math, Greedy, Minimax, Counting, Game Theory, Nim Game, Zero-Sum Game

## Problem Description

<p>Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array <code>stones</code>, where <code>stones[i]</code> is the <strong>value</strong> of the <code>i<sup>th</sup></code> stone.</p>

<p>Alice and Bob take turns, with <strong>Alice</strong> starting first. On each turn, the player may remove any stone from <code>stones</code>. The player who removes a stone <strong>loses</strong> if the <strong>sum</strong> of the values of <strong>all removed stones</strong> is divisible by <code>3</code>. Bob will win automatically if there are no remaining stones (even if it is Alice&#39;s turn).</p>

<p>Assuming both players play <strong>optimally</strong>, return <code>true</code> <em>if Alice wins and</em> <code>false</code> <em>if Bob wins</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [2,1]
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [2]
<strong>Output:</strong> false
<strong>Explanation:</strong>&nbsp;Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> stones = [5,1,2,4,3]
<strong>Output:</strong> false
<strong>Explanation:</strong> Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= stones[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. There are limited outcomes given the current sum and the stones remaining.

2. Can we greedily simulate starting with taking a stone with remainder 1 or 2 divided by 3?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by counting the stones based on their remainders when divided by 3. Let $cnt_0, cnt_1$, and $cnt_2$ be the counts of stones with remainders 0, 1, and 2, respectively. Stones with remainder 0 are turn-flippers: they don't change the current sum modulo 3, but they change whose turn it is. Alice starts first and cannot pick a stone with remainder 0 because the initial sum is 0, making it divisible by 3 and resulting in an immediate loss. Thus, she must begin with a stone of remainder 1 or 2.

The game's outcome depends on the parity of $cnt_0$. If $cnt_0$ is even, the zero-remainder stones effectively cancel each other out, and Alice wins if she can start with a 1 or 2 and force Bob into a situation where all available moves lead to a sum divisible by 3. This occurs if both $cnt_1 > 0$ and $cnt_2 > 0$. If $cnt_0$ is odd, it acts as a single turn-skip that can be used once. In this scenario, Alice wins only if the difference between the number of stones of remainder 1 and remainder 2 is large enough to survive the turn-skip and force Bob into a loss, which mathematically simplifies to $|cnt_1 - cnt_2| > 2$.

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
    bool stoneGameIX(vector<int>& stones) {
        int cnt[3] = {0, 0, 0};
        for (int s : stones) {
            cnt[s % 3]++;
        }
        if (cnt[0] % 2 == 0) {
            return cnt[1] > 0 && cnt[2] > 0;
        }
        return (cnt[1] - cnt[2] > 2) || (cnt[2] - cnt[1] > 2);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean stoneGameIX(int[] stones) {
        int[] cnt = new int[3];
        for (int s : stones) {
            cnt[s % 3]++;
        }
        if (cnt[0] % 2 == 0) {
            return cnt[1] > 0 && cnt[2] > 0;
        }
        return Math.abs(cnt[1] - cnt[2]) > 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        cnt = [0, 0, 0]
        for s in stones:
            cnt[s % 3] += 1
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        return abs(cnt[1] - cnt[2]) > 2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        for s in stones:
            cnt[s % 3] += 1
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        return abs(cnt[1] - cnt[2]) > 2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool stoneGameIX(int* stones, int stonesSize) {
    int cnt[3] = {0, 0, 0};
    for (int i = 0; i < stonesSize; i++) {
        cnt[stones[i] % 3]++;
    }
    if (cnt[0] % 2 == 0) {
        return cnt[1] > 0 && cnt[2] > 0;
    } else {
        return (cnt[1] - cnt[2] > 2) || (cnt[2] - cnt[1] > 2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public bool StoneGameIX(int[] stones) {
        int[] counts = new int[3];
        foreach (int s in stones) {
            counts[s % 3]++;
        }

        if (counts[0] % 2 == 0) {
            return counts[1] > 0 && counts[2] > 0;
        }

        return Math.Abs(counts[1] - counts[2]) > 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} stones
 * @return {boolean}
 */
var stoneGameIX = function(stones) {
    let counts = [0, 0, 0];
    for (let s of stones) {
        counts[s % 3]++;
    }

    if (counts[0] % 2 === 0) {
        return counts[1] > 0 && counts[2] > 0;
    }

    return Math.abs(counts[1] - counts[2]) > 2;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function stoneGameIX(stones: number[]): boolean {
    let counts: [number, number, number] = [0, 0, 0];
    for (let s of stones) {
        counts[s % 3]++;
    }

    if (counts[0] % 2 === 0) {
        return counts[1] > 0 && counts[2] > 0;
    }

    return Math.abs(counts[1] - counts[2]) > 2;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $stones
     * @return Boolean
     */
    function stoneGameIX($stones) {
        $counts = [0, 0, 0];
        foreach ($stones as $s) {
            $counts[$s % 3]++;
        }

        if ($counts[0] % 2 == 0) {
            return $counts[1] > 0 && $counts[2] > 0;
        }

        return abs($counts[1] - $counts[2]) > 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func stoneGameIX(_ stones: [Int]) -> Bool {
        var counts = [0, 0, 0]
        for s in stones {
            counts[s % 3] += 1
        }

        if counts[0] % 2 == 0 {
            return counts[1] > 0 && counts[2] > 0
        }

        return abs(counts[1] - counts[2]) > 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun stoneGameIX(stones: IntArray): Boolean {
        var cnt0 = 0
        var cnt1 = 0
        var cnt2 = 0
        for (s in stones) {
            val rem = s % 3
            if (rem == 0) {
                cnt0++
            } else if (rem == 1) {
                cnt1++
            } else {
                cnt2++
            }
        }
        return if (cnt0 % 2 == 0) {
            cnt1 > 0 && cnt2 > 0
        } else {
            Math.abs(cnt1 - cnt2) > 2
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool stoneGameIX(List<int> stones) {
    int cnt0 = 0;
    int cnt1 = 0;
    int cnt2 = 0;
    for (int s in stones) {
      int rem = s % 3;
      if (rem == 0) {
        cnt0++;
      } else if (rem == 1) {
        cnt1++;
      } else {
        cnt2++;
      }
    }
    if (cnt0 % 2 == 0) {
      return cnt1 > 0 && cnt2 > 0;
    } else {
      return (cnt1 - cnt2).abs() > 2;
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func stoneGameIX(stones []int) bool {
	cnt0, cnt1, cnt2 := 0, 0, 0
	for _, s := range stones {
		rem := s % 3
		if rem == 0 {
			cnt0++
		} else if rem == 1 {
			cnt1++
		} else {
			cnt2++
		}
	}
	if cnt0%2 == 0 {
		return cnt1 > 0 && cnt2 > 0
	}
	diff := cnt1 - cnt2
	if diff < 0 {
		diff = -diff
	}
	return diff > 2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} stones
# @return {Boolean}
def stone_game_ix(stones)
  cnt0 = 0
  cnt1 = 0
  cnt2 = 0
  stones.each do |s|
    rem = s % 3
    if rem == 0
      cnt0 += 1
    elsif rem == 1
      cnt1 += 1
    else
      cnt2 += 1
    end
  end
  if cnt0 % 2 == 0
    cnt1 > 0 && cnt2 > 0
  else
    (cnt1 - cnt2).abs > 2
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def stoneGameIX(stones: Array[Int]): Boolean = {
        var cnt0 = 0
        var cnt1 = 0
        var cnt2 = 0
        for (s <- stones) {
            val rem = s % 3
            if (rem == 0) {
                cnt0 += 1
            } else if (rem == 1) {
                cnt1 += 1
            } else {
                cnt2 += 1
            }
        }
        if (cnt0 % 2 == 0) {
            cnt1 > 0 && cnt2 > 0
        } else {
            math.abs(cnt1 - cnt2) > 2
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn stone_game_ix(stones: Vec<i32>) -> bool {
        let mut counts = [0i32; 3];
        for &s in &stones {
            counts[(s % 3) as usize] += 1;
        }

        let c0 = counts[0];
        let c1 = counts[1];
        let c2 = counts[2];

        if c0 % 2 == 0 {
            c1 > 0 && c2 > 0
        } else {
            (c1 - c2).abs() > 2
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (stone-game-ix stones)
  (-> (listof exact-integer?) boolean?)
  (let-values ([(c0 c1 c2) (for/fold ([c0 0] [c1 0] [c2 0]) ([s stones])
                             (let ([m (modulo s 3)])
                               (cond
                                 [(= m 0) (values (+ c0 1) c1 c2)]
                                 [(= m 1) (values c0 (+ c1 1) c2)]
                                 [(= m 2) (values c0 c1 (+ c2 1))]))])
    (if (even? c0)
        (and (> c1 0) (> c2 0))
        (> (abs (- c1 c2)) 2))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec stone_game_ix(Stones :: [integer()]) -> boolean().
stone_game_ix(Stones) ->
    {C0, C1, C2} = lists:foldl(fun(S, {Acc0, Acc1, Acc2}) ->
        case S rem 3 of
            0 -> {Acc0 + 1, Acc1, Acc2};
            1 -> {Acc0, Acc1 + 1, Acc2};
            2 -> {Acc0, Acc1, Acc2 + 1}
        end
    end, {0, 0, 0}, Stones),
    case C0 rem 2 of
        0 -> (C1 > 0) and (C2 > 0);
        1 -> abs(C1 - C2) > 2
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec stone_game_ix(stones :: [integer]) :: boolean
  def stone_game_ix(stones) do
    {c0, c1, c2} = Enum.reduce(stones, {0, 0, 0}, fn s, {acc0, acc1, acc2} ->
      case rem(s, 3) do
        0 -> {acc0 + 1, acc1, acc2}
        1 -> {acc0, acc1 + 1, acc2}
        2 -> {acc0, acc1, acc2 + 1}
      end
    end)
    if rem(c0, 2) == 0 do
      c1 > 0 and c2 > 0
    else
      abs(c1 - c2) > 2
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) with one-paragraph explanation: We iterate through the stones array exactly once to count the occurrences of each remainder modulo 3, where n is the number of stones in the input array.
- **Space Complexity:** O(1) with one-paragraph explanation: We use a fixed-size array of length 3 (or three integer variables) to store the counts of the remainders, which does not grow with the input size.
