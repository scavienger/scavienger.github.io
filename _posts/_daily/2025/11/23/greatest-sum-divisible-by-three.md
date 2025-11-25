---
layout: post
title: "Greatest Sum Divisible by Three"
date: 2025-11-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/greatest-sum-divisible-by-three/
---

## Problem #1262: Greatest Sum Divisible by Three

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Greedy, Sorting

## Problem Description

<p>Given an integer array <code>nums</code>, return <em>the <strong>maximum possible sum </strong>of elements of the array such that it is divisible by three</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,6,5,1,8]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since 4 is not divisible by 3, do not pick any number.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,4]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 03:30:00 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum possible sum of elements from an array `nums` such that the sum is divisible by three. This can be efficiently solved using dynamic programming. We maintain a small DP array, `dp`, of size 3, where `dp[i]` represents the maximum sum encountered so far that has a remainder of `i` when divided by 3.

We initialize `dp = [0, 0, 0]`. `dp[0]` is initialized to 0 because an empty sum (0) is divisible by 3. `dp[1]` and `dp[2]` are also initialized to 0. This works because all numbers in `nums` are positive (`nums[i] >= 1`). If we add any positive number to a sum of 0, the new sum will be positive. The `max` operation will ensure we always pick the largest valid sum. If no numbers can form a sum with remainder 1 or 2, `dp[1]` or `dp[2]` might remain 0, which is fine as they won't contribute to the final `dp[0]` unless combined with other numbers to form a sum divisible by 3.

