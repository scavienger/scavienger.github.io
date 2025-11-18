---
layout: post
title: Check If All 1's Are at Least Length K Places Away
date: "2025-11-02 09:00:00 +0900"
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: "https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/"
---
## Problem #1437: Check If All 1's Are at Least Length K Places Away

**Difficulty:** Easy

**Topics:** Array

## Problem Description

Given an binary array `nums` and an integer `k`, return `true` _if all_`1` _'s are at least_`k` _places away from each other, otherwise return_`false`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)

``` Input: nums = [1,0,0,0,1,0,0,1], k = 2 Output: true Explanation: Each of the 1s are at least 2 places away from each other. ``` 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)

``` Input: nums = [1,0,0,1,0,1], k = 2 Output: false Explanation: The second 1 and third 1 are only one apart from each other. ``` 

**Constraints:**

  * `1 <= nums.length <= 105`
  * `0 <= k <= nums.length`
  * `nums[i]` is `0` or `1`

### Illustrations

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)

## Hints

1. Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details open>
<summary><strong>✨ Solution from gemini-2.5-flash</strong></summary>

### Approach

The problem requires us to verify if all '1's in a given binary array `nums` are separated by at least `k` places. This means if we find a '1' at index `i` and the next '1' at index `j`, there must be at least `k` zeros strictly between them. Mathematically, this translates to `j - i - 1 >= k`.

Our approach involves a single pass through the array, keeping track of the count of zeros since the last '1' was encountered. To handle the initial state and edge cases correctly, we use two variables: `zero_count` and `found_first_one`. `zero_count` will keep track of how many zeros we've seen since the most recent '1'. `found_first_one` is a boolean flag that helps us know if we've already encountered at least one '1' in the array.

Initially, `zero_count` is set to `k`. This seemingly arbitrary initial value is crucial. If the very first element of `nums` is '1', we don't have a previous '1' to compare it against, so the distance condition is vacuously true for it. By initializing `zero_count` to `k` (or any value greater than or equal to `k`), when the first '1' is encountered, the check `zero_count < k` will evaluate to `false`, thus not triggering an premature `false` return. `found_first_one` is initialized to `false` because we haven't seen any '1's yet.

As we iterate through the `nums` array element by element: if the current element is a '1':
1. We first check `found_first_one`. If it's `true`, it means this is not the first '1' in the array, and we must check the distance from the previous '1'. We compare `zero_count` with `k`. If `zero_count` is less than `k`, it signifies that there are fewer than `k` zeros separating this '1' from the previous one, violating the problem's condition. In this scenario, we immediately return `false`.
2. After the check (or if `found_first_one` was `false`), we set `found_first_one` to `true` because we have now definitely encountered at least one '1'.
3. Finally, we reset `zero_count` to `0`. This is because we just found a '1', and any subsequent zeros will be counted starting from this point.

If the current element is a '0': we only care about counting zeros if we've already found at least one '1'. So, if `found_first_one` is `true`, we simply increment `zero_count`. If `found_first_one` is `false`, we do nothing, as these zeros are before the first relevant '1'. If the loop completes without returning `false`, it means all '1's adhere to the `k`-length separation requirement, or there were no '1's at all, so we return `true`.

### Code

