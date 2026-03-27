---
layout: post
title: "Matrix Similarity After Cyclic Shifts"
date: 2026-03-27 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math", "Matrix", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool areSimilar(vector<vector<int>>& mat,\
        \ int k) {\n        int m = mat.size();\n        int n = mat[0].size();\n  \
        \      k %= n;\n        if (k == 0) return true;\n        for (int i = 0; i\
        \ < m; ++i) {\n            for (int j = 0; j < n; ++j) {\n                if\
        \ (mat[i][j] != mat[i][(j + k) % n]) {\n                    return false;\n\
        \                }\n            }\n        }\n        return true;\n    }\n\
        };"
      java: "class Solution {\n    public boolean areSimilar(int[][] mat, int k) {\n\
        \        int m = mat.length;\n        int n = mat[0].length;\n        k %= n;\n\
        \        for (int i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++)\
        \ {\n                if (mat[i][j] != mat[i][(j + k) % n]) {\n             \
        \       return false;\n                }\n            }\n        }\n       \
        \ return true;\n    }\n}"
      python: "class Solution(object):\n    def areSimilar(self, mat, k):\n        \"\
        \"\"\n        :type mat: List[List[int]]\n        :type k: int\n        :rtype:\
        \ bool\n        \"\"\"\n        m = len(mat)\n        n = len(mat[0])\n    \
        \    k %= n\n        for i in range(m):\n            for j in range(n):\n  \
        \              if mat[i][j] != mat[i][(j + k) % n]:\n                    return\
        \ False\n        return True"
      python3: "class Solution:\n    def areSimilar(self, mat: List[List[int]], k: int)\
        \ -> bool:\n        m, n = len(mat), len(mat[0])\n        k %= n\n        for\
        \ i in range(m):\n            for j in range(n):\n                if mat[i][j]\
        \ != mat[i][(j + k) % n]:\n                    return False\n        return\
        \ True"
      c: "bool areSimilar(int** mat, int matSize, int* matColSize, int k) {\n    int\
        \ m = matSize;\n    int n = matColSize[0];\n    k %= n;\n    for (int i = 0;\
        \ i < m; i++) {\n        for (int j = 0; j < n; j++) {\n            if (mat[i][j]\
        \ != mat[i][(j + k) % n]) {\n                return false;\n            }\n\
        \        }\n    }\n    return true;\n}"
      csharp: "public class Solution {\n    public bool AreSimilar(int[][] mat, int\
        \ k) {\n        int m = mat.Length;\n        int n = mat[0].Length;\n      \
        \  k %= n;\n        for (int i = 0; i < m; i++) {\n            for (int j =\
        \ 0; j < n; j++) {\n                if (mat[i][j] != mat[i][(j + k) % n]) {\n\
        \                    return false;\n                }\n            }\n     \
        \   }\n        return true;\n    }\n}"
      javascript: "/**\n * @param {number[][]} mat\n * @param {number} k\n * @return\
        \ {boolean}\n */\nvar areSimilar = function(mat, k) {\n    const m = mat.length;\n\
        \    const n = mat[0].length;\n    const shift = k % n;\n    for (let i = 0;\
        \ i < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if (mat[i][j]\
        \ !== mat[i][(j + shift) % n]) {\n                return false;\n          \
        \  }\n        }\n    }\n    return true;\n};"
      typescript: "function areSimilar(mat: number[][], k: number): boolean {\n    const\
        \ m = mat.length;\n    const n = mat[0].length;\n    const shift = k % n;\n\
        \    if (shift === 0) return true;\n    for (let i = 0; i < m; i++) {\n    \
        \    for (let j = 0; j < n; j++) {\n            if (mat[i][j] !== mat[i][(j\
        \ + shift) % n]) {\n                return false;\n            }\n        }\n\
        \    }\n    return true;\n};"
      php: "class Solution {\n    /**\n     * @param Integer[][] $mat\n     * @param\
        \ Integer $k\n     * @return Boolean\n     */\n    function areSimilar($mat,\
        \ $k) {\n        $m = count($mat);\n        $n = count($mat[0]);\n        $shift\
        \ = $k % $n;\n        if ($shift == 0) return true;\n        for ($i = 0; $i\
        \ < $m; $i++) {\n            for ($j = 0; $j < $n; $j++) {\n               \
        \ if ($mat[$i][$j] != $mat[$i][($j + $shift) % $n]) {\n                    return\
        \ false;\n                }\n            }\n        }\n        return true;\n\
        \    }\n}"
      swift: "class Solution {\n    func areSimilar(_ mat: [[Int]], _ k: Int) -> Bool\
        \ {\n        let m = mat.count\n        let n = mat[0].count\n        let shift\
        \ = k % n\n        if shift == 0 { return true }\n        for i in 0..<m {\n\
        \            for j in 0..<n {\n                if mat[i][j] != mat[i][(j + shift)\
        \ % n] {\n                    return false\n                }\n            }\n\
        \        }\n        return true\n    }\n}"
      kotlin: "class Solution {\n    fun areSimilar(mat: Array<IntArray>, k: Int): Boolean\
        \ {\n        val m = mat.size\n        val n = mat[0].size\n        val shift\
        \ = k % n\n        if (shift == 0) return true\n        for (i in 0 until m)\
        \ {\n            for (j in 0 until n) {\n                if (mat[i][j] != mat[i][(j\
        \ + shift) % n]) {\n                    return false\n                }\n  \
        \          }\n        }\n        return true\n    }\n}"
      dart: "class Solution {\n  bool areSimilar(List<List<int>> mat, int k) {\n   \
        \ int m = mat.length;\n    int n = mat[0].length;\n    int shift = k % n;\n\
        \    if (shift == 0) return true;\n    for (int i = 0; i < m; i++) {\n     \
        \ for (int j = 0; j < n; j++) {\n        if (mat[i][j] != mat[i][(j + shift)\
        \ % n]) {\n          return false;\n        }\n      }\n    }\n    return true;\n\
        \  }\n}"
      go: "func areSimilar(mat [][]int, k int) bool {\n    m := len(mat)\n    n := len(mat[0])\n\
        \    shift := k % n\n    if shift == 0 {\n        return true\n    }\n    for\
        \ i := 0; i < m; i++ {\n        for j := 0; j < n; j++ {\n            if mat[i][j]\
        \ != mat[i][(j+shift)%n] {\n                return false\n            }\n  \
        \      }\n    }\n    return true\n}"
      ruby: "def are_similar(mat, k)\n  n = mat[0].length\n  shift = k % n\n  mat.each\
        \ do |row|\n    n.times do |j|\n      return false if row[j] != row[(j + shift)\
        \ % n]\n    end\n  end\n  true\nend"
      scala: "object Solution {\n    def areSimilar(mat: Array[Array[Int]], k: Int):\
        \ Boolean = {\n        val n = mat(0).length\n        val shift = k % n\n  \
        \      for (i <- mat.indices) {\n            for (j <- 0 until n) {\n      \
        \          if (mat(i)(j) != mat(i)((j + shift) % n)) {\n                   \
        \ return false\n                }\n            }\n        }\n        true\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn are_similar(mat: Vec<Vec<i32>>, k: i32) ->\
        \ bool {\n        let n = mat[0].len();\n        let shift = (k as usize) %\
        \ n;\n        for row in mat {\n            for j in 0..n {\n              \
        \  if row[j] != row[(j + shift) % n] {\n                    return false;\n\
        \                }\n            }\n        }\n        true\n    }\n}"
      racket: "(define/contract (are-similar mat k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? boolean?)\n  (let* ([n (length (car mat))]\n         [shift\
        \ (remainder k n)])\n    (for/and ([row mat])\n      (let ([row-vec (list->vector\
        \ row)])\n        (for/and ([j (in-range n)])\n          (= (vector-ref row-vec\
        \ j)\n             (vector-ref row-vec (remainder (+ j shift) n))))))))"
      erlang: "-spec are_similar(Mat :: [[integer()]], K :: integer()) -> boolean().\n\
        are_similar(Mat, K) ->\n  N = length(hd(Mat)),\n  Shift = K rem N,\n  lists:all(fun(Row)\
        \ ->\n    RowVec = list_to_tuple(Row),\n    lists:all(fun(J) ->\n      element(J\
        \ + 1, RowVec) =:= element((J + Shift) rem N + 1, RowVec)\n    end, lists:seq(0,\
        \ N - 1))\n  end, Mat)."
      elixir: "defmodule Solution do\n  @spec are_similar(mat :: [[integer]], k :: integer)\
        \ :: boolean\n  def are_similar(mat, k) do\n    n = length(hd(mat))\n    shift\
        \ = rem(k, n)\n    Enum.all?(mat, fn row ->\n      row_tuple = List.to_tuple(row)\n\
        \      Enum.all?(0..(n - 1), fn j ->\n        elem(row_tuple, j) == elem(row_tuple,\
        \ rem(j + shift, n))\n      end)\n    end)\n  end\nend"
    approach: 'A cyclic shift of a row by k positions results in the same row if and
      only if each element at index j is identical to the element at the position it
      was shifted from. Specifically, for a left shift, the element at index j in the
      new matrix originates from index (j + k) % n in the original matrix. For a right
      shift, it originates from (j - k + n) % n. In both cases, the row remains identical
      if the sequence is periodic such that mat[i][j] == mat[i][(j + k) % n] for all
      j.


      Since the problem asks if the matrix remains identical after k shifts, we can
      simplify k by taking k % n. We then iterate through every element in the matrix
      and check if mat[i][j] matches its counterpart mat[i][(j + k) % n]. If this condition
      holds for all elements, the cyclic shifts (regardless of whether they are left
      or right) will preserve the row''s content, and we return true. Otherwise, we
      return false.'
    time_complexity: O(m * n) where m is the number of rows and n is the number of columns.
      We perform a nested loop over every element in the matrix exactly once to verify
      the condition.
    space_complexity: O(1) as we only use a constant amount of extra space for the column
      count and loop indices, without allocating any additional data structures.
    elapsed_time: 122.29508686065674
    model: gemini-3-flash-preview
    generated_at: '2026-03-27 01:48:00 '
