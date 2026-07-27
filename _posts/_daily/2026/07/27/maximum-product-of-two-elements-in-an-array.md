---
layout: post
title: "Maximum Product of Two Elements in an Array"
date: 2026-07-27 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Sorting", "Heap (Priority Queue)"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProduct(vector<int>& nums) {\n   \
        \     int max1 = 0;\n        int max2 = 0;\n        for (int num : nums) {\n\
        \            if (num > max1) {\n                max2 = max1;\n             \
        \   max1 = num;\n            } else if (num > max2) {\n                max2\
        \ = num;\n            }\n        }\n        return (max1 - 1) * (max2 - 1);\n\
        \    }\n};"
      java: "class Solution {\n    public int maxProduct(int[] nums) {\n        int\
        \ max1 = 0;\n        int max2 = 0;\n        for (int num : nums) {\n       \
        \     if (num > max1) {\n                max2 = max1;\n                max1\
        \ = num;\n            } else if (num > max2) {\n                max2 = num;\n\
        \            }\n        }\n        return (max1 - 1) * (max2 - 1);\n    }\n}"
      python: "class Solution(object):\n    def maxProduct(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n   \
        \     max1 = 0\n        max2 = 0\n        for num in nums:\n            if num\
        \ > max1:\n                max2 = max1\n                max1 = num\n       \
        \     elif num > max2:\n                max2 = num\n        return (max1 - 1)\
        \ * (max2 - 1)"
      python3: "class Solution:\n    def maxProduct(self, nums: List[int]) -> int:\n\
        \        max1 = 0\n        max2 = 0\n        for num in nums:\n            if\
        \ num > max1:\n                max2 = max1\n                max1 = num\n   \
        \         elif num > max2:\n                max2 = num\n        return (max1\
        \ - 1) * (max2 - 1)"
      c: "int maxProduct(int* nums, int numsSize) {\n    int max1 = 0;\n    int max2\
        \ = 0;\n    for (int i = 0; i < numsSize; i++) {\n        if (nums[i] > max1)\
        \ {\n            max2 = max1;\n            max1 = nums[i];\n        } else if\
        \ (nums[i] > max2) {\n            max2 = nums[i];\n        }\n    }\n    return\
        \ (max1 - 1) * (max2 - 1);\n}"
      csharp: "public class Solution {\n    public int MaxProduct(int[] nums) {\n  \
        \      int max1 = 0;\n        int max2 = 0;\n        foreach (int num in nums)\
        \ {\n            if (num > max1) {\n                max2 = max1;\n         \
        \       max1 = num;\n            } else if (num > max2) {\n                max2\
        \ = num;\n            }\n        }\n        return (max1 - 1) * (max2 - 1);\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxProduct\
        \ = function(nums) {\n    let max1 = 0;\n    let max2 = 0;\n    for (let num\
        \ of nums) {\n        if (num > max1) {\n            max2 = max1;\n        \
        \    max1 = num;\n        } else if (num > max2) {\n            max2 = num;\n\
        \        }\n    }\n    return (max1 - 1) * (max2 - 1);\n};"
      typescript: "function maxProduct(nums: number[]): number {\n    let max1 = 0;\n\
        \    let max2 = 0;\n    for (const num of nums) {\n        if (num > max1) {\n\
        \            max2 = max1;\n            max1 = num;\n        } else if (num >\
        \ max2) {\n            max2 = num;\n        }\n    }\n    return (max1 - 1)\
        \ * (max2 - 1);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxProduct($nums) {\n        $max1 = 0;\n \
        \       $max2 = 0;\n        foreach ($nums as $num) {\n            if ($num\
        \ > $max1) {\n                $max2 = $max1;\n                $max1 = $num;\n\
        \            } else if ($num > $max2) {\n                $max2 = $num;\n   \
        \         }\n        }\n        return ($max1 - 1) * ($max2 - 1);\n    }\n}"
      swift: "class Solution {\n    func maxProduct(_ nums: [Int]) -> Int {\n      \
        \  var max1 = 0\n        var max2 = 0\n        for num in nums {\n         \
        \   if num > max1 {\n                max2 = max1\n                max1 = num\n\
        \            } else if num > max2 {\n                max2 = num\n          \
        \  }\n        }\n        return (max1 - 1) * (max2 - 1)\n    }\n}"
      kotlin: "class Solution {\n    fun maxProduct(nums: IntArray): Int {\n       \
        \ var max1 = 0\n        var max2 = 0\n        for (num in nums) {\n        \
        \    if (num > max1) {\n                max2 = max1\n                max1 =\
        \ num\n            } else if (num > max2) {\n                max2 = num\n  \
        \          }\n        }\n        return (max1 - 1) * (max2 - 1)\n    }\n}"
      dart: "class Solution {\n  int maxProduct(List<int> nums) {\n    int max1 = 0;\n\
        \    int max2 = 0;\n    for (int num in nums) {\n      if (num > max1) {\n \
        \       max2 = max1;\n        max1 = num;\n      } else if (num > max2) {\n\
        \        max2 = num;\n      }\n    }\n    return (max1 - 1) * (max2 - 1);\n\
        \  }\n}"
      go: "func maxProduct(nums []int) int {\n    max1 := 0\n    max2 := 0\n    for\
        \ _, num := range nums {\n        if num > max1 {\n            max2 = max1\n\
        \            max1 = num\n        } else if num > max2 {\n            max2 =\
        \ num\n        }\n    }\n    return (max1 - 1) * (max2 - 1)\n}"
      ruby: "def max_product(nums)\n  max1 = 0\n  max2 = 0\n  nums.each do |n|\n   \
        \ if n > max1\n      max2 = max1\n      max1 = n\n    elsif n > max2\n     \
        \ max2 = n\n    end\n  end\n  (max1 - 1) * (max2 - 1)\nend"
      scala: "object Solution {\n    def maxProduct(nums: Array[Int]): Int = {\n   \
        \     var max1 = 0\n        var max2 = 0\n        for (n <- nums) {\n      \
        \      if (n > max1) {\n                max2 = max1\n                max1 =\
        \ n\n            } else if (n > max2) {\n                max2 = n\n        \
        \    }\n        }\n        (max1 - 1) * (max2 - 1)\n    }\n}"
      rust: "impl Solution {\n    pub fn max_product(nums: Vec<i32>) -> i32 {\n    \
        \    let mut max1 = 0;\n        let mut max2 = 0;\n        for n in nums {\n\
        \            if n > max1 {\n                max2 = max1;\n                max1\
        \ = n;\n            } else if n > max2 {\n                max2 = n;\n      \
        \      }\n        }\n        (max1 - 1) * (max2 - 1)\n    }\n}"
      racket: "(define/contract (max-product nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let loop ([ns nums] [m1 0] [m2 0])\n    (if (null? ns)\n        (* (- m1\
        \ 1) (- m2 1))\n        (let ([n (car ns)])\n          (cond\n            [(>\
        \ n m1) (loop (cdr ns) n m1)]\n            [(> n m2) (loop (cdr ns) m1 n)]\n\
        \            [else (loop (cdr ns) m1 m2)])))))"
      erlang: "-spec max_product(Nums :: [integer()]) -> integer().\nmax_product(Nums)\
        \ ->\n  find_maxes(Nums, 0, 0).\n\nfind_maxes([], M1, M2) ->\n  (M1 - 1) * (M2\
        \ - 1);\nfind_maxes([H | T], M1, M2) ->\n  if\n    H > M1 -> find_maxes(T, H,\
        \ M1);\n    H > M2 -> find_maxes(T, M1, H);\n    true -> find_maxes(T, M1, M2)\n\
        \  end."
      elixir: "defmodule Solution do\n  @spec max_product(nums :: [integer]) :: integer\n\
        \  def max_product(nums) do\n    {m1, m2} = Enum.reduce(nums, {0, 0}, fn n,\
        \ {m1, m2} ->\n      cond do\n        n > m1 -> {n, m1}\n        n > m2 -> {m1,\
        \ n}\n        true -> {m1, m2}\n      end\n    end)\n    (m1 - 1) * (m2 - 1)\n\
        \  end\nend"
    approach: 'To maximize the product (nums[i]-1) * (nums[j]-1), we must identify the
      two largest values in the given array. Since all elements are positive integers
      (at least 1), the expressions (nums[i]-1) and (nums[j]-1) will always be non-negative.
      Maximizing the product of two non-negative terms is achieved by selecting the
      two largest possible factors from the set.


      We can find these two maximum values efficiently in a single pass through the
      array. We maintain two variables, max1 and max2, representing the largest and
      second-largest values found so far. For each element in the array, we compare
      it to max1; if it is larger, we update max2 to be the current max1 and then set
      max1 to the new element. If it is not larger than max1 but is larger than max2,
      we simply update max2. After processing all elements, we calculate and return
      the product (max1 - 1) * (max2 - 1).'
    time_complexity: O(n) where n is the length of the input array. This is because
      we perform a single linear scan through the array to find the two largest elements,
      performing a constant number of comparisons at each step.
    space_complexity: O(1) because we only utilize a fixed number of integer variables
      (max1 and max2) to store the top two elements, regardless of the input size.
    elapsed_time: 46.176475286483765
    model: gemini-3-flash-preview
    generated_at: '2026-07-27 02:10:22 '
