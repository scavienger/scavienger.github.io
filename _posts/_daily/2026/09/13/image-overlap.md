---
layout: post
title: "Image Overlap"
date: 2026-09-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/image-overlap/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      java: '// Generation failed for Java

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python: '// Generation failed for Python

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python3: '// Generation failed for Python3

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      c: '// Generation failed for C

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      csharp: "public class Solution {\n    public int LargestOverlap(int[][] img1,\
        \ int[][] img2) {\n        int n = img1.Length;\n        var ones1 = new System.Collections.Generic.List<(int,\
        \ int)>();\n        var ones2 = new System.Collections.Generic.List<(int, int)>();\n\
        \n        for (int r = 0; r < n; r++) {\n            for (int c = 0; c < n;\
        \ c++) {\n                if (img1[r][c] == 1) ones1.Add((r, c));\n        \
        \        if (img2[r][c] == 1) ones2.Add((r, c));\n            }\n        }\n\
        \n        var counts = new System.Collections.Generic.Dictionary<int, int>();\n\
        \        int maxOverlap = 0;\n\n        foreach (var p1 in ones1) {\n      \
        \      foreach (var p2 in ones2) {\n                int dr = p2.Item1 - p1.Item1;\n\
        \                int dc = p2.Item2 - p1.Item2;\n                int key = (dr\
        \ + n) * 100 + (dc + n);\n                if (!counts.ContainsKey(key)) counts[key]\
        \ = 0;\n                counts[key]++;\n                maxOverlap = Math.Max(maxOverlap,\
        \ counts[key]);\n            }\n        }\n\n        return maxOverlap;\n  \
        \  }\n}"
      javascript: "/**\n * @param {number[][]} img1\n * @param {number[][]} img2\n *\
        \ @return {number}\n */\nvar largestOverlap = function(img1, img2) {\n    const\
        \ n = img1.length;\n    const ones1 = [];\n    const ones2 = [];\n\n    for\
        \ (let r = 0; r < n; r++) {\n        for (let c = 0; c < n; c++) {\n       \
        \     if (img1[r][c] === 1) ones1.push([r, c]);\n            if (img2[r][c]\
        \ === 1) ones2.push([r, c]);\n        }\n    }\n\n    const counts = new Map();\n\
        \    let maxOverlap = 0;\n\n    for (const [r1, c1] of ones1) {\n        for\
        \ (const [r2, c2] of ones2) {\n            const dr = r2 - r1;\n           \
        \ const dc = c2 - c1;\n            const key = `${dr},${dc}`;\n            const\
        \ current = (counts.get(key) || 0) + 1;\n            counts.set(key, current);\n\
        \            if (current > maxOverlap) maxOverlap = current;\n        }\n  \
        \  }\n\n    return maxOverlap;\n};"
      typescript: "function largestOverlap(img1: number[][], img2: number[][]): number\
        \ {\n    const n = img1.length;\n    const ones1: [number, number][] = [];\n\
        \    const ones2: [number, number][] = [];\n\n    for (let r = 0; r < n; r++)\
        \ {\n        for (let c = 0; c < n; c++) {\n            if (img1[r][c] === 1)\
        \ ones1.push([r, c]);\n            if (img2[r][c] === 1) ones2.push([r, c]);\n\
        \        }\n    }\n\n    const counts = new Map<string, number>();\n    let\
        \ maxOverlap = 0;\n\n    for (const [r1, c1] of ones1) {\n        for (const\
        \ [r2, c2] of ones2) {\n            const dr = r2 - r1;\n            const dc\
        \ = c2 - c1;\n            const key = `${dr},${dc}`;\n            const current\
        \ = (counts.get(key) || 0) + 1;\n            counts.set(key, current);\n   \
        \         if (current > maxOverlap) maxOverlap = current;\n        }\n    }\n\
        \n    return maxOverlap;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $img1\n     * @param\
        \ Integer[][] $img2\n     * @return Integer\n     */\n    function largestOverlap($img1,\
        \ $img2) {\n        $n = count($img1);\n        $ones1 = [];\n        $ones2\
        \ = [];\n\n        for ($r = 0; $r < $n; $r++) {\n            for ($c = 0; $c\
        \ < $n; $c++) {\n                if ($img1[$r][$c] == 1) $ones1[] = [$r, $c];\n\
        \                if ($img2[$r][$c] == 1) $ones2[] = [$r, $c];\n            }\n\
        \        }\n\n        $counts = [];\n        $maxOverlap = 0;\n\n        foreach\
        \ ($ones1 as $p1) {\n            foreach ($ones2 as $p2) {\n               \
        \ $dr = $p2[0] - $p1[0];\n                $dc = $p2[1] - $p1[1];\n         \
        \       $key = \"$dr,$dc\";\n                if (!isset($counts[$key])) {\n\
        \                    $counts[$key] = 0;\n                }\n               \
        \ $counts[$key]++;\n                if ($counts[$key] > $maxOverlap) {\n   \
        \                 $maxOverlap = $counts[$key];\n                }\n        \
        \    }\n        }\n\n        return $maxOverlap;\n    }\n}"
      swift: "class Solution {\n    func largestOverlap(_ img1: [[Int]], _ img2: [[Int]])\
        \ -> Int {\n        let n = img1.count\n        var ones1 = [(Int, Int)]()\n\
        \        var ones2 = [(Int, Int)]()\n\n        for r in 0..<n {\n          \
        \  for c in 0..<n {\n                if img1[r][c] == 1 { ones1.append((r, c))\
        \ }\n                if img2[r][c] == 1 { ones2.append((r, c)) }\n         \
        \   }\n        }\n\n        var counts = [String: Int]()\n        var maxOverlap\
        \ = 0\n\n        for p1 in ones1 {\n            for p2 in ones2 {\n        \
        \        let dr = p2.0 - p1.0\n                let dc = p2.1 - p1.1\n      \
        \          let key = \"\\(dr),\\(dc)\"\n                let currentCount = (counts[key]\
        \ ?? 0) + 1\n                counts[key] = currentCount\n                maxOverlap\
        \ = max(maxOverlap, currentCount)\n            }\n        }\n\n        return\
        \ maxOverlap\n    }\n}"
      kotlin: '// Generation failed for Kotlin

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      dart: '// Generation failed for Dart

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      go: '// Generation failed for Go

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      ruby: '// Generation failed for Ruby

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      scala: '// Generation failed for Scala

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn largest_overlap(img1:\
        \ Vec<Vec<i32>>, img2: Vec<Vec<i32>>) -> i32 {\n        let n = img1.len();\n\
        \        let mut points1 = Vec::new();\n        let mut points2 = Vec::new();\n\
        \n        for r in 0..n {\n            for c in 0..n {\n                if img1[r][c]\
        \ == 1 {\n                    points1.push((r as i32, c as i32));\n        \
        \        }\n                if img2[r][c] == 1 {\n                    points2.push((r\
        \ as i32, c as i32));\n                }\n            }\n        }\n\n     \
        \   let mut counts: HashMap<(i32, i32), i32> = HashMap::new();\n        let\
        \ mut max_overlap = 0;\n\n        for p1 in &points1 {\n            for p2 in\
        \ &points2 {\n                let dr = p2.0 - p1.0;\n                let dc\
        \ = p2.1 - p1.1;\n                let count = counts.entry((dr, dc)).or_insert(0);\n\
        \                *count += 1;\n                if *count > max_overlap {\n \
        \                   max_overlap = *count;\n                }\n            }\n\
        \        }\n\n        max_overlap\n    }\n}"
      racket: "(define/contract (largest-overlap img1 img2)\n  (-> (listof (listof exact-integer?))\
        \ (listof (listof exact-integer?)) exact-integer?)\n  (let* ([n (length img1)]\n\
        \         [get-points (lambda (img)\n                       (for*/list ([r (in-range\
        \ n)]\n                                   [c (in-range n)]\n               \
        \                    #:when (= (list-ref (list-ref img r) c) 1))\n         \
        \                (cons r c)))]\n         [points1 (get-points img1)]\n     \
        \    [points2 (get-points img2)]\n         [counts (make-hash)])\n    (for*\
        \ ([p1 points1]\n           [p2 points2])\n      (let* ([dr (- (car p2) (car\
        \ p1))]\n             [dc (- (cdr p2) (cdr p1))]\n             [key (cons dr\
        \ dc)])\n        (hash-set! counts key (+ 1 (hash-ref counts key 0)))))\n  \
        \  (foldl max 0 (hash-values counts))))"
      erlang: "-spec largest_overlap(Img1 :: [[integer()]], Img2 :: [[integer()]]) ->\
        \ integer().\nlargest_overlap(Img1, Img2) ->\n    Points1 = get_points(Img1),\n\
        \    Points2 = get_points(Img2),\n    Counts = calculate_counts(Points1, Points2,\
        \ #{}),\n    lists:foldl(fun(V, Acc) -> max(V, Acc) end, 0, maps:values(Counts)).\n\
        \nget_points(Img) ->\n    N = length(Img),\n    Indices = lists:seq(0, N - 1),\n\
        \    lists:flatmap(fun({R, Row}) ->\n        RowWithIdx = lists:zip(lists:seq(0,\
        \ length(Row) - 1), Row),\n        [{R, C} || {C, 1} <- RowWithIdx]\n    end,\
        \ lists:zip(Indices, Img)).\n\ncalculate_counts([], _Points2, Map) -> \n   \
        \ Map;\ncalculate_counts([{R1, C1} | T1], Points2, Map) ->\n    NewMap = lists:foldl(fun({R2,\
        \ C2}, AccMap) ->\n        Key = {R2 - R1, C2 - C1},\n        maps:put(Key,\
        \ maps:get(Key, AccMap, 0) + 1, AccMap)\n    end, Map, Points2),\n    calculate_counts(T1,\
        \ Points2, NewMap)."
      elixir: "defmodule Solution do\n  @spec largest_overlap(img1 :: [[integer]], img2\
        \ :: [[integer]]) :: integer\n  def largest_overlap(img1, img2) do\n    points1\
        \ = get_points(img1)\n    points2 = get_points(img2)\n\n    counts = for {r1,\
        \ c1} <- points1, {r2, c2} <- points2, reduce: %{} do\n      acc ->\n      \
        \  key = {r2 - r1, c2 - c1}\n        Map.update(acc, key, 1, &(&1 + 1))\n  \
        \  end\n\n    if map_size(counts) == 0 do\n      0\n    else\n      counts |>\
        \ Map.values() |> Enum.max()\n    end\n  end\n\n  defp get_points(img) do\n\
        \    for {row, r} <- Enum.with_index(img),\n        {1, c} <- Enum.with_index(row)\
        \ do\n      {r, c}\n    end\n  end\nend"
    approach: The algorithm identifies the coordinates of every cell containing a 1
      in both matrices and stores them in two separate lists. Since the problem asks
      for the maximum number of overlapping 1s after a translation, we can iterate through
      every possible pair of 1s—one from img1 and one from img2. For each pair at coordinates
      (r1, c1) and (r2, c2), we calculate the translation vector required to move (r1,
      c1) onto (r2, c2), which is (r2 - r1, c2 - c1).
    time_complexity: O(N^4) where N is the side length of the square matrix. In the
      worst case, both images are filled with 1s, leading to N^2 coordinates in each
      list. The nested loop comparing every pair results in (N^2) * (N^2) = N^4 operations.
      With N <= 30, this complexity is well within limits.
    space_complexity: O(N^2) to store the coordinates of cells containing 1s. In the
      worst case, there are N^2 such coordinates for each image. Additionally, the hash
      map used to store the frequency of translation vectors can contain at most (2N-1)^2
      entries.
    elapsed_time: 881.4262316226959
    model: gemini-3-flash-preview
    generated_at: '2026-09-13 03:08:50 '
