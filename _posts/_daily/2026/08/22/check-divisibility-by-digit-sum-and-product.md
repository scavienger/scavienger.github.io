---
layout: post
title: "Check Divisibility by Digit Sum and Product"
date: 2026-08-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool checkDivisibility(int n) {\n       \
        \ int digitSum = 0;\n        long long digitProduct = 1;\n        int temp =\
        \ n;\n        while (temp > 0) {\n            int digit = temp % 10;\n     \
        \       digitSum += digit;\n            digitProduct *= digit;\n           \
        \ temp /= 10;\n        }\n        return n % (digitSum + digitProduct) == 0;\n\
        \    }\n};"
      java: "class Solution {\n    public boolean checkDivisibility(int n) {\n     \
        \   int digitSum = 0;\n        long digitProduct = 1;\n        int temp = n;\n\
        \        while (temp > 0) {\n            int digit = temp % 10;\n          \
        \  digitSum += digit;\n            digitProduct *= digit;\n            temp\
        \ /= 10;\n        }\n        return n % (digitSum + digitProduct) == 0;\n  \
        \  }\n}"
      python: "class Solution(object):\n    def checkDivisibility(self, n):\n      \
        \  \"\"\"\n        :type n: int\n        :rtype: bool\n        \"\"\"\n    \
        \    digit_sum = 0\n        digit_product = 1\n        temp = n\n        while\
        \ temp > 0:\n            digit = temp % 10\n            digit_sum += digit\n\
        \            digit_product *= digit\n            temp //= 10\n        return\
        \ n % (digit_sum + digit_product) == 0"
      python3: "class Solution:\n    def checkDivisibility(self, n: int) -> bool:\n\
        \        digit_sum = 0\n        digit_product = 1\n        temp = n\n      \
        \  while temp > 0:\n            digit = temp % 10\n            digit_sum +=\
        \ digit\n            digit_product *= digit\n            temp //= 10\n     \
        \   return n % (digit_sum + digit_product) == 0"
      c: "bool checkDivisibility(int n) {\n    int digitSum = 0;\n    long long digitProduct\
        \ = 1;\n    int temp = n;\n    while (temp > 0) {\n        int digit = temp\
        \ % 10;\n        digitSum += digit;\n        digitProduct *= digit;\n      \
        \  temp /= 10;\n    }\n    return n % (digitSum + digitProduct) == 0;\n}"
      csharp: "public class Solution {\n    public bool CheckDivisibility(int n) {\n\
        \        int digitSum = 0;\n        long digitProduct = 1;\n        int temp\
        \ = n;\n        while (temp > 0) {\n            int digit = temp % 10;\n   \
        \         digitSum += digit;\n            digitProduct *= digit;\n         \
        \   temp /= 10;\n        }\n        return n % (digitSum + (int)digitProduct)\
        \ == 0;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {boolean}\n */\nvar checkDivisibility\
        \ = function(n) {\n    let digitSum = 0;\n    let digitProduct = 1;\n    let\
        \ temp = n;\n    while (temp > 0) {\n        let digit = temp % 10;\n      \
        \  digitSum += digit;\n        digitProduct *= digit;\n        temp = Math.floor(temp\
        \ / 10);\n    }\n    return n % (digitSum + digitProduct) === 0;\n};"
      typescript: "function checkDivisibility(n: number): boolean {\n    let digitSum\
        \ = 0;\n    let digitProduct = 1;\n    let temp = n;\n    while (temp > 0) {\n\
        \        let digit = temp % 10;\n        digitSum += digit;\n        digitProduct\
        \ *= digit;\n        temp = Math.floor(temp / 10);\n    }\n    return n % (digitSum\
        \ + digitProduct) === 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Boolean\n\
        \     */\n    function checkDivisibility($n) {\n        $digitSum = 0;\n   \
        \     $digitProduct = 1;\n        $temp = $n;\n        while ($temp > 0) {\n\
        \            $digit = $temp % 10;\n            $digitSum += $digit;\n      \
        \      $digitProduct *= $digit;\n            $temp = (int)($temp / 10);\n  \
        \      }\n        return $n % ($digitSum + $digitProduct) === 0;\n    }\n}"
      swift: "class Solution {\n    func checkDivisibility(_ n: Int) -> Bool {\n   \
        \     var digitSum = 0\n        var digitProduct = 1\n        var temp = n\n\
        \        while temp > 0 {\n            let digit = temp % 10\n            digitSum\
        \ += digit\n            digitProduct *= digit\n            temp /= 10\n    \
        \    }\n        return n % (digitSum + digitProduct) == 0\n    }\n}"
      kotlin: "class Solution {\n    fun checkDivisibility(n: Int): Boolean {\n    \
        \    var digitSum = 0\n        var digitProduct = 1\n        var temp = n\n\
        \        while (temp > 0) {\n            val digit = temp % 10\n           \
        \ digitSum += digit\n            digitProduct *= digit\n            temp /=\
        \ 10\n        }\n        return n % (digitSum + digitProduct) == 0\n    }\n}"
      dart: "class Solution {\n  bool checkDivisibility(int n) {\n    int digitSum =\
        \ 0;\n    int digitProduct = 1;\n    int temp = n;\n    while (temp > 0) {\n\
        \      int digit = temp % 10;\n      digitSum += digit;\n      digitProduct\
        \ *= digit;\n      temp ~/= 10;\n    }\n    return n % (digitSum + digitProduct)\
        \ == 0;\n  }\n}"
      go: "func checkDivisibility(n int) bool {\n    digitSum := 0\n    digitProduct\
        \ := 1\n    temp := n\n    for temp > 0 {\n        digit := temp % 10\n    \
        \    digitSum += digit\n        digitProduct *= digit\n        temp /= 10\n\
        \    }\n    return n % (digitSum + digitProduct) == 0\n}"
      ruby: "# @param {Integer} n\n# @return {Boolean}\ndef check_divisibility(n)\n\
        \  sum = 0\n  prod = 1\n  temp = n\n  while temp > 0\n    digit = temp % 10\n\
        \    sum += digit\n    prod *= digit\n    temp /= 10\n  end\n  n % (sum + prod)\
        \ == 0\nend"
      scala: "object Solution {\n    def checkDivisibility(n: Int): Boolean = {\n  \
        \      var sum = 0\n        var prod = 1\n        var temp = n\n        while\
        \ (temp > 0) {\n            val digit = temp % 10\n            sum += digit\n\
        \            prod *= digit\n            temp /= 10\n        }\n        n % (sum\
        \ + prod) == 0\n    }\n}"
      rust: "impl Solution {\n    pub fn check_divisibility(n: i32) -> bool {\n    \
        \    let mut sum = 0;\n        let mut prod = 1;\n        let mut temp = n;\n\
        \        while temp > 0 {\n            let digit = temp % 10;\n            sum\
        \ += digit;\n            prod *= digit;\n            temp /= 10;\n        }\n\
        \        n % (sum + prod) == 0\n    }\n}"
      racket: "(define/contract (check-divisibility n)\n  (-> exact-integer? boolean?)\n\
        \  (let* ([s-n (number->string n)]\n         [digits (map (lambda (c) (- (char->integer\
        \ c) 48)) (string->list s-n))]\n         [sum (apply + digits)]\n         [prod\
        \ (apply * digits)])\n    (= (remainder n (+ sum prod)) 0)))"
      erlang: "-spec check_divisibility(N :: integer()) -> boolean().\ncheck_divisibility(N)\
        \ ->\n  Digits = [X - $0 || X <- integer_to_list(N)],\n  Sum = lists:sum(Digits),\n\
        \  Prod = lists:foldl(fun(X, Acc) -> X * Acc end, 1, Digits),\n  N rem (Sum\
        \ + Prod) =:= 0."
      elixir: "defmodule Solution do\n  @spec check_divisibility(n :: integer) :: boolean\n\
        \  def check_divisibility(n) do\n    digits = Integer.digits(n)\n    sum = Enum.sum(digits)\n\
        \    prod = Enum.reduce(digits, 1, fn x, acc -> x * acc end)\n    rem(n, sum\
        \ + prod) == 0\n  end\nend"
    approach: 'The algorithm extracts each digit of the integer n individually by repeatedly
      performing modulo 10 and integer division by 10 operations. For each digit obtained,
      we update two running variables: one representing the sum of the digits (initialized
      at 0) and one representing the product of the digits (initialized at 1). This
      process continues until all digits of n have been processed, effectively converting
      the decimal representation of n into its constituent numeric components.


      After calculating the final digit sum and digit product, we determine their total
      by adding them together. The final step involves a divisibility check to see if
      the original value of n is a multiple of this combined total. Since the input
      is a positive integer, the digit sum will always be at least 1, ensuring the divisor
      is always non-zero. The constraint of n up to 10^6 ensures that calculations stay
      within standard 32-bit integer bounds.'
    time_complexity: O(log_{10} n) with one-paragraph explanation. The number of iterations
      in the digit-extraction loop is directly proportional to the number of digits
      in the integer n, which is log_{10} n + 1. For n = 10^6, this results in at most
      7 iterations.
    space_complexity: O(1) with one-paragraph explanation. The solution uses a constant
      amount of extra space for auxiliary variables like the digit sum, digit product,
      and temporary copies of the input, regardless of the size of n.
    elapsed_time: 90.09638857841492
    model: gemini-3-flash-preview
    generated_at: '2026-08-22 00:48:20 '
