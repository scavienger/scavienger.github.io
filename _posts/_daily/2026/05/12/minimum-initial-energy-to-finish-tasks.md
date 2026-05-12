---
layout: post
title: "Minimum Initial Energy to Finish Tasks"
date: 2026-05-12 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    int minimumEffort(vector<vector<int>>& tasks) {\n\
        \        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>&\
        \ b) {\n            return (a[1] - a[0]) > (b[1] - b[0]);\n        });\n\n \
        \       int totalRequired = 0;\n        int currentEnergy = 0;\n\n        for\
        \ (const auto& task : tasks) {\n            int actual = task[0];\n        \
        \    int minimum = task[1];\n\n            if (currentEnergy < minimum) {\n\
        \                totalRequired += (minimum - currentEnergy);\n             \
        \   currentEnergy = minimum;\n            }\n            currentEnergy -= actual;\n\
        \        }\n\n        return totalRequired;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minimumEffort(int[][]\
        \ tasks) {\n        Arrays.sort(tasks, (a, b) -> (b[1] - b[0]) - (a[1] - a[0]));\n\
        \n        int totalRequired = 0;\n        int currentEnergy = 0;\n\n       \
        \ for (int[] task : tasks) {\n            int actual = task[0];\n          \
        \  int minimum = task[1];\n\n            if (currentEnergy < minimum) {\n  \
        \              totalRequired += (minimum - currentEnergy);\n               \
        \ currentEnergy = minimum;\n            }\n            currentEnergy -= actual;\n\
        \        }\n\n        return totalRequired;\n    }\n}"
      python: "class Solution(object):\n    def minimumEffort(self, tasks):\n      \
        \  \"\"\"\n        :type tasks: List[List[int]]\n        :rtype: int\n     \
        \   \"\"\"\n        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)\n\n\
        \        total_required = 0\n        current_energy = 0\n\n        for actual,\
        \ minimum in tasks:\n            if current_energy < minimum:\n            \
        \    diff = minimum - current_energy\n                total_required += diff\n\
        \                current_energy = minimum\n            current_energy -= actual\n\
        \n        return total_required"
      python3: "class Solution:\n    def minimumEffort(self, tasks: List[List[int]])\
        \ -> int:\n        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)\n   \
        \     ans = 0\n        current_sum = 0\n        for actual, minimum in tasks:\n\
        \            if current_sum + minimum > ans:\n                ans = current_sum\
        \ + minimum\n            current_sum += actual\n        return ans"
      c: "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int*\
        \ taskA = *(int**)a;\n    int* taskB = *(int**)b;\n    int diffA = taskA[1]\
        \ - taskA[0];\n    int diffB = taskB[1] - taskB[0];\n    if (diffA < diffB)\
        \ return 1;\n    if (diffA > diffB) return -1;\n    return 0;\n}\n\nint minimumEffort(int**\
        \ tasks, int tasksSize, int* tasksColSize) {\n    qsort(tasks, tasksSize, sizeof(int*),\
        \ compare);\n    int ans = 0;\n    int currentSum = 0;\n    for (int i = 0;\
        \ i < tasksSize; i++) {\n        if (currentSum + tasks[i][1] > ans) {\n   \
        \         ans = currentSum + tasks[i][1];\n        }\n        currentSum +=\
        \ tasks[i][0];\n    }\n    return ans;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MinimumEffort(int[][]\
        \ tasks) {\n        Array.Sort(tasks, (a, b) => (b[1] - b[0]).CompareTo(a[1]\
        \ - a[0]));\n        int ans = 0;\n        int currentSum = 0;\n        foreach\
        \ (int[] task in tasks) {\n            if (currentSum + task[1] > ans) {\n \
        \               ans = currentSum + task[1];\n            }\n            currentSum\
        \ += task[0];\n        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[][]} tasks\n * @return {number}\n */\nvar\
        \ minimumEffort = function(tasks) {\n    tasks.sort((a, b) => (b[1] - b[0])\
        \ - (a[1] - a[0]));\n    let ans = 0;\n    let currentSum = 0;\n    for (let\
        \ i = 0; i < tasks.length; i++) {\n        if (currentSum + tasks[i][1] > ans)\
        \ {\n            ans = currentSum + tasks[i][1];\n        }\n        currentSum\
        \ += tasks[i][0];\n    }\n    return ans;\n};"
      typescript: "function minimumEffort(tasks: number[][]): number {\n    tasks.sort((a,\
        \ b) => (b[1] - b[0]) - (a[1] - a[0]));\n\n    let ans = 0;\n    let current\
        \ = 0;\n\n    for (const task of tasks) {\n        const actual = task[0];\n\
        \        const minimum = task[1];\n\n        if (current < minimum) {\n    \
        \        const diff = minimum - current;\n            ans += diff;\n       \
        \     current = minimum;\n        }\n        current -= actual;\n    }\n\n \
        \   return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $tasks\n     * @return\
        \ Integer\n     */\n    function minimumEffort($tasks) {\n        usort($tasks,\
        \ function($a, $b) {\n            return ($b[1] - $b[0]) <=> ($a[1] - $a[0]);\n\
        \        });\n\n        $ans = 0;\n        $current = 0;\n\n        foreach\
        \ ($tasks as $task) {\n            $actual = $task[0];\n            $minimum\
        \ = $task[1];\n\n            if ($current < $minimum) {\n                $diff\
        \ = $minimum - $current;\n                $ans += $diff;\n                $current\
        \ = $minimum;\n            }\n            $current -= $actual;\n        }\n\n\
        \        return $ans;\n    }\n}"
      swift: "class Solution {\n    func minimumEffort(_ tasks: [[Int]]) -> Int {\n\
        \        let sortedTasks = tasks.sorted { ($0[1] - $0[0]) > ($1[1] - $1[0])\
        \ }\n\n        var ans = 0\n        var current = 0\n\n        for task in sortedTasks\
        \ {\n            let actual = task[0]\n            let minimum = task[1]\n\n\
        \            if current < minimum {\n                let diff = minimum - current\n\
        \                ans += diff\n                current = minimum\n          \
        \  }\n            current -= actual\n        }\n\n        return ans\n    }\n\
        }"
      kotlin: "class Solution {\n    fun minimumEffort(tasks: Array<IntArray>): Int\
        \ {\n        tasks.sortWith(Comparator { a, b ->\n            val diffA = a[1]\
        \ - a[0]\n            val diffB = b[1] - b[0]\n            diffB.compareTo(diffA)\n\
        \        })\n\n        var ans = 0\n        var current = 0\n\n        for (task\
        \ in tasks) {\n            val actual = task[0]\n            val minimum = task[1]\n\
        \n            if (current < minimum) {\n                val diff = minimum -\
        \ current\n                ans += diff\n                current = minimum\n\
        \            }\n            current -= actual\n        }\n\n        return ans\n\
        \    }\n}"
      dart: "class Solution {\n  int minimumEffort(List<List<int>> tasks) {\n    tasks.sort((a,\
        \ b) => (b[1] - b[0]).compareTo(a[1] - a[0]));\n    int ans = 0;\n    int currentSumA\
        \ = 0;\n    for (var task in tasks) {\n      int actual = task[0];\n      int\
        \ minimum = task[1];\n      if (currentSumA + minimum > ans) {\n        ans\
        \ = currentSumA + minimum;\n      }\n      currentSumA += actual;\n    }\n \
        \   return ans;\n  }\n}"
      go: "import \"sort\"\n\nfunc minimumEffort(tasks [][]int) int {\n    sort.Slice(tasks,\
        \ func(i, j int) bool {\n        return (tasks[i][1] - tasks[i][0]) > (tasks[j][1]\
        \ - tasks[j][0])\n    })\n    ans := 0\n    currentSumA := 0\n    for _, task\
        \ := range tasks {\n        actual := task[0]\n        minimum := task[1]\n\
        \        if currentSumA + minimum > ans {\n            ans = currentSumA + minimum\n\
        \        }\n        currentSumA += actual\n    }\n    return ans\n}"
      ruby: "def minimum_effort(tasks)\n  tasks.sort! { |a, b| (b[1] - b[0]) <=> (a[1]\
        \ - a[0]) }\n  ans = 0\n  current_sum_a = 0\n  tasks.each do |task|\n    actual\
        \ = task[0]\n    minimum = task[1]\n    if current_sum_a + minimum > ans\n \
        \     ans = current_sum_a + minimum\n    end\n    current_sum_a += actual\n\
        \  end\n  ans\nend"
      scala: "object Solution {\n    def minimumEffort(tasks: Array[Array[Int]]): Int\
        \ = {\n        val sortedTasks = tasks.sortWith((t1, t2) => (t1(1) - t1(0))\
        \ > (t2(1) - t2(0)))\n        var ans = 0\n        var currentSumA = 0\n   \
        \     for (task <- sortedTasks) {\n            val actual = task(0)\n      \
        \      val minimum = task(1)\n            if (currentSumA + minimum > ans) {\n\
        \                ans = currentSumA + minimum\n            }\n            currentSumA\
        \ += actual\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_effort(mut tasks: Vec<Vec<i32>>) ->\
        \ i32 {\n        tasks.sort_unstable_by(|a, b| {\n            let diff_a = a[1]\
        \ - a[0];\n            let diff_b = b[1] - b[0];\n            diff_b.cmp(&diff_a)\n\
        \        });\n\n        let mut max_e = 0;\n        let mut sum_a = 0;\n   \
        \     for task in tasks {\n            let actual = task[0];\n            let\
        \ minimum = task[1];\n            if minimum + sum_a > max_e {\n           \
        \     max_e = minimum + sum_a;\n            }\n            sum_a += actual;\n\
        \        }\n        max_e\n    }\n}"
      racket: "(define/contract (minimum-effort tasks)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([sorted-tasks (sort tasks (lambda (a b)\n      \
        \                              (> (- (second a) (first a)) \n              \
        \                         (- (second b) (first b)))))]\n         [res-sum (foldl\
        \ (lambda (task acc)\n                           (let* ([actual (first task)]\n\
        \                                  [minimum (second task)]\n               \
        \                   [current-max-e (first acc)]\n                          \
        \        [current-sum-a (second acc)])\n                             (list (max\
        \ current-max-e (+ minimum current-sum-a))\n                               \
        \    (+ current-sum-a actual))))\n                         (list 0 0)\n    \
        \                     sorted-tasks)])\n    (first res-sum)))"
      erlang: "-spec minimum_effort(Tasks :: [[integer()]]) -> integer().\nminimum_effort(Tasks)\
        \ ->\n    SortedTasks = lists:sort(fun([A1, M1], [A2, M2]) ->\n            \
        \                     (M1 - A1) >= (M2 - A2)\n                             end,\
        \ Tasks),\n    {Res, _} = lists:foldl(fun([A, M], {MaxE, SumA}) ->\n       \
        \                        {max(MaxE, M + SumA), SumA + A}\n                 \
        \          end, {0, 0}, SortedTasks),\n    Res."
      elixir: "defmodule Solution do\n  @spec minimum_effort(tasks :: [[integer]]) ::\
        \ integer\n  def minimum_effort(tasks) do\n    {res, _} = tasks\n    |> Enum.sort_by(fn\
        \ [a, m] -> m - a end, :desc)\n    |> Enum.reduce({0, 0}, fn [a, m], {max_e,\
        \ sum_a} ->\n      {max(max_e, m + sum_a), sum_a + a}\n    end)\n    res\n \
        \ end\nend"
    approach: 'The problem is solved using a greedy strategy by sorting the tasks based
      on the difference between the minimum energy required to start a task and the
      actual energy spent on it ($minimum_i - actual_i$) in descending order. This intuition
      is based on the idea of preserving the largest ''buffer'' possible. Tasks with
      a larger difference between start-up cost and actual consumption provide a higher
      residual energy level relative to their requirement, which can then be used to
      satisfy the starting requirements of subsequent tasks with smaller buffers. Mathematically,
      sorting by this difference minimizes the peak initial energy required at any point
      in the sequence.


      After sorting the tasks, we simulate the process to find the minimum initial energy.
      We initialize both the total starting energy required and the current energy level
      to zero. We iterate through the sorted tasks, and for each task, we check if the
      current energy level is at least the task''s minimum starting requirement. If
      it is not, we increase the total starting energy (and the current energy pool)
      by the deficit. After completing each task, we subtract the actual energy cost
      from our current pool. The accumulated starting energy after processing all tasks
      is the minimum value required.'
    time_complexity: O(N log N) where N is the number of tasks. This complexity is dominated
      by the sorting step. The subsequent linear pass to simulate energy expenditure
      takes O(N) time.
    space_complexity: O(N) for Python and Java, as their sorting implementations (TimSort)
      generally require O(N) additional space, while C++ typically uses O(log N) space
      for the sorting recursion stack.
    elapsed_time: 307.1522045135498
    model: gemini-3-flash-preview
    generated_at: '2026-05-12 02:20:15 '
