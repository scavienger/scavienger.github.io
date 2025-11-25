---
layout: post
title: "Count Unguarded Cells in the Grid"
date: 2025-11-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
---

## Problem #2257: Count Unguarded Cells in the Grid

**Difficulty:** Medium

**Topics:** Array, Matrix, Simulation

## Problem Description

<p>You are given two integers <code>m</code> and <code>n</code> representing a <strong>0-indexed</strong> <code>m x n</code> grid. You are also given two 2D integer arrays <code>guards</code> and <code>walls</code> where <code>guards[i] = [row<sub>i</sub>, col<sub>i</sub>]</code> and <code>walls[j] = [row<sub>j</sub>, col<sub>j</sub>]</code> represent the positions of the <code>i<sup>th</sup></code> guard and <code>j<sup>th</sup></code> wall respectively.</p>

<p>A guard can see <b>every</b> cell in the four cardinal directions (north, east, south, or west) starting from their position unless <strong>obstructed</strong> by a wall or another guard. A cell is <strong>guarded</strong> if there is <strong>at least</strong> one guard that can see it.</p>

<p>Return<em> the number of unoccupied cells that are <strong>not</strong> <strong>guarded</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png" style="width: 300px; height: 204px;" />
<pre>
<strong>Input:</strong> m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png" style="width: 200px; height: 201px;" />
<pre>
<strong>Input:</strong> m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= guards.length, walls.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= guards.length + walls.length &lt;= m * n</code></li>
	<li><code>guards[i].length == walls[j].length == 2</code></li>
	<li><code>0 &lt;= row<sub>i</sub>, row<sub>j</sub> &lt; m</code></li>
	<li><code>0 &lt;= col<sub>i</sub>, col<sub>j</sub> &lt; n</code></li>
	<li>All the positions in <code>guards</code> and <code>walls</code> are <strong>unique</strong>.</li>
</ul>


## Hints

1. Create a 2D array to represent the grid. Can you mark the tiles that can be seen by a guard?

2. Iterate over the guards, and for each of the 4 directions, advance the current tile and mark the tile. When should you stop advancing?

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-23 07:25:26 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

