---
layout: post
title: "Increment Submatrices by One"
date: 2025-11-14 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/increment-submatrices-by-one/
---

## Problem #2536: Increment Submatrices by One

**Difficulty:** Medium

**Topics:** Array, Matrix, Prefix Sum

## Problem Description

You are given a positive integer `n`, indicating that we initially have an `n x n` **0-indexed** integer matrix `mat` filled with zeroes.

You are also given a 2D integer array `query`. For each `query[i] = [row1i, col1i, row2i, col2i]`, you should do the following operation:

  * Add `1` to **every element** in the submatrix with the **top left** corner `(row1i, col1i)` and the **bottom right** corner `(row2i, col2i)`. That is, add `1` to `mat[x][y]` for all `row1i <= x <= row2i` and `col1i <= y <= col2i`.

Return _the matrix_ `mat` _after performing every query._

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/11/24/p2example11.png)

``` Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]] Output: [[1,1,0],[1,2,1],[0,1,1]] Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query. \- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2). \- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1). ``` 

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/11/24/p2example22.png)

``` Input: n = 2, queries = [[0,0,1,1]] Output: [[1,1],[1,1]] Explanation: The diagram above shows the initial matrix and the matrix after the first query. \- In the first query we add 1 to every element in the matrix. ``` 

**Constraints:**

```

{% raw %}
**Input:** n = 3, queries = [[1,1,2,2],[0,0,1,1]]
**Output:** [[1,1,0],[1,2,1],[0,1,1]]
{% endraw %}
**Explanation:** The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

```

### Illustrations

![](https://assets.leetcode.com/uploads/2022/11/24/p2example11.png)

![](https://assets.leetcode.com/uploads/2022/11/24/p2example22.png)

## Hints

{% raw %}
**Input:** n = 2, queries = [[0,0,1,1]]
**Output:** [[1,1],[1,1]]
{% endraw %}
**Explanation:** The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.

2. For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].

3. After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1].

## ⚡ AI-Generated Solution (llama-3.3-70b-versatile)

### Approach

The approach to this problem is to use a prefix sum array to store the cumulative sum of the elements in each row. We iterate over each query and update the prefix sum array accordingly. After all queries have been processed, we update each row in the matrix using the prefix sum array.

### Code

