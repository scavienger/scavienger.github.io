---
layout: post
title: "1-bit and 2-bit Characters"
date: 2025-11-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/1-bit-and-2-bit-characters/
---

## Problem #717: 1-bit and 2-bit Characters

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<div class="leetcode-problem-description" markdown="0">

<p>We have two special characters:</p>

<ul>
	<li>The first character can be represented by one bit <code>0</code>.</li>
	<li>The second character can be represented by two bits (<code>10</code> or <code>11</code>).</li>
</ul>

<p>Given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,0,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,1,1,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bits.length &lt;= 1000</code></li>
	<li><code>bits[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


</div>

## Hints

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 13:44:50)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The problem asks us to determine if the last character in a given binary array `bits` (which is guaranteed to end with `0`) must be a one-bit character. We are given two types of characters: a one-bit character represented by `0`, and a two-bit character represented by `10` or `11`. The key observation is that the decoding process is unambiguous: if we encounter a `0`, it must be a one-bit character; if we encounter a `1`, it must be the start of a two-bit character. This means there's only one valid way to parse the `bits` array from left to right.

Our strategy is to simulate the decoding process from the beginning of the `bits` array. We maintain an index `i` that points to the start of the current character being decoded. If `bits[i]` is `0`, it signifies a one-bit character, so we advance `i` by 1. If `bits[i]` is `1`, it signifies a two-bit character (which consumes `bits[i]` and `bits[i+1]`), so we advance `i` by 2. We continue this process, moving `i` forward, until `i` reaches or surpasses the end of the array.

The crucial condition to check is whether the last character decoded was indeed a one-bit character. This happens if our index `i` *exactly lands on* the last position (`bits.length - 1`) as a result of processing a `0`. If `i` skips over `bits.length - 1` (meaning it becomes `bits.length` or `bits.length + 1` directly from `bits.length - 2` or `bits.length - 1` respectively, due to a two-bit character), then the `0` at `bits.length - 1` was part of a two-bit character, and thus the last character is not a one-bit character.

We can implement this by iterating with a `while` loop. Inside the loop, before attempting to decode `bits[i]`, we first check if `i` has reached `bits.length - 1`. If it has, it means we successfully parsed all preceding characters, and the character starting at `i` (which is `bits[bits.length - 1]`) is a `0` (as per problem constraint). This `0` must therefore be a standalone one-bit character, so we return `true`. If `i` has not reached the end, we proceed with decoding: if `bits[i]` is `1`, increment `i` by 2; otherwise (if `bits[i]` is `0`), increment `i` by 1. If the loop finishes without `i` ever being exactly `bits.length - 1` (because `i` overshot due to a two-bit character consuming the last `0`), then we return `false`.

