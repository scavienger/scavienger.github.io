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

<p>You are given a positive integer <code>n</code>, indicating that we initially have an <code>n x n</code>&nbsp;<strong>0-indexed</strong> integer matrix <code>mat</code> filled with zeroes.</p>

<p>You are also given a 2D integer array <code>query</code>. For each <code>query[i] = [row1<sub>i</sub>, col1<sub>i</sub>, row2<sub>i</sub>, col2<sub>i</sub>]</code>, you should do the following operation:</p>

<ul>
	<li>Add <code>1</code> to <strong>every element</strong> in the submatrix with the <strong>top left</strong> corner <code>(row1<sub>i</sub>, col1<sub>i</sub>)</code> and the <strong>bottom right</strong> corner <code>(row2<sub>i</sub>, col2<sub>i</sub>)</code>. That is, add <code>1</code> to <code>mat[x][y]</code> for all <code>row1<sub>i</sub> &lt;= x &lt;= row2<sub>i</sub></code> and <code>col1<sub>i</sub> &lt;= y &lt;= col2<sub>i</sub></code>.</li>
</ul>

<p>Return<em> the matrix</em> <code>mat</code><em> after performing every query.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example11.png" style="width: 531px; height: 121px;" />
<pre>
<strong>Input:</strong> n = 3, queries = [[1,1,2,2],[0,0,1,1]]
<strong>Output:</strong> [[1,1,0],[1,2,1],[0,1,1]]
<strong>Explanation:</strong> The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example22.png" style="width: 261px; height: 82px;" />
<pre>
<strong>Input:</strong> n = 2, queries = [[0,0,1,1]]
<strong>Output:</strong> [[1,1],[1,1]]
<strong>Explanation:</strong> The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= row1<sub>i</sub> &lt;= row2<sub>i</sub> &lt; n</code></li>
	<li><code>0 &lt;= col1<sub>i</sub> &lt;= col2<sub>i</sub> &lt; n</code></li>
</ul>


## Hints

1. Imagine each row as a separate array. Instead of updating the whole submatrix together, we can use prefix sum to update each row separately.

2. For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].

3. After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1].

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 19:58:40 UTC)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The problem asks us to perform a series of range updates on an `n x n` matrix initialized with zeros. For each query `[row1, col1, row2, col2]`, we need to add 1 to every element within the submatrix defined by the top-left corner `(row1, col1)` and the bottom-right corner `(row2, col2)`. After all queries, we must return the final matrix.

A naive approach would be to iterate through the specified submatrix for each query and increment every cell directly. If there are `Q` queries and the maximum submatrix size is `n x n`, this approach would have a time complexity of `O(Q * n^2)`. Given `n` up to 500 and `Q` up to 10^4, `500^2 * 10^4 = 25 * 10^4 * 10^4 = 2.5 * 10^9`, which is too slow for typical time limits (usually around `10^8` operations per second).

To optimize this, we can use a technique based on difference arrays, specifically adapted for 2D range updates. Instead of directly updating all cells in a submatrix, we leverage the property that a range update can be represented by only a few point updates in a 'difference' matrix. When calculating prefix sums on this difference matrix, the range updates propagate correctly. The specific approach suggested by the hints is to treat each row independently for horizontal range updates, and then compute the prefix sums for each row. This avoids the more complex 2D difference array setup (which involves four corners `(r1, c1), (r1, c2+1), (r2+1, c1), (r2+1, c2+1)`).

The algorithm works in two main steps:

1.  **Difference Accumulation**: We initialize an `n x n` matrix `mat` with all zeros. For each query `[row1, col1, row2, col2]`, we iterate through each row `r` from `row1` to `row2`. For each such row `r`, we perform two operations:
    *   `mat[r][col1] += 1`: This marks the beginning of an increment for the current row `r` starting at `col1`.
    *   `mat[r][col2 + 1] -= 1`: If `col2 + 1` is within the matrix bounds (`col2 + 1 < n`), this operation effectively cancels out the increment from column `col2 + 1` onwards in row `r`. This ensures that the increment only applies to columns from `col1` to `col2`.
    This step essentially applies a 1D difference array logic to each individual row affected by the query.

2.  **Prefix Sum Calculation**: After processing all queries, the `mat` matrix stores these difference values. To transform these differences into the actual accumulated sums, we perform a row-wise prefix sum calculation. For each row `r` from `0` to `n-1`, and for each column `c` from `1` to `n-1`, we update `mat[r][c] = mat[r][c] + mat[r][c-1]`. This propagates the increments horizontally across each row, resulting in `mat[r][c]` holding the total sum of increments for cell `(r, c)`. The final `mat` matrix is then the required answer.

