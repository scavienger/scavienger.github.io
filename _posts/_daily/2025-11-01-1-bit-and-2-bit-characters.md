---
layout: post
title: 1-bit and 2-bit Characters
date: "2025-11-01 09:00:00 +0900"
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: "https://leetcode.com/problems/1-bit-and-2-bit-characters/"
---
## Problem #717: 1-bit and 2-bit Characters

**Difficulty:** Easy

**Topics:** Array

## Problem Description

We have two special characters:

  * The first character can be represented by one bit `0`.
  * The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

**Example 1:**

``` Input: bits = [1,0,0] Output: true Explanation: The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character. ``` 

**Example 2:**

``` Input: bits = [1,1,1,0] Output: false Explanation: The only way to decode it is two-bit character and two-bit character. So the last character is not one-bit character. ``` 

**Constraints:**

  * `1 <= bits.length <= 1000`
  * `bits[i]` is either `0` or `1`.

## Hints

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-19 22:40:31)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to determine if the last character in a given binary array `bits` must be a one-bit character. We are given two special character types: a one-bit character represented by `0`, and a two-bit character represented by `10` or `11`. A crucial piece of information is that the input array `bits` always ends with `0`. The decoding process is deterministic: if we encounter a `0`, it's a one-bit character; if we encounter a `1`, it's the start of a two-bit character. This deterministic nature allows us to process the array sequentially from left to right.

The core idea is to simulate the decoding process by iterating through the `bits` array using a pointer, say `i`. We advance `i` based on the character type we decode. If `bits[i]` is `0`, we have decoded a one-bit character, so we increment `i` by `1`. If `bits[i]` is `1`, we have decoded a two-bit character, which means `bits[i]` and `bits[i+1]` form a single character. In this case, we increment `i` by `2`. We continue this process until we are ready to consider the last bit of the array.

