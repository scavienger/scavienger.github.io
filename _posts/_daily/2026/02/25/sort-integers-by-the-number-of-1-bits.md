---
layout: post
title: "Sort Integers by The Number of 1 Bits"
date: 2026-02-25 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Bit Manipulation", "Sorting", "Counting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> sortByBits(vector<int>& arr)\
        \ {\n        sort(arr.begin(), arr.end(), [](int a, int b) {\n            int\
        \ countA = __builtin_popcount(a);\n            int countB = __builtin_popcount(b);\n\
        \            if (countA != countB) return countA < countB;\n            return\
        \ a < b;\n        });\n        return arr;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int[] sortByBits(int[]\
        \ arr) {\n        Integer[] boxed = new Integer[arr.length];\n        for (int\
        \ i = 0; i < arr.length; i++) boxed[i] = arr[i];\n\n        Arrays.sort(boxed,\
        \ (a, b) -> {\n            int ca = Integer.bitCount(a);\n            int cb\
        \ = Integer.bitCount(b);\n            if (ca != cb) return ca - cb;\n      \
        \      return a - b;\n        });\n\n        for (int i = 0; i < arr.length;\
        \ i++) arr[i] = boxed[i];\n        return arr;\n    }\n}"
      python: "class Solution(object):\n    def sortByBits(self, arr):\n        \"\"\
        \"\n        :type arr: List[int]\n        :rtype: List[int]\n        \"\"\"\n\
        \        def get_bits(n):\n            count = 0\n            while n > 0:\n\
        \                n &= (n - 1)\n                count += 1\n            return\
        \ count\n\n        arr.sort(key=lambda x: (get_bits(x), x))\n        return\
        \ arr"
      python3: "class Solution:\n    def sortByBits(self, arr: List[int]) -> List[int]:\n\
        \        # Python 3.10+ provides int.bit_count()\n        # For compatibility,\
        \ bin(x).count('1') is used\n        arr.sort(key=lambda x: (bin(x).count('1'),\
        \ x))\n        return arr"
      c: "int countBits(int n) {\n    int count = 0;\n    while (n > 0) {\n        n\
        \ &= (n - 1);\n        count++;\n    }\n    return count;\n}\n\nint compare(const\
        \ void* a, const void* b) {\n    int x = *(int*)a;\n    int y = *(int*)b;\n\
        \    int cx = countBits(x);\n    int cy = countBits(y);\n    if (cx != cy) return\
        \ cx - cy;\n    return x - y;\n}\n\nint* sortByBits(int* arr, int arrSize, int*\
        \ returnSize) {\n    *returnSize = arrSize;\n    int* result = (int*)malloc(arrSize\
        \ * sizeof(int));\n    for (int i = 0; i < arrSize; i++) result[i] = arr[i];\n\
        \    qsort(result, arrSize, sizeof(int), compare);\n    return result;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int[] SortByBits(int[]\
        \ arr) {\n        Array.Sort(arr, (a, b) => {\n            int ca = BitCount(a);\n\
        \            int cb = BitCount(b);\n            if (ca != cb) return ca.CompareTo(cb);\n\
        \            return a.CompareTo(b);\n        });\n        return arr;\n    }\n\
        \n    private int BitCount(int n) {\n        int count = 0;\n        while (n\
        \ > 0) {\n            n &= (n - 1);\n            count++;\n        }\n     \
        \   return count;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @return {number[]}\n */\nvar sortByBits\
        \ = function(arr) {\n    const getBits = (n) => {\n        let count = 0;\n\
        \        while (n > 0) {\n            n &= (n - 1);\n            count++;\n\
        \        }\n        return count;\n    };\n\n    return arr.sort((a, b) => {\n\
        \        const ca = getBits(a);\n        const cb = getBits(b);\n        return\
        \ ca === cb ? a - b : ca - cb;\n    });\n};"
      typescript: "function sortByBits(arr: number[]): number[] {\n    const countBits\
        \ = (n: number): number => {\n        let count = 0;\n        while (n > 0)\
        \ {\n            n &= (n - 1);\n            count++;\n        }\n        return\
        \ count;\n    };\n    return arr.sort((a, b) => {\n        const cntA = countBits(a);\n\
        \        const cntB = countBits(b);\n        if (cntA !== cntB) {\n        \
        \    return cntA - cntB;\n        }\n        return a - b;\n    });\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @return\
        \ Integer[]\n     */\n    function sortByBits($arr) {\n        usort($arr, function($a,\
        \ $b) {\n            $cntA = substr_count(decbin($a), '1');\n            $cntB\
        \ = substr_count(decbin($b), '1');\n            if ($cntA == $cntB) {\n    \
        \            return $a - $b;\n            }\n            return $cntA - $cntB;\n\
        \        });\n        return $arr;\n    }\n}"
      swift: "class Solution {\n    func sortByBits(_ arr: [Int]) -> [Int] {\n     \
        \   return arr.sorted { a, b in\n            let countA = a.nonzeroBitCount\n\
        \            let countB = b.nonzeroBitCount\n            if countA == countB\
        \ {\n                return a < b\n            }\n            return countA\
        \ < countB\n        }\n    }\n}"
      kotlin: "class Solution {\n    fun sortByBits(arr: IntArray): IntArray {\n   \
        \     val result = arr.toTypedArray()\n        result.sortWith(Comparator {\
        \ a, b ->\n            val cntA = Integer.bitCount(a)\n            val cntB\
        \ = Integer.bitCount(b)\n            if (cntA != cntB) {\n                cntA\
        \ - cntB\n            } else {\n                a - b\n            }\n     \
        \   })\n        return result.toIntArray()\n    }\n}"
      dart: "class Solution {\n  List<int> sortByBits(List<int> arr) {\n    int countBits(int\
        \ n) {\n      int count = 0;\n      while (n > 0) {\n        n &= (n - 1);\n\
        \        count++;\n      }\n      return count;\n    }\n    arr.sort((a, b)\
        \ {\n      int cntA = countBits(a);\n      int cntB = countBits(b);\n      if\
        \ (cntA != cntB) {\n        return cntA.compareTo(cntB);\n      }\n      return\
        \ a.compareTo(b);\n    });\n    return arr;\n  }\n}"
      go: "import (\n    \"math/bits\"\n    \"sort\"\n)\n\nfunc sortByBits(arr []int)\
        \ []int {\n    sort.Slice(arr, func(i, j int) bool {\n        cntI := bits.OnesCount(uint(arr[i]))\n\
        \        cntJ := bits.OnesCount(uint(arr[j]))\n        if cntI != cntJ {\n \
        \           return cntI < cntJ\n        }\n        return arr[i] < arr[j]\n\
        \    })\n    return arr\n}"
      ruby: "# @param {Integer[]} arr\n# @return {Integer[]}\ndef sort_by_bits(arr)\n\
        \  arr.sort_by { |x| [x.to_s(2).count('1'), x] }\nend"
      scala: "object Solution {\n    def sortByBits(arr: Array[Int]): Array[Int] = {\n\
        \        arr.sortBy(x => (java.lang.Integer.bitCount(x), x))\n    }\n}"
      rust: "impl Solution {\n    pub fn sort_by_bits(arr: Vec<i32>) -> Vec<i32> {\n\
        \        let mut arr = arr;\n        arr.sort_by_key(|&x| (x.count_ones(), x));\n\
        \        arr\n    }\n}"
      racket: "(define/contract (sort-by-bits arr)\n  (-> (listof exact-integer?) (listof\
        \ exact-integer?))\n  (sort arr (lambda (a b)\n              (let ([ca (bitwise-bit-count\
        \ a)]\n                    [cb (bitwise-bit-count b)])\n                (if\
        \ (= ca cb)\n                    (< a b)\n                    (< ca cb))))))"
      erlang: "-spec sort_by_bits(Arr :: [integer()]) -> [integer()].\nsort_by_bits(Arr)\
        \ ->\n  BC = fun Count(0, Acc) -> Acc;\n           Count(N, Acc) -> Count(N\
        \ div 2, Acc + (N rem 2))\n       end,\n  lists:sort(fun(A, B) ->\n    CA =\
        \ BC(A, 0),\n    CB = BC(B, 0),\n    if CA < CB -> true; CA == CB -> A =< B;\
        \ true -> false end\n  end, Arr)."
      elixir: "defmodule Solution do\n  @spec sort_by_bits(arr :: [integer]) :: [integer]\n\
        \  def sort_by_bits(arr) do\n    Enum.sort_by(arr, fn x -> {Integer.digits(x,\
        \ 2) |> Enum.sum(), x} end)\n  end\nend"
    approach: 'The core of the problem involves sorting elements based on two criteria:
      the number of set bits (binary 1s) and the numerical value itself. To achieve
      this, we define a custom comparator that calculates the Hamming weight (the number
      of 1s in the binary representation) for each integer. If two integers have different
      bit counts, the one with the smaller bit count is prioritized. If their bit counts
      are identical, the integers are compared based on their actual numerical values
      in ascending order.


      Technically, bit counting can be done using built-in library functions like `__builtin_popcount`
      in C++, `Integer.bitCount` in Java, or `int.bit_count()` in newer Python versions.
      For languages without a direct built-in, we use Brian Kernighan''s algorithm ($n
      \&= n - 1$) or a simple bit-shift loop. Since the input array size and integer
      values are small, sorting with these criteria ensures we maintain stability and
      efficiency using the standard libraries'' sorting routines.'
    time_complexity: O(N log N * log M), where N is the number of elements in the array
      and M is the maximum value in the array. The O(N log N) factor comes from the
      sorting algorithm, while the O(log M) factor arises from counting bits in each
      comparison (though bit counting is effectively O(1) for fixed-width integers).
    space_complexity: O(N) in some languages due to creating boxed objects or auxiliary
      arrays for sorting (like in Java or Python), or O(log N) for the recursion stack
      of the sorting algorithm in languages like C or C++.
    elapsed_time: 861.0179750919342
    model: gemini-3-flash-preview
    generated_at: '2026-02-25 01:40:53 '
