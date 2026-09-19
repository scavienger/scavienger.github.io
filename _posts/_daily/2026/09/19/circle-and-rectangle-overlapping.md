---
layout: post
title: "Circle and Rectangle Overlapping"
date: 2026-09-19 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Geometry"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/circle-and-rectangle-overlapping/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool checkOverlap(int radius, int xCenter,\
        \ int yCenter, int x1, int y1, int x2, int y2) {\n        int nearestX = (xCenter\
        \ < x1) ? x1 : (xCenter > x2 ? x2 : xCenter);\n        int nearestY = (yCenter\
        \ < y1) ? y1 : (yCenter > y2 ? y2 : yCenter);\n\n        int dx = nearestX -\
        \ xCenter;\n        int dy = nearestY - yCenter;\n\n        return (dx * dx\
        \ + dy * dy) <= (radius * radius);\n    }\n};"
      java: "class Solution {\n    public boolean checkOverlap(int radius, int xCenter,\
        \ int yCenter, int x1, int y1, int x2, int y2) {\n        int nearestX = Math.max(x1,\
        \ Math.min(xCenter, x2));\n        int nearestY = Math.max(y1, Math.min(yCenter,\
        \ y2));\n\n        int dx = nearestX - xCenter;\n        int dy = nearestY -\
        \ yCenter;\n\n        return (dx * dx + dy * dy) <= (radius * radius);\n   \
        \ }\n}"
      python: "class Solution(object):\n    def checkOverlap(self, radius, xCenter,\
        \ yCenter, x1, y1, x2, y2):\n        \"\"\"\n        :type radius: int\n   \
        \     :type xCenter: int\n        :type yCenter: int\n        :type x1: int\n\
        \        :type y1: int\n        :type x2: int\n        :type y2: int\n     \
        \   :rtype: bool\n        \"\"\"\n        nearest_x = max(x1, min(xCenter, x2))\n\
        \        nearest_y = max(y1, min(yCenter, y2))\n\n        dx = nearest_x - xCenter\n\
        \        dy = nearest_y - yCenter\n\n        return (dx * dx + dy * dy) <= (radius\
        \ * radius)"
      python3: "class Solution:\n    def checkOverlap(self, radius: int, xCenter: int,\
        \ yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:\n        nearest_x\
        \ = max(x1, min(xCenter, x2))\n        nearest_y = max(y1, min(yCenter, y2))\n\
        \n        dx = nearest_x - xCenter\n        dy = nearest_y - yCenter\n\n   \
        \     return (dx * dx + dy * dy) <= (radius * radius)"
      c: "bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int\
        \ x2, int y2) {\n    int nearestX = (xCenter < x1) ? x1 : (xCenter > x2 ? x2\
        \ : xCenter);\n    int nearestY = (yCenter < y1) ? y1 : (yCenter > y2 ? y2 :\
        \ yCenter);\n\n    int dx = nearestX - xCenter;\n    int dy = nearestY - yCenter;\n\
        \n    return (dx * dx + dy * dy) <= (radius * radius);\n}"
      csharp: "public class Solution {\n    public bool CheckOverlap(int radius, int\
        \ xCenter, int yCenter, int x1, int y1, int x2, int y2) {\n        int closestX\
        \ = System.Math.Max(x1, System.Math.Min(xCenter, x2));\n        int closestY\
        \ = System.Math.Max(y1, System.Math.Min(yCenter, y2));\n        int dx = closestX\
        \ - xCenter;\n        int dy = closestY - yCenter;\n        return (dx * dx\
        \ + dy * dy) <= (radius * radius);\n    }\n}"
      javascript: "/**\n * @param {number} radius\n * @param {number} xCenter\n * @param\
        \ {number} yCenter\n * @param {number} x1\n * @param {number} y1\n * @param\
        \ {number} x2\n * @param {number} y2\n * @return {boolean}\n */\nvar checkOverlap\
        \ = function(radius, xCenter, yCenter, x1, y1, x2, y2) {\n    const closestX\
        \ = Math.max(x1, Math.min(xCenter, x2));\n    const closestY = Math.max(y1,\
        \ Math.min(yCenter, y2));\n    const dx = closestX - xCenter;\n    const dy\
        \ = closestY - yCenter;\n    return (dx * dx + dy * dy) <= (radius * radius);\n\
        };"
      typescript: "function checkOverlap(radius: number, xCenter: number, yCenter: number,\
        \ x1: number, y1: number, x2: number, y2: number): boolean {\n    const closestX:\
        \ number = Math.max(x1, Math.min(xCenter, x2));\n    const closestY: number\
        \ = Math.max(y1, Math.min(yCenter, y2));\n    const dx: number = closestX -\
        \ xCenter;\n    const dy: number = closestY - yCenter;\n    return (dx * dx\
        \ + dy * dy) <= (radius * radius);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $radius\n     * @param\
        \ Integer $xCenter\n     * @param Integer $yCenter\n     * @param Integer $x1\n\
        \     * @param Integer $y1\n     * @param Integer $x2\n     * @param Integer\
        \ $y2\n     * @return Boolean\n     */\n    function checkOverlap($radius, $xCenter,\
        \ $yCenter, $x1, $y1, $x2, $y2) {\n        $closestX = max($x1, min($xCenter,\
        \ $x2));\n        $closestY = max($y1, min($yCenter, $y2));\n        $dx = $closestX\
        \ - $xCenter;\n        $dy = $closestY - $yCenter;\n        return ($dx * $dx\
        \ + $dy * $dy) <= ($radius * $radius);\n    }\n}"
      swift: "class Solution {\n    func checkOverlap(_ radius: Int, _ xCenter: Int,\
        \ _ yCenter: Int, _ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Bool {\n  \
        \      let closestX = max(x1, min(xCenter, x2))\n        let closestY = max(y1,\
        \ min(yCenter, y2))\n        let dx = closestX - xCenter\n        let dy = closestY\
        \ - yCenter\n        return (dx * dx + dy * dy) <= (radius * radius)\n    }\n\
        }"
      kotlin: "class Solution {\n    fun checkOverlap(radius: Int, xCenter: Int, yCenter:\
        \ Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean {\n        val closestX\
        \ = if (xCenter < x1) x1 else if (xCenter > x2) x2 else xCenter\n        val\
        \ closestY = if (yCenter < y1) y1 else if (yCenter > y2) y2 else yCenter\n \
        \       val dx = xCenter - closestX\n        val dy = yCenter - closestY\n \
        \       return dx * dx + dy * dy <= radius * radius\n    }\n}"
      dart: "class Solution {\n  bool checkOverlap(int radius, int xCenter, int yCenter,\
        \ int x1, int y1, int x2, int y2) {\n    int closestX = (xCenter < x1) ? x1\
        \ : (xCenter > x2 ? x2 : xCenter);\n    int closestY = (yCenter < y1) ? y1 :\
        \ (yCenter > y2 ? y2 : yCenter);\n    int dx = xCenter - closestX;\n    int\
        \ dy = yCenter - closestY;\n    return dx * dx + dy * dy <= radius * radius;\n\
        \  }\n}"
      go: "func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2\
        \ int, y2 int) bool {\n    closestX := xCenter\n    if xCenter < x1 {\n    \
        \    closestX = x1\n    } else if xCenter > x2 {\n        closestX = x2\n  \
        \  }\n\n    closestY := yCenter\n    if yCenter < y1 {\n        closestY = y1\n\
        \    } else if yCenter > y2 {\n        closestY = y2\n    }\n\n    dx := xCenter\
        \ - closestX\n    dy := yCenter - closestY\n    return dx*dx + dy*dy <= radius*radius\n\
        }"
      ruby: "# @param {Integer} radius\n# @param {Integer} x_center\n# @param {Integer}\
        \ y_center\n# @param {Integer} x1\n# @param {Integer} y1\n# @param {Integer}\
        \ x2\n# @param {Integer} y2\n# @return {Boolean}\ndef check_overlap(radius,\
        \ x_center, y_center, x1, y1, x2, y2)\n    closest_x = x_center.clamp(x1, x2)\n\
        \    closest_y = y_center.clamp(y1, y2)\n    dx = x_center - closest_x\n   \
        \ dy = y_center - closest_y\n    dx * dx + dy * dy <= radius * radius\nend"
      scala: "object Solution {\n    def checkOverlap(radius: Int, xCenter: Int, yCenter:\
        \ Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean = {\n        val closestX\
        \ = if (xCenter < x1) x1 else if (xCenter > x2) x2 else xCenter\n        val\
        \ closestY = if (yCenter < y1) y1 else if (yCenter > y2) y2 else yCenter\n \
        \       val dx = xCenter - closestX\n        val dy = yCenter - closestY\n \
        \       dx * dx + dy * dy <= radius * radius\n    }\n}"
      rust: "impl Solution {\n    pub fn check_overlap(radius: i32, x_center: i32, y_center:\
        \ i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {\n        let closest_x\
        \ = if x_center < x1 {\n            x1\n        } else if x_center > x2 {\n\
        \            x2\n        } else {\n            x_center\n        };\n\n    \
        \    let closest_y = if y_center < y1 {\n            y1\n        } else if y_center\
        \ > y2 {\n            y2\n        } else {\n            y_center\n        };\n\
        \n        let dx = closest_x - x_center;\n        let dy = closest_y - y_center;\n\
        \n        (dx * dx + dy * dy) <= (radius * radius)\n    }\n}"
      racket: "(define/contract (check-overlap radius xCenter yCenter x1 y1 x2 y2)\n\
        \  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?\
        \ exact-integer? exact-integer? boolean?)\n  (let* ([closest-x (max x1 (min\
        \ xCenter x2))]\n         [closest-y (max y1 (min yCenter y2))]\n         [dx\
        \ (- closest-x xCenter)]\n         [dy (- closest-y yCenter)])\n    (<= (+ (*\
        \ dx dx) (* dy dy)) (* radius radius))))"
      erlang: "-spec check_overlap(Radius :: integer(), XCenter :: integer(), YCenter\
        \ :: integer(), X1 :: integer(), Y1 :: integer(), X2 :: integer(), Y2 :: integer())\
        \ -> boolean().\ncheck_overlap(Radius, XCenter, YCenter, X1, Y1, X2, Y2) ->\n\
        \  ClosestX = erlang:max(X1, erlang:min(XCenter, X2)),\n  ClosestY = erlang:max(Y1,\
        \ erlang:min(YCenter, Y2)),\n  DX = ClosestX - XCenter,\n  DY = ClosestY - YCenter,\n\
        \  (DX * DX + DY * DY) =< (Radius * Radius)."
      elixir: "defmodule Solution do\n  @spec check_overlap(radius :: integer, x_center\
        \ :: integer, y_center :: integer, x1 :: integer, y1 :: integer, x2 :: integer,\
        \ y2 :: integer) :: boolean\n  def check_overlap(radius, x_center, y_center,\
        \ x1, y1, x2, y2) do\n    closest_x = max(x1, min(x_center, x2))\n    closest_y\
        \ = max(y1, min(y_center, y2))\n\n    dx = closest_x - x_center\n    dy = closest_y\
        \ - y_center\n\n    (dx * dx + dy * dy) <= (radius * radius)\n  end\nend"
    approach: 'The algorithm works by finding the point on or within the axis-aligned
      rectangle that is closest to the circle''s center $(xCenter, yCenter)$. For an
      axis-aligned rectangle defined by boundaries $[x1, x2]$ and $[y1, y2]$, the closest
      $x$-coordinate is the circle''s $x$-center clamped to the interval $[x1, x2]$,
      and the closest $y$-coordinate is the circle''s $y$-center clamped to $[y1, y2]$.
      Clamping effectively projects the circle''s center onto the nearest boundary of
      the rectangle or leaves it unchanged if the center is already inside.


      Once this nearest point $(nearestX, nearestY)$ is determined, the Euclidean distance
      between this point and the circle''s center is calculated. If the squared distance
      $(nearestX - xCenter)^2 + (nearestY - yCenter)^2$ is less than or equal to the
      square of the circle''s radius $radius^2$, it means the circle and the rectangle
      share at least one point, confirming an overlap. This method is efficient and
      robust, as it handles all configurations: circle inside rectangle, rectangle inside
      circle, or partial intersection.'
    time_complexity: O(1). The solution performs a fixed number of comparisons and arithmetic
      operations (clamping and distance calculation) regardless of the input values.
    space_complexity: O(1). Only a few scalar integer variables are used to store the
      nearest point and distance, requiring constant additional space.
    elapsed_time: 105.63251423835754
    model: gemini-3-flash-preview
    generated_at: '2026-09-19 02:32:09 '