We iterate through each `num` in the input array `nums`. For each `num`, we consider how adding it affects the current maximum sums stored in `dp`. It's crucial to use the `dp` values from the *previous* state (before considering the current `num`) to calculate the *new* `dp` values. To achieve this, we create a temporary copy of the `dp` array, say `temp_dp`, at the beginning of each iteration for `num`. Then, for each possible remainder `rem` (0, 1, 2), we calculate `current_sum = temp_dp[rem] + num`. The new remainder for this `current_sum` will be `new_rem = current_sum % 3`. We then update `dp[new_rem]` by taking the maximum of its current value and `current_sum`. After processing all `num`s, `dp[0]` will hold the maximum sum divisible by three.

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
    int maxSumDivThree(std::vector<int>& nums) {
        std::vector<int> dp(3, 0); // dp[i] stores the maximum sum with remainder i

        for (int num : nums) {
            std::vector<int> temp_dp = dp; // Create a temporary copy of dp for current iteration
            for (int rem = 0; rem < 3; ++rem) {
                // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                int current_sum = temp_dp[rem] + num;
                int new_rem = current_sum % 3;
                dp[new_rem] = std::max(dp[new_rem], current_sum);
            }
        }

        return dp[0];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxSumDivThree(int[] nums) {
        int[] dp = new int[3]; // dp[i] stores the maximum sum with remainder i

        for (int num : nums) {
            int[] temp_dp = new int[3];
            System.arraycopy(dp, 0, temp_dp, 0, 3); // Create a temporary copy of dp for current iteration

            for (int rem = 0; rem < 3; ++rem) {
                // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                int current_sum = temp_dp[rem] + num;
                int new_rem = current_sum % 3;
                dp[new_rem] = Math.max(dp[new_rem], current_sum);
            }
        }

        return dp[0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0] # dp[i] stores the maximum sum with remainder i

        for num in nums:
            temp_dp = dp[:] # Create a temporary copy of dp for current iteration
            for rem in range(3):
                # current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                current_sum = temp_dp[rem] + num
                new_rem = current_sum % 3
                dp[new_rem] = max(dp[new_rem], current_sum)

        return dp[0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0] # dp[i] stores the maximum sum with remainder i

        for num in nums:
            temp_dp = dp[:] # Create a temporary copy of dp for current iteration
            for rem in range(3):
                # current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                current_sum = temp_dp[rem] + num
                new_rem = current_sum % 3
                dp[new_rem] = max(dp[new_rem], current_sum)

        return dp[0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper for max function
int max(int a, int b) {
    return a > b ? a : b;
}

int maxSumDivThree(int* nums, int numsSize) {
    int dp[3] = {0, 0, 0}; // dp[i] stores the maximum sum with remainder i

    for (int i = 0; i < numsSize; ++i) {
        int num = nums[i];
        int temp_dp[3];
        memcpy(temp_dp, dp, sizeof(int) * 3); // Create a temporary copy of dp for current iteration

        for (int rem = 0; rem < 3; ++rem) {
            // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
            int current_sum = temp_dp[rem] + num;
            int new_rem = current_sum % 3;
            dp[new_rem] = max(dp[new_rem], current_sum);
        }
    }

    return dp[0];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxSumDivThree(int[] nums) {
        int[] dp = new int[3]; // dp[i] stores the maximum sum with remainder i

        foreach (int num in nums) {
            int[] temp_dp = new int[3];
            Array.Copy(dp, temp_dp, 3); // Create a temporary copy of dp for current iteration

            for (int rem = 0; rem < 3; ++rem) {
                // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                int current_sum = temp_dp[rem] + num;
                int new_rem = current_sum % 3;
                dp[new_rem] = Math.Max(dp[new_rem], current_sum);
            }
        }

        return dp[0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumDivThree = function(nums) {
    let dp = [0, 0, 0]; // dp[i] stores the maximum sum with remainder i

    for (let num of nums) {
        let temp_dp = [...dp]; // Create a temporary copy of dp for current iteration
        for (let rem = 0; rem < 3; ++rem) {
            // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
            let current_sum = temp_dp[rem] + num;
            let new_rem = current_sum % 3;
            dp[new_rem] = Math.max(dp[new_rem], current_sum);
        }
    }

    return dp[0];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSumDivThree(nums: number[]): number {
    let dp: number[] = [0, 0, 0]; // dp[i] stores the maximum sum with remainder i

    for (const num of nums) {
        const temp_dp: number[] = [...dp]; // Create a temporary copy of dp for current iteration
        for (let rem = 0; rem < 3; ++rem) {
            // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
            const current_sum: number = temp_dp[rem] + num;
            const new_rem: number = current_sum % 3;
            dp[new_rem] = Math.max(dp[new_rem], current_sum);
        }
    }

    return dp[0];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumDivThree($nums) {
        $dp = [0, 0, 0]; // dp[i] stores the maximum sum with remainder i

        foreach ($nums as $num) {
            $temp_dp = $dp; // Create a temporary copy of dp for current iteration
            for ($rem = 0; $rem < 3; ++$rem) {
                // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                $current_sum = $temp_dp[$rem] + $num;
                $new_rem = $current_sum % 3;
                $dp[$new_rem] = max($dp[$new_rem], $current_sum);
            }
        }

        return $dp[0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSumDivThree(_ nums: [Int]) -> Int {
        var dp = [0, 0, 0] // dp[i] stores the maximum sum with remainder i

        for num in nums {
            var temp_dp = dp // Create a temporary copy of dp for current iteration
            for rem in 0..<3 {
                // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                let current_sum = temp_dp[rem] + num
                let new_rem = current_sum % 3
                dp[new_rem] = max(dp[new_rem], current_sum)
            }
        }

        return dp[0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSumDivThree(nums: IntArray): Int {
        val dp = IntArray(3) { 0 } // dp[i] stores the maximum sum with remainder i

        for (num in nums) {
            val temp_dp = dp.copyOf() // Create a temporary copy of dp for current iteration
            for (rem in 0 until 3) {
                // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                val current_sum = temp_dp[rem] + num
                val new_rem = current_sum % 3
                dp[new_rem] = Math.max(dp[new_rem], current_sum)
            }
        }

        return dp[0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxSumDivThree(List<int> nums) {
    List<int> dp = [0, 0, 0]; // dp[i] stores the maximum sum with remainder i

    for (int num in nums) {
      List<int> temp_dp = List.from(dp); // Create a temporary copy of dp for current iteration
      for (int rem = 0; rem < 3; ++rem) {
        // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
        int current_sum = temp_dp[rem] + num;
        int new_rem = current_sum % 3;
        dp[new_rem] = Math.max(dp[new_rem], current_sum);
      }
    }

    return dp[0];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxSumDivThree(nums []int) int {
    dp := [3]int{0, 0, 0} // dp[i] stores the maximum sum with remainder i

    for _, num := range nums {
        temp_dp := [3]int{}
        copy(temp_dp[:], dp[:]) // Create a temporary copy of dp for current iteration

        for rem := 0; rem < 3; rem++ {
            // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
            current_sum := temp_dp[rem] + num
            new_rem := current_sum % 3
            if current_sum > dp[new_rem] {
                dp[new_rem] = current_sum
            }
        }
    }

    return dp[0]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer[]} nums
    # @return {Integer}
    def max_sum_div_three(nums)
        dp = [0, 0, 0] # dp[i] stores the maximum sum with remainder i

        nums.each do |num|
            temp_dp = dp.dup # Create a temporary copy of dp for current iteration
            (0..2).each do |rem|
                # current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                current_sum = temp_dp[rem] + num
                new_rem = current_sum % 3
                dp[new_rem] = [dp[new_rem], current_sum].max
            end
        end

        return dp[0]
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSumDivThree(nums: Array[Int]): Int = {
        var dp = Array(0, 0, 0) // dp(i) stores the maximum sum with remainder i

        for (num <- nums) {
            val temp_dp = dp.clone() // Create a temporary copy of dp for current iteration
            for (rem <- 0 until 3) {
                // current_sum will always be non-negative because nums(i) >= 1 and dp values are non-negative.
                val current_sum = temp_dp(rem) + num
                val new_rem = current_sum % 3
                dp(new_rem) = math.max(dp(new_rem), current_sum)
            }
        }

        dp(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        let mut dp = [0, 0, 0]; // dp[i] stores the maximum sum with remainder i

        for num in nums {
            let temp_dp = dp; // Create a temporary copy of dp for current iteration
            for rem in 0..3 {
                // current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
                let current_sum = temp_dp[rem] + num;
                let new_rem = current_sum % 3;
                dp[new_rem as usize] = dp[new_rem as usize].max(current_sum);
            }
        }

        dp[0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (max-sum-div-three nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((nums nums) (dp (vector 0 0 0)))
    (if (empty? nums)
        (vector-ref dp 0)
        (let* ((num (first nums))
               (temp-dp (vector-copy dp)))
          (for ([rem (in-range 3)])
            (let* ((current-sum (+ (vector-ref temp-dp rem) num))
                   (new-rem (modulo current-sum 3)))
              ;; current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
              (vector-set! dp new-rem (max (vector-ref dp new-rem) current-sum))))
          (loop (rest nums) dp)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_sum_div_three/1]).

max_sum_div_three(Nums) ->
    % dp[i] stores the maximum sum with remainder i
    % Initial state: {0, 0, 0} representing {dp0, dp1, dp2}
    {Dp0, _, _} = lists:foldl(fun(Num, {Dp0Acc, Dp1Acc, Dp2Acc}) ->
        % Calculate all possible new sums based on the *current* dp state
        % and the new 'Num'. These are candidates for the *next* dp state.
        Candidates = [
            {Dp0Acc + Num, (Dp0Acc + Num) rem 3},
            {Dp1Acc + Num, (Dp1Acc + Num) rem 3},
            {Dp2Acc + Num, (Dp2Acc + Num) rem 3}
        ],

        % Initialize the next dp state with the current dp state
        NextDp0 = Dp0Acc,
        NextDp1 = Dp1Acc,
        NextDp2 = Dp2Acc,

        % Iterate through candidates and update the next dp state
        lists:foldl(fun({Sum, Rem}, {Acc0, Acc1, Acc2}) ->
            % current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
            case Rem of
                0 -> {max(Acc0, Sum), Acc1, Acc2};
                1 -> {Acc0, max(Acc1, Sum), Acc2};
                2 -> {Acc0, Acc1, max(Acc2, Sum)}
            end
        end, {NextDp0, NextDp1, NextDp2}, Candidates)
    end, {0, 0, 0}, Nums),
    Dp0.

max(A, B) when A > B -> A;
max(A, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_sum_div_three(nums :: [integer]) :: integer
  def max_sum_div_three(nums) do
    # dp[i] stores the maximum sum with remainder i
    # Initial state: {0, 0, 0} representing {dp0, dp1, dp2}
    Enum.reduce(nums, {0, 0, 0}, fn num, {dp0, dp1, dp2} ->
      # Calculate all possible new sums based on the *current* dp state
      # and the new 'num'. These are candidates for the *next* dp state.
      candidates = [
        {dp0 + num, rem(dp0 + num, 3)},
        {dp1 + num, rem(dp1 + num, 3)},
        {dp2 + num, rem(dp2 + num, 3)}
      ]

      # Initialize the next dp state with the current dp state
      next_dp0 = dp0
      next_dp1 = dp1
      next_dp2 = dp2

      # Iterate through candidates and update the next dp state
      Enum.reduce(candidates, {next_dp0, next_dp1, next_dp2}, fn {s, r}, {acc0, acc1, acc2} ->
        # current_sum will always be non-negative because nums[i] >= 1 and dp values are non-negative.
        case r do
          0 -> {max(acc0, s), acc1, acc2}
          1 -> {acc0, max(acc1, s), acc2}
          2 -> {acc0, acc1, max(acc2, s)}
        end
      end)
    end)
    |> elem(0) # Return dp0
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with detailed explanation

- **Space Complexity:** O(1) with detailed explanation

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-25 03:30:10 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We can represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod. We initialize DP[0][0] to 0, and DP[0][1] and DP[0][2] to negative infinity. Then, for each position in the array, we update DP[pos][mod] to be the maximum of its current value and DP[pos-1][mod], DP[pos-1][(mod-nums[pos])%3] + nums[pos], and DP[pos-1][(mod-nums[pos]+3)%3] + nums[pos]. Finally, we return DP[n-1][0], where n is the length of the array. This approach ensures that we consider all possible sums and choose the maximum one that is divisible by 3. The time complexity of this approach is O(n), where n is the length of the array, because we make a constant amount of work for each position in the array. The space complexity is also O(n), because we need to store the DP table of size n x 3.

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
#include <climits>
using namespace std;
class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(3, INT_MIN));
        dp[0][0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                if (i > 0) {
                    dp[i][j] = max(dp[i][j], dp[i-1][j]);
                }
                int mod = (j - nums[i]) % 3;
                if (mod < 0) mod += 3;
                if (i > 0) {
                    dp[i][j] = max(dp[i][j], dp[i-1][mod] + nums[i]);
                }
            }
        }
        return dp[n-1][0];
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
    public int maxSumDivThree(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n][3];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], Integer.MIN_VALUE);
        }
        dp[0][0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                if (i > 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
                }
                int mod = (j - nums[i]) % 3;
                if (mod < 0) mod += 3;
                if (i > 0) {
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][mod] + nums[i]);
                }
            }
        }
        return dp[n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[float('-inf')] * 3 for _ in range(n)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(3):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                mod = (j - nums[i]) % 3
                if mod < 0:
                    mod += 3
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][mod] + nums[i])
        return dp[n-1][0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[float('-inf')] * 3 for _ in range(n)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(3):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                mod = (j - nums[i]) % 3
                if mod < 0:
                    mod += 3
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][mod] + nums[i])
        return dp[n-1][0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <limits.h>
int maxSumDivThree(int* nums, int numsSize) {
    int dp[numsSize][3];
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < 3; j++) {
            dp[i][j] = INT_MIN;
        }
    }
    dp[0][0] = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < 3; j++) {
            if (i > 0) {
                dp[i][j] = (dp[i][j] > dp[i-1][j]) ? dp[i][j] : dp[i-1][j];
            }
            int mod = (j - nums[i]) % 3;
            if (mod < 0) mod += 3;
            if (i > 0) {
                dp[i][j] = (dp[i][j] > dp[i-1][mod] + nums[i]) ? dp[i][j] : dp[i-1][mod] + nums[i];
            }
        }
    }
    return dp[numsSize-1][0];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
public class Solution {
    public int MaxSumDivThree(int[] nums) {
        int n = nums.Length;
        int[][] dp = new int[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new int[3];
            for (int j = 0; j < 3; j++) {
                dp[i][j] = int.MinValue;
            }
        }
        dp[0][0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                if (i > 0) {
                    dp[i][j] = Math.Max(dp[i][j], dp[i-1][j]);
                }
                int mod = (j - nums[i]) % 3;
                if (mod < 0) mod += 3;
                if (i > 0) {
                    dp[i][j] = Math.Max(dp[i][j], dp[i-1][mod] + nums[i]);
                }
            }
        }
        return dp[n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxSumDivThree = function(nums) {
    let n = nums.length;
    let dp = new Array(n);
    for (let i = 0; i < n; i++) {
        dp[i] = new Array(3).fill(-Infinity);
    }
    dp[0][0] = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < 3; j++) {
            if (i > 0) {
                dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
            }
            let mod = (j - nums[i]) % 3;
            if (mod < 0) mod += 3;
            if (i > 0) {
                dp[i][j] = Math.max(dp[i][j], dp[i-1][mod] + nums[i]);
            }
        }
    }
    return dp[n-1][0];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSumDivThree(nums: number[]): number {
    let n: number = nums.length;
    let dp: number[][] = new Array(n);
    for (let i: number = 0; i < n; i++) {
        dp[i] = new Array(3).fill(-Infinity);
    }
    dp[0][0] = 0;
    for (let i: number = 0; i < n; i++) {
        for (let j: number = 0; j < 3; j++) {
            if (i > 0) {
                dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);
            }
            let mod: number = (j - nums[i]) % 3;
            if (mod < 0) mod += 3;
            if (i > 0) {
                dp[i][j] = Math.max(dp[i][j], dp[i-1][mod] + nums[i]);
            }
        }
    }
    return dp[n-1][0];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxSumDivThree($nums) {
        $n = count($nums);
        $dp = array_fill(0, $n, array_fill(0, 3, -INF));
        $dp[0][0] = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < 3; $j++) {
                if ($i > 0) {
                    $dp[$i][$j] = max($dp[$i][$j], $dp[$i-1][$j]);
                }
                $mod = ($j - $nums[$i]) % 3;
                if ($mod < 0) $mod += 3;
                if ($i > 0) {
                    $dp[$i][$j] = max($dp[$i][$j], $dp[$i-1][$mod] + $nums[$i]);
                }
            }
        }
        return $dp[$n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSumDivThree(_ nums: [Int]) -> Int {
        let n = nums.count
        var dp = [[Int]](repeating: [Int](repeating: Int.min, count: 3), count: n)
        dp[0][0] = 0
        for i in 0..<n {
            for j in 0..<3 {
                if i > 0 {
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                }
                let mod = (j - nums[i]) % 3
                if mod < 0 {
                    let mod = mod + 3
                }
                if i > 0 {
                    dp[i][j] = max(dp[i][j], dp[i-1][mod] + nums[i])
                }
            }
        }
        return dp[n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSumDivThree(nums: IntArray): Int {
        val n = nums.size
        val dp = Array(n) { IntArray(3) { Int.MIN_VALUE } }
        dp[0][0] = 0
        for (i in 0 until n) {
            for (j in 0 until 3) {
                if (i > 0) {
                    dp[i][j] = maxOf(dp[i][j], dp[i-1][j])
                }
                val mod = (j - nums[i]) % 3
                if (mod < 0) {
                    val mod = mod + 3
                }
                if (i > 0) {
                    dp[i][j] = maxOf(dp[i][j], dp[i-1][mod] + nums[i])
                }
            }
        }
        return dp[n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxSumDivThree(List<int> nums) {
        int n = nums.length;
        List<List<int>> dp = List.generate(n, (i) => List.generate(3, (j) => -1000000));
        dp[0][0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                if (i > 0) {
                    dp[i][j] = max(dp[i][j], dp[i-1][j]);
                }
                int mod = (j - nums[i]) % 3;
                if (mod < 0) mod += 3;
                if (i > 0) {
                    dp[i][j] = max(dp[i][j], dp[i-1][mod] + nums[i]);
                }
            }
        }
        return dp[n-1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main
import "fmt"
func maxSumDivThree(nums []int) int {
    n := len(nums)
    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, 3)
        for j := range dp[i] {
            dp[i][j] = -1 << 31
        }
    }
    dp[0][0] = 0
    for i := 0; i < n; i++ {
        for j := 0; j < 3; j++ {
            if i > 0 {
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            }
            mod := (j - nums[i]) % 3
            if mod < 0 {
                mod += 3
            }
            if i > 0 {
                dp[i][j] = max(dp[i][j], dp[i-1][mod]+nums[i])
            }
        }
    }
    return dp[n-1][0]
}
func max(a, b int) int {
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
    def max_sum_div_three(nums)
        n = nums.size
        dp = Array.new(n) { Array.new(3, -1000000) }
        dp[0][0] = 0
        for i in 0...n
            for j in 0...3
                if i > 0
                    dp[i][j] = [dp[i][j], dp[i-1][j]].max
                end
                mod = (j - nums[i]) % 3
                if mod < 0
                    mod += 3
                end
                if i > 0
                    dp[i][j] = [dp[i][j], dp[i-1][mod] + nums[i]].max
                end
            end
        end
        dp[n-1][0]
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSumDivThree(nums: Array[Int]): Int = {
        val n = nums.length
        val dp = Array.fill(n)(Array.fill(3)(Int.MinValue))
        dp(0)(0) = 0
        for (i <- 0 until n) {
            for (j <- 0 until 3) {
                if (i > 0) {
                    dp(i)(j) = math.max(dp(i)(j), dp(i-1)(j))
                }
                val mod = (j - nums(i)) % 3
                if (mod < 0) {
                    val mod = mod + 3
                }
                if (i > 0) {
                    dp(i)(j) = math.max(dp(i)(j), dp(i-1)(mod) + nums(i))
                }
            }
        }
        dp(n-1)(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp: Vec<Vec<i32>> = vec![vec![-1000000; 3]; n];
        dp[0][0] = 0;
        for i in 0..n {
            for j in 0..3 {
                if i > 0 {
                    dp[i][j] = std::cmp::max(dp[i][j], dp[i-1][j]);
                }
                let mod = (j as i32 - nums[i]) % 3;
                if mod < 0 {
                    let mod = mod + 3;
                }
                if i > 0 {
                    dp[i][j] = std::cmp::max(dp[i][j], dp[i-1][mod as usize] + nums[i]);
                }
            }
        }
        dp[n-1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define (max-sum-div-three nums)
  (let* ((n (length nums))
         (dp (make-vector n (make-vector 3 -1000000))))
    (vector-set! (vector-ref dp 0) 0 0)
    (for ((i (range n)))
      (for ((j (range 3)))
        (when (> i 0)
          (vector-set! (vector-ref dp i) j (max (vector-ref (vector-ref dp i) j) (vector-ref (vector-ref dp (- i 1)) j))))
        (let ((mod (- j (vector-ref nums i))))
          (when (< mod 0)
            (set! mod (+ mod 3)))
          (when (> i 0)
            (vector-set! (vector-ref dp i) j (max (vector-ref (vector-ref dp i) j) (+ (vector-ref (vector-ref dp (- i 1)) mod) (vector-ref nums i))))))))
    (vector-ref (vector-ref dp (- n 1)) 0))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solutions).
-export([maxSumDivThree/1]).
maxSumDivThree(Nums) ->
    Length = length(Nums),
    DP = array:new(Length, {default, -1000000}),
    array:set(0, 0, DP),
    maxSumDivThree(Nums, DP, 0, Length).
maxSumDivThree([_|T], DP, I, Length) when I >= Length ->
    array:get(Length - 1, 0, DP);
maxSumDivThree([H|T], DP, I, Length) ->
    NewDP = lists:foldl(
        fun(J, Acc) ->
            case I of
                0 ->
                    array:set(I, J, max(array:get(I, J, Acc), 0), Acc);
                _ ->
                    array:set(I, J, max(array:get(I, J, Acc), array:get(I - 1, J, Acc)), Acc)
            end
        end,
        DP,
        lists:seq(0, 2)
    ),
    Mod = fun(J) -> (J - H) rem 3 end,
    NewDP2 = lists:foldl(
        fun(J, Acc) ->
            case I of
                0 ->
                    Acc;
                _ ->
                    M = Mod(J),
                    case M < 0 of
                        true -> M1 = M + 3;
                        false -> M1 = M
                    end,
                    array:set(I, J, max(array:get(I, J, Acc), array:get(I - 1, M1, Acc) + H), Acc)
            end
        end,
        NewDP,
        lists:seq(0, 2)
    ),
    maxSumDivThree(T, NewDP2, I + 1, Length).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def max_sum_div_three(nums) do
    n = length(nums)
    dp = for i <- 0..n-1, do: for j <- 0..2, do: -1000000
    dp = List.update_at(dp, 0, fn x -> List.update_at(x, 0, fn _ -> 0 end) end)
    max_sum_div_three(nums, dp, 0, n)
  end

  defp max_sum_div_three([], dp, _, _), do: Enum.at(Enum.at(dp, -1), 0)

  defp max_sum_div_three([h|t], dp, i, n) do
    dp = Enum.with_index(dp)
    |> Enum.map(fn {row, row_index} ->
      Enum.with_index(row)
      |> Enum.map(fn {val, col_index} ->
        cond do
          row_index == 0 -> val
          true ->
            max(val, Enum.at(Enum.at(dp, row_index - 1), col_index))
        end
      end)
    end)
    dp = Enum.with_index(dp)
    |> Enum.map(fn {row, row_index} ->
      Enum.with_index(row)
      |> Enum.map(fn {val, col_index} ->
        cond do
          row_index == 0 -> val
          true ->
            mod = (col_index - h) |> rem(3)
            cond do
              mod < 0 -> mod = mod + 3
              true -> mod
            end
            max(val, Enum.at(Enum.at(dp, row_index - 1), mod) + h)
        end
      end)
    end)
    max_sum_div_three(t, dp, i + 1, n)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the array, because we make a constant amount of work for each position in the array.

- **Space Complexity:** O(n) because we need to store the DP table of size n x 3.

</div>
</details>