---

## Problem #1356: Sort Integers by The Number of 1 Bits

**Difficulty:** Easy

**Topics:** Array, Bit Manipulation, Sorting, Counting

## Problem Description

<p>You are given an integer array <code>arr</code>. Sort the integers in the array&nbsp;in ascending order by the number of <code>1</code>&#39;s&nbsp;in their binary representation and in case of two or more integers have the same number of <code>1</code>&#39;s you have to sort them in ascending order.</p>

<p>Return <em>the array after sorting it</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [0,1,2,3,4,5,6,7,8]
<strong>Output:</strong> [0,1,2,4,8,3,5,6,7]
<strong>Explantion:</strong> [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1024,512,256,128,64,32,16,8,4,2,1]
<strong>Output:</strong> [1,2,4,8,16,32,64,128,256,512,1024]
<strong>Explantion:</strong> All integers have 1 bit in the binary representation, you should just sort them in ascending order.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Simulate the problem. Count the number of 1's in the binary representation of each integer.

2. Sort by the number of 1's ascending and by the value in case of tie.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core of the problem involves sorting elements based on two criteria: the number of set bits (binary 1s) and the numerical value itself. To achieve this, we define a custom comparator that calculates the Hamming weight (the number of 1s in the binary representation) for each integer. If two integers have different bit counts, the one with the smaller bit count is prioritized. If their bit counts are identical, the integers are compared based on their actual numerical values in ascending order.

