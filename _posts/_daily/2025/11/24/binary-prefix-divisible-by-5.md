---
layout: post
title: "Binary Prefix Divisible By 5"
date: 2025-11-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-prefix-divisible-by-5/
---

## Problem #1018: Binary Prefix Divisible By 5

**Difficulty:** Easy

**Topics:** Array, Bit Manipulation

## Problem Description

<p>You are given a binary array <code>nums</code> (<strong>0-indexed</strong>).</p>

<p>We define <code>x<sub>i</sub></code> as the number whose binary representation is the subarray <code>nums[0..i]</code> (from most-significant-bit to least-significant-bit).</p>

<ul>
	<li>For example, if <code>nums = [1,0,1]</code>, then <code>x<sub>0</sub> = 1</code>, <code>x<sub>1</sub> = 2</code>, and <code>x<sub>2</sub> = 5</code>.</li>
</ul>

<p>Return <em>an array of booleans </em><code>answer</code><em> where </em><code>answer[i]</code><em> is </em><code>true</code><em> if </em><code>x<sub>i</sub></code><em> is divisible by </em><code>5</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> [true,false,false]
<strong>Explanation:</strong> The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> [false,false,false]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. If X is the first i digits of the array as a binary number, then 2X + A[i] is the first i+1 digits.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 03:58:36 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to determine, for each prefix of a given binary array `nums`, if the decimal number represented by that prefix is divisible by 5. A direct approach of converting each prefix to its decimal value would quickly lead to integer overflow, as the length of `nums` can be up to 10^5, meaning the decimal values could be astronomically large (up to 2^(10^5)).

The key insight comes from the hint: if `X` is the decimal value of the binary prefix `nums[0...i-1]`, then the decimal value of the next prefix `nums[0...i]` is `2 * X + nums[i]`. Since we only care about divisibility by 5, we can use modulo arithmetic. Instead of tracking the full decimal value `X`, we only need to track `X % 5`. The property `(A * B + C) % M = ((A % M * B % M) % M + C % M) % M` allows us to compute the remainder iteratively.

