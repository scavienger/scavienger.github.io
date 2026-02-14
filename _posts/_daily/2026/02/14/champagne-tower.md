---
layout: post
title: "Champagne Tower"
date: 2026-02-14 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/champagne-tower/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    double champagneTower(int poured, int query_row,\
        \ int query_glass) {\n        double tower[101][101] = {0.0};\n        tower[0][0]\
        \ = (double)poured;\n        for (int r = 0; r <= query_row; ++r) {\n      \
        \      for (int c = 0; c <= r; ++c) {\n                double excess = (tower[r][c]\
        \ - 1.0) / 2.0;\n                if (excess > 0) {\n                    tower[r\
        \ + 1][c] += excess;\n                    tower[r + 1][c + 1] += excess;\n \
        \               }\n            }\n        }\n        return tower[query_row][query_glass]\
        \ > 1.0 ? 1.0 : tower[query_row][query_glass];\n    }\n};"
      java: "class Solution {\n    public double champagneTower(int poured, int query_row,\
        \ int query_glass) {\n        double[][] tower = new double[102][102];\n   \
        \     tower[0][0] = (double) poured;\n        for (int r = 0; r <= query_row;\
        \ r++) {\n            for (int c = 0; c <= r; c++) {\n                double\
        \ excess = (tower[r][c] - 1.0) / 2.0;\n                if (excess > 0) {\n \
        \                   tower[r + 1][c] += excess;\n                    tower[r\
        \ + 1][c + 1] += excess;\n                }\n            }\n        }\n    \
        \    return Math.min(1.0, tower[query_row][query_glass]);\n    }\n}"
      python: "class Solution(object):\n    def champagneTower(self, poured, query_row,\
        \ query_glass):\n        \"\"\"\n        :type poured: int\n        :type query_row:\
        \ int\n        :type query_glass: int\n        :rtype: float\n        \"\"\"\
        \n        tower = [[0.0] * 101 for _ in range(101)]\n        tower[0][0] = float(poured)\n\
        \        for r in range(query_row + 1):\n            for c in range(r + 1):\n\
        \                excess = (tower[r][c] - 1.0) / 2.0\n                if excess\
        \ > 0:\n                    tower[r + 1][c] += excess\n                    tower[r\
        \ + 1][c + 1] += excess\n        return min(1.0, tower[query_row][query_glass])"
      python3: "class Solution:\n    def champagneTower(self, poured: int, query_row:\
        \ int, query_glass: int) -> float:\n        tower = [[0.0] * 101 for _ in range(101)]\n\
        \        tower[0][0] = float(poured)\n        for r in range(query_row + 1):\n\
        \            for c in range(r + 1):\n                excess = (tower[r][c] -\
        \ 1.0) / 2.0\n                if excess > 0:\n                    tower[r +\
        \ 1][c] += excess\n                    tower[r + 1][c + 1] += excess\n     \
        \   return min(1.0, tower[query_row][query_glass])"
      c: "double champagneTower(int poured, int query_row, int query_glass){\n    double\
        \ tower[101][101] = {0.0};\n    tower[0][0] = (double)poured;\n    for (int\
        \ r = 0; r <= query_row; r++) {\n        for (int c = 0; c <= r; c++) {\n  \
        \          double excess = (tower[r][c] - 1.0) / 2.0;\n            if (excess\
        \ > 0) {\n                tower[r + 1][c] += excess;\n                tower[r\
        \ + 1][c + 1] += excess;\n            }\n        }\n    }\n    return tower[query_row][query_glass]\
        \ > 1.0 ? 1.0 : tower[query_row][query_glass];\n}"
      csharp: "public class Solution {\n    public double ChampagneTower(int poured,\
        \ int query_row, int query_glass) {\n        double[,] tower = new double[102,\
        \ 102];\n        tower[0, 0] = (double)poured;\n        for (int r = 0; r <=\
        \ query_row; r++) {\n            for (int c = 0; c <= r; c++) {\n          \
        \      double excess = (tower[r, c] - 1.0) / 2.0;\n                if (excess\
        \ > 0) {\n                    tower[r + 1, c] += excess;\n                 \
        \   tower[r + 1, c + 1] += excess;\n                }\n            }\n     \
        \   }\n        return tower[query_row, query_glass] > 1.0 ? 1.0 : tower[query_row,\
        \ query_glass];\n    }\n}"
      javascript: "/**\n * @param {number} poured\n * @param {number} query_row\n *\
        \ @param {number} query_glass\n * @return {number}\n */\nvar champagneTower\
        \ = function(poured, query_row, query_glass) {\n    let tower = Array.from({\
        \ length: 101 }, () => new Float64Array(101));\n    tower[0][0] = poured;\n\
        \    for (let r = 0; r <= query_row; r++) {\n        for (let c = 0; c <= r;\
        \ c++) {\n            let excess = (tower[r][c] - 1.0) / 2.0;\n            if\
        \ (excess > 0) {\n                if (r + 1 < 101) {\n                    tower[r\
        \ + 1][c] += excess;\n                    tower[r + 1][c + 1] += excess;\n \
        \               }\n            }\n        }\n    }\n    return Math.min(1, tower[query_row][query_glass]);\n\
        };"
      typescript: "function champagneTower(poured: number, query_row: number, query_glass:\
        \ number): number {\n    const dp: number[][] = Array.from({ length: 102 },\
        \ () => Array(102).fill(0));\n    dp[0][0] = poured;\n    for (let r = 0; r\
        \ <= query_row; r++) {\n        for (let c = 0; c <= r; c++) {\n           \
        \ if (dp[r][c] > 1.0) {\n                const q = (dp[r][c] - 1.0) / 2.0;\n\
        \                dp[r + 1][c] += q;\n                dp[r + 1][c + 1] += q;\n\
        \            }\n        }\n    }\n    const res = dp[query_row][query_glass];\n\
        \    return res > 1.0 ? 1.0 : res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $poured\n     * @param\
        \ Integer $query_row\n     * @param Integer $query_glass\n     * @return Float\n\
        \     */\n    function champagneTower($poured, $query_row, $query_glass) {\n\
        \        $dp = array_fill(0, 102, array_fill(0, 102, 0.0));\n        $dp[0][0]\
        \ = (double)$poured;\n        for ($r = 0; $r <= $query_row; $r++) {\n     \
        \       for ($c = 0; $c <= $r; $c++) {\n                if ($dp[$r][$c] > 1.0)\
        \ {\n                    $q = ($dp[$r][$c] - 1.0) / 2.0;\n                 \
        \   $dp[$r + 1][$c] += $q;\n                    $dp[$r + 1][$c + 1] += $q;\n\
        \                }\n            }\n        }\n        $res = $dp[$query_row][$query_glass];\n\
        \        return $res > 1.0 ? 1.0 : (double)$res;\n    }\n}"
      swift: "class Solution {\n    func champagneTower(_ poured: Int, _ query_row:\
        \ Int, _ query_glass: Int) -> Double {\n        var dp = Array(repeating: Array(repeating:\
        \ 0.0, count: 102), count: 102)\n        dp[0][0] = Double(poured)\n       \
        \ for r in 0...query_row {\n            for c in 0...r {\n                if\
        \ dp[r][c] > 1.0 {\n                    let q = (dp[r][c] - 1.0) / 2.0\n   \
        \                 dp[r + 1][c] += q\n                    dp[r + 1][c + 1] +=\
        \ q\n                }\n            }\n        }\n        let res = dp[query_row][query_glass]\n\
        \        return res > 1.0 ? 1.0 : res\n    }\n}"
      kotlin: "class Solution {\n    fun champagneTower(poured: Int, query_row: Int,\
        \ query_glass: Int): Double {\n        val dp = Array(102) { DoubleArray(102)\
        \ }\n        dp[0][0] = poured.toDouble()\n        for (r in 0..query_row) {\n\
        \            for (c in 0..r) {\n                if (dp[r][c] > 1.0) {\n    \
        \                val q = (dp[r][c] - 1.0) / 2.0\n                    dp[r +\
        \ 1][c] += q\n                    dp[r + 1][c + 1] += q\n                }\n\
        \            }\n        }\n        val res = dp[query_row][query_glass]\n  \
        \      return if (res > 1.0) 1.0 else res\n    }\n}"
      dart: "class Solution {\n  double champagneTower(int poured, int query_row, int\
        \ query_glass) {\n    List<List<double>> dp = List.generate(102, (_) => List.filled(102,\
        \ 0.0));\n    dp[0][0] = poured.toDouble();\n    for (int r = 0; r <= query_row;\
        \ r++) {\n      for (int c = 0; c <= r; c++) {\n        if (dp[r][c] > 1.0)\
        \ {\n          double q = (dp[r][c] - 1.0) / 2.0;\n          dp[r + 1][c] +=\
        \ q;\n          dp[r + 1][c + 1] += q;\n        }\n      }\n    }\n    double\
        \ res = dp[query_row][query_glass];\n    return res > 1.0 ? 1.0 : res;\n  }\n\
        }"
      go: "func champagneTower(poured int, query_row int, query_glass int) float64 {\n\
        \    var dp [102][102]float64\n    dp[0][0] = float64(poured)\n    for r :=\
        \ 0; r <= query_row; r++ {\n        for c := 0; c <= r; c++ {\n            if\
        \ dp[r][c] > 1.0 {\n                q := (dp[r][c] - 1.0) / 2.0\n          \
        \      dp[r+1][c] += q\n                dp[r+1][c+1] += q\n            }\n \
        \       }\n    }\n    res := dp[query_row][query_glass]\n    if res > 1.0 {\n\
        \        return 1.0\n    }\n    return res\n}"
      ruby: "def champagne_tower(poured, query_row, query_glass)\n  res = [poured.to_f]\n\
        \  query_row.times do |r|\n    next_row = Array.new(r + 2, 0.0)\n    res.each_with_index\
        \ do |val, c|\n      if val > 1.0\n        overflow = (val - 1.0) / 2.0\n  \
        \      next_row[c] += overflow\n        next_row[c + 1] += overflow\n      end\n\
        \    end\n    res = next_row\n  end\n  [1.0, res[query_glass]].min\nend"
      scala: "object Solution {\n  def champagneTower(poured: Int, query_row: Int, query_glass:\
        \ Int): Double = {\n    var res = Array(poured.toDouble)\n    for (r <- 0 until\
        \ query_row) {\n      val nextRow = Array.fill(r + 2)(0.0)\n      for (c <-\
        \ 0 to r) {\n        if (res(c) > 1.0) {\n          val overflow = (res(c) -\
        \ 1.0) / 2.0\n          nextRow(c) += overflow\n          nextRow(c + 1) +=\
        \ overflow\n        }\n      }\n      res = nextRow\n    }\n    Math.min(1.0,\
        \ res(query_glass))\n  }\n}"
      rust: "impl Solution {\n    pub fn champagne_tower(poured: i32, query_row: i32,\
        \ query_glass: i32) -> f64 {\n        let qr = query_row as usize;\n       \
        \ let qg = query_glass as usize;\n        let mut row = vec![poured as f64];\n\
        \        for r in 0..qr {\n            let mut next_row = vec![0.0; r + 2];\n\
        \            for (c, &val) in row.iter().enumerate() {\n                if val\
        \ > 1.0 {\n                    let overflow = (val - 1.0) / 2.0;\n         \
        \           next_row[c] += overflow;\n                    next_row[c + 1] +=\
        \ overflow;\n                }\n            }\n            row = next_row;\n\
        \        }\n        row[qg].min(1.0)\n    }\n}"
      racket: "(define (champagne-tower poured query_row query_glass)\n  (let loop ([r\
        \ 0] [row (list (real->double-flonum poured))])\n    (if (= r query_row)\n \
        \       (min 1.0 (list-ref row query_glass))\n        (let* ([overflows (map\
        \ (lambda (x) (max 0.0 (/ (- x 1.0) 2.0))) row)]\n               [left (append\
        \ overflows '(0.0))]\n               [right (cons 0.0 overflows)]\n        \
        \       [next-row (map + left right)])\n          (loop (+ r 1) next-row)))))"
      erlang: "-module(solution).\n-export([champagne_tower/3]).\n\nchampagne_tower(Poured,\
        \ QueryRow, QueryGlass) ->\n    FinalRow = simulate(0, QueryRow, [Poured * 1.0]),\n\
        \    Res = lists:nth(QueryGlass + 1, FinalRow),\n    min_val(1.0, Res).\n\n\
        simulate(CurrentRow, TargetRow, RowValues) when CurrentRow >= TargetRow ->\n\
        \    RowValues;\nsimulate(CurrentRow, TargetRow, RowValues) ->\n    Overflows\
        \ = [max_val(0.0, (X - 1.0) / 2.0) || X <- RowValues],\n    LeftPours = Overflows\
        \ ++ [0.0],\n    RightPours = [0.0] ++ Overflows,\n    NextRow = lists:zipwith(fun(A,\
        \ B) -> A + B end, LeftPours, RightPours),\n    simulate(CurrentRow + 1, TargetRow,\
        \ NextRow).\n\nmin_val(A, B) when A < B -> A;\nmin_val(_, B) -> B.\n\nmax_val(A,\
        \ B) when A > B -> A;\nmax_val(_, B) -> B."
      elixir: "defmodule Solution do\n  @spec champagne_tower(poured :: integer, query_row\
        \ :: integer, query_glass :: integer) :: float\n  def champagne_tower(poured,\
        \ query_row, query_glass) do\n    final_row = \n      if query_row == 0 do\n\
        \        [poured / 1.0]\n      else\n        Enum.reduce(1..query_row, [poured\
        \ / 1.0], fn _, row_values ->\n          overflows = Enum.map(row_values, fn\
        \ x -> max(0.0, (x - 1.0) / 2.0) end)\n          left_pours = overflows ++ [0.0]\n\
        \          right_pours = [0.0] ++ overflows\n          Enum.zip_with(left_pours,\
        \ right_pours, &+/2)\n        end)\n      end\n\n    final_row\n    |> Enum.at(query_glass)\n\
        \    |> Kernel.min(1.0)\n  end\nend"
    approach: 'We simulate the flow of champagne row by row starting from the top glass.
      We initialize a 2D array representing the glasses and place the total amount of
      champagne poured into the glass at (0, 0). For each glass in the pyramid, if its
      content exceeds 1.0 cup, we calculate the excess amount. This excess is then divided
      equally and poured into the two glasses immediately below it in the next row.


      The simulation continues row by row until we reach the target query_row. At each
      step, if glass (r, c) has a value V > 1, the amount (V - 1) / 2 is added to both
      glass (r + 1, c) and glass (r + 1, c + 1). Finally, we return the amount in the
      target glass, capped at 1.0 since a glass cannot hold more than its capacity.
      Using a 101x101 array is sufficient as the problem constraints state the tower
      has at most 100 rows.'
    time_complexity: O(R^2), where R is the number of rows in the pyramid. We iterate
      through each glass in each row up to query_row, which is at most 100.
    space_complexity: O(R^2), where R is the number of rows. We maintain a 2D grid to
      store the volume of liquid in each glass. This can be optimized to O(R) by only
      keeping track of the current and previous rows.
    elapsed_time: 355.0072138309479
    model: gemini-3-flash-preview
    generated_at: '2026-02-14 01:27:16 '