---

## Problem #1401: Circle and Rectangle Overlapping

**Difficulty:** Medium

**Topics:** Math, Geometry

## Problem Description

<p>You are given a circle represented as <code>(radius, xCenter, yCenter)</code> and an axis-aligned rectangle represented as <code>(x1, y1, x2, y2)</code>, where <code>(x1, y1)</code> are the coordinates of the bottom-left corner, and <code>(x2, y2)</code> are the coordinates of the top-right corner of the rectangle.</p>

<p>Return <code>true</code><em> if the circle and rectangle are overlapped otherwise return </em><code>false</code>. In other words, check if there is <strong>any</strong> point <code>(x<sub>i</sub>, y<sub>i</sub>)</code> that belongs to the circle and the rectangle at the same time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png" style="width: 258px; height: 167px;" />
<pre>
<strong>Input:</strong> radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> Circle and rectangle share the point (1,0).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png" style="width: 150px; height: 135px;" />
<pre>
<strong>Input:</strong> radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= radius &lt;= 2000</code></li>
	<li><code>-10<sup>4</sup> &lt;= xCenter, yCenter &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= x1 &lt; x2 &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= y1 &lt; y2 &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Locate the closest point of the square to the circle, you can then find the distance from this point to the center of the circle and check if this is less than or equal to the radius.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm works by finding the point on or within the axis-aligned rectangle that is closest to the circle's center $(xCenter, yCenter)$. For an axis-aligned rectangle defined by boundaries $[x1, x2]$ and $[y1, y2]$, the closest $x$-coordinate is the circle's $x$-center clamped to the interval $[x1, x2]$, and the closest $y$-coordinate is the circle's $y$-center clamped to $[y1, y2]$. Clamping effectively projects the circle's center onto the nearest boundary of the rectangle or leaves it unchanged if the center is already inside.

