---
layout: post
title: "Rotate Image"
date: 2026-05-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/rotate-image/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    void rotate(vector<vector<int>>& matrix)\
        \ {\n        int n = matrix.size();\n        for (int i = 0; i < n; i++) {\n\
        \            for (int j = i + 1; j < n; j++) {\n                int temp = matrix[i][j];\n\
        \                matrix[i][j] = matrix[j][i];\n                matrix[j][i]\
        \ = temp;\n            }\n        }\n        for (int i = 0; i < n; i++) {\n\
        \            for (int j = 0; j < n / 2; j++) {\n                int temp = matrix[i][j];\n\
        \                matrix[i][j] = matrix[i][n - 1 - j];\n                matrix[i][n\
        \ - 1 - j] = temp;\n            }\n        }\n    }\n};"
      java: "class Solution {\n    public void rotate(int[][] matrix) {\n        int\
        \ n = matrix.length;\n        for (int i = 0; i < n; i++) {\n            for\
        \ (int j = i + 1; j < n; j++) {\n                int temp = matrix[i][j];\n\
        \                matrix[i][j] = matrix[j][i];\n                matrix[j][i]\
        \ = temp;\n            }\n        }\n        for (int i = 0; i < n; i++) {\n\
        \            for (int j = 0; j < n / 2; j++) {\n                int temp = matrix[i][j];\n\
        \                matrix[i][j] = matrix[i][n - 1 - j];\n                matrix[i][n\
        \ - 1 - j] = temp;\n            }\n        }\n    }\n}"
      python: "class Solution(object):\n    def rotate(self, matrix):\n        \"\"\"\
        \n        :type matrix: List[List[int]]\n        :rtype: None Do not return\
        \ anything, modify matrix in-place instead.\n        \"\"\"\n        n = len(matrix)\n\
        \        for i in range(n):\n            for j in range(i + 1, n):\n       \
        \         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n        for\
        \ i in range(n):\n            matrix[i].reverse()"
      python3: "class Solution:\n    def rotate(self, matrix: List[List[int]]) -> None:\n\
        \        \"\"\"\n        Do not return anything, modify matrix in-place instead.\n\
        \        \"\"\"\n        n = len(matrix)\n        for i in range(n):\n     \
        \       for j in range(i + 1, n):\n                matrix[i][j], matrix[j][i]\
        \ = matrix[j][i], matrix[i][j]\n        for i in range(n):\n            matrix[i].reverse()"
      c: "void rotate(int** matrix, int matrixSize, int* matrixColSize) {\n    for (int\
        \ i = 0; i < matrixSize; i++) {\n        for (int j = i + 1; j < matrixSize;\
        \ j++) {\n            int temp = matrix[i][j];\n            matrix[i][j] = matrix[j][i];\n\
        \            matrix[j][i] = temp;\n        }\n    }\n    for (int i = 0; i <\
        \ matrixSize; i++) {\n        for (int j = 0; j < matrixSize / 2; j++) {\n \
        \           int temp = matrix[i][j];\n            matrix[i][j] = matrix[i][matrixSize\
        \ - 1 - j];\n            matrix[i][matrixSize - 1 - j] = temp;\n        }\n\
        \    }\n}"
      csharp: "public class Solution {\n    public void Rotate(int[][] matrix) {\n \
        \       int n = matrix.Length;\n        for (int i = 0; i < n; i++) {\n    \
        \        for (int j = i + 1; j < n; j++) {\n                int temp = matrix[i][j];\n\
        \                matrix[i][j] = matrix[j][i];\n                matrix[j][i]\
        \ = temp;\n            }\n        }\n        for (int i = 0; i < n; i++) {\n\
        \            System.Array.Reverse(matrix[i]);\n        }\n    }\n}"
      javascript: "/**\n * @param {number[][]} matrix\n * @return {void} Do not return\
        \ anything, modify matrix in-place instead.\n */\nvar rotate = function(matrix)\
        \ {\n    const n = matrix.length;\n    for (let i = 0; i < n; i++) {\n     \
        \   for (let j = i + 1; j < n; j++) {\n            let temp = matrix[i][j];\n\
        \            matrix[i][j] = matrix[j][i];\n            matrix[j][i] = temp;\n\
        \        }\n    }\n    for (let i = 0; i < n; i++) {\n        matrix[i].reverse();\n\
        \    }\n};"
      typescript: "/**\n Do not return anything, modify matrix in-place instead.\n */\n\
        function rotate(matrix: number[][]): void {\n    const n = matrix.length;\n\
        \    for (let i = 0; i < n; i++) {\n        for (let j = i + 1; j < n; j++)\
        \ {\n            let temp = matrix[i][j];\n            matrix[i][j] = matrix[j][i];\n\
        \            matrix[j][i] = temp;\n        }\n    }\n    for (let i = 0; i <\
        \ n; i++) {\n        matrix[i].reverse();\n    }\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $matrix\n     * @return\
        \ NULL\n     */\n    function rotate(&$matrix) {\n        $n = count($matrix);\n\
        \        for ($i = 0; $i < $n; $i++) {\n            for ($j = $i + 1; $j < $n;\
        \ $j++) {\n                $temp = $matrix[$i][$j];\n                $matrix[$i][$j]\
        \ = $matrix[$j][$i];\n                $matrix[$j][$i] = $temp;\n           \
        \ }\n        }\n        for ($i = 0; $i < $n; $i++) {\n            $matrix[$i]\
        \ = array_reverse($matrix[$i]);\n        }\n    }\n}"
      swift: "class Solution {\n    func rotate(_ matrix: inout [[Int]]) {\n       \
        \ let n = matrix.count\n        for i in 0..<n {\n            for j in i + 1..<n\
        \ {\n                let temp = matrix[i][j]\n                matrix[i][j] =\
        \ matrix[j][i]\n                matrix[j][i] = temp\n            }\n       \
        \ }\n        for i in 0..<n {\n            matrix[i].reverse()\n        }\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun rotate(matrix: Array<IntArray>): Unit {\n \
        \       val n = matrix.size\n        for (i in 0 until n) {\n            for\
        \ (j in i + 1 until n) {\n                val temp = matrix[i][j]\n        \
        \        matrix[i][j] = matrix[j][i]\n                matrix[j][i] = temp\n\
        \            }\n        }\n        for (i in 0 until n) {\n            matrix[i].reverse()\n\
        \        }\n    }\n}"
      dart: "class Solution {\n  void rotate(List<List<int>> matrix) {\n    int n =\
        \ matrix.length;\n    for (int i = 0; i < n; i++) {\n      for (int j = i +\
        \ 1; j < n; j++) {\n        int temp = matrix[i][j];\n        matrix[i][j] =\
        \ matrix[j][i];\n        matrix[j][i] = temp;\n      }\n    }\n    for (int\
        \ i = 0; i < n; i++) {\n      int left = 0;\n      int right = n - 1;\n    \
        \  while (left < right) {\n        int temp = matrix[i][left];\n        matrix[i][left]\
        \ = matrix[i][right];\n        matrix[i][right] = temp;\n        left++;\n \
        \       right--;\n      }\n    }\n  }\n}"
      go: "func rotate(matrix [][]int) {\n    n := len(matrix)\n    for i := 0; i <\
        \ n; i++ {\n        for j := i + 1; j < n; j++ {\n            matrix[i][j],\
        \ matrix[j][i] = matrix[j][i], matrix[i][j]\n        }\n    }\n    for i :=\
        \ 0; i < n; i++ {\n        for j, k := 0, n-1; j < k; j, k = j+1, k-1 {\n  \
        \          matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]\n       \
        \ }\n    }\n}"
      ruby: "# @param {Integer[][]} matrix\n# @return {Void} Do not return anything,\
        \ modify matrix in-place instead.\ndef rotate(matrix)\n    n = matrix.length\n\
        \    (0...n).each do |i|\n        (i + 1...n).each do |j|\n            matrix[i][j],\
        \ matrix[j][i] = matrix[j][i], matrix[i][j]\n        end\n    end\n    matrix.each\
        \ do |row|\n        row.reverse!\n    end\nend"
      scala: "object Solution {\n    def rotate(matrix: Array[Array[Int]]): Unit = {\n\
        \        val n = matrix.length\n        for (i <- 0 until n) {\n           \
        \ for (j <- i + 1 until n) {\n                val temp = matrix(i)(j)\n    \
        \            matrix(i)(j) = matrix(j)(i)\n                matrix(j)(i) = temp\n\
        \            }\n        }\n        for (i <- 0 until n) {\n            val row\
        \ = matrix(i)\n            var left = 0\n            var right = n - 1\n   \
        \         while (left < right) {\n                val temp = row(left)\n   \
        \             row(left) = row(right)\n                row(right) = temp\n  \
        \              left += 1\n                right -= 1\n            }\n      \
        \  }\n    }\n}"
      rust: "impl Solution {\n    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {\n    \
        \    let n = matrix.len();\n        for i in 0..n {\n            for j in i\
        \ + 1..n {\n                let temp = matrix[i][j];\n                matrix[i][j]\
        \ = matrix[j][i];\n                matrix[j][i] = temp;\n            }\n   \
        \     }\n        for i in 0..n {\n            matrix[i].reverse();\n       \
        \ }\n    }\n}"
      racket: "(define/contract (rotate matrix)\n  (-> (vectorof (vectorof exact-integer?))\
        \ void?)\n  (let ([n (vector-length matrix)])\n    (for ([i (in-range n)])\n\
        \      (for ([j (in-range (+ i 1) n)])\n        (let ([temp (vector-ref (vector-ref\
        \ matrix i) j)])\n          (vector-set! (vector-ref matrix i) j (vector-ref\
        \ (vector-ref matrix j) i))\n          (vector-set! (vector-ref matrix j) i\
        \ temp))))\n    (for ([i (in-range n)])\n      (let* ([row (vector-ref matrix\
        \ i)]\n             [len (vector-length row)])\n        (for ([j (in-range (quotient\
        \ len 2))])\n          (let ([temp (vector-ref row j)])\n            (vector-set!\
        \ row j (vector-ref row (- len 1 j)))\n            (vector-set! row (- len 1\
        \ j) temp)))))\n    (void)))"
      erlang: "-spec rotate(Matrix :: [[integer()]]) -> [[integer()]].\nrotate(Matrix)\
        \ ->\n    transpose(lists:reverse(Matrix)).\n\ntranspose([[]|_]) -> [];\ntranspose(Matrix)\
        \ ->\n    [[hd(Row) || Row <- Matrix] | transpose([tl(Row) || Row <- Matrix])]."
      elixir: "defmodule Solution do\n  @spec rotate(matrix :: [[integer]]) :: any\n\
        \  def rotate(matrix) do\n    matrix\n    |> Enum.reverse()\n    |> Enum.zip()\n\
        \    |> Enum.map(&Tuple.to_list/1)\n  end\nend"
    approach: To rotate an $n \times n$ matrix 90 degrees clockwise in-place, the transformation
      can be decomposed into two distinct steps. First, perform a matrix transposition
      by swapping elements across the main diagonal, such that $matrix[i][j]$ is swapped
      with $matrix[j][i]$. This operation effectively converts the rows of the original
      matrix into columns, but in a reflected orientation.
    time_complexity: O(n^2) where $n$ is the number of rows or columns in the matrix.
      Transposing the matrix involves iterating over approximately half of the elements,
      and reversing each row involves iterating over half the elements per row. Each
      cell is visited and swapped a constant number of times, leading to a quadratic
      time complexity relative to $n$.
    space_complexity: O(1) as the rotation is performed entirely in-place. The algorithm
      only uses a few temporary variables for swapping elements and does not allocate
      any additional data structures that scale with the input size.
    elapsed_time: 82.03651237487793
    model: gemini-3-flash-preview
    generated_at: '2026-05-04 02:09:19 '
