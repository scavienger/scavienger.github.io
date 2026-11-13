---
layout: post
title: "Keep Multiplying Found Values by Two"
date: 2025-11-19 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sorting", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int findFinalValue(vector<int>& nums, int\
        \ original) {\n        unordered_set<int> values(nums.begin(), nums.end());\n\
        \        while (values.count(original)) {\n            original *= 2;\n    \
        \    }\n        return original;\n    }\n};"
      java: "class Solution {\n    public int findFinalValue(int[] nums, int original)\
        \ {\n        Set<Integer> values = new HashSet<>();\n        for (int value\
        \ : nums) {\n            values.add(value);\n        }\n        while (values.contains(original))\
        \ {\n            original *= 2;\n        }\n        return original;\n    }\n\
        }"
      python: "class Solution(object):\n    def findFinalValue(self, nums, original):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type original: int\n\
        \        :rtype: int\n        \"\"\"\n        values = set(nums)\n        while\
        \ original in values:\n            original *= 2\n        return original"
      python3: "class Solution:\n    def findFinalValue(self, nums: list[int], original:\
        \ int) -> int:\n        values = set(nums)\n        while original in values:\n\
        \            original *= 2\n        return original"
      c: "int findFinalValue(int* nums, int numsSize, int original) {\n    int found;\n\
        \    do {\n        found = 0;\n        for (int i = 0; i < numsSize; i++) {\n\
        \            if (nums[i] == original) {\n                found = 1;\n      \
        \          original *= 2;\n                break;\n            }\n        }\n\
        \    } while (found);\n    return original;\n}"
      csharp: "public class Solution {\n    public int FindFinalValue(int[] nums, int\
        \ original) {\n        HashSet<int> values = new HashSet<int>(nums);\n     \
        \   while (values.Contains(original)) {\n            original *= 2;\n      \
        \  }\n        return original;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} original\n * @return\
        \ {number}\n */\nvar findFinalValue = function(nums, original) {\n    const\
        \ values = new Set(nums);\n    while (values.has(original)) {\n        original\
        \ *= 2;\n    }\n    return original;\n};"
      typescript: "function findFinalValue(nums: number[], original: number): number\
        \ {\n    const values = new Set(nums);\n    while (values.has(original)) {\n\
        \        original *= 2;\n    }\n    return original;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $original\n     * @return Integer\n     */\n    function findFinalValue($nums,\
        \ $original) {\n        $values = array_fill_keys($nums, true);\n        while\
        \ (isset($values[$original])) {\n            $original *= 2;\n        }\n  \
        \      return $original;\n    }\n}"
      swift: "class Solution {\n    func findFinalValue(_ nums: [Int], _ original: Int)\
        \ -> Int {\n        let values = Set(nums)\n        var current = original\n\
        \        while values.contains(current) {\n            current *= 2\n      \
        \  }\n        return current\n    }\n}"
      kotlin: "class Solution {\n    fun findFinalValue(nums: IntArray, original: Int):\
        \ Int {\n        val values = nums.toHashSet()\n        var current = original\n\
        \        while (current in values) {\n            current *= 2\n        }\n\
        \        return current\n    }\n}"
      dart: "class Solution {\n  int findFinalValue(List<int> nums, int original) {\n\
        \    final values = nums.toSet();\n    var current = original;\n    while (values.contains(current))\
        \ {\n      current *= 2;\n    }\n    return current;\n  }\n}"
      go: "func findFinalValue(nums []int, original int) int {\n    values := make(map[int]struct{},\
        \ len(nums))\n    for _, value := range nums {\n        values[value] = struct{}{}\n\
        \    }\n    for {\n        if _, found := values[original]; !found {\n     \
        \       return original\n        }\n        original *= 2\n    }\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} original\n# @return {Integer}\n\
        def find_final_value(nums, original)\n  values = nums.to_set\n  original *=\
        \ 2 while values.include?(original)\n  original\nend"
      scala: "object Solution {\n    def findFinalValue(nums: Array[Int], original:\
        \ Int): Int = {\n        val values = nums.toSet\n        var current = original\n\
        \        while (values.contains(current)) {\n            current *= 2\n    \
        \    }\n        current\n    }\n}"
      rust: "impl Solution {\n    pub fn find_final_value(nums: Vec<i32>, original:\
        \ i32) -> i32 {\n        let values: std::collections::HashSet<i32> = nums.into_iter().collect();\n\
        \        let mut current = original;\n        while values.contains(&current)\
        \ {\n            current *= 2;\n        }\n        current\n    }\n}"
      racket: "(define/contract (find-final-value nums original)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let ([values (list->set nums)])\n    (let\
        \ loop ([current original])\n      (if (set-member? values current)\n      \
        \    (loop (* current 2))\n          current))))"
      erlang: "-spec find_final_value(Nums :: [integer()], Original :: integer()) ->\
        \ integer().\nfind_final_value(Nums, Original) ->\n  Values = sets:from_list(Nums),\n\
        \  find_final_value_loop(Values, Original).\n\nfind_final_value_loop(Values,\
        \ Original) ->\n  case sets:is_element(Original, Values) of\n    true -> find_final_value_loop(Values,\
        \ Original * 2);\n    false -> Original\n  end."
      elixir: "defmodule Solution do\n  @spec find_final_value(nums :: [integer], original\
        \ :: integer) :: integer\n  def find_final_value(nums, original) do\n    values\
        \ = MapSet.new(nums)\n    find_final_value_loop(values, original)\n  end\n\n\
        \  defp find_final_value_loop(values, original) do\n    if MapSet.member?(values,\
        \ original) do\n      find_final_value_loop(values, original * 2)\n    else\n\
        \      original\n    end\n  end\nend"
    approach: 'Store all values in nums in a set for fast membership checks. Starting
      with original, repeatedly check whether the current value is in the set.


      When it is found, double it and check again. When it is absent, return the current
      value.'
    time_complexity: O(n + k), where n is the length of nums and k is the number of
      times original is doubled. Set construction takes O(n) on average, followed by
      O(k) average membership checks.
    space_complexity: O(n) for the set containing the values from nums.
    elapsed_time: 37.46995782852173
    model: gpt-6-luna
    generated_at: '2026-11-13 00:05:43 '
