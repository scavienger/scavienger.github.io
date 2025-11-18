---
layout: post
title: "1-bit and 2-bit Characters"
date: 2025-11-01 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/1-bit-and-2-bit-characters/
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


<details open>
<summary><strong>⚡ Solution from llama-3.3-70b-versatile</strong></summary>

### Approach

The problem can be solved by iterating over the binary array and keeping track of the current position. We start from the beginning of the array and move forward based on the current bit. If the current bit is 0, we move one step forward. If the current bit is 1, we move two steps forward because it must be part of a two-bit character. We continue this process until we reach the end of the array. If the last character we encounter is a one-bit character (i.e., we end at the second last position), we return true. Otherwise, we return false.

### Code

<div class="code-tabs">
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
                           i += 1;
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
                       i += 1;
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
           def isOneBitCharacter(self, bits: list[int]) -> bool:
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
           def isOneBitCharacter(self, bits: list[int]) -> bool:
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
                   i += 1;
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
                       i += 1;
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
                   i += 1;
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
                   i += 1;
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
                       $i += 1;
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
                       i += 1
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
                       i += 1;
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
                   i += 1
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
               i == 0
           end
       end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of bits in the array. This is because we are scanning the array once.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the current position and the result.

</details>