Technically, bit counting can be done using built-in library functions like `__builtin_popcount` in C++, `Integer.bitCount` in Java, or `int.bit_count()` in newer Python versions. For languages without a direct built-in, we use Brian Kernighan's algorithm ($n \&= n - 1$) or a simple bit-shift loop. Since the input array size and integer values are small, sorting with these criteria ensures we maintain stability and efficiency using the standard libraries' sorting routines.

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
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), [](int a, int b) {
            int countA = __builtin_popcount(a);
            int countB = __builtin_popcount(b);
            if (countA != countB) return countA < countB;
            return a < b;
        });
        return arr;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public int[] sortByBits(int[] arr) {
        Integer[] boxed = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) boxed[i] = arr[i];

        Arrays.sort(boxed, (a, b) -> {
            int ca = Integer.bitCount(a);
            int cb = Integer.bitCount(b);
            if (ca != cb) return ca - cb;
            return a - b;
        });

        for (int i = 0; i < arr.length; i++) arr[i] = boxed[i];
        return arr;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def get_bits(n):
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count

        arr.sort(key=lambda x: (get_bits(x), x))
        return arr
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Python 3.10+ provides int.bit_count()
        # For compatibility, bin(x).count('1') is used
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        return arr
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countBits(int n) {
    int count = 0;
    while (n > 0) {
        n &= (n - 1);
        count++;
    }
    return count;
}

int compare(const void* a, const void* b) {
    int x = *(int*)a;
    int y = *(int*)b;
    int cx = countBits(x);
    int cy = countBits(y);
    if (cx != cy) return cx - cy;
    return x - y;
}