---

## Problem #2946: Matrix Similarity After Cyclic Shifts

**Difficulty:** Easy

**Topics:** Array, Math, Matrix, Simulation

## Problem Description

<p>You are given an <code>m x n</code> integer matrix <code>mat</code> and an integer <code>k</code>. The matrix rows are 0-indexed.</p>

<p>The following proccess happens <code>k</code> times:</p>

<ul>
	<li><strong>Even-indexed</strong> rows (0, 2, 4, ...) are cyclically shifted to the left.</li>
</ul>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/lshift.jpg" style="width: 283px; height: 90px;" /></p>

<ul>
	<li><strong>Odd-indexed</strong> rows (1, 3, 5, ...) are cyclically shifted to the right.</li>
</ul>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/rshift-stlone.jpg" style="width: 283px; height: 90px;" /></p>

<p>Return <code>true</code> if the final modified matrix after <code>k</code> steps is identical to the original matrix, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).</p>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/t1-2.jpg" style="width: 857px; height: 150px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/t1-3.jpg" style="width: 632px; height: 150px;" /></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[2,2],[2,2]], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= mat.length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i].length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 25</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>


## Hints

1. You can reduce `k` shifts to `(k % n)` shifts as after `n` shifts the matrix will become similar to the initial matrix.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

A cyclic shift of a row by k positions results in the same row if and only if each element at index j is identical to the element at the position it was shifted from. Specifically, for a left shift, the element at index j in the new matrix originates from index (j + k) % n in the original matrix. For a right shift, it originates from (j - k + n) % n. In both cases, the row remains identical if the sequence is periodic such that mat[i][j] == mat[i][(j + k) % n] for all j.