<div class="code-tabs">
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
class Solution {
       public:
           vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
               vector<vector<int>> mat(n, vector<int>(n, 0));
               for (auto& query : queries) {
                   int row1 = query[0];
                   int col1 = query[1];
                   int row2 = query[2];
                   int col2 = query[3];
                   for (int i = row1; i <= row2; i++) {
                       mat[i][col1]++;
                       if (col2 + 1 < n) {
                           mat[i][col2 + 1]--;
                       }
                   }
               }
               for (int i = 0; i < n; i++) {
                   for (int j = 1; j < n; j++) {
                       mat[i][j] += mat[i][j - 1];
                   }
               }
               return mat;
           }
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
           public int[][] rangeAddQueries(int n, int[][] queries) {
               int[][] mat = new int[n][n];
               for (int[] query : queries) {
                   int row1 = query[0];
                   int col1 = query[1];
                   int row2 = query[2];
                   int col2 = query[3];
                   for (int i = row1; i <= row2; i++) {
                       mat[i][col1]++;
                       if (col2 + 1 < n) {
                           mat[i][col2 + 1]--;
                       }
                   }
               }
               for (int i = 0; i < n; i++) {
                   for (int j = 1; j < n; j++) {
                       mat[i][j] += mat[i][j - 1];
                   }
               }
               return mat;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
           def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
               mat = [[0] * n for _ in range(n)]
               for query in queries:
                   row1, col1, row2, col2 = query
                   for i in range(row1, row2 + 1):
                       mat[i][col1] += 1
                       if col2 + 1 < n:
                           mat[i][col2 + 1] -= 1
               for i in range(n):
                   for j in range(1, n):
                       mat[i][j] += mat[i][j - 1]
               return mat
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
               mat = [[0] * n for _ in range(n)]
               for query in queries:
                   row1, col1, row2, col2 = query
                   for i in range(row1, row2 + 1):
                       mat[i][col1] += 1
                       if col2 + 1 < n:
                           mat[i][col2 + 1] -= 1
               for i in range(n):
                   for j in range(1, n):
                       mat[i][j] += mat[i][j - 1]
               return mat
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
       #include <stdlib.h>

       int** rangeAddQueries(int n, int** queries, int queriesSize, int* queriesColSize, int** columnSizes, int* returnSize) {
           int** mat = (int**)malloc(n * sizeof(int*));
           for (int i = 0; i < n; i++) {
               mat[i] = (int*)malloc(n * sizeof(int));
               for (int j = 0; j < n; j++) {
                   mat[i][j] = 0;
               }
           }
           for (int i = 0; i < queriesSize; i++) {
               int row1 = queries[i][0];
               int col1 = queries[i][1];
               int row2 = queries[i][2];
               int col2 = queries[i][3];
               for (int j = row1; j <= row2; j++) {
                   mat[j][col1]++;
                   if (col2 + 1 < n) {
                       mat[j][col2 + 1]--;
                   }
               }
           }
           for (int i = 0; i < n; i++) {
               for (int j = 1; j < n; j++) {
                   mat[i][j] += mat[i][j - 1];
               }
           }
           *returnSize = n;
           *columnSizes = (int*)malloc(n * sizeof(int));
           for (int i = 0; i < n; i++) {
               (*columnSizes)[i] = n;
           }
           return mat;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
           public int[][] RangeAddQueries(int n, int[][] queries) {
               int[][] mat = new int[n][];
               for (int i = 0; i < n; i++) {
                   mat[i] = new int[n];
               }
               foreach (int[] query in queries) {
                   int row1 = query[0];
                   int col1 = query[1];
                   int row2 = query[2];
                   int col2 = query[3];
                   for (int i = row1; i <= row2; i++) {
                       mat[i][col1]++;
                       if (col2 + 1 < n) {
                           mat[i][col2 + 1]--;
                       }
                   }
               }
               for (int i = 0; i < n; i++) {
                   for (int j = 1; j < n; j++) {
                       mat[i][j] += mat[i][j - 1];
                   }
               }
               return mat;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var rangeAddQueries = function(n, queries) {
           let mat = Array(n).fill(0).map(() => Array(n).fill(0));
           for (let query of queries) {
               let row1 = query[0];
               let col1 = query[1];
               let row2 = query[2];
               let col2 = query[3];
               for (let i = row1; i <= row2; i++) {
                   mat[i][col1]++;
                   if (col2 + 1 < n) {
                       mat[i][col2 + 1]--;
                   }
               }
           }
           for (let i = 0; i < n; i++) {
               for (let j = 1; j < n; j++) {
                   mat[i][j] += mat[i][j - 1];
               }
           }
           return mat;
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function rangeAddQueries(n: number, queries: number[][]): number[][] {
           let mat: number[][] = Array(n).fill(0).map(() => Array(n).fill(0));
           for (let query of queries) {
               let row1: number = query[0];
               let col1: number = query[1];
               let row2: number = query[2];
               let col2: number = query[3];
               for (let i: number = row1; i <= row2; i++) {
                   mat[i][col1]++;
                   if (col2 + 1 < n) {
                       mat[i][col2 + 1]--;
                   }
               }
           }
           for (let i: number = 0; i < n; i++) {
               for (let j: number = 1; j < n; j++) {
                   mat[i][j] += mat[i][j - 1];
               }
           }
           return mat;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
           function rangeAddQueries($n, $queries) {
               $mat = array_fill(0, $n, array_fill(0, $n, 0));
               foreach ($queries as $query) {
                   $row1 = $query[0];
                   $col1 = $query[1];
                   $row2 = $query[2];
                   $col2 = $query[3];
                   for ($i = $row1; $i <= $row2; $i++) {
                       $mat[$i][$col1]++;
                       if ($col2 + 1 < $n) {
                           $mat[$i][$col2 + 1]--;
                       }
                   }
               }
               for ($i = 0; $i < $n; $i++) {
                   for ($j = 1; $j < $n; $j++) {
                       $mat[$i][$j] += $mat[$i][$j - 1];
                   }
               }
               return $mat;
           }
       }
{% endhighlight %}

{% raw %}
<div class="code-tabs">
  <input type="radio" name="code-lang" id="lang-python" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-cpp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-go">
  <div class="tab-labels">
    <label for="lang-python">Python</label>
    <label for="lang-java">Java</label>
    <label for="lang-cpp">C++</label>
    <label for="lang-javascript">JS</label>
    <label for="lang-typescript">TS</label>
    <label for="lang-go">Go</label>
  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
           func rangeAddQueries(_ n: Int, _ queries: [[Int]]) -> [[Int]] {
               var mat = Array(repeating: Array(repeating: 0, count: n), count: n)
               for query in queries {
                   let row1 = query[0]
                   let col1 = query[1]
                   let row2 = query[2]
                   let col2 = query[3]
                   for i in row1...row2 {
                       mat[i][col1] += 1
                       if col2 + 1 < n {
                           mat[i][col2 + 1] -= 1
                       }
                   }
               }
               for i in 0..<n {
                   for j in 1..<n {
                       mat[i][j] += mat[i][j - 1]
                   }
               }
               return mat
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
           fun rangeAddQueries(n: Int, queries: Array<IntArray>): Array<IntArray> {
               val mat = Array(n) { IntArray(n) }
               for (query in queries) {
                   val row1 = query[0]
                   val col1 = query[1]
                   val row2 = query[2]
                   val col2 = query[3]
                   for (i in row1..row2) {
                       mat[i][col1]++
                       if (col2 + 1 < n) {
                           mat[i][col2 + 1]--
                       }
                   }
               }
               for (i in 0 until n) {
                   for (j in 1 until n) {
                       mat[i][j] += mat[i][j - 1]
                   }
               }
               return mat
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
           List<List<int>> rangeAddQueries(int n, List<List<int>> queries) {
               List<List<int>> mat = List.generate(n, (i) => List.generate(n, (j) => 0));
               for (var query in queries) {
                   int row1 = query[0];
                   int col1 = query[1];
                   int row2 = query[2];
                   int col2 = query[3];
                   for (int i = row1; i <= row2; i++) {
                       mat[i][col1]++;
                       if (col2 + 1 < n) {
                           mat[i][col2 + 1]--;
                       }
                   }
               }
               for (int i = 0; i < n; i++) {
                   for (int j = 1; j < n; j++) {
                       mat[i][j] += mat[i][j - 1];
                   }
               }
               return mat;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

       import (
           "fmt"
       )

       func rangeAddQueries(n int, queries [][]int) [][]int {
           mat := make([][]int, n)
           for i := range mat {
               mat[i] = make([]int, n)
           }
           for _, query := range queries {
               row1, col1, row2, col2 := query[0], query[1], query[2], query[3]
               for i := row1; i <= row2; i++ {
                   mat[i][col1]++
                   if col2+1 < n {
                       mat[i][col2+1]--
                   }
               }
           }
           for i := range mat {
               for j := 1; j < n; j++ {
                   mat[i][j] += mat[i][j-1]
               }
           }
           return mat
       }

       func main() {
           n := 3
           queries := [][]int{{1,1,2,2},{0,0,1,1}}
           fmt.Println(rangeAddQueries(n, queries))
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer} n
       # @param {Integer[][]} queries
       # @return {Integer[][]}
       def range_add_queries(n, queries)
           mat = Array.new(n) { Array.new(n, 0) }
           queries.each do |query|
               row1, col1, row2, col2 = query
               (row1..row2).each do |i|
                   mat[i][col1] += 1
                   mat[i][col2 + 1] -= 1 if col2 + 1 < n
               end
           end
           (0...n).each do |i|
               (1...n).each do |j|
                   mat[i][j] += mat[i][j - 1]
               end
           end
           mat
       end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
           def rangeAddQueries(n: Int, queries: Array[Array[Int]]): Array[Array[Int]] = {
               val mat = Array.fill(n, n)(0)
               for (query <- queries) {
                   val row1 = query(0)
                   val col1 = query(1)
                   val row2 = query(2)
                   val col2 = query(3)
                   for (i <- row1 to row2) {
                       mat(i)(col1) += 1
                       if (col2 + 1 < n) {
                           mat(i)(col2 + 1) -= 1
                       }
                   }
               }
               for (i <- 0 until n) {
                   for (j <- 1 until n) {
                       mat(i)(j) += mat(i)(j - 1)
                   }
               }
               mat
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
           pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
               let mut mat: Vec<Vec<i32>> = vec![vec![0; n as usize]; n as usize];
               for query in queries {
                   let row1 = query[0] as usize;
                   let col1 = query[1] as usize;
                   let row2 = query[2] as usize;
                   let col2 = query[3] as usize;
                   for i in row1..=row2 {
                       mat[i][col1] += 1;
                       if col2 + 1 < n as usize {
                           mat[i][col2 + 1] -= 1;
                       }
                   }
               }
               for i in 0..n as usize {
                   for j in 1..n as usize {
                       mat[i][j] += mat[i][j - 1];
                   }
               }
               mat
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

       (define (range-add-queries n queries)
           (define mat (make-vector n (make-vector n 0)))
           (for-each
               (λ (query)
                   (define row1 (vector-ref query 0))
                   (define col1 (vector-ref query 1))
                   (define row2 (vector-ref query 2))
                   (define col2 (vector-ref query 3))
                   (for ([i (in-range row1 (add1 row2))])
                       (vector-set! (vector-ref mat i) col1 (add1 (vector-ref (vector-ref mat i) col1)))
                       (when (< (add1 col2) n)
                           (vector-set! (vector-ref mat i) (add1 col2) (sub1 (vector-ref (vector-ref mat i) (add1 col2)))))))
               queries)
           (for ([i (in-range n)])
               (for ([j (in-range 1 n)])
                   (vector-set! (vector-ref mat i) j (+ (vector-ref (vector-ref mat i) j) (vector-ref (vector-ref mat i) (sub1 j))))))
           mat)
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([range_add_queries/2]).

       range_add_queries(N, Queries) ->
           Mat = array:new(N, {default, 0}),
           lists:foldl(
               fun(Query, MatAcc) ->
                   [Row1, Col1, Row2, Col2] = Query,
                   lists:foldl(
                       fun(I, MatAcc2) ->
                           Mat3 = array:set(I, Col1, array:get(I, Col1, MatAcc2) + 1, MatAcc2),
                           case Col2 + 1 < N of
                               true -> array:set(I, Col2 + 1, array:get(I, Col2 + 1, Mat3) - 1, Mat3);
                               false -> Mat3
                           end
                       end,
                       MatAcc,
                       lists:seq(Row1, Row2)
                   )
               end,
               Mat,
               Queries
           ),
           lists:map(
               fun(I) ->
                   lists:foldl(
                       fun(J, Acc) ->
                           [array:get(I, J, Mat) | Acc]
                       end,
                       [],
                       lists:seq(0, N - 1)
                   )
               end,
               lists:seq(0, N - 1)
           ).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def range_add_queries(n, queries) do
               mat = Array.new(n, fn -> Array.new(n, 0))
               Enum.reduce(queries, mat, fn query, mat ->
                   [row1, col1, row2, col2] = query
                   Enum.reduce(row1..row2, mat, fn i, mat ->
                       mat
                       |> Array.update!(i, fn row -> Array.update!(row, col1, &(&1 + 1)) end)
                       |> case do
                           mat when col2 + 1 < n ->
                               Array.update!(mat, i, fn row -> Array.update!(row, col2 + 1, &(&1 - 1)) end)

                           mat ->
                               mat
                       end
                   end)
               end)
               |> Enum.reduce(0..n-1, fn i, mat ->
                   Enum.reduce(1..n-1, mat, fn j, mat ->
                       Array.update!(mat, i, fn row -> Array.update!(row, j, &(&1 + Enum.at(Array.get(mat, i), j - 1))) end)
                   end)
               end)
               |> Enum.map(fn i -> Array.get(&1, i))
           end
       end
{% endhighlight %}

  </div>

</div>
{% endraw %}


### Complexity Analysis

- **Time Complexity:** O(n * m + q * n) where n is the number of rows, m is the number of columns, and q is the number of queries. The reason for this time complexity is that we are iterating over each query and updating the prefix sum array, and then we are iterating over each row in the matrix to update the elements.

- **Space Complexity:** O(n * m) where n is the number of rows and m is the number of columns. The reason for this space complexity is that we need to store the prefix sum array and the resulting matrix.
