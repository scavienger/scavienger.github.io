---
layout: post
title: "Robot Return to Origin"
date: 2026-04-05 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/robot-return-to-origin/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool judgeCircle(string moves) {\n      \
        \  int x = 0, y = 0;\n        for (char move : moves) {\n            if (move\
        \ == 'U') y++;\n            else if (move == 'D') y--;\n            else if\
        \ (move == 'L') x--;\n            else if (move == 'R') x++;\n        }\n  \
        \      return x == 0 && y == 0;\n    }\n};"
      java: "class Solution {\n    public boolean judgeCircle(String moves) {\n    \
        \    int x = 0, y = 0;\n        for (char move : moves.toCharArray()) {\n  \
        \          if (move == 'U') y++;\n            else if (move == 'D') y--;\n \
        \           else if (move == 'L') x--;\n            else if (move == 'R') x++;\n\
        \        }\n        return x == 0 && y == 0;\n    }\n}"
      python: "class Solution(object):\n    def judgeCircle(self, moves):\n        \"\
        \"\"\n        :type moves: str\n        :rtype: bool\n        \"\"\"\n     \
        \   return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')"
      python3: "class Solution:\n    def judgeCircle(self, moves: str) -> bool:\n  \
        \      return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')"
      c: "bool judgeCircle(char* moves) {\n    int x = 0, y = 0;\n    for (int i = 0;\
        \ moves[i] != '\\0'; i++) {\n        if (moves[i] == 'U') y++;\n        else\
        \ if (moves[i] == 'D') y--;\n        else if (moves[i] == 'L') x--;\n      \
        \  else if (moves[i] == 'R') x++;\n    }\n    return x == 0 && y == 0;\n}"
      csharp: "public class Solution {\n    public bool JudgeCircle(string moves) {\n\
        \        int x = 0, y = 0;\n        foreach (char move in moves) {\n       \
        \     if (move == 'U') y++;\n            else if (move == 'D') y--;\n      \
        \      else if (move == 'L') x--;\n            else if (move == 'R') x++;\n\
        \        }\n        return x == 0 && y == 0;\n    }\n}"
      javascript: "/**\n * @param {string} moves\n * @return {boolean}\n */\nvar judgeCircle\
        \ = function(moves) {\n    let x = 0, y = 0;\n    for (let move of moves) {\n\
        \        if (move === 'U') y++;\n        else if (move === 'D') y--;\n     \
        \   else if (move === 'L') x--;\n        else if (move === 'R') x++;\n    }\n\
        \    return x === 0 && y === 0;\n};"
      typescript: "function judgeCircle(moves: string): boolean {\n    let x = 0;\n\
        \    let y = 0;\n    for (let i = 0; i < moves.length; i++) {\n        const\
        \ move = moves[i];\n        if (move === 'U') y++;\n        else if (move ===\
        \ 'D') y--;\n        else if (move === 'L') x--;\n        else if (move ===\
        \ 'R') x++;\n    }\n    return x === 0 && y === 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $moves\n     * @return\
        \ Boolean\n     */\n    function judgeCircle($moves) {\n        $x = 0;\n  \
        \      $y = 0;\n        $len = strlen($moves);\n        for ($i = 0; $i < $len;\
        \ $i++) {\n            $move = $moves[$i];\n            if ($move == 'U') $y++;\n\
        \            else if ($move == 'D') $y--;\n            else if ($move == 'L')\
        \ $x--;\n            else if ($move == 'R') $x++;\n        }\n        return\
        \ $x == 0 && $y == 0;\n    }\n}"
      swift: "class Solution {\n    func judgeCircle(_ moves: String) -> Bool {\n  \
        \      var x = 0\n        var y = 0\n        for move in moves {\n         \
        \   if move == \"U\" { y += 1 }\n            else if move == \"D\" { y -= 1\
        \ }\n            else if move == \"L\" { x -= 1 }\n            else if move\
        \ == \"R\" { x += 1 }\n        }\n        return x == 0 && y == 0\n    }\n}"
      kotlin: "class Solution {\n    fun judgeCircle(moves: String): Boolean {\n   \
        \     var x = 0\n        var y = 0\n        for (move in moves) {\n        \
        \    when (move) {\n                'U' -> y++\n                'D' -> y--\n\
        \                'L' -> x--\n                'R' -> x++\n            }\n   \
        \     }\n        return x == 0 && y == 0\n    }\n}"
      dart: "class Solution {\n  bool judgeCircle(String moves) {\n    int x = 0;\n\
        \    int y = 0;\n    for (int i = 0; i < moves.length; i++) {\n      String\
        \ move = moves[i];\n      if (move == 'U') {\n        y++;\n      } else if\
        \ (move == 'D') {\n        y--;\n      } else if (move == 'L') {\n        x--;\n\
        \      } else if (move == 'R') {\n        x++;\n      }\n    }\n    return x\
        \ == 0 && y == 0;\n  }\n}"
      go: "func judgeCircle(moves string) bool {\n    x, y := 0, 0\n    for _, move\
        \ := range moves {\n        if move == 'U' {\n            y++\n        } else\
        \ if move == 'D' {\n            y--\n        } else if move == 'L' {\n     \
        \       x--\n        } else if move == 'R' {\n            x++\n        }\n \
        \   }\n    return x == 0 && y == 0\n}"
      ruby: "# @param {String} moves\n# @return {Boolean}\ndef judge_circle(moves)\n\
        \  moves.count(\"U\") == moves.count(\"D\") && moves.count(\"L\") == moves.count(\"\
        R\")\nend"
      scala: "object Solution {\n    def judgeCircle(moves: String): Boolean = {\n \
        \       moves.count(_ == 'U') == moves.count(_ == 'D') && moves.count(_ == 'L')\
        \ == moves.count(_ == 'R')\n    }\n}"
      rust: "impl Solution {\n    pub fn judge_circle(moves: String) -> bool {\n   \
        \     let (mut x, mut y) = (0, 0);\n        for c in moves.chars() {\n     \
        \       match c {\n                'U' => y += 1,\n                'D' => y\
        \ -= 1,\n                'L' => x -= 1,\n                'R' => x += 1,\n  \
        \              _ => (),\n            }\n        }\n        x == 0 && y == 0\n\
        \    }\n}"
      racket: "(define/contract (judge-circle moves)\n  (-> string? boolean?)\n  (let\
        \ loop ([i 0] [x 0] [y 0])\n    (if (= i (string-length moves))\n        (and\
        \ (= x 0) (= y 0))\n        (case (string-ref moves i)\n          [(#\\U) (loop\
        \ (+ i 1) x (+ y 1))]\n          [(#\\D) (loop (+ i 1) x (- y 1))]\n       \
        \   [(#\\L) (loop (+ i 1) (- x 1) y)]\n          [(#\\R) (loop (+ i 1) (+ x\
        \ 1) y)]))))"
      erlang: "-spec judge_circle(Moves :: unicode:unicode_binary()) -> boolean().\n\
        judge_circle(Moves) ->\n  {X, Y} = lists:foldl(fun(C, {AX, AY}) ->\n    case\
        \ C of\n      $U -> {AX, AY + 1};\n      $D -> {AX, AY - 1};\n      $L -> {AX\
        \ - 1, AY};\n      $R -> {AX + 1, AY}\n    end\n  end, {0, 0}, binary_to_list(Moves)),\n\
        \  X =:= 0 andalso Y =:= 0."
      elixir: "defmodule Solution do\n  @spec judge_circle(moves :: String.t) :: boolean\n\
        \  def judge_circle(moves) do\n    {x, y} = moves\n    |> String.to_charlist()\n\
        \    |> Enum.reduce({0, 0}, fn\n      ?U, {x, y} -> {x, y + 1}\n      ?D, {x,\
        \ y} -> {x, y - 1}\n      ?L, {x, y} -> {x - 1, y}\n      ?R, {x, y} -> {x +\
        \ 1, y}\n    end)\n    x == 0 and y == 0\n  end\nend"
    approach: 'The robot''s movement can be modeled on a 2D coordinate system where
      the starting position is (0, 0). To determine if the robot returns to the origin,
      we track the net displacement in both horizontal (x-axis) and vertical (y-axis)
      directions. We iterate through each character in the input string, incrementing
      or decrementing the respective coordinate: ''U'' increases y, ''D'' decreases
      y, ''R'' increases x, and ''L'' decreases x.


      The key intuition is that for the robot to end up at the origin, every move in
      one direction must be neutralized by a move in the opposite direction. Therefore,
      the robot returns to (0, 0) if and only if the total number of ''U'' moves equals
      the total number of ''D'' moves, and the total number of ''L'' moves equals the
      total number of ''R'' moves. If the final values of both the x and y coordinates
      are zero, the function returns true; otherwise, it returns false.'
    time_complexity: O(N), where N is the length of the input string. The algorithm
      performs a single linear pass through the string to process each move and update
      the coordinates, resulting in a time complexity proportional to the number of
      characters.
    space_complexity: O(1). Only a fixed number of integer variables are used to track
      the robot's coordinates, regardless of the length of the input string, ensuring
      constant space usage.
    elapsed_time: 120.26874494552612
    model: gemini-3-flash-preview
    generated_at: '2026-04-05 01:51:48 '
