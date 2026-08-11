---
layout: post
title: "Smallest Missing Integer Greater Than Sequential Prefix Sum"
date: 2026-08-11 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int missingInteger(vector<int>& nums) {\n\
        \        int prefixSum = nums[0];\n        for (int i = 1; i < nums.size();\
        \ ++i) {\n            if (nums[i] == nums[i - 1] + 1) {\n                prefixSum\
        \ += nums[i];\n            } else {\n                break;\n            }\n\
        \        }\n\n        unordered_set<int> seen(nums.begin(), nums.end());\n \
        \       while (seen.count(prefixSum)) {\n            prefixSum++;\n        }\n\
        \        return prefixSum;\n    }\n};"
      java: "class Solution {\n    public int missingInteger(int[] nums) {\n       \
        \ int prefixSum = nums[0];\n        for (int i = 1; i < nums.length; i++) {\n\
        \            if (nums[i] == nums[i - 1] + 1) {\n                prefixSum +=\
        \ nums[i];\n            } else {\n                break;\n            }\n  \
        \      }\n\n        Set<Integer> seen = new HashSet<>();\n        for (int num\
        \ : nums) {\n            seen.add(num);\n        }\n\n        while (seen.contains(prefixSum))\
        \ {\n            prefixSum++;\n        }\n        return prefixSum;\n    }\n\
        }"
      python: "class Solution(object):\n    def missingInteger(self, nums):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\
        \n        prefix_sum = nums[0]\n        for i in range(1, len(nums)):\n    \
        \        if nums[i] == nums[i-1] + 1:\n                prefix_sum += nums[i]\n\
        \            else:\n                break\n\n        seen = set(nums)\n    \
        \    while prefix_sum in seen:\n            prefix_sum += 1\n        return\
        \ prefix_sum"
      python3: "class Solution:\n    def missingInteger(self, nums: List[int]) -> int:\n\
        \        prefix_sum = nums[0]\n        for i in range(1, len(nums)):\n     \
        \       if nums[i] == nums[i-1] + 1:\n                prefix_sum += nums[i]\n\
        \            else:\n                break\n\n        seen = set(nums)\n    \
        \    while prefix_sum in seen:\n            prefix_sum += 1\n        return\
        \ prefix_sum"
      c: "int missingInteger(int* nums, int numsSize) {\n    int prefixSum = nums[0];\n\
        \    for (int i = 1; i < numsSize; i++) {\n        if (nums[i] == nums[i - 1]\
        \ + 1) {\n            prefixSum += nums[i];\n        } else {\n            break;\n\
        \        }\n    }\n\n    while (1) {\n        int found = 0;\n        for (int\
        \ i = 0; i < numsSize; i++) {\n            if (nums[i] == prefixSum) {\n   \
        \             found = 1;\n                break;\n            }\n        }\n\
        \        if (!found) {\n            return prefixSum;\n        }\n        prefixSum++;\n\
        \    }\n}"
      csharp: "public class Solution {\n    public int MissingInteger(int[] nums) {\n\
        \        int prefixSum = nums[0];\n        for (int i = 1; i < nums.Length;\
        \ i++) {\n            if (nums[i] == nums[i - 1] + 1) {\n                prefixSum\
        \ += nums[i];\n            } else {\n                break;\n            }\n\
        \        }\n\n        HashSet<int> seen = new HashSet<int>(nums);\n        while\
        \ (seen.Contains(prefixSum)) {\n            prefixSum++;\n        }\n      \
        \  return prefixSum;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar missingInteger\
        \ = function(nums) {\n    let prefixSum = nums[0];\n    for (let i = 1; i <\
        \ nums.length; i++) {\n        if (nums[i] === nums[i - 1] + 1) {\n        \
        \    prefixSum += nums[i];\n        } else {\n            break;\n        }\n\
        \    }\n\n    const seen = new Set(nums);\n    while (seen.has(prefixSum)) {\n\
        \        prefixSum++;\n    }\n    return prefixSum;\n};"
      typescript: "function missingInteger(nums: number[]): number {\n    let sum =\
        \ nums[0];\n    for (let i = 1; i < nums.length; i++) {\n        if (nums[i]\
        \ === nums[i - 1] + 1) {\n            sum += nums[i];\n        } else {\n  \
        \          break;\n        }\n    }\n    const numSet = new Set(nums);\n   \
        \ let result = sum;\n    while (numSet.has(result)) {\n        result++;\n \
        \   }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function missingInteger($nums) {\n        $sum = $nums[0];\n\
        \        for ($i = 1; $i < count($nums); $i++) {\n            if ($nums[$i]\
        \ == $nums[$i - 1] + 1) {\n                $sum += $nums[$i];\n            }\
        \ else {\n                break;\n            }\n        }\n        $numSet\
        \ = array_flip($nums);\n        $result = $sum;\n        while (isset($numSet[$result]))\
        \ {\n            $result++;\n        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func missingInteger(_ nums: [Int]) -> Int {\n  \
        \      var sum = nums[0]\n        for i in 1..<nums.count {\n            if\
        \ nums[i] == nums[i - 1] + 1 {\n                sum += nums[i]\n           \
        \ } else {\n                break\n            }\n        }\n        let numSet\
        \ = Set(nums)\n        var result = sum\n        while numSet.contains(result)\
        \ {\n            result += 1\n        }\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun missingInteger(nums: IntArray): Int {\n   \
        \     var sum = nums[0]\n        for (i in 1 until nums.size) {\n          \
        \  if (nums[i] == nums[i - 1] + 1) {\n                sum += nums[i]\n     \
        \       } else {\n                break\n            }\n        }\n        val\
        \ numSet = nums.toSet()\n        var result = sum\n        while (numSet.contains(result))\
        \ {\n            result++\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  int missingInteger(List<int> nums) {\n    int sum =\
        \ nums[0];\n    for (int i = 1; i < nums.length; i++) {\n      if (nums[i] ==\
        \ nums[i - 1] + 1) {\n        sum += nums[i];\n      } else {\n        break;\n\
        \      }\n    }\n    Set<int> numSet = nums.toSet();\n    int result = sum;\n\
        \    while (numSet.contains(result)) {\n      result++;\n    }\n    return result;\n\
        \  }\n}"
      go: "func missingInteger(nums []int) int {\n    sum := nums[0]\n    for i := 1;\
        \ i < len(nums); i++ {\n        if nums[i] == nums[i-1]+1 {\n            sum\
        \ += nums[i]\n        } else {\n            break\n        }\n    }\n    numMap\
        \ := make(map[int]bool)\n    for _, v := range nums {\n        numMap[v] = true\n\
        \    }\n    result := sum\n    for numMap[result] {\n        result++\n    }\n\
        \    return result\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef missing_integer(nums)\n\
        \  sum = nums[0]\n  (1...nums.length).each do |i|\n    if nums[i] == nums[i-1]\
        \ + 1\n      sum += nums[i]\n    else\n      break\n    end\n  end\n  while\
        \ nums.include?(sum)\n    sum += 1\n  end\n  sum\nend"
      scala: "object Solution {\n    def missingInteger(nums: Array[Int]): Int = {\n\
        \        var sum = nums(0)\n        var i = 1\n        while (i < nums.length\
        \ && nums(i) == nums(i - 1) + 1) {\n            sum += nums(i)\n           \
        \ i += 1\n        }\n        var currentSum = sum\n        while (nums.contains(currentSum))\
        \ {\n            currentSum += 1\n        }\n        currentSum\n    }\n}"
      rust: "impl Solution {\n    pub fn missing_integer(nums: Vec<i32>) -> i32 {\n\
        \        let mut sum = nums[0];\n        for i in 1..nums.len() {\n        \
        \    if nums[i] == nums[i - 1] + 1 {\n                sum += nums[i];\n    \
        \        } else {\n                break;\n            }\n        }\n      \
        \  let mut current_sum = sum;\n        while nums.contains(&current_sum) {\n\
        \            current_sum += 1;\n        }\n        current_sum\n    }\n}"
      racket: "(define/contract (missing-integer nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([first-val (car nums)]\n         [prefix-sum (let\
        \ loop ([lst (cdr nums)] [prev first-val] [acc first-val])\n               \
        \        (cond\n                         [(null? lst) acc]\n               \
        \          [(= (car lst) (+ prev 1)) (loop (cdr lst) (car lst) (+ acc (car lst)))]\n\
        \                         [else acc]))])\n    (let loop-missing ([curr prefix-sum])\n\
        \      (if (member curr nums)\n          (loop-missing (+ curr 1))\n       \
        \   curr))))"
      erlang: "-spec missing_integer(Nums :: [integer()]) -> integer().\nmissing_integer(Nums)\
        \ ->\n    [H | T] = Nums,\n    PrefixSum = find_prefix_sum(T, H, H),\n    find_missing(PrefixSum,\
        \ Nums).\n\nfind_prefix_sum([H | T], Prev, Acc) when H == Prev + 1 ->\n    find_prefix_sum(T,\
        \ H, Acc + H);\nfind_prefix_sum(_, _, Acc) ->\n    Acc.\n\nfind_missing(Sum,\
        \ Nums) ->\n    case lists:member(Sum, Nums) of\n        true -> find_missing(Sum\
        \ + 1, Nums);\n        false -> Sum\n    end."
      elixir: "defmodule Solution do\n  @spec missing_integer(nums :: [integer]) ::\
        \ integer\n  def missing_integer([h | t] = nums) do\n    prefix_sum = find_prefix_sum(t,\
        \ h, h)\n    find_missing(prefix_sum, nums)\n  end\n\n  defp find_prefix_sum([h\
        \ | t], prev, acc) when h == prev + 1 do\n    find_prefix_sum(t, h, acc + h)\n\
        \  end\n  defp find_prefix_sum(_, _, acc), do: acc\n\n  defp find_missing(sum,\
        \ nums) do\n    if Enum.member?(nums, sum) do\n      find_missing(sum + 1, nums)\n\
        \    else\n      sum\n    end\n  end\nend"
    approach: 'The problem asks for the smallest integer $x$ that is missing from the
      entire array $nums$, provided that $x$ is greater than or equal to the sum of
      the longest sequential prefix. A sequential prefix $nums[0..i]$ is defined such
      that each element is exactly one greater than the preceding element. We first
      iterate through the array starting from the first element, adding $nums[i]$ to
      a running total as long as $nums[i] = nums[i-1] + 1$. Once this condition fails,
      we stop, and the current total represents the sum of the longest sequential prefix.


      After calculating the prefix sum, we must find the smallest integer $x \ge \text{sum}$
      that is not present anywhere in the original array $nums$. To do this efficiently,
      we store all elements of $nums$ in a hash set (or perform a search) for quick
      lookup. Starting from the calculated sum, we check if the value exists in the
      set. If it does, we increment the value by one and repeat the check until we find
      a value that is not in the set. This value is the smallest missing integer we
      need to return.'
    time_complexity: O(N) where N is the length of the array. Finding the longest sequential
      prefix takes $O(N)$ time by iterating through the array once. Building a hash
      set for existence checks also takes $O(N)$ time. In the worst case, we might increment
      the prefix sum up to $N$ times, with each lookup taking $O(1)$ on average, leading
      to a total linear time complexity.
    space_complexity: O(N) to store the elements of the input array in a hash set for
      efficient existence checks. In the C implementation, where we use linear scanning
      for existence, the space complexity is O(1) beyond the input array storage.
    elapsed_time: 90.34905886650085
    model: gemini-3-flash-preview
    generated_at: '2026-08-11 01:08:37 '