---

## Problem #799: Champagne Tower

**Difficulty:** Medium

**Topics:** Dynamic Programming

## Problem Description

<p>We stack glasses in a pyramid, where the <strong>first</strong> row has <code>1</code> glass, the <strong>second</strong> row has <code>2</code> glasses, and so on until the 100<sup>th</sup> row.&nbsp; Each glass holds one cup&nbsp;of champagne.</p>

<p>Then, some champagne is poured into the first glass at the top.&nbsp; When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.&nbsp; When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.&nbsp; (A glass at the bottom row has its excess champagne fall on the floor.)</p>

<p>For example, after one cup of champagne is poured, the top most glass is full.&nbsp; After two cups of champagne are poured, the two glasses on the second row are half full.&nbsp; After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.&nbsp; After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height: 241px; width: 350px;" /></p>

<p>Now after pouring some non-negative integer cups of champagne, return how full the <code>j<sup>th</sup></code> glass in the <code>i<sup>th</sup></code> row is (both <code>i</code> and <code>j</code> are 0-indexed.)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> poured = 1, query_row = 1, query_glass = 1
<strong>Output:</strong> 0.00000
<strong>Explanation:</strong> We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> poured = 2, query_row = 1, query_glass = 1
<strong>Output:</strong> 0.50000
<strong>Explanation:</strong> We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> poured = 100000009, query_row = 33, query_glass = 17
<strong>Output:</strong> 1.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;=&nbsp;poured &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= query_glass &lt;= query_row&nbsp;&lt; 100</code></li>
</ul>

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We simulate the flow of champagne row by row starting from the top glass. We initialize a 2D array representing the glasses and place the total amount of champagne poured into the glass at (0, 0). For each glass in the pyramid, if its content exceeds 1.0 cup, we calculate the excess amount. This excess is then divided equally and poured into the two glasses immediately below it in the next row.

