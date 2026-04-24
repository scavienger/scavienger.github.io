---
layout: post
title: "Furthest Point From Origin"
date: 2026-04-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "Counting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/furthest-point-from-origin/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int furthestDistanceFromOrigin(string moves)\
        \ {\n        int l_count = 0, r_count = 0, u_count = 0;\n        for (char c\
        \ : moves) {\n            if (c == 'L') l_count++;\n            else if (c ==\
        \ 'R') r_count++;\n            else u_count++;\n        }\n        return abs(l_count\
        \ - r_count) + u_count;\n    }\n};"
      java: "class Solution {\n    public int furthestDistanceFromOrigin(String moves)\
        \ {\n        int lCount = 0, rCount = 0, uCount = 0;\n        for (int i = 0;\
        \ i < moves.length(); i++) {\n            char c = moves.charAt(i);\n      \
        \      if (c == 'L') lCount++;\n            else if (c == 'R') rCount++;\n \
        \           else uCount++;\n        }\n        return Math.abs(lCount - rCount)\
        \ + uCount;\n    }\n}"
      python: "class Solution(object):\n    def furthestDistanceFromOrigin(self, moves):\n\
        \        \"\"\"\n        :type moves: str\n        :rtype: int\n        \"\"\
        \"\n        l_count = moves.count('L')\n        r_count = moves.count('R')\n\
        \        u_count = moves.count('_')\n        return abs(l_count - r_count) +\
        \ u_count"
      python3: "class Solution:\n    def furthestDistanceFromOrigin(self, moves: str)\
        \ -> int:\n        l_count = moves.count('L')\n        r_count = moves.count('R')\n\
        \        u_count = moves.count('_')\n        return abs(l_count - r_count) +\
        \ u_count"
      c: "int furthestDistanceFromOrigin(char* moves) {\n    int l_count = 0, r_count\
        \ = 0, u_count = 0;\n    for (int i = 0; moves[i] != '\\0'; i++) {\n       \
        \ if (moves[i] == 'L') l_count++;\n        else if (moves[i] == 'R') r_count++;\n\
        \        else u_count++;\n    }\n    int diff = l_count - r_count;\n    if (diff\
        \ < 0) diff = -diff;\n    return diff + u_count;\n}"
      csharp: "public class Solution {\n    public int FurthestDistanceFromOrigin(string\
        \ moves) {\n        int lCount = 0, rCount = 0, uCount = 0;\n        foreach\
        \ (char c in moves) {\n            if (c == 'L') lCount++;\n            else\
        \ if (c == 'R') rCount++;\n            else uCount++;\n        }\n        return\
        \ Math.Abs(lCount - rCount) + uCount;\n    }\n}"
      javascript: "/**\n * @param {string} moves\n * @return {number}\n */\nvar furthestDistanceFromOrigin\
        \ = function(moves) {\n    let lCount = 0, rCount = 0, uCount = 0;\n    for\
        \ (let i = 0; i < moves.length; i++) {\n        if (moves[i] === 'L') lCount++;\n\
        \        else if (moves[i] === 'R') rCount++;\n        else uCount++;\n    }\n\
        \    return Math.abs(lCount - rCount) + uCount;\n};"
      typescript: "function furthestDistanceFromOrigin(moves: string): number {\n  \
        \  let countL = 0;\n    let countR = 0;\n    let countUnderscore = 0;\n    for\
        \ (let i = 0; i < moves.length; i++) {\n        if (moves[i] === 'L') {\n  \
        \          countL++;\n        } else if (moves[i] === 'R') {\n            countR++;\n\
        \        } else {\n            countUnderscore++;\n        }\n    }\n    return\
        \ Math.abs(countL - countR) + countUnderscore;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $moves\n     * @return\
        \ Integer\n     */\n    function furthestDistanceFromOrigin($moves) {\n    \
        \    $countL = 0;\n        $countR = 0;\n        $countUnderscore = 0;\n   \
        \     $len = strlen($moves);\n        for ($i = 0; $i < $len; $i++) {\n    \
        \        if ($moves[$i] == 'L') {\n                $countL++;\n            }\
        \ else if ($moves[$i] == 'R') {\n                $countR++;\n            } else\
        \ {\n                $countUnderscore++;\n            }\n        }\n       \
        \ return abs($countL - countR) + $countUnderscore;\n    }\n}"
      swift: "class Solution {\n    func furthestDistanceFromOrigin(_ moves: String)\
        \ -> Int {\n        var countL = 0\n        var countR = 0\n        var countUnderscore\
        \ = 0\n        for char in moves {\n            if char == \"L\" {\n       \
        \         countL += 1\n            } else if char == \"R\" {\n             \
        \   countR += 1\n            } else {\n                countUnderscore += 1\n\
        \            }\n        }\n        return abs(countL - countR) + countUnderscore\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun furthestDistanceFromOrigin(moves: String):\
        \ Int {\n        var countL = 0\n        var countR = 0\n        var countUnderscore\
        \ = 0\n        for (char in moves) {\n            when (char) {\n          \
        \      'L' -> countL++\n                'R' -> countR++\n                '_'\
        \ -> countUnderscore++\n            }\n        }\n        return Math.abs(countL\
        \ - countR) + countUnderscore\n    }\n}"
      dart: "class Solution {\n  int furthestDistanceFromOrigin(String moves) {\n  \
        \  int countL = 0;\n    int countR = 0;\n    int countUnderscore = 0;\n    for\
        \ (int i = 0; i < moves.length; i++) {\n      if (moves[i] == 'L') {\n     \
        \   countL++;\n      } else if (moves[i] == 'R') {\n        countR++;\n    \
        \  } else {\n        countUnderscore++;\n      }\n    }\n    return (countL\
        \ - countR).abs() + countUnderscore;\n  }\n}"
      go: "func furthestDistanceFromOrigin(moves string) int {\n    countL := 0\n  \
        \  countR := 0\n    countUnderscore := 0\n    for _, char := range moves {\n\
        \        if char == 'L' {\n            countL++\n        } else if char == 'R'\
        \ {\n            countR++\n        } else {\n            countUnderscore++\n\
        \        }\n    }\n    diff := countL - countR\n    if diff < 0 {\n        diff\
        \ = -diff\n    }\n    return diff + countUnderscore\n}"
      ruby: "# @param {String} moves\n# @return {Integer}\ndef furthest_distance_from_origin(moves)\n\
        \  l_count = moves.count('L')\n  r_count = moves.count('R')\n  underscore_count\
        \ = moves.count('_')\n  (l_count - r_count).abs + underscore_count\nend"
      scala: "object Solution {\n  def furthestDistanceFromOrigin(moves: String): Int\
        \ = {\n    val lCount = moves.count(_ == 'L')\n    val rCount = moves.count(_\
        \ == 'R')\n    val underscoreCount = moves.count(_ == '_')\n    (lCount - rCount).abs\
        \ + underscoreCount\n  }\n}"
      rust: "impl Solution {\n    pub fn furthest_distance_from_origin(moves: String)\
        \ -> i32 {\n        let (mut l_count, mut r_count, mut underscore_count) = (0,\
        \ 0, 0);\n        for c in moves.chars() {\n            match c {\n        \
        \        'L' => l_count += 1,\n                'R' => r_count += 1,\n      \
        \          '_' => underscore_count += 1,\n                _ => ()\n        \
        \    }\n        }\n        (l_count - r_count).abs() + underscore_count\n  \
        \  }\n}"
      racket: "(define/contract (furthest-distance-from-origin moves)\n  (-> string?\
        \ exact-integer?)\n  (let-values ([(l r u) \n                (for/fold ([l 0]\
        \ [r 0] [u 0])\n                          ([c (in-string moves)])\n        \
        \          (cond\n                    [(char=? c #\\L) (values (+ l 1) r u)]\n\
        \                    [(char=? c #\\R) (values l (+ r 1) u)]\n              \
        \      [(char=? c #\\_) (values l r (+ u 1))]\n                    [else (values\
        \ l r u)]))])\n    (+ (abs (- l r)) u)))"
      erlang: "-spec furthest_distance_from_origin(Moves :: unicode:unicode_binary())\
        \ -> integer().\nfurthest_distance_from_origin(Moves) ->\n  {L, R, U} = lists:foldl(fun(C,\
        \ {AccL, AccR, AccU}) ->\n    case C of\n      $L -> {AccL + 1, AccR, AccU};\n\
        \      $R -> {AccL, AccR + 1, AccU};\n      $_ -> {AccL, AccR, AccU + 1};\n\
        \      _ -> {AccL, AccR, AccU}\n    end\n  end, {0, 0, 0}, binary_to_list(Moves)),\n\
        \  abs(L - R) + U."
      elixir: "defmodule Solution do\n  @spec furthest_distance_from_origin(moves ::\
        \ String.t) :: integer\n  def furthest_distance_from_origin(moves) do\n    {l,\
        \ r, u} = \n      moves\n      |> String.to_charlist()\n      |> Enum.reduce({0,\
        \ 0, 0}, fn \n        ?L, {l, r, u} -> {l + 1, r, u}\n        ?R, {l, r, u}\
        \ -> {l, r + 1, u}\n        ?_, {l, r, u} -> {l, r, u + 1}\n        _, acc ->\
        \ acc\n      end)\n    abs(l - r) + u\n  end\nend"
    approach: "The core intuition is that to maximize the distance from the origin,\
      \ all underscores should be converted to either 'L' or 'R' consistently, depending\
      \ on which direction currently has more moves or which direction results in a\
      \ larger absolute displacement. By calculating the difference between the number\
      \ of 'R' moves and 'L' moves, we determine the net displacement caused by fixed\
      \ characters. The underscores can then be added to this displacement to move further\
      \ away in whichever direction (positive or negative) results in a larger absolute\
      \ value.\n\nMathematically, let $L$ be the count of 'L', $R$ be the count of 'R',\
      \ and $U$ be the count of underscores. The position after all moves will be $(R\
      \ - L) + \text{offset}$, where the offset is formed by assigning each underscore\
      \ a value of $+1$ or $-1$. To maximize the absolute distance, we calculate the\
      \ absolute difference between $R$ and $L$ and then add the total number of underscores\
      \ $U$ to it. This effectively treats all underscores as moves in the direction\
      \ that already has the net majority, or simply picks a direction if they are balanced,\
      \ resulting in the formula: $abs(R - L) + U$."
    time_complexity: O(n) where n is the length of the moves string. We perform a single
      pass through the string (or multiple passes to count specific characters) to count
      the occurrences of 'L', 'R', and '_'.
    space_complexity: O(1) because we only use a constant amount of extra space for
      integer variables to store the counts of the characters, regardless of the input
      size.
    elapsed_time: 57.55170488357544
    model: gemini-3-flash-preview
    generated_at: '2026-04-24 01:59:14 '
