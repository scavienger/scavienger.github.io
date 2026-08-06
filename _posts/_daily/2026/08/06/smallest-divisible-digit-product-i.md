---
layout: post
title: "Smallest Divisible Digit Product I"
date: 2026-08-06 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Enumeration"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/smallest-divisible-digit-product-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int smallestNumber(int n, int t) {\n    \
        \    int curr = n;\n        while (true) {\n            int p = 1;\n       \
        \     int temp = curr;\n            while (temp > 0) {\n                p *=\
        \ (temp % 10);\n                temp /= 10;\n            }\n            if (p\
        \ % t == 0) return curr;\n            curr++;\n        }\n    }\n};"
      java: "class Solution {\n    public int smallestNumber(int n, int t) {\n     \
        \   int curr = n;\n        while (true) {\n            int p = 1;\n        \
        \    int temp = curr;\n            while (temp > 0) {\n                p *=\
        \ (temp % 10);\n                temp /= 10;\n            }\n            if (p\
        \ % t == 0) return curr;\n            curr++;\n        }\n    }\n}"
      python: "class Solution(object):\n    def smallestNumber(self, n, t):\n      \
        \  \"\"\"\n        :type n: int\n        :type t: int\n        :rtype: int\n\
        \        \"\"\"\n        curr = n\n        while True:\n            p = 1\n\
        \            for digit in str(curr):\n                p *= int(digit)\n    \
        \        if p % t == 0:\n                return curr\n            curr += 1"
      python3: "class Solution:\n    def smallestNumber(self, n: int, t: int) -> int:\n\
        \        curr = n\n        while True:\n            p = 1\n            for digit\
        \ in str(curr):\n                p *= int(digit)\n            if p % t == 0:\n\
        \                return curr\n            curr += 1"
      c: "int smallestNumber(int n, int t) {\n    int curr = n;\n    while (1) {\n \
        \       int p = 1;\n        int temp = curr;\n        while (temp > 0) {\n \
        \           p *= (temp % 10);\n            temp /= 10;\n        }\n        if\
        \ (p % t == 0) return curr;\n        curr++;\n    }\n}"
      csharp: "public class Solution {\n    public int SmallestNumber(int n, int t)\
        \ {\n        int curr = n;\n        while (true) {\n            int p = 1;\n\
        \            int temp = curr;\n            while (temp > 0) {\n            \
        \    p *= (temp % 10);\n                temp /= 10;\n            }\n       \
        \     if (p % t == 0) return curr;\n            curr++;\n        }\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number} t\n * @return {number}\n\
        \ */\nvar smallestNumber = function(n, t) {\n    let curr = n;\n    while (true)\
        \ {\n        let p = 1;\n        let temp = curr;\n        while (temp > 0)\
        \ {\n            p *= (temp % 10);\n            temp = Math.floor(temp / 10);\n\
        \        }\n        if (p % t === 0) return curr;\n        curr++;\n    }\n\
        };"
      typescript: "function smallestNumber(n: number, t: number): number {\n    let\
        \ curr = n;\n    while (true) {\n        let product = 1;\n        let temp\
        \ = curr;\n        if (temp === 0) {\n            product = 0;\n        } else\
        \ {\n            while (temp > 0) {\n                product *= (temp % 10);\n\
        \                temp = Math.floor(temp / 10);\n            }\n        }\n \
        \       if (product % t === 0) {\n            return curr;\n        }\n    \
        \    curr++;\n    }\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer\
        \ $t\n     * @return Integer\n     */\n    function smallestNumber($n, $t) {\n\
        \        $curr = $n;\n        while (true) {\n            $product = 1;\n  \
        \          $temp = $curr;\n            if ($temp == 0) {\n                $product\
        \ = 0;\n            } else {\n                while ($temp > 0) {\n        \
        \            $product *= ($temp % 10);\n                    $temp = intdiv($temp,\
        \ 10);\n                }\n            }\n            if ($product % $t == 0)\
        \ {\n                return $curr;\n            }\n            $curr++;\n  \
        \      }\n    }\n}"
      swift: "class Solution {\n    func smallestNumber(_ n: Int, _ t: Int) -> Int {\n\
        \        var curr = n\n        while true {\n            var product = 1\n \
        \           var temp = curr\n            if temp == 0 {\n                product\
        \ = 0\n            } else {\n                while temp > 0 {\n            \
        \        product *= (temp % 10)\n                    temp /= 10\n          \
        \      }\n            }\n            if product % t == 0 {\n               \
        \ return curr\n            }\n            curr += 1\n        }\n    }\n}"
      kotlin: "class Solution {\n    fun smallestNumber(n: Int, t: Int): Int {\n   \
        \     var curr = n\n        while (true) {\n            var product = 1\n  \
        \          var temp = curr\n            if (temp == 0) {\n                product\
        \ = 0\n            } else {\n                while (temp > 0) {\n          \
        \          product *= (temp % 10)\n                    temp /= 10\n        \
        \        }\n            }\n            if (product % t == 0) {\n           \
        \     return curr\n            }\n            curr++\n        }\n    }\n}"
      dart: "class Solution {\n  int smallestNumber(int n, int t) {\n    int curr =\
        \ n;\n    while (true) {\n      int product = 1;\n      int temp = curr;\n \
        \     if (temp == 0) {\n        product = 0;\n      } else {\n        while\
        \ (temp > 0) {\n          product *= (temp % 10);\n          temp ~/= 10;\n\
        \        }\n      }\n      if (product % t == 0) {\n        return curr;\n \
        \     }\n      curr++;\n    }\n  }\n}"
      go: "func smallestNumber(n int, t int) int {\n    curr := n\n    for {\n     \
        \   product := 1\n        temp := curr\n        if temp == 0 {\n           \
        \ product = 0\n        } else {\n            for temp > 0 {\n              \
        \  product *= (temp % 10)\n                temp /= 10\n            }\n     \
        \   }\n        if product%t == 0 {\n            return curr\n        }\n   \
        \     curr++\n    }\n}"
      ruby: "def smallest_number(n, t)\n  curr = n\n  loop do\n    p = 1\n    v = curr\n\
        \    if v == 0\n      p = 0\n    else\n      while v > 0\n        p *= (v %\
        \ 10)\n        v /= 10\n      end\n    end\n    return curr if p % t == 0\n\
        \    curr += 1\n  end\nend"
      scala: "object Solution {\n    def smallestNumber(n: Int, t: Int): Int = {\n \
        \       def getDigitProduct(num: Int): Int = {\n            if (num == 0) return\
        \ 0\n            var p = 1\n            var v = num\n            while (v >\
        \ 0) {\n                p *= (v % 10)\n                v /= 10\n           \
        \ }\n            p\n        }\n        var curr = n\n        while (getDigitProduct(curr)\
        \ % t != 0) {\n            curr += 1\n        }\n        curr\n    }\n}"
      rust: "impl Solution {\n    pub fn smallest_number(n: i32, t: i32) -> i32 {\n\
        \        let mut curr = n;\n        loop {\n            let mut p = 1;\n   \
        \         let mut v = curr;\n            if v == 0 {\n                p = 0;\n\
        \            } else {\n                while v > 0 {\n                    p\
        \ *= v % 10;\n                    v /= 10;\n                }\n            }\n\
        \            if p % t == 0 {\n                return curr;\n            }\n\
        \            curr += 1;\n        }\n    }\n}"
      racket: "(define/contract (smallest-number n t)\n  (-> exact-integer? exact-integer?\
        \ exact-integer?)\n  (define (digit-product num)\n    (if (= num 0) 0\n    \
        \    (let loop ([v num] [p 1])\n          (if (= v 0) p\n              (loop\
        \ (quotient v 10) (* p (remainder v 10)))))))\n  (let loop-n ([curr n])\n  \
        \  (if (= 0 (modulo (digit-product curr) t))\n        curr\n        (loop-n\
        \ (+ curr 1)))))"
      erlang: "-spec smallest_number(N :: integer(), T :: integer()) -> integer().\n\
        smallest_number(N, T) ->\n  case (digit_product(N) rem T) of\n    0 -> N;\n\
        \    _ -> smallest_number(N + 1, T)\n  end.\n\ndigit_product(0) -> 0;\ndigit_product(N)\
        \ -> digit_product_acc(N, 1).\n\ndigit_product_acc(0, Acc) -> Acc;\ndigit_product_acc(N,\
        \ Acc) -> digit_product_acc(N div 10, Acc * (N rem 10))."
      elixir: "defmodule Solution do\n  @spec smallest_number(n :: integer, t :: integer)\
        \ :: integer\n  def smallest_number(n, t) do\n    if rem(digit_product(n), t)\
        \ == 0 do\n      n\n    else\n      smallest_number(n + 1, t)\n    end\n  end\n\
        \n  defp digit_product(0), do: 0\n  defp digit_product(n), do: digit_product_acc(n,\
        \ 1)\n\n  defp digit_product_acc(0, acc), do: acc\n  defp digit_product_acc(n,\
        \ acc), do: digit_product_acc(div(n, 10), acc * rem(n, 10))\nend"
    approach: 'The algorithm employs a brute-force search starting from the integer
      n. Since we seek the smallest integer x >= n whose digit product is divisible
      by t, we iterate through integers starting from n, incrementing by one in each
      step. A key intuition, as suggested by the hints, is that the solution will be
      found very quickly; in any sequence of 10 consecutive integers, at least one ends
      in the digit 0, resulting in a digit product of 0, which is divisible by any t
      in the range [1, 10].


      For each candidate integer, we calculate the product of its digits by repeatedly
      extracting the last digit using the modulo operator and performing integer division
      to shift to the next digit. Once the digit product is determined, we check its
      divisibility by t using the modulo operator. The first integer that satisfies
      the condition product % t == 0 is returned as the result, ensuring we find the
      smallest possible value greater than or equal to n.'
    time_complexity: O(1). Although the complexity can be technically expressed as O(D)
      where D is the number of digits, the problem constraints cap n at 100 (meaning
      at most 3 digits) and guarantee a solution within 10 iterations. Thus, the total
      number of operations is constant and very small.
    space_complexity: O(1). The solution only requires a few integer variables to store
      the current candidate number, the running digit product, and temporary values
      during digit extraction, regardless of the input size.
    elapsed_time: 136.6537070274353
    model: gemini-3-flash-preview
    generated_at: '2026-08-06 01:53:39 '