Initialize a grid marking walls and guards. For each guard, simulate its line of sight in four directions, marking visible empty cells as guarded until an obstruction (wall or another guard) is encountered. Finally, count the remaining empty, unmarked cells.

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
    int countUnguarded(int m, int n, std::vector<std::vector<int>>& guards, std::vector<std::vector<int>>& walls) {
        std::vector<std::vector<int>> grid(m, std::vector<int>(n, 0));

        for (const auto& wall : walls) {
            grid[wall[0]][wall[1]] = 1;
        }

        for (const auto& guard : guards) {
            grid[guard[0]][guard[1]] = 2;
        }

        std::vector<std::pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (const auto& guard_pos : guards) {
            int gr = guard_pos[0];
            int gc = guard_pos[1];

            for (const auto& dir : directions) {
                int dr = dir.first;
                int dc = dir.second;

                int r = gr + dr;
                int c = gc + dc;

                while (r >= 0 && r < m && c >= 0 && c < n) {
                    if (grid[r][c] == 1 || grid[r][c] == 2) {
                        break;
                    }

                    if (grid[r][c] == 0) {
                        grid[r][c] = 3;
                    }

                    r += dr;
                    c += dc;
                }
            }
        }

        int unguarded_count = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 0) {
                    unguarded_count += 1;
                }
            }
        }

        return unguarded_count;
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
    public int countUnguarded(int m, int n, List<List<Integer>> guards, List<List<Integer>> walls) {
        int[][] grid = new int[m][n];

        for (List<Integer> wall : walls) {
            grid[wall.get(0)][wall.get(1)] = 1;
        }

        for (List<Integer> guard : guards) {
            grid[guard.get(0)][guard.get(1)] = 2;
        }

        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (List<Integer> guard_pos : guards) {
            int gr = guard_pos.get(0);
            int gc = guard_pos.get(1);

            for (int[] dir : directions) {
                int dr = dir[0];
                int dc = dir[1];

                int r = gr + dr;
                int c = gc + dc;

                while (r >= 0 && r < m && c >= 0 && c < n) {
                    if (grid[r][c] == 1 || grid[r][c] == 2) {
                        break;
                    }

                    if (grid[r][c] == 0) {
                        grid[r][c] = 3;
                    }

                    r += dr;
                    c += dc;
                }
            }
        }

        int unguarded_count = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 0) {
                    unguarded_count += 1;
                }
            }
        }

        return unguarded_count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 1

        for r, c in guards:
            grid[r][c] = 2

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 1 or grid[r][c] == 2:
                        break

                    if grid[r][c] == 0:
                        grid[r][c] = 3

                    r += dr
                    c += dc

        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded_count += 1

        return unguarded_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 1

        for r, c in guards:
            grid[r][c] = 2

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 1 or grid[r][c] == 2:
                        break

                    if grid[r][c] == 0:
                        grid[r][c] = 3

                    r += dr
                    c += dc

        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded_count += 1

        return unguarded_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int countUnguarded(int m, int n, int** guards, int guardsSize, int* guardsColSize, int** walls, int wallsSize, int* wallsColSize) {
    int* grid = (int*)malloc(m * n * sizeof(int));
    if (grid == NULL) return -1;
    memset(grid, 0, m * n * sizeof(int));

    for (int i = 0; i < wallsSize; ++i) {
        grid[walls[i][0] * n + walls[i][1]] = 1;
    }

    for (int i = 0; i < guardsSize; ++i) {
        grid[guards[i][0] * n + guards[i][1]] = 2;
    }

    int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    for (int i = 0; i < guardsSize; ++i) {
        int gr = guards[i][0];
        int gc = guards[i][1];

        for (int d = 0; d < 4; ++d) {
            int dr = directions[d][0];
            int dc = directions[d][1];

            int r = gr + dr;
            int c = gc + dc;

            while (r >= 0 && r < m && c >= 0 && c < n) {
                if (grid[r * n + c] == 1 || grid[r * n + c] == 2) {
                    break;
                }

                if (grid[r * n + c] == 0) {
                    grid[r * n + c] = 3;
                }

                r += dr;
                c += dc;
            }
        }
    }

    int unguarded_count = 0;
    for (int r = 0; r < m; ++r) {
        for (int c = 0; c < n; ++c) {
            if (grid[r * n + c] == 0) {
                unguarded_count += 1;
            }
        }
    }

    free(grid);
    return unguarded_count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int CountUnguarded(int m, int n, IList<IList<int>> guards, IList<IList<int>> walls) {
        int[][] grid = new int[m][];
        for (int i = 0; i < m; i++) {
            grid[i] = new int[n];
        }

        foreach (var wall in walls) {
            grid[wall[0]][wall[1]] = 1;
        }

        foreach (var guard in guards) {
            grid[guard[0]][guard[1]] = 2;
        }

        int[][] directions = new int[][] {
            new int[] {0, 1},
            new int[] {0, -1},
            new int[] {1, 0},
            new int[] {-1, 0}
        };

        foreach (var guard_pos in guards) {
            int gr = guard_pos[0];
            int gc = guard_pos[1];

            foreach (var dir in directions) {
                int dr = dir[0];
                int dc = dir[1];

                int r = gr + dr;
                int c = gc + dc;

                while (r >= 0 && r < m && c >= 0 && c < n) {
                    if (grid[r][c] == 1 || grid[r][c] == 2) {
                        break;
                    }

                    if (grid[r][c] == 0) {
                        grid[r][c] = 3;
                    }

                    r += dr;
                    c += dc;
                }
            }
        }

        int unguarded_count = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 0) {
                    unguarded_count += 1;
                }
            }
        }

        return unguarded_count;
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
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    const grid = Array(m).fill(0).map(() => Array(n).fill(0));

    for (const [r, c] of walls) {
        grid[r][c] = 1;
    }

    for (const [r, c] of guards) {
        grid[r][c] = 2;
    }

    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    for (const [gr, gc] of guards) {
        for (const [dr, dc] of directions) {
            let r = gr + dr;
            let c = gc + dc;

            while (r >= 0 && r < m && c >= 0 && c < n) {
                if (grid[r][c] === 1 || grid[r][c] === 2) {
                    break;
                }

                if (grid[r][c] === 0) {
                    grid[r][c] = 3;
                }

                r += dr;
                c += dc;
            }
        }
    }

    let unguarded_count = 0;
    for (let r = 0; r < m; ++r) {
        for (let c = 0; c < n; ++c) {
            if (grid[r][c] === 0) {
                unguarded_count += 1;
            }
        }
    }

    return unguarded_count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    const grid: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));

    for (const [r, c] of walls) {
        grid[r][c] = 1;
    }

    for (const [r, c] of guards) {
        grid[r][c] = 2;
    }

    const directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];

    for (const [gr, gc] of guards) {
        for (const [dr, dc] of directions) {
            let r: number = gr + dr;
            let c: number = gc + dc;

            while (r >= 0 && r < m && c >= 0 && c < n) {
                if (grid[r][c] === 1 || grid[r][c] === 2) {
                    break;
                }

                if (grid[r][c] === 0) {
                    grid[r][c] = 3;
                }

                r += dr;
                c += dc;
            }
        }
    }

    let unguarded_count: number = 0;
    for (let r = 0; r < m; ++r) {
        for (let c = 0; c < n; ++c) {
            if (grid[r][c] === 0) {
                unguarded_count += 1;
            }
        }
    }

    return unguarded_count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class Solution {

    function countUnguarded($m, $n, $guards, $walls) {
        $grid = array_fill(0, $m, array_fill(0, $n, 0));

        foreach ($walls as $wall) {
            $grid[$wall[0]][$wall[1]] = 1;
        }

        foreach ($guards as $guard) {
            $grid[$guard[0]][$guard[1]] = 2;
        }

        $directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];

        foreach ($guards as $guard_pos) {
            $gr = $guard_pos[0];
            $gc = $guard_pos[1];

            foreach ($directions as $dir) {
                $dr = $dir[0];
                $dc = $dir[1];

                $r = $gr + $dr;
                $c = $gc + $dc;

                while ($r >= 0 && $r < $m && $c >= 0 && $c < $n) {
                    if ($grid[$r][$c] == 1 || $grid[$r][$c] == 2) {
                        break;
                    }

                    if ($grid[$r][$c] == 0) {
                        $grid[$r][$c] = 3;
                    }

                    $r += $dr;
                    $c += $dc;
                }
            }
        }

        $unguarded_count = 0;
        for ($r = 0; $r < $m; ++$r) {
            for ($c = 0; $c < $n; ++$c) {
                if ($grid[$r][$c] == 0) {
                    $unguarded_count += 1;
                }
            }
        }

        return $unguarded_count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countUnguarded(_ m: Int, _ n: Int, _ guards: [[Int]], _ walls: [[Int]]) -> Int {
        var grid = Array(repeating: Array(repeating: 0, count: n), count: m);

        for wall in walls {
            grid[wall[0]][wall[1]] = 1;
        }

        for guardPos in guards {
            grid[guardPos[0]][guardPos[1]] = 2;
        }

        let directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];

        for guardPos in guards {
            let gr = guardPos[0];
            let gc = guardPos[1];

            for dir in directions {
                let dr = dir[0];
                let dc = dir[1];

                var r = gr + dr;
                var c = gc + dc;

                while r >= 0 && r < m && c >= 0 && c < n {
                    if grid[r][c] == 1 || grid[r][c] == 2 {
                        break;
                    }

                    if grid[r][c] == 0 {
                        grid[r][c] = 3;
                    }

                    r += dr;
                    c += dc;
                }
            }
        }

        var unguardedCount = 0;
        for r in 0..<m {
            for c in 0..<n {
                if grid[r][c] == 0 {
                    unguardedCount += 1;
                }
            }
        }

        return unguardedCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countUnguarded(m: Int, n: Int, guards: List<List<Int>>, walls: List<List<Int>>): Int {
        val grid = Array(m) { IntArray(n) { 0 } }

        for (wall in walls) {
            grid[wall[0]][wall[1]] = 1
        }

        for (guard in guards) {
            grid[guard[0]][guard[1]] = 2
        }

        val directions = arrayOf(intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(-1, 0))

        for (guardPos in guards) {
            val gr = guardPos[0]
            val gc = guardPos[1]

            for (dir in directions) {
                val dr = dir[0]
                val dc = dir[1]

                var r = gr + dr
                var c = gc + dc

                while (r >= 0 && r < m && c >= 0 && c < n) {
                    if (grid[r][c] == 1 || grid[r][c] == 2) {
                        break
                    }

                    if (grid[r][c] == 0) {
                        grid[r][c] = 3
                    }

                    r += dr
                    c += dc
                }
            }
        }

        var unguardedCount = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (grid[r][c] == 0) {
                    unguardedCount += 1
                }
            }
        }

        return unguardedCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countUnguarded(int m, int n, List<List<int>> guards, List<List<int>> walls) {
    List<List<int>> grid = List.generate(m, (_) => List.filled(n, 0));

    for (final wall in walls) {
      grid[wall[0]][wall[1]] = 1;
    }

    for (final guard in guards) {
      grid[guard[0]][guard[1]] = 2;
    }

    List<List<int>> directions = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0]
    ];

    for (final guardPos in guards) {
      int gr = guardPos[0];
      int gc = guardPos[1];

      for (final dir in directions) {
        int dr = dir[0];
        int dc = dir[1];

        int r = gr + dr;
        int c = gc + dc;

        while (r >= 0 && r < m && c >= 0 && c < n) {
          if (grid[r][c] == 1 || grid[r][c] == 2) {
            break;
          }

          if (grid[r][c] == 0) {
            grid[r][c] = 3;
          }

          r += dr;
          c += dc;
        }
      }
    }

    int unguardedCount = 0;
    for (int r = 0; r < m; ++r) {
      for (int c = 0; c < n; ++c) {
        if (grid[r][c] == 0) {
          unguardedCount += 1;
        }
      }
    }

    return unguardedCount;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    grid := make([][]int, m)
    for i := range grid {
        grid[i] = make([]int, n)
    }

    for _, wall := range walls {
        grid[wall[0]][wall[1]] = 1
    }

    for _, guard := range guards {
        grid[guard[0]][guard[1]] = 2
    }

    directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

    for _, guard_pos := range guards {
        gr := guard_pos[0]
        gc := guard_pos[1]

        for _, dir := range directions {
            dr := dir[0]
            dc := dir[1]

            r := gr + dr
            c := gc + dc

            for r >= 0 && r < m && c >= 0 && c < n {
                if grid[r][c] == 1 || grid[r][c] == 2 {
                    break
                }

                if grid[r][c] == 0 {
                    grid[r][c] = 3
                }

                r += dr
                c += dc
            }
        }
    }

    unguarded_count := 0
    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            if grid[r][c] == 0 {
                unguarded_count += 1
            }
        }
    }

    return unguarded_count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def count_unguarded(m, n, guards, walls)
        grid = Array.new(m) { Array.new(n, 0) }

        walls.each do |r, c|
            grid[r][c] = 1
        end

        guards.each do |r, c|
            grid[r][c] = 2
        end

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        guards.each do |gr, gc|
            directions.each do |dr, dc|
                r, c = gr + dr, gc + dc
                while r >= 0 && r < m && c >= 0 && c < n
                    if grid[r][c] == 1 || grid[r][c] == 2
                        break
                    end

                    if grid[r][c] == 0
                        grid[r][c] = 3
                    end

                    r += dr
                    c += dc
                end
            end
        end

        unguarded_count = 0
        (0...m).each do |r|
            (0...n).each do |c|
                if grid[r][c] == 0
                    unguarded_count += 1
                end
            end
        end

        unguarded_count
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