---

## Problem #2833: Furthest Point From Origin

**Difficulty:** Easy

**Topics:** String, Counting

## Problem Description

<p>You are given a string <code>moves</code> of length <code>n</code> consisting only of characters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, and <code>&#39;_&#39;</code>. The string represents your movement on a number line starting from the origin <code>0</code>.</p>

<p>In the <code>i<sup>th</sup></code> move, you can choose one of the following directions:</p>

<ul>
	<li>move to the left if <code>moves[i] = &#39;L&#39;</code> or <code>moves[i] = &#39;_&#39;</code></li>
	<li>move to the right if <code>moves[i] = &#39;R&#39;</code> or <code>moves[i] = &#39;_&#39;</code></li>
</ul>

<p>Return <em>the <strong>distance from the origin</strong> of the <strong>furthest</strong> point you can get to after </em><code>n</code><em> moves</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;L_RL__R&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves &quot;LLRLLLR&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;_R__LL_&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves &quot;LRLLLLL&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;_______&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves &quot;RRRRRRR&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= moves.length == n &lt;= 50</code></li>
	<li><code>moves</code> consists only of characters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code> and <code>&#39;_&#39;</code>.</li>
</ul>


## Hints

1. In an optimal answer, all occurrences of `'_’` will be replaced with the **same** character.

