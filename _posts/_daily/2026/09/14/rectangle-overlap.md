---
layout: post
title: "Rectangle Overlap"
date: 2026-09-14 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Geometry"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/rectangle-overlap/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool isRectangleOverlap(vector<int>& rec1,\
        \ vector<int>& rec2) {\n        return rec1[0] < rec2[2] && rec1[2] > rec2[0]\
        \ &&\n               rec1[1] < rec2[3] && rec1[3] > rec2[1];\n    }\n};"
      java: "class Solution {\n    public boolean isRectangleOverlap(int[] rec1, int[]\
        \ rec2) {\n        return rec1[0] < rec2[2] && rec1[2] > rec2[0] &&\n      \
        \         rec1[1] < rec2[3] && rec1[3] > rec2[1];\n    }\n}"
      python: "class Solution(object):\n    def isRectangleOverlap(self, rec1, rec2):\n\
        \        \"\"\"\n        :type rec1: List[int]\n        :type rec2: List[int]\n\
        \        :rtype: bool\n        \"\"\"\n        return (rec1[0] < rec2[2] and\
        \ rec1[2] > rec2[0] and\n                rec1[1] < rec2[3] and rec1[3] > rec2[1])"
      python3: "class Solution:\n    def isRectangleOverlap(self, rec1: List[int], rec2:\
        \ List[int]) -> bool:\n        return (rec1[0] < rec2[2] and rec1[2] > rec2[0]\
        \ and\n                rec1[1] < rec2[3] and rec1[3] > rec2[1])"
      c: "bool isRectangleOverlap(int* rec1, int rec1Size, int* rec2, int rec2Size)\
        \ {\n    return (rec1[0] < rec2[2] && rec1[2] > rec2[0] &&\n            rec1[1]\
        \ < rec2[3] && rec1[3] > rec2[1]);\n}"
      csharp: "public class Solution {\n    public bool IsRectangleOverlap(int[] rec1,\
        \ int[] rec2) {\n        return rec1[0] < rec2[2] && rec1[2] > rec2[0] &&\n\
        \               rec1[1] < rec2[3] && rec1[3] > rec2[1];\n    }\n}"
      javascript: "/**\n * @param {number[]} rec1\n * @param {number[]} rec2\n * @return\
        \ {boolean}\n */\nvar isRectangleOverlap = function(rec1, rec2) {\n    return\
        \ (rec1[0] < rec2[2] && rec1[2] > rec2[0] &&\n            rec1[1] < rec2[3]\
        \ && rec1[3] > rec2[1]);\n};"
      typescript: "function isRectangleOverlap(rec1: number[], rec2: number[]): boolean\
        \ {\n    return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3]\
        \ && rec2[1] < rec1[3];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $rec1\n     * @param\
        \ Integer[] $rec2\n     * @return Boolean\n     */\n    function isRectangleOverlap($rec1,\
        \ $rec2) {\n        return $rec1[0] < $rec2[2] && $rec2[0] < $rec1[2] && $rec1[1]\
        \ < $rec2[3] && $rec2[1] < $rec1[3];\n    }\n}"
      swift: "class Solution {\n    func isRectangleOverlap(_ rec1: [Int], _ rec2: [Int])\
        \ -> Bool {\n        return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1]\
        \ < rec2[3] && rec2[1] < rec1[3]\n    }\n}"
      kotlin: "class Solution {\n    fun isRectangleOverlap(rec1: IntArray, rec2: IntArray):\
        \ Boolean {\n        return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1]\
        \ < rec2[3] && rec2[1] < rec1[3]\n    }\n}"
      dart: "class Solution {\n  bool isRectangleOverlap(List<int> rec1, List<int> rec2)\
        \ {\n    return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3]\
        \ && rec2[1] < rec1[3];\n  }\n}"
      go: "func isRectangleOverlap(rec1 []int, rec2 []int) bool {\n    return rec1[0]\
        \ < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3]\n\
        }"
      ruby: "# @param {Integer[]} rec1\n# @param {Integer[]} rec2\n# @return {Boolean}\n\
        def is_rectangle_overlap(rec1, rec2)\n  rec1[0] < rec2[2] && rec2[0] < rec1[2]\
        \ && rec1[1] < rec2[3] && rec2[1] < rec1[3]\nend"
      scala: "object Solution {\n    def isRectangleOverlap(rec1: Array[Int], rec2:\
        \ Array[Int]): Boolean = {\n        rec1(0) < rec2(2) && rec2(0) < rec1(2) &&\
        \ rec1(1) < rec2(3) && rec2(1) < rec1(3)\n    }\n}"
      rust: "impl Solution {\n    pub fn is_rectangle_overlap(rec1: Vec<i32>, rec2:\
        \ Vec<i32>) -> bool {\n        rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1]\
        \ < rec2[3] && rec2[1] < rec1[3]\n    }\n}"
      racket: "(define/contract (is-rectangle-overlap rec1 rec2)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) boolean?)\n  (and (< (list-ref rec1 0) (list-ref rec2\
        \ 2))\n       (< (list-ref rec2 0) (list-ref rec1 2))\n       (< (list-ref rec1\
        \ 1) (list-ref rec2 3))\n       (< (list-ref rec2 1) (list-ref rec1 3)))\n \
        \ )"
      erlang: "-spec is_rectangle_overlap(Rec1 :: [integer()], Rec2 :: [integer()])\
        \ -> boolean().\nis_rectangle_overlap(Rec1, Rec2) ->\n  [X11, Y11, X12, Y12]\
        \ = Rec1,\n  [X21, Y21, X22, Y22] = Rec2,\n  (X11 < X22) andalso (X21 < X12)\
        \ andalso (Y11 < Y22) andalso (Y21 < Y12)."
      elixir: "defmodule Solution do\n  @spec is_rectangle_overlap(rec1 :: [integer],\
        \ rec2 :: [integer]) :: boolean\n  def is_rectangle_overlap(rec1, rec2) do\n\
        \    [x11, y11, x12, y12] = rec1\n    [x21, y21, x22, y22] = rec2\n    x11 <\
        \ x22 and x21 < x12 and y11 < y22 and y21 < y12\n  end\nend"
    approach: 'To determine if two axis-aligned rectangles overlap, we check if their
      projections onto the x-axis and y-axis both overlap. Since the rectangles are
      axis-aligned, their overlap on the x-axis occurs if the range [x1, x2] and [x3,
      x4] have a common intersection with a positive length, which is satisfied if max(x1,
      x3) < min(x2, x4). Similarly, the y-axis projections must satisfy max(y1, y3)
      < min(y2, y4) for a positive intersection area to exist.


      Alternatively, we can express this by checking the inverse: a rectangle does not
      overlap if it is entirely to the left, right, above, or below the other rectangle.
      By applying De Morgan''s laws to negate these four conditions, we derive the intersection
      condition: the left edge of each rectangle must be strictly to the left of the
      right edge of the other, and the bottom edge of each rectangle must be strictly
      below the top edge of the other. This translates to the boolean expression: rec1[0]
      < rec2[2] && rec1[2] > rec2[0] && rec1[1] < rec2[3] && rec1[3] > rec2[1].'
    time_complexity: O(1). The algorithm performs a fixed number of logical comparisons
      (four) regardless of the coordinate values provided in the input.
    space_complexity: O(1). The solution uses a constant amount of memory and does not
      allocate any additional data structures or stack frames proportional to the input
      size.
    elapsed_time: 41.847177028656006
    model: gemini-3-flash-preview
    generated_at: '2026-09-14 02:42:48 '
