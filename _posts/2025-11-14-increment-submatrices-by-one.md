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



You are also given a 2D integer array `query`. For each `query[i] = [row1_i, col1_i, row2_i, col2_i]`, you should do the following operation:





	- Add `1` to **every element** in the submatrix with the **top left** corner `(row1_i, col1_i)` and the **bottom right** corner `(row2_i, col2_i)`. That is, add `1` to `mat[x][y]` for all `row1_i Example 1:



```

{% raw %}
**Input:** n = 3, queries = [[1,1,2,2],[0,0,1,1]]
**Output:** [[1,1,0],[1,2,1],[0,1,1]]
{% endraw %}
**Explanation:** The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).

```

Example 2:



```

{% raw %}
**Input:** n = 2, queries = [[0,0,1,1]]
**Output:** [[1,1],[1,1]]
{% endraw %}
**Explanation:** The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.

```

 


**Constraints:**





	- `1 <= n <= 500`
	- `1 <= queries.length <= 10^4`
	- `0 <= row1_i <= row2_i < n`
	- `0 <= col1_i <= col2_i < n`

## Hints

1. Imagine each row as a separate array. Instead of updating the whole submatrix together, we can use prefix sum to update each row separately.

2. For each query, iterate over the rows i in the range [row1, row2] and add 1 to prefix sum S[i][col1], and subtract 1 from S[i][col2 + 1].

3. After doing this operation for all the queries, update each row separately with S[i][j] = S[i][j] + S[i][j - 1].

## Solution

### Approach

TODO: Add solution approach here.

### Code

```python
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
```

### Complexity Analysis

- **Time Complexity:** O(?)

- **Space Complexity:** O(?)

## ✨ AI-Generated Solution (GEMINI)

### Approach

The problem asks us to perform multiple range update operations on an `n x n` matrix and return the final state of the matrix. A naive approach of iterating through each submatrix for every query would be too slow given `n` up to 500 and `queries.length` up to 10^4, leading to a worst-case time complexity of O(queries.length * n^2), which is roughly 2.5 * 10^9 operations. 

We can optimize this using a 2D difference array (also known as a 2D prefix sum array technique). The core idea is to mark the boundaries of each update operation. Instead of directly adding 1 to every element in the submatrix, we record the "start" and "end" effects of the addition at specific points in a auxiliary matrix, let's call it `diff`. After processing all queries, we then compute the actual values in the final matrix by calculating 2D prefix sums of the `diff` matrix.

For each query `[row1, col1, row2, col2]` where we need to add `k=1` to the submatrix:
1. **`diff[row1][col1] += k`**: This marks the top-left corner of the submatrix. An increment here will effectively propagate `k` to all cells `(x, y)` where `x >= row1` and `y >= col1` when we compute prefix sums.
2. **`diff[row1][col2 + 1] -= k`**: To cancel the effect of `k` for columns `y > col2` within the rows starting from `row1`, we subtract `k` at `(row1, col2 + 1)`. This boundary check `col2 + 1 < n` is important to avoid out-of-bounds access.
3. **`diff[row2 + 1][col1] -= k`**: Similarly, to cancel the effect of `k` for rows `x > row2` within the columns starting from `col1`, we subtract `k` at `(row2 + 1, col1)`. This boundary check `row2 + 1 < n` is important.
4. **`diff[row2 + 1][col2 + 1] += k`**: When we subtracted `k` at `(row1, col2 + 1)` and `(row2 + 1, col1)`, the region `(x, y)` where `x > row2` and `y > col2` had `k` double-subtracted. To correct this, we add `k` back at `(row2 + 1, col2 + 1)`. This boundary check `row2 + 1 < n` and `col2 + 1 < n` is important.

After processing all `queries` and populating the `diff` matrix, the final value `mat[x][y]` can be computed using the 2D prefix sum formula: 
`mat[x][y] = diff[x][y] + mat[x-1][y] + mat[x][y-1] - mat[x-1][y-1]`

This calculation needs to be done iteratively for all `x` from `0` to `n-1` and `y` from `0` to `n-1`. For `x=0` or `y=0`, the terms `mat[x-1][y]`, `mat[x][y-1]`, or `mat[x-1][y-1]` are considered zero (or handled by appropriate boundary checks).

**Algorithm Steps:**
1. Initialize an `n x n` matrix `mat` (which will serve as our `diff` matrix and then the final result matrix) with all zeroes.
2. For each query `[row1, col1, row2, col2]`:
   a. `mat[row1][col1] += 1`
   b. If `col2 + 1 < n`, then `mat[row1][col2 + 1] -= 1`
   c. If `row2 + 1 < n`, then `mat[row2 + 1][col1] -= 1`
   d. If `row2 + 1 < n` and `col2 + 1 < n`, then `mat[row2 + 1][col2 + 1] += 1`
3. After processing all queries, iterate through the `mat` matrix to compute the actual values (2D prefix sums):
   a. For `x` from `0` to `n-1`:
   b.   For `y` from `0` to `n-1`:
   c.     If `x > 0`, `mat[x][y] += mat[x-1][y]`
   d.     If `y > 0`, `mat[x][y] += mat[x][y-1]`
   e.     If `x > 0` and `y > 0`, `mat[x][y] -= mat[x-1][y-1]`
4. Return `mat`.

### Code

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

  <div class="tab-panel" data-lang="python">

```python
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Initialize an n x n matrix with zeros. This will serve as our difference array.
        mat = [[0] * n for _ in range(n)]

        # Process each query to populate the difference array
        for r1, c1, r2, c2 in queries:
            # Add 1 at the top-left corner of the submatrix
            mat[r1][c1] += 1

            # Subtract 1 at (r1, c2+1) to cancel effect for columns beyond c2
            if c2 + 1 < n:
                mat[r1][c2 + 1] -= 1
            
            # Subtract 1 at (r2+1, c1) to cancel effect for rows beyond r2
            if r2 + 1 < n:
                mat[r2 + 1][c1] -= 1
            
            # Add 1 at (r2+1, c2+1) to correct double subtraction for the region beyond r2 and c2
            if r2 + 1 < n and c2 + 1 < n:
                mat[r2 + 1][c2 + 1] += 1
        
        # Compute the 2D prefix sums to get the final matrix values
        for r in range(n):
            for c in range(n):
                # Add value from cell above (if not in first row)
                if r > 0:
                    mat[r][c] += mat[r-1][c]
                
                # Add value from cell to the left (if not in first column)
                if c > 0:
                    mat[r][c] += mat[r][c-1]
                
                # Subtract value from top-left diagonal (if not in first row or col)
                # This is because mat[r-1][c] and mat[r][c-1] both include mat[r-1][c-1],
                # so it's counted twice and needs to be subtracted once.
                if r > 0 and c > 0:
                    mat[r][c] -= mat[r-1][c-1]
        
        return mat