2. Replace all characters of `'_’` with the character that occurs the most.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core intuition is that to maximize the distance from the origin, all underscores should be converted to either 'L' or 'R' consistently, depending on which direction currently has more moves or which direction results in a larger absolute displacement. By calculating the difference between the number of 'R' moves and 'L' moves, we determine the net displacement caused by fixed characters. The underscores can then be added to this displacement to move further away in whichever direction (positive or negative) results in a larger absolute value.

Mathematically, let $L$ be the count of 'L', $R$ be the count of 'R', and $U$ be the count of underscores. The position after all moves will be $(R - L) + 	ext{offset}$, where the offset is formed by assigning each underscore a value of $+1$ or $-1$. To maximize the absolute distance, we calculate the absolute difference between $R$ and $L$ and then add the total number of underscores $U$ to it. This effectively treats all underscores as moves in the direction that already has the net majority, or simply picks a direction if they are balanced, resulting in the formula: $abs(R - L) + U$.

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
    int furthestDistanceFromOrigin(string moves) {
        int l_count = 0, r_count = 0, u_count = 0;
        for (char c : moves) {
            if (c == 'L') l_count++;
            else if (c == 'R') r_count++;
            else u_count++;
        }
        return abs(l_count - r_count) + u_count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        int lCount = 0, rCount = 0, uCount = 0;
        for (int i = 0; i < moves.length(); i++) {
            char c = moves.charAt(i);
            if (c == 'L') lCount++;
            else if (c == 'R') rCount++;
            else uCount++;
        }
        return Math.abs(lCount - rCount) + uCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l_count = moves.count('L')
        r_count = moves.count('R')
        u_count = moves.count('_')
        return abs(l_count - r_count) + u_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = moves.count('L')
        r_count = moves.count('R')
        u_count = moves.count('_')
        return abs(l_count - r_count) + u_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int furthestDistanceFromOrigin(char* moves) {
    int l_count = 0, r_count = 0, u_count = 0;
    for (int i = 0; moves[i] != '\0'; i++) {
        if (moves[i] == 'L') l_count++;
        else if (moves[i] == 'R') r_count++;
        else u_count++;
    }
    int diff = l_count - r_count;
    if (diff < 0) diff = -diff;
    return diff + u_count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        int lCount = 0, rCount = 0, uCount = 0;
        foreach (char c in moves) {
            if (c == 'L') lCount++;
            else if (c == 'R') rCount++;
            else uCount++;
        }
        return Math.Abs(lCount - rCount) + uCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} moves
 * @return {number}
 */
var furthestDistanceFromOrigin = function(moves) {
    let lCount = 0, rCount = 0, uCount = 0;
    for (let i = 0; i < moves.length; i++) {
        if (moves[i] === 'L') lCount++;
        else if (moves[i] === 'R') rCount++;
        else uCount++;
    }
    return Math.abs(lCount - rCount) + uCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function furthestDistanceFromOrigin(moves: string): number {
    let countL = 0;
    let countR = 0;
    let countUnderscore = 0;
    for (let i = 0; i < moves.length; i++) {
        if (moves[i] === 'L') {
            countL++;
        } else if (moves[i] === 'R') {
            countR++;
        } else {
            countUnderscore++;
        }
    }
    return Math.abs(countL - countR) + countUnderscore;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $moves
     * @return Integer
     */
    function furthestDistanceFromOrigin($moves) {
        $countL = 0;
        $countR = 0;
        $countUnderscore = 0;
        $len = strlen($moves);
        for ($i = 0; $i < $len; $i++) {
            if ($moves[$i] == 'L') {
                $countL++;
            } else if ($moves[$i] == 'R') {
                $countR++;
            } else {
                $countUnderscore++;
            }
        }
        return abs($countL - countR) + $countUnderscore;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func furthestDistanceFromOrigin(_ moves: String) -> Int {
        var countL = 0
        var countR = 0
        var countUnderscore = 0
        for char in moves {
            if char == "L" {
                countL += 1
            } else if char == "R" {
                countR += 1
            } else {
                countUnderscore += 1
            }
        }
        return abs(countL - countR) + countUnderscore
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun furthestDistanceFromOrigin(moves: String): Int {
        var countL = 0
        var countR = 0
        var countUnderscore = 0
        for (char in moves) {
            when (char) {
                'L' -> countL++
                'R' -> countR++
                '_' -> countUnderscore++
            }
        }
        return Math.abs(countL - countR) + countUnderscore
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int furthestDistanceFromOrigin(String moves) {
    int countL = 0;
    int countR = 0;
    int countUnderscore = 0;
    for (int i = 0; i < moves.length; i++) {
      if (moves[i] == 'L') {
        countL++;
      } else if (moves[i] == 'R') {
        countR++;
      } else {
        countUnderscore++;
      }
    }
    return (countL - countR).abs() + countUnderscore;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func furthestDistanceFromOrigin(moves string) int {
    countL := 0
    countR := 0
    countUnderscore := 0
    for _, char := range moves {
        if char == 'L' {
            countL++
        } else if char == 'R' {
            countR++
        } else {
            countUnderscore++
        }
    }
    diff := countL - countR
    if diff < 0 {
        diff = -diff
    }
    return diff + countUnderscore
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} moves
# @return {Integer}
def furthest_distance_from_origin(moves)
  l_count = moves.count('L')
  r_count = moves.count('R')
  underscore_count = moves.count('_')
  (l_count - r_count).abs + underscore_count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def furthestDistanceFromOrigin(moves: String): Int = {
    val lCount = moves.count(_ == 'L')
    val rCount = moves.count(_ == 'R')
    val underscoreCount = moves.count(_ == '_')
    (lCount - rCount).abs + underscoreCount
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn furthest_distance_from_origin(moves: String) -> i32 {
        let (mut l_count, mut r_count, mut underscore_count) = (0, 0, 0);
        for c in moves.chars() {
            match c {
                'L' => l_count += 1,
                'R' => r_count += 1,
                '_' => underscore_count += 1,
                _ => ()
            }
        }
        (l_count - r_count).abs() + underscore_count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (furthest-distance-from-origin moves)
  (-> string? exact-integer?)
  (let-values ([(l r u) 
                (for/fold ([l 0] [r 0] [u 0])
                          ([c (in-string moves)])
                  (cond
                    [(char=? c #\L) (values (+ l 1) r u)]
                    [(char=? c #\R) (values l (+ r 1) u)]
                    [(char=? c #\_) (values l r (+ u 1))]
                    [else (values l r u)]))])
    (+ (abs (- l r)) u)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec furthest_distance_from_origin(Moves :: unicode:unicode_binary()) -> integer().
furthest_distance_from_origin(Moves) ->
  {L, R, U} = lists:foldl(fun(C, {AccL, AccR, AccU}) ->
    case C of
      $L -> {AccL + 1, AccR, AccU};
      $R -> {AccL, AccR + 1, AccU};
      $_ -> {AccL, AccR, AccU + 1};
      _ -> {AccL, AccR, AccU}
    end
  end, {0, 0, 0}, binary_to_list(Moves)),
  abs(L - R) + U.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec furthest_distance_from_origin(moves :: String.t) :: integer
  def furthest_distance_from_origin(moves) do
    {l, r, u} = 
      moves
      |> String.to_charlist()
      |> Enum.reduce({0, 0, 0}, fn 
        ?L, {l, r, u} -> {l + 1, r, u}
        ?R, {l, r, u} -> {l, r + 1, u}
        ?_, {l, r, u} -> {l, r, u + 1}
        _, acc -> acc
      end)
    abs(l - r) + u
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the moves string. We perform a single pass through the string (or multiple passes to count specific characters) to count the occurrences of 'L', 'R', and '_'.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for integer variables to store the counts of the characters, regardless of the input size.