---

## Problem #1464: Maximum Product of Two Elements in an Array

**Difficulty:** Easy

**Topics:** Array, Sorting, Heap (Priority Queue)

## Problem Description

Given the array of integers <code>nums</code>, you will choose two different indices <code>i</code> and <code>j</code> of that array. <em>Return the maximum value of</em> <code>(nums[i]-1)*(nums[j]-1)</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,2]
<strong>Output:</strong> 12 
<strong>Explanation:</strong> If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,4,5]
<strong>Output:</strong> 16
<strong>Explanation:</strong> Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,7]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul>


## Hints

1. Use brute force: two loops to select i and j, then select the maximum value of (nums[i]-1)*(nums[j]-1).

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To maximize the product (nums[i]-1) * (nums[j]-1), we must identify the two largest values in the given array. Since all elements are positive integers (at least 1), the expressions (nums[i]-1) and (nums[j]-1) will always be non-negative. Maximizing the product of two non-negative terms is achieved by selecting the two largest possible factors from the set.

We can find these two maximum values efficiently in a single pass through the array. We maintain two variables, max1 and max2, representing the largest and second-largest values found so far. For each element in the array, we compare it to max1; if it is larger, we update max2 to be the current max1 and then set max1 to the new element. If it is not larger than max1 but is larger than max2, we simply update max2. After processing all elements, we calculate and return the product (max1 - 1) * (max2 - 1).

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
    int maxProduct(vector<int>& nums) {
        int max1 = 0;
        int max2 = 0;
        for (int num : nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProduct(int[] nums) {
        int max1 = 0;
        int max2 = 0;
        for (int num : nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }
        return (max1 - 1) * (max2 - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        max2 = 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxProduct(int* nums, int numsSize) {
    int max1 = 0;
    int max2 = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > max1) {
            max2 = max1;
            max1 = nums[i];
        } else if (nums[i] > max2) {
            max2 = nums[i];
        }
    }
    return (max1 - 1) * (max2 - 1);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProduct(int[] nums) {
        int max1 = 0;
        int max2 = 0;
        foreach (int num in nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }
        return (max1 - 1) * (max2 - 1);
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
var maxProduct = function(nums) {
    let max1 = 0;
    let max2 = 0;
    for (let num of nums) {
        if (num > max1) {
            max2 = max1;
            max1 = num;
        } else if (num > max2) {
            max2 = num;
        }
    }
    return (max1 - 1) * (max2 - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProduct(nums: number[]): number {
    let max1 = 0;
    let max2 = 0;
    for (const num of nums) {
        if (num > max1) {
            max2 = max1;
            max1 = num;
        } else if (num > max2) {
            max2 = num;
        }
    }
    return (max1 - 1) * (max2 - 1);
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
    function maxProduct($nums) {
        $max1 = 0;
        $max2 = 0;
        foreach ($nums as $num) {
            if ($num > $max1) {
                $max2 = $max1;
                $max1 = $num;
            } else if ($num > $max2) {
                $max2 = $num;
            }
        }
        return ($max1 - 1) * ($max2 - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        var max1 = 0
        var max2 = 0
        for num in nums {
            if num > max1 {
                max2 = max1
                max1 = num
            } else if num > max2 {
                max2 = num
            }
        }
        return (max1 - 1) * (max2 - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProduct(nums: IntArray): Int {
        var max1 = 0
        var max2 = 0
        for (num in nums) {
            if (num > max1) {
                max2 = max1
                max1 = num
            } else if (num > max2) {
                max2 = num
            }
        }
        return (max1 - 1) * (max2 - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxProduct(List<int> nums) {
    int max1 = 0;
    int max2 = 0;
    for (int num in nums) {
      if (num > max1) {
        max2 = max1;
        max1 = num;
      } else if (num > max2) {
        max2 = num;
      }
    }
    return (max1 - 1) * (max2 - 1);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxProduct(nums []int) int {
    max1 := 0
    max2 := 0
    for _, num := range nums {
        if num > max1 {
            max2 = max1
            max1 = num
        } else if num > max2 {
            max2 = num
        }
    }
    return (max1 - 1) * (max2 - 1)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_product(nums)
  max1 = 0
  max2 = 0
  nums.each do |n|
    if n > max1
      max2 = max1
      max1 = n
    elsif n > max2
      max2 = n
    end
  end
  (max1 - 1) * (max2 - 1)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        var max1 = 0
        var max2 = 0
        for (n <- nums) {
            if (n > max1) {
                max2 = max1
                max1 = n
            } else if (n > max2) {
                max2 = n
            }
        }
        (max1 - 1) * (max2 - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max1 = 0;
        let mut max2 = 0;
        for n in nums {
            if n > max1 {
                max2 = max1;
                max1 = n;
            } else if n > max2 {
                max2 = n;
            }
        }
        (max1 - 1) * (max2 - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-product nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ([ns nums] [m1 0] [m2 0])
    (if (null? ns)
        (* (- m1 1) (- m2 1))
        (let ([n (car ns)])
          (cond
            [(> n m1) (loop (cdr ns) n m1)]
            [(> n m2) (loop (cdr ns) m1 n)]
            [else (loop (cdr ns) m1 m2)])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_product(Nums :: [integer()]) -> integer().
max_product(Nums) ->
  find_maxes(Nums, 0, 0).

find_maxes([], M1, M2) ->
  (M1 - 1) * (M2 - 1);
find_maxes([H | T], M1, M2) ->
  if
    H > M1 -> find_maxes(T, H, M1);
    H > M2 -> find_maxes(T, M1, H);
    true -> find_maxes(T, M1, M2)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_product(nums :: [integer]) :: integer
  def max_product(nums) do
    {m1, m2} = Enum.reduce(nums, {0, 0}, fn n, {m1, m2} ->
      cond do
        n > m1 -> {n, m1}
        n > m2 -> {m1, n}
        true -> {m1, m2}
      end
    end)
    (m1 - 1) * (m2 - 1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. This is because we perform a single linear scan through the array to find the two largest elements, performing a constant number of comparisons at each step.
- **Space Complexity:** O(1) because we only utilize a fixed number of integer variables (max1 and max2) to store the top two elements, regardless of the input size.
