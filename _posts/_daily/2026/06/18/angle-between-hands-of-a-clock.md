---
layout: post
title: "Angle Between Hands of a Clock"
date: 2026-06-18 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/angle-between-hands-of-a-clock/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    double angleClock(int hour, int minutes)\
        \ {\n        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;\n      \
        \  double minuteAngle = minutes * 6.0;\n        double diff = hourAngle - minuteAngle;\n\
        \        if (diff < 0) diff = -diff;\n        return diff > 180.0 ? 360.0 -\
        \ diff : diff;\n    }\n};"
      java: "class Solution {\n    public double angleClock(int hour, int minutes) {\n\
        \        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;\n        double\
        \ minuteAngle = minutes * 6.0;\n        double diff = Math.abs(hourAngle - minuteAngle);\n\
        \        if (diff > 180.0) {\n            diff = 360.0 - diff;\n        }\n\
        \        return diff;\n    }\n}"
      python: "class Solution(object):\n    def angleClock(self, hour, minutes):\n \
        \       \"\"\"\n        :type hour: int\n        :type minutes: int\n      \
        \  :rtype: float\n        \"\"\"\n        hour_angle = (hour % 12) * 30.0 +\
        \ minutes * 0.5\n        minute_angle = minutes * 6.0\n        diff = abs(hour_angle\
        \ - minute_angle)\n        return min(diff, 360.0 - diff)"
      python3: "class Solution:\n    def angleClock(self, hour: int, minutes: int) ->\
        \ float:\n        hour_angle = (hour % 12) * 30.0 + minutes * 0.5\n        minute_angle\
        \ = minutes * 6.0\n        diff = abs(hour_angle - minute_angle)\n        return\
        \ min(diff, 360.0 - diff)"
      c: "double angleClock(int hour, int minutes) {\n    double hourAngle = (hour %\
        \ 12) * 30.0 + minutes * 0.5;\n    double minuteAngle = minutes * 6.0;\n   \
        \ double diff = hourAngle - minuteAngle;\n    if (diff < 0) diff = -diff;\n\
        \    if (diff > 180.0) {\n        diff = 360.0 - diff;\n    }\n    return diff;\n\
        }"
      csharp: "using System;\n\npublic class Solution {\n    public double AngleClock(int\
        \ hour, int minutes) {\n        double minuteAngle = minutes * 6.0;\n      \
        \  double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;\n        double diff\
        \ = Math.Abs(hourAngle - minuteAngle);\n        return Math.Min(diff, 360.0\
        \ - diff);\n    }\n}"
      javascript: "/**\n * @param {number} hour\n * @param {number} minutes\n * @return\
        \ {number}\n */\nvar angleClock = function(hour, minutes) {\n    let minuteAngle\
        \ = minutes * 6;\n    let hourAngle = (hour % 12) * 30 + minutes * 0.5;\n  \
        \  let diff = Math.abs(hourAngle - minuteAngle);\n    return Math.min(diff,\
        \ 360 - diff);\n};"
      typescript: "function angleClock(hour: number, minutes: number): number {\n  \
        \  const minuteAngle: number = minutes * 6;\n    const hourAngle: number = (hour\
        \ % 12) * 30 + minutes * 0.5;\n    const diff: number = Math.abs(hourAngle -\
        \ minuteAngle);\n    return Math.min(diff, 360 - diff);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $hour\n     * @param\
        \ Integer $minutes\n     * @return Float\n     */\n    function angleClock($hour,\
        \ $minutes) {\n        $minuteAngle = $minutes * 6.0;\n        $hourAngle =\
        \ ($hour % 12) * 30.0 + $minutes * 0.5;\n        $diff = abs($hourAngle - $minuteAngle);\n\
        \        return min($diff, 360.0 - $diff);\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func angleClock(_ hour: Int,\
        \ _ minutes: Int) -> Double {\n        let minuteAngle = Double(minutes) * 6.0\n\
        \        let hourAngle = Double(hour % 12) * 30.0 + Double(minutes) * 0.5\n\
        \        let diff = abs(hourAngle - minuteAngle)\n        return min(diff, 360.0\
        \ - diff)\n    }\n}"
      kotlin: "class Solution {\n    fun angleClock(hour: Int, minutes: Int): Double\
        \ {\n        val minuteAngle = minutes * 6.0\n        val hourAngle = (hour\
        \ % 12) * 30.0 + (minutes * 0.5)\n        val diff = Math.abs(hourAngle - minuteAngle)\n\
        \        return if (diff > 180.0) 360.0 - diff else diff\n    }\n}"
      dart: "class Solution {\n  double angleClock(int hour, int minutes) {\n    double\
        \ minuteAngle = minutes * 6.0;\n    double hourAngle = (hour % 12) * 30.0 +\
        \ (minutes * 0.5);\n    double diff = (hourAngle - minuteAngle).abs();\n   \
        \ return diff > 180.0 ? 360.0 - diff : diff;\n  }\n}"
      go: "import \"math\"\n\nfunc angleClock(hour int, minutes int) float64 {\n   \
        \ minuteAngle := float64(minutes) * 6.0\n    hourAngle := float64(hour%12)*30.0\
        \ + float64(minutes)*0.5\n    diff := math.Abs(hourAngle - minuteAngle)\n  \
        \  if diff > 180.0 {\n        return 360.0 - diff\n    }\n    return diff\n}"
      ruby: "# @param {Integer} hour\n# @param {Integer} minutes\n# @return {Float}\n\
        def angle_clock(hour, minutes)\n    minute_angle = minutes * 6.0\n    hour_angle\
        \ = (hour % 12) * 30.0 + (minutes * 0.5)\n    diff = (hour_angle - minute_angle).abs\n\
        \    diff > 180.0 ? 360.0 - diff : diff\nend"
      scala: "object Solution {\n    def angleClock(hour: Int, minutes: Int): Double\
        \ = {\n        val minuteAngle: Double = minutes * 6.0\n        val hourAngle:\
        \ Double = (hour % 12) * 30.0 + (minutes * 0.5)\n        val diff: Double =\
        \ Math.abs(hourAngle - minuteAngle)\n        if (diff > 180.0) 360.0 - diff\
        \ else diff\n    }\n}"
      rust: "impl Solution {\n    pub fn angle_clock(hour: i32, minutes: i32) -> f64\
        \ {\n        let minute_angle = (minutes as f64) * 6.0;\n        let hour_angle\
        \ = ((hour % 12) as f64 * 30.0) + ((minutes as f64) * 0.5);\n        let diff\
        \ = (hour_angle - minute_angle).abs();\n        if diff > 180.0 {\n        \
        \    360.0 - diff\n        } else {\n            diff\n        }\n    }\n}"
      racket: "(define/contract (angle-clock hour minutes)\n  (-> exact-integer? exact-integer?\
        \ flonum?)\n  (let* ([minute-angle (* (exact->inexact minutes) 6.0)]\n     \
        \    [hour-angle (+ (* (modulo hour 12) 30.0) (* (exact->inexact minutes) 0.5))]\n\
        \         [diff (abs (- hour-angle minute-angle))])\n    (if (> diff 180.0)\n\
        \        (- 360.0 diff)\n        diff)))"
      erlang: "-spec angle_clock(Hour :: integer(), Minutes :: integer()) -> float().\n\
        angle_clock(Hour, Minutes) ->\n  MinuteAngle = Minutes * 6.0,\n  HourAngle =\
        \ (Hour rem 12) * 30.0 + Minutes * 0.5,\n  Diff = abs(HourAngle - MinuteAngle),\n\
        \  if\n    Diff > 180.0 -> 360.0 - Diff;\n    true -> Diff\n  end."
      elixir: "defmodule Solution do\n  @spec angle_clock(hour :: integer, minutes ::\
        \ integer) :: float\n  def angle_clock(hour, minutes) do\n    minute_angle =\
        \ minutes * 6.0\n    hour_angle = rem(hour, 12) * 30.0 + minutes * 0.5\n   \
        \ diff = abs(hour_angle - minute_angle)\n    if diff > 180.0 do\n      360.0\
        \ - diff\n    else\n      diff\n    end\n  end\nend"
    approach: 'The algorithm calculates the precise angular position of the hour hand
      and the minute hand relative to the 12:00 position (0 degrees). The minute hand
      rotates 360 degrees in 60 minutes, which equates to 6 degrees per minute. The
      hour hand rotates 360 degrees in 12 hours, meaning 30 degrees per hour, but it
      also shifts slightly as minutes pass at a rate of 0.5 degrees per minute (30 degrees
      divided by 60 minutes).


      To find the final result, we compute the absolute difference between the hour
      hand''s angle and the minute hand''s angle. Since we need the smaller angle between
      the two hands, we check if the calculated difference is greater than 180 degrees.
      If it is, we return the difference subtracted from 360 degrees, ensuring the result
      is always the interior angle between the hands.'
    time_complexity: O(1). The solution performs a constant number of basic arithmetic
      operations (multiplication, addition, and subtraction) regardless of the input
      values.
    space_complexity: O(1). The algorithm only utilizes a few primitive double-precision
      floating-point variables to store the hand positions and their difference, requiring
      no additional space that scales with input size.
    elapsed_time: 59.342326402664185
    model: gemini-3-flash-preview
    generated_at: '2026-06-18 02:51:12 '