---

## Problem #48: Rotate Image

**Difficulty:** Medium

**Topics:** Array, Math, Matrix

## Problem Description

<p>You are given an <code>n x n</code> 2D <code>matrix</code> representing an image, rotate the image by <strong>90</strong> degrees (clockwise).</p>

<p>You have to rotate the image <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>, which means you have to modify the input 2D matrix directly. <strong>DO NOT</strong> allocate another 2D matrix and do the rotation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" style="width: 500px; height: 188px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [[7,4,1],[8,5,2],[9,6,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" style="width: 500px; height: 201px;" />
<pre>
<strong>Input:</strong> matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
<strong>Output:</strong> [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>-1000 &lt;= matrix[i][j] &lt;= 1000</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To rotate an $n \times n$ matrix 90 degrees clockwise in-place, the transformation can be decomposed into two distinct steps. First, perform a matrix transposition by swapping elements across the main diagonal, such that $matrix[i][j]$ is swapped with $matrix[j][i]$. This operation effectively converts the rows of the original matrix into columns, but in a reflected orientation.

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
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    for (int i = 0; i < matrixSize; i++) {
        for (int j = i + 1; j < matrixSize; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixSize / 2; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[i][matrixSize - 1 - j];
            matrix[i][matrixSize - 1 - j] = temp;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public void Rotate(int[][] matrix) {
        int n = matrix.Length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            System.Array.Reverse(matrix[i]);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    const n = matrix.length;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    const n = matrix.length;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function rotate(&$matrix) {
        $n = count($matrix);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $temp = $matrix[$i][$j];
                $matrix[$i][$j] = $matrix[$j][$i];
                $matrix[$j][$i] = $temp;
            }
        }
        for ($i = 0; $i < $n; $i++) {
            $matrix[$i] = array_reverse($matrix[$i]);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count
        for i in 0..<n {
            for j in i + 1..<n {
                let temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }
        for i in 0..<n {
            matrix[i].reverse()
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun rotate(matrix: Array<IntArray>): Unit {
        val n = matrix.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }
        for (i in 0 until n) {
            matrix[i].reverse()
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
  void rotate(List<List<int>> matrix) {
    int n = matrix.length;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
      }
    }
    for (int i = 0; i < n; i++) {
      int left = 0;
      int right = n - 1;
      while (left < right) {
        int temp = matrix[i][left];
        matrix[i][left] = matrix[i][right];
        matrix[i][right] = temp;
        left++;
        right--;
      }
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func rotate(matrix [][]int) {
    n := len(matrix)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        }
    }
    for i := 0; i < n; i++ {
        for j, k := 0, n-1; j < k; j, k = j+1, k-1 {
            matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def rotate(matrix)
    n = matrix.length
    (0...n).each do |i|
        (i + 1...n).each do |j|
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        end
    end
    matrix.each do |row|
        row.reverse!
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def rotate(matrix: Array[Array[Int]]): Unit = {
        val n = matrix.length
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                val temp = matrix(i)(j)
                matrix(i)(j) = matrix(j)(i)
                matrix(j)(i) = temp
            }
        }
        for (i <- 0 until n) {
            val row = matrix(i)
            var left = 0
            var right = n - 1
            while (left < right) {
                val temp = row(left)
                row(left) = row(right)
                row(right) = temp
                left += 1
                right -= 1
            }
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
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        for i in 0..n {
            for j in i + 1..n {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for i in 0..n {
            matrix[i].reverse();
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (rotate matrix)
  (-> (vectorof (vectorof exact-integer?)) void?)
  (let ([n (vector-length matrix)])
    (for ([i (in-range n)])
      (for ([j (in-range (+ i 1) n)])
        (let ([temp (vector-ref (vector-ref matrix i) j)])
          (vector-set! (vector-ref matrix i) j (vector-ref (vector-ref matrix j) i))
          (vector-set! (vector-ref matrix j) i temp))))
    (for ([i (in-range n)])
      (let* ([row (vector-ref matrix i)]
             [len (vector-length row)])
        (for ([j (in-range (quotient len 2))])
          (let ([temp (vector-ref row j)])
            (vector-set! row j (vector-ref row (- len 1 j)))
            (vector-set! row (- len 1 j) temp)))))
    (void)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec rotate(Matrix :: [[integer()]]) -> [[integer()]].
rotate(Matrix) ->
    transpose(lists:reverse(Matrix)).

transpose([[]|_]) -> [];
transpose(Matrix) ->
    [[hd(Row) || Row <- Matrix] | transpose([tl(Row) || Row <- Matrix])].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec rotate(matrix :: [[integer]]) :: any
  def rotate(matrix) do
    matrix
    |> Enum.reverse()
    |> Enum.zip()
    |> Enum.map(&Tuple.to_list/1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where $n$ is the number of rows or columns in the matrix. Transposing the matrix involves iterating over approximately half of the elements, and reversing each row involves iterating over half the elements per row. Each cell is visited and swapped a constant number of times, leading to a quadratic time complexity relative to $n$.
- **Space Complexity:** O(1) as the rotation is performed entirely in-place. The algorithm only uses a few temporary variables for swapping elements and does not allocate any additional data structures that scale with the input size.