---

## Problem #657: Robot Return to Origin

**Difficulty:** Easy

**Topics:** String, Simulation

## Problem Description

<p>There is a robot starting at the position <code>(0, 0)</code>, the origin, on a 2D plane. Given a sequence of its moves, judge if this robot <strong>ends up at </strong><code>(0, 0)</code> after it completes its moves.</p>

<p>You are given a string <code>moves</code> that represents the move sequence of the robot where <code>moves[i]</code> represents its <code>i<sup>th</sup></code> move. Valid moves are <code>&#39;R&#39;</code> (right), <code>&#39;L&#39;</code> (left), <code>&#39;U&#39;</code> (up), and <code>&#39;D&#39;</code> (down).</p>

<p>Return <code>true</code><em> if the robot returns to the origin after it finishes all of its moves, or </em><code>false</code><em> otherwise</em>.</p>

<p><strong>Note</strong>: The way that the robot is &quot;facing&quot; is irrelevant. <code>&#39;R&#39;</code> will always make the robot move to the right once, <code>&#39;L&#39;</code> will always make it move left, etc. Also, assume that the magnitude of the robot&#39;s movement is the same for each move.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;UD&quot;
<strong>Output:</strong> true
<strong>Explanation</strong>: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> moves = &quot;LL&quot;
<strong>Output:</strong> false
<strong>Explanation</strong>: The robot moves left twice. It ends up two &quot;moves&quot; to the left of the origin. We return false because it is not at the origin at the end of its moves.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= moves.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>moves</code> only contains the characters <code>&#39;U&#39;</code>, <code>&#39;D&#39;</code>, <code>&#39;L&#39;</code> and <code>&#39;R&#39;</code>.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The robot's movement can be modeled on a 2D coordinate system where the starting position is (0, 0). To determine if the robot returns to the origin, we track the net displacement in both horizontal (x-axis) and vertical (y-axis) directions. We iterate through each character in the input string, incrementing or decrementing the respective coordinate: 'U' increases y, 'D' decreases y, 'R' increases x, and 'L' decreases x.

