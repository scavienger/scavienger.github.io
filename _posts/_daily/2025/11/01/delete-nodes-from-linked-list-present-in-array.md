---
layout: post
title: "Delete Nodes From Linked List Present in Array"
date: 2025-11-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Linked List"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
---

## Problem #3217: Delete Nodes From Linked List Present in Array

**Difficulty:** Medium

**Topics:** Array, Hash Table, Linked List

## Problem Description

<p>You are given an array of integers <code>nums</code> and the <code>head</code> of a linked list. Return the <code>head</code> of the modified linked list after <strong>removing</strong> all nodes from the linked list that have a value that exists in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3], head = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,5]</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png" style="width: 400px; height: 66px;" /></strong></p>

<p>Remove the nodes with values 1, 2, and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1], head = [1,2,1,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png" style="height: 62px; width: 450px;" /></p>

<p>Remove the nodes with value 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5], head = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,3,4]</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png" style="width: 400px; height: 83px;" /></strong></p>

<p>No node has value 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li>All elements in <code>nums</code> are unique.</li>
	<li>The number of nodes in the given list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>The input is generated such that there is at least one node in the linked list that has a value not present in <code>nums</code>.</li>
</ul>


## Hints

1. Add all elements of `nums` into a Set.

2. Scan the list to check if the current element should be deleted by checking the Set.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 22:27:47 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to remove all nodes from a given linked list whose values are present in an input array `nums`. We need to return the head of the modified linked list.

The core challenge is efficiently determining if a node's value exists in the `nums` array. A naive approach would be to iterate through `nums` for each node in the linked list, which would lead to a time complexity of O(N*M), where N is the number of nodes in the list and M is the length of `nums`. Given that both N and M can be up to 10^5, N*M could be 10^10, which is too slow.