So, we can maintain a `current_remainder` variable, initialized to 0. For each digit `nums[i]` in the input array, we update `current_remainder = (current_remainder * 2 + nums[i]) % 5`. After each update, if `current_remainder` is 0, it means the number represented by the prefix `nums[0...i]` is divisible by 5, and we append `true` to our result array; otherwise, we append `false`. This process is repeated for all elements in `nums`, building up the boolean result array.

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
    std::vector<bool> prefixesDivBy5(std::vector<int>& nums) {
        std::vector<bool> answer;
        int currentRemainder = 0;
        for (int num : nums) {
            currentRemainder = (currentRemainder * 2 + num) % 5;
            answer.push_back(currentRemainder == 0);
        }
        return answer;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> answer = new ArrayList<>();
        int currentRemainder = 0;
        for (int num : nums) {
            currentRemainder = (currentRemainder * 2 + num) % 5;
            answer.add(currentRemainder == 0);
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        answer = []
        current_remainder = 0
        for num in nums:
            current_remainder = (current_remainder * 2 + num) % 5
            answer.append(current_remainder == 0)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        answer = []
        current_remainder = 0
        for num in nums:
            current_remainder = (current_remainder * 2 + num) % 5
            answer.append(current_remainder == 0)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, and free'd by the caller.
 */
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    bool* answer = (bool*)malloc(sizeof(bool) * numsSize);
    *returnSize = numsSize;
    int currentRemainder = 0;
    for (int i = 0; i < numsSize; i++) {
        currentRemainder = (currentRemainder * 2 + nums[i]) % 5;
        answer[i] = (currentRemainder == 0);
    }
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public IList<bool> PrefixesDivBy5(int[] nums) {
        IList<bool> answer = new List<bool>();
        int currentRemainder = 0;
        foreach (int num in nums) {
            currentRemainder = (currentRemainder * 2 + num) % 5;
            answer.Add(currentRemainder == 0);
        }
        return answer;
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
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    const answer = [];
    let currentRemainder = 0;
    for (let i = 0; i < nums.length; i++) {
        currentRemainder = (currentRemainder * 2 + nums[i]) % 5;
        answer.push(currentRemainder === 0);
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function prefixesDivBy5(nums: number[]): boolean[] {
    const answer: boolean[] = [];
    let currentRemainder: number = 0;
    for (let i = 0; i < nums.length; i++) {
        currentRemainder = (currentRemainder * 2 + nums[i]) % 5;
        answer.push(currentRemainder === 0);
    }
    return answer;
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
     * @return Boolean[]
     */
    function prefixesDivBy5($nums) {
        $answer = [];
        $currentRemainder = 0;
        foreach ($nums as $num) {
            $currentRemainder = ($currentRemainder * 2 + $num) % 5;
            $answer[] = ($currentRemainder === 0);
        }
        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func prefixesDivBy5(_ nums: [Int]) -> [Bool] {
        var answer: [Bool] = []
        var currentRemainder: Int = 0
        for num in nums {
            currentRemainder = (currentRemainder * 2 + num) % 5
            answer.append(currentRemainder == 0)
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun prefixesDivBy5(nums: IntArray): List<Boolean> {
        val answer = mutableListOf<Boolean>()
        var currentRemainder = 0
        for (num in nums) {
            currentRemainder = (currentRemainder * 2 + num) % 5
            answer.add(currentRemainder == 0)
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<bool> prefixesDivBy5(List<int> nums) {
    List<bool> answer = [];
    int currentRemainder = 0;
    for (int num in nums) {
      currentRemainder = (currentRemainder * 2 + num) % 5;
      answer.add(currentRemainder == 0);
    }
    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func prefixesDivBy5(nums []int) []bool {
    answer := make([]bool, len(nums))
    currentRemainder := 0
    for i, num := range nums {
        currentRemainder = (currentRemainder * 2 + num) % 5
        answer[i] = (currentRemainder == 0)
    }
    return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    /**
     * @param {Integer[]} nums
     * @return {Boolean[]}
     */
    def prefixes_div_by5(nums)
        answer = []
        current_remainder = 0
        nums.each do |num|
            current_remainder = (current_remainder * 2 + num) % 5
            answer << (current_remainder == 0)
        end
        answer
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def prefixesDivBy5(nums: Array[Int]): List[Boolean] = {
        var answer = List.empty[Boolean]
        var currentRemainder = 0
        for (num <- nums) {
            currentRemainder = (currentRemainder * 2 + num) % 5
            answer = answer :+ (currentRemainder == 0)
        }
        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut answer: Vec<bool> = Vec::with_capacity(nums.len());
        let mut current_remainder: i32 = 0;
        for num in nums {
            current_remainder = (current_remainder * 2 + num) % 5;
            answer.push(current_remainder == 0);
        }
        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (prefixes-div-by5 nums)
  (-> (listof exact-integer?) (listof boolean?))
  (let loop ((nums-list nums)
             (current-remainder 0)
             (result '()))
    (if (empty? nums-list)
        (reverse result)
        (let* ((num (car nums-list))
               (new-remainder (modulo (+ (* current-remainder 2) num) 5)))
          (loop (cdr nums-list)
                new-remainder
                (cons (= new-remainder 0) result))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([prefixes_div_by5/1]).

prefixes_div_by5(Nums) ->
    lists:reverse(prefixes_div_by5_acc(Nums, 0, [])).

prefixes_div_by5_acc([], _CurrentRemainder, Acc) ->
    Acc;
prefixes_div_by5_acc([Num | Rest], CurrentRemainder, Acc) ->
    NewRemainder = (CurrentRemainder * 2 + Num) rem 5,
    prefixes_div_by5_acc(Rest, NewRemainder, [NewRemainder == 0 | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec prefixes_div_by5(nums :: [integer]) :: [boolean]
  def prefixes_div_by5(nums) do
    do_prefixes_div_by5(nums, 0, []) |> Enum.reverse()
  end

  defp do_prefixes_div_by5([], _current_remainder, acc) do
    acc
  end

  defp do_prefixes_div_by5([num | rest], current_remainder, acc) do
    new_remainder = rem(current_remainder * 2 + num, 5)
    do_prefixes_div_by5(rest, new_remainder, [new_remainder == 0 | acc])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with detailed explanation: The algorithm iterates through the input array `nums` exactly once. For each element, it performs a constant number of arithmetic operations (multiplication, addition, and modulo) and a constant number of array operations (appending to the result list). Therefore, the total time taken is directly proportional to the number of elements `N` in the `nums` array.

- **Space Complexity:** O(N) with detailed explanation: The algorithm creates a new list or array to store the boolean results, `answer`. This result array will have the same number of elements as the input array `nums`. Thus, the space required to store the output is proportional to `N`, the length of `nums`. No additional auxiliary space that scales with `N` is used beyond the output array itself.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-25 03:58:40 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires us to determine whether the binary representation of a subarray is divisible by 5. We can solve this problem by maintaining a running total of the binary representation of the subarray and checking its divisibility by 5 at each step. The key insight here is that if X is the first i digits of the array as a binary number, then 2X + A[i] is the first i+1 digits. This allows us to efficiently calculate the binary representation of the subarray at each step without having to recalculate it from scratch. We can then check whether this value is divisible by 5 and update our result accordingly.

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
class Solution {
public:
    std::vector<bool> prefixesDivBy5(std::vector<int>& nums) {
        std::vector<bool> result;
        int num = 0;
        for (int i = 0; i < nums.size(); i++) {
            num = (num << 1) + nums[i];
            result.push_back(num % 5 == 0);
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayList;
import java.util.List;
class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> result = new ArrayList<>();
        int num = 0;
        for (int i = 0; i < nums.length; i++) {
            num = (num << 1) + nums[i];
            result.add(num % 5 == 0);
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
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result = []
        num = 0
        for i in range(len(nums)):
            num = (num << 1) + nums[i]
            result.append(num % 5 == 0)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result = []
        num = 0
        for i in range(len(nums)):
            num = (num << 1) + nums[i]
            result.append(num % 5 == 0)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct {
    int* data;
    int size;
    int capacity;
} Vector;
void vector_init(Vector* vec) {
    vec->data = NULL;
    vec->size = 0;
    vec->capacity = 0;
}
void vector_add(Vector* vec, int value) {
    if (vec->size == vec->capacity) {
        vec->capacity = vec->capacity == 0 ? 1 : vec->capacity * 2;
        vec->data = realloc(vec->data, vec->capacity * sizeof(int));
    }
    vec->data[vec->size++] = value;
}
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    Vector vec;
    vector_init(&vec);
    int num = 0;
    for (int i = 0; i < numsSize; i++) {
        num = (num << 1) + nums[i];
        vector_add(&vec, num % 5 == 0);
    }
    *returnSize = vec.size;
    return vec.data;
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
    public bool[] PrefixesDivBy5(int[] nums) {
        bool[] result = new bool[nums.Length];
        int num = 0;
        for (int i = 0; i < nums.Length; i++) {
            num = (num << 1) + nums[i];
            result[i] = num % 5 == 0;
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
var prefixesDivBy5 = function(nums) {
    let result = [];
    let num = 0;
    for (let i = 0; i < nums.length; i++) {
        num = (num << 1) + nums[i];
        result.push(num % 5 == 0);
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function prefixesDivBy5(nums: number[]): boolean[] {
    let result: boolean[] = [];
    let num: number = 0;
    for (let i: number = 0; i < nums.length; i++) {
        num = (num << 1) + nums[i];
        result.push(num % 5 == 0);
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function prefixesDivBy5($nums) {
        $result = array();
        $num = 0;
        for ($i = 0; $i < count($nums); $i++) {
            $num = ($num << 1) + $nums[$i];
            array_push($result, $num % 5 == 0);
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
    func prefixesDivBy5(_ nums: [Int]) -> [Bool] {
        var result: [Bool] = []
        var num: Int = 0
        for i in 0..<nums.count {
            num = (num << 1) + nums[i]
            result.append(num % 5 == 0)
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
    fun prefixesDivBy5(nums: IntArray): BooleanArray {
        val result = BooleanArray(nums.size)
        var num = 0
        for (i in nums.indices) {
            num = (num shl 1) + nums[i]
            result[i] = num % 5 == 0
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
    List<bool> prefixesDivBy5(List<int> nums) {
        List<bool> result = [];
        int num = 0;
        for (int i = 0; i < nums.length; i++) {
            num = (num << 1) + nums[i];
            result.add(num % 5 == 0);
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
package main
import "fmt"
func prefixesDivBy5(nums []int) []bool {
    result := make([]bool, len(nums))
    num := 0
    for i := range nums {
        num = (num << 1) + nums[i]
        result[i] = num % 5 == 0
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def prefixes_div_by5(nums)
    result = []
    num = 0
    nums.each_with_index do |n, i|
        num = (num << 1) + n
        result << (num % 5 == 0)
    end
    result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def prefixesDivBy5(nums: Array[Int]): Array[Boolean] = {
        val result = new Array[Boolean](nums.length)
        var num = 0
        for (i <- nums.indices) {
            num = (num << 1) + nums(i)
            result(i) = num % 5 == 0
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut result = vec![false; nums.len()];
        let mut num = 0;
        for i in 0..nums.len() {
            num = (num << 1) + nums[i];
            result[i] = num % 5 == 0;
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define (prefixes-div-by5 nums)
  (let loop ((nums nums)
             (num 0)
             (result '()))
    (if (null? nums)
        (reverse result)
        (loop (cdr nums)
              (+ (* 2 num) (car nums))
              (cons (= (% (+ (* 2 num) (car nums)) 5) 0) result)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([prefixes_div_by5/1]).
prefixes_div_by5(Nums) ->
    prefixes_div_by5(Nums, 0, []).
prefixes_div_by5([], _, Result) ->
    lists:reverse(Result);
prefixes_div_by5([H|T], Num, Result) ->
    NewNum = (Num bsl 1) + H,
    prefixes_div_by5(T, NewNum, [(NewNum rem 5 == 0)|Result]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def prefixes_div_by5(nums) do
    prefixes_div_by5(nums, 0, [])
  end

  defp prefixes_div_by5([], _, result), do: Enum.reverse(result)
  defp prefixes_div_by5([h|t], num, result) do
    new_num = (num <<< 1) + h
    prefixes_div_by5(t, new_num, [(new_num |> rem(5) == 0)|result])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array, because we are scanning the array once and performing a constant amount of work at each step.

- **Space Complexity:** O(n) where n is the length of the input array, because we need to store the result for each subarray.

</div>
</details>
