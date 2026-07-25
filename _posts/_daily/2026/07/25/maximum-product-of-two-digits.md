---
layout: post
title: "Maximum Product of Two Digits"
date: 2026-07-25 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-product-of-two-digits/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProduct(int n) {\n        int max1\
        \ = 0, max2 = 0;\n        while (n > 0) {\n            int d = n % 10;\n   \
        \         if (d >= max1) {\n                max2 = max1;\n                max1\
        \ = d;\n            } else if (d > max2) {\n                max2 = d;\n    \
        \        }\n            n /= 10;\n        }\n        return max1 * max2;\n \
        \   }\n};"
      java: "class Solution {\n    public int maxProduct(int n) {\n        int max1\
        \ = 0, max2 = 0;\n        while (n > 0) {\n            int d = n % 10;\n   \
        \         if (d >= max1) {\n                max2 = max1;\n                max1\
        \ = d;\n            } else if (d > max2) {\n                max2 = d;\n    \
        \        }\n            n /= 10;\n        }\n        return max1 * max2;\n \
        \   }\n}"
      python: "class Solution(object):\n    def maxProduct(self, n):\n        \"\"\"\
        \n        :type n: int\n        :rtype: int\n        \"\"\"\n        digits\
        \ = sorted([int(d) for d in str(n)])\n        return digits[-1] * digits[-2]"
      python3: "class Solution:\n    def maxProduct(self, n: int) -> int:\n        digits\
        \ = sorted([int(d) for d in str(n)])\n        return digits[-1] * digits[-2]"
      c: "int maxProduct(int n) {\n    int max1 = 0, max2 = 0;\n    while (n > 0) {\n\
        \        int d = n % 10;\n        if (d >= max1) {\n            max2 = max1;\n\
        \            max1 = d;\n        } else if (d > max2) {\n            max2 = d;\n\
        \        }\n        n /= 10;\n    }\n    return max1 * max2;\n}"
      csharp: "public class Solution {\n    public int MaxProduct(int n) {\n       \
        \ int max1 = 0, max2 = 0;\n        while (n > 0) {\n            int d = n %\
        \ 10;\n            if (d >= max1) {\n                max2 = max1;\n        \
        \        max1 = d;\n            } else if (d > max2) {\n                max2\
        \ = d;\n            }\n            n /= 10;\n        }\n        return max1\
        \ * max2;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar maxProduct\
        \ = function(n) {\n    let max1 = 0, max2 = 0;\n    while (n > 0) {\n      \
        \  let d = n % 10;\n        if (d >= max1) {\n            max2 = max1;\n   \
        \         max1 = d;\n        } else if (d > max2) {\n            max2 = d;\n\
        \        }\n        n = Math.floor(n / 10);\n    }\n    return max1 * max2;\n\
        };"
      typescript: "function maxProduct(n: number): number {\n    let max1 = -1;\n  \
        \  let max2 = -1;\n    while (n > 0) {\n        const d = n % 10;\n        if\
        \ (d > max1) {\n            max2 = max1;\n            max1 = d;\n        } else\
        \ if (d > max2) {\n            max2 = d;\n        }\n        n = Math.floor(n\
        \ / 10);\n    }\n    return max1 * max2;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function maxProduct($n) {\n        $max1 = -1;\n        $max2\
        \ = -1;\n        while ($n > 0) {\n            $d = $n % 10;\n            if\
        \ ($d > $max1) {\n                $max2 = $max1;\n                $max1 = $d;\n\
        \            } else if ($d > $max2) {\n                $max2 = $d;\n       \
        \     }\n            $n = (int)($n / 10);\n        }\n        return $max1 *\
        \ $max2;\n    }\n}"
      swift: "class Solution {\n    func maxProduct(_ n: Int) -> Int {\n        var\
        \ max1 = -1\n        var max2 = -1\n        var temp = n\n        while temp\
        \ > 0 {\n            let d = temp % 10\n            if d > max1 {\n        \
        \        max2 = max1\n                max1 = d\n            } else if d > max2\
        \ {\n                max2 = d\n            }\n            temp /= 10\n     \
        \   }\n        return max1 * max2\n    }\n}"
      kotlin: "class Solution {\n    fun maxProduct(n: Int): Int {\n        var max1\
        \ = -1\n        var max2 = -1\n        var temp = n\n        while (temp > 0)\
        \ {\n            val d = temp % 10\n            if (d > max1) {\n          \
        \      max2 = max1\n                max1 = d\n            } else if (d > max2)\
        \ {\n                max2 = d\n            }\n            temp /= 10\n     \
        \   }\n        return max1 * max2\n    }\n}"
      dart: "class Solution {\n  int maxProduct(int n) {\n    int max1 = -1;\n    int\
        \ max2 = -1;\n    while (n > 0) {\n      int d = n % 10;\n      if (d > max1)\
        \ {\n        max2 = max1;\n        max1 = d;\n      } else if (d > max2) {\n\
        \        max2 = d;\n      }\n      n = n ~/ 10;\n    }\n    return max1 * max2;\n\
        \  }\n}"
      go: "func maxProduct(n int) int {\n    max1 := -1\n    max2 := -1\n    for n >\
        \ 0 {\n        d := n % 10\n        if d > max1 {\n            max2 = max1\n\
        \            max1 = d\n        } else if d > max2 {\n            max2 = d\n\
        \        }\n        n /= 10\n    }\n    return max1 * max2\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef max_product(n)\n  digits\
        \ = n.to_s.chars.map(&:to_i)\n  sorted = digits.sort.reverse\n  sorted[0] *\
        \ sorted[1]\nend"
      scala: "object Solution {\n    def maxProduct(n: Int): Int = {\n        val digits\
        \ = n.toString.map(_.asDigit)\n        val sorted = digits.sorted.reverse\n\
        \        sorted(0) * sorted(1)\n    }\n}"
      rust: "impl Solution {\n    pub fn max_product(n: i32) -> i32 {\n        let mut\
        \ digits: Vec<i32> = n.to_string()\n            .chars()\n            .map(|c|\
        \ c.to_digit(10).unwrap() as i32)\n            .collect();\n        digits.sort_unstable_by(|a,\
        \ b| b.cmp(a));\n        digits[0] * digits[1]\n    }\n}"
      racket: "(define/contract (max-product n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let* ([digits (map (lambda (c) (- (char->integer c) 48)) (string->list (number->string\
        \ n)))]\n         [sorted (sort digits >)])\n    (* (car sorted) (cadr sorted)))\n\
        \  )"
      erlang: "-spec max_product(N :: integer()) -> integer().\nmax_product(N) ->\n\
        \  Digits = [C - $0 || C <- integer_to_list(N)],\n  Sorted = lists:reverse(lists:sort(Digits)),\n\
        \  [D1, D2 | _] = Sorted,\n  D1 * D2."
      elixir: "defmodule Solution do\n  @spec max_product(n :: integer) :: integer\n\
        \  def max_product(n) do\n    sorted = n\n             |> Integer.digits()\n\
        \             |> Enum.sort(:desc)\n    Enum.at(sorted, 0) * Enum.at(sorted,\
        \ 1)\n  end\nend"
    approach: 'To find the maximum product of any two digits in a positive integer $n$,
      the most effective strategy is to identify the two largest digits present in the
      number. Since the input $n$ is between $10$ and $10^9$, we are guaranteed at least
      two digits. By finding the largest digit (max1) and the second-largest digit (max2)
      from all available digits (including duplicates), the product of these two values
      will yield the maximum possible result because the product of non-negative integers
      is maximized by choosing the largest available factors.


      The implementation involves extracting each digit of $n$ using modular arithmetic
      ($n \% 10$) and then reducing the number via integer division ($n / 10$). During
      this extraction process, we maintain two variables, `max1` and `max2`. If the
      current digit is greater than or equal to `max1`, we update `max2` to the previous
      `max1` and set `max1` to the new digit. If the digit is only greater than `max2`,
      we update `max2` alone. Alternatively, converting the integer to a string or list
      and sorting the digits allows for a simple selection of the last two elements.
      This approach handles all edge cases, such as multiple occurrences of the same
      digit, efficiently.'
    time_complexity: O(\log n) with one-paragraph explanation. The time complexity is
      determined by the number of digits in the integer $n$, which is $\lfloor \log_{10}
      n \rfloor + 1$. The algorithm iterates through these digits once to find the maximum
      values, and since $n$ is at most $10^9$, the number of iterations is capped at
      10, making the solution very efficient.
    space_complexity: O(1) with one-paragraph explanation. If we use variables to track
      the two largest digits during extraction via arithmetic operations, the space
      complexity is constant. Even if the number is converted to a string or a list
      of digits, the space required remains $O(\log n)$, which is extremely small (at
      most 10 characters).
    elapsed_time: 141.16230058670044
    model: gemini-3-flash-preview
    generated_at: '2026-07-25 01:59:49 '