object Solution {
    def countUnguarded(m: Int, n: Int, guards: List[List[Int]], walls: List[List[Int]]): Int = {
        val grid: Array[Array[Int]] = Array.ofDim[Int](m, n)

        for (wall <- walls) {
            grid(wall(0))(wall(1)) = 1
        }

        for (guardPos <- guards) {
            grid(guardPos(0))(guardPos(1)) = 2
        }

        val directions = Array((0, 1), (0, -1), (1, 0), (-1, 0))

        for (guardPos <- guards) {
            val gr = guardPos(0)
            val gc = guardPos(1)

            for (dir <- directions) {
                val dr = dir._1
                val dc = dir._2

                var r = gr + dr
                var c = gc + dc

                while (r >= 0 && r < m && c >= 0 && c < n) {
                    if (grid(r)(c) == 1 || grid(r)(c) == 2) {
                        break
                    }

                    if (grid(r)(c) == 0) {
                        grid(r)(c) = 3
                    }

                    r += dr
                    c += dc
                }
            }
        }

        var unguardedCount = 0
        for (r <- 0 until m) {
            for (c <- 0 until n) {
                if (grid(r)(c) == 0) {
                    unguardedCount += 1
                }
            }
        }

        unguardedCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_unguarded(m: i32, n: i32, guards: Vec<Vec<i32>>, walls: Vec<Vec<i32>>) -> i32 {
        let m_usize = m as usize;
        let n_usize = n as usize;

        let mut grid = vec![vec![0; n_usize]; m_usize];

        for wall in walls {
            grid[wall[0] as usize][wall[1] as usize] = 1;
        }

        for guard_pos in &guards {
            grid[guard_pos[0] as usize][guard_pos[1] as usize] = 2;
        }

        let directions = [(0, 1), (0, -1), (1, 0), (-1, 0)];

        for guard_pos in guards {
            let gr = guard_pos[0];
            let gc = guard_pos[1];

            for (dr, dc) in directions.iter() {
                let mut r = gr + dr;
                let mut c = gc + dc;

                while r >= 0 && r < m && c >= 0 && c < n {
                    let r_usize = r as usize;
                    let c_usize = c as usize;

                    if grid[r_usize][c_usize] == 1 || grid[r_usize][c_usize] == 2 {
                        break;
                    }

                    if grid[r_usize][c_usize] == 0 {
                        grid[r_usize][c_usize] = 3;
                    }

                    r += dr;
                    c += dc;
                }
            }
        }

        let mut unguarded_count = 0;
        for r in 0..m_usize {
            for c in 0..n_usize {
                if grid[r][c] == 0 {
                    unguarded_count += 1;
                }
            }
        }

        unguarded_count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-unguarded m n guards walls)
  (define grid (build-vector m (lambda (r) (build-vector n (lambda (c) 0)))))

  (for-each (lambda (wall)
              (vector-set! (vector-ref grid (car wall)) (cadr wall) 1))
            walls)

  (for-each (lambda (guard)
              (vector-set! (vector-ref grid (car guard)) (cadr guard) 2))
            guards)

  (define directions '((0 1) (0 -1) (1 0) (-1 0)))

  (for-each (lambda (guard-pos)
              (define gr (car guard-pos))
              (define gc (cadr guard-pos))

              (for-each (lambda (dir)
                          (define dr (car dir))
                          (define dc (cadr dir))

                          (let loop ((r (+ gr dr)) (c (+ gc dc)))
                            (when (and (>= r 0) (< r m) (>= c 0) (< c n))
                              (define current-cell (vector-ref (vector-ref grid r) c))
                              (unless (or (= current-cell 1) (= current-cell 2))
                                (when (= current-cell 0)
                                  (vector-set! (vector-ref grid r) c 3))

                                (loop (+ r dr) (+ c dc)))))))
            guards)

  (define unguarded-count 0)
  (for ([r (in-range m)])
    (for ([c (in-range n)])
      (when (= (vector-ref (vector-ref grid r) c) 0)
        (set! unguarded-count (+ unguarded-count 1)))))

  unguarded-count)

(provide (all-defined-out))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_unguarded/4]).

count_unguarded(M, N, Guards, Walls) ->
    GridSize = M * N,
    InitialGrid = array:new(GridSize, 0),