{% endraw %}

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
    bool isOneBitCharacter(std::vector<int>& bits) {
        int i = 0;
        int n = bits.size();

        while (i < n) {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if (i == n - 1) {
                return true;
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if (bits[i] == 1) {
                i += 2;
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits[i] == 0
                i += 1;
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        int n = bits.length;

        while (i < n) {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if (i == n - 1) {
                return true;
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if (bits[i] == 1) {
                i += 2;
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits[i] == 0
                i += 1;
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n:
            # If we are at the last index, and we haven't overshot it yet,
            # it means this '0' at the end must be a one-bit character.
            if i == n - 1:
                return True

            # If the current bit is 1, it's a two-bit character.
            # We advance the index by 2.
            if bits[i] == 1:
                i += 2
            # If the current bit is 0, it's a one-bit character.
            # We advance the index by 1.
            else:  # bits[i] == 0
                i += 1

        # If the loop finishes, it means 'i' has become >= n.
        # This implies the last character was a two-bit character that
        # consumed the final '0' and potentially overshot the array boundary.
        # So, the last character was NOT a one-bit character.
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n:
            # If we are at the last index, and we haven't overshot it yet,
            # it means this '0' at the end must be a one-bit character.
            if i == n - 1:
                return True

            # If the current bit is 1, it's a two-bit character.
            # We advance the index by 2.
            if bits[i] == 1:
                i += 2
            # If the current bit is 0, it's a one-bit character.
            # We advance the index by 1.
            else:  # bits[i] == 0
                i += 1

        # If the loop finishes, it means 'i' has become >= n.
        # This implies the last character was a two-bit character that
        # consumed the final '0' and potentially overshot the array boundary.
        # So, the last character was NOT a one-bit character.
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>

bool isOneBitCharacter(int* bits, int bitsSize) {
    int i = 0;

    while (i < bitsSize) {
        // If we are at the last index, and we haven't overshot it yet,
        // it means this '0' at the end must be a one-bit character.
        if (i == bitsSize - 1) {
            return true;
        }

        // If the current bit is 1, it's a two-bit character.
        // We advance the index by 2.
        if (bits[i] == 1) {
            i += 2;
        } 
        // If the current bit is 0, it's a one-bit character.
        // We advance the index by 1.
        else { // bits[i] == 0
            i += 1;
        }
    }

    // If the loop finishes, it means 'i' has become >= bitsSize.
    // This implies the last character was a two-bit character that
    // consumed the final '0' and potentially overshot the array boundary.
    // So, the last character was NOT a one-bit character.
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int i = 0;
        int n = bits.Length;

        while (i < n) {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if (i == n - 1) {
                return true;
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if (bits[i] == 1) {
                i += 2;
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits[i] == 0
                i += 1;
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    let i = 0;
    const n = bits.length;

    while (i < n) {
        // If we are at the last index, and we haven't overshot it yet,
        // it means this '0' at the end must be a one-bit character.
        if (i === n - 1) {
            return true;
        }

        // If the current bit is 1, it's a two-bit character.
        // We advance the index by 2.
        if (bits[i] === 1) {
            i += 2;
        } 
        // If the current bit is 0, it's a one-bit character.
        // We advance the index by 1.
        else { // bits[i] === 0
            i += 1;
        }
    }

    // If the loop finishes, it means 'i' has become >= n.
    // This implies the last character was a two-bit character that
    // consumed the final '0' and potentially overshot the array boundary.
    // So, the last character was NOT a one-bit character.
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isOneBitCharacter(bits: number[]): boolean {
    let i = 0;
    const n = bits.length;

    while (i < n) {
        // If we are at the last index, and we haven't overshot it yet,
        // it means this '0' at the end must be a one-bit character.
        if (i === n - 1) {
            return true;
        }

        // If the current bit is 1, it's a two-bit character.
        // We advance the index by 2.
        if (bits[i] === 1) {
            i += 2;
        } 
        // If the current bit is 0, it's a one-bit character.
        // We advance the index by 1.
        else { // bits[i] === 0
            i += 1;
        }
    }

    // If the loop finishes, it means 'i' has become >= n.
    // This implies the last character was a two-bit character that
    // consumed the final '0' and potentially overshot the array boundary.
    // So, the last character was NOT a one-bit character.
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits): bool {
        $i = 0;
        $n = count($bits);

        while ($i < $n) {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if ($i === $n - 1) {
                return true;
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if ($bits[$i] === 1) {
                $i += 2;
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // $bits[$i] === 0
                $i += 1;
            }
        }

        // If the loop finishes, it means '$i' has become >= $n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        var i = 0
        let n = bits.count

        while i < n {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if i == n - 1 {
                return true
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if bits[i] == 1 {
                i += 2
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits[i] == 0
                i += 1
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        var i = 0
        val n = bits.size

        while (i < n) {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if (i == n - 1) {
                return true
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if (bits[i] == 1) {
                i += 2
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits[i] == 0
                i += 1
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    bool isOneBitCharacter(List<int> bits) {
        int i = 0;
        int n = bits.length;

        while (i < n) {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if (i == n - 1) {
                return true;
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if (bits[i] == 1) {
                i += 2;
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits[i] == 0
                i += 1;
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isOneBitCharacter(bits []int) bool {
    i := 0
    n := len(bits)

    for i < n {
        // If we are at the last index, and we haven't overshot it yet,
        // it means this '0' at the end must be a one-bit character.
        if i == n - 1 {
            return true
        }

        // If the current bit is 1, it's a two-bit character.
        // We advance the index by 2.
        if bits[i] == 1 {
            i += 2
        } 
        // If the current bit is 0, it's a one-bit character.
        // We advance the index by 1.
        else { // bits[i] == 0
            i += 1
        }
    }

    // If the loop finishes, it means 'i' has become >= n.
    // This implies the last character was a two-bit character that
    // consumed the final '0' and potentially overshot the array boundary.
    // So, the last character was NOT a one-bit character.
    return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def is_one_bit_character(bits)
    i = 0
    n = bits.length

    while i < n
        # If we are at the last index, and we haven't overshot it yet,
        # it means this '0' at the end must be a one-bit character.
        if i == n - 1
            return true
        end

        # If the current bit is 1, it's a two-bit character.
        # We advance the index by 2.
        if bits[i] == 1
            i += 2
        # If the current bit is 0, it's a one-bit character.
        # We advance the index by 1.
        else # bits[i] == 0
            i += 1
        end
    end

    # If the loop finishes, it means 'i' has become >= n.
    # This implies the last character was a two-bit character that
    # consumed the final '0' and potentially overshot the array boundary.
    # So, the last character was NOT a one-bit character.
    return false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        var i = 0
        val n = bits.length

        while (i < n) {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if (i == n - 1) {
                return true
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if (bits(i) == 1) {
                i += 2
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits(i) == 0
                i += 1
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        false // Scala implicitly returns the last expression
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        let n = bits.len();

        while i < n {
            // If we are at the last index, and we haven't overshot it yet,
            // it means this '0' at the end must be a one-bit character.
            if i == n - 1 {
                return true;
            }

            // If the current bit is 1, it's a two-bit character.
            // We advance the index by 2.
            if bits[i] == 1 {
                i += 2;
            } 
            // If the current bit is 0, it's a one-bit character.
            // We advance the index by 1.
            else { // bits[i] == 0
                i += 1;
            }
        }

        // If the loop finishes, it means 'i' has become >= n.
        // This implies the last character was a two-bit character that
        // consumed the final '0' and potentially overshot the array boundary.
        // So, the last character was NOT a one-bit character.
        false // Rust implicitly returns the last expression
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(provide (contract-out
  [is-one-bit-character (-> (listof exact-integer?) boolean?)]))

(define (is-one-bit-character bits)
  (let loop ((i 0) (n (length bits)))
    (cond
      ;; If the current index 'i' is exactly the last index (n-1),
      ;; it means the character starting at 'i' is the final character.
      ;; Since the problem guarantees the array ends with '0', this character
      ;; must be a one-bit character.
      [(= i (- n 1)) #true]

      ;; If 'i' has gone beyond the array bounds (i.e., >= n),
      ;; it implies that the character preceding this point consumed the last bit
      ;; as part of a two-bit character. Thus, the last character was not one-bit.
      [(>= i n) #false]

      ;; If bits[i] is 1, it's a two-bit character. Advance 'i' by 2.
      [(= (list-ref bits i) 1) (loop (+ i 2) n)]

      ;; Otherwise (bits[i] is 0), it's a one-bit character. Advance 'i' by 1.
      [else (loop (+ i 1) n)])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([is_one_bit_character/1]).

%% @spec is_one_bit_character(Bits :: [integer()]) -> boolean()
%% @doc Determines if the last character in the bits array is a one-bit character.
is_one_bit_character(Bits) ->
    N = length(Bits),
    is_one_bit_character_recursive(Bits, 0, N).

is_one_bit_character_recursive(_Bits, I, N) when I =:= N - 1 ->
    % If the current index 'I' is exactly the last index (N-1),
    % it means the character starting at 'I' is the final character.
    % Since the problem guarantees the array ends with '0', this character
    % must be a one-bit character.
    true;

is_one_bit_character_recursive(_Bits, I, N) when I >= N ->
    % If 'I' has gone beyond the array bounds (i.e., >= N),
    % it implies that the character preceding this point consumed the last bit
    % as part of a two-bit character. Thus, the last character was not one-bit.
    false;

is_one_bit_character_recursive(Bits, I, N) ->
    % Erlang lists are 1-indexed for lists:nth, so (I + 1)
    case lists:nth(I + 1, Bits) of
        1 -> % If bits[I] is 1, it's a two-bit character. Advance 'I' by 2.
            is_one_bit_character_recursive(Bits, I + 2, N);
        0 -> % Otherwise (bits[I] is 0), it's a one-bit character. Advance 'I' by 1.
            is_one_bit_character_recursive(Bits, I + 1, N)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @doc """
  Determines if the last character in the bits array is a one-bit character.
  """
  @spec is_one_bit_character(bits :: [integer]) :: boolean
  def is_one_bit_character(bits) do
    n = length(bits)
    is_one_bit_character_recursive(bits, 0, n)
  end

  defp is_one_bit_character_recursive(_bits, i, n) when i == n - 1 do
    # If the current index 'i' is exactly the last index (n-1),
    # it means the character starting at 'i' is the final character.
    # Since the problem guarantees the array ends with '0', this character
    # must be a one-bit character.
    true
  end

  defp is_one_bit_character_recursive(_bits, i, n) when i >= n do
    # If 'i' has gone beyond the array bounds (i.e., >= n),
    # it implies that the character preceding this point consumed the last bit
    # as part of a two-bit character. Thus, the last character was not one-bit.
    false
  end

  defp is_one_bit_character_recursive(bits, i, n) do
    case Enum.at(bits, i) do
      1 -> # If bits[i] is 1, it's a two-bit character. Advance 'i' by 2.
        is_one_bit_character_recursive(bits, i + 2, n)
      0 -> # Otherwise (bits[i] is 0), it's a one-bit character. Advance 'i' by 1.
        is_one_bit_character_recursive(bits, i + 1, n)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)

</div>
</details>


<hr class="ai-solution-separator">


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 13:44:54)</small>
</summary>

<div class="ai-solution-content">

{% raw %}

### Approach

The problem can be solved by iterating through the binary array from left to right and keeping track of the current position. If the current bit is 0, it means we have encountered a one-bit character, so we move to the next position. If the current bit is 1, it means we have encountered a two-bit character, so we move two positions forward. At the end, if the last position we reached is the second last position in the array, it means the last character must be a one-bit character.

{% endraw %}

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
class Solution {
       public:
           bool isOneBitCharacter(vector<int>& bits) {
               int i = 0;
               while (i < bits.size() - 1) {
                   if (bits[i] == 0) {
                       i++;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.size() - 1;
           }
       };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
           public boolean isOneBitCharacter(int[] bits) {
               int i = 0;
               while (i < bits.length - 1) {
                   if (bits[i] == 0) {
                       i++;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.length - 1;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
           def isOneBitCharacter(self, bits: List[int]) -> bool:
               i = 0
               while i < len(bits) - 1:
                   if bits[i] == 0:
                       i += 1
                   else:
                       i += 2
               return i == len(bits) - 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
           def isOneBitCharacter(self, bits: List[int]) -> bool:
               i = 0
               while i < len(bits) - 1:
                   if bits[i] == 0:
                       i += 1
                   else:
                       i += 2
               return i == len(bits) - 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool isOneBitCharacter(int* bits, int bitsSize) {
           int i = 0;
           while (i < bitsSize - 1) {
               if (bits[i] == 0) {
                   i++;
               } else {
                   i += 2;
               }
           }
           return i == bitsSize - 1;
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
           public bool IsOneBitCharacter(int[] bits) {
               int i = 0;
               while (i < bits.Length - 1) {
                   if (bits[i] == 0) {
                       i++;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.Length - 1;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var isOneBitCharacter = function(bits) {
           let i = 0;
           while (i < bits.length - 1) {
               if (bits[i] == 0) {
                   i++;
               } else {
                   i += 2;
               }
           }
           return i == bits.length - 1;
       };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isOneBitCharacter(bits: number[]): boolean {
           let i: number = 0;
           while (i < bits.length - 1) {
               if (bits[i] == 0) {
                   i++;
               } else {
                   i += 2;
               }
           }
           return i == bits.length - 1;
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
           function isOneBitCharacter($bits) {
               $i = 0;
               while ($i < count($bits) - 1) {
                   if ($bits[$i] == 0) {
                       $i++;
                   } else {
                       $i += 2;
                   }
               }
               return $i == count($bits) - 1;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
           func isOneBitCharacter(_ bits: [Int]) -> Bool {
               var i = 0
               while i < bits.count - 1 {
                   if bits[i] == 0 {
                       i += 1
                   } else {
                       i += 2
                   }
               }
               return i == bits.count - 1
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
           fun isOneBitCharacter(bits: IntArray): Boolean {
               var i = 0
               while (i < bits.size - 1) {
                   if (bits[i] == 0) {
                       i++
                   } else {
                       i += 2
                   }
               }
               return i == bits.size - 1
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
           bool isOneBitCharacter(List<int> bits) {
               int i = 0;
               while (i < bits.length - 1) {
                   if (bits[i] == 0) {
                       i++;
                   } else {
                       i += 2;
                   }
               }
               return i == bits.length - 1;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isOneBitCharacter(bits []int) bool {
           i := 0
           for i < len(bits)-1 {
               if bits[i] == 0 {
                   i++
               } else {
                   i += 2
               }
           }
           return i == len(bits)-1
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} bits
       # @return {Boolean}
       def is_one_bit_character(bits)
           i = 0
           while i < bits.size - 1
               if bits[i] == 0
                   i += 1
               else
                   i += 2
               end
           end
           i == bits.size - 1
       end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
           def isOneBitCharacter(bits: Array[Int]): Boolean = {
               var i = 0
               while (i < bits.length - 1) {
                   if (bits(i) == 0) {
                       i += 1
                   } else {
                       i += 2
                   }
               }
               i == bits.length - 1
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
           pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
               let mut i = 0;
               while i < bits.len() - 1 {
                   if bits[i] == 0 {
                       i += 1;
                   } else {
                       i += 2;
                   }
               }
               i == bits.len() - 1
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
       (define (is-one-bit-character bits)
           (let loop ((i 0))
               (cond
                   ((>= i (sub1 (length bits))) (= i (sub1 (length bits))))
                   ((= (list-ref bits i) 0) (loop (add1 i)))
                   (else (loop (+ i 2))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
       -export([is_one_bit_character/1]).
       is_one_bit_character(Bits) ->
           is_one_bit_character(Bits, 0).
       is_one_bit_character([0 | Rest], I) ->
           is_one_bit_character(Rest, I + 1);
       is_one_bit_character([1, _ | Rest], I) ->
           is_one_bit_character(Rest, I + 2);
       is_one_bit_character([], I) ->
           I == length([]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
           def is_one_bit_character(bits) do
               is_one_bit_character(bits, 0)
           end

           defp is_one_bit_character([0 | rest], i) do
               is_one_bit_character(rest, i + 1)
           end

           defp is_one_bit_character([1, _ | rest], i) do
               is_one_bit_character(rest, i + 2)
           end

           defp is_one_bit_character([], i) do
               i == length([])
           end
       end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of bits in the array, because we are scanning the array once.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the current position and the result.

</div>
</details>