The simulation continues row by row until we reach the target query_row. At each step, if glass (r, c) has a value V > 1, the amount (V - 1) / 2 is added to both glass (r + 1, c) and glass (r + 1, c + 1). Finally, we return the amount in the target glass, capped at 1.0 since a glass cannot hold more than its capacity. Using a 101x101 array is sufficient as the problem constraints state the tower has at most 100 rows.

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
    double champagneTower(int poured, int query_row, int query_glass) {
        double tower[101][101] = {0.0};
        tower[0][0] = (double)poured;
        for (int r = 0; r <= query_row; ++r) {
            for (int c = 0; c <= r; ++c) {
                double excess = (tower[r][c] - 1.0) / 2.0;
                if (excess > 0) {
                    tower[r + 1][c] += excess;
                    tower[r + 1][c + 1] += excess;
                }
            }
        }
        return tower[query_row][query_glass] > 1.0 ? 1.0 : tower[query_row][query_glass];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] tower = new double[102][102];
        tower[0][0] = (double) poured;
        for (int r = 0; r <= query_row; r++) {
            for (int c = 0; c <= r; c++) {
                double excess = (tower[r][c] - 1.0) / 2.0;
                if (excess > 0) {
                    tower[r + 1][c] += excess;
                    tower[r + 1][c + 1] += excess;
                }
            }
        }
        return Math.min(1.0, tower[query_row][query_glass]);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        tower = [[0.0] * 101 for _ in range(101)]
        tower[0][0] = float(poured)
        for r in range(query_row + 1):
            for c in range(r + 1):
                excess = (tower[r][c] - 1.0) / 2.0
                if excess > 0:
                    tower[r + 1][c] += excess
                    tower[r + 1][c + 1] += excess
        return min(1.0, tower[query_row][query_glass])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * 101 for _ in range(101)]
        tower[0][0] = float(poured)
        for r in range(query_row + 1):
            for c in range(r + 1):
                excess = (tower[r][c] - 1.0) / 2.0
                if excess > 0:
                    tower[r + 1][c] += excess
                    tower[r + 1][c + 1] += excess
        return min(1.0, tower[query_row][query_glass])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