```

  </div>

  <div class="tab-panel" data-lang="java">

```java
class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        // Initialize an n x n matrix with zeros. This will serve as our difference array.
        int[][] mat = new int[n][n];

        // Process each query to populate the difference array
        for (int[] query : queries) {
            int r1 = query[0];
            int c1 = query[1];
            int r2 = query[2];
            int c2 = query[3];

            // Add 1 at the top-left corner of the submatrix
            mat[r1][c1] += 1;

            // Subtract 1 at (r1, c2+1) to cancel effect for columns beyond c2
            if (c2 + 1 < n) {
                mat[r1][c2 + 1] -= 1;
            }
            
            // Subtract 1 at (r2+1, c1) to cancel effect for rows beyond r2
            if (r2 + 1 < n) {
                mat[r2 + 1][c1] -= 1;
            }
            
            // Add 1 at (r2+1, c2+1) to correct double subtraction for the region beyond r2 and c2
            if (r2 + 1 < n && c2 + 1 < n) {
                mat[r2 + 1][c2 + 1] += 1;
            }
        }
        
        // Compute the 2D prefix sums to get the final matrix values
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                // Add value from cell above (if not in first row)
                if (r > 0) {
                    mat[r][c] += mat[r-1][c];
                }
                
                // Add value from cell to the left (if not in first column)
                if (c > 0) {
                    mat[r][c] += mat[r][c-1];
                }
                
                // Subtract value from top-left diagonal (if not in first row or col)
                // This is because mat[r-1][c] and mat[r][c-1] both include mat[r-1][c-1],
                // so it's counted twice and needs to be subtracted once.
                if (r > 0 && c > 0) {
                    mat[r][c] -= mat[r-1][c-1];
                }
            }
        }
        
        return mat;
    }
}
```

  </div>

  <div class="tab-panel" data-lang="cpp">

```cpp
class Solution {
public:
    std::vector<std::vector<int>> rangeAddQueries(int n, std::vector<std::vector<int>>& queries) {
        // Initialize an n x n matrix with zeros. This will serve as our difference array.
        std::vector<std::vector<int>> mat(n, std::vector<int>(n, 0));

        // Process each query to populate the difference array
        for (const auto& query : queries) {
            int r1 = query[0];
            int c1 = query[1];
            int r2 = query[2];
            int c2 = query[3];

            // Add 1 at the top-left corner of the submatrix
            mat[r1][c1] += 1;

            // Subtract 1 at (r1, c2+1) to cancel effect for columns beyond c2
            if (c2 + 1 < n) {
                mat[r1][c2 + 1] -= 1;
            }
            
            // Subtract 1 at (r2+1, c1) to cancel effect for rows beyond r2
            if (r2 + 1 < n) {
                mat[r2 + 1][c1] -= 1;
            }
            
            // Add 1 at (r2+1, c2+1) to correct double subtraction for the region beyond r2 and c2
            if (r2 + 1 < n && c2 + 1 < n) {
                mat[r2 + 1][c2 + 1] += 1;
            }
        }
        
        // Compute the 2D prefix sums to get the final matrix values
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                // Add value from cell above (if not in first row)
                if (r > 0) {
                    mat[r][c] += mat[r-1][c];
                }
                
                // Add value from cell to the left (if not in first column)
                if (c > 0) {
                    mat[r][c] += mat[r][c-1];
                }
                
                // Subtract value from top-left diagonal (if not in first row or col)
                // This is because mat[r-1][c] and mat[r][c-1] both include mat[r-1][c-1],
                // so it's counted twice and needs to be subtracted once.
                if (r > 0 && c > 0) {
                    mat[r][c] -= mat[r-1][c-1];
                }
            }
        }
        
        return mat;
    }
};
```

  </div>

  <div class="tab-panel" data-lang="javascript">

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[][]}
 */
var rangeAddQueries = function(n, queries) {
    // Initialize an n x n matrix with zeros. This will serve as our difference array.
    const mat = Array(n).fill(0).map(() => Array(n).fill(0));

    // Process each query to populate the difference array
    for (const query of queries) {
        const r1 = query[0];
        const c1 = query[1];
        const r2 = query[2];
        const c2 = query[3];

        // Add 1 at the top-left corner of the submatrix
        mat[r1][c1] += 1;

        // Subtract 1 at (r1, c2+1) to cancel effect for columns beyond c2
        if (c2 + 1 < n) {
            mat[r1][c2 + 1] -= 1;
        }
        
        // Subtract 1 at (r2+1, c1) to cancel effect for rows beyond r2
        if (r2 + 1 < n) {
            mat[r2 + 1][c1] -= 1;
        }
        
        // Add 1 at (r2+1, c2+1) to correct double subtraction for the region beyond r2 and c2
        if (r2 + 1 < n && c2 + 1 < n) {
            mat[r2 + 1][c2 + 1] += 1;
        }
    }
    
    // Compute the 2D prefix sums to get the final matrix values
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            // Add value from cell above (if not in first row)
            if (r > 0) {
                mat[r][c] += mat[r-1][c];
            }
            
            // Add value from cell to the left (if not in first column)
            if (c > 0) {
                mat[r][c] += mat[r][c-1];
            }
            
            // Subtract value from top-left diagonal (if not in first row or col)
            // This is because mat[r-1][c] and mat[r][c-1] both include mat[r-1][c-1],
            // so it's counted twice and needs to be subtracted once.
            if (r > 0 && c > 0) {
                mat[r][c] -= mat[r-1][c-1];
            }
        }
    }
    
    return mat;
};
```

  </div>

  <div class="tab-panel" data-lang="typescript">

