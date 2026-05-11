---
layout: post
title: "Separate the Digits in an Array"
date: 2026-05-11 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/separate-the-digits-in-an-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> separateDigits(vector<int>& nums)\
        \ {\n        vector<int> answer;\n        for (int n : nums) {\n           \
        \ string s = to_string(n);\n            for (char c : s) {\n               \
        \ answer.push_back(c - '0');\n            }\n        }\n        return answer;\n\
        \    }\n};"
      java: "class Solution {\n    public int[] separateDigits(int[] nums) {\n     \
        \   java.util.List<Integer> list = new java.util.ArrayList<>();\n        for\
        \ (int n : nums) {\n            String s = Integer.toString(n);\n          \
        \  for (char c : s.toCharArray()) {\n                list.add(c - '0');\n  \
        \          }\n        }\n        int[] result = new int[list.size()];\n    \
        \    for (int i = 0; i < list.size(); i++) {\n            result[i] = list.get(i);\n\
        \        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def separateDigits(self, nums):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :rtype: List[int]\n      \
        \  \"\"\"\n        answer = []\n        for n in nums:\n            for digit\
        \ in str(n):\n                answer.append(int(digit))\n        return answer"
      python3: "class Solution:\n    def separateDigits(self, nums: List[int]) -> List[int]:\n\
        \        answer = []\n        for n in nums:\n            for digit in str(n):\n\
        \                answer.append(int(digit))\n        return answer"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* separateDigits(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ temp = (int*)malloc(sizeof(int) * numsSize * 6);\n    int count = 0;\n   \
        \ for (int i = 0; i < numsSize; i++) {\n        int val = nums[i];\n       \
        \ int digits[10];\n        int d_count = 0;\n        while (val > 0) {\n   \
        \         digits[d_count++] = val % 10;\n            val /= 10;\n        }\n\
        \        for (int j = d_count - 1; j >= 0; j--) {\n            temp[count++]\
        \ = digits[j];\n        }\n    }\n    *returnSize = count;\n    int* result\
        \ = (int*)malloc(sizeof(int) * count);\n    for (int i = 0; i < count; i++)\
        \ {\n        result[i] = temp[i];\n    }\n    free(temp);\n    return result;\n\
        }"
      csharp: "public class Solution {\n    public int[] SeparateDigits(int[] nums)\
        \ {\n        System.Collections.Generic.List<int> result = new System.Collections.Generic.List<int>();\n\
        \        foreach (int n in nums) {\n            string s = n.ToString();\n \
        \           foreach (char c in s) {\n                result.Add(c - '0');\n\
        \            }\n        }\n        return result.ToArray();\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar separateDigits\
        \ = function(nums) {\n    const answer = [];\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        const s = nums[i].toString();\n        for (let j = 0; j <\
        \ s.length; j++) {\n            answer.push(parseInt(s[j]));\n        }\n  \
        \  }\n    return answer;\n};"
      typescript: "function separateDigits(nums: number[]): number[] {\n    const answer:\
        \ number[] = [];\n    for (const num of nums) {\n        const s = num.toString();\n\
        \        for (let i = 0; i < s.length; i++) {\n            answer.push(parseInt(s[i]));\n\
        \        }\n    }\n    return answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function separateDigits($nums) {\n        $answer\
        \ = [];\n        foreach ($nums as $num) {\n            $s = (string)$num;\n\
        \            $len = strlen($s);\n            for ($i = 0; $i < $len; $i++) {\n\
        \                $answer[] = (int)$s[$i];\n            }\n        }\n      \
        \  return $answer;\n    }\n}"
      swift: "class Solution {\n    func separateDigits(_ nums: [Int]) -> [Int] {\n\
        \        var answer = [Int]()\n        for num in nums {\n            let s\
        \ = String(num)\n            for char in s {\n                if let digit =\
        \ Int(String(char)) {\n                    answer.append(digit)\n          \
        \      }\n            }\n        }\n        return answer\n    }\n}"
      kotlin: "class Solution {\n    fun separateDigits(nums: IntArray): IntArray {\n\
        \        val answer = mutableListOf<Int>()\n        for (num in nums) {\n  \
        \          val s = num.toString()\n            for (char in s) {\n         \
        \       answer.add(char.digitToInt())\n            }\n        }\n        return\
        \ answer.toIntArray()\n    }\n}"
      dart: "class Solution {\n  List<int> separateDigits(List<int> nums) {\n    List<int>\
        \ answer = [];\n    for (var num in nums) {\n      String s = num.toString();\n\
        \      for (var i = 0; i < s.length; i++) {\n        answer.add(int.parse(s[i]));\n\
        \      }\n    }\n    return answer;\n  }\n}"
      go: "func separateDigits(nums []int) []int {\n    answer := make([]int, 0)\n \
        \   for _, num := range nums {\n        tempDigits := make([]int, 0)\n     \
        \   t := num\n        for t > 0 {\n            tempDigits = append(tempDigits,\
        \ t % 10)\n            t /= 10\n        }\n        for i := len(tempDigits)\
        \ - 1; i >= 0; i-- {\n            answer = append(answer, tempDigits[i])\n \
        \       }\n    }\n    return answer\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef separate_digits(nums)\n\
        \  nums.flat_map do |n|\n    n.to_s.chars.map(&:to_i)\n  end\nend"
      scala: "object Solution {\n    def separateDigits(nums: Array[Int]): Array[Int]\
        \ = {\n        nums.flatMap(n => n.toString.map(_.asDigit))\n    }\n}"
      rust: "impl Solution {\n    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        nums.into_iter()\n            .flat_map(|n| {\n               \
        \ n.to_string()\n                    .chars()\n                    .map(|c|\
        \ c.to_digit(10).unwrap() as i32)\n                    .collect::<Vec<i32>>()\n\
        \            })\n            .collect()\n    }\n}"
      racket: "(define/contract (separate-digits nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (apply append (map (lambda (n)\n             \
        \          (map (lambda (c)\n                              (- (char->integer\
        \ c) (char->integer #\\0)))\n                            (string->list (number->string\
        \ n))))\n                     nums))\n  )"
      erlang: "-spec separate_digits(Nums :: [integer()]) -> [integer()].\nseparate_digits(Nums)\
        \ ->\n  lists:flatmap(fun(N) -> [C - $0 || C <- integer_to_list(N)] end, Nums)."
      elixir: "defmodule Solution do\n  @spec separate_digits(nums :: [integer]) ::\
        \ [integer]\n  def separate_digits(nums) do\n    Enum.flat_map(nums, fn n ->\n\
        \      Integer.digits(n)\n    end)\n  end\nend"
    approach: 'The core objective is to decompose each integer in the input array into
      its constituent digits while preserving the relative order of both the integers
      and their digits. The most straightforward strategy involves iterating through
      each number in the input list and converting it into a format that allows sequential
      access to its digits from left to right. This can be achieved by converting each
      integer to its string representation and then iterating through the characters
      of that string, or by repeatedly applying modulo and division operations to extract
      digits and then reversing them.


      After extracting the digits for a specific integer, they are appended to a dynamic
      result container. By processing integers in the order they appear in the input
      and processing their digits from the most significant bit to the least significant
      bit, the final result array naturally maintains the required global order. Once
      all numbers have been processed, the container is returned as an array or list
      as specified by the language requirements.'
    time_complexity: O(N * D) where N is the number of elements in the input array and
      D is the maximum number of digits per element. Since each integer is at most 10^5,
      D is at most 6, making the complexity effectively linear with respect to the total
      number of digits processed across all input integers.
    space_complexity: O(N * D) to store the final result array. If excluding the output
      space, the auxiliary space complexity is O(D) for temporary string storage or
      digit buffering during the decomposition of an individual integer.
    elapsed_time: 87.20424437522888
    model: gemini-3-flash-preview
    generated_at: '2026-05-11 02:31:04 '