---

## Problem #3345: Smallest Divisible Digit Product I

**Difficulty:** Easy

**Topics:** Math, Enumeration

## Problem Description

<p>You are given two integers <code>n</code> and <code>t</code>. Return the <strong>smallest</strong> number greater than or equal to <code>n</code> such that the <strong>product of its digits</strong> is divisible by <code>t</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10, t = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 15, t = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= t &lt;= 10</code></li>
</ul>


## Hints

1. You have to check at most 10 numbers.

2. Apply a brute-force approach by checking each possible number.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a brute-force search starting from the integer n. Since we seek the smallest integer x >= n whose digit product is divisible by t, we iterate through integers starting from n, incrementing by one in each step. A key intuition, as suggested by the hints, is that the solution will be found very quickly; in any sequence of 10 consecutive integers, at least one ends in the digit 0, resulting in a digit product of 0, which is divisible by any t in the range [1, 10].

For each candidate integer, we calculate the product of its digits by repeatedly extracting the last digit using the modulo operator and performing integer division to shift to the next digit. Once the digit product is determined, we check its divisibility by t using the modulo operator. The first integer that satisfies the condition product % t == 0 is returned as the result, ensuring we find the smallest possible value greater than or equal to n.

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
    int smallestNumber(int n, int t) {
        int curr = n;
        while (true) {
            int p = 1;
            int temp = curr;
            while (temp > 0) {
                p *= (temp % 10);
                temp /= 10;
            }
            if (p % t == 0) return curr;
            curr++;
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int smallestNumber(int n, int t) {
        int curr = n;
        while (true) {
            int p = 1;
            int temp = curr;
            while (temp > 0) {
                p *= (temp % 10);
                temp /= 10;
            }
            if (p % t == 0) return curr;
            curr++;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        curr = n
        while True:
            p = 1
            for digit in str(curr):
                p *= int(digit)
            if p % t == 0:
                return curr
            curr += 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        curr = n
        while True:
            p = 1
            for digit in str(curr):
                p *= int(digit)
            if p % t == 0:
                return curr
            curr += 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int smallestNumber(int n, int t) {
    int curr = n;
    while (1) {
        int p = 1;
        int temp = curr;
        while (temp > 0) {
            p *= (temp % 10);
            temp /= 10;
        }
        if (p % t == 0) return curr;
        curr++;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SmallestNumber(int n, int t) {
        int curr = n;
        while (true) {
            int p = 1;
            int temp = curr;
            while (temp > 0) {
                p *= (temp % 10);
                temp /= 10;
            }
            if (p % t == 0) return curr;
            curr++;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number} t
 * @return {number}
 */
var smallestNumber = function(n, t) {
    let curr = n;
    while (true) {
        let p = 1;
        let temp = curr;
        while (temp > 0) {
            p *= (temp % 10);
            temp = Math.floor(temp / 10);
        }
        if (p % t === 0) return curr;
        curr++;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function smallestNumber(n: number, t: number): number {
    let curr = n;
    while (true) {
        let product = 1;
        let temp = curr;
        if (temp === 0) {
            product = 0;
        } else {
            while (temp > 0) {
                product *= (temp % 10);
                temp = Math.floor(temp / 10);
            }
        }
        if (product % t === 0) {
            return curr;
        }
        curr++;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer $t
     * @return Integer
     */
    function smallestNumber($n, $t) {
        $curr = $n;
        while (true) {
            $product = 1;
            $temp = $curr;
            if ($temp == 0) {
                $product = 0;
            } else {
                while ($temp > 0) {
                    $product *= ($temp % 10);
                    $temp = intdiv($temp, 10);
                }
            }
            if ($product % $t == 0) {
                return $curr;
            }
            $curr++;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func smallestNumber(_ n: Int, _ t: Int) -> Int {
        var curr = n
        while true {
            var product = 1
            var temp = curr
            if temp == 0 {
                product = 0
            } else {
                while temp > 0 {
                    product *= (temp % 10)
                    temp /= 10
                }
            }
            if product % t == 0 {
                return curr
            }
            curr += 1
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
    fun smallestNumber(n: Int, t: Int): Int {
        var curr = n
        while (true) {
            var product = 1
            var temp = curr
            if (temp == 0) {
                product = 0
            } else {
                while (temp > 0) {
                    product *= (temp % 10)
                    temp /= 10
                }
            }
            if (product % t == 0) {
                return curr
            }
            curr++
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int smallestNumber(int n, int t) {
    int curr = n;
    while (true) {
      int product = 1;
      int temp = curr;
      if (temp == 0) {
        product = 0;
      } else {
        while (temp > 0) {
          product *= (temp % 10);
          temp ~/= 10;
        }
      }
      if (product % t == 0) {
        return curr;
      }
      curr++;
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func smallestNumber(n int, t int) int {
    curr := n
    for {
        product := 1
        temp := curr
        if temp == 0 {
            product = 0
        } else {
            for temp > 0 {
                product *= (temp % 10)
                temp /= 10
            }
        }
        if product%t == 0 {
            return curr
        }
        curr++
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def smallest_number(n, t)
  curr = n
  loop do
    p = 1
    v = curr
    if v == 0
      p = 0
    else
      while v > 0
        p *= (v % 10)
        v /= 10
      end
    end
    return curr if p % t == 0
    curr += 1
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def smallestNumber(n: Int, t: Int): Int = {
        def getDigitProduct(num: Int): Int = {
            if (num == 0) return 0
            var p = 1
            var v = num
            while (v > 0) {
                p *= (v % 10)
                v /= 10
            }
            p
        }
        var curr = n
        while (getDigitProduct(curr) % t != 0) {
            curr += 1
        }
        curr
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn smallest_number(n: i32, t: i32) -> i32 {
        let mut curr = n;
        loop {
            let mut p = 1;
            let mut v = curr;
            if v == 0 {
                p = 0;
            } else {
                while v > 0 {
                    p *= v % 10;
                    v /= 10;
                }
            }
            if p % t == 0 {
                return curr;
            }
            curr += 1;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-number n t)
  (-> exact-integer? exact-integer? exact-integer?)
  (define (digit-product num)
    (if (= num 0) 0
        (let loop ([v num] [p 1])
          (if (= v 0) p
              (loop (quotient v 10) (* p (remainder v 10)))))))
  (let loop-n ([curr n])
    (if (= 0 (modulo (digit-product curr) t))
        curr
        (loop-n (+ curr 1)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_number(N :: integer(), T :: integer()) -> integer().
smallest_number(N, T) ->
  case (digit_product(N) rem T) of
    0 -> N;
    _ -> smallest_number(N + 1, T)
  end.

digit_product(0) -> 0;
digit_product(N) -> digit_product_acc(N, 1).

digit_product_acc(0, Acc) -> Acc;
digit_product_acc(N, Acc) -> digit_product_acc(N div 10, Acc * (N rem 10)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_number(n :: integer, t :: integer) :: integer
  def smallest_number(n, t) do
    if rem(digit_product(n), t) == 0 do
      n
    else
      smallest_number(n + 1, t)
    end
  end

  defp digit_product(0), do: 0
  defp digit_product(n), do: digit_product_acc(n, 1)

  defp digit_product_acc(0, acc), do: acc
  defp digit_product_acc(n, acc), do: digit_product_acc(div(n, 10), acc * rem(n, 10))
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). Although the complexity can be technically expressed as O(D) where D is the number of digits, the problem constraints cap n at 100 (meaning at most 3 digits) and guarantee a solution within 10 iterations. Thus, the total number of operations is constant and very small.
- **Space Complexity:** O(1). The solution only requires a few integer variables to store the current candidate number, the running digit product, and temporary values during digit extraction, regardless of the input size.
