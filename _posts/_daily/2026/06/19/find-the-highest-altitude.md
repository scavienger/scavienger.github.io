---
layout: post
title: "Find the Highest Altitude"
date: 2026-06-19 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Prefix Sum"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-the-highest-altitude/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int largestAltitude(vector<int>& gain) {\n\
        \        int currentAltitude = 0;\n        int maxAltitude = 0;\n        for\
        \ (int i = 0; i < gain.size(); ++i) {\n            currentAltitude += gain[i];\n\
        \            if (currentAltitude > maxAltitude) {\n                maxAltitude\
        \ = currentAltitude;\n            }\n        }\n        return maxAltitude;\n\
        \    }\n};"
      java: "class Solution {\n    public int largestAltitude(int[] gain) {\n      \
        \  int currentAltitude = 0;\n        int maxAltitude = 0;\n        for (int\
        \ g : gain) {\n            currentAltitude += g;\n            if (currentAltitude\
        \ > maxAltitude) {\n                maxAltitude = currentAltitude;\n       \
        \     }\n        }\n        return maxAltitude;\n    }\n}"
      python: "class Solution(object):\n    def largestAltitude(self, gain):\n     \
        \   \"\"\"\n        :type gain: List[int]\n        :rtype: int\n        \"\"\
        \"\n        current_altitude = 0\n        max_altitude = 0\n        for g in\
        \ gain:\n            current_altitude += g\n            if current_altitude\
        \ > max_altitude:\n                max_altitude = current_altitude\n       \
        \ return max_altitude"
      python3: "class Solution:\n    def largestAltitude(self, gain: List[int]) -> int:\n\
        \        current_altitude = 0\n        max_altitude = 0\n        for g in gain:\n\
        \            current_altitude += g\n            if current_altitude > max_altitude:\n\
        \                max_altitude = current_altitude\n        return max_altitude"
      c: "int largestAltitude(int* gain, int gainSize) {\n    int currentAltitude =\
        \ 0;\n    int maxAltitude = 0;\n    for (int i = 0; i < gainSize; i++) {\n \
        \       currentAltitude += gain[i];\n        if (currentAltitude > maxAltitude)\
        \ {\n            maxAltitude = currentAltitude;\n        }\n    }\n    return\
        \ maxAltitude;\n}"
      csharp: "public class Solution {\n    public int LargestAltitude(int[] gain) {\n\
        \        int currentAltitude = 0;\n        int maxAltitude = 0;\n        foreach\
        \ (int g in gain) {\n            currentAltitude += g;\n            if (currentAltitude\
        \ > maxAltitude) {\n                maxAltitude = currentAltitude;\n       \
        \     }\n        }\n        return maxAltitude;\n    }\n}"
      javascript: "/**\n * @param {number[]} gain\n * @return {number}\n */\nvar largestAltitude\
        \ = function(gain) {\n    let currentAltitude = 0;\n    let maxAltitude = 0;\n\
        \    for (let i = 0; i < gain.length; i++) {\n        currentAltitude += gain[i];\n\
        \        if (currentAltitude > maxAltitude) {\n            maxAltitude = currentAltitude;\n\
        \        }\n    }\n    return maxAltitude;\n};"
      typescript: "function largestAltitude(gain: number[]): number {\n    let maxAlt\
        \ = 0;\n    let currentAlt = 0;\n    for (let i = 0; i < gain.length; i++) {\n\
        \        currentAlt += gain[i];\n        if (currentAlt > maxAlt) {\n      \
        \      maxAlt = currentAlt;\n        }\n    }\n    return maxAlt;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $gain\n     * @return\
        \ Integer\n     */\n    function largestAltitude($gain) {\n        $maxAlt =\
        \ 0;\n        $currentAlt = 0;\n        foreach ($gain as $g) {\n          \
        \  $currentAlt += $g;\n            if ($currentAlt > $maxAlt) {\n          \
        \      $maxAlt = $currentAlt;\n            }\n        }\n        return $maxAlt;\n\
        \    }\n}"
      swift: "class Solution {\n    func largestAltitude(_ gain: [Int]) -> Int {\n \
        \       var maxAlt = 0\n        var currentAlt = 0\n        for g in gain {\n\
        \            currentAlt += g\n            if currentAlt > maxAlt {\n       \
        \         maxAlt = currentAlt\n            }\n        }\n        return maxAlt\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun largestAltitude(gain: IntArray): Int {\n  \
        \      var maxAlt = 0\n        var currentAlt = 0\n        for (g in gain) {\n\
        \            currentAlt += g\n            if (currentAlt > maxAlt) {\n     \
        \           maxAlt = currentAlt\n            }\n        }\n        return maxAlt\n\
        \    }\n}"
      dart: "class Solution {\n  int largestAltitude(List<int> gain) {\n    int maxAlt\
        \ = 0;\n    int currentAlt = 0;\n    for (int g in gain) {\n      currentAlt\
        \ += g;\n      if (currentAlt > maxAlt) {\n        maxAlt = currentAlt;\n  \
        \    }\n    }\n    return maxAlt;\n  }\n}"
      go: "func largestAltitude(gain []int) int {\n    maxAlt := 0\n    currentAlt :=\
        \ 0\n    for _, g := range gain {\n        currentAlt += g\n        if currentAlt\
        \ > maxAlt {\n            maxAlt = currentAlt\n        }\n    }\n    return\
        \ maxAlt\n}"
      ruby: "# @param {Integer[]} gain\n# @return {Integer}\ndef largest_altitude(gain)\n\
        \  max_alt = 0\n  current_alt = 0\n  gain.each do |g|\n    current_alt += g\n\
        \    max_alt = current_alt if current_alt > max_alt\n  end\n  max_alt\nend"
      scala: "object Solution {\n    def largestAltitude(gain: Array[Int]): Int = {\n\
        \        var maxAlt = 0\n        var currentAlt = 0\n        for (g <- gain)\
        \ {\n            currentAlt += g\n            if (currentAlt > maxAlt) {\n \
        \               maxAlt = currentAlt\n            }\n        }\n        maxAlt\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn largest_altitude(gain: Vec<i32>) -> i32 {\n\
        \        let mut max_alt = 0;\n        let mut current_alt = 0;\n        for\
        \ g in gain {\n            current_alt += g;\n            if current_alt > max_alt\
        \ {\n                max_alt = current_alt;\n            }\n        }\n    \
        \    max_alt\n    }\n}"
      racket: "(define/contract (largest-altitude gain)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let loop ([remaining gain]\n             [current 0]\n\
        \             [max-alt 0])\n    (if (null? remaining)\n        max_alt\n   \
        \     (let ([next-alt (+ current (car remaining))])\n          (loop (cdr remaining)\
        \ next-alt (max max-alt next-alt))))))"
      erlang: "-spec largest_altitude(Gain :: [integer()]) -> integer().\nlargest_altitude(Gain)\
        \ ->\n  largest_altitude_recursive(Gain, 0, 0).\n\nlargest_altitude_recursive([],\
        \ _Current, Max) ->\n  Max;\nlargest_altitude_recursive([H | T], Current, Max)\
        \ ->\n  Next = Current + H,\n  NewMax = if Next > Max -> Next; true -> Max end,\n\
        \  largest_altitude_recursive(T, Next, NewMax)."
      elixir: "defmodule Solution do\n  @spec largest_altitude(gain :: [integer]) ::\
        \ integer\n  def largest_altitude(gain) do\n    {_last, max_alt} = Enum.reduce(gain,\
        \ {0, 0}, fn g, {current, max_alt} ->\n      next = current + g\n      {next,\
        \ max(max_alt, next)}\n    end)\n    max_alt\n  end\nend"
    approach: 'The biker begins the journey at an altitude of 0. To find the altitude
      at any point $i+1$, we simply calculate the sum of all altitude gains from index
      0 to $i$. This represents a prefix sum problem where each value in the sequence
      of altitudes is the cumulative sum of the ''gain'' array elements encountered
      so far, starting from the initial base of 0.


      We iterate through the ''gain'' array once, maintaining a running total of the
      current altitude. At each step, we update this running total by adding the current
      gain and then check if this new altitude exceeds our previously recorded maximum
      altitude. Since the biker starts at altitude 0, we initialize the maximum altitude
      to 0 and return the highest value found after processing all gains.'
    time_complexity: O(n) where n is the length of the gain array. The algorithm performs
      a single linear pass through the input array to calculate the cumulative sum and
      track the maximum value.
    space_complexity: O(1) because we only use a constant amount of extra space for
      the current altitude and the maximum altitude variables, regardless of the size
      of the input array.
    elapsed_time: 301.5842809677124
    model: gemini-3-flash-preview
    generated_at: '2026-06-19 03:40:59 '