{% endraw %}

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    std::vector<std::vector<int>> rangeAddQueries(int n, std::vector<std::vector<int>>& queries) {
        // Initialize an n x n matrix with zeros
        std::vector<std::vector<int>> mat(n, std::vector<int>(n, 0));

        // Step 2: Process Queries (Difference Accumulation)
        for (const auto& query : queries) {
            int r1 = query[0];
            int c1 = query[1];
            int r2 = query[2];
            int c2 = query[3];

            // For each row affected by the query
            for (int r = r1; r <= r2; ++r) {
                // Add 1 at the starting column
                mat[r][c1] += 1;
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if (c2 + 1 < n) {
                    mat[r][c2 + 1] -= 1;
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for (int r = 0; r < n; ++r) {
            // For each column starting from the second one
            for (int c = 1; c < n; ++c) {
                // Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1];
            }
        }

        return mat;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;

class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        // Initialize an n x n matrix with zeros
        int[][] mat = new int[n][n]; // int arrays are initialized to 0 by default

        // Step 2: Process Queries (Difference Accumulation)
        for (int[] query : queries) {
            int r1 = query[0];
            int c1 = query[1];
            int r2 = query[2];
            int c2 = query[3];

            // For each row affected by the query
            for (int r = r1; r <= r2; ++r) {
                // Add 1 at the starting column
                mat[r][c1] += 1;
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if (c2 + 1 < n) {
                    mat[r][c2 + 1] -= 1;
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for (int r = 0; r < n; ++r) {
            // For each column starting from the second one
            for (int c = 1; c < n; ++c) {
                // Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1];
            }
        }

        return mat;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        mat = [[0] * n for _ in range(n)]

        # Step 2: Process Queries (Difference Accumulation)
        for r1, c1, r2, c2 in queries:
            # For each row affected by the query
            for r in range(r1, r2 + 1):
                # Add 1 at the starting column
                mat[r][c1] += 1
                # If the increment range ends before the matrix boundary,
                # subtract 1 at the column after the ending column to cancel out
                if c2 + 1 < n:
                    mat[r][c2 + 1] -= 1

        # Step 3: Compute Final Matrix (Prefix Sum Calculation)
        # Iterate through each row
        for r in range(n):
            # For each column starting from the second one
            for c in range(1, n):
                # Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1]

        return mat
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        mat = [[0] * n for _ in range(n)]

        # Step 2: Process Queries (Difference Accumulation)
        for r1, c1, r2, c2 in queries:
            # For each row affected by the query
            for r in range(r1, r2 + 1):
                # Add 1 at the starting column
                mat[r][c1] += 1
                # If the increment range ends before the matrix boundary,
                # subtract 1 at the column after the ending column to cancel out
                if c2 + 1 < n:
                    mat[r][c2 + 1] -= 1

        # Step 3: Compute Final Matrix (Prefix Sum Calculation)
        # Iterate through each row
        for r in range(n):
            # For each column starting from the second one
            for c in range(1, n):
                # Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1]

        return mat
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For malloc and calloc

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both functions malloc and free need to be used to manage memory.
 */
int** rangeAddQueries(int n, int** queries, int queriesSize, int* queriesColSize, int** returnSize, int** returnColumnSizes) {
    // Initialize an n x n matrix with zeros
    int** mat = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        mat[i] = (int*)calloc(n, sizeof(int)); // calloc initializes memory to zero
    }

    // Step 2: Process Queries (Difference Accumulation)
    for (int i = 0; i < queriesSize; i++) {
        int r1 = queries[i][0];
        int c1 = queries[i][1];
        int r2 = queries[i][2];
        int c2 = queries[i][3];

        // For each row affected by the query
        for (int r = r1; r <= r2; ++r) {
            // Add 1 at the starting column
            mat[r][c1] += 1;
            // If the increment range ends before the matrix boundary,
            // subtract 1 at the column after the ending column to cancel out
            if (c2 + 1 < n) {
                mat[r][c2 + 1] -= 1;
            }
        }
    }

    // Step 3: Compute Final Matrix (Prefix Sum Calculation)
    // Iterate through each row
    for (int r = 0; r < n; ++r) {
        // For each column starting from the second one
        for (int c = 1; c < n; ++c) {
            // Add the value from the previous column to accumulate the sum
            mat[r][c] += mat[r][c-1];
        }
    }

    // Set return size and column sizes as required by LeetCode C signature
    *returnSize = n;
    *returnColumnSizes = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        (*returnColumnSizes)[i] = n;
    }

    return mat;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int[][] RangeAddQueries(int n, int[][] queries) {
        // Initialize an n x n matrix with zeros
        int[][] mat = new int[n][];
        for (int i = 0; i < n; i++) {
            mat[i] = new int[n]; // Elements are initialized to 0 by default
        }

        // Step 2: Process Queries (Difference Accumulation)
        foreach (var query in queries) {
            int r1 = query[0];
            int c1 = query[1];
            int r2 = query[2];
            int c2 = query[3];

            // For each row affected by the query
            for (int r = r1; r <= r2; ++r) {
                // Add 1 at the starting column
                mat[r][c1] += 1;
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if (c2 + 1 < n) {
                    mat[r][c2 + 1] -= 1;
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for (int r = 0; r < n; ++r) {
            // For each column starting from the second one
            for (int c = 1; c < n; ++c) {
                // Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1];
            }
        }

        return mat;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[][]}
 */
var rangeAddQueries = function(n, queries) {
    // Initialize an n x n matrix with zeros
    const mat = Array(n).fill(0).map(() => Array(n).fill(0));

    // Step 2: Process Queries (Difference Accumulation)
    for (const query of queries) {
        const r1 = query[0];
        const c1 = query[1];
        const r2 = query[2];
        const c2 = query[3];

        // For each row affected by the query
        for (let r = r1; r <= r2; ++r) {
            // Add 1 at the starting column
            mat[r][c1] += 1;
            // If the increment range ends before the matrix boundary,
            // subtract 1 at the column after the ending column to cancel out
            if (c2 + 1 < n) {
                mat[r][c2 + 1] -= 1;
            }
        }
    }

    // Step 3: Compute Final Matrix (Prefix Sum Calculation)
    // Iterate through each row
    for (let r = 0; r < n; ++r) {
        // For each column starting from the second one
        for (let c = 1; c < n; ++c) {
            // Add the value from the previous column to accumulate the sum
            mat[r][c] += mat[r][c-1];
        }
    }

    return mat;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function rangeAddQueries(n: number, queries: number[][]): number[][] {
    // Initialize an n x n matrix with zeros
    const mat: number[][] = Array(n).fill(0).map(() => Array(n).fill(0));

    // Step 2: Process Queries (Difference Accumulation)
    for (const query of queries) {
        const r1 = query[0];
        const c1 = query[1];
        const r2 = query[2];
        const c2 = query[3];

        // For each row affected by the query
        for (let r = r1; r <= r2; ++r) {
            // Add 1 at the starting column
            mat[r][c1] += 1;
            // If the increment range ends before the matrix boundary,
            // subtract 1 at the column after the ending column to cancel out
            if (c2 + 1 < n) {
                mat[r][c2 + 1] -= 1;
            }
        }
    }

    // Step 3: Compute Final Matrix (Prefix Sum Calculation)
    // Iterate through each row
    for (let r = 0; r < n; ++r) {
        // For each column starting from the second one
        for (let c = 1; c < n; ++c) {
            // Add the value from the previous column to accumulate the sum
            mat[r][c] += mat[r][c-1];
        }
    }

    return mat;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[][]
     */
    function rangeAddQueries($n, $queries) {
        // Initialize an n x n matrix with zeros
        $mat = array_fill(0, $n, array_fill(0, $n, 0));

        // Step 2: Process Queries (Difference Accumulation)
        foreach ($queries as $query) {
            $r1 = $query[0];
            $c1 = $query[1];
            $r2 = $query[2];
            $c2 = $query[3];

            // For each row affected by the query
            for ($r = $r1; $r <= $r2; ++$r) {
                // Add 1 at the starting column
                $mat[$r][$c1] += 1;
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if ($c2 + 1 < $n) {
                    $mat[$r][$c2 + 1] -= 1;
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for ($r = 0; $r < $n; ++$r) {
            // For each column starting from the second one
            for ($c = 1; $c < $n; ++$c) {
                // Add the value from the previous column to accumulate the sum
                $mat[$r][$c] += $mat[$r][$c-1];
            }
        }

        return $mat;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func rangeAddQueries(_ n: Int, _ queries: [[Int]]) -> [[Int]] {
        // Initialize an n x n matrix with zeros
        var mat = Array(repeating: Array(repeating: 0, count: n), count: n)

        // Step 2: Process Queries (Difference Accumulation)
        for query in queries {
            let r1 = query[0]
            let c1 = query[1]
            let r2 = query[2]
            let c2 = query[3]

            // For each row affected by the query
            for r in r1...r2 { // Swift range operator
                // Add 1 at the starting column
                mat[r][c1] += 1
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if c2 + 1 < n {
                    mat[r][c2 + 1] -= 1
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for r in 0..<n {
            // For each column starting from the second one
            for c in 1..<n {
                // Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1]
            }
        }

        return mat
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun rangeAddQueries(n: Int, queries: Array<IntArray>): Array<IntArray> {
        // Initialize an n x n matrix with zeros
        val mat = Array(n) { IntArray(n) { 0 } }

        // Step 2: Process Queries (Difference Accumulation)
        for (query in queries) {
            val r1 = query[0]
            val c1 = query[1]
            val r2 = query[2]
            val c2 = query[3]

            // For each row affected by the query
            for (r in r1..r2) {
                // Add 1 at the starting column
                mat[r][c1] += 1
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if (c2 + 1 < n) {
                    mat[r][c2 + 1] -= 1
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for (r in 0 until n) {
            // For each column starting from the second one
            for (c in 1 until n) {
                // Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1]
            }
        }

        return mat
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<List<int>> rangeAddQueries(int n, List<List<int>> queries) {
    // Initialize an n x n matrix with zeros
    List<List<int>> mat = List.generate(n, (_) => List.filled(n, 0));

    // Step 2: Process Queries (Difference Accumulation)
    for (final query in queries) {
      int r1 = query[0];
      int c1 = query[1];
      int r2 = query[2];
      int c2 = query[3];

      // For each row affected by the query
      for (int r = r1; r <= r2; ++r) {
        // Add 1 at the starting column
        mat[r][c1] += 1;
        // If the increment range ends before the matrix boundary,
        // subtract 1 at the column after the ending column to cancel out
        if (c2 + 1 < n) {
          mat[r][c2 + 1] -= 1;
        }
      }
    }

    // Step 3: Compute Final Matrix (Prefix Sum Calculation)
    // Iterate through each row
    for (int r = 0; r < n; ++r) {
      // For each column starting from the second one
      for (int c = 1; c < n; ++c) {
        // Add the value from the previous column to accumulate the sum
        mat[r][c] += mat[r][c-1];
      }
    }

    return mat;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

func rangeAddQueries(n int, queries [][]int) [][]int {
    // Initialize an n x n matrix with zeros
    mat := make([][]int, n)
    for i := range mat {
        mat[i] = make([]int, n) // Elements are initialized to 0 by default
    }

    // Step 2: Process Queries (Difference Accumulation)
    for _, query := range queries {
        r1, c1, r2, c2 := query[0], query[1], query[2], query[3]

        // For each row affected by the query
        for r := r1; r <= r2; r++ {
            // Add 1 at the starting column
            mat[r][c1] += 1
            // If the increment range ends before the matrix boundary,
            // subtract 1 at the column after the ending column to cancel out
            if c2 + 1 < n {
                mat[r][c2 + 1] -= 1
            }
        }
    }

    // Step 3: Compute Final Matrix (Prefix Sum Calculation)
    // Iterate through each row
    for r := 0; r < n; r++ {
        // For each column starting from the second one
        for c := 1; c < n; c++ {
            // Add the value from the previous column to accumulate the sum
            mat[r][c] += mat[r][c-1]
        }
    }

    return mat
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[][]}
def range_add_queries(n, queries)
    # Initialize an n x n matrix with zeros
    mat = Array.new(n) { Array.new(n, 0) }

    # Step 2: Process Queries (Difference Accumulation)
    queries.each do |query|
        r1, c1, r2, c2 = query[0], query[1], query[2], query[3]

        # For each row affected by the query
        (r1..r2).each do |r|
            # Add 1 at the starting column
            mat[r][c1] += 1
            # If the increment range ends before the matrix boundary,
            # subtract 1 at the column after the ending column to cancel out
            if c2 + 1 < n
                mat[r][c2 + 1] -= 1
            end
        end
    end

    # Step 3: Compute Final Matrix (Prefix Sum Calculation)
    # Iterate through each row
    (0...n).each do |r|
        # For each column starting from the second one
        (1...n).each do |c|
            # Add the value from the previous column to accumulate the sum
            mat[r][c] += mat[r][c-1]
        end
    end

    return mat
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def rangeAddQueries(n: Int, queries: Array[Array[Int]]): Array[Array[Int]] = {
        // Initialize an n x n matrix with zeros
        val mat: Array[Array[Int]] = Array.ofDim[Int](n, n) // Elements are initialized to 0

        // Step 2: Process Queries (Difference Accumulation)
        for (query <- queries) {
            val r1 = query(0)
            val c1 = query(1)
            val r2 = query(2)
            val c2 = query(3)

            // For each row affected by the query
            for (r <- r1 to r2) {
                // Add 1 at the starting column
                mat(r)(c1) += 1
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if (c2 + 1 < n) {
                    mat(r)(c2 + 1) -= 1
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for (r <- 0 until n) {
            // For each column starting from the second one
            for (c <- 1 until n) {
                // Add the value from the previous column to accumulate the sum
                mat(r)(c) += mat(r)(c-1)
            }
        }

        mat
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n_usize = n as usize;
        // Initialize an n x n matrix with zeros
        let mut mat: Vec<Vec<i32>> = vec![vec![0; n_usize]; n_usize];

        // Step 2: Process Queries (Difference Accumulation)
        for query in queries {
            let r1 = query[0] as usize;
            let c1 = query[1] as usize;
            let r2 = query[2] as usize;
            let c2 = query[3] as usize;

            // For each row affected by the query
            for r in r1..=r2 {
                // Add 1 at the starting column
                mat[r][c1] += 1;
                // If the increment range ends before the matrix boundary,
                // subtract 1 at the column after the ending column to cancel out
                if c2 + 1 < n_usize {
                    mat[r][c2 + 1] -= 1;
                }
            }
        }

        // Step 3: Compute Final Matrix (Prefix Sum Calculation)
        // Iterate through each row
        for r in 0..n_usize {
            // For each column starting from the second one
            for c in 1..n_usize {
                // Add the value from the previous column to accumulate the sum
                mat[r][c] += mat[r][c-1];
            }
        }

        mat
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (range-add-queries n queries)
  ;; Initialize an n x n matrix with zeros using vectors for efficiency
  (define mat (build-vector n (lambda (r) (make-vector n 0))))

  ;; Step 2: Process Queries (Difference Accumulation)
  (for-each
   (lambda (query)
     (define r1 (list-ref query 0))
     (define c1 (list-ref query 1))
     (define r2 (list-ref query 2))
     (define c2 (list-ref query 3))

     ;; For each row affected by the query
     (for ([r (range r1 (+ r2 1))])
       (define current-row (vector-ref mat r))
       ;; Add 1 at the starting column
       (vector-set! current-row c1 (+ (vector-ref current-row c1) 1))
       ;; If the increment range ends before the matrix boundary,
       ;; subtract 1 at the column after the ending column to cancel out
       (when (< (+ c2 1) n)
         (vector-set! current-row (+ c2 1) (- (vector-ref current-row (+ c2 1)) 1))))
     )
   queries)

  ;; Step 3: Compute Final Matrix (Prefix Sum Calculation)
  ;; Iterate through each row
  (for ([r (range 0 n)])
    (define current-row (vector-ref mat r))
    ;; For each column starting from the second one
    (for ([c (range 1 n)])
      ;; Add the value from the previous column to accumulate the sum
      (vector-set! current-row c (+ (vector-ref current-row c) (vector-ref current-row (- c 1)))))
    )

  ;; Convert vector of vectors back to list of lists as output format implies
  (for/list ([v (in-vector mat)])
    (vector->list v))
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([range_add_queries/2]).
-include_lib("kernel/include/array.hrl").

range_add_queries(N, Queries) ->
    % Initialize an N x N matrix with zeros using Erlang's array module for efficient access/update
    ZeroArray = array:new([{size, N}, {fixed, true}, {default, 0}]),
    Mat = lists:duplicate(N, ZeroArray),

    % Step 2: Process Queries (Difference Accumulation)
    FinalMatWithDiffs = lists:foldl(
        fun(Query, CurrentMat) ->
            [R1, C1, R2, C2] = Query,
            lists:mapi(
                fun(RIdx, RowArray) ->
                    if
                        RIdx >= R1, RIdx =< R2 ->
                            % Add 1 at the starting column
                            ValC1 = array:get(C1, RowArray),
                            UpdatedRowArray1 = array:set(C1, ValC1 + 1, RowArray),
                            if
                                C2 + 1 < N ->
                                    % Subtract 1 at the column after the ending column to cancel out
                                    ValC2Plus1 = array:get(C2 + 1, UpdatedRowArray1),
                                    array:set(C2 + 1, ValC2Plus1 - 1, UpdatedRowArray1);
                                true ->
                                    UpdatedRowArray1
                            end;
                        true ->
                            RowArray
                    end
                end,
                CurrentMat
            )
        end,
        Mat,
        Queries
    ),

    % Step 3: Compute Final Matrix (Prefix Sum Calculation)
    % Iterate through each row and compute prefix sum
    lists:map(
        fun(RowArray) ->
            RowList = array:to_list(RowArray), % Convert to list to build prefix sum functionally
            lists:foldl(
                fun(CurrentVal, Acc) ->
                    case Acc of
                        [] ->
                            [CurrentVal];
                        [PrevSum | _] ->
                            [CurrentVal + PrevSum | Acc]
                    end
                end,
                [],
                RowList
            ) |> lists:reverse % Prefix sum accumulates from left to right, foldl builds in reverse
        end,
        FinalMatWithDiffs
    ).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec range_add_queries(n :: integer, queries :: [[integer]]) :: [[integer]]
  def range_add_queries(n, queries) do
    # Initialize an n x n matrix with zeros using Erlang's :array module
    zero_array = :array.new(size: n, fixed: true, default: 0)
    mat = for _ <- 0..(n-1), do: zero_array

    # Step 2: Process Queries (Difference Accumulation)
    final_mat_with_diffs = Enum.reduce(queries, mat, fn [r1, c1, r2, c2], current_mat ->
      Enum.mapi(current_mat, fn r_idx, row_array ->
        if r_idx >= r1 and r_idx <= r2 do
          # Add 1 at the starting column
          val_c1 = :array.get(c1, row_array)
          updated_row_array1 = :array.set(c1, val_c1 + 1, row_array)
          # If the increment range ends before the matrix boundary,
          # subtract 1 at the column after the ending column to cancel out
          if c2 + 1 < n do
            val_c2_plus_1 = :array.get(c2 + 1, updated_row_array1)
            :array.set(c2 + 1, val_c2_plus_1 - 1, updated_row_array1)
          else
            updated_row_array1
          end
        else
          row_array
        end
      end)
    end)

    # Step 3: Compute Final Matrix (Prefix Sum Calculation)
    # Iterate through each row and compute prefix sum
    Enum.map(final_mat_with_diffs, fn row_array ->
      # Convert array to list for `Enum.scan`
      row_list = :array.to_list(row_array)
      Enum.scan(row_list, fn val, acc -> val + acc end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(Q * n + n^2)

- **Space Complexity:** O(n^2)

</div>
</details>


<hr class="ai-solution-separator">


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 19:58:51 UTC)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The approach to solve this problem involves using a prefix sum array to efficiently update the submatrices. 
We start by initializing a 2D array of size n x n with all elements as 0. 
Then, for each query, we iterate over the rows in the range [row1, row2] and add 1 to the prefix sum at column col1, 
and subtract 1 from the prefix sum at column col2 + 1. 
After processing all queries, we update each row separately by calculating the prefix sum for each column.

The problem-solving strategy involves the following steps:
1. Initialize a 2D array of size n x n with all elements as 0.
2. Process each query by updating the prefix sum array.
3. Update each row separately by calculating the prefix sum for each column.

The algorithm logic can be described as follows:
1. For each query, iterate over the rows in the range [row1, row2].
2. For each row, add 1 to the prefix sum at column col1, and subtract 1 from the prefix sum at column col2 + 1.
3. After processing all queries, update each row separately by calculating the prefix sum for each column.

The time complexity of this approach is O(n * m * q), where n is the size of the matrix, m is the number of columns, 
and q is the number of queries. The space complexity is O(n * m), which is used to store the prefix sum array.

The approach can be illustrated with an example. Suppose we have a 3x3 matrix and two queries: 
[[1,1,2,2],[0,0,1,1]]. We start by initializing the prefix sum array with all elements as 0. 
Then, we process each query by updating the prefix sum array. 
After processing all queries, we update each row separately by calculating the prefix sum for each column.

{% endraw %}

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
#include <vector>
         #include <iostream>

         using namespace std;

         class Solution {
         public:
             vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
                 vector<vector<int>> res(n, vector<int>(n, 0));
                 for (auto& query : queries) {
                     int row1 = query[0], col1 = query[1], row2 = query[2], col2 = query[3];
                     for (int i = row1; i <= row2; i++) {
                         res[i][col1]++;
                         if (col2 + 1 < n) {
                             res[i][col2 + 1]--;
                         }
                     }
                 }
                 for (int i = 0; i < n; i++) {
                     for (int j = 1; j < n; j++) {
                         res[i][j] += res[i][j - 1];
                     }
                 }
                 return res;
             }
         };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

         public class Solution {
             public int[][] rangeAddQueries(int n, int[][] queries) {
                 int[][] res = new int[n][n];
                 for (int[] query : queries) {
                     int row1 = query[0], col1 = query[1], row2 = query[2], col2 = query[3];
                     for (int i = row1; i <= row2; i++) {
                         res[i][col1]++;
                         if (col2 + 1 < n) {
                             res[i][col2 + 1]--;
                         }
                     }
                 }
                 for (int i = 0; i < n; i++) {
                     for (int j = 1; j < n; j++) {
                         res[i][j] += res[i][j - 1];
                     }
                 }
                 return res;
             }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
             def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
                 res = [[0] * n for _ in range(n)]
                 for query in queries:
                     row1, col1, row2, col2 = query
                     for i in range(row1, row2 + 1):
                         res[i][col1] += 1
                         if col2 + 1 < n:
                             res[i][col2 + 1] -= 1
                 for i in range(n):
                     for j in range(1, n):
                         res[i][j] += res[i][j - 1]
                 return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
             def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
                 res = [[0] * n for _ in range(n)]
                 for query in queries:
                     row1, col1, row2, col2 = query
                     for i in range(row1, row2 + 1):
                         res[i][col1] += 1
                         if col2 + 1 < n:
                             res[i][col2 + 1] -= 1
                 for i in range(n):
                     for j in range(1, n):
                         res[i][j] += res[i][j - 1]
                 return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
         #include <stdlib.h>

         int** rangeAddQueries(int n, int** queries, int queriesSize, int* queriesColSize, int** columnSizes, int* returnSize) {
             int** res = (int**)malloc(n * sizeof(int*));
             for (int i = 0; i < n; i++) {
                 res[i] = (int*)malloc(n * sizeof(int));
                 for (int j = 0; j < n; j++) {
                     res[i][j] = 0;
                 }
             }
             for (int i = 0; i < queriesSize; i++) {
                 int row1 = queries[i][0], col1 = queries[i][1], row2 = queries[i][2], col2 = queries[i][3];
                 for (int j = row1; j <= row2; j++) {
                     res[j][col1]++;
                     if (col2 + 1 < n) {
                         res[j][col2 + 1]--;
                     }
                 }
             }
             for (int i = 0; i < n; i++) {
                 for (int j = 1; j < n; j++) {
                     res[i][j] += res[i][j - 1];
                 }
             }
             *returnSize = n;
             *columnSizes = (int*)malloc(n * sizeof(int));
             for (int i = 0; i < n; i++) {
                 (*columnSizes)[i] = n;
             }
             return res;
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
             public int[][] RangeAddQueries(int n, int[][] queries) {
                 int[][] res = new int[n][];
                 for (int i = 0; i < n; i++) {
                     res[i] = new int[n];
                 }
                 foreach (var query in queries) {
                     int row1 = query[0], col1 = query[1], row2 = query[2], col2 = query[3];
                     for (int i = row1; i <= row2; i++) {
                         res[i][col1]++;
                         if (col2 + 1 < n) {
                             res[i][col2 + 1]--;
                         }
                     }
                 }
                 for (int i = 0; i < n; i++) {
                     for (int j = 1; j < n; j++) {
                         res[i][j] += res[i][j - 1];
                     }
                 }
                 return res;
             }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var rangeAddQueries = function(n, queries) {
             let res = Array(n).fill(0).map(() => Array(n).fill(0));
             for (let query of queries) {
                 let row1 = query[0], col1 = query[1], row2 = query[2], col2 = query[3];
                 for (let i = row1; i <= row2; i++) {
                     res[i][col1]++;
                     if (col2 + 1 < n) {
                         res[i][col2 + 1]--;
                     }
                 }
             }
             for (let i = 0; i < n; i++) {
                 for (let j = 1; j < n; j++) {
                     res[i][j] += res[i][j - 1];
                 }
             }
             return res;
         };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function rangeAddQueries(n: number, queries: number[][]): number[][] {
             let res: number[][] = Array(n).fill(0).map(() => Array(n).fill(0));
             for (let query of queries) {
                 let row1: number = query[0], col1: number = query[1], row2: number = query[2], col2: number = query[3];
                 for (let i: number = row1; i <= row2; i++) {
                     res[i][col1]++;
                     if (col2 + 1 < n) {
                         res[i][col2 + 1]--;
                     }
                 }
             }
             for (let i: number = 0; i < n; i++) {
                 for (let j: number = 1; j < n; j++) {
                     res[i][j] += res[i][j - 1];
                 }
             }
             return res;
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
             function rangeAddQueries($n, $queries) {
                 $res = array_fill(0, $n, array_fill(0, $n, 0));
                 foreach ($queries as $query) {
                     $row1 = $query[0]; $col1 = $query[1]; $row2 = $query[2]; $col2 = $query[3];
                     for ($i = $row1; $i <= $row2; $i++) {
                         $res[$i][$col1]++;
                         if ($col2 + 1 < $n) {
                             $res[$i][$col2 + 1]--;
                         }
                     }
                 }
                 for ($i = 0; $i < $n; $i++) {
                     for ($j = 1; $j < $n; $j++) {
                         $res[$i][$j] += $res[$i][$j - 1];
                     }
                 }
                 return $res;
             }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
             func rangeAddQueries(_ n: Int, _ queries: [[Int]]) -> [[Int]] {
                 var res = Array(repeating: Array(repeating: 0, count: n), count: n)
                 for query in queries {
                     let row1 = query[0], col1 = query[1], row2 = query[2], col2 = query[3]
                     for i in row1...row2 {
                         res[i][col1] += 1
                         if col2 + 1 < n {
                             res[i][col2 + 1] -= 1
                         }
                     }
                 }
                 for i in 0..<n {
                     for j in 1..<n {
                         res[i][j] += res[i][j - 1]
                     }
                 }
                 return res
             }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
             fun rangeAddQueries(n: Int, queries: Array<IntArray>): Array<IntArray> {
                 val res = Array(n) { IntArray(n) }
                 for (query in queries) {
                     val row1 = query[0]
                     val col1 = query[1]
                     val row2 = query[2]
                     val col2 = query[3]
                     for (i in row1..row2) {
                         res[i][col1]++
                         if (col2 + 1 < n) {
                             res[i][col2 + 1]--
                         }
                     }
                 }
                 for (i in 0 until n) {
                     for (j in 1 until n) {
                         res[i][j] += res[i][j - 1]
                     }
                 }
                 return res
             }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
           List<List<int>> rangeAddQueries(int n, List<List<int>> queries) {
             List<List<int>> res = List.generate(n, (i) => List.generate(n, (j) => 0));
             for (var query in queries) {
               int row1 = query[0], col1 = query[1], row2 = query[2], col2 = query[3];
               for (int i = row1; i <= row2; i++) {
                 res[i][col1]++;
                 if (col2 + 1 < n) {
                   res[i][col2 + 1]--;
                 }
               }
             }
             for (int i = 0; i < n; i++) {
               for (int j = 1; j < n; j++) {
                 res[i][j] += res[i][j - 1];
               }
             }
             return res;
           }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func rangeAddQueries(n int, queries [][]int) [][]int {
             res := make([][]int, n)
             for i := range res {
                 res[i] = make([]int, n)
             }
             for _, query := range queries {
                 row1, col1, row2, col2 := query[0], query[1], query[2], query[3]
                 for i := row1; i <= row2; i++ {
                     res[i][col1]++
                     if col2+1 < n {
                         res[i][col2+1]--
                     }
                 }
             }
             for i := 0; i < n; i++ {
                 for j := 1; j < n; j++ {
                     res[i][j] += res[i][j-1]
                 }
             }
             return res
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
         # @param {Integer[][]} queries
         # @return {Integer[][]}
         def range_add_queries(n, queries)
           res = Array.new(n) { Array.new(n, 0) }
           queries.each do |query|
             row1, col1, row2, col2 = query
             (row1..row2).each do |i|
               res[i][col1] += 1
               res[i][col2 + 1] -= 1 if col2 + 1 < n
             end
           end
           (0...n).each do |i|
             (1...n).each do |j|
               res[i][j] += res[i][j - 1]
             end
           end
           res
         end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
           def rangeAddQueries(n: Int, queries: Array[Array[Int]]): Array[Array[Int]] = {
             val res = Array.fill(n)(new Array[Int](n))
             queries.foreach { query =>
               val row1 = query(0)
               val col1 = query(1)
               val row2 = query(2)
               val col2 = query(3)
               (row1 to row2).foreach { i =>
                 res(i)(col1) += 1
                 if (col2 + 1 < n) {
                   res(i)(col2 + 1) -= 1
                 }
               }
             }
             (0 until n).foreach { i =>
               (1 until n).foreach { j =>
                 res(i)(j) += res(i)(j - 1)
               }
             }
             res
           }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
             pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
                 let n = n as usize;
                 let mut res: Vec<Vec<i32>> = vec![vec![0; n]; n];
                 for query in queries {
                     let row1 = query[0] as usize;
                     let col1 = query[1] as usize;
                     let row2 = query[2] as usize;
                     let col2 = query[3] as usize;
                     for i in row1..=row2 {
                         res[i][col1] += 1;
                         if col2 + 1 < n {
                             res[i][col2 + 1] -= 1;
                         }
                     }
                 }
                 for i in 0..n {
                     for j in 1..n {
                         res[i][j] += res[i][j - 1];
                     }
                 }
                 res
             }
         }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
         (define (range-add-queries n queries)
           (define res (make-vector n (make-vector n 0)))
           (for-each
             (lambda (query)
               (define row1 (vector-ref query 0))
               (define col1 (vector-ref query 1))
               (define row2 (vector-ref query 2))
               (define col2 (vector-ref query 3))
               (for ([i (in-range row1 (add1 row2))])
                 (vector-set! (vector-ref res i) col1 (add1 (vector-ref (vector-ref res i) col1)))
                 (when (< (add1 col2) n)
                   (vector-set! (vector-ref res i) (add1 col2) (sub1 (vector-ref (vector-ref res i) (add1 col2)))))))
             queries)
           (for ([i (in-range n)])
             (for ([j (in-range 1 n)])
               (vector-set! (vector-ref res i) j (+ (vector-ref (vector-ref res i) j) (vector-ref (vector-ref res i) (sub1 j))))))
           res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
         -export([range_add_queries/2]).

         range_add_queries(N, Queries) ->
             Res = array:new(N, {default, 0}),
             lists:foldl(
               fun(Query, Res0) ->
                   [Row1, Col1, Row2, Col2] = Query,
                   lists:foldl(
                     fun(I, Res1) ->
                       array:set(I, Col1, array:get(I, Col1) + 1, Res1),
                       if Col2 + 1 < N ->
                           array:set(I, Col2 + 1, array:get(I, Col2 + 1) - 1, Res1);
                          true -> Res1
                       end
                     end,
                     Res0,
                     lists:seq(Row1, Row2)
                   )
               end,
               Res,
               Queries
             ),
             lists:foldl(
               fun(I, Res0) ->
                 lists:foldl(
                   fun(J, Res1) ->
                     array:set(I, J, array:get(I, J) + array:get(I, J - 1), Res1)
                   end,
                   Res0,
                   lists:seq(1, N - 1)
                 )
               end,
               Res,
               lists:seq(0, N - 1)
             ).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
           def range_add_queries(n, queries) do
             res = Array.new(n, fn -> Array.new(n, 0) end)
             Enum.reduce(queries, res, fn query, res ->
               [row1, col1, row2, col2] = query
               Enum.reduce(row1..row2, res, fn i, res ->
                 res
                 |> Array.put(i, Array.put(Enum.at(res, i), col1, Enum.at(Enum.at(res, i), col1) + 1))
                 |> if col2 + 1 < n do
                       Array.put(i, Array.put(Enum.at(res, i), col2 + 1, Enum.at(Enum.at(res, i), col2 + 1) - 1))
                     else
                       &1
                   end)
             end)
             |> Enum.reduce(0..n-1, fn i, res ->
               Enum.reduce(1..n-1, res, fn j, res ->
                 Array.put(i, Array.put(Enum.at(res, i), j, Enum.at(Enum.at(res, i), j) + Enum.at(Enum.at(res, i), j - 1)), res)
               end)
             end)
           end
         end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * m * q) where n is the size of the matrix, m is the number of columns, and q is the number of queries. 
      The time complexity is O(n * m * q) because we need to process each query, which involves iterating over the rows in the range [row1, row2] 
      and updating the prefix sum array. We also need to update each row separately by calculating the prefix sum for each column.

- **Space Complexity:** O(n * m) which is used to store the prefix sum array. 
      The space complexity is O(n * m) because we need to store the prefix sum array, which has a size of n x m.

</div>
</details>