    GridWithWalls = lists:foldl(
        fun([R, C], AccGrid) ->
            array:set(R * N + C, 1, AccGrid)
        end, InitialGrid, Walls),

    GridWithGuards = lists:foldl(
        fun([R, C], AccGrid) ->
            array:set(R * N + C, 2, AccGrid)
        end, GridWithWalls, Guards),

    Directions = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}],

    FinalGrid = lists:foldl(
        fun([Gr, Gc], CurrentGrid) ->
            lists:foldl(
                fun({Dr, Dc}, InnerGrid) ->
                    propagate_guard_vision(Gr, Gc, Dr, Dc, M, N, InnerGrid)
                end, CurrentGrid, Directions)
        end, GridWithGuards, Guards),

    count_unguarded_cells(M, N, FinalGrid, 0).

propagate_guard_vision(Gr, Gc, Dr, Dc, M, N, Grid) ->
    R = Gr + Dr,
    C = Gc + Dc,
    propagate_guard_vision_loop(R, C, Dr, Dc, M, N, Grid).

propagate_guard_vision_loop(R, C, Dr, Dc, M, N, Grid) ->
    if
        R >= 0 andalso R < M andalso C >= 0 andalso C < N ->
            CurrentCell = array:get(R * N + C, Grid),
            if
                CurrentCell == 1; CurrentCell == 2 ->
                    Grid;
                true ->
                    NewGrid = if
                        CurrentCell == 0 ->
                            array:set(R * N + C, 3, Grid);
                        true ->
                            Grid
                    end,
                    propagate_guard_vision_loop(R + Dr, C + Dc, Dr, Dc, M, N, NewGrid)
            end;
        true ->
            Grid
    end.

count_unguarded_cells(M, N, Grid, Count) ->
    count_unguarded_cells_loop(0, 0, M, N, Grid, Count).