---

## Problem #1344: Angle Between Hands of a Clock

**Difficulty:** Medium

**Topics:** Math

## Problem Description

<p>Given two numbers, <code>hour</code> and <code>minutes</code>, return <em>the smaller angle (in degrees) formed between the </em><code>hour</code><em> and the </em><code>minute</code><em> hand</em>.</p>

<p>Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted as correct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_1_1673.png" style="width: 300px; height: 296px;" />
<pre>
<strong>Input:</strong> hour = 12, minutes = 30
<strong>Output:</strong> 165
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_2_1673.png" style="width: 300px; height: 301px;" />
<pre>
<strong>Input:</strong> hour = 3, minutes = 30
<strong>Output:</strong> 75
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/26/sample_3_1673.png" style="width: 300px; height: 301px;" />
<pre>
<strong>Input:</strong> hour = 3, minutes = 15
<strong>Output:</strong> 7.5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hour &lt;= 12</code></li>
	<li><code>0 &lt;= minutes &lt;= 59</code></li>
</ul>


## Hints

1. The tricky part is determining how the minute hand affects the position of the hour hand.

2. Calculate the angles separately then find the difference.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm calculates the precise angular position of the hour hand and the minute hand relative to the 12:00 position (0 degrees). The minute hand rotates 360 degrees in 60 minutes, which equates to 6 degrees per minute. The hour hand rotates 360 degrees in 12 hours, meaning 30 degrees per hour, but it also shifts slightly as minutes pass at a rate of 0.5 degrees per minute (30 degrees divided by 60 minutes).