---

## Problem #3536: Maximum Product of Two Digits

**Difficulty:** Easy

**Topics:** Math, Sorting

## Problem Description

<p>You are given a positive integer <code>n</code>.</p>

<p>Return the <strong>maximum</strong> product of any two digits in <code>n</code>.</p>

<p><strong>Note:</strong> You may use the <strong>same</strong> digit twice if it appears more than once in <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 31</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The digits of <code>n</code> are <code>[3, 1]</code>.</li>
	<li>The possible products of any two digits are: <code>3 * 1 = 3</code>.</li>
	<li>The maximum product is 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 22</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The digits of <code>n</code> are <code>[2, 2]</code>.</li>
	<li>The possible products of any two digits are: <code>2 * 2 = 4</code>.</li>
	<li>The maximum product is 4.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 124</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The digits of <code>n</code> are <code>[1, 2, 4]</code>.</li>
	<li>The possible products of any two digits are: <code>1 * 2 = 2</code>, <code>1 * 4 = 4</code>, <code>2 * 4 = 8</code>.</li>
	<li>The maximum product is 8.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>10 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use brute force

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the maximum product of any two digits in a positive integer $n$, the most effective strategy is to identify the two largest digits present in the number. Since the input $n$ is between $10$ and $10^9$, we are guaranteed at least two digits. By finding the largest digit (max1) and the second-largest digit (max2) from all available digits (including duplicates), the product of these two values will yield the maximum possible result because the product of non-negative integers is maximized by choosing the largest available factors.