Once this nearest point $(nearestX, nearestY)$ is determined, the Euclidean distance between this point and the circle's center is calculated. If the squared distance $(nearestX - xCenter)^2 + (nearestY - yCenter)^2$ is less than or equal to the square of the circle's radius $radius^2$, it means the circle and the rectangle share at least one point, confirming an overlap. This method is efficient and robust, as it handles all configurations: circle inside rectangle, rectangle inside circle, or partial intersection.

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
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int nearestX = (xCenter < x1) ? x1 : (xCenter > x2 ? x2 : xCenter);
        int nearestY = (yCenter < y1) ? y1 : (yCenter > y2 ? y2 : yCenter);

        int dx = nearestX - xCenter;
        int dy = nearestY - yCenter;

        return (dx * dx + dy * dy) <= (radius * radius);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int nearestX = Math.max(x1, Math.min(xCenter, x2));
        int nearestY = Math.max(y1, Math.min(yCenter, y2));

        int dx = nearestX - xCenter;
        int dy = nearestY - yCenter;

        return (dx * dx + dy * dy) <= (radius * radius);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))

        dx = nearest_x - xCenter
        dy = nearest_y - yCenter

        return (dx * dx + dy * dy) <= (radius * radius)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))

        dx = nearest_x - xCenter
        dy = nearest_y - yCenter

        return (dx * dx + dy * dy) <= (radius * radius)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
    int nearestX = (xCenter < x1) ? x1 : (xCenter > x2 ? x2 : xCenter);
    int nearestY = (yCenter < y1) ? y1 : (yCenter > y2 ? y2 : yCenter);

    int dx = nearestX - xCenter;
    int dy = nearestY - yCenter;

    return (dx * dx + dy * dy) <= (radius * radius);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CheckOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int closestX = System.Math.Max(x1, System.Math.Min(xCenter, x2));
        int closestY = System.Math.Max(y1, System.Math.Min(yCenter, y2));
        int dx = closestX - xCenter;
        int dy = closestY - yCenter;
        return (dx * dx + dy * dy) <= (radius * radius);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} radius
 * @param {number} xCenter
 * @param {number} yCenter
 * @param {number} x1
 * @param {number} y1
 * @param {number} x2
 * @param {number} y2
 * @return {boolean}
 */