---

## Problem #2996: Smallest Missing Integer Greater Than Sequential Prefix Sum

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sorting

## Problem Description

<p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code>.</p>

<p>A prefix <code>nums[0..i]</code> is <strong>sequential</strong> if, for all <code>1 &lt;= j &lt;= i</code>, <code>nums[j] = nums[j - 1] + 1</code>. In particular, the prefix consisting only of <code>nums[0]</code> is <strong>sequential</strong>.</p>

<p>Return <em>the <strong>smallest</strong> integer</em> <code>x</code> <em>missing from</em> <code>nums</code> <em>such that</em> <code>x</code> <em>is greater than or equal to the sum of the <strong>longest</strong> sequential prefix.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,2,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,12,14,13]
<strong>Output:</strong> 15
<strong>Explanation:</strong> The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## Hints

1. To find the longest sequential prefix, iterate from left to right. For a fixed `i`, if `nums[i] != nums[i - 1] + 1` then the longest sequential prefix ends at `i - 1`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the smallest integer $x$ that is missing from the entire array $nums$, provided that $x$ is greater than or equal to the sum of the longest sequential prefix. A sequential prefix $nums[0..i]$ is defined such that each element is exactly one greater than the preceding element. We first iterate through the array starting from the first element, adding $nums[i]$ to a running total as long as $nums[i] = nums[i-1] + 1$. Once this condition fails, we stop, and the current total represents the sum of the longest sequential prefix.

