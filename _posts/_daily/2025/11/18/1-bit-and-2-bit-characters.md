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


## Hints

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 04:03:51 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to determine if the last character in a given binary array `bits` must be a one-bit character. We are given two types of characters: a one-bit character represented by `0`, and a two-bit character represented by `10` or `11`. A crucial constraint is that the input array `bits` always ends with `0`. This simplifies the problem as we don't need to consider cases where the array ends with an incomplete two-bit character (e.g., ending with `1`).

We can solve this problem by simulating the decoding process from left to right. We maintain an index `i` that points to the beginning of the current character we are trying to decode. We iterate through the `bits` array, advancing `i` based on the character type. If `bits[i]` is `0`, it represents a one-bit character, so we advance `i` by `1`. If `bits[i]` is `1`, it must represent the start of a two-bit character (either `10` or `11`), so we advance `i` by `2` (consuming `bits[i]` and `bits[i+1]`).

The loop continues as long as `i` is less than `n-1`, where `n` is the total length of the `bits` array. This means we stop when `i` points to the second-to-last element or beyond. After the loop terminates, we check the final value of `i`. If `i` is exactly equal to `n-1`, it means the character starting at `n-1` (which must be `0` according to the problem constraints) was decoded as a one-bit character. In this scenario, the last character is a one-bit character, and we return `true`. If `i` is equal to `n` (meaning it has gone past the end of the array), it implies that the character starting at `n-2` was a two-bit character (`10`), consuming `bits[n-2]` and `bits[n-1]`. In this case, the last character was a two-bit character, and we return `false`.

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
        int n = bits.size();
        int i = 0;
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        return i == n - 1;
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
        int n = bits.length;
        int i = 0;
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        return i == n - 1;
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
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else: # bits[i] == 1
                i += 2
        return i == n - 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else: # bits[i] == 1
                i += 2
        return i == n - 1
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
            i += 1;
        } else { // bits[i] == 1
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
        int n = bits.Length;
        int i = 0;
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        return i == n - 1;
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
    let n = bits.length;
    let i = 0;
    while (i < n - 1) {
        if (bits[i] === 0) {
            i += 1;
        } else { // bits[i] === 1
            i += 2;
        }
    }
    return i === n - 1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isOneBitCharacter(bits: number[]): boolean {
    let n: number = bits.length;
    let i: number = 0;
    while (i < n - 1) {
        if (bits[i] === 0) {
            i += 1;
        } else { // bits[i] === 1
            i += 2;
        }
    }
    return i === n - 1;
}
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
    function isOneBitCharacter($bits) {
        $n = count($bits);
        $i = 0;
        while ($i < $n - 1) {
            if ($bits[$i] == 0) {
                $i += 1;
            } else { // $bits[$i] == 1
                $i += 2;
            }
        }
        return $i == $n - 1;
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
        let n = bits.count
        var i = 0
        while i < n - 1 {
            if bits[i] == 0 {
                i += 1
            } else { // bits[i] == 1
                i += 2
            }
        }
        return i == n - 1
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
        val n = bits.size
        var i = 0
        while (i < n - 1) {
            if (bits[i] == 0) {
                i += 1
            } else { // bits[i] == 1
                i += 2
            }
        }
        return i == n - 1
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
    int n = bits.length;
    int i = 0;
    while (i < n - 1) {
      if (bits[i] == 0) {
        i += 1;
      } else { // bits[i] == 1
        i += 2;
      }
    }
    return i == n - 1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isOneBitCharacter(bits []int) bool {
    n := len(bits)
    i := 0
    for i < n - 1 {
        if bits[i] == 0 {
            i += 1
        } else { // bits[i] == 1
            i += 2
        }
    }
    return i == n - 1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    /**
     * @param {Integer[]} bits
     * @return {Boolean}
     */
    def is_one_bit_character(bits)
        n = bits.length
        i = 0
        while i < n - 1
            if bits[i] == 0
                i += 1
            else # bits[i] == 1
                i += 2
            end
        end
        return i == n - 1
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        val n = bits.length
        var i = 0
        while (i < n - 1) {
            if (bits(i) == 0) {
                i += 1
            } else { // bits(i) == 1
                i += 2
            }
        }
        i == n - 1
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
        let n = bits.len();
        let mut i = 0;
        while i < n - 1 {
            if bits[i] == 0 {
                i += 1;
            } else { // bits[i] == 1
                i += 2;
            }
        }
        i == n - 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (is-one-bit-character bits)
  (-> (listof exact-integer?) boolean?)
  (let* ([n (length bits)]
         [bits-vec (list->vector bits)])
    (let loop ([i 0])
      (cond
        [(>= i (- n 1)) ; If i is at or past the second-to-last element
         (= i (- n 1))] ; Return true if i landed exactly on n-1
        [(zero? (vector-ref bits-vec i))
         (loop (+ i 1))]
        [else ; (vector-ref bits-vec i) is 1
         (loop (+ i 2))]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec is_one_bit_character(Bits :: [0 | 1]) -> boolean().
is_one_bit_character(Bits) ->
    N = length(Bits),
    is_one_bit_character_recursive(Bits, N, 0).

is_one_bit_character_recursive(_Bits, N, I) when I == N - 1 ->
    true;
is_one_bit_character_recursive(_Bits, N, I) when I >= N ->
    false;
is_one_bit_character_recursive(Bits, N, I) ->
    case lists:nth(I + 1, Bits) of % lists:nth is 1-indexed
        0 -> is_one_bit_character_recursive(Bits, N, I + 1);
        1 -> is_one_bit_character_recursive(Bits, N, I + 2)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec is_one_bit_character(bits :: [0 | 1]) :: boolean
  def is_one_bit_character(bits) do
    n = Enum.count(bits)
    do_check(bits, n, 0)
  end

  defp do_check(_bits, n, idx) when idx == n - 1, do: true
  defp do_check(_bits, n, idx) when idx >= n, do: false
  defp do_check(bits, n, idx) do
    case Enum.at(bits, idx) do
      0 -> do_check(bits, n, idx + 1)
      1 -> do_check(bits, n, idx + 2)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with detailed explanation

- **Space Complexity:** O(1) with detailed explanation

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-25 04:03:56 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

Failed to parse AI response

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile" checked>
  <div class="tab-labels">
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Failed to parse response
# Check logs for full output.
# Full Response:
'''
{
  "approach": "The problem can be solved by iterating through the binary array from left to right. We keep track of the index where the next character starts. If the current bit is 0, it represents a one-bit character, so we move to the next index. If the current bit is 1, it represents a two-bit character, so we move two indices forward. At the end, we check if the last character is a one-bit character by checking if the index is at the second last position.",
  
  "The algorithm logic is as follows: we start at the beginning of the array and iterate through it. For each bit, we check if it is 0 or 1. If it is 0, we move to the next index. If it is 1, we move two indices forward because the current bit and the next bit represent a two-bit character. We continue this process until we reach the end of the array. If the last index we visited is the second last index, it means the last character is a one-bit character, so we return True. Otherwise, we return False.",
  
  "The time complexity of this algorithm is O(n), where n is the length of the binary array, because we make a single pass through the array. The space complexity is O(1), because we only use a constant amount of space to store the index and the result.",
  
  "time_complexity": "O(n) where n is the length of the binary array, because we make a single pass through the array.",
  "space_complexity": "O(1) because we only use a constant amount of space to store the index and the result.",
  "solutions": {
    "cpp": "
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
    ",
    "java": "
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
    ",
    "python": "
    class Solution:
        def isOneBitCharacter(self, bits: list[int]) -> bool:
            i = 0
            while i < len(bits) - 1:
                if bits[i] == 0:
                    i += 1
                else:
                    i += 2
            return i == len(bits) - 1
    ",
    "python3": "
    class Solution:
        def isOneBitCharacter(self, bits: list[int]) -> bool:
            i = 0
            while i < len(bits) - 1:
                if bits[i] == 0:
                    i += 1
                else:
                    i += 2
            return i == len(bits) - 1
    ",
    "c": "
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
    ",
    "csharp": "
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
    ",
    "javascript": "
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
    ",
    "typescript": "
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
    ",
    "php": "
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
    ",
    "swift": "
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
    ",
    "kotlin": "
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
    ",
    "dart": "
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
    ",
    "go": "
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
    ",
    "ruby": "
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
    ",
    "scala": "
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
    ",
    "rust": "
    impl Solution {
        pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
            let mut i: usize = 0;
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
    ",
    "racket": "
    #lang racket
    (define (is-one-bit-character bits)
        (let loop ((i 0))
            (cond
                ((>= i (sub1 (length bits))) (= i (sub1 (length bits))))
                ((= (list-ref bits i) 0) (loop (add1 i)))
                (else (loop (+ i 2))))))
    ",
    "erlang": "
    -module(solution).
    -export([is_one_bit_character/1]).
    
    is_one_bit_character(Bits) ->
        is_one_bit_character(Bits, 0).
    
    is_one_bit_character([0 | T], I) ->
        is_one_bit_character(T, I + 1);
    is_one_bit_character([1, _ | T], I) ->
        is_one_bit_character(T, I + 2);
    is_one_bit_character([], I) ->
        I == length([]) - 1.
    ",
    "elixir": "
    defmodule Solution do
        def is_one_bit_character(bits) do
            is_one_bit_character(bits, 0)
        end
        
        defp is_one_bit_character([0 | t], i) do
            is_one_bit_character(t, i + 1)
        end
        
        defp is_one_bit_character([1, _ | t], i) do
            is_one_bit_character(t, i + 2)
        end
        
        defp is_one_bit_character([], i) do
            i == length([]) - 1
        end
    end
    "
  }
}
'''
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