count_unguarded_cells_loop(R, C, M, N, Grid, Acc) ->
    if
        R < M ->
            if
                C < N ->
                    CurrentCell = array:get(R * N + C, Grid),
                    NewAcc = if CurrentCell == 0 -> Acc + 1; true -> Acc end,
                    count_unguarded_cells_loop(R, C + 1, M, N, Grid, NewAcc);
                true ->
                    count_unguarded_cells_loop(R + 1, 0, M, N, Grid, Acc)
            end;
        true ->
            Acc
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def count_unguarded(m, n, guards, walls) do
    grid_size = m * n
    initial_grid = :array.new(grid_size, 0)

    grid_with_walls = Enum.reduce(walls, initial_grid, fn [r, c], acc_grid ->
      :array.set(r * n + c, 1, acc_grid)
    end)

    grid_with_guards = Enum.reduce(guards, grid_with_walls, fn [r, c], acc_grid ->
      :array.set(r * n + c, 2, acc_grid)
    end)

    directions = [{0, 1}, {0, -1}, {1, 0}, {-1, 0}]

    final_grid = Enum.reduce(guards, grid_with_guards, fn [gr, gc], current_grid ->
      Enum.reduce(directions, current_grid, fn {dr, dc}, inner_grid ->
        propagate_guard_vision(gr, gc, dr, dc, m, n, inner_grid)
      end)
    end)

    count_unguarded_cells(m, n, final_grid, 0)
  end

  defp propagate_guard_vision(gr, gc, dr, dc, m, n, grid) do
    r = gr + dr
    c = gc + dc
    propagate_guard_vision_loop(r, c, dr, dc, m, n, grid)
  end

  defp propagate_guard_vision_loop(r, c, dr, dc, m, n, grid) do
    if r >= 0 and r < m and c >= 0 and c < n do
      current_cell = :array.get(r * n + c, grid)
      cond do
        current_cell == 1 or current_cell == 2 ->
          grid
        true ->
          new_grid = if current_cell == 0 do
            :array.set(r * n + c, 3, grid)
          else
            grid
          end
          propagate_guard_vision_loop(r + dr, c + dc, dr, dc, m, n, new_grid)
      end
    else
      grid
    end
  end

  defp count_unguarded_cells(m, n, grid, count) do
    count_unguarded_cells_loop(0, 0, m, n, grid, count)
  end

  defp count_unguarded_cells_loop(r, c, m, n, grid, acc) do
    if r < m do
      if c < n do
        current_cell = :array.get(r * n + c, grid)
        new_acc = if current_cell == 0, do: acc + 1, else: acc
        count_unguarded_cells_loop(r, c + 1, m, n, grid, new_acc)
      else
        count_unguarded_cells_loop(r + 1, 0, m, n, grid, acc)
      end
    else
      acc
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n)

- **Space Complexity:** O(m * n)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 07:25:42 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