To optimize the lookup, we can use a hash set (also known as a hash table, `HashSet` in Java/C#, `set` in Python, `unordered_set` in C++, `Map` or `Set` in JavaScript/TypeScript/Go/Kotlin/Swift, etc.). By first converting all elements of `nums` into a hash set, we can check for the existence of any value in O(1) average time. This pre-processing step takes O(M) time.

Once we have the hash set, we traverse the linked list. During traversal, we need to handle node deletions. Deleting a node in a singly linked list requires modifying the `next` pointer of the *previous* node. To simplify the logic, especially when the head node itself needs to be deleted, we introduce a 'dummy' or 'sentinel' node. This dummy node points to the original head of the list. We maintain two pointers: `previous` (initially pointing to the dummy node) and `current` (initially pointing to the actual head). As we iterate, if `current.val` is in our hash set, it means the node should be deleted. We perform the deletion by setting `previous.next = current.next`, effectively bypassing `current`. In this case, `previous` does not advance, because the new `current` (which was `current.next`) might also need to be deleted, and `previous` still needs to point to the node *before* it. If `current.val` is not in the hash set, the node should be kept. In this scenario, both `previous` and `current` advance one step forward (`previous = current` and `current = current.next`). After iterating through the entire list, the modified list's head will be `dummy.next`.

This two-phase approach (build hash set, then traverse and delete) ensures efficiency. The problem statement guarantees that there will be at least one node in the linked list that is *not* present in `nums`, meaning the resulting list will never be empty, and `dummy.next` will always point to a valid (though possibly short) linked list.

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
#include <vector>
#include <unordered_set>
#include <cstddef> // For NULL or nullptr

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* modifiedList(std::vector<int>& nums, ListNode* head) {
        std::unordered_set<int> delete_set;
        for (int num : nums) {
            delete_set.insert(num);
        }

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        ListNode* curr = head;

        while (curr != nullptr) {
            if (delete_set.count(curr->val)) {
                // Current node's value is in the set, delete it
                prev->next = curr->next;
                // Move curr to the next node to check, prev stays the same
                ListNode* node_to_delete = curr; // Temporarily store curr for deletion if needed
                curr = curr->next;
                // In C++, if ListNode objects are dynamically allocated with `new`,
                // they should be freed with `delete`. LeetCode usually manages this.
                // If managing memory explicitly:
                // delete node_to_delete;
            } else {
                // Current node's value is not in the set, keep it
                prev = curr;
                curr = curr->next;
            }
        }

        return dummy.next;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.HashSet;
import java.util.Set;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> deleteSet = new HashSet<>();
        for (int num : nums) {
            deleteSet.add(num);
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null) {
            if (deleteSet.contains(curr.val)) {
                // Current node's value is in the set, delete it
                prev.next = curr.next;
                // Move curr to the next node to check, prev stays the same
                curr = curr.next;
            } else {
                // Current node's value is not in the set, keep it
                prev = curr;
                curr = curr.next;
            }
        }

        return dummy.next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        delete_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val in delete_set:
                # Current node's value is in the set, delete it
                prev.next = curr.next
                # Move curr to the next node to check, prev stays the same
                curr = curr.next
            else:
                # Current node's value is not in the set, keep it
                prev = curr
                curr = curr.next

        return dummy.next
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        delete_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val in delete_set:
                # Current node's value is in the set, delete it
                prev.next = curr.next
                # Move curr to the next node to check, prev stays the same
                curr = curr.next
            else:
                # Current node's value is not in the set, keep it
                prev = curr
                curr = curr.next

        return dummy.next
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For malloc, free, NULL
#include <stdbool.h> // For bool type

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

// A basic hash set implementation for integers within a known range.
// Constraints: 1 <= Node.val <= 10^5, so a boolean array is efficient enough.
#define MAX_VAL 100001 // Max Node.val + 1
bool exists_in_nums_set[MAX_VAL];

struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    // Initialize the set (boolean array) to false
    for (int i = 0; i < MAX_VAL; ++i) {
        exists_in_nums_set[i] = false;
    }

    // Populate the set
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] >= 1 && nums[i] < MAX_VAL) { // Ensure value is within bounds
            exists_in_nums_set[nums[i]] = true;
        }
    }

    // Create a dummy node
    struct ListNode* dummy = (struct ListNode*) malloc(sizeof(struct ListNode));
    if (dummy == NULL) { /* Handle allocation failure */ return NULL; }
    dummy->val = 0; // Value doesn't matter for dummy node
    dummy->next = head;

    struct ListNode* prev = dummy;
    struct ListNode* curr = head;

    while (curr != NULL) {
        if (curr->val >= 1 && curr->val < MAX_VAL && exists_in_nums_set[curr->val]) {
            // Current node's value is in the set, delete it
            prev->next = curr->next;
            // Move curr to the next node to check, prev stays the same
            struct ListNode* node_to_free = curr;
            curr = curr->next;
            free(node_to_free); // Free the deleted node's memory
        } else {
            // Current node's value is not in the set, keep it
            prev = curr;
            curr = curr->next;
        }
    }

    struct ListNode* new_head = dummy->next;
    free(dummy); // Free the dummy node
    return new_head;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode ModifiedList(int[] nums, ListNode head) {
        HashSet<int> deleteSet = new HashSet<int>();
        foreach (int num in nums) {
            deleteSet.Add(num);
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null) {
            if (deleteSet.Contains(curr.val)) {
                // Current node's value is in the set, delete it
                prev.next = curr.next;
                // Move curr to the next node to check, prev stays the same
                curr = curr.next;
            } else {
                // Current node's value is not in the set, keep it
                prev = curr;
                curr = curr.next;
            }
        }

        return dummy.next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function(nums, head) {
    const deleteSet = new Set(nums);

    const dummy = new ListNode(0);
    dummy.next = head;

    let prev = dummy;
    let curr = head;

    while (curr !== null) {
        if (deleteSet.has(curr.val)) {
            // Current node's value is in the set, delete it
            prev.next = curr.next;
            // Move curr to the next node to check, prev stays the same
            curr = curr.next;
        } else {
            // Current node's value is not in the set, keep it
            prev = curr;
            curr = curr.next;
        }
    }

    return dummy.next;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function modifiedList(nums: number[], head: ListNode | null): ListNode | null {
    const deleteSet: Set<number> = new Set(nums);

    const dummy: ListNode = new ListNode(0);
    dummy.next = head;

    let prev: ListNode = dummy;
    let curr: ListNode | null = head;

    while (curr !== null) {
        if (deleteSet.has(curr.val)) {
            // Current node's value is in the set, delete it
            prev.next = curr.next;
            // Move curr to the next node to check, prev stays the same
            curr = curr.next;
        } else {
            // Current node's value is not in the set, keep it
            prev = curr;
            curr = curr.next;
        }
    }

    return dummy.next;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

// Definition for a singly-linked list.
class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param ListNode $head
     * @return ListNode
     */
    function modifiedList($nums, $head) {
        $deleteSet = [];
        foreach ($nums as $num) {
            $deleteSet[$num] = true; // Using associative array as a hash set
        }

        $dummy = new ListNode(0);
        $dummy->next = $head;

        $prev = $dummy;
        $curr = $head;

        while ($curr !== null) {
            if (isset($deleteSet[$curr->val])) {
                // Current node's value is in the set, delete it
                $prev->next = $curr->next;
                // Move curr to the next node to check, prev stays the same
                $curr = $curr->next;
            } else {
                // Current node's value is not in the set, keep it
                $prev = $curr;
                $curr = $curr->next;
            }
        }

        return $dummy->next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

// Definition for singly-linked list.
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    func modifiedList(_ nums: [Int], _ head: ListNode?) -> ListNode? {
        let deleteSet = Set(nums)

        let dummy = ListNode(0)
        dummy.next = head

        var prev: ListNode = dummy
        var curr: ListNode? = head

        while curr != nil {
            if deleteSet.contains(curr!.val) {
                // Current node's value is in the set, delete it
                prev.next = curr!.next
                // Move curr to the next node to check, prev stays the same
                curr = curr!.next
            } else {
                // Current node's value is not in the set, keep it
                prev = curr!
                curr = curr!.next
            }
        }

        return dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Definition for singly-linked list.
class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun modifiedList(nums: IntArray, head: ListNode?): ListNode? {
        val deleteSet = nums.toHashSet()

        val dummy = ListNode(0)
        dummy.next = head

        var prev: ListNode = dummy
        var curr: ListNode? = head

        while (curr != null) {
            if (deleteSet.contains(curr.`val`)) {
                // Current node's value is in the set, delete it
                prev.next = curr.next
                // Move curr to the next node to check, prev stays the same
                curr = curr.next
            } else {
                // Current node's value is not in the set, keep it
                prev = curr
                curr = curr.next
            }
        }

        return dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  ListNode? modifiedList(List<int> nums, ListNode? head) {
    final Set<int> deleteSet = nums.toSet();

    final ListNode dummy = ListNode(0);
    dummy.next = head;

    ListNode prev = dummy;
    ListNode? curr = head;

    while (curr != null) {
      if (deleteSet.contains(curr.val)) {
        // Current node's value is in the set, delete it
        prev.next = curr.next;
        // Move curr to the next node to check, prev stays the same
        curr = curr.next;
      } else {
        // Current node's value is not in the set, keep it
        prev = curr;
        curr = curr.next;
      }
    }

    return dummy.next;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

// Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

func modifiedList(nums []int, head *ListNode) *ListNode {
    deleteSet := make(map[int]bool)
    for _, num := range nums {
        deleteSet[num] = true
    }

    dummy := &ListNode{Val: 0, Next: head}

    prev := dummy
    curr := head

    for curr != nil {
        if deleteSet[curr.Val] {
            // Current node's value is in the set, delete it
            prev.Next = curr.Next
            // Move curr to the next node to check, prev stays the same
            curr = curr.Next
        } else {
            // Current node's value is not in the set, keep it
            prev = curr
            curr = curr.Next
        }
    }

    return dummy.Next
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end

# @param {Integer[]} nums
# @param {ListNode} head
# @return {ListNode}
def modified_list(nums, head)
    require 'set' # Ensure Set is available
    delete_set = Set.new(nums)

    dummy = ListNode.new(0)
    dummy.next = head

    prev = dummy
    curr = head

    while curr
        if delete_set.include?(curr.val)
            # Current node's value is in the set, delete it
            prev.next = curr.next
            # Move curr to the next node to check, prev stays the same
            curr = curr.next
        else
            # Current node's value is not in the set, keep it
            prev = curr
            curr = curr.next
        end
    end

    dummy.next
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

// Definition for singly-linked list.
class ListNode(_val: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var val: Int = _val
}

object Solution {
    def modifiedList(nums: Array[Int], head: ListNode): ListNode = {
        val deleteSet: mutable.Set[Int] = mutable.Set.empty[Int]
        nums.foreach(deleteSet.add)

        val dummy = new ListNode(0)
        dummy.next = head

        var prev: ListNode = dummy
        var curr: ListNode = head

        while (curr != null) {
            if (deleteSet.contains(curr.val)) {
                // Current node's value is in the set, delete it
                prev.next = curr.next
                // Move curr to the next node to check, prev stays the same
                curr = curr.next
            } else {
                // Current node's value is not in the set, keep it
                prev = curr
                curr = curr.next
            }
        }

        dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode { next: None, val }
  }
}

use std::collections::HashSet;

impl Solution {
    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let delete_set: HashSet<i32> = nums.into_iter().collect();

        let mut dummy = ListNode::new(0);
        let mut prev_ptr = &mut dummy.next; // A pointer to the 'next' field of the previous node
        let mut current_node_opt = head; // The current node we are examining

        while let Some(mut node) = current_node_opt.take() { // take() moves ownership out of current_node_opt
            if delete_set.contains(&node.val) {
                // This node should be deleted. Skip it by taking its 'next' field
                // and making it the new `current_node_opt` for the next iteration.
                current_node_opt = node.next;
            } else {
                // This node should be kept. Attach it to the `prev_ptr`.
                // Then update `prev_ptr` to point to the `next` field of the node we just kept.
                current_node_opt = node.next; // Store the next part of the original list
                node.next = None; // Detach node from the rest of its original list
                *prev_ptr = Some(node); // Attach the current node to the new list
                prev_ptr = &mut prev_ptr.as_mut().unwrap().next; // Advance prev_ptr to the 'next' of the just-attached node
            }
        }

        dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

;; Provided ListNode structure (assuming mutable for typical linked-list operations)
(struct ListNode (val next) #:mutable #t)

(define (modifiedList nums head)
  (define delete-set (make-hash))
  (for ([num nums])
    (hash-set! delete-set num #t))

  (define dummy (ListNode 0 #f))
  (set-ListNode-next! dummy head)

  (define prev dummy)
  (define curr head)

  (let loop ( (curr-node curr) (prev-node prev) )
    (when curr-node
      (if (hash-has-key? delete-set (ListNode-val curr-node))
          ;; Delete current node: bypass it by linking prev-node's next to curr-node's next
          (begin
            (set-ListNode-next! prev-node (ListNode-next curr-node))
            ;; Move to the next node, prev-node remains the same because the new curr-node might also be deleted
            (loop (ListNode-next curr-node) prev-node))
          ;; Keep current node: move both prev-node and curr-node forward
          (begin
            (loop (ListNode-next curr-node) curr-node)))))

  (ListNode-next dummy))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([modified_list/2]).

%% Definition for singly-linked list.
%% Records are immutable. To simulate mutable pointers, we pass modified records.
%% This approach rebuilds the list or passes accumulated state. The direct iterative
%% approach with two pointers is not idiomatic Erlang. Instead, a recursive approach
%% that constructs the new list is typically used.

-record(list_node, {val = 0, next = null}).

modified_list(Nums, Head) ->
    DeleteSet = sets:from_list(Nums),

    % Recursive helper to build the new list
    build_new_list(Head, DeleteSet).

build_new_list(null, _DeleteSet) ->
    null;
build_new_list(Curr = #list_node{val = Val, next = Next}, DeleteSet) ->
    case sets:is_element(Val, DeleteSet) of
        true ->
            % Node value is in delete set, skip this node
            build_new_list(Next, DeleteSet);
        false ->
            % Node value is NOT in delete set, keep this node
            #list_node{val = Val, next = build_new_list(Next, DeleteSet)}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @type list_node :: %__MODULE__{val: integer, next: list_node() | nil}
  defstruct val: 0, next: nil

  @spec modified_list(nums :: [integer], head :: list_node | nil) :: list_node | nil
  def modified_list(nums, head) do
    delete_set = MapSet.new(nums)

    # In functional languages like Elixir, linked lists are typically immutable.
    # We don't 'mutate' pointers; instead, we build a new list by recursing.
    # This function recursively processes the input list and constructs the new list.
    do_modified_list(head, delete_set)
  end

  defp do_modified_list(nil, _delete_set), do: nil
  defp do_modified_list(%Solution.ListNode{val: val, next: next} = curr, delete_set) do
    if MapSet.member?(delete_set, val) do
      # If current node's value is in the set, skip this node and process the rest of the list.
      do_modified_list(next, delete_set)
    else
      # If current node's value is not in the set, keep this node.
      # Its 'next' pointer should point to the result of processing the rest of the list.
      %Solution.ListNode{val: val, next: do_modified_list(next, delete_set)}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M + N)

- **Space Complexity:** O(M)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 22:27:57 )</small>
</summary>

<div class="ai-solution-content">

### Approach


The problem requires us to remove nodes from a linked list that have values present in a given array. To solve this problem, we will follow these steps:

1. Create a Set from the given array to store the values that need to be removed from the linked list. This is because checking if an element exists in a Set is an O(1) operation, which will help us to efficiently check if a node's value should be removed.

2. Initialize a dummy node that points to the head of the linked list. This dummy node will help us to handle the case where the head node itself needs to be removed.

3. Initialize a pointer to the current node in the linked list.

4. Traverse the linked list. For each node, check if its value exists in the Set. If it does, skip this node by updating the next pointer of the previous node to point to the next node. If it does not, move the previous pointer to the current node.

5. After traversing the entire linked list, the next pointer of the dummy node will point to the new head of the modified linked list.

This approach ensures that we remove all nodes with values present in the given array and return the head of the modified linked list.

The problem-solving strategy involves using a Set to efficiently check if a node's value should be removed, and using a dummy node to handle the case where the head node itself needs to be removed.

The algorithm logic is as follows:

- Create a Set from the given array.
- Initialize a dummy node and a pointer to the current node.
- Traverse the linked list, checking if each node's value exists in the Set.
- If a node's value exists in the Set, skip this node by updating the next pointer of the previous node.
- If a node's value does not exist in the Set, move the previous pointer to the current node.
- Return the next pointer of the dummy node as the head of the modified linked list.

Examples and edge cases:

- If the given array is empty, the linked list remains unchanged.
- If the linked list is empty, the function returns None.
- If the head node itself needs to be removed, the function returns the next node as the new head.

Time complexity:

The time complexity of this solution is O(n + m), where n is the number of nodes in the linked list and m is the number of elements in the given array. This is because we are traversing the linked list once and creating a Set from the given array.

Space complexity:

The space complexity of this solution is O(m), where m is the number of elements in the given array. This is because we are storing the elements of the given array in a Set.



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
// Definition for singly-linked list.
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution {
public:
    ListNode* removeElements(ListNode* head, vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        ListNode* curr = head;

        while (curr) {
            if (numSet.find(curr->val) != numSet.end()) {
                prev->next = curr->next;
            } else {
                prev = curr;
            }
            curr = curr->next;
        }

        return dummy->next;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

// Definition for singly-linked list.
// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode() {}
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
// }

class Solution {
    public ListNode removeElements(ListNode head, int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null) {
            if (numSet.contains(curr.val)) {
                prev.next = curr.next;
            } else {
                prev = curr;
            }
            curr = curr.next;
        }

        return dummy.next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], nums: List[int]) -> Optional[ListNode]:
        numSet = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.val in numSet:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], nums: List[int]) -> Optional[ListNode]:
        numSet = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.val in numSet:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Definition for singly-linked list.
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };

struct ListNode* removeElements(struct ListNode* head, int* nums, int numsSize) {
    int numSet[100001] = {0};
    for (int i = 0; i < numsSize; i++) {
        numSet[nums[i]] = 1;
    }
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    struct ListNode* prev = dummy;
    struct ListNode* curr = head;

    while (curr) {
        if (numSet[curr->val]) {
            prev->next = curr->next;
        } else {
            prev = curr;
        }
        curr = curr->next;
    }

    return dummy->next;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Definition for singly-linked list.
// public class ListNode {
//     public int val;
//     public ListNode next;
//     public ListNode(int val=0, ListNode next=null) {
//         this.val = val;
//         this.next = next;
//     }
// }

public class Solution {
    public ListNode RemoveElements(ListNode head, int[] nums) {
        HashSet<int> numSet = new HashSet<int>(nums);
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode curr = head;

        while (curr != null) {
            if (numSet.Contains(curr.val)) {
                prev.next = curr.next;
            } else {
                prev = curr;
            }
            curr = curr.next;
        }

        return dummy.next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Definition for singly-linked list.
// var ListNode = function(val, next) {
//     this.val = (val===undefined ? 0 : val)
//     this.next = (next===undefined ? null : next)
// }

var removeElements = function(head, nums) {
    let numSet = new Set(nums);
    let dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;
    let curr = head;

    while (curr) {
        if (numSet.has(curr.val)) {
            prev.next = curr.next;
        } else {
            prev = curr;
        }
        curr = curr.next;
    }

    return dummy.next;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Definition for singly-linked list.
// class ListNode {
//     val: number
//     next: ListNode | null
//     constructor(val?: number, next?: ListNode | null) {
//         this.val = (val===undefined ? 0 : val)
//         this.next = (next===undefined ? null : next)
//     }
// }

function removeElements(head: ListNode | null, nums: number[]): ListNode | null {
    let numSet: Set<number> = new Set(nums);
    let dummy: ListNode = new ListNode(0);
    dummy.next = head;
    let prev: ListNode = dummy;
    let curr: ListNode | null = head;

    while (curr) {
        if (numSet.has(curr.val)) {
            prev.next = curr.next;
        } else {
            prev = curr;
        }
        curr = curr.next;
    }

    return dummy.next;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Definition for singly-linked list.
// class ListNode {
//     public $val = 0;
//     public $next = null;
//     function __construct($val = 0, $next = null) {
//         $this->val = $val;
//         $this->next = $next;
//     }
// }

class Solution {
    function removeElements($head, $nums) {
        $numSet = array_flip($nums);
        $dummy = new ListNode(0);
        $dummy->next = $head;
        $prev = $dummy;
        $curr = $head;

        while ($curr) {
            if (isset($numSet[$curr->val])) {
                $prev->next = $curr->next;
            } else {
                $prev = $curr;
            }
            $curr = $curr->next;
        }

        return $dummy->next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Definition for singly-linked list.
// public class ListNode {
//     public var val: Int
//     public var next: ListNode?
//     public init(_ val: Int) {
//         self.val = val
//         self.next = nil
//     }
// }

class Solution {
    func removeElements(_ head: ListNode?, _ nums: [Int]) -> ListNode? {
        let numSet = Set(nums)
        let dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        var curr: ListNode? = head

        while let curr = curr {
            if numSet.contains(curr.val) {
                prev?.next = curr.next
            } else {
                prev = curr
            }
            curr = curr.next
        }

        return dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Definition for singly-linked list.
// class ListNode(var `val`: Int) {
//     var next: ListNode? = null
// }

class Solution {
    fun removeElements(head: ListNode?, nums: IntArray): ListNode? {
        val numSet = nums.toSet()
        val dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        var curr: ListNode? = head

        while (curr != null) {
            if (curr.`val` in numSet) {
                prev?.next = curr.next
            } else {
                prev = curr
            }
            curr = curr.next
        }

        return dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Definition for singly-linked list.
// class ListNode {
//   int val;
//   ListNode? next;
//   ListNode([this.val = 0, this.next]);
// }

class Solution {
    ListNode? removeElements(ListNode? head, List<int> nums) {
        Set<int> numSet = Set.from(nums);
        ListNode dummy = ListNode(0);
        dummy.next = head;
        ListNode? prev = dummy;
        ListNode? curr = head;

        while (curr != null) {
            if (numSet.contains(curr.val)) {
                prev?.next = curr.next;
            } else {
                prev = curr;
            }
            curr = curr.next;
        }

        return dummy.next;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Definition for singly-linked list.
// type ListNode struct {
//     Val int
//     Next *ListNode
// }

func removeElements(head *ListNode, nums []int) *ListNode {
    numSet := make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }
    dummy := &ListNode{Val: 0}
    dummy.Next = head
    prev := dummy
    curr := head

    for curr != nil {
        if numSet[curr.Val] {
            prev.Next = curr.Next
        } else {
            prev = curr
        }
        curr = curr.Next
    }

    return dummy.Next
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# Definition for singly-linked list.
# # class ListNode
# #     attr_accessor :val, :next
# #     def initialize(val = 0, _next = nil)
# #         @val = val
# #         @next = _next
# #     end
# # end

# @param {ListNode} head
# @param {Integer[]} nums
# @return {ListNode}
def remove_elements(head, nums)
    num_set = Set.new(nums)
    dummy = ListNode.new(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr
        if num_set.include?(curr.val)
            prev.next = curr.next
        else
            prev = curr
        end
        curr = curr.next
    end

    dummy.next
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Definition for singly-linked list.
// class ListNode(_value: Int) {
//   var value: Int = _value
//   var next: ListNode = null
// }

object Solution {
    def removeElements(_head: ListNode, nums: Array[Int]): ListNode = {
        val numSet = nums.toSet
        val dummy = new ListNode(0)
        dummy.next = _head
        var prev: ListNode = dummy
        var curr: ListNode = _head

        while (curr != null) {
            if (numSet.contains(curr.value)) {
                prev.next = curr.next
            } else {
                prev = curr
            }
            curr = curr.next
        }

        dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

struct Solution;

impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, nums: Vec<i32>) -> Option<Box<ListNode>> {
        let num_set: std::collections::HashSet<i32> = nums.into_iter().collect();
        let mut dummy = Some(Box::new(ListNode::new(0)));
        dummy.as_mut().unwrap().next = head;
        let mut prev = dummy.as_mut().unwrap();
        let mut curr = prev.next.take();

        while let Some(mut node) = curr {
            if num_set.contains(&node.val) {
                curr = node.next.take();
            } else {
                prev.next = Some(node);
                prev = prev.next.as_mut().unwrap();
                curr = prev.next.take();
            }
        }

        dummy.unwrap().next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

; Definition for singly-linked list.
(struct list-node (val next) #:transparent)

(define (remove-elements head nums)
  (let ((num-set (list->set nums)))
    (let loop ((dummy (list-node 0 head)) (prev dummy) (curr head))
      (cond
        ((not curr) (list-node-next dummy))
        ((set-member? num-set (list-node-val curr))
         (set-list-node-next! prev (list-node-next curr))
         (loop dummy prev (list-node-next curr)))
        (else
         (loop dummy curr (list-node-next curr)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).

-export([remove_elements/2]).

% Definition for singly-linked list.
-record(list_node, {val, next}).

remove_elements(Head, Nums) ->
    NumSet = sets:from_list(Nums),
    Dummy = #list_node{val = 0, next = Head},
    remove_elements_loop(Dummy, Head, NumSet).

remove_elements_loop(Prev, null, _NumSet) ->
    Prev#list_node.next;
remove_elements_loop(Prev, #list_node{val = Val, next = Next} = Curr, NumSet) ->
    case sets:is_element(Val, NumSet) of
        true ->
            Prev#list_node.next := Next,
            remove_elements_loop(Prev, Next, NumSet);
        false ->
            remove_elements_loop(Curr, Next, NumSet)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @doc
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + m) where n is the number of nodes in the linked list and m is the number of elements in the given array. This is because we are traversing the linked list once and creating a Set from the given array.

- **Space Complexity:** O(m) where m is the number of elements in the given array. This is because we are storing the elements of the given array in a Set.

</div>
</details>