---

## Problem #3622: Check Divisibility by Digit Sum and Product

**Difficulty:** Easy

**Topics:** Math

## Problem Description

<p>You are given a positive integer <code>n</code>. Determine whether <code>n</code> is divisible by the <strong>sum </strong>of the following two values:</p>

<ul>
	<li>
	<p>The <strong>digit sum</strong> of <code>n</code> (the sum of its digits).</p>
	</li>
	<li>
	<p>The <strong>digit</strong> <strong>product</strong> of <code>n</code> (the product of its digits).</p>
	</li>
</ul>

<p>Return <code>true</code> if <code>n</code> is divisible by this sum; otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 99</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 23</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Compute the digits' sum and product, then check if `n % (sum + product) == 0`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm extracts each digit of the integer n individually by repeatedly performing modulo 10 and integer division by 10 operations. For each digit obtained, we update two running variables: one representing the sum of the digits (initialized at 0) and one representing the product of the digits (initialized at 1). This process continues until all digits of n have been processed, effectively converting the decimal representation of n into its constituent numeric components.

After calculating the final digit sum and digit product, we determine their total by adding them together. The final step involves a divisibility check to see if the original value of n is a multiple of this combined total. Since the input is a positive integer, the digit sum will always be at least 1, ensuring the divisor is always non-zero. The constraint of n up to 10^6 ensures that calculations stay within standard 32-bit integer bounds.

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
    bool checkDivisibility(int n) {
        int digitSum = 0;
        long long digitProduct = 1;
        int temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            digitSum += digit;
            digitProduct *= digit;
            temp /= 10;
        }
        return n % (digitSum + digitProduct) == 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean checkDivisibility(int n) {
        int digitSum = 0;
        long digitProduct = 1;
        int temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            digitSum += digit;
            digitProduct *= digit;
            temp /= 10;
        }
        return n % (digitSum + digitProduct) == 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit_sum = 0
        digit_product = 1
        temp = n
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10
        return n % (digit_sum + digit_product) == 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        temp = n
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10
        return n % (digit_sum + digit_product) == 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool checkDivisibility(int n) {
    int digitSum = 0;
    long long digitProduct = 1;
    int temp = n;
    while (temp > 0) {
        int digit = temp % 10;
        digitSum += digit;
        digitProduct *= digit;
        temp /= 10;
    }
    return n % (digitSum + digitProduct) == 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CheckDivisibility(int n) {
        int digitSum = 0;
        long digitProduct = 1;
        int temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            digitSum += digit;
            digitProduct *= digit;
            temp /= 10;
        }
        return n % (digitSum + (int)digitProduct) == 0;
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
 * @return {boolean}
 */
var checkDivisibility = function(n) {
    let digitSum = 0;
    let digitProduct = 1;
    let temp = n;
    while (temp > 0) {
        let digit = temp % 10;
        digitSum += digit;
        digitProduct *= digit;
        temp = Math.floor(temp / 10);
    }
    return n % (digitSum + digitProduct) === 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function checkDivisibility(n: number): boolean {
    let digitSum = 0;
    let digitProduct = 1;
    let temp = n;
    while (temp > 0) {
        let digit = temp % 10;
        digitSum += digit;
        digitProduct *= digit;
        temp = Math.floor(temp / 10);
    }
    return n % (digitSum + digitProduct) === 0;
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
     * @return Boolean
     */
    function checkDivisibility($n) {
        $digitSum = 0;
        $digitProduct = 1;
        $temp = $n;
        while ($temp > 0) {
            $digit = $temp % 10;
            $digitSum += $digit;
            $digitProduct *= $digit;
            $temp = (int)($temp / 10);
        }
        return $n % ($digitSum + $digitProduct) === 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func checkDivisibility(_ n: Int) -> Bool {
        var digitSum = 0
        var digitProduct = 1
        var temp = n
        while temp > 0 {
            let digit = temp % 10
            digitSum += digit
            digitProduct *= digit
            temp /= 10
        }
        return n % (digitSum + digitProduct) == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun checkDivisibility(n: Int): Boolean {
        var digitSum = 0
        var digitProduct = 1
        var temp = n
        while (temp > 0) {
            val digit = temp % 10
            digitSum += digit
            digitProduct *= digit
            temp /= 10
        }
        return n % (digitSum + digitProduct) == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool checkDivisibility(int n) {
    int digitSum = 0;
    int digitProduct = 1;
    int temp = n;
    while (temp > 0) {
      int digit = temp % 10;
      digitSum += digit;
      digitProduct *= digit;
      temp ~/= 10;
    }
    return n % (digitSum + digitProduct) == 0;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func checkDivisibility(n int) bool {
    digitSum := 0
    digitProduct := 1
    temp := n
    for temp > 0 {
        digit := temp % 10
        digitSum += digit
        digitProduct *= digit
        temp /= 10
    }
    return n % (digitSum + digitProduct) == 0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Boolean}
def check_divisibility(n)
  sum = 0
  prod = 1
  temp = n
  while temp > 0
    digit = temp % 10
    sum += digit
    prod *= digit
    temp /= 10
  end
  n % (sum + prod) == 0
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def checkDivisibility(n: Int): Boolean = {
        var sum = 0
        var prod = 1
        var temp = n
        while (temp > 0) {
            val digit = temp % 10
            sum += digit
            prod *= digit
            temp /= 10
        }
        n % (sum + prod) == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn check_divisibility(n: i32) -> bool {
        let mut sum = 0;
        let mut prod = 1;
        let mut temp = n;
        while temp > 0 {
            let digit = temp % 10;
            sum += digit;
            prod *= digit;
            temp /= 10;
        }
        n % (sum + prod) == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (check-divisibility n)
  (-> exact-integer? boolean?)
  (let* ([s-n (number->string n)]
         [digits (map (lambda (c) (- (char->integer c) 48)) (string->list s-n))]
         [sum (apply + digits)]
         [prod (apply * digits)])
    (= (remainder n (+ sum prod)) 0)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec check_divisibility(N :: integer()) -> boolean().
check_divisibility(N) ->
  Digits = [X - $0 || X <- integer_to_list(N)],
  Sum = lists:sum(Digits),
  Prod = lists:foldl(fun(X, Acc) -> X * Acc end, 1, Digits),
  N rem (Sum + Prod) =:= 0.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec check_divisibility(n :: integer) :: boolean
  def check_divisibility(n) do
    digits = Integer.digits(n)
    sum = Enum.sum(digits)
    prod = Enum.reduce(digits, 1, fn x, acc -> x * acc end)
    rem(n, sum + prod) == 0
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log_{10} n) with one-paragraph explanation. The number of iterations in the digit-extraction loop is directly proportional to the number of digits in the integer n, which is log_{10} n + 1. For n = 10^6, this results in at most 7 iterations.
- **Space Complexity:** O(1) with one-paragraph explanation. The solution uses a constant amount of extra space for auxiliary variables like the digit sum, digit product, and temporary copies of the input, regardless of the size of n.