---

## Problem #2154: Keep Multiplying Found Values by Two

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sorting, Simulation

## Problem Description

<p>You are given an array of integers <code>nums</code>. You are also given an integer <code>original</code> which is the first number that needs to be searched for in <code>nums</code>.</p>

<p>You then do the following steps:</p>

<ol>
	<li>If <code>original</code> is found in <code>nums</code>, <strong>multiply</strong> it by two (i.e., set <code>original = 2 * original</code>).</li>
	<li>Otherwise, <strong>stop</strong> the process.</li>
	<li><strong>Repeat</strong> this process with the new number as long as you keep finding the number.</li>
</ol>

<p>Return <em>the <strong>final</strong> value of </em><code>original</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,3,6,1,12], original = 3
<strong>Output:</strong> 24
<strong>Explanation:</strong> 
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,9], original = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
- 4 is not found in nums. Thus, 4 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], original &lt;= 1000</code></li>
</ul>


## Hints

1. Repeatedly iterate through the array and check if the current value of original is in the array.

2. If original is not found, stop and return its current value.

3. Otherwise, multiply original by 2 and repeat the process.

4. Use set data structure to check the existence faster.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Store all values in nums in a set for fast membership checks. Starting with original, repeatedly check whether the current value is in the set.

When it is found, double it and check again. When it is absent, return the current value.

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
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int> values(nums.begin(), nums.end());
        while (values.count(original)) {
            original *= 2;
        }
        return original;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> values = new HashSet<>();
        for (int value : nums) {
            values.add(value);
        }
        while (values.contains(original)) {
            original *= 2;
        }
        return original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        values = set(nums)
        while original in values:
            original *= 2
        return original
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        values = set(nums)
        while original in values:
            original *= 2
        return original
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int findFinalValue(int* nums, int numsSize, int original) {
    int found;
    do {
        found = 0;
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] == original) {
                found = 1;
                original *= 2;
                break;
            }
        }
    } while (found);
    return original;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        HashSet<int> values = new HashSet<int>(nums);
        while (values.Contains(original)) {
            original *= 2;
        }
        return original;
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
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    const values = new Set(nums);
    while (values.has(original)) {
        original *= 2;
    }
    return original;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findFinalValue(nums: number[], original: number): number {
    const values = new Set(nums);
    while (values.has(original)) {
        original *= 2;
    }
    return original;
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
     * @param Integer $original
     * @return Integer
     */
    function findFinalValue($nums, $original) {
        $values = array_fill_keys($nums, true);
        while (isset($values[$original])) {
            $original *= 2;
        }
        return $original;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findFinalValue(_ nums: [Int], _ original: Int) -> Int {
        let values = Set(nums)
        var current = original
        while values.contains(current) {
            current *= 2
        }
        return current
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findFinalValue(nums: IntArray, original: Int): Int {
        val values = nums.toHashSet()
        var current = original
        while (current in values) {
            current *= 2
        }
        return current
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int findFinalValue(List<int> nums, int original) {
    final values = nums.toSet();
    var current = original;
    while (values.contains(current)) {
      current *= 2;
    }
    return current;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findFinalValue(nums []int, original int) int {
    values := make(map[int]struct{}, len(nums))
    for _, value := range nums {
        values[value] = struct{}{}
    }
    for {
        if _, found := values[original]; !found {
            return original
        }
        original *= 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} original
# @return {Integer}
def find_final_value(nums, original)
  values = nums.to_set
  original *= 2 while values.include?(original)
  original
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findFinalValue(nums: Array[Int], original: Int): Int = {
        val values = nums.toSet
        var current = original
        while (values.contains(current)) {
            current *= 2
        }
        current
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let values: std::collections::HashSet<i32> = nums.into_iter().collect();
        let mut current = original;
        while values.contains(&current) {
            current *= 2;
        }
        current
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-final-value nums original)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([values (list->set nums)])
    (let loop ([current original])
      (if (set-member? values current)
          (loop (* current 2))
          current))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_final_value(Nums :: [integer()], Original :: integer()) -> integer().
find_final_value(Nums, Original) ->
  Values = sets:from_list(Nums),
  find_final_value_loop(Values, Original).

find_final_value_loop(Values, Original) ->
  case sets:is_element(Original, Values) of
    true -> find_final_value_loop(Values, Original * 2);
    false -> Original
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_final_value(nums :: [integer], original :: integer) :: integer
  def find_final_value(nums, original) do
    values = MapSet.new(nums)
    find_final_value_loop(values, original)
  end

  defp find_final_value_loop(values, original) do
    if MapSet.member?(values, original) do
      find_final_value_loop(values, original * 2)
    else
      original
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + k), where n is the length of nums and k is the number of times original is doubled. Set construction takes O(n) on average, followed by O(k) average membership checks.
- **Space Complexity:** O(n) for the set containing the values from nums.