Create a 2D array to represent the grid and mark the tiles that can be seen by a guard. Iterate over the guards and mark the tiles in the four cardinal directions.

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
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<int>> grid(m, vector<int>(n, 0));
        for (auto& wall : walls) {
            grid[wall[0]][wall[1]] = -1;
        }
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    bool seen = false;
                    for (auto& guard : guards) {
                        if (canSee(grid, i, j, guard[0], guard[1])) {
                            seen = true;
                            break;
                        }
                    }
                    if (!seen) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    bool canSee(vector<vector<int>>& grid, int x, int y, int guardX, int guardY) {
        int dx = x - guardX;
        int dy = y - guardY;
        if (dx == 0) {
            for (int i = min(y, guardY) + 1; i < max(y, guardY); i++) {
                if (grid[x][i] == -1) {
                    return false;
                }
            }
        } else if (dy == 0) {
            for (int i = min(x, guardX) + 1; i < max(x, guardX); i++) {
                if (grid[i][y] == -1) {
                    return false;
                }
            }
        } else {
            return false;
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
public class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] grid = new int[m][n];
        for (int[] wall : walls) {
            grid[wall[0]][wall[1]] = -1;
        }
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    boolean seen = false;
                    for (int[] guard : guards) {
                        if (canSee(grid, i, j, guard[0], guard[1])) {
                            seen = true;
                            break;
                        }
                    }
                    if (!seen) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    boolean canSee(int[][] grid, int x, int y, int guardX, int guardY) {
        int dx = x - guardX;
        int dy = y - guardY;
        if (dx == 0) {
            for (int i = Math.min(y, guardY) + 1; i < Math.max(y, guardY); i++) {
                if (grid[x][i] == -1) {
                    return false;
                }
            }
        } else if (dy == 0) {
            for (int i = Math.min(x, guardX) + 1; i < Math.max(x, guardX); i++) {
                if (grid[i][y] == -1) {
                    return false;
                }
            }
        } else {
            return false;
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
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in walls:
            grid[x][y] = -1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = False
                    for x, y in guards:
                        if self.canSee(grid, i, j, x, y):
                            seen = True
                            break
                    if not seen:
                        count += 1
        return count

    def canSee(self, grid, x, y, guardX, guardY):
        dx = x - guardX
        dy = y - guardY
        if dx == 0:
            for i in range(min(y, guardY) + 1, max(y, guardY)):
                if grid[x][i] == -1:
                    return False
        elif dy == 0:
            for i in range(min(x, guardX) + 1, max(x, guardX)):
                if grid[i][y] == -1:
                    return False
        else:
            return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in walls:
            grid[x][y] = -1
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = False
                    for x, y in guards:
                        if self.canSee(grid, i, j, x, y):
                            seen = True
                            break
                    if not seen:
                        count += 1
        return count

    def canSee(self, grid, x, y, guardX, guardY):
        dx = x - guardX
        dy = y - guardY
        if dx == 0:
            for i in range(min(y, guardY) + 1, max(y, guardY)):
                if grid[x][i] == -1:
                    return False
        elif dy == 0:
            for i in range(min(x, guardX) + 1, max(x, guardX)):
                if grid[i][y] == -1:
                    return False
        else:
            return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

int canSee(int** grid, int m, int n, int x, int y, int guardX, int guardY) {
    int dx = x - guardX;
    int dy = y - guardY;
    if (dx == 0) {
        for (int i = (y < guardY ? y + 1 : guardY + 1); i < (y > guardY ? y : guardY); i++) {
            if (grid[x][i] == -1) {
                return 0;
            }
        }
    } else if (dy == 0) {
        for (int i = (x < guardX ? x + 1 : guardX + 1); i < (x > guardX ? x : guardX); i++) {
            if (grid[i][y] == -1) {
                return 0;
            }
        }
    } else {
        return 0;
    }
    return 1;
}

int countUnguarded(int m, int n, int** guards, int guardsSize, int* guardsColSize, int** walls, int wallsSize, int* wallsColSize) {
    int** grid = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        grid[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) {
            grid[i][j] = 0;
        }
    }
    for (int i = 0; i < wallsSize; i++) {
        grid[walls[i][0]][walls[i][1]] = -1;
    }
    int count = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                int seen = 0;
                for (int k = 0; k < guardsSize; k++) {
                    if (canSee(grid, m, n, i, j, guards[k][0], guards[k][1])) {
                        seen = 1;
                        break;
                    }
                }
                if (!seen) {
                    count++;
                }
            }
        }
    }
    for (int i = 0; i < m; i++) {
        free(grid[i]);
    }
    free(grid);
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] grid = new int[m][];
        for (int i = 0; i < m; i++) {
            grid[i] = new int[n];
        }
        foreach (int[] wall in walls) {
            grid[wall[0]][wall[1]] = -1;
        }
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    bool seen = false;
                    foreach (int[] guard in guards) {
                        if (CanSee(grid, i, j, guard[0], guard[1])) {
                            seen = true;
                            break;
                        }
                    }
                    if (!seen) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    bool CanSee(int[][] grid, int x, int y, int guardX, int guardY) {
        int dx = x - guardX;
        int dy = y - guardY;
        if (dx == 0) {
            for (int i = Math.Min(y, guardY) + 1; i < Math.Max(y, guardY); i++) {
                if (grid[x][i] == -1) {
                    return false;
                }
            }
        } else if (dy == 0) {
            for (int i = Math.Min(x, guardX) + 1; i < Math.Max(x, guardX); i++) {
                if (grid[i][y] == -1) {
                    return false;
                }
            }
        } else {
            return false;
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
var countUnguarded = function(m, n, guards, walls) {
    let grid = Array(m).fill(0).map(() => Array(n).fill(0));
    for (let [x, y] of walls) {
        grid[x][y] = -1;
    }
    let count = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                let seen = false;
                for (let [x, y] of guards) {
                    if (canSee(grid, i, j, x, y)) {
                        seen = true;
                        break;
                    }
                }
                if (!seen) {
                    count++;
                }
            }
        }
    }
    return count;

    function canSee(grid, x, y, guardX, guardY) {
        let dx = x - guardX;
        let dy = y - guardY;
        if (dx == 0) {
            for (let i = Math.min(y, guardY) + 1; i < Math.max(y, guardY); i++) {
                if (grid[x][i] == -1) {
                    return false;
                }
            }
        } else if (dy == 0) {
            for (let i = Math.min(x, guardX) + 1; i < Math.max(x, guardX); i++) {
                if (grid[i][y] == -1) {
                    return false;
                }
            }
        } else {
            return false;
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    let grid: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
    for (let [x, y] of walls) {
        grid[x][y] = -1;
    }
    let count: number = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                let seen: boolean = false;
                for (let [x, y] of guards) {
                    if (canSee(grid, i, j, x, y)) {
                        seen = true;
                        break;
                    }
                }
                if (!seen) {
                    count++;
                }
            }
        }
    }
    return count;

    function canSee(grid: number[][], x: number, y: number, guardX: number, guardY: number): boolean {
        let dx: number = x - guardX;
        let dy: number = y - guardY;
        if (dx == 0) {
            for (let i: number = Math.min(y, guardY) + 1; i < Math.max(y, guardY); i++) {
                if (grid[x][i] == -1) {
                    return false;
                }
            }
        } else if (dy == 0) {
            for (let i: number = Math.min(x, guardX) + 1; i < Math.max(x, guardX); i++) {
                if (grid[i][y] == -1) {
                    return false;
                }
            }
        } else {
            return false;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countUnguarded($m, $n, $guards, $walls) {
        $grid = array_fill(0, $m, array_fill(0, $n, 0));
        foreach ($walls as $wall) {
            $grid[$wall[0]][$wall[1]] = -1;
        }
        $count = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($grid[$i][$j] == 0) {
                    $seen = false;
                    foreach ($guards as $guard) {
                        if ($this->canSee($grid, $i, $j, $guard[0], $guard[1])) {
                            $seen = true;
                            break;
                        }
                    }
                    if (!$seen) {
                        $count++;
                    }
                }
            }
        }
        return $count;
    }

    function canSee($grid, $x, $y, $guardX, $guardY) {
        $dx = $x - $guardX;
        $dy = $y - $guardY;
        if ($dx == 0) {
            for ($i = min($y, $guardY) + 1; $i < max($y, $guardY); $i++) {
                if ($grid[$x][$i] == -1) {
                    return false;
                }
            }
        } else if ($dy == 0) {
            for ($i = min($x, $guardX) + 1; $i < max($x, $guardX); $i++) {
                if ($grid[$i][$y] == -1) {
                    return false;
                }
            }
        } else {
            return false;
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
    func countUnguarded(_ m: Int, _ n: Int, _ guards: [[Int]], _ walls: [[Int]]) -> Int {
        var grid = Array(repeating: Array(repeating: 0, count: n), count: m)
        for wall in walls {
            grid[wall[0]][wall[1]] = -1
        }
        var count = 0
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 0 {
                    var seen = false
                    for guard in guards {
                        if canSee(&grid, i, j, guard[0], guard[1]) {
                            seen = true
                            break
                        }
                    }
                    if !seen {
                        count += 1
                    }
                }
            }
        }
        return count
    }

    func canSee(_ grid: inout [[Int]], _ x: Int, _ y: Int, _ guardX: Int, _ guardY: Int) -> Bool {
        let dx = x - guardX
        let dy = y - guardY
        if dx == 0 {
            for i in min(y, guardY) + 1..<max(y, guardY) {
                if grid[x][i] == -1 {
                    return false
                }
            }
        } else if dy == 0 {
            for i in min(x, guardX) + 1..<max(x, guardX) {
                if grid[i][y] == -1 {
                    return false
                }
            }
        } else {
            return false
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
    fun countUnguarded(m: Int, n: Int, guards: Array<IntArray>, walls: Array<IntArray>): Int {
        val grid = Array(m) { IntArray(n) }
        for (wall in walls) {
            grid[wall[0]][wall[1]] = -1
        }
        var count = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 0) {
                    var seen = false
                    for (guard in guards) {
                        if (canSee(grid, i, j, guard[0], guard[1])) {
                            seen = true
                            break
                        }
                    }
                    if (!seen) {
                        count++
                    }
                }
            }
        }
        return count
    }

    fun canSee(grid: Array<IntArray>, x: Int, y: Int, guardX: Int, guardY: Int): Boolean {
        val dx = x - guardX
        val dy = y - guardY
        if (dx == 0) {
            for (i in minOf(y, guardY) + 1 until maxOf(y, guardY)) {
                if (grid[x][i] == -1) {
                    return false
                }
            }
        } else if (dy == 0) {
            for (i in minOf(x, guardX) + 1 until maxOf(x, guardX)) {
                if (grid[i][y] == -1) {
                    return false
                }
            }
        } else {
            return false
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
  int countUnguarded(int m, int n, List<List<int>> guards, List<List<int>> walls) {
      List<List<int>> grid = List.generate(m, (i) => List.generate(n, (j) => 0));
      for (var wall in walls) {
          grid[wall[0]][wall[1]] = -1;
      }
      int count = 0;
      for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
              if (grid[i][j] == 0) {
                  bool seen = false;
                  for (var guard in guards) {
                      if (canSee(grid, i, j, guard[0], guard[1])) {
                          seen = true;
                          break;
                      }
                  }
                  if (!seen) {
                      count++;
                  }
              }
          }
      }
      return count;
  }

  bool canSee(List<List<int>> grid, int x, int y, int guardX, int guardY) {
      int dx = x - guardX;
      int dy = y - guardY;
      if (dx == 0) {
          for (int i = min(y, guardY) + 1; i < max(y, guardY); i++) {
              if (grid[x][i] == -1) {
                  return false;
              }
          }
      } else if (dy == 0) {
          for (int i = min(x, guardX) + 1; i < max(x, guardX); i++) {
              if (grid[i][y] == -1) {
                  return false;
              }
          }
      } else {
          return false;
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
package main

import (
    "fmt"
)

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    grid := make([][]int, m)
    for i := range grid {
        grid[i] = make([]int, n)
    }
    for _, wall := range walls {
        grid[wall[0]][wall[1]] = -1
    }
    count := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 0 {
                seen := false
                for _, guard := range guards {
                    if canSee(grid, i, j, guard[0], guard[1]) {
                        seen = true
                        break
                    }
                }
                if !seen {
                    count++
                }
            }
        }
    }
    return count
}