The key to solving this problem lies in where we stop our iteration. We are interested in whether the very last `0` in the `bits` array forms a one-bit character by itself. This means we want to see if our decoding process *lands* exactly on the index `len(bits) - 1`. If our pointer `i` is less than `len(bits) - 1`, we continue decoding. Once `i` reaches `len(bits) - 1` (meaning we've potentially processed all characters *before* the last bit, and the last bit `bits[len(bits)-1]` is still to be processed), or `i` exceeds `len(bits) - 1` (meaning the last bit was consumed as part of a two-bit character), our loop terminates. After the loop, we simply check the final value of `i`. If `i` is exactly `len(bits) - 1`, it implies that the last `0` was not part of any preceding two-bit character and hence must be a one-bit character. If `i` is `len(bits)`, it implies that a two-bit character consumed both `bits[len(bits)-2]` and `bits[len(bits)-1]`, meaning the last `0` was the second bit of a two-bit character.

Let's walk through the algorithm with an example: `bits = [1,0,0]`. The length `n` is 3. We initialize `i = 0`. The loop condition is `i < n - 1` (i.e., `i < 2`).
1.  `i = 0`. `0 < 2` is true. `bits[0]` is `1`. This is a two-bit character. We increment `i` by `2`, so `i` becomes `2`.
2.  `i = 2`. `2 < 2` is false. The loop terminates.
After the loop, `i` is `2`. We check if `i == n - 1` (i.e., `2 == 2`). This is true. Therefore, the last character is a one-bit character, and we return `true`. This correctly decodes as `10` (two-bit) followed by `0` (one-bit).

Consider another example: `bits = [1,1,1,0]`. The length `n` is 4. We initialize `i = 0`. The loop condition is `i < n - 1` (i.e., `i < 3`).
1.  `i = 0`. `0 < 3` is true. `bits[0]` is `1`. Two-bit character. `i` becomes `2`.
2.  `i = 2`. `2 < 3` is true. `bits[2]` is `1`. Two-bit character. `i` becomes `4`.
3.  `i = 4`. `4 < 3` is false. The loop terminates.
After the loop, `i` is `4`. We check if `i == n - 1` (i.e., `4 == 3`). This is false. Therefore, the last character is not a one-bit character, and we return `false`. This correctly decodes as `11` (two-bit) followed by `10` (two-bit). The final `0` was part of the `10` two-bit character.

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
class Solution {
public:
    bool isOneBitCharacter(std::vector<int>& bits) {
        int i = 0;
        int n = bits.size();

        while (i < n - 1) {
            if (bits[i] == 1) {
                i += 2;
            } else { // bits[i] == 0
                i += 1;
            }
        }

        return i == n - 1;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        int n = bits.length;

        while (i < n - 1) {
            if (bits[i] == 1) {
                i += 2;
            } else { // bits[i] == 0
                i += 1;
            }
        }

        return i == n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:  # bits[i] == 0
                i += 1

        return i == n - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:  # bits[i] == 0
                i += 1

        return i == n - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
bool isOneBitCharacter(int* bits, int bitsSize) {
    int i = 0;

    while (i < bitsSize - 1) {
        if (bits[i] == 1) {
            i += 2;
        } else { // bits[i] == 0
            i += 1;
        }
    }

    return i == bitsSize - 1;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int i = 0;
        int n = bits.Length;

        while (i < n - 1) {
            if (bits[i] == 1) {
                i += 2;
            } else { // bits[i] == 0
                i += 1;
            }
        }

        return i == n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    let i = 0;
    const n = bits.length;

    while (i < n - 1) {
        if (bits[i] === 1) {
            i += 2;
        } else { // bits[i] === 0
            i += 1;
        }
    }

    return i === n - 1;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function isOneBitCharacter(bits: number[]): boolean {
    let i: number = 0;
    const n: number = bits.length;

    while (i < n - 1) {
        if (bits[i] === 1) {
            i += 2;
        } else { // bits[i] === 0
            i += 1;
        }
    }

    return i === n - 1;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits) {
        $i = 0;
        $n = count($bits);

        while ($i < $n - 1) {
            if ($bits[$i] == 1) {
                $i += 2;
            } else { // $bits[$i] == 0
                $i += 1;
            }
        }

        return $i == $n - 1;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        var i = 0
        let n = bits.count

        while i < n - 1 {
            if bits[i] == 1 {
                i += 2
            } else { // bits[i] == 0
                i += 1
            }
        }

        return i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        var i = 0
        val n = bits.size

        while (i < n - 1) {
            if (bits[i] == 1) {
                i += 2
            } else { // bits[i] == 0
                i += 1
            }
        }

        return i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  bool isOneBitCharacter(List<int> bits) {
    int i = 0;
    int n = bits.length;

    while (i < n - 1) {
      if (bits[i] == 1) {
        i += 2;
      } else { // bits[i] == 0
        i += 1;
      }
    }

    return i == n - 1;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func isOneBitCharacter(bits []int) bool {
    i := 0
    n := len(bits)

    for i < n - 1 {
        if bits[i] == 1 {
            i += 2
        } else { // bits[i] == 0
            i += 1
        }
    }

    return i == n - 1
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
class Solution
    # @param {Integer[]} bits
    # @return {Boolean}
    def is_one_bit_character(bits)
        i = 0
        n = bits.length

        while i < n - 1
            if bits[i] == 1
                i += 2
            else # bits[i] == 0
                i += 1
            end
        end

        return i == n - 1
    end
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        var i = 0
        val n = bits.length

        while (i < n - 1) {
            if (bits(i) == 1) {
                i += 2
            } else { // bits(i) == 0
                i += 1
            }
        }

        i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        let n = bits.len();

        while i < n - 1 {
            if bits[i] == 1 {
                i += 2;
            } else { // bits[i] == 0
                i += 1;
            }
        }

        i == n - 1
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
(define/contract (is-one-bit-character bits)
  (-> (list/c exact-integer?) boolean?)
  (let ([n (length bits)])
    (let loop ([i 0])
      (cond
        [(< i (- n 1))
         (if (= (list-ref bits i) 1)
             (loop (+ i 2))
             (loop (+ i 1)))]
        [else
         (= i (- n 1))]))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([is_one_bit_character/1]).

is_one_bit_character(Bits) ->
    N = length(Bits),
    is_one_bit_character_recursive(Bits, 0, N).

is_one_bit_character_recursive(_Bits, I, N) when I >= N - 1 ->
    I == N - 1;
is_one_bit_character_recursive(Bits, I, N) ->
    case lists:nth(I + 1, Bits) of % lists:nth is 1-indexed
        1 -> is_one_bit_character_recursive(Bits, I + 2, N);
        0 -> is_one_bit_character_recursive(Bits, I + 1, N)
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec is_one_bit_character(bits :: [integer]) :: boolean
  def is_one_bit_character(bits) do
    n = length(bits)
    is_one_bit_character_recursive(bits, 0, n)
  end

  defp is_one_bit_character_recursive(_bits, i, n) when i >= n - 1 do
    i == n - 1
  end

  defp is_one_bit_character_recursive(bits, i, n) do
    case Enum.at(bits, i) do
      1 -> is_one_bit_character_recursive(bits, i + 2, n)
      0 -> is_one_bit_character_recursive(bits, i + 1, n)
    end
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-19 22:40:35)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a simple iterative approach. We start from the beginning of the array and keep track of the current index. If the current bit is 0, we move one step forward. If the current bit is 1, we move two steps forward because it must be followed by another bit. At the end, we check if the last character is a one-bit character by checking if the index is at the second last position.

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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
           def isOneBitCharacter(self, bits: List[int]) -> bool:
               i = 0
               while i < len(bits) - 1:
                   if bits[i] == 0:
                       i += 1
                   else:
                       i += 2
               return i == len(bits) - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def isOneBitCharacter(self, bits: List[int]) -> bool:
               i = 0
               while i < len(bits) - 1:
                   if bits[i] == 0:
                       i += 1
                   else:
                       i += 2
               return i == len(bits) - 1
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
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
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
       (define (is-one-bit-character bits)
           (let loop ((i 0))
               (cond
                   ((>= i (sub1 (length bits))) (= i (sub1 (length bits))))
                   ((= (list-ref bits i) 0) (loop (add1 i)))
                   (else (loop (+ i 2))))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([is_one_bit_character/1]).
       is_one_bit_character(Bits) ->
           is_one_bit_character(Bits, 0).
       is_one_bit_character([0 | Rest], I) ->
           is_one_bit_character(Rest, I + 1);
       is_one_bit_character([1, _ | Rest], I) ->
           is_one_bit_character(Rest, I + 2);
       is_one_bit_character([], I) ->
           I == 0.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
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
               i == length([]) - 1
           end
       end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of bits in the array, because we are scanning the array once.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the index and the result.

</div>
</details>