double champagneTower(int poured, int query_row, int query_glass){
    double tower[101][101] = {0.0};
    tower[0][0] = (double)poured;
    for (int r = 0; r <= query_row; r++) {
        for (int c = 0; c <= r; c++) {
            double excess = (tower[r][c] - 1.0) / 2.0;
            if (excess > 0) {
                tower[r + 1][c] += excess;
                tower[r + 1][c + 1] += excess;
            }
        }
    }
    return tower[query_row][query_glass] > 1.0 ? 1.0 : tower[query_row][query_glass];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public double ChampagneTower(int poured, int query_row, int query_glass) {
        double[,] tower = new double[102, 102];
        tower[0, 0] = (double)poured;
        for (int r = 0; r <= query_row; r++) {
            for (int c = 0; c <= r; c++) {
                double excess = (tower[r, c] - 1.0) / 2.0;
                if (excess > 0) {
                    tower[r + 1, c] += excess;
                    tower[r + 1, c + 1] += excess;
                }
            }
        }
        return tower[query_row, query_glass] > 1.0 ? 1.0 : tower[query_row, query_glass];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
var champagneTower = function(poured, query_row, query_glass) {
    let tower = Array.from({ length: 101 }, () => new Float64Array(101));
    tower[0][0] = poured;
    for (let r = 0; r <= query_row; r++) {
        for (let c = 0; c <= r; c++) {
            let excess = (tower[r][c] - 1.0) / 2.0;
            if (excess > 0) {
                if (r + 1 < 101) {
                    tower[r + 1][c] += excess;
                    tower[r + 1][c + 1] += excess;
                }
            }
        }
    }
    return Math.min(1, tower[query_row][query_glass]);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function champagneTower(poured: number, query_row: number, query_glass: number): number {
    const dp: number[][] = Array.from({ length: 102 }, () => Array(102).fill(0));
    dp[0][0] = poured;
    for (let r = 0; r <= query_row; r++) {
        for (let c = 0; c <= r; c++) {
            if (dp[r][c] > 1.0) {
                const q = (dp[r][c] - 1.0) / 2.0;
                dp[r + 1][c] += q;
                dp[r + 1][c + 1] += q;
            }
        }
    }
    const res = dp[query_row][query_glass];
    return res > 1.0 ? 1.0 : res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $poured
     * @param Integer $query_row
     * @param Integer $query_glass
     * @return Float
     */
    function champagneTower($poured, $query_row, $query_glass) {
        $dp = array_fill(0, 102, array_fill(0, 102, 0.0));
        $dp[0][0] = (double)$poured;
        for ($r = 0; $r <= $query_row; $r++) {
            for ($c = 0; $c <= $r; $c++) {
                if ($dp[$r][$c] > 1.0) {
                    $q = ($dp[$r][$c] - 1.0) / 2.0;
                    $dp[$r + 1][$c] += $q;
                    $dp[$r + 1][$c + 1] += $q;
                }
            }
        }
        $res = $dp[$query_row][$query_glass];
        return $res > 1.0 ? 1.0 : (double)$res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func champagneTower(_ poured: Int, _ query_row: Int, _ query_glass: Int) -> Double {
        var dp = Array(repeating: Array(repeating: 0.0, count: 102), count: 102)
        dp[0][0] = Double(poured)
        for r in 0...query_row {
            for c in 0...r {
                if dp[r][c] > 1.0 {
                    let q = (dp[r][c] - 1.0) / 2.0
                    dp[r + 1][c] += q
                    dp[r + 1][c + 1] += q
                }
            }
        }
        let res = dp[query_row][query_glass]
        return res > 1.0 ? 1.0 : res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun champagneTower(poured: Int, query_row: Int, query_glass: Int): Double {
        val dp = Array(102) { DoubleArray(102) }
        dp[0][0] = poured.toDouble()
        for (r in 0..query_row) {
            for (c in 0..r) {
                if (dp[r][c] > 1.0) {
                    val q = (dp[r][c] - 1.0) / 2.0
                    dp[r + 1][c] += q
                    dp[r + 1][c + 1] += q
                }
            }
        }
        val res = dp[query_row][query_glass]
        return if (res > 1.0) 1.0 else res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  double champagneTower(int poured, int query_row, int query_glass) {
    List<List<double>> dp = List.generate(102, (_) => List.filled(102, 0.0));
    dp[0][0] = poured.toDouble();
    for (int r = 0; r <= query_row; r++) {
      for (int c = 0; c <= r; c++) {
        if (dp[r][c] > 1.0) {
          double q = (dp[r][c] - 1.0) / 2.0;
          dp[r + 1][c] += q;
          dp[r + 1][c + 1] += q;
        }
      }
    }
    double res = dp[query_row][query_glass];
    return res > 1.0 ? 1.0 : res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func champagneTower(poured int, query_row int, query_glass int) float64 {
    var dp [102][102]float64
    dp[0][0] = float64(poured)
    for r := 0; r <= query_row; r++ {
        for c := 0; c <= r; c++ {
            if dp[r][c] > 1.0 {
                q := (dp[r][c] - 1.0) / 2.0
                dp[r+1][c] += q
                dp[r+1][c+1] += q
            }
        }
    }
    res := dp[query_row][query_glass]
    if res > 1.0 {
        return 1.0
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def champagne_tower(poured, query_row, query_glass)
  res = [poured.to_f]
  query_row.times do |r|
    next_row = Array.new(r + 2, 0.0)
    res.each_with_index do |val, c|
      if val > 1.0
        overflow = (val - 1.0) / 2.0
        next_row[c] += overflow
        next_row[c + 1] += overflow
      end
    end
    res = next_row
  end
  [1.0, res[query_glass]].min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def champagneTower(poured: Int, query_row: Int, query_glass: Int): Double = {
    var res = Array(poured.toDouble)
    for (r <- 0 until query_row) {
      val nextRow = Array.fill(r + 2)(0.0)
      for (c <- 0 to r) {
        if (res(c) > 1.0) {
          val overflow = (res(c) - 1.0) / 2.0
          nextRow(c) += overflow
          nextRow(c + 1) += overflow
        }
      }
      res = nextRow
    }
    Math.min(1.0, res(query_glass))
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let qr = query_row as usize;
        let qg = query_glass as usize;
        let mut row = vec![poured as f64];
        for r in 0..qr {
            let mut next_row = vec![0.0; r + 2];
            for (c, &val) in row.iter().enumerate() {
                if val > 1.0 {
                    let overflow = (val - 1.0) / 2.0;
                    next_row[c] += overflow;
                    next_row[c + 1] += overflow;
                }
            }
            row = next_row;
        }
        row[qg].min(1.0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (champagne-tower poured query_row query_glass)
  (let loop ([r 0] [row (list (real->double-flonum poured))])
    (if (= r query_row)
        (min 1.0 (list-ref row query_glass))
        (let* ([overflows (map (lambda (x) (max 0.0 (/ (- x 1.0) 2.0))) row)]
               [left (append overflows '(0.0))]
               [right (cons 0.0 overflows)]
               [next-row (map + left right)])
          (loop (+ r 1) next-row)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([champagne_tower/3]).

champagne_tower(Poured, QueryRow, QueryGlass) ->
    FinalRow = simulate(0, QueryRow, [Poured * 1.0]),
    Res = lists:nth(QueryGlass + 1, FinalRow),
    min_val(1.0, Res).

simulate(CurrentRow, TargetRow, RowValues) when CurrentRow >= TargetRow ->
    RowValues;
simulate(CurrentRow, TargetRow, RowValues) ->
    Overflows = [max_val(0.0, (X - 1.0) / 2.0) || X <- RowValues],
    LeftPours = Overflows ++ [0.0],
    RightPours = [0.0] ++ Overflows,
    NextRow = lists:zipwith(fun(A, B) -> A + B end, LeftPours, RightPours),
    simulate(CurrentRow + 1, TargetRow, NextRow).

min_val(A, B) when A < B -> A;
min_val(_, B) -> B.

max_val(A, B) when A > B -> A;
max_val(_, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec champagne_tower(poured :: integer, query_row :: integer, query_glass :: integer) :: float
  def champagne_tower(poured, query_row, query_glass) do
    final_row = 
      if query_row == 0 do
        [poured / 1.0]
      else
        Enum.reduce(1..query_row, [poured / 1.0], fn _, row_values ->
          overflows = Enum.map(row_values, fn x -> max(0.0, (x - 1.0) / 2.0) end)
          left_pours = overflows ++ [0.0]
          right_pours = [0.0] ++ overflows
          Enum.zip_with(left_pours, right_pours, &+/2)
        end)
      end

    final_row
    |> Enum.at(query_glass)
    |> Kernel.min(1.0)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(R^2), where R is the number of rows in the pyramid. We iterate through each glass in each row up to query_row, which is at most 100.
- **Space Complexity:** O(R^2), where R is the number of rows. We maintain a 2D grid to store the volume of liquid in each glass. This can be optimized to O(R) by only keeping track of the current and previous rows.