Since the problem asks if the matrix remains identical after k shifts, we can simplify k by taking k % n. We then iterate through every element in the matrix and check if mat[i][j] matches its counterpart mat[i][(j + k) % n]. If this condition holds for all elements, the cyclic shifts (regardless of whether they are left or right) will preserve the row's content, and we return true. Otherwise, we return false.

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
    bool areSimilar(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();
        k %= n;
        if (k == 0) return true;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] != mat[i][(j + k) % n]) {
                    return false;
                }
            }
        }
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
    public boolean areSimilar(int[][] mat, int k) {
        int m = mat.length;
        int n = mat[0].length;
        k %= n;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != mat[i][(j + k) % n]) {
                    return false;
                }
            }
        }
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
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])
        k %= n
        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n
        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool areSimilar(int** mat, int matSize, int* matColSize, int k) {
    int m = matSize;
    int n = matColSize[0];
    k %= n;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] != mat[i][(j + k) % n]) {
                return false;
            }
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool AreSimilar(int[][] mat, int k) {
        int m = mat.Length;
        int n = mat[0].Length;
        k %= n;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != mat[i][(j + k) % n]) {
                    return false;
                }
            }
        }
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
 * @param {number[][]} mat
 * @param {number} k
 * @return {boolean}
 */