After calculating the prefix sum, we must find the smallest integer $x \ge \text{sum}$ that is not present anywhere in the original array $nums$. To do this efficiently, we store all elements of $nums$ in a hash set (or perform a search) for quick lookup. Starting from the calculated sum, we check if the value exists in the set. If it does, we increment the value by one and repeat the check until we find a value that is not in the set. This value is the smallest missing integer we need to return.

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
    int missingInteger(vector<int>& nums) {
        int prefixSum = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1] + 1) {
                prefixSum += nums[i];
            } else {
                break;
            }
        }

        unordered_set<int> seen(nums.begin(), nums.end());
        while (seen.count(prefixSum)) {
            prefixSum++;
        }
        return prefixSum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int missingInteger(int[] nums) {
        int prefixSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                prefixSum += nums[i];
            } else {
                break;
            }
        }

        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            seen.add(num);
        }

        while (seen.contains(prefixSum)) {
            prefixSum++;
        }
        return prefixSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefix_sum += nums[i]
            else:
                break

        seen = set(nums)
        while prefix_sum in seen:
            prefix_sum += 1
        return prefix_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefix_sum += nums[i]
            else:
                break

        seen = set(nums)
        while prefix_sum in seen:
            prefix_sum += 1
        return prefix_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int missingInteger(int* nums, int numsSize) {
    int prefixSum = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1] + 1) {
            prefixSum += nums[i];
        } else {
            break;
        }
    }

    while (1) {
        int found = 0;
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] == prefixSum) {
                found = 1;
                break;
            }
        }
        if (!found) {
            return prefixSum;
        }
        prefixSum++;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MissingInteger(int[] nums) {
        int prefixSum = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                prefixSum += nums[i];
            } else {
                break;
            }
        }

        HashSet<int> seen = new HashSet<int>(nums);
        while (seen.Contains(prefixSum)) {
            prefixSum++;
        }
        return prefixSum;
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
var missingInteger = function(nums) {
    let prefixSum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1] + 1) {
            prefixSum += nums[i];
        } else {
            break;
        }
    }

    const seen = new Set(nums);
    while (seen.has(prefixSum)) {
        prefixSum++;
    }
    return prefixSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function missingInteger(nums: number[]): number {
    let sum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1] + 1) {
            sum += nums[i];
        } else {
            break;
        }
    }
    const numSet = new Set(nums);
    let result = sum;
    while (numSet.has(result)) {
        result++;
    }
    return result;
};
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
    function missingInteger($nums) {
        $sum = $nums[0];
        for ($i = 1; $i < count($nums); $i++) {
            if ($nums[$i] == $nums[$i - 1] + 1) {
                $sum += $nums[$i];
            } else {
                break;
            }
        }
        $numSet = array_flip($nums);
        $result = $sum;
        while (isset($numSet[$result])) {
            $result++;
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
    func missingInteger(_ nums: [Int]) -> Int {
        var sum = nums[0]
        for i in 1..<nums.count {
            if nums[i] == nums[i - 1] + 1 {
                sum += nums[i]
            } else {
                break
            }
        }
        let numSet = Set(nums)
        var result = sum
        while numSet.contains(result) {
            result += 1
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
    fun missingInteger(nums: IntArray): Int {
        var sum = nums[0]
        for (i in 1 until nums.size) {
            if (nums[i] == nums[i - 1] + 1) {
                sum += nums[i]
            } else {
                break
            }
        }
        val numSet = nums.toSet()
        var result = sum
        while (numSet.contains(result)) {
            result++
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
  int missingInteger(List<int> nums) {
    int sum = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] == nums[i - 1] + 1) {
        sum += nums[i];
      } else {
        break;
      }
    }
    Set<int> numSet = nums.toSet();
    int result = sum;
    while (numSet.contains(result)) {
      result++;
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
func missingInteger(nums []int) int {
    sum := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] == nums[i-1]+1 {
            sum += nums[i]
        } else {
            break
        }
    }
    numMap := make(map[int]bool)
    for _, v := range nums {
        numMap[v] = true
    }
    result := sum
    for numMap[result] {
        result++
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def missing_integer(nums)
  sum = nums[0]
  (1...nums.length).each do |i|
    if nums[i] == nums[i-1] + 1
      sum += nums[i]
    else
      break
    end
  end
  while nums.include?(sum)
    sum += 1
  end
  sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def missingInteger(nums: Array[Int]): Int = {
        var sum = nums(0)
        var i = 1
        while (i < nums.length && nums(i) == nums(i - 1) + 1) {
            sum += nums(i)
            i += 1
        }
        var currentSum = sum
        while (nums.contains(currentSum)) {
            currentSum += 1
        }
        currentSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        let mut sum = nums[0];
        for i in 1..nums.len() {
            if nums[i] == nums[i - 1] + 1 {
                sum += nums[i];
            } else {
                break;
            }
        }
        let mut current_sum = sum;
        while nums.contains(&current_sum) {
            current_sum += 1;
        }
        current_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (missing-integer nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([first-val (car nums)]
         [prefix-sum (let loop ([lst (cdr nums)] [prev first-val] [acc first-val])
                       (cond
                         [(null? lst) acc]
                         [(= (car lst) (+ prev 1)) (loop (cdr lst) (car lst) (+ acc (car lst)))]
                         [else acc]))])
    (let loop-missing ([curr prefix-sum])
      (if (member curr nums)
          (loop-missing (+ curr 1))
          curr))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec missing_integer(Nums :: [integer()]) -> integer().
missing_integer(Nums) ->
    [H | T] = Nums,
    PrefixSum = find_prefix_sum(T, H, H),
    find_missing(PrefixSum, Nums).

find_prefix_sum([H | T], Prev, Acc) when H == Prev + 1 ->
    find_prefix_sum(T, H, Acc + H);
find_prefix_sum(_, _, Acc) ->
    Acc.

find_missing(Sum, Nums) ->
    case lists:member(Sum, Nums) of
        true -> find_missing(Sum + 1, Nums);
        false -> Sum
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec missing_integer(nums :: [integer]) :: integer
  def missing_integer([h | t] = nums) do
    prefix_sum = find_prefix_sum(t, h, h)
    find_missing(prefix_sum, nums)
  end

  defp find_prefix_sum([h | t], prev, acc) when h == prev + 1 do
    find_prefix_sum(t, h, acc + h)
  end
  defp find_prefix_sum(_, _, acc), do: acc

  defp find_missing(sum, nums) do
    if Enum.member?(nums, sum) do
      find_missing(sum + 1, nums)
    else
      sum
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the array. Finding the longest sequential prefix takes $O(N)$ time by iterating through the array once. Building a hash set for existence checks also takes $O(N)$ time. In the worst case, we might increment the prefix sum up to $N$ times, with each lookup taking $O(1)$ on average, leading to a total linear time complexity.
- **Space Complexity:** O(N) to store the elements of the input array in a hash set for efficient existence checks. In the C implementation, where we use linear scanning for existence, the space complexity is O(1) beyond the input array storage.