```typescript
function rangeAddQueries(n: number, queries: number[][]): number[][] {
    // Initialize an n x n matrix with zeros. This will serve as our difference array.
    const mat: number[][] = Array(n).fill(0).map(() => Array(n).fill(0));

    // Process each query to populate the difference array
    for (const query of queries) {
        const r1 = query[0];
        const c1 = query[1];
        const r2 = query[2];
        const c2 = query[3];

        // Add 1 at the top-left corner of the submatrix
        mat[r1][c1] += 1;

        // Subtract 1 at (r1, c2+1) to cancel effect for columns beyond c2
        if (c2 + 1 < n) {
            mat[r1][c2 + 1] -= 1;
        }
        
        // Subtract 1 at (r2+1, c1) to cancel effect for rows beyond r2
        if (r2 + 1 < n) {
            mat[r2 + 1][c1] -= 1;
        }
        
        // Add 1 at (r2+1, c2+1) to correct double subtraction for the region beyond r2 and c2
        if (r2 + 1 < n && c2 + 1 < n) {
            mat[r2 + 1][c2 + 1] += 1;
        }
    }
    
    // Compute the 2D prefix sums to get the final matrix values
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            // Add value from cell above (if not in first row)
            if (r > 0) {
                mat[r][c] += mat[r-1][c];
            }
            
            // Add value from cell to the left (if not in first column)
            if (c > 0) {
                mat[r][c] += mat[r][c-1];
            }
            
            // Subtract value from top-left diagonal (if not in first row or col)
            // This is because mat[r-1][c] and mat[r][c-1] both include mat[r-1][c-1],
            // so it's counted twice and needs to be subtracted once.
            if (r > 0 && c > 0) {
                mat[r][c] -= mat[r-1][c-1];
            }
        }
    }
    
    return mat;
}
```

  </div>

  <div class="tab-panel" data-lang="go">