var areSimilar = function(mat, k) {
    const m = mat.length;
    const n = mat[0].length;
    const shift = k % n;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] !== mat[i][(j + shift) % n]) {
                return false;
            }
        }
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function areSimilar(mat: number[][], k: number): boolean {
    const m = mat.length;
    const n = mat[0].length;
    const shift = k % n;
    if (shift === 0) return true;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] !== mat[i][(j + shift) % n]) {
                return false;
            }
        }
    }
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
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Boolean
     */
    function areSimilar($mat, $k) {
        $m = count($mat);
        $n = count($mat[0]);
        $shift = $k % $n;
        if ($shift == 0) return true;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] != $mat[$i][($j + $shift) % $n]) {
                    return false;
                }
            }
        }
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
    func areSimilar(_ mat: [[Int]], _ k: Int) -> Bool {
        let m = mat.count
        let n = mat[0].count
        let shift = k % n
        if shift == 0 { return true }
        for i in 0..<m {
            for j in 0..<n {
                if mat[i][j] != mat[i][(j + shift) % n] {
                    return false
                }
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun areSimilar(mat: Array<IntArray>, k: Int): Boolean {
        val m = mat.size
        val n = mat[0].size
        val shift = k % n
        if (shift == 0) return true
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] != mat[i][(j + shift) % n]) {
                    return false
                }
            }
        }
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
  bool areSimilar(List<List<int>> mat, int k) {
    int m = mat.length;
    int n = mat[0].length;
    int shift = k % n;
    if (shift == 0) return true;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] != mat[i][(j + shift) % n]) {
          return false;
        }
      }
    }
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func areSimilar(mat [][]int, k int) bool {
    m := len(mat)
    n := len(mat[0])
    shift := k % n
    if shift == 0 {
        return true
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if mat[i][j] != mat[i][(j+shift)%n] {
                return false
            }
        }
    }
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def are_similar(mat, k)
  n = mat[0].length
  shift = k % n
  mat.each do |row|
    n.times do |j|
      return false if row[j] != row[(j + shift) % n]
    end
  end
  true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def areSimilar(mat: Array[Array[Int]], k: Int): Boolean = {
        val n = mat(0).length
        val shift = k % n
        for (i <- mat.indices) {
            for (j <- 0 until n) {
                if (mat(i)(j) != mat(i)((j + shift) % n)) {
                    return false
                }
            }
        }
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
    pub fn are_similar(mat: Vec<Vec<i32>>, k: i32) -> bool {
        let n = mat[0].len();
        let shift = (k as usize) % n;
        for row in mat {
            for j in 0..n {
                if row[j] != row[(j + shift) % n] {
                    return false;
                }
            }
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (are-similar mat k)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  (let* ([n (length (car mat))]
         [shift (remainder k n)])
    (for/and ([row mat])
      (let ([row-vec (list->vector row)])
        (for/and ([j (in-range n)])
          (= (vector-ref row-vec j)
             (vector-ref row-vec (remainder (+ j shift) n))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec are_similar(Mat :: [[integer()]], K :: integer()) -> boolean().
are_similar(Mat, K) ->
  N = length(hd(Mat)),
  Shift = K rem N,
  lists:all(fun(Row) ->
    RowVec = list_to_tuple(Row),
    lists:all(fun(J) ->
      element(J + 1, RowVec) =:= element((J + Shift) rem N + 1, RowVec)
    end, lists:seq(0, N - 1))
  end, Mat).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec are_similar(mat :: [[integer]], k :: integer) :: boolean
  def are_similar(mat, k) do
    n = length(hd(mat))
    shift = rem(k, n)
    Enum.all?(mat, fn row ->
      row_tuple = List.to_tuple(row)
      Enum.all?(0..(n - 1), fn j ->
        elem(row_tuple, j) == elem(row_tuple, rem(j + shift, n))
      end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n) where m is the number of rows and n is the number of columns. We perform a nested loop over every element in the matrix exactly once to verify the condition.
- **Space Complexity:** O(1) as we only use a constant amount of extra space for the column count and loop indices, without allocating any additional data structures.