<div class="code-tabs">
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
    bool kLengthApart(std::vector<int>& nums, int k) {
        int zeroCount = k;
        bool foundFirstOne = false;

        for (int num : nums) {
            if (num == 1) {
                if (foundFirstOne) {
                    if (zeroCount < k) {
                        return false;
                    }
                }
                foundFirstOne = true;
                zeroCount = 0;
            } else {
                if (foundFirstOne) {
                    zeroCount++;
                }
            }
        }

        return true;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int zeroCount = k;
        boolean foundFirstOne = false;

        for (int num : nums) {
            if (num == 1) {
                if (foundFirstOne) {
                    if (zeroCount < k) {
                        return false;
                    }
                }
                foundFirstOne = true;
                zeroCount = 0;
            } else {
                if (foundFirstOne) {
                    zeroCount++;
                }
            }
        }

        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zero_count = k
        found_first_one = False

        for num in nums:
            if num == 1:
                if found_first_one:
                    if zero_count < k:
                        return False
                
                found_first_one = True
                zero_count = 0
            else: # num == 0
                if found_first_one:
                    zero_count += 1
        
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zero_count = k
        found_first_one = False

        for num in nums:
            if num == 1:
                if found_first_one:
                    if zero_count < k:
                        return False
                
                found_first_one = True
                zero_count = 0
            else: # num == 0
                if found_first_one:
                    zero_count += 1
        
        return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>

bool kLengthApart(int* nums, int numsSize, int k) {
    int zeroCount = k;
    bool foundFirstOne = false;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            if (foundFirstOne) {
                if (zeroCount < k) {
                    return false;
                }
            }
            foundFirstOne = true;
            zeroCount = 0;
        } else {
            if (foundFirstOne) {
                zeroCount++;
            }
        }
    }

    return true;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int zeroCount = k;
        bool foundFirstOne = false;

        foreach (int num in nums) {
            if (num == 1) {
                if (foundFirstOne) {
                    if (zeroCount < k) {
                        return false;
                    }
                }
                foundFirstOne = true;
                zeroCount = 0;
            } else {
                if (foundFirstOne) {
                    zeroCount++;
                }
            }
        }

        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    let zeroCount = k;
    let foundFirstOne = false;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (foundFirstOne) {
                if (zeroCount < k) {
                    return false;
                }
            }
            foundFirstOne = true;
            zeroCount = 0;
        } else { // nums[i] === 0
            if (foundFirstOne) {
                zeroCount++;
            }
        }
    }

    return true;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function kLengthApart(nums: number[], k: number): boolean {
    let zeroCount: number = k;
    let foundFirstOne: boolean = false;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (foundFirstOne) {
                if (zeroCount < k) {
                    return false;
                }
            }
            foundFirstOne = true;
            zeroCount = 0;
        } else { // nums[i] === 0
            if (foundFirstOne) {
                zeroCount++;
            }
        }
    }

    return true;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        $zeroCount = $k;
        $foundFirstOne = false;

        foreach ($nums as $num) {
            if ($num === 1) {
                if ($foundFirstOne) {
                    if ($zeroCount < $k) {
                        return false;
                    }
                }
                $foundFirstOne = true;
                $zeroCount = 0;
            } else { // $num === 0
                if ($foundFirstOne) {
                    $zeroCount++;
                }
            }
        }

        return true;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var zeroCount = k
        var foundFirstOne = false

        for num in nums {
            if num == 1 {
                if foundFirstOne {
                    if zeroCount < k {
                        return false
                    }
                }
                foundFirstOne = true
                zeroCount = 0
            } else { // num == 0
                if foundFirstOne {
                    zeroCount += 1
                }
            }
        }

        return true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var zeroCount = k
        var foundFirstOne = false

        for (num in nums) {
            if (num == 1) {
                if (foundFirstOne) {
                    if (zeroCount < k) {
                        return false
                    }
                }
                foundFirstOne = true
                zeroCount = 0
            } else { // num == 0
                if (foundFirstOne) {
                    zeroCount++
                }
            }
        }

        return true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
  bool kLengthApart(List<int> nums, int k) {
    int zeroCount = k;
    bool foundFirstOne = false;

    for (int num in nums) {
      if (num == 1) {
        if (foundFirstOne) {
          if (zeroCount < k) {
            return false;
          }
        }
        foundFirstOne = true;
        zeroCount = 0;
      } else { // num == 0
        if (foundFirstOne) {
          zeroCount++;
        }
      }
    }

    return true;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func kLengthApart(nums []int, k int) bool {
    zeroCount := k
    foundFirstOne := false

    for _, num := range nums {
        if num == 1 {
            if foundFirstOne {
                if zeroCount < k {
                    return false
                }
            }
            foundFirstOne = true
            zeroCount = 0
        } else { // num == 0
            if foundFirstOne {
                zeroCount++
            }
        }
    }

    return true
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
def k_length_apart(nums, k)
    zero_count = k
    found_first_one = false

    nums.each do |num|
        if num == 1
            if found_first_one
                return false if zero_count < k
            end
            found_first_one = true
            zero_count = 0
        else # num == 0
            zero_count += 1 if found_first_one
        end
    end

    true
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var zeroCount = k
        var foundFirstOne = false

        for (num <- nums) {
            if (num == 1) {
                if (foundFirstOne) {
                    if (zeroCount < k) {
                        return false
                    }
                }
                foundFirstOne = true
                zeroCount = 0
            } else { // num == 0
                if (foundFirstOne) {
                    zeroCount += 1
                }
            }
        }

        true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut zero_count = k;
        let mut found_first_one = false;

        for num in nums {
            if num == 1 {
                if found_first_one {
                    if zero_count < k {
                        return false;
                    }
                }
                found_first_one = true;
                zero_count = 0;
            } else { // num == 0
                if found_first_one {
                    zero_count += 1;
                }
            }
        }

        true
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
(define/contract (k-length-apart nums k)
  (-> (listof integer?) integer? boolean?)
  (let loop ((nums nums)
             (zero-count k)
             (found-first-one #f))
    (cond
      ((empty? nums) #t)
      ((= (car nums) 1)
       (if found-first-one
           (if (< zero-count k)
               #f ; Condition violated
               (loop (cdr nums) 0 #t))
           (loop (cdr nums) 0 #t))) ; First 1, reset count, set flag
      (else ; (= (car nums) 0)
       (if found-first-one
           (loop (cdr nums) (+ zero-count 1) found-first-one)
           (loop (cdr nums) zero-count found-first-one))))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([k_length_apart/2]).

k_length_apart(Nums, K) ->
    k_length_apart_impl(Nums, K, K, false).

k_length_apart_impl([], _K, _ZeroCount, _FoundFirstOne) ->
    true;

k_length_apart_impl([1 | Rest], K, ZeroCount, FoundFirstOne) ->
    if
        FoundFirstOne andalso (ZeroCount < K) ->
            false;
        true ->
            k_length_apart_impl(Rest, K, 0, true)
    end;

k_length_apart_impl([0 | Rest], K, ZeroCount, FoundFirstOne) ->
    if
        FoundFirstOne ->
            k_length_apart_impl(Rest, K, ZeroCount + 1, FoundFirstOne);
        true ->
            k_length_apart_impl(Rest, K, ZeroCount, FoundFirstOne)
    end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    do_k_length_apart(nums, k, k, false)
  end

  defp do_k_length_apart([], _k, _zero_count, _found_first_one), do: true

  defp do_k_length_apart([1 | rest], k, zero_count, found_first_one) do
    if found_first_one && zero_count < k do
      false
    else
      do_k_length_apart(rest, k, 0, true)
    end
  end

  defp do_k_length_apart([0 | rest], k, zero_count, found_first_one) do
    if found_first_one do
      do_k_length_apart(rest, k, zero_count + 1, found_first_one)
    else
      do_k_length_apart(rest, k, zero_count, found_first_one)
    end
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the `nums` array. The algorithm iterates through the array exactly once, performing a constant number of operations (comparisons, assignments, increments) for each element. Thus, the execution time grows linearly with the input size.

- **Space Complexity:** O(1). The algorithm uses a fixed number of auxiliary variables (`zero_count` and `found_first_one`) regardless of the input array's size. No additional data structures are allocated that depend on N.

</details>


<details>
<summary><strong>⚡ Solution from llama-3.3-70b-versatile</strong></summary>

### Approach

The problem can be solved by iterating over the given binary array and checking the distance between each pair of 1's. We can use a variable to keep track of the position of the last 1 encountered. If the distance between the current 1 and the last 1 is less than k, we return false. If we finish iterating over the array without finding any pair of 1's that are less than k places apart, we return true.

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
#include <vector>
       class Solution {
       public:
           bool kLengthApart(std::vector<int>& nums, int k) {
               int lastOne = -1;
               for (int i = 0; i < nums.size(); i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
                   }
               }
               return true;
           }
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
           public boolean kLengthApart(int[] nums, int k) {
               int lastOne = -1;
               for (int i = 0; i < nums.length; i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
                   }
               }
               return true;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
           def kLengthApart(self, nums: list[int], k: int) -> bool:
               lastOne = -1
               for i in range(len(nums)):
                   if nums[i] == 1:
                       if lastOne != -1 and i - lastOne - 1 < k:
                           return False
                       lastOne = i
               return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def kLengthApart(self, nums: list[int], k: int) -> bool:
               lastOne = -1
               for i in range(len(nums)):
                   if nums[i] == 1:
                       if lastOne != -1 and i - lastOne - 1 < k:
                           return False
                       lastOne = i
               return True
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdbool.h>
       bool kLengthApart(int* nums, int numsSize, int k) {
           int lastOne = -1;
           for (int i = 0; i < numsSize; i++) {
               if (nums[i] == 1) {
                   if (lastOne != -1 && i - lastOne - 1 < k) {
                       return false;
                   }
                   lastOne = i;
               }
           }
           return true;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
           public bool KLengthApart(int[] nums, int k) {
               int lastOne = -1;
               for (int i = 0; i < nums.Length; i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
                   }
               }
               return true;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var kLengthApart = function(nums, k) {
           let lastOne = -1;
           for (let i = 0; i < nums.length; i++) {
               if (nums[i] == 1) {
                   if (lastOne != -1 && i - lastOne - 1 < k) {
                       return false;
                   }
                   lastOne = i;
               }
           }
           return true;
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function kLengthApart(nums: number[], k: number): boolean {
           let lastOne: number = -1;
           for (let i: number = 0; i < nums.length; i++) {
               if (nums[i] == 1) {
                   if (lastOne != -1 && i - lastOne - 1 < k) {
                       return false;
                   }
                   lastOne = i;
               }
           }
           return true;
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
           function kLengthApart($nums, $k) {
               $lastOne = -1;
               for ($i = 0; $i < count($nums); $i++) {
                   if ($nums[$i] == 1) {
                       if ($lastOne != -1 && $i - $lastOne - 1 < $k) {
                           return false;
                       }
                       $lastOne = $i;
                   }
               }
               return true;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
           func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
               var lastOne: Int = -1
               for i in 0..<nums.count {
                   if nums[i] == 1 {
                       if lastOne != -1 && i - lastOne - 1 < k {
                           return false
                       }
                       lastOne = i
                   }
               }
               return true
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
           fun kLengthApart(nums: IntArray, k: Int): Boolean {
               var lastOne: Int = -1
               for (i in nums.indices) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false
                       }
                       lastOne = i
                   }
               }
               return true
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
           bool kLengthApart(List<int> nums, int k) {
               int lastOne = -1;
               for (int i = 0; i < nums.length; i++) {
                   if (nums[i] == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false;
                       }
                       lastOne = i;
                   }
               }
               return true;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func kLengthApart(nums []int, k int) bool {
           lastOne := -1
           for i := 0; i < len(nums); i++ {
               if nums[i] == 1 {
                   if lastOne != -1 && i-lastOne-1 < k {
                       return false
                   }
                   lastOne = i
               }
           }
           return true
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer[]} nums
       # @param {Integer} k
       # @return {Boolean}
       def k_length_apart(nums, k)
           last_one = -1
           nums.each_with_index do |num, i|
               if num == 1
                   if last_one != -1 && i - last_one - 1 < k
                       return false
                   end
                   last_one = i
               end
           end
           true
       end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
           def kLengthApart(nums: Array[Int], k: Int): Boolean = {
               var lastOne: Int = -1
               for (i <- nums.indices) {
                   if (nums(i) == 1) {
                       if (lastOne != -1 && i - lastOne - 1 < k) {
                           return false
                       }
                       lastOne = i
                   }
               }
               true
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
           pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
               let mut last_one: i32 = -1;
               for (i, &num) in nums.iter().enumerate() {
                   if num == 1 {
                       if last_one != -1 && i as i32 - last_one - 1 < k {
                           return false;
                       }
                       last_one = i as i32;
                   }
               }
               true
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
       (define (k-length-apart nums k)
           (let loop ((nums nums) (last-one -1))
             (cond
               ((null? nums) #t)
               ((= (car nums) 1)
                (if (and (not (= last-one -1)) (< (- (length nums) last-one -1) k))
                    #f
                    (loop (cdr nums) (- (length nums) (length (cdr nums))))))
               (else (loop (cdr nums) last-one)))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([k_length_apart/2]).
       k_length_apart(Nums, K) ->
           k_length_apart(Nums, K, -1).
       k_length_apart([], _, _) ->
           true;
       k_length_apart([1|T], K, -1) ->
           k_length_apart(T, K, 0);
       k_length_apart([1|T], K, LastOne) ->
           case (length(T) + LastOne) < K of
               true -> false;
               false -> k_length_apart(T, K, 0)
           end;
       k_length_apart([_|T], K, LastOne) ->
           k_length_apart(T, K, LastOne).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def k_length_apart(nums, k) do
               k_length_apart(nums, k, -1)
           end

           defp k_length_apart([], _, _), do: true
           defp k_length_apart([1|t], k, -1), do: k_length_apart(t, k, 0)
           defp k_length_apart([1|t], k, last_one) when length(t) + last_one < k, do: false
           defp k_length_apart([1|t], k, _), do: k_length_apart(t, k, 0)
           defp k_length_apart([_|t], k, last_one), do: k_length_apart(t, k, last_one)
       end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array, because we are doing a single pass over the array.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the position of the last 1 and the current index.

</details>