int* sortByBits(int* arr, int arrSize, int* returnSize) {
    *returnSize = arrSize;
    int* result = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) result[i] = arr[i];
    qsort(result, arrSize, sizeof(int), compare);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int[] SortByBits(int[] arr) {
        Array.Sort(arr, (a, b) => {
            int ca = BitCount(a);
            int cb = BitCount(b);
            if (ca != cb) return ca.CompareTo(cb);
            return a.CompareTo(b);
        });
        return arr;
    }

    private int BitCount(int n) {
        int count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    const getBits = (n) => {
        let count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    };

    return arr.sort((a, b) => {
        const ca = getBits(a);
        const cb = getBits(b);
        return ca === cb ? a - b : ca - cb;
    });
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sortByBits(arr: number[]): number[] {
    const countBits = (n: number): number => {
        let count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    };
    return arr.sort((a, b) => {
        const cntA = countBits(a);
        const cntB = countBits(b);
        if (cntA !== cntB) {
            return cntA - cntB;
        }
        return a - b;
    });
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function sortByBits($arr) {
        usort($arr, function($a, $b) {
            $cntA = substr_count(decbin($a), '1');
            $cntB = substr_count(decbin($b), '1');
            if ($cntA == $cntB) {
                return $a - $b;
            }
            return $cntA - $cntB;
        });
        return $arr;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sortByBits(_ arr: [Int]) -> [Int] {
        return arr.sorted { a, b in
            let countA = a.nonzeroBitCount
            let countB = b.nonzeroBitCount
            if countA == countB {
                return a < b
            }
            return countA < countB
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sortByBits(arr: IntArray): IntArray {
        val result = arr.toTypedArray()
        result.sortWith(Comparator { a, b ->
            val cntA = Integer.bitCount(a)
            val cntB = Integer.bitCount(b)
            if (cntA != cntB) {
                cntA - cntB
            } else {
                a - b
            }
        })
        return result.toIntArray()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> sortByBits(List<int> arr) {
    int countBits(int n) {
      int count = 0;
      while (n > 0) {
        n &= (n - 1);
        count++;
      }
      return count;
    }
    arr.sort((a, b) {
      int cntA = countBits(a);
      int cntB = countBits(b);
      if (cntA != cntB) {
        return cntA.compareTo(cntB);
      }
      return a.compareTo(b);
    });
    return arr;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
    "math/bits"
    "sort"
)

func sortByBits(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        cntI := bits.OnesCount(uint(arr[i]))
        cntJ := bits.OnesCount(uint(arr[j]))
        if cntI != cntJ {
            return cntI < cntJ
        }
        return arr[i] < arr[j]
    })
    return arr
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} arr
# @return {Integer[]}
def sort_by_bits(arr)
  arr.sort_by { |x| [x.to_s(2).count('1'), x] }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sortByBits(arr: Array[Int]): Array[Int] = {
        arr.sortBy(x => (java.lang.Integer.bitCount(x), x))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sort_by_bits(arr: Vec<i32>) -> Vec<i32> {
        let mut arr = arr;
        arr.sort_by_key(|&x| (x.count_ones(), x));
        arr
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sort-by-bits arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (sort arr (lambda (a b)
              (let ([ca (bitwise-bit-count a)]
                    [cb (bitwise-bit-count b)])
                (if (= ca cb)
                    (< a b)
                    (< ca cb))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sort_by_bits(Arr :: [integer()]) -> [integer()].
sort_by_bits(Arr) ->
  BC = fun Count(0, Acc) -> Acc;
           Count(N, Acc) -> Count(N div 2, Acc + (N rem 2))
       end,
  lists:sort(fun(A, B) ->
    CA = BC(A, 0),
    CB = BC(B, 0),
    if CA < CB -> true; CA == CB -> A =< B; true -> false end
  end, Arr).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sort_by_bits(arr :: [integer]) :: [integer]
  def sort_by_bits(arr) do
    Enum.sort_by(arr, fn x -> {Integer.digits(x, 2) |> Enum.sum(), x} end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N * log M), where N is the number of elements in the array and M is the maximum value in the array. The O(N log N) factor comes from the sorting algorithm, while the O(log M) factor arises from counting bits in each comparison (though bit counting is effectively O(1) for fixed-width integers).
- **Space Complexity:** O(N) in some languages due to creating boxed objects or auxiliary arrays for sorting (like in Java or Python), or O(log N) for the recursion stack of the sorting algorithm in languages like C or C++.