func canSee(grid [][]int, x int, y int, guardX int, guardY int) bool {
    dx := x - guardX
    dy := y - guardY
    if dx == 0 {
        for i := min(y, guardY) + 1; i < max(y, guardY); i++ {
            if grid[x][i] == -1 {
                return false
            }
        }
    } else if dy == 0 {
        for i := min(x, guardX) + 1; i < max(x, guardX); i++ {
            if grid[i][y] == -1 {
                return false
            }
        }
    } else {
        return false
    }
    return true
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
def count_unguarded(m, n, guards, walls)
    grid = Array.new(m) { Array.new(n, 0) }
    walls.each do |wall|
        grid[wall[0]][wall[1]] = -1
    end
    count = 0
    (0...m).each do |i|
        (0...n).each do |j|
            if grid[i][j] == 0
                seen = false
                guards.each do |guard|
                    if can_see(grid, i, j, guard[0], guard[1])
                        seen = true
                        break
                    end
                end
                if !seen
                    count += 1
                end
            end
        end
    end
    count
end

def can_see(grid, x, y, guard_x, guard_y)
    dx = x - guard_x
    dy = y - guard_y
    if dx == 0
        (([y, guard_y].min + 1)...([y, guard_y].max)).each do |i|
            if grid[x][i] == -1
                return false
            end
        end
    elsif dy == 0
        (([x, guard_x].min + 1)...([x, guard_x].max)).each do |i|
            if grid[i][y] == -1
                return false
            end
        end
    else
        return false
    end
    true
end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countUnguarded(m: Int, n: Int, guards: Array[Array[Int]], walls: Array[Array[Int]]): Int = {
        val grid = Array.fill(m, n)(0)
        for (wall <- walls) {
            grid(wall(0))(wall(1)) = -1
        }
        var count = 0
        for (i <- 0 until m; j <- 0 until n) {
            if (grid(i)(j) == 0) {
                var seen = false
                for (guard <- guards) {
                    if (canSee(grid, i, j, guard(0), guard(1))) {
                        seen = true
                        break
                    }
                }
                if (!seen) {
                    count += 1
                }
            }
        }
        count
    }

    def canSee(grid: Array[Array[Int]], x: Int, y: Int, guardX: Int, guardY: Int): Boolean = {
        val dx = x - guardX
        val dy = y - guardY
        if (dx == 0) {
            for (i <- math.min(y, guardY) + 1 until math.max(y, guardY)) {
                if (grid(x)(i) == -1) {
                    return false
                }
            }
        } else if (dy == 0) {
            for (i <- math.min(x, guardX) + 1 until math.max(x, guardX)) {
                if (grid(i)(y) == -1) {
                    return false
                }
            }
        } else {
            return false
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
struct Solution;

impl Solution {
    pub fn count_unguarded(m: i32, n: i32, guards: Vec<Vec<i32>>, walls: Vec<Vec<i32>>) -> i32 {
        let mut grid = vec![vec![0; n as usize]; m as usize];
        for wall in walls {
            grid[wall[0] as usize][wall[1] as usize] = -1;
        }
        let mut count = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i as usize][j as usize] == 0 {
                    let mut seen = false;
                    for guard in &guards {
                        if Solution::can_see(&grid, i as usize, j as usize, guard[0] as usize, guard[1] as usize) {
                            seen = true;
                            break;
                        }
                    }
                    if !seen {
                        count += 1;
                    }
                }
            }
        }
        count
    }

    fn can_see(grid: &Vec<Vec<i32>>, x: usize, y: usize, guard_x: usize, guard_y: usize) -> bool {
        let dx = x as i32 - guard_x as i32;
        let dy = y as i32 - guard_y as i32;
        if dx == 0 {
            for i in std::cmp::min(y, guard_y) + 1..std::cmp::max(y, guard_y) {
                if grid[x][i] == -1 {
                    return false;
                }
            }
        } else if dy == 0 {
            for i in std::cmp::min(x, guard_x) + 1..std::cmp::max(x, guard_x) {
                if grid[i][y] == -1 {
                    return false;
                }
            }
        } else {
            return false;
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
#lang racket

(define (count-unguarded m n guards walls)
    (define grid (make-vector m (make-vector n 0)))
    (for-each (lambda (wall) (vector-set! (vector-ref grid (first wall)) (second wall) -1)) walls)
    (define count 0)
    (for* ((i (range m)) (j (range n)))
      (when (= (vector-ref (vector-ref grid i) j) 0)
        (define seen #f)
        (for-each (lambda (guard) (when (can-see grid i j (first guard) (second guard))
                                  (set! seen #t)
                                  (break)))
                  guards)
        (unless seen (set! count (+ count 1)))))
    count)

(define (can-see grid x y guard-x guard-y)
    (define dx (- x guard-x))
    (define dy (- y guard-y))
    (cond
      ((= dx 0)
       (for/and ((i (range (add1 (min y guard-y)) (min y guard-y))))
         (not (= (vector-ref (vector-ref grid x) i) -1))))
      ((= dy 0)
       (for/and ((i (range (add1 (min x guard-x)) (min x guard-x))))
         (not (= (vector-ref (vector-ref grid i) y) -1))))
      (else #f)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_unguarded/4]).

count_unguarded(M, N, Guards, Walls) ->
    Grid = array:new(M, {default, 0}),
    lists:foreach(fun(Wall) -> array:set(Wall, -1, Grid) end, Walls),
    Count = count_unguarded(Grid, Guards, 0, 0, M, N, 0),
    Count.

count_unguarded(Grid, Guards, I, J, M, N, Count) when I >= M ->
    Count;
count_unguarded(Grid, Guards, I, J, M, N, Count) when J >= N ->
    count_unguarded(Grid, Guards, I + 1, 0, M, N, Count);
count_unguarded(Grid, Guards, I, J, M, N, Count) ->
    Seen = lists:any(fun(Guard) -> can_see(Grid, I, J, Guard) end, Guards),
    case array:get([I, J], Grid) of
        0 when not Seen ->
            count_unguarded(Grid, Guards, I, J + 1, M, N, Count + 1);
        _ ->
            count_unguarded(Grid, Guards, I, J + 1, M, N, Count)
    end.

can_see(Grid, X, Y, [GuardX, GuardY]) ->
    DX = X - GuardX,
    DY = Y - GuardY,
    case {DX, DY} of
        {0, _} ->
            can_see_x(Grid, X, min(Y, GuardY) + 1, max(Y, GuardY));
        {_, 0} ->
            can_see_y(Grid, min(X, GuardX) + 1, max(X, GuardX), Y);
        _ ->
            false
    end.

can_see_x(Grid, X, I, MaxY) when I >= MaxY ->
    true;
can_see_x(Grid, X, I, MaxY) ->
    case array:get([X, I], Grid) of
        -1 ->
            false;
        _ ->
            can_see_x(Grid, X, I + 1, MaxY)
    end.

can_see_y(Grid, I, MaxX, Y) when I >= MaxX ->
    true;
can_see_y(Grid, I, MaxX, Y) ->
    case array:get([I, Y], Grid) of
        -1 ->
            false;
        _ ->
            can_see_y(Grid, I + 1, MaxX, Y)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def count_unguarded(m, n, guards, walls) do
      grid = for i <- 0..m-1, do: for j <- 0..n-1, do: 0
      Enum.each(walls, fn [x, y] -> grid = List.update_at(grid, x, fn row -> List.update_at(row, y, fn _ -> -1 end) end) end)
      count_unguarded(grid, guards, 0, 0, m, n, 0)
  end

  defp count_unguarded(grid, guards, i, j, m, n, count) when i >= m, do: count
  defp count_unguarded(grid, guards, i, j, m, n, count) when j >= n, do: count_unguarded(grid, guards, i + 1, 0, m, n, count)
  defp count_unguarded(grid, guards, i, j, m, n, count) do
      seen = Enum.any?(guards, fn [x, y] -> can_see(grid, i, j, x, y) end)
      case Enum.at(Enum.at(grid, i), j) do
          0 when not seen -> count_unguarded(grid, guards, i, j + 1, m, n, count + 1)
          _ -> count_unguarded(grid, guards, i, j + 1, m, n, count)
      end
  end

  defp can_see(grid, x, y, guard_x, guard_y) do
      dx = x - guard_x
      dy = y - guard_y
      cond do
          dx == 0 -> can_see_x(grid, x, min(y, guard_y) + 1, max(y, guard_y))
          dy == 0 -> can_see_y(grid, min(x, guard_x) + 1, max(x, guard_x), y)
          true -> false
      end
  end

  defp can_see_x(grid, x, i, max_y) when i >= max_y, do: true
  defp can_see_x(grid, x, i, max_y) do
      case Enum.at(Enum.at(grid, x), i) do
          -1 -> false
          _ -> can_see_x(grid, x, i + 1, max_y)
      end
  end

  defp can_see_y(grid, i, max_x, y) when i >= max_x, do: true
  defp can_see_y(grid, i, max_x, y) do
      case Enum.at(Enum.at(grid, i), y) do
          -1 -> false
          _ -> can_see_y(grid, i + 1, max_x, y)
      end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n + g * (m + n))

- **Space Complexity:** O(m * n)

</div>
</details>