var checkOverlap = function(radius, xCenter, yCenter, x1, y1, x2, y2) {
    const closestX = Math.max(x1, Math.min(xCenter, x2));
    const closestY = Math.max(y1, Math.min(yCenter, y2));
    const dx = closestX - xCenter;
    const dy = closestY - yCenter;
    return (dx * dx + dy * dy) <= (radius * radius);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function checkOverlap(radius: number, xCenter: number, yCenter: number, x1: number, y1: number, x2: number, y2: number): boolean {
    const closestX: number = Math.max(x1, Math.min(xCenter, x2));
    const closestY: number = Math.max(y1, Math.min(yCenter, y2));
    const dx: number = closestX - xCenter;
    const dy: number = closestY - yCenter;
    return (dx * dx + dy * dy) <= (radius * radius);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $radius
     * @param Integer $xCenter
     * @param Integer $yCenter
     * @param Integer $x1
     * @param Integer $y1
     * @param Integer $x2
     * @param Integer $y2
     * @return Boolean
     */
    function checkOverlap($radius, $xCenter, $yCenter, $x1, $y1, $x2, $y2) {
        $closestX = max($x1, min($xCenter, $x2));
        $closestY = max($y1, min($yCenter, $y2));
        $dx = $closestX - $xCenter;
        $dy = $closestY - $yCenter;
        return ($dx * $dx + $dy * $dy) <= ($radius * $radius);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func checkOverlap(_ radius: Int, _ xCenter: Int, _ yCenter: Int, _ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Bool {
        let closestX = max(x1, min(xCenter, x2))
        let closestY = max(y1, min(yCenter, y2))
        let dx = closestX - xCenter
        let dy = closestY - yCenter
        return (dx * dx + dy * dy) <= (radius * radius)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean {
        val closestX = if (xCenter < x1) x1 else if (xCenter > x2) x2 else xCenter
        val closestY = if (yCenter < y1) y1 else if (yCenter > y2) y2 else yCenter
        val dx = xCenter - closestX
        val dy = yCenter - closestY
        return dx * dx + dy * dy <= radius * radius
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
    int closestX = (xCenter < x1) ? x1 : (xCenter > x2 ? x2 : xCenter);
    int closestY = (yCenter < y1) ? y1 : (yCenter > y2 ? y2 : yCenter);
    int dx = xCenter - closestX;
    int dy = yCenter - closestY;
    return dx * dx + dy * dy <= radius * radius;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
    closestX := xCenter
    if xCenter < x1 {
        closestX = x1
    } else if xCenter > x2 {
        closestX = x2
    }

    closestY := yCenter
    if yCenter < y1 {
        closestY = y1
    } else if yCenter > y2 {
        closestY = y2
    }

    dx := xCenter - closestX
    dy := yCenter - closestY
    return dx*dx + dy*dy <= radius*radius
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} radius
# @param {Integer} x_center
# @param {Integer} y_center
# @param {Integer} x1
# @param {Integer} y1
# @param {Integer} x2
# @param {Integer} y2
# @return {Boolean}
def check_overlap(radius, x_center, y_center, x1, y1, x2, y2)
    closest_x = x_center.clamp(x1, x2)
    closest_y = y_center.clamp(y1, y2)
    dx = x_center - closest_x
    dy = y_center - closest_y
    dx * dx + dy * dy <= radius * radius
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean = {
        val closestX = if (xCenter < x1) x1 else if (xCenter > x2) x2 else xCenter
        val closestY = if (yCenter < y1) y1 else if (yCenter > y2) y2 else yCenter
        val dx = xCenter - closestX
        val dy = yCenter - closestY
        dx * dx + dy * dy <= radius * radius
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn check_overlap(radius: i32, x_center: i32, y_center: i32, x1: i32, y1: i32, x2: i32, y2: i32) -> bool {
        let closest_x = if x_center < x1 {
            x1
        } else if x_center > x2 {
            x2
        } else {
            x_center
        };

        let closest_y = if y_center < y1 {
            y1
        } else if y_center > y2 {
            y2
        } else {
            y_center
        };

        let dx = closest_x - x_center;
        let dy = closest_y - y_center;

        (dx * dx + dy * dy) <= (radius * radius)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (check-overlap radius xCenter yCenter x1 y1 x2 y2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? boolean?)
  (let* ([closest-x (max x1 (min xCenter x2))]
         [closest-y (max y1 (min yCenter y2))]
         [dx (- closest-x xCenter)]
         [dy (- closest-y yCenter)])
    (<= (+ (* dx dx) (* dy dy)) (* radius radius))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec check_overlap(Radius :: integer(), XCenter :: integer(), YCenter :: integer(), X1 :: integer(), Y1 :: integer(), X2 :: integer(), Y2 :: integer()) -> boolean().
check_overlap(Radius, XCenter, YCenter, X1, Y1, X2, Y2) ->
  ClosestX = erlang:max(X1, erlang:min(XCenter, X2)),
  ClosestY = erlang:max(Y1, erlang:min(YCenter, Y2)),
  DX = ClosestX - XCenter,
  DY = ClosestY - YCenter,
  (DX * DX + DY * DY) =< (Radius * Radius).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec check_overlap(radius :: integer, x_center :: integer, y_center :: integer, x1 :: integer, y1 :: integer, x2 :: integer, y2 :: integer) :: boolean
  def check_overlap(radius, x_center, y_center, x1, y1, x2, y2) do
    closest_x = max(x1, min(x_center, x2))
    closest_y = max(y1, min(y_center, y2))

    dx = closest_x - x_center
    dy = closest_y - y_center

    (dx * dx + dy * dy) <= (radius * radius)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The solution performs a fixed number of comparisons and arithmetic operations (clamping and distance calculation) regardless of the input values.
- **Space Complexity:** O(1). Only a few scalar integer variables are used to store the nearest point and distance, requiring constant additional space.