```go
func rangeAddQueries(n int, queries [][]int) [][]int {
    // Initialize an n x n matrix with zeros. This will serve as our difference array.
    mat := make([][]int, n)
    for i := range mat {
        mat[i] = make([]int, n)
    }

    // Process each query to populate the difference array
    for _, query := range queries {
        r1, c1, r2, c2 := query[0], query[1], query[2], query[3]

        // Add 1 at the top-left corner of the submatrix
        mat[r1][c1] += 1

        // Subtract 1 at (r1, c2+1) to cancel effect for columns beyond c2
        if c2 + 1 < n {
            mat[r1][c2 + 1] -= 1
        }
        
        // Subtract 1 at (r2+1, c1) to cancel effect for rows beyond r2
        if r2 + 1 < n {
            mat[r2 + 1][c1] -= 1
        }
        
        // Add 1 at (r2+1, c2+1) to correct double subtraction for the region beyond r2 and c2
        if r2 + 1 < n && c2 + 1 < n {
            mat[r2 + 1][c2 + 1] += 1
        }
    }
    
    // Compute the 2D prefix sums to get the final matrix values
    for r := 0; r < n; r++ {
        for c := 0; c < n; c++ {
            // Add value from cell above (if not in first row)
            if r > 0 {
                mat[r][c] += mat[r-1][c]
            }
            
            // Add value from cell to the left (if not in first column)
            if c > 0 {
                mat[r][c] += mat[r][c-1]
            }
            
            // Subtract value from top-left diagonal (if not in first row or col)
            // This is because mat[r-1][c] and mat[r][c-1] both include mat[r-1][c-1],
            // so it's counted twice and needs to be subtracted once.
            if r > 0 && c > 0 {
                mat[r][c] -= mat[r-1][c-1]
            }
        }
    }
    
    return mat
}
```

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N^2 + Q)

- **Space Complexity:** O(N^2)
