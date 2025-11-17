---
layout: post
title: "Check If All 1's Are at Least Length K Places Away"
date: 2025-11-17 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
---

## Problem #1437: Check If All 1's Are at Least Length K Places Away

**Difficulty:** Easy

**Topics:** Array

## Problem Description

Given an binary array `nums` and an integer `k`, return `true` _if all_`1` _'s are at least_`k` _places away from each other, otherwise return_`false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)

``` Input: nums = [1,0,0,0,1,0,0,1], k = 2 Output: true Explanation: Each of the 1s are at least 2 places away from each other. ``` 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)

``` Input: nums = [1,0,0,1,0,1], k = 2 Output: false Explanation: The second 1 and third 1 are only one apart from each other. ``` 

**Constraints:**

  * `1 <= nums.length <= 105`
  * `0 <= k <= nums.length`
  * `nums[i]` is `0` or `1`

### Illustrations

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)

## Hints

1. Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

## ⚡ AI-Generated Solution (llama-3.3-70b-versatile)

### Approach

The approach is to iterate through the binary array and keep track of the position of the last encountered 1. If a 1 is found and the distance between the current position and the last encountered 1 is less than k, return false. Otherwise, update the position of the last encountered 1. If the iteration completes without finding any 1s that are less than k places apart, return true.

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
class Solution { public: bool kLengthApart(vector<int>& nums, int k) { int last = -k - 1; for (int i = 0; i < nums.size(); i++) { if (nums[i] == 1) { if (i - last <= k) return false; last = i; } } return true; } };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution { public boolean kLengthApart(int[] nums, int k) { int last = -k - 1; for (int i = 0; i < nums.length; i++) { if (nums[i] == 1) { if (i - last <= k) return false; last = i; } } return true; } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution: def kLengthApart(self, nums: list[int], k: int) -> bool: last = -k - 1; for i, num in enumerate(nums): if num == 1: if i - last <= k: return False; last = i; return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution: def kLengthApart(self, nums: list[int], k: int) -> bool: last = -k - 1; for i, num in enumerate(nums): if num == 1: if i - last <= k: return False; last = i; return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
bool kLengthApart(int* nums, int numsSize, int k) { int last = -k - 1; for (int i = 0; i < numsSize; i++) { if (nums[i] == 1) { if (i - last <= k) return 0; last = i; } } return 1; }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution { public bool KLengthApart(int[] nums, int k) { int last = -k - 1; for (int i = 0; i < nums.Length; i++) { if (nums[i] == 1) { if (i - last <= k) return false; last = i; } } return true; } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var kLengthApart = function(nums, k) { let last = -k - 1; for (let i = 0; i < nums.length; i++) { if (nums[i] == 1) { if (i - last <= k) return false; last = i; } } return true; };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function kLengthApart(nums: number[], k: number): boolean { let last: number = -k - 1; for (let i: number = 0; i < nums.length; i++) { if (nums[i] == 1) { if (i - last <= k) return false; last = i; } } return true; }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution { function kLengthApart($nums, $k) { $last = -$k - 1; for ($i = 0; $i < count($nums); $i++) { if ($nums[$i] == 1) { if ($i - $last <= $k) return false; $last = $i; } } return true; } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution { func kLengthApart(_ nums: [Int], _ k: Int) -> Bool { var last: Int = -k - 1; for (i, num) in nums.enumerated() { if num == 1 { if i - last <= k { return false } last = i } } return true } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution { fun kLengthApart(nums: IntArray, k: Int): Boolean { var last: Int = -k - 1; for (i in nums.indices) { if (nums[i] == 1) { if (i - last <= k) return false; last = i } } return true } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution { bool kLengthApart(List<int> nums, int k) { int last = -k - 1; for (int i = 0; i < nums.length; i++) { if (nums[i] == 1) { if (i - last <= k) return false; last = i; } } return true; } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func kLengthApart(nums []int, k int) bool { last := -k - 1; for i, num := range nums { if num == 1 { if i-last <= k { return false } last = i } } return true }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
class Solution def k_length_apart(nums, k) last = -k - 1 nums.each_with_index do |num, i| if num == 1 if i - last <= k return false end last = i end end true end end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution { def kLengthApart(nums: Array[Int], k: Int): Boolean = { var last: Int = -k - 1; nums.indices.foreach { i => if (nums(i) == 1) { if (i - last <= k) return false; last = i } }; true } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution { pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool { let mut last: i32 = -k - 1; for (i, num) in nums.into_iter().enumerate() { if num == 1 { if i as i32 - last <= k { return false; } last = i as i32; } } true } }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
(define (k-length-apart nums k) (let loop ((last (- k 1)) (nums nums)) (cond ((null? nums) #t) ((= (car nums) 1) (if (<= (- (length nums) (length (cdr nums))) last k) #f (loop (length nums) (cdr nums)))) (else (loop last (cdr nums))))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution). -export([k_length_apart/2]). k_length_apart(nums, k) -> k_length_apart(nums, k, -k-1). k_length_apart([1|nums], k, last) -> if length(nums) - length(tl(nums)) =< k -> false; true -> k_length_apart(nums, k, length(nums)); k_length_apart([_|nums], k, last) -> k_length_apart(nums, k, last); k_length_apart([], _, _) -> true.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do def k_length_apart(nums, k) do k_length_apart(nums, k, -k-1) end defp k_length_apart([1|nums], k, last) when length(nums) - length(tl(nums)) <= k, do: false defp k_length_apart([1|nums], k, _), do: k_length_apart(nums, k, length(nums)) defp k_length_apart([_|nums], k, last), do: k_length_apart(nums, k, last) defp k_length_apart([], _, _), do: true end
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the binary array, because we are making a single pass through the array.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the position of the last encountered 1.