---

## Problem #2553: Separate the Digits in an Array

**Difficulty:** Easy

**Topics:** Array, Simulation

## Problem Description

<p>Given an array of positive integers <code>nums</code>, return <em>an array </em><code>answer</code><em> that consists of the digits of each integer in </em><code>nums</code><em> after separating them in <strong>the same order</strong> they appear in </em><code>nums</code>.</p>

<p>To separate the digits of an integer is to get all the digits it has in the same order.</p>

<ul>
	<li>For example, for the integer <code>10921</code>, the separation of its digits is <code>[1,0,9,2,1]</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [13,25,83,77]
<strong>Output:</strong> [1,3,2,5,8,3,7,7]
<strong>Explanation:</strong> 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,1,3,9]
<strong>Output:</strong> [7,1,3,9]
<strong>Explanation:</strong> The separation of each integer in nums is itself.
answer = [7,1,3,9].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Convert each number into a list and append that list to the answer.

2. You can convert the integer into a string to do that easily.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core objective is to decompose each integer in the input array into its constituent digits while preserving the relative order of both the integers and their digits. The most straightforward strategy involves iterating through each number in the input list and converting it into a format that allows sequential access to its digits from left to right. This can be achieved by converting each integer to its string representation and then iterating through the characters of that string, or by repeatedly applying modulo and division operations to extract digits and then reversing them.