---

## Problem #1732: Find the Highest Altitude

**Difficulty:** Easy

**Topics:** Array, Prefix Sum

## Problem Description

<p>There is a biker going on a road trip. The road trip consists of <code>n + 1</code> points at different altitudes. The biker starts his trip on point <code>0</code> with altitude equal <code>0</code>.</p>

<p>You are given an integer array <code>gain</code> of length <code>n</code> where <code>gain[i]</code> is the <strong>net gain in altitude</strong> between points <code>i</code>​​​​​​ and <code>i + 1</code> for all (<code>0 &lt;= i &lt; n)</code>. Return <em>the <strong>highest altitude</strong> of a point.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> gain = [-5,1,5,0,-7]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> gain = [-4,-3,-2,-1,4,3,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == gain.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>-100 &lt;= gain[i] &lt;= 100</code></li>
</ul>


## Hints

1. Let's note that the altitude of an element is the sum of gains of all the elements behind it

2. Getting the altitudes can be done by getting the prefix sum array of the given array

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The biker begins the journey at an altitude of 0. To find the altitude at any point $i+1$, we simply calculate the sum of all altitude gains from index 0 to $i$. This represents a prefix sum problem where each value in the sequence of altitudes is the cumulative sum of the 'gain' array elements encountered so far, starting from the initial base of 0.

We iterate through the 'gain' array once, maintaining a running total of the current altitude. At each step, we update this running total by adding the current gain and then check if this new altitude exceeds our previously recorded maximum altitude. Since the biker starts at altitude 0, we initialize the maximum altitude to 0 and return the highest value found after processing all gains.

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
    int largestAltitude(vector<int>& gain) {
        int currentAltitude = 0;
        int maxAltitude = 0;
        for (int i = 0; i < gain.size(); ++i) {
            currentAltitude += gain[i];
            if (currentAltitude > maxAltitude) {
                maxAltitude = currentAltitude;
            }
        }
        return maxAltitude;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int largestAltitude(int[] gain) {
        int currentAltitude = 0;
        int maxAltitude = 0;
        for (int g : gain) {
            currentAltitude += g;
            if (currentAltitude > maxAltitude) {
                maxAltitude = currentAltitude;
            }
        }
        return maxAltitude;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        max_altitude = 0
        for g in gain:
            current_altitude += g
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        for g in gain:
            current_altitude += g
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int largestAltitude(int* gain, int gainSize) {
    int currentAltitude = 0;
    int maxAltitude = 0;
    for (int i = 0; i < gainSize; i++) {
        currentAltitude += gain[i];
        if (currentAltitude > maxAltitude) {
            maxAltitude = currentAltitude;
        }
    }
    return maxAltitude;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LargestAltitude(int[] gain) {
        int currentAltitude = 0;
        int maxAltitude = 0;
        foreach (int g in gain) {
            currentAltitude += g;
            if (currentAltitude > maxAltitude) {
                maxAltitude = currentAltitude;
            }
        }
        return maxAltitude;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let currentAltitude = 0;
    let maxAltitude = 0;
    for (let i = 0; i < gain.length; i++) {
        currentAltitude += gain[i];
        if (currentAltitude > maxAltitude) {
            maxAltitude = currentAltitude;
        }
    }
    return maxAltitude;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestAltitude(gain: number[]): number {
    let maxAlt = 0;
    let currentAlt = 0;
    for (let i = 0; i < gain.length; i++) {
        currentAlt += gain[i];
        if (currentAlt > maxAlt) {
            maxAlt = currentAlt;
        }
    }
    return maxAlt;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $gain
     * @return Integer
     */
    function largestAltitude($gain) {
        $maxAlt = 0;
        $currentAlt = 0;
        foreach ($gain as $g) {
            $currentAlt += $g;
            if ($currentAlt > $maxAlt) {
                $maxAlt = $currentAlt;
            }
        }
        return $maxAlt;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestAltitude(_ gain: [Int]) -> Int {
        var maxAlt = 0
        var currentAlt = 0
        for g in gain {
            currentAlt += g
            if currentAlt > maxAlt {
                maxAlt = currentAlt
            }
        }
        return maxAlt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var maxAlt = 0
        var currentAlt = 0
        for (g in gain) {
            currentAlt += g
            if (currentAlt > maxAlt) {
                maxAlt = currentAlt
            }
        }
        return maxAlt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int largestAltitude(List<int> gain) {
    int maxAlt = 0;
    int currentAlt = 0;
    for (int g in gain) {
      currentAlt += g;
      if (currentAlt > maxAlt) {
        maxAlt = currentAlt;
      }
    }
    return maxAlt;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func largestAltitude(gain []int) int {
    maxAlt := 0
    currentAlt := 0
    for _, g := range gain {
        currentAlt += g
        if currentAlt > maxAlt {
            maxAlt = currentAlt
        }
    }
    return maxAlt
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} gain
# @return {Integer}
def largest_altitude(gain)
  max_alt = 0
  current_alt = 0
  gain.each do |g|
    current_alt += g
    max_alt = current_alt if current_alt > max_alt
  end
  max_alt
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def largestAltitude(gain: Array[Int]): Int = {
        var maxAlt = 0
        var currentAlt = 0
        for (g <- gain) {
            currentAlt += g
            if (currentAlt > maxAlt) {
                maxAlt = currentAlt
            }
        }
        maxAlt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let mut max_alt = 0;
        let mut current_alt = 0;
        for g in gain {
            current_alt += g;
            if current_alt > max_alt {
                max_alt = current_alt;
            }
        }
        max_alt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (largest-altitude gain)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ([remaining gain]
             [current 0]
             [max-alt 0])
    (if (null? remaining)
        max_alt
        (let ([next-alt (+ current (car remaining))])
          (loop (cdr remaining) next-alt (max max-alt next-alt))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec largest_altitude(Gain :: [integer()]) -> integer().
largest_altitude(Gain) ->
  largest_altitude_recursive(Gain, 0, 0).

largest_altitude_recursive([], _Current, Max) ->
  Max;
largest_altitude_recursive([H | T], Current, Max) ->
  Next = Current + H,
  NewMax = if Next > Max -> Next; true -> Max end,
  largest_altitude_recursive(T, Next, NewMax).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_altitude(gain :: [integer]) :: integer
  def largest_altitude(gain) do
    {_last, max_alt} = Enum.reduce(gain, {0, 0}, fn g, {current, max_alt} ->
      next = current + g
      {next, max(max_alt, next)}
    end)
    max_alt
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the gain array. The algorithm performs a single linear pass through the input array to calculate the cumulative sum and track the maximum value.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for the current altitude and the maximum altitude variables, regardless of the size of the input array.