The implementation involves extracting each digit of $n$ using modular arithmetic ($n \% 10$) and then reducing the number via integer division ($n / 10$). During this extraction process, we maintain two variables, `max1` and `max2`. If the current digit is greater than or equal to `max1`, we update `max2` to the previous `max1` and set `max1` to the new digit. If the digit is only greater than `max2`, we update `max2` alone. Alternatively, converting the integer to a string or list and sorting the digits allows for a simple selection of the last two elements. This approach handles all edge cases, such as multiple occurrences of the same digit, efficiently.

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
    int maxProduct(int n) {
        int max1 = 0, max2 = 0;
        while (n > 0) {
            int d = n % 10;
            if (d >= max1) {
                max2 = max1;
                max1 = d;
            } else if (d > max2) {
                max2 = d;
            }
            n /= 10;
        }
        return max1 * max2;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProduct(int n) {
        int max1 = 0, max2 = 0;
        while (n > 0) {
            int d = n % 10;
            if (d >= max1) {
                max2 = max1;
                max1 = d;
            } else if (d > max2) {
                max2 = d;
            }
            n /= 10;
        }
        return max1 * max2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = sorted([int(d) for d in str(n)])
        return digits[-1] * digits[-2]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted([int(d) for d in str(n)])
        return digits[-1] * digits[-2]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxProduct(int n) {
    int max1 = 0, max2 = 0;
    while (n > 0) {
        int d = n % 10;
        if (d >= max1) {
            max2 = max1;
            max1 = d;
        } else if (d > max2) {
            max2 = d;
        }
        n /= 10;
    }
    return max1 * max2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProduct(int n) {
        int max1 = 0, max2 = 0;
        while (n > 0) {
            int d = n % 10;
            if (d >= max1) {
                max2 = max1;
                max1 = d;
            } else if (d > max2) {
                max2 = d;
            }
            n /= 10;
        }
        return max1 * max2;
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
 * @return {number}
 */
var maxProduct = function(n) {
    let max1 = 0, max2 = 0;
    while (n > 0) {
        let d = n % 10;
        if (d >= max1) {
            max2 = max1;
            max1 = d;
        } else if (d > max2) {
            max2 = d;
        }
        n = Math.floor(n / 10);
    }
    return max1 * max2;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProduct(n: number): number {
    let max1 = -1;
    let max2 = -1;
    while (n > 0) {
        const d = n % 10;
        if (d > max1) {
            max2 = max1;
            max1 = d;
        } else if (d > max2) {
            max2 = d;
        }
        n = Math.floor(n / 10);
    }
    return max1 * max2;
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
     * @return Integer
     */
    function maxProduct($n) {
        $max1 = -1;
        $max2 = -1;
        while ($n > 0) {
            $d = $n % 10;
            if ($d > $max1) {
                $max2 = $max1;
                $max1 = $d;
            } else if ($d > $max2) {
                $max2 = $d;
            }
            $n = (int)($n / 10);
        }
        return $max1 * $max2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxProduct(_ n: Int) -> Int {
        var max1 = -1
        var max2 = -1
        var temp = n
        while temp > 0 {
            let d = temp % 10
            if d > max1 {
                max2 = max1
                max1 = d
            } else if d > max2 {
                max2 = d
            }
            temp /= 10
        }
        return max1 * max2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProduct(n: Int): Int {
        var max1 = -1
        var max2 = -1
        var temp = n
        while (temp > 0) {
            val d = temp % 10
            if (d > max1) {
                max2 = max1
                max1 = d
            } else if (d > max2) {
                max2 = d
            }
            temp /= 10
        }
        return max1 * max2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxProduct(int n) {
    int max1 = -1;
    int max2 = -1;
    while (n > 0) {
      int d = n % 10;
      if (d > max1) {
        max2 = max1;
        max1 = d;
      } else if (d > max2) {
        max2 = d;
      }
      n = n ~/ 10;
    }
    return max1 * max2;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxProduct(n int) int {
    max1 := -1
    max2 := -1
    for n > 0 {
        d := n % 10
        if d > max1 {
            max2 = max1
            max1 = d
        } else if d > max2 {
            max2 = d
        }
        n /= 10
    }
    return max1 * max2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def max_product(n)
  digits = n.to_s.chars.map(&:to_i)
  sorted = digits.sort.reverse
  sorted[0] * sorted[1]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxProduct(n: Int): Int = {
        val digits = n.toString.map(_.asDigit)
        val sorted = digits.sorted.reverse
        sorted(0) * sorted(1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_product(n: i32) -> i32 {
        let mut digits: Vec<i32> = n.to_string()
            .chars()
            .map(|c| c.to_digit(10).unwrap() as i32)
            .collect();
        digits.sort_unstable_by(|a, b| b.cmp(a));
        digits[0] * digits[1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-product n)
  (-> exact-integer? exact-integer?)
  (let* ([digits (map (lambda (c) (- (char->integer c) 48)) (string->list (number->string n)))]
         [sorted (sort digits >)])
    (* (car sorted) (cadr sorted)))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_product(N :: integer()) -> integer().
max_product(N) ->
  Digits = [C - $0 || C <- integer_to_list(N)],
  Sorted = lists:reverse(lists:sort(Digits)),
  [D1, D2 | _] = Sorted,
  D1 * D2.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_product(n :: integer) :: integer
  def max_product(n) do
    sorted = n
             |> Integer.digits()
             |> Enum.sort(:desc)
    Enum.at(sorted, 0) * Enum.at(sorted, 1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(\log n) with one-paragraph explanation. The time complexity is determined by the number of digits in the integer $n$, which is $\lfloor \log_{10} n \rfloor + 1$. The algorithm iterates through these digits once to find the maximum values, and since $n$ is at most $10^9$, the number of iterations is capped at 10, making the solution very efficient.
- **Space Complexity:** O(1) with one-paragraph explanation. If we use variables to track the two largest digits during extraction via arithmetic operations, the space complexity is constant. Even if the number is converted to a string or a list of digits, the space required remains $O(\log n)$, which is extremely small (at most 10 characters).