---

## Problem #836: Rectangle Overlap

**Difficulty:** Easy

**Topics:** Math, Geometry

## Problem Description

<p>An axis-aligned rectangle is represented as a list <code>[x1, y1, x2, y2]</code>, where <code>(x1, y1)</code> is the coordinate of its bottom-left corner, and <code>(x2, y2)</code> is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.</p>

<p>Two rectangles overlap if the area of their intersection is <strong>positive</strong>. To be clear, two rectangles that only touch at the corner or edges do not overlap.</p>

<p>Given two axis-aligned rectangles <code>rec1</code> and <code>rec2</code>, return <code>true</code><em> if they overlap, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rec1 = [0,0,2,2], rec2 = [1,1,3,3]
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rec1 = [0,0,1,1], rec2 = [1,0,2,1]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> rec1 = [0,0,1,1], rec2 = [2,2,3,3]
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>rec1.length == 4</code></li>
	<li><code>rec2.length == 4</code></li>
	<li><code>-10<sup>9</sup> &lt;= rec1[i], rec2[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>rec1</code> and <code>rec2</code> represent a valid rectangle with a non-zero area.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To determine if two axis-aligned rectangles overlap, we check if their projections onto the x-axis and y-axis both overlap. Since the rectangles are axis-aligned, their overlap on the x-axis occurs if the range [x1, x2] and [x3, x4] have a common intersection with a positive length, which is satisfied if max(x1, x3) < min(x2, x4). Similarly, the y-axis projections must satisfy max(y1, y3) < min(y2, y4) for a positive intersection area to exist.

Alternatively, we can express this by checking the inverse: a rectangle does not overlap if it is entirely to the left, right, above, or below the other rectangle. By applying De Morgan's laws to negate these four conditions, we derive the intersection condition: the left edge of each rectangle must be strictly to the left of the right edge of the other, and the bottom edge of each rectangle must be strictly below the top edge of the other. This translates to the boolean expression: rec1[0] < rec2[2] && rec1[2] > rec2[0] && rec1[1] < rec2[3] && rec1[3] > rec2[1].

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
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return rec1[0] < rec2[2] && rec1[2] > rec2[0] &&
               rec1[1] < rec2[3] && rec1[3] > rec2[1];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        return rec1[0] < rec2[2] && rec1[2] > rec2[0] &&
               rec1[1] < rec2[3] && rec1[3] > rec2[1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return (rec1[0] < rec2[2] and rec1[2] > rec2[0] and
                rec1[1] < rec2[3] and rec1[3] > rec2[1])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (rec1[0] < rec2[2] and rec1[2] > rec2[0] and
                rec1[1] < rec2[3] and rec1[3] > rec2[1])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool isRectangleOverlap(int* rec1, int rec1Size, int* rec2, int rec2Size) {
    return (rec1[0] < rec2[2] && rec1[2] > rec2[0] &&
            rec1[1] < rec2[3] && rec1[3] > rec2[1]);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool IsRectangleOverlap(int[] rec1, int[] rec2) {
        return rec1[0] < rec2[2] && rec1[2] > rec2[0] &&
               rec1[1] < rec2[3] && rec1[3] > rec2[1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
    return (rec1[0] < rec2[2] && rec1[2] > rec2[0] &&
            rec1[1] < rec2[3] && rec1[3] > rec2[1]);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isRectangleOverlap(rec1: number[], rec2: number[]): boolean {
    return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $rec1
     * @param Integer[] $rec2
     * @return Boolean
     */
    function isRectangleOverlap($rec1, $rec2) {
        return $rec1[0] < $rec2[2] && $rec2[0] < $rec1[2] && $rec1[1] < $rec2[3] && $rec2[1] < $rec1[3];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func isRectangleOverlap(_ rec1: [Int], _ rec2: [Int]) -> Bool {
        return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun isRectangleOverlap(rec1: IntArray, rec2: IntArray): Boolean {
        return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool isRectangleOverlap(List<int> rec1, List<int> rec2) {
    return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isRectangleOverlap(rec1 []int, rec2 []int) bool {
    return rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} rec1
# @param {Integer[]} rec2
# @return {Boolean}
def is_rectangle_overlap(rec1, rec2)
  rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def isRectangleOverlap(rec1: Array[Int], rec2: Array[Int]): Boolean = {
        rec1(0) < rec2(2) && rec2(0) < rec1(2) && rec1(1) < rec2(3) && rec2(1) < rec1(3)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn is_rectangle_overlap(rec1: Vec<i32>, rec2: Vec<i32>) -> bool {
        rec1[0] < rec2[2] && rec2[0] < rec1[2] && rec1[1] < rec2[3] && rec2[1] < rec1[3]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (is-rectangle-overlap rec1 rec2)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  (and (< (list-ref rec1 0) (list-ref rec2 2))
       (< (list-ref rec2 0) (list-ref rec1 2))
       (< (list-ref rec1 1) (list-ref rec2 3))
       (< (list-ref rec2 1) (list-ref rec1 3)))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec is_rectangle_overlap(Rec1 :: [integer()], Rec2 :: [integer()]) -> boolean().
is_rectangle_overlap(Rec1, Rec2) ->
  [X11, Y11, X12, Y12] = Rec1,
  [X21, Y21, X22, Y22] = Rec2,
  (X11 < X22) andalso (X21 < X12) andalso (Y11 < Y22) andalso (Y21 < Y12).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec is_rectangle_overlap(rec1 :: [integer], rec2 :: [integer]) :: boolean
  def is_rectangle_overlap(rec1, rec2) do
    [x11, y11, x12, y12] = rec1
    [x21, y21, x22, y22] = rec2
    x11 < x22 and x21 < x12 and y11 < y22 and y21 < y12
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). The algorithm performs a fixed number of logical comparisons (four) regardless of the coordinate values provided in the input.
- **Space Complexity:** O(1). The solution uses a constant amount of memory and does not allocate any additional data structures or stack frames proportional to the input size.