The key intuition is that for the robot to end up at the origin, every move in one direction must be neutralized by a move in the opposite direction. Therefore, the robot returns to (0, 0) if and only if the total number of 'U' moves equals the total number of 'D' moves, and the total number of 'L' moves equals the total number of 'R' moves. If the final values of both the x and y coordinates are zero, the function returns true; otherwise, it returns false.

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
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (char move : moves) {
            if (move == 'U') y++;
            else if (move == 'D') y--;
            else if (move == 'L') x--;
            else if (move == 'R') x++;
        }
        return x == 0 && y == 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        for (char move : moves.toCharArray()) {
            if (move == 'U') y++;
            else if (move == 'D') y--;
            else if (move == 'L') x--;
            else if (move == 'R') x++;
        }
        return x == 0 && y == 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool judgeCircle(char* moves) {
    int x = 0, y = 0;
    for (int i = 0; moves[i] != '\0'; i++) {
        if (moves[i] == 'U') y++;
        else if (moves[i] == 'D') y--;
        else if (moves[i] == 'L') x--;
        else if (moves[i] == 'R') x++;
    }
    return x == 0 && y == 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool JudgeCircle(string moves) {
        int x = 0, y = 0;
        foreach (char move in moves) {
            if (move == 'U') y++;
            else if (move == 'D') y--;
            else if (move == 'L') x--;
            else if (move == 'R') x++;
        }
        return x == 0 && y == 0;
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
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let x = 0, y = 0;
    for (let move of moves) {
        if (move === 'U') y++;
        else if (move === 'D') y--;
        else if (move === 'L') x--;
        else if (move === 'R') x++;
    }
    return x === 0 && y === 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function judgeCircle(moves: string): boolean {
    let x = 0;
    let y = 0;
    for (let i = 0; i < moves.length; i++) {
        const move = moves[i];
        if (move === 'U') y++;
        else if (move === 'D') y--;
        else if (move === 'L') x--;
        else if (move === 'R') x++;
    }
    return x === 0 && y === 0;
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
     * @return Boolean
     */
    function judgeCircle($moves) {
        $x = 0;
        $y = 0;
        $len = strlen($moves);
        for ($i = 0; $i < $len; $i++) {
            $move = $moves[$i];
            if ($move == 'U') $y++;
            else if ($move == 'D') $y--;
            else if ($move == 'L') $x--;
            else if ($move == 'R') $x++;
        }
        return $x == 0 && $y == 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func judgeCircle(_ moves: String) -> Bool {
        var x = 0
        var y = 0
        for move in moves {
            if move == "U" { y += 1 }
            else if move == "D" { y -= 1 }
            else if move == "L" { x -= 1 }
            else if move == "R" { x += 1 }
        }
        return x == 0 && y == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun judgeCircle(moves: String): Boolean {
        var x = 0
        var y = 0
        for (move in moves) {
            when (move) {
                'U' -> y++
                'D' -> y--
                'L' -> x--
                'R' -> x++
            }
        }
        return x == 0 && y == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool judgeCircle(String moves) {
    int x = 0;
    int y = 0;
    for (int i = 0; i < moves.length; i++) {
      String move = moves[i];
      if (move == 'U') {
        y++;
      } else if (move == 'D') {
        y--;
      } else if (move == 'L') {
        x--;
      } else if (move == 'R') {
        x++;
      }
    }
    return x == 0 && y == 0;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func judgeCircle(moves string) bool {
    x, y := 0, 0
    for _, move := range moves {
        if move == 'U' {
            y++
        } else if move == 'D' {
            y--
        } else if move == 'L' {
            x--
        } else if move == 'R' {
            x++
        }
    }
    return x == 0 && y == 0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
  moves.count("U") == moves.count("D") && moves.count("L") == moves.count("R")
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def judgeCircle(moves: String): Boolean = {
        moves.count(_ == 'U') == moves.count(_ == 'D') && moves.count(_ == 'L') == moves.count(_ == 'R')
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        let (mut x, mut y) = (0, 0);
        for c in moves.chars() {
            match c {
                'U' => y += 1,
                'D' => y -= 1,
                'L' => x -= 1,
                'R' => x += 1,
                _ => (),
            }
        }
        x == 0 && y == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (judge-circle moves)
  (-> string? boolean?)
  (let loop ([i 0] [x 0] [y 0])
    (if (= i (string-length moves))
        (and (= x 0) (= y 0))
        (case (string-ref moves i)
          [(#\U) (loop (+ i 1) x (+ y 1))]
          [(#\D) (loop (+ i 1) x (- y 1))]
          [(#\L) (loop (+ i 1) (- x 1) y)]
          [(#\R) (loop (+ i 1) (+ x 1) y)]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec judge_circle(Moves :: unicode:unicode_binary()) -> boolean().
judge_circle(Moves) ->
  {X, Y} = lists:foldl(fun(C, {AX, AY}) ->
    case C of
      $U -> {AX, AY + 1};
      $D -> {AX, AY - 1};
      $L -> {AX - 1, AY};
      $R -> {AX + 1, AY}
    end
  end, {0, 0}, binary_to_list(Moves)),
  X =:= 0 andalso Y =:= 0.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec judge_circle(moves :: String.t) :: boolean
  def judge_circle(moves) do
    {x, y} = moves
    |> String.to_charlist()
    |> Enum.reduce({0, 0}, fn
      ?U, {x, y} -> {x, y + 1}
      ?D, {x, y} -> {x, y - 1}
      ?L, {x, y} -> {x - 1, y}
      ?R, {x, y} -> {x + 1, y}
    end)
    x == 0 and y == 0
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the input string. The algorithm performs a single linear pass through the string to process each move and update the coordinates, resulting in a time complexity proportional to the number of characters.
- **Space Complexity:** O(1). Only a fixed number of integer variables are used to track the robot's coordinates, regardless of the length of the input string, ensuring constant space usage.