---

## Problem #835: Image Overlap

**Difficulty:** Medium

**Topics:** Array, Matrix

## Problem Description

<p>You are given two images, <code>img1</code> and <code>img2</code>, represented as binary, square matrices of size <code>n x n</code>. A binary matrix has only <code>0</code>s and <code>1</code>s as values.</p>

<p>We <strong>translate</strong> one image however we choose by sliding all the <code>1</code> bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the <strong>overlap</strong> by counting the number of positions that have a <code>1</code> in <strong>both</strong> images.</p>

<p>Note also that a translation does <strong>not</strong> include any kind of rotation. Any <code>1</code> bits that are translated outside of the matrix borders are erased.</p>

<p>Return <em>the largest possible overlap</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg" style="width: 450px; height: 231px;" />
<pre>
<strong>Input:</strong> img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We translate img1 to right by 1 unit and down by 1 unit.
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg" style="width: 450px; height: 105px;" />
The number of positions that have a 1 in both images is 3 (shown in red).
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg" style="width: 450px; height: 231px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> img1 = [[1]], img2 = [[1]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> img1 = [[0]], img2 = [[0]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == img1.length == img1[i].length</code></li>
	<li><code>n == img2.length == img2[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 30</code></li>
	<li><code>img1[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>img2[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm identifies the coordinates of every cell containing a 1 in both matrices and stores them in two separate lists. Since the problem asks for the maximum number of overlapping 1s after a translation, we can iterate through every possible pair of 1s—one from img1 and one from img2. For each pair at coordinates (r1, c1) and (r2, c2), we calculate the translation vector required to move (r1, c1) onto (r2, c2), which is (r2 - r1, c2 - c1).

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
// Generation failed for C++
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LargestOverlap(int[][] img1, int[][] img2) {
        int n = img1.Length;
        var ones1 = new System.Collections.Generic.List<(int, int)>();
        var ones2 = new System.Collections.Generic.List<(int, int)>();

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (img1[r][c] == 1) ones1.Add((r, c));
                if (img2[r][c] == 1) ones2.Add((r, c));
            }
        }

        var counts = new System.Collections.Generic.Dictionary<int, int>();
        int maxOverlap = 0;

        foreach (var p1 in ones1) {
            foreach (var p2 in ones2) {
                int dr = p2.Item1 - p1.Item1;
                int dc = p2.Item2 - p1.Item2;
                int key = (dr + n) * 100 + (dc + n);
                if (!counts.ContainsKey(key)) counts[key] = 0;
                counts[key]++;
                maxOverlap = Math.Max(maxOverlap, counts[key]);
            }
        }

        return maxOverlap;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} img1
 * @param {number[][]} img2
 * @return {number}
 */
var largestOverlap = function(img1, img2) {
    const n = img1.length;
    const ones1 = [];
    const ones2 = [];

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            if (img1[r][c] === 1) ones1.push([r, c]);
            if (img2[r][c] === 1) ones2.push([r, c]);
        }
    }

    const counts = new Map();
    let maxOverlap = 0;

    for (const [r1, c1] of ones1) {
        for (const [r2, c2] of ones2) {
            const dr = r2 - r1;
            const dc = c2 - c1;
            const key = `${dr},${dc}`;
            const current = (counts.get(key) || 0) + 1;
            counts.set(key, current);
            if (current > maxOverlap) maxOverlap = current;
        }
    }

    return maxOverlap;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestOverlap(img1: number[][], img2: number[][]): number {
    const n = img1.length;
    const ones1: [number, number][] = [];
    const ones2: [number, number][] = [];

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            if (img1[r][c] === 1) ones1.push([r, c]);
            if (img2[r][c] === 1) ones2.push([r, c]);
        }
    }

    const counts = new Map<string, number>();
    let maxOverlap = 0;

    for (const [r1, c1] of ones1) {
        for (const [r2, c2] of ones2) {
            const dr = r2 - r1;
            const dc = c2 - c1;
            const key = `${dr},${dc}`;
            const current = (counts.get(key) || 0) + 1;
            counts.set(key, current);
            if (current > maxOverlap) maxOverlap = current;
        }
    }

    return maxOverlap;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $img1
     * @param Integer[][] $img2
     * @return Integer
     */
    function largestOverlap($img1, $img2) {
        $n = count($img1);
        $ones1 = [];
        $ones2 = [];

        for ($r = 0; $r < $n; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($img1[$r][$c] == 1) $ones1[] = [$r, $c];
                if ($img2[$r][$c] == 1) $ones2[] = [$r, $c];
            }
        }

        $counts = [];
        $maxOverlap = 0;

        foreach ($ones1 as $p1) {
            foreach ($ones2 as $p2) {
                $dr = $p2[0] - $p1[0];
                $dc = $p2[1] - $p1[1];
                $key = "$dr,$dc";
                if (!isset($counts[$key])) {
                    $counts[$key] = 0;
                }
                $counts[$key]++;
                if ($counts[$key] > $maxOverlap) {
                    $maxOverlap = $counts[$key];
                }
            }
        }

        return $maxOverlap;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestOverlap(_ img1: [[Int]], _ img2: [[Int]]) -> Int {
        let n = img1.count
        var ones1 = [(Int, Int)]()
        var ones2 = [(Int, Int)]()

        for r in 0..<n {
            for c in 0..<n {
                if img1[r][c] == 1 { ones1.append((r, c)) }
                if img2[r][c] == 1 { ones2.append((r, c)) }
            }
        }

        var counts = [String: Int]()
        var maxOverlap = 0

        for p1 in ones1 {
            for p2 in ones2 {
                let dr = p2.0 - p1.0
                let dc = p2.1 - p1.1
                let key = "\(dr),\(dc)"
                let currentCount = (counts[key] ?? 0) + 1
                counts[key] = currentCount
                maxOverlap = max(maxOverlap, currentCount)
            }
        }

        return maxOverlap
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

impl Solution {
    pub fn largest_overlap(img1: Vec<Vec<i32>>, img2: Vec<Vec<i32>>) -> i32 {
        let n = img1.len();
        let mut points1 = Vec::new();
        let mut points2 = Vec::new();

        for r in 0..n {
            for c in 0..n {
                if img1[r][c] == 1 {
                    points1.push((r as i32, c as i32));
                }
                if img2[r][c] == 1 {
                    points2.push((r as i32, c as i32));
                }
            }
        }

        let mut counts: HashMap<(i32, i32), i32> = HashMap::new();
        let mut max_overlap = 0;

        for p1 in &points1 {
            for p2 in &points2 {
                let dr = p2.0 - p1.0;
                let dc = p2.1 - p1.1;
                let count = counts.entry((dr, dc)).or_insert(0);
                *count += 1;
                if *count > max_overlap {
                    max_overlap = *count;
                }
            }
        }

        max_overlap
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (largest-overlap img1 img2)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length img1)]
         [get-points (lambda (img)
                       (for*/list ([r (in-range n)]
                                   [c (in-range n)]
                                   #:when (= (list-ref (list-ref img r) c) 1))
                         (cons r c)))]
         [points1 (get-points img1)]
         [points2 (get-points img2)]
         [counts (make-hash)])
    (for* ([p1 points1]
           [p2 points2])
      (let* ([dr (- (car p2) (car p1))]
             [dc (- (cdr p2) (cdr p1))]
             [key (cons dr dc)])
        (hash-set! counts key (+ 1 (hash-ref counts key 0)))))
    (foldl max 0 (hash-values counts))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec largest_overlap(Img1 :: [[integer()]], Img2 :: [[integer()]]) -> integer().
largest_overlap(Img1, Img2) ->
    Points1 = get_points(Img1),
    Points2 = get_points(Img2),
    Counts = calculate_counts(Points1, Points2, #{}),
    lists:foldl(fun(V, Acc) -> max(V, Acc) end, 0, maps:values(Counts)).

get_points(Img) ->
    N = length(Img),
    Indices = lists:seq(0, N - 1),
    lists:flatmap(fun({R, Row}) ->
        RowWithIdx = lists:zip(lists:seq(0, length(Row) - 1), Row),
        [{R, C} || {C, 1} <- RowWithIdx]
    end, lists:zip(Indices, Img)).

calculate_counts([], _Points2, Map) -> 
    Map;
calculate_counts([{R1, C1} | T1], Points2, Map) ->
    NewMap = lists:foldl(fun({R2, C2}, AccMap) ->
        Key = {R2 - R1, C2 - C1},
        maps:put(Key, maps:get(Key, AccMap, 0) + 1, AccMap)
    end, Map, Points2),
    calculate_counts(T1, Points2, NewMap).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_overlap(img1 :: [[integer]], img2 :: [[integer]]) :: integer
  def largest_overlap(img1, img2) do
    points1 = get_points(img1)
    points2 = get_points(img2)

    counts = for {r1, c1} <- points1, {r2, c2} <- points2, reduce: %{} do
      acc ->
        key = {r2 - r1, c2 - c1}
        Map.update(acc, key, 1, &(&1 + 1))
    end

    if map_size(counts) == 0 do
      0
    else
      counts |> Map.values() |> Enum.max()
    end
  end

  defp get_points(img) do
    for {row, r} <- Enum.with_index(img),
        {1, c} <- Enum.with_index(row) do
      {r, c}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^4) where N is the side length of the square matrix. In the worst case, both images are filled with 1s, leading to N^2 coordinates in each list. The nested loop comparing every pair results in (N^2) * (N^2) = N^4 operations. With N <= 30, this complexity is well within limits.
- **Space Complexity:** O(N^2) to store the coordinates of cells containing 1s. In the worst case, there are N^2 such coordinates for each image. Additionally, the hash map used to store the frequency of translation vectors can contain at most (2N-1)^2 entries.
