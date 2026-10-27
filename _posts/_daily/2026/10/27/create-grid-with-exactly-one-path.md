---
layout: post
title: "Create Grid With Exactly One Path"
date: 2026-10-27 09:00:00 +0900
categories: [LeetCode, Easy]
tags: []
difficulty: Easy
leetcode_url: https://leetcode.com/problems/create-grid-with-exactly-one-path/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<string> createGrid(int m, int n) {\n\
        \        vector<string> grid(m, string(n, '#'));\n        for (int j = 0; j\
        \ < n; ++j) {\n            grid[0][j] = '.';\n        }\n        for (int i\
        \ = 0; i < m; ++i) {\n            grid[i][n - 1] = '.';\n        }\n       \
        \ return grid;\n    }\n};"
      java: "class Solution {\n    public String[] createGrid(int m, int n) {\n    \
        \    char[][] grid = new char[m][n];\n        for (int i = 0; i < m; i++) {\n\
        \            for (int j = 0; j < n; j++) {\n                grid[i][j] = '#';\n\
        \            }\n        }\n        for (int j = 0; j < n; j++) {\n         \
        \   grid[0][j] = '.';\n        }\n        for (int i = 0; i < m; i++) {\n  \
        \          grid[i][n - 1] = '.';\n        }\n        String[] result = new String[m];\n\
        \        for (int i = 0; i < m; i++) {\n            result[i] = new String(grid[i]);\n\
        \        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def createGrid(self, m, n):\n        \"\"\
        \"\n        :type m: int\n        :type n: int\n        :rtype: List[str]\n\
        \        \"\"\"\n        grid = [['#' for _ in range(n)] for _ in range(m)]\n\
        \        for j in range(n):\n            grid[0][j] = '.'\n        for i in\
        \ range(m):\n            grid[i][n - 1] = '.'\n        return [\"\".join(row)\
        \ for row in grid]"
      python3: "class Solution:\n    def createGrid(self, m: int, n: int) -> list[str]:\n\
        \        grid = [['#' for _ in range(n)] for _ in range(m)]\n        for j in\
        \ range(n):\n            grid[0][j] = '.'\n        for i in range(m):\n    \
        \        grid[i][n - 1] = '.'\n        return [\"\".join(row) for row in grid]"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nchar** createGrid(int m, int n, int* returnSize) {\n    *returnSize =\
        \ m;\n    char** grid = (char**)malloc(m * sizeof(char*));\n    for (int i =\
        \ 0; i < m; i++) {\n        grid[i] = (char*)malloc((n + 1) * sizeof(char));\n\
        \        for (int j = 0; j < n; j++) {\n            grid[i][j] = '#';\n    \
        \    }\n        grid[i][n] = '\\0';\n    }\n    for (int j = 0; j < n; j++)\
        \ {\n        grid[0][j] = '.';\n    }\n    for (int i = 0; i < m; i++) {\n \
        \       grid[i][n - 1] = '.';\n    }\n    return grid;\n}"
      csharp: "public class Solution {\n    public string[] CreateGrid(int m, int n)\
        \ {\n        char[][] grid = new char[m][];\n        for (int i = 0; i < m;\
        \ i++) {\n            grid[i] = new char[n];\n            for (int j = 0; j\
        \ < n; j++) {\n                grid[i][j] = '#';\n            }\n        }\n\
        \        for (int j = 0; j < n; j++) {\n            grid[0][j] = '.';\n    \
        \    }\n        for (int i = 0; i < m; i++) {\n            grid[i][n - 1] =\
        \ '.';\n        }\n        string[] result = new string[m];\n        for (int\
        \ i = 0; i < m; i++) {\n            result[i] = new string(grid[i]);\n     \
        \   }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number} m\n * @param {number} n\n * @return {string[]}\n\
        \ */\nvar createGrid = function(m, n) {\n    let grid = Array.from({ length:\
        \ m }, () => Array(n).fill('#'));\n    for (let j = 0; j < n; j++) {\n     \
        \   grid[0][j] = '.';\n    }\n    for (let i = 0; i < m; i++) {\n        grid[i][n\
        \ - 1] = '.';\n    }\n    return grid.map(row => row.join(''));\n};"
      typescript: "function createGrid(m: number, n: number): string[] {\n    const\
        \ result: string[] = [];\n    for (let i = 0; i < m; i++) {\n        let row\
        \ = \"\";\n        for (let j = 0; j < n; j++) {\n            if (i === 0 ||\
        \ j === n - 1) {\n                row += \".\";\n            } else {\n    \
        \            row += \"#\";\n            }\n        }\n        result.push(row);\n\
        \    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $m\n     * @param Integer\
        \ $n\n     * @return String[]\n     */\n    function createGrid($m, $n) {\n\
        \        $result = [];\n        for ($i = 0; $i < $m; $i++) {\n            $row\
        \ = \"\";\n            for ($j = 0; $j < $n; $j++) {\n                if ($i\
        \ == 0 || $j == $n - 1) {\n                    $row .= \".\";\n            \
        \    } else {\n                    $row .= \"#\";\n                }\n     \
        \       }\n            $result[] = $row;\n        }\n        return $result;\n\
        \    }\n}"
      swift: "class Solution {\n    func createGrid(_ m: Int, _ n: Int) -> [String]\
        \ {\n        var result: [String] = []\n        for i in 0..<m {\n         \
        \   var row = \"\"\n            for j in 0..<n {\n                if i == 0\
        \ || j == n - 1 {\n                    row += \".\"\n                } else\
        \ {\n                    row += \"#\"\n                }\n            }\n  \
        \          result.append(row)\n        }\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun createGrid(m: Int, n: Int): Array<String> {\n\
        \        val result = Array(m) { \"\" }\n        for (i in 0 until m) {\n  \
        \          val row = CharArray(n)\n            for (j in 0 until n) {\n    \
        \            if (i == 0 || j == n - 1) {\n                    row[j] = '.'\n\
        \                } else {\n                    row[j] = '#'\n              \
        \  }\n            }\n            result[i] = String(row)\n        }\n      \
        \  return result\n    }\n}"
      dart: "class Solution {\n  List<String> createGrid(int m, int n) {\n    List<String>\
        \ result = [];\n    for (int i = 0; i < m; i++) {\n      String row = \"\";\n\
        \      for (int j = 0; j < n; j++) {\n        if (i == 0 || j == n - 1) {\n\
        \          row += \".\";\n        } else {\n          row += \"#\";\n      \
        \  }\n      }\n      result.add(row);\n    }\n    return result;\n  }\n}"
      go: "func createGrid(m int, n int) []string {\n    grid := make([]string, m)\n\
        \    for i := 0; i < m; i++ {\n        row := make([]byte, n)\n        for j\
        \ := 0; j < n; j++ {\n            if i == 0 || j == n-1 {\n                row[j]\
        \ = '.'\n            } else {\n                row[j] = '#'\n            }\n\
        \        }\n        grid[i] = string(row)\n    }\n    return grid\n}"
      ruby: "# @param {Integer} m\n# @param {Integer} n\n# @return {String[]}\ndef create_grid(m,\
        \ n)\n  (0...m).map do |i|\n    (0...n).map { |j| (i == 0 || j == n - 1) ? \"\
        .\" : \"#\" }.join\n  end\nend"
      scala: "object Solution {\n  def createGrid(m: Int, n: Int): Array[String] = {\n\
        \    Array.tabulate(m) { i =>\n      (0 until n).map { j =>\n        if (i ==\
        \ 0 || j == n - 1) '.' else '#'\n      }.mkString\n    }\n  }\n}"
      rust: "impl Solution {\n    pub fn create_grid(m: i32, n: i32) -> Vec<String>\
        \ {\n        (0..m).map(|i| {\n            (0..n).map(|j| {\n              \
        \  if i == 0 || j == n - 1 { '.' } else { '#' }\n            }).collect::<String>()\n\
        \        }).collect()\n    }\n}"
      racket: "(define/contract (create-grid m n)\n  (-> exact-integer? exact-integer?\
        \ (listof string?))\n  (for/list ([i (in-range m)])\n    (build-string n (lambda\
        \ (j)\n                      (if (or (= i 0) (= j (- n 1)))\n              \
        \            #\\. \n                          #\\#))))\n  )"
      erlang: "-spec create_grid(M :: integer(), N :: integer()) -> [unicode:unicode_binary()].\n\
        create_grid(M, N) ->\n  [list_to_binary([case (I == 0 orelse J == N - 1) of\n\
        \                     true -> $.;\n                     false -> $#\n      \
        \             end || J <- lists:seq(0, N - 1)]) || I <- lists:seq(0, M - 1)]."
      elixir: "defmodule Solution do\n  @spec create_grid(m :: integer, n :: integer)\
        \ :: [String.t]\n  def create_grid(m, n) do\n    Enum.map(0..(m - 1), fn i ->\n\
        \      Enum.map(0..(n - 1), fn j ->\n        if i == 0 or j == n - 1, do: \"\
        .\", else: \"#\"\n      end) |> Enum.join(\"\")\n    end)\n  end\nend"
    approach: 'To create a grid with exactly one path, we can construct a deterministic
      "L-shaped" route that connects the starting cell (0, 0) to the destination (m
      - 1, n - 1). This is achieved by designating every cell in the first row and every
      cell in the last column as free cells (''.'') while filling all other cells with
      obstacles (''#''). This specific layout forces any valid path to move horizontally
      from (0, 0) to the corner at (0, n - 1) and then descend vertically to (m - 1,
      n - 1).


      This construction guarantees that exactly one path exists because, at any cell
      along the route, the movement is restricted to a single valid direction. For cells
      in the first row (except for the last column), the obstacle placed directly below
      them prevents any downward branching. Once the path reaches the last column, no
      rightward movement is possible by definition of the grid boundaries, and only
      downward free cells are available. By blocking all cells outside this L-shaped
      sequence, we eliminate any alternative paths or branching points, ensuring the
      path is unique.'
    time_complexity: O(m * n). The algorithm initializes each of the m * n grid cells
      exactly once. The operations to set the first row and last column to free cells
      are proportional to the dimensions of the grid, resulting in a total time complexity
      that is linear with respect to the total number of cells.
    space_complexity: O(m * n). The space complexity is driven by the storage required
      for the output grid, which contains m * n characters. No additional large auxiliary
      data structures are used during the construction process.
    elapsed_time: 163.71313881874084
    model: gemini-3-flash-preview
    generated_at: '2026-10-27 03:10:40 '
---

## Problem #3963: Create Grid With Exactly One Path

**Difficulty:** Easy

## Problem Description

<p>You are given two integers <code>m</code> and <code>n</code>, representing the number of rows and columns of a grid.</p>

<p>Construct <strong>any</strong> <code>m x n</code> grid consisting only of the characters <code>&#39;.&#39;</code> and <code>&#39;#&#39;</code>, where:</p>

<ul>
	<li><code>&#39;.&#39;</code> represents a free cell.</li>
	<li><code>&#39;#&#39;</code> represents an obstacle cell.</li>
</ul>

<p>A <strong>valid path</strong> is a sequence of free cells that:</p>

<ul>
	<li>Starts at the top-left cell <code>(0, 0)</code>.</li>
	<li>Ends at the bottom-right cell <code>(m - 1, n - 1)</code>.</li>
	<li>Moves only:
	<ul>
		<li>Right, from <code>(i, j)</code> to <code>(i, j + 1)</code>, or</li>
		<li>Down, from <code>(i, j)</code> to <code>(i + 1, j)</code>.</li>
	</ul>
	</li>
</ul>

<p>Return any grid such that there is <strong>exactly one valid path</strong> from the top-left cell to the bottom-right cell.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 2, n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;..#&quot;,&quot;#..&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61005pm.png" style="width: 200px; height: 95px;" /></p>

<p>The only valid path is: <code>(0,0) &rarr; (0,1) &rarr; (1,1) &rarr; (1,2)</code></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 3, n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;..#&quot;,&quot;#..&quot;,&quot;##.&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61129pm.png" style="width: 220px; height: 150px;" /></p>

<p>The only valid path is: <code>(0,0) &rarr; (0,1) &rarr; (1,1) &rarr; (1,2) &rarr; (2,2)</code></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 1, n = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;....&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<p>The only valid path is: <code>(0,0) &rarr; (0,1) &rarr; (0,2) &rarr; (0,3)</code></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 25</code></li>
</ul>


## Hints

1. It is enough to leave one simple route made of free cells and block every other cell.

2. There are many routes to choose from. What is the simplest one you can think of?

3. One possible route: Go right while possible, then go down till you reach the destination.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To create a grid with exactly one path, we can construct a deterministic "L-shaped" route that connects the starting cell (0, 0) to the destination (m - 1, n - 1). This is achieved by designating every cell in the first row and every cell in the last column as free cells ('.') while filling all other cells with obstacles ('#'). This specific layout forces any valid path to move horizontally from (0, 0) to the corner at (0, n - 1) and then descend vertically to (m - 1, n - 1).

This construction guarantees that exactly one path exists because, at any cell along the route, the movement is restricted to a single valid direction. For cells in the first row (except for the last column), the obstacle placed directly below them prevents any downward branching. Once the path reaches the last column, no rightward movement is possible by definition of the grid boundaries, and only downward free cells are available. By blocking all cells outside this L-shaped sequence, we eliminate any alternative paths or branching points, ensuring the path is unique.

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
    vector<string> createGrid(int m, int n) {
        vector<string> grid(m, string(n, '#'));
        for (int j = 0; j < n; ++j) {
            grid[0][j] = '.';
        }
        for (int i = 0; i < m; ++i) {
            grid[i][n - 1] = '.';
        }
        return grid;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String[] createGrid(int m, int n) {
        char[][] grid = new char[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = '#';
            }
        }
        for (int j = 0; j < n; j++) {
            grid[0][j] = '.';
        }
        for (int i = 0; i < m; i++) {
            grid[i][n - 1] = '.';
        }
        String[] result = new String[m];
        for (int i = 0; i < m; i++) {
            result[i] = new String(grid[i]);
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [['#' for _ in range(n)] for _ in range(m)]
        for j in range(n):
            grid[0][j] = '.'
        for i in range(m):
            grid[i][n - 1] = '.'
        return ["".join(row) for row in grid]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]
        for j in range(n):
            grid[0][j] = '.'
        for i in range(m):
            grid[i][n - 1] = '.'
        return ["".join(row) for row in grid]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** createGrid(int m, int n, int* returnSize) {
    *returnSize = m;
    char** grid = (char**)malloc(m * sizeof(char*));
    for (int i = 0; i < m; i++) {
        grid[i] = (char*)malloc((n + 1) * sizeof(char));
        for (int j = 0; j < n; j++) {
            grid[i][j] = '#';
        }
        grid[i][n] = '\0';
    }
    for (int j = 0; j < n; j++) {
        grid[0][j] = '.';
    }
    for (int i = 0; i < m; i++) {
        grid[i][n - 1] = '.';
    }
    return grid;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string[] CreateGrid(int m, int n) {
        char[][] grid = new char[m][];
        for (int i = 0; i < m; i++) {
            grid[i] = new char[n];
            for (int j = 0; j < n; j++) {
                grid[i][j] = '#';
            }
        }
        for (int j = 0; j < n; j++) {
            grid[0][j] = '.';
        }
        for (int i = 0; i < m; i++) {
            grid[i][n - 1] = '.';
        }
        string[] result = new string[m];
        for (int i = 0; i < m; i++) {
            result[i] = new string(grid[i]);
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} m
 * @param {number} n
 * @return {string[]}
 */
var createGrid = function(m, n) {
    let grid = Array.from({ length: m }, () => Array(n).fill('#'));
    for (let j = 0; j < n; j++) {
        grid[0][j] = '.';
    }
    for (let i = 0; i < m; i++) {
        grid[i][n - 1] = '.';
    }
    return grid.map(row => row.join(''));
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function createGrid(m: number, n: number): string[] {
    const result: string[] = [];
    for (let i = 0; i < m; i++) {
        let row = "";
        for (let j = 0; j < n; j++) {
            if (i === 0 || j === n - 1) {
                row += ".";
            } else {
                row += "#";
            }
        }
        result.push(row);
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @return String[]
     */
    function createGrid($m, $n) {
        $result = [];
        for ($i = 0; $i < $m; $i++) {
            $row = "";
            for ($j = 0; $j < $n; $j++) {
                if ($i == 0 || $j == $n - 1) {
                    $row .= ".";
                } else {
                    $row .= "#";
                }
            }
            $result[] = $row;
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func createGrid(_ m: Int, _ n: Int) -> [String] {
        var result: [String] = []
        for i in 0..<m {
            var row = ""
            for j in 0..<n {
                if i == 0 || j == n - 1 {
                    row += "."
                } else {
                    row += "#"
                }
            }
            result.append(row)
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun createGrid(m: Int, n: Int): Array<String> {
        val result = Array(m) { "" }
        for (i in 0 until m) {
            val row = CharArray(n)
            for (j in 0 until n) {
                if (i == 0 || j == n - 1) {
                    row[j] = '.'
                } else {
                    row[j] = '#'
                }
            }
            result[i] = String(row)
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<String> createGrid(int m, int n) {
    List<String> result = [];
    for (int i = 0; i < m; i++) {
      String row = "";
      for (int j = 0; j < n; j++) {
        if (i == 0 || j == n - 1) {
          row += ".";
        } else {
          row += "#";
        }
      }
      result.add(row);
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func createGrid(m int, n int) []string {
    grid := make([]string, m)
    for i := 0; i < m; i++ {
        row := make([]byte, n)
        for j := 0; j < n; j++ {
            if i == 0 || j == n-1 {
                row[j] = '.'
            } else {
                row[j] = '#'
            }
        }
        grid[i] = string(row)
    }
    return grid
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} m
# @param {Integer} n
# @return {String[]}
def create_grid(m, n)
  (0...m).map do |i|
    (0...n).map { |j| (i == 0 || j == n - 1) ? "." : "#" }.join
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def createGrid(m: Int, n: Int): Array[String] = {
    Array.tabulate(m) { i =>
      (0 until n).map { j =>
        if (i == 0 || j == n - 1) '.' else '#'
      }.mkString
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
    pub fn create_grid(m: i32, n: i32) -> Vec<String> {
        (0..m).map(|i| {
            (0..n).map(|j| {
                if i == 0 || j == n - 1 { '.' } else { '#' }
            }).collect::<String>()
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (create-grid m n)
  (-> exact-integer? exact-integer? (listof string?))
  (for/list ([i (in-range m)])
    (build-string n (lambda (j)
                      (if (or (= i 0) (= j (- n 1)))
                          #\. 
                          #\#))))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec create_grid(M :: integer(), N :: integer()) -> [unicode:unicode_binary()].
create_grid(M, N) ->
  [list_to_binary([case (I == 0 orelse J == N - 1) of
                     true -> $.;
                     false -> $#
                   end || J <- lists:seq(0, N - 1)]) || I <- lists:seq(0, M - 1)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec create_grid(m :: integer, n :: integer) :: [String.t]
  def create_grid(m, n) do
    Enum.map(0..(m - 1), fn i ->
      Enum.map(0..(n - 1), fn j ->
        if i == 0 or j == n - 1, do: ".", else: "#"
      end) |> Enum.join("")
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n). The algorithm initializes each of the m * n grid cells exactly once. The operations to set the first row and last column to free cells are proportional to the dimensions of the grid, resulting in a total time complexity that is linear with respect to the total number of cells.
- **Space Complexity:** O(m * n). The space complexity is driven by the storage required for the output grid, which contains m * n characters. No additional large auxiliary data structures are used during the construction process.
