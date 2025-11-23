---
layout: post
title: "Count Operations to Obtain Zero"
date: 2025-11-09 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-operations-to-obtain-zero/
---

## Problem #2169: Count Operations to Obtain Zero

**Difficulty:** Easy

**Topics:** Math, Simulation

## Problem Description

<p>You are given two <strong>non-negative</strong> integers <code>num1</code> and <code>num2</code>.</p>

<p>In one <strong>operation</strong>, if <code>num1 &gt;= num2</code>, you must subtract <code>num2</code> from <code>num1</code>, otherwise subtract <code>num1</code> from <code>num2</code>.</p>

<ul>
	<li>For example, if <code>num1 = 5</code> and <code>num2 = 4</code>, subtract <code>num2</code> from <code>num1</code>, thus obtaining <code>num1 = 1</code> and <code>num2 = 4</code>. However, if <code>num1 = 4</code> and <code>num2 = 5</code>, after one operation, <code>num1 = 4</code> and <code>num2 = 1</code>.</li>
</ul>

<p>Return <em>the <strong>number of operations</strong> required to make either</em> <code>num1 = 0</code> <em>or</em> <code>num2 = 0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 2, num2 = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
- Operation 1: num1 = 2, num2 = 3. Since num1 &lt; num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 &gt; num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = 10, num2 = 10
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
- Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
So the total number of operations required is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num1, num2 &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Try simulating the process until either of the two integers is zero.

2. Count the number of operations done.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:03:44 )</small>
</summary>

<div class="ai-solution-content">

### Approach

Simulate the operations described in the problem statement in a loop, incrementing a counter in each step, until either `num1` or `num2` becomes zero. In each step, subtract the smaller number from the larger one.

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
    int countOperations(int num1, int num2) {
        int operations = 0;
        while (num1 != 0 && num2 != 0) {
            if (num1 >= num2) {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations++;
        }
        return operations;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countOperations(int num1, int num2) {
        int operations = 0;
        while (num1 != 0 && num2 != 0) {
            if (num1 >= num2) {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations++;
        }
        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            operations += 1
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            operations += 1
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countOperations(int num1, int num2) {
    int operations = 0;
    while (num1 != 0 && num2 != 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        operations++;
    }
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountOperations(int num1, int num2) {
        int operations = 0;
        while (num1 != 0 && num2 != 0) {
            if (num1 >= num2) {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations++;
        }
        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var countOperations = function(num1, num2) {
    let operations = 0;
    while (num1 !== 0 && num2 !== 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        operations++;
    }
    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countOperations(num1: number, num2: number): number {
    let operations: number = 0;
    while (num1 !== 0 && num2 !== 0) {
        if (num1 >= num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
        operations++;
    }
    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @return Integer
     */
    function countOperations($num1, $num2) {
        $operations = 0;
        while ($num1 != 0 && $num2 != 0) {
            if ($num1 >= $num2) {
                $num1 -= $num2;
            } else {
                $num2 -= $num1;
            }
            $operations++;
        }
        return $operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countOperations(_ num1: Int, _ num2: Int) -> Int {
        var n1 = num1
        var n2 = num2
        var operations = 0
        while n1 != 0 && n2 != 0 {
            if n1 >= n2 {
                n1 -= n2
            } else {
                n2 -= n1
            }
            operations += 1
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countOperations(num1: Int, num2: Int): Int {
        var n1 = num1
        var n2 = num2
        var operations = 0
        while (n1 != 0 && n2 != 0) {
            if (n1 >= n2) {
                n1 -= n2
            } else {
                n2 -= n1
            }
            operations++
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countOperations(int num1, int num2) {
    int operations = 0;
    while (num1 != 0 && num2 != 0) {
      if (num1 >= num2) {
        num1 -= num2;
      } else {
        num2 -= num1;
      }
      operations++;
    }
    return operations;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countOperations(num1 int, num2 int) int {
    operations := 0
    for num1 != 0 && num2 != 0 {
        if num1 >= num2 {
            num1 -= num2
        } else {
            num2 -= num1
        }
        operations++
    }
    return operations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def count_operations(num1, num2)
    operations = 0
    while num1 != 0 && num2 != 0
        if num1 >= num2
            num1 -= num2
        else
            num2 -= num1
        end
        operations += 1
    end
    return operations
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countOperations(num1: Int, num2: Int): Int = {
        var n1 = num1
        var n2 = num2
        var operations = 0
        while (n1 != 0 && n2 != 0) {
            if (n1 >= n2) {
                n1 -= n2
            } else {
                n2 -= n1
            }
            operations += 1
        }
        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_operations(mut num1: i32, mut num2: i32) -> i32 {
        let mut operations = 0;
        while num1 != 0 && num2 != 0 {
            if num1 >= num2 {
                num1 -= num2;
            } else {
                num2 -= num1;
            }
            operations += 1;
        }
        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-operations num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((n1 num1) (n2 num2) (ops 0))
    (cond
      ((or (= n1 0) (= n2 0)) ops)
      ((>= n1 n2) (loop (- n1 n2) n2 (+ ops 1)))
      (else (loop n1 (- n2 n1) (+ ops 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_operations(Num1 :: integer(), Num2 :: integer()) -> integer().
count_operations(Num1, Num2) ->
    count_operations_recursive(Num1, Num2, 0).

count_operations_recursive(0, _, Operations) -> Operations;
count_operations_recursive(_, 0, Operations) -> Operations;
count_operations_recursive(Num1, Num2, Operations) when Num1 >= Num2 ->
    count_operations_recursive(Num1 - Num2, Num2, Operations + 1);
count_operations_recursive(Num1, Num2, Operations) when Num1 < Num2 ->
    count_operations_recursive(Num1, Num2 - Num1, Operations + 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_operations(num1 :: integer, num2 :: integer) :: integer
  def count_operations(num1, num2) do
    count_operations_recursive(num1, num2, 0)
  end

  defp count_operations_recursive(0, _num2, operations), do: operations
  defp count_operations_recursive(_num1, 0, operations), do: operations
  defp count_operations_recursive(num1, num2, operations) when num1 >= num2 do
    count_operations_recursive(num1 - num2, num2, operations + 1)
  end
  defp count_operations_recursive(num1, num2, operations) when num1 < num2 do
    count_operations_recursive(num1, num2 - num1, operations + 1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(max(num1, num2))

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:03:45 )</small>
</summary>

<div class="ai-solution-content">

### Approach

No approach provided

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
// Generation failed for C++
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