---

## Problem #1665: Minimum Initial Energy to Finish Tasks

**Difficulty:** Hard

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given an array <code>tasks</code> where <code>tasks[i] = [actual<sub>i</sub>, minimum<sub>i</sub>]</code>:</p>

<ul>
	<li><code>actual<sub>i</sub></code> is the actual amount of energy you <strong>spend to finish</strong> the <code>i<sup>th</sup></code> task.</li>
	<li><code>minimum<sub>i</sub></code> is the minimum amount of energy you <strong>require to begin</strong> the <code>i<sup>th</sup></code> task.</li>
</ul>

<p>For example, if the task is <code>[10, 12]</code> and your current energy is <code>11</code>, you cannot start this task. However, if your current energy is <code>13</code>, you can complete this task, and your energy will be <code>3</code> after finishing it.</p>

<p>You can finish the tasks in <strong>any order</strong> you like.</p>

<p>Return <em>the <strong>minimum</strong> initial amount of energy you will need</em> <em>to finish all the tasks</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> tasks = [[1,2],[2,4],[4,8]]
<strong>Output:</strong> 8
<strong>Explanation:</strong>
Starting with 8 energy, we finish the tasks in the following order:
    - 3rd task. Now energy = 8 - 4 = 4.
    - 2nd task. Now energy = 4 - 2 = 2.
    - 1st task. Now energy = 2 - 1 = 1.
Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
<strong>Output:</strong> 32
<strong>Explanation:</strong>
Starting with 32 energy, we finish the tasks in the following order:
    - 1st task. Now energy = 32 - 1 = 31.
    - 2nd task. Now energy = 31 - 2 = 29.
    - 3rd task. Now energy = 29 - 10 = 19.
    - 4th task. Now energy = 19 - 10 = 9.
    - 5th task. Now energy = 9 - 8 = 1.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