To find the final result, we compute the absolute difference between the hour hand's angle and the minute hand's angle. Since we need the smaller angle between the two hands, we check if the calculated difference is greater than 180 degrees. If it is, we return the difference subtracted from 360 degrees, ensuring the result is always the interior angle between the hands.

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
    double angleClock(int hour, int minutes) {
        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;
        double minuteAngle = minutes * 6.0;
        double diff = hourAngle - minuteAngle;
        if (diff < 0) diff = -diff;
        return diff > 180.0 ? 360.0 - diff : diff;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public double angleClock(int hour, int minutes) {
        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;
        double minuteAngle = minutes * 6.0;
        double diff = Math.abs(hourAngle - minuteAngle);
        if (diff > 180.0) {
            diff = 360.0 - diff;
        }
        return diff;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = (hour % 12) * 30.0 + minutes * 0.5
        minute_angle = minutes * 6.0
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360.0 - diff)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30.0 + minutes * 0.5
        minute_angle = minutes * 6.0
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360.0 - diff)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
double angleClock(int hour, int minutes) {
    double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;
    double minuteAngle = minutes * 6.0;
    double diff = hourAngle - minuteAngle;
    if (diff < 0) diff = -diff;
    if (diff > 180.0) {
        diff = 360.0 - diff;
    }
    return diff;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public double AngleClock(int hour, int minutes) {
        double minuteAngle = minutes * 6.0;
        double hourAngle = (hour % 12) * 30.0 + minutes * 0.5;
        double diff = Math.Abs(hourAngle - minuteAngle);
        return Math.Min(diff, 360.0 - diff);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} hour
 * @param {number} minutes
 * @return {number}
 */
var angleClock = function(hour, minutes) {
    let minuteAngle = minutes * 6;
    let hourAngle = (hour % 12) * 30 + minutes * 0.5;
    let diff = Math.abs(hourAngle - minuteAngle);
    return Math.min(diff, 360 - diff);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function angleClock(hour: number, minutes: number): number {
    const minuteAngle: number = minutes * 6;
    const hourAngle: number = (hour % 12) * 30 + minutes * 0.5;
    const diff: number = Math.abs(hourAngle - minuteAngle);
    return Math.min(diff, 360 - diff);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $hour
     * @param Integer $minutes
     * @return Float
     */
    function angleClock($hour, $minutes) {
        $minuteAngle = $minutes * 6.0;
        $hourAngle = ($hour % 12) * 30.0 + $minutes * 0.5;
        $diff = abs($hourAngle - $minuteAngle);
        return min($diff, 360.0 - $diff);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func angleClock(_ hour: Int, _ minutes: Int) -> Double {
        let minuteAngle = Double(minutes) * 6.0
        let hourAngle = Double(hour % 12) * 30.0 + Double(minutes) * 0.5
        let diff = abs(hourAngle - minuteAngle)
        return min(diff, 360.0 - diff)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun angleClock(hour: Int, minutes: Int): Double {
        val minuteAngle = minutes * 6.0
        val hourAngle = (hour % 12) * 30.0 + (minutes * 0.5)
        val diff = Math.abs(hourAngle - minuteAngle)
        return if (diff > 180.0) 360.0 - diff else diff
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  double angleClock(int hour, int minutes) {
    double minuteAngle = minutes * 6.0;
    double hourAngle = (hour % 12) * 30.0 + (minutes * 0.5);
    double diff = (hourAngle - minuteAngle).abs();
    return diff > 180.0 ? 360.0 - diff : diff;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "math"

func angleClock(hour int, minutes int) float64 {
    minuteAngle := float64(minutes) * 6.0
    hourAngle := float64(hour%12)*30.0 + float64(minutes)*0.5
    diff := math.Abs(hourAngle - minuteAngle)
    if diff > 180.0 {
        return 360.0 - diff
    }
    return diff
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} hour
# @param {Integer} minutes
# @return {Float}
def angle_clock(hour, minutes)
    minute_angle = minutes * 6.0
    hour_angle = (hour % 12) * 30.0 + (minutes * 0.5)
    diff = (hour_angle - minute_angle).abs
    diff > 180.0 ? 360.0 - diff : diff
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def angleClock(hour: Int, minutes: Int): Double = {
        val minuteAngle: Double = minutes * 6.0
        val hourAngle: Double = (hour % 12) * 30.0 + (minutes * 0.5)
        val diff: Double = Math.abs(hourAngle - minuteAngle)
        if (diff > 180.0) 360.0 - diff else diff
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn angle_clock(hour: i32, minutes: i32) -> f64 {
        let minute_angle = (minutes as f64) * 6.0;
        let hour_angle = ((hour % 12) as f64 * 30.0) + ((minutes as f64) * 0.5);
        let diff = (hour_angle - minute_angle).abs();
        if diff > 180.0 {
            360.0 - diff
        } else {
            diff
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (angle-clock hour minutes)
  (-> exact-integer? exact-integer? flonum?)
  (let* ([minute-angle (* (exact->inexact minutes) 6.0)]
         [hour-angle (+ (* (modulo hour 12) 30.0) (* (exact->inexact minutes) 0.5))]
         [diff (abs (- hour-angle minute-angle))])
    (if (> diff 180.0)
        (- 360.0 diff)
        diff)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec angle_clock(Hour :: integer(), Minutes :: integer()) -> float().
angle_clock(Hour, Minutes) ->
  MinuteAngle = Minutes * 6.0,
  HourAngle = (Hour rem 12) * 30.0 + Minutes * 0.5,
  Diff = abs(HourAngle - MinuteAngle),
  if
    Diff > 180.0 -> 360.0 - Diff;
    true -> Diff
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec angle_clock(hour :: integer, minutes :: integer) :: float
  def angle_clock(hour, minutes) do
    minute_angle = minutes * 6.0
    hour_angle = rem(hour, 12) * 30.0 + minutes * 0.5
    diff = abs(hour_angle - minute_angle)
    if diff > 180.0 do
      360.0 - diff
    else
      diff
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The solution performs a constant number of basic arithmetic operations (multiplication, addition, and subtraction) regardless of the input values.
- **Space Complexity:** O(1). The algorithm only utilizes a few primitive double-precision floating-point variables to store the hand positions and their difference, requiring no additional space that scales with input size.