After extracting the digits for a specific integer, they are appended to a dynamic result container. By processing integers in the order they appear in the input and processing their digits from the most significant bit to the least significant bit, the final result array naturally maintains the required global order. Once all numbers have been processed, the container is returned as an array or list as specified by the language requirements.

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
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> answer;
        for (int n : nums) {
            string s = to_string(n);
            for (char c : s) {
                answer.push_back(c - '0');
            }
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
class Solution {
    public int[] separateDigits(int[] nums) {
        java.util.List<Integer> list = new java.util.ArrayList<>();
        for (int n : nums) {
            String s = Integer.toString(n);
            for (char c : s.toCharArray()) {
                list.add(c - '0');
            }
        }
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
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
class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for n in nums:
            for digit in str(n):
                answer.append(int(digit))
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for n in nums:
            for digit in str(n):
                answer.append(int(digit))
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* separateDigits(int* nums, int numsSize, int* returnSize) {
    int* temp = (int*)malloc(sizeof(int) * numsSize * 6);
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        int val = nums[i];
        int digits[10];
        int d_count = 0;
        while (val > 0) {
            digits[d_count++] = val % 10;
            val /= 10;
        }
        for (int j = d_count - 1; j >= 0; j--) {
            temp[count++] = digits[j];
        }
    }
    *returnSize = count;
    int* result = (int*)malloc(sizeof(int) * count);
    for (int i = 0; i < count; i++) {
        result[i] = temp[i];
    }
    free(temp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] SeparateDigits(int[] nums) {
        System.Collections.Generic.List<int> result = new System.Collections.Generic.List<int>();
        foreach (int n in nums) {
            string s = n.ToString();
            foreach (char c in s) {
                result.Add(c - '0');
            }
        }
        return result.ToArray();
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
 * @return {number[]}
 */
var separateDigits = function(nums) {
    const answer = [];
    for (let i = 0; i < nums.length; i++) {
        const s = nums[i].toString();
        for (let j = 0; j < s.length; j++) {
            answer.push(parseInt(s[j]));
        }
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function separateDigits(nums: number[]): number[] {
    const answer: number[] = [];
    for (const num of nums) {
        const s = num.toString();
        for (let i = 0; i < s.length; i++) {
            answer.push(parseInt(s[i]));
        }
    }
    return answer;
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
     * @return Integer[]
     */
    function separateDigits($nums) {
        $answer = [];
        foreach ($nums as $num) {
            $s = (string)$num;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $answer[] = (int)$s[$i];
            }
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
    func separateDigits(_ nums: [Int]) -> [Int] {
        var answer = [Int]()
        for num in nums {
            let s = String(num)
            for char in s {
                if let digit = Int(String(char)) {
                    answer.append(digit)
                }
            }
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
    fun separateDigits(nums: IntArray): IntArray {
        val answer = mutableListOf<Int>()
        for (num in nums) {
            val s = num.toString()
            for (char in s) {
                answer.add(char.digitToInt())
            }
        }
        return answer.toIntArray()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> separateDigits(List<int> nums) {
    List<int> answer = [];
    for (var num in nums) {
      String s = num.toString();
      for (var i = 0; i < s.length; i++) {
        answer.add(int.parse(s[i]));
      }
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
func separateDigits(nums []int) []int {
    answer := make([]int, 0)
    for _, num := range nums {
        tempDigits := make([]int, 0)
        t := num
        for t > 0 {
            tempDigits = append(tempDigits, t % 10)
            t /= 10
        }
        for i := len(tempDigits) - 1; i >= 0; i-- {
            answer = append(answer, tempDigits[i])
        }
    }
    return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer[]}
def separate_digits(nums)
  nums.flat_map do |n|
    n.to_s.chars.map(&:to_i)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def separateDigits(nums: Array[Int]): Array[Int] = {
        nums.flatMap(n => n.toString.map(_.asDigit))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
        nums.into_iter()
            .flat_map(|n| {
                n.to_string()
                    .chars()
                    .map(|c| c.to_digit(10).unwrap() as i32)
                    .collect::<Vec<i32>>()
            })
            .collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (separate-digits nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (apply append (map (lambda (n)
                       (map (lambda (c)
                              (- (char->integer c) (char->integer #\0)))
                            (string->list (number->string n))))
                     nums))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec separate_digits(Nums :: [integer()]) -> [integer()].
separate_digits(Nums) ->
  lists:flatmap(fun(N) -> [C - $0 || C <- integer_to_list(N)] end, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec separate_digits(nums :: [integer]) :: [integer]
  def separate_digits(nums) do
    Enum.flat_map(nums, fn n ->
      Integer.digits(n)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * D) where N is the number of elements in the input array and D is the maximum number of digits per element. Since each integer is at most 10^5, D is at most 6, making the complexity effectively linear with respect to the total number of digits processed across all input integers.
- **Space Complexity:** O(N * D) to store the final result array. If excluding the output space, the auxiliary space complexity is O(D) for temporary string storage or digit buffering during the decomposition of an individual integer.