<strong>Output:</strong> 27
<strong>Explanation:</strong>
Starting with 27 energy, we finish the tasks in the following order:
    - 5th task. Now energy = 27 - 5 = 22.
    - 2nd task. Now energy = 22 - 2 = 20.
    - 3rd task. Now energy = 20 - 3 = 17.
    - 1st task. Now energy = 17 - 1 = 16.
    - 4th task. Now energy = 16 - 4 = 12.
    - 6th task. Now energy = 12 - 6 = 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= actual<sub>​i</sub>&nbsp;&lt;= minimum<sub>i</sub>&nbsp;&lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. We can easily figure that the f(x) : does x solve this array is monotonic so binary Search is doable

2. Figure a sorting pattern

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using a greedy strategy by sorting the tasks based on the difference between the minimum energy required to start a task and the actual energy spent on it ($minimum_i - actual_i$) in descending order. This intuition is based on the idea of preserving the largest 'buffer' possible. Tasks with a larger difference between start-up cost and actual consumption provide a higher residual energy level relative to their requirement, which can then be used to satisfy the starting requirements of subsequent tasks with smaller buffers. Mathematically, sorting by this difference minimizes the peak initial energy required at any point in the sequence.

After sorting the tasks, we simulate the process to find the minimum initial energy. We initialize both the total starting energy required and the current energy level to zero. We iterate through the sorted tasks, and for each task, we check if the current energy level is at least the task's minimum starting requirement. If it is not, we increase the total starting energy (and the current energy pool) by the deficit. After completing each task, we subtract the actual energy cost from our current pool. The accumulated starting energy after processing all tasks is the minimum value required.

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
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b) {
            return (a[1] - a[0]) > (b[1] - b[0]);
        });

        int totalRequired = 0;
        int currentEnergy = 0;

        for (const auto& task : tasks) {
            int actual = task[0];
            int minimum = task[1];

            if (currentEnergy < minimum) {
                totalRequired += (minimum - currentEnergy);
                currentEnergy = minimum;
            }
            currentEnergy -= actual;
        }

        return totalRequired;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int minimumEffort(int[][] tasks) {
        Arrays.sort(tasks, (a, b) -> (b[1] - b[0]) - (a[1] - a[0]));

        int totalRequired = 0;
        int currentEnergy = 0;

        for (int[] task : tasks) {
            int actual = task[0];
            int minimum = task[1];

            if (currentEnergy < minimum) {
                totalRequired += (minimum - currentEnergy);
                currentEnergy = minimum;
            }
            currentEnergy -= actual;
        }

        return totalRequired;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        total_required = 0
        current_energy = 0

        for actual, minimum in tasks:
            if current_energy < minimum:
                diff = minimum - current_energy
                total_required += diff
                current_energy = minimum
            current_energy -= actual

        return total_required
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        ans = 0
        current_sum = 0
        for actual, minimum in tasks:
            if current_sum + minimum > ans:
                ans = current_sum + minimum
            current_sum += actual
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compare(const void* a, const void* b) {
    int* taskA = *(int**)a;
    int* taskB = *(int**)b;
    int diffA = taskA[1] - taskA[0];
    int diffB = taskB[1] - taskB[0];
    if (diffA < diffB) return 1;
    if (diffA > diffB) return -1;
    return 0;
}

int minimumEffort(int** tasks, int tasksSize, int* tasksColSize) {
    qsort(tasks, tasksSize, sizeof(int*), compare);
    int ans = 0;
    int currentSum = 0;
    for (int i = 0; i < tasksSize; i++) {
        if (currentSum + tasks[i][1] > ans) {
            ans = currentSum + tasks[i][1];
        }
        currentSum += tasks[i][0];
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinimumEffort(int[][] tasks) {
        Array.Sort(tasks, (a, b) => (b[1] - b[0]).CompareTo(a[1] - a[0]));
        int ans = 0;
        int currentSum = 0;
        foreach (int[] task in tasks) {
            if (currentSum + task[1] > ans) {
                ans = currentSum + task[1];
            }
            currentSum += task[0];
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} tasks
 * @return {number}
 */
var minimumEffort = function(tasks) {
    tasks.sort((a, b) => (b[1] - b[0]) - (a[1] - a[0]));
    let ans = 0;
    let currentSum = 0;
    for (let i = 0; i < tasks.length; i++) {
        if (currentSum + tasks[i][1] > ans) {
            ans = currentSum + tasks[i][1];
        }
        currentSum += tasks[i][0];
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumEffort(tasks: number[][]): number {
    tasks.sort((a, b) => (b[1] - b[0]) - (a[1] - a[0]));

    let ans = 0;
    let current = 0;

    for (const task of tasks) {
        const actual = task[0];
        const minimum = task[1];

        if (current < minimum) {
            const diff = minimum - current;
            ans += diff;
            current = minimum;
        }
        current -= actual;
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $tasks
     * @return Integer
     */
    function minimumEffort($tasks) {
        usort($tasks, function($a, $b) {
            return ($b[1] - $b[0]) <=> ($a[1] - $a[0]);
        });

        $ans = 0;
        $current = 0;

        foreach ($tasks as $task) {
            $actual = $task[0];
            $minimum = $task[1];

            if ($current < $minimum) {
                $diff = $minimum - $current;
                $ans += $diff;
                $current = $minimum;
            }
            $current -= $actual;
        }

        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumEffort(_ tasks: [[Int]]) -> Int {
        let sortedTasks = tasks.sorted { ($0[1] - $0[0]) > ($1[1] - $1[0]) }

        var ans = 0
        var current = 0

        for task in sortedTasks {
            let actual = task[0]
            let minimum = task[1]

            if current < minimum {
                let diff = minimum - current
                ans += diff
                current = minimum
            }
            current -= actual
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumEffort(tasks: Array<IntArray>): Int {
        tasks.sortWith(Comparator { a, b ->
            val diffA = a[1] - a[0]
            val diffB = b[1] - b[0]
            diffB.compareTo(diffA)
        })

        var ans = 0
        var current = 0

        for (task in tasks) {
            val actual = task[0]
            val minimum = task[1]

            if (current < minimum) {
                val diff = minimum - current
                ans += diff
                current = minimum
            }
            current -= actual
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumEffort(List<List<int>> tasks) {
    tasks.sort((a, b) => (b[1] - b[0]).compareTo(a[1] - a[0]));
    int ans = 0;
    int currentSumA = 0;
    for (var task in tasks) {
      int actual = task[0];
      int minimum = task[1];
      if (currentSumA + minimum > ans) {
        ans = currentSumA + minimum;
      }
      currentSumA += actual;
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minimumEffort(tasks [][]int) int {
    sort.Slice(tasks, func(i, j int) bool {
        return (tasks[i][1] - tasks[i][0]) > (tasks[j][1] - tasks[j][0])
    })
    ans := 0
    currentSumA := 0
    for _, task := range tasks {
        actual := task[0]
        minimum := task[1]
        if currentSumA + minimum > ans {
            ans = currentSumA + minimum
        }
        currentSumA += actual
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_effort(tasks)
  tasks.sort! { |a, b| (b[1] - b[0]) <=> (a[1] - a[0]) }
  ans = 0
  current_sum_a = 0
  tasks.each do |task|
    actual = task[0]
    minimum = task[1]
    if current_sum_a + minimum > ans
      ans = current_sum_a + minimum
    end
    current_sum_a += actual
  end
  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumEffort(tasks: Array[Array[Int]]): Int = {
        val sortedTasks = tasks.sortWith((t1, t2) => (t1(1) - t1(0)) > (t2(1) - t2(0)))
        var ans = 0
        var currentSumA = 0
        for (task <- sortedTasks) {
            val actual = task(0)
            val minimum = task(1)
            if (currentSumA + minimum > ans) {
                ans = currentSumA + minimum
            }
            currentSumA += actual
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_effort(mut tasks: Vec<Vec<i32>>) -> i32 {
        tasks.sort_unstable_by(|a, b| {
            let diff_a = a[1] - a[0];
            let diff_b = b[1] - b[0];
            diff_b.cmp(&diff_a)
        });

        let mut max_e = 0;
        let mut sum_a = 0;
        for task in tasks {
            let actual = task[0];
            let minimum = task[1];
            if minimum + sum_a > max_e {
                max_e = minimum + sum_a;
            }
            sum_a += actual;
        }
        max_e
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-effort tasks)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted-tasks (sort tasks (lambda (a b)
                                    (> (- (second a) (first a)) 
                                       (- (second b) (first b)))))]
         [res-sum (foldl (lambda (task acc)
                           (let* ([actual (first task)]
                                  [minimum (second task)]
                                  [current-max-e (first acc)]
                                  [current-sum-a (second acc)])
                             (list (max current-max-e (+ minimum current-sum-a))
                                   (+ current-sum-a actual))))
                         (list 0 0)
                         sorted-tasks)])
    (first res-sum)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_effort(Tasks :: [[integer()]]) -> integer().
minimum_effort(Tasks) ->
    SortedTasks = lists:sort(fun([A1, M1], [A2, M2]) ->
                                 (M1 - A1) >= (M2 - A2)
                             end, Tasks),
    {Res, _} = lists:foldl(fun([A, M], {MaxE, SumA}) ->
                               {max(MaxE, M + SumA), SumA + A}
                           end, {0, 0}, SortedTasks),
    Res.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_effort(tasks :: [[integer]]) :: integer
  def minimum_effort(tasks) do
    {res, _} = tasks
    |> Enum.sort_by(fn [a, m] -> m - a end, :desc)
    |> Enum.reduce({0, 0}, fn [a, m], {max_e, sum_a} ->
      {max(max_e, m + sum_a), sum_a + a}
    end)
    res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) where N is the number of tasks. This complexity is dominated by the sorting step. The subsequent linear pass to simulate energy expenditure takes O(N) time.
- **Space Complexity:** O(N) for Python and Java, as their sorting implementations (TimSort) generally require O(N) additional space, while C++ typically uses O(log N) space for the sorting recursion stack.
