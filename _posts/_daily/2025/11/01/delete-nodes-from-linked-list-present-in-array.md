---
layout: post
title: "Delete Nodes From Linked List Present in Array"
date: 2025-11-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Linked List"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *   \
        \  int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr)\
        \ {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int\
        \ x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\n\
        public:\n    ListNode* modifiedList(vector<int>& nums, ListNode* head) {\n \
        \       unordered_set<int> values(nums.begin(), nums.end());\n        ListNode\
        \ dummy(0, head);\n        ListNode* prev = &dummy;\n        while (prev->next\
        \ != nullptr) {\n            if (values.count(prev->next->val)) {\n        \
        \        prev->next = prev->next->next;\n            } else {\n            \
        \    prev = prev->next;\n            }\n        }\n        return dummy.next;\n\
        \    }\n};"
      java: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int\
        \ val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val\
        \ = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode\
        \ modifiedList(int[] nums, ListNode head) {\n        Set<Integer> values = new\
        \ HashSet<>();\n        for (int value : nums) {\n            values.add(value);\n\
        \        }\n        ListNode dummy = new ListNode(0, head);\n        ListNode\
        \ prev = dummy;\n        while (prev.next != null) {\n            if (values.contains(prev.next.val))\
        \ {\n                prev.next = prev.next.next;\n            } else {\n   \
        \             prev = prev.next;\n            }\n        }\n        return dummy.next;\n\
        \    }\n}"
      python: "# Definition for singly-linked list.\n# class ListNode(object):\n#  \
        \   def __init__(self, val=0, next=None):\n#         self.val = val\n#     \
        \    self.next = next\nclass Solution(object):\n    def modifiedList(self, nums,\
        \ head):\n        \"\"\"\n        :type nums: List[int]\n        :type head:\
        \ Optional[ListNode]\n        :rtype: Optional[ListNode]\n        \"\"\"\n \
        \       values = set(nums)\n        dummy = ListNode(0, head)\n        prev\
        \ = dummy\n        while prev.next is not None:\n            if prev.next.val\
        \ in values:\n                prev.next = prev.next.next\n            else:\n\
        \                prev = prev.next\n        return dummy.next"
      python3: "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self,\
        \ val=0, next=None):\n#         self.val = val\n#         self.next = next\n\
        class Solution:\n    def modifiedList(self, nums: List[int], head: Optional[ListNode])\
        \ -> Optional[ListNode]:\n        values = set(nums)\n        dummy = ListNode(0,\
        \ head)\n        prev = dummy\n        while prev.next is not None:\n      \
        \      if prev.next.val in values:\n                prev.next = prev.next.next\n\
        \            else:\n                prev = prev.next\n        return dummy.next"
      c: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int\
        \ val;\n *     struct ListNode *next;\n * };\n */\nstruct ListNode* modifiedList(int*\
        \ nums, int numsSize, struct ListNode* head) {\n    int* values = calloc(100001,\
        \ sizeof(int));\n    for (int i = 0; i < numsSize; i++) {\n        values[nums[i]]\
        \ = 1;\n    }\n    struct ListNode dummy;\n    dummy.val = 0;\n    dummy.next\
        \ = head;\n    struct ListNode* prev = &dummy;\n    while (prev->next != NULL)\
        \ {\n        if (values[prev->next->val]) {\n            prev->next = prev->next->next;\n\
        \        } else {\n            prev = prev->next;\n        }\n    }\n    free(values);\n\
        \    return dummy.next;\n}"
      csharp: "/**\n * Definition for singly-linked list.\n * public class ListNode\
        \ {\n *     public int val;\n *     public ListNode next;\n *     public ListNode(int\
        \ val=0, ListNode next=null) {\n *         this.val = val;\n *         this.next\
        \ = next;\n *     }\n * }\n */\npublic class Solution {\n    public ListNode\
        \ ModifiedList(int[] nums, ListNode head) {\n        var values = new HashSet<int>(nums);\n\
        \        var dummy = new ListNode(0, head);\n        var prev = dummy;\n   \
        \     while (prev.next != null) {\n            if (values.Contains(prev.next.val))\
        \ {\n                prev.next = prev.next.next;\n            } else {\n   \
        \             prev = prev.next;\n            }\n        }\n        return dummy.next;\n\
        \    }\n}"
      javascript: "/**\n * Definition for singly-linked list.\n * function ListNode(val,\
        \ next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next =\
        \ (next===undefined ? null : next)\n * }\n */\n/**\n * @param {number[]} nums\n\
        \ * @param {ListNode} head\n * @return {ListNode}\n */\nvar modifiedList = function(nums,\
        \ head) {\n    const values = new Set(nums);\n    const dummy = new ListNode(0,\
        \ head);\n    let prev = dummy;\n    while (prev.next !== null) {\n        if\
        \ (values.has(prev.next.val)) {\n            prev.next = prev.next.next;\n \
        \       } else {\n            prev = prev.next;\n        }\n    }\n    return\
        \ dummy.next;\n};"
      typescript: "/**\n * Definition for singly-linked list.\n * class ListNode {\n\
        \ *     val: number\n *     next: ListNode | null\n *     constructor(val?:\
        \ number, next?: ListNode | null) {\n *         this.val = (val===undefined\
        \ ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *  \
        \   }\n * }\n */\n\nfunction modifiedList(nums: number[], head: ListNode | null):\
        \ ListNode | null {\n    const values = new Set(nums);\n    const dummy = new\
        \ ListNode(0, head);\n    let prev = dummy;\n    while (prev.next !== null)\
        \ {\n        if (values.has(prev.next.val)) {\n            prev.next = prev.next.next;\n\
        \        } else {\n            prev = prev.next;\n        }\n    }\n    return\
        \ dummy.next;\n};"
      php: "/**\n * Definition for a singly-linked list.\n * class ListNode {\n *  \
        \   public $val = 0;\n *     public $next = null;\n *     function __construct($val\
        \ = 0, $next = null) {\n *         $this->val = $val;\n *         $this->next\
        \ = $next;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ Integer[] $nums\n     * @param ListNode $head\n     * @return ListNode\n \
        \    */\n    function modifiedList($nums, $head) {\n        $values = array_fill_keys($nums,\
        \ true);\n        $dummy = new ListNode(0, $head);\n        $prev = $dummy;\n\
        \        while ($prev->next !== null) {\n            if (isset($values[$prev->next->val]))\
        \ {\n                $prev->next = $prev->next->next;\n            } else {\n\
        \                $prev = $prev->next;\n            }\n        }\n        return\
        \ $dummy->next;\n    }\n}"
      swift: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     public var val: Int\n *     public var next: ListNode?\n *     public\
        \ init() { self.val = 0; self.next = nil; }\n *     public init(_ val: Int)\
        \ { self.val = val; self.next = nil; }\n *     public init(_ val: Int, _ next:\
        \ ListNode?) { self.val = val; self.next = next; }\n * }\n */\nclass Solution\
        \ {\n    func modifiedList(_ nums: [Int], _ head: ListNode?) -> ListNode? {\n\
        \        let values = Set(nums)\n        let dummy = ListNode(0, head)\n   \
        \     var prev = dummy\n        while let next = prev.next {\n            if\
        \ values.contains(next.val) {\n                prev.next = next.next\n     \
        \       } else {\n                prev = next\n            }\n        }\n  \
        \      return dummy.next\n    }\n}"
      kotlin: "class Solution {\n    fun modifiedList(nums: IntArray, head: ListNode?):\
        \ ListNode? {\n        val values = nums.toHashSet()\n        val dummy = ListNode(0)\n\
        \        dummy.next = head\n        var prev = dummy\n        while (prev.next\
        \ != null) {\n            val next = prev.next!!\n            if (next.`val`\
        \ in values) {\n                prev.next = next.next\n            } else {\n\
        \                prev = next\n            }\n        }\n        return dummy.next\n\
        \    }\n}"
      dart: "class Solution {\n  ListNode? modifiedList(List<int> nums, ListNode? head)\
        \ {\n    final values = nums.toSet();\n    final dummy = ListNode(0, head);\n\
        \    var prev = dummy;\n    while (prev.next != null) {\n      final next =\
        \ prev.next!;\n      if (values.contains(next.val)) {\n        prev.next = next.next;\n\
        \      } else {\n        prev = next;\n      }\n    }\n    return dummy.next;\n\
        \  }\n}"
      go: "func modifiedList(nums []int, head *ListNode) *ListNode {\n\tvalues := make(map[int]struct{},\
        \ len(nums))\n\tfor _, value := range nums {\n\t\tvalues[value] = struct{}{}\n\
        \t}\n\n\tdummy := &ListNode{Next: head}\n\tprev := dummy\n\tfor prev.Next !=\
        \ nil {\n\t\tif _, exists := values[prev.Next.Val]; exists {\n\t\t\tprev.Next\
        \ = prev.Next.Next\n\t\t} else {\n\t\t\tprev = prev.Next\n\t\t}\n\t}\n\treturn\
        \ dummy.Next\n}"
      ruby: "def modified_list(nums, head)\n    values = nums.to_set\n    dummy = ListNode.new(0,\
        \ head)\n    prev = dummy\n    while prev.next\n        if values.include?(prev.next.val)\n\
        \            prev.next = prev.next.next\n        else\n            prev = prev.next\n\
        \        end\n    end\n    dummy.next\nend"
      scala: "object Solution {\n    def modifiedList(nums: Array[Int], head: ListNode):\
        \ ListNode = {\n        val values = nums.toSet\n        val dummy = new ListNode(0,\
        \ head)\n        var prev = dummy\n        while (prev.next != null) {\n   \
        \         if (values.contains(prev.next.x)) {\n                prev.next = prev.next.next\n\
        \            } else {\n                prev = prev.next\n            }\n   \
        \     }\n        dummy.next\n    }\n}"
      rust: "// Definition for singly-linked list.\n// #[derive(PartialEq, Eq, Clone,\
        \ Debug)]\n// pub struct ListNode {\n//   pub val: i32,\n//   pub next: Option<Box<ListNode>>\n\
        // }\n// \n// impl ListNode {\n//   #[inline]\n//   fn new(val: i32) -> Self\
        \ {\n//     ListNode {\n//       next: None,\n//       val\n//     }\n//   }\n\
        // }\nimpl Solution {\n    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>)\
        \ -> Option<Box<ListNode>> {\n        use std::collections::HashSet;\n\n   \
        \     let values: HashSet<i32> = nums.into_iter().collect();\n        let mut\
        \ dummy = Box::new(ListNode { val: 0, next: head });\n        let mut prev =\
        \ &mut dummy;\n\n        while prev.next.is_some() {\n            if values.contains(&prev.next.as_ref().unwrap().val)\
        \ {\n                let next = prev.next.as_mut().unwrap().next.take();\n \
        \               prev.next = next;\n            } else {\n                prev\
        \ = prev.next.as_mut().unwrap();\n            }\n        }\n\n        dummy.next\n\
        \    }\n}"
      racket: "; Definition for singly-linked list:\n#|\n\n; val : integer?\n; next\
        \ : (or/c list-node? #f)\n(struct list-node\n  (val next) #:mutable #:transparent)\n\
        \n; constructor\n(define (make-list-node [val 0])\n  (list-node val #f))\n\n\
        |#\n\n(define/contract (modified-list nums head)\n  (-> (listof exact-integer?)\
        \ (or/c list-node? #f) (or/c list-node? #f))\n  (let ([values (list->set nums)])\n\
        \    (define dummy (make-list-node 0))\n    (set-list-node-next! dummy head)\n\
        \    (let loop ([prev dummy])\n      (define next (list-node-next prev))\n \
        \     (when next\n        (if (set-member? values (list-node-val next))\n  \
        \          (set-list-node-next! prev (list-node-next next))\n            (loop\
        \ next)))\n      (when (and next (set-member? values (list-node-val next)))\n\
        \        (loop prev)))\n    (list-node-next dummy)))"
      erlang: "%% Definition for singly-linked list.\n%%\n%% -record(list_node, {val\
        \ = 0 :: integer(),\n%%                     next = null :: 'null' | #list_node{}}).\n\
        \n-spec modified_list(Nums :: [integer()], Head :: #list_node{} | null) -> #list_node{}\
        \ | null.\nmodified_list(Nums, Head) ->\n  Values = sets:from_list(Nums),\n\
        \  Dummy = #list_node{val = 0, next = Head},\n  modified_list_loop(Dummy, Values),\n\
        \  Dummy#list_node.next.\n\nmodified_list_loop(Prev, Values) ->\n  case Prev#list_node.next\
        \ of\n    null ->\n      ok;\n    Next ->\n      case sets:is_element(Next#list_node.val,\
        \ Values) of\n        true ->\n          Prev#list_node{next = Next#list_node.next},\n\
        \          modified_list_loop(Prev, Values);\n        false ->\n          modified_list_loop(Next,\
        \ Values)\n      end\n  end."
      elixir: "# Definition for singly-linked list.\n#\n# defmodule ListNode do\n# \
        \  @type t :: %__MODULE__{\n#           val: integer,\n#           next: ListNode.t()\
        \ | nil\n#         }\n#   defstruct val: 0, next: nil\n# end\n\ndefmodule Solution\
        \ do\n  @spec modified_list(nums :: [integer], head :: ListNode.t | nil) ::\
        \ ListNode.t | nil\n  def modified_list(nums, head) do\n    values = MapSet.new(nums)\n\
        \    dummy = %ListNode{val: 0, next: head}\n    remove_nodes(dummy, values)\n\
        \    dummy.next\n  end\n\n  defp remove_nodes(prev, values) do\n    case prev.next\
        \ do\n      nil ->\n        :ok\n\n      next ->\n        if MapSet.member?(values,\
        \ next.val) do\n          prev.next = next.next\n          remove_nodes(prev,\
        \ values)\n        else\n          remove_nodes(next, values)\n        end\n\
        \    end\n  end\nend"
    approach: 'Store the values in nums in a hash set so each list node can be checked
      for removal in expected constant time. Use a dummy node before the head to handle
      deletions at the beginning uniformly.


      Traverse the list with a pointer to the previous node. If the next node''s value
      is in the set, bypass that node; otherwise advance the pointer. Return the dummy
      node''s next pointer.'
    time_complexity: O(m + n) expected time, where m is the length of nums and n is
      the number of list nodes.
    space_complexity: O(m) for the set of values from nums.
    elapsed_time: 78.65448641777039
    model: gpt-6-luna
    generated_at: '2026-11-13 00:14:24 '
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

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Store the values in nums in a hash set so each list node can be checked for removal in expected constant time. Use a dummy node before the head to handle deletions at the beginning uniformly.

Traverse the list with a pointer to the previous node. If the next node's value is in the set, bypass that node; otherwise advance the pointer. Return the dummy node's next pointer.

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
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> values(nums.begin(), nums.end());
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        while (prev->next != nullptr) {
            if (values.count(prev->next->val)) {
                prev->next = prev->next->next;
            } else {
                prev = prev->next;
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
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> values = new HashSet<>();
        for (int value : nums) {
            values.add(value);
        }
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        while (prev.next != null) {
            if (values.contains(prev.next.val)) {
                prev.next = prev.next.next;
            } else {
                prev = prev.next;
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
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        values = set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next is not None:
            if prev.next.val in values:
                prev.next = prev.next.next
            else:
                prev = prev.next
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
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values = set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next is not None:
            if prev.next.val in values:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    int* values = calloc(100001, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        values[nums[i]] = 1;
    }
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;
    struct ListNode* prev = &dummy;
    while (prev->next != NULL) {
        if (values[prev->next->val]) {
            prev->next = prev->next->next;
        } else {
            prev = prev->next;
        }
    }
    free(values);
    return dummy.next;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ModifiedList(int[] nums, ListNode head) {
        var values = new HashSet<int>(nums);
        var dummy = new ListNode(0, head);
        var prev = dummy;
        while (prev.next != null) {
            if (values.Contains(prev.next.val)) {
                prev.next = prev.next.next;
            } else {
                prev = prev.next;
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
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function(nums, head) {
    const values = new Set(nums);
    const dummy = new ListNode(0, head);
    let prev = dummy;
    while (prev.next !== null) {
        if (values.has(prev.next.val)) {
            prev.next = prev.next.next;
        } else {
            prev = prev.next;
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
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function modifiedList(nums: number[], head: ListNode | null): ListNode | null {
    const values = new Set(nums);
    const dummy = new ListNode(0, head);
    let prev = dummy;
    while (prev.next !== null) {
        if (values.has(prev.next.val)) {
            prev.next = prev.next.next;
        } else {
            prev = prev.next;
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
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param Integer[] $nums
     * @param ListNode $head
     * @return ListNode
     */
    function modifiedList($nums, $head) {
        $values = array_fill_keys($nums, true);
        $dummy = new ListNode(0, $head);
        $prev = $dummy;
        while ($prev->next !== null) {
            if (isset($values[$prev->next->val])) {
                $prev->next = $prev->next->next;
            } else {
                $prev = $prev->next;
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
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func modifiedList(_ nums: [Int], _ head: ListNode?) -> ListNode? {
        let values = Set(nums)
        let dummy = ListNode(0, head)
        var prev = dummy
        while let next = prev.next {
            if values.contains(next.val) {
                prev.next = next.next
            } else {
                prev = next
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
class Solution {
    fun modifiedList(nums: IntArray, head: ListNode?): ListNode? {
        val values = nums.toHashSet()
        val dummy = ListNode(0)
        dummy.next = head
        var prev = dummy
        while (prev.next != null) {
            val next = prev.next!!
            if (next.`val` in values) {
                prev.next = next.next
            } else {
                prev = next
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
class Solution {
  ListNode? modifiedList(List<int> nums, ListNode? head) {
    final values = nums.toSet();
    final dummy = ListNode(0, head);
    var prev = dummy;
    while (prev.next != null) {
      final next = prev.next!;
      if (values.contains(next.val)) {
        prev.next = next.next;
      } else {
        prev = next;
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
func modifiedList(nums []int, head *ListNode) *ListNode {
	values := make(map[int]struct{}, len(nums))
	for _, value := range nums {
		values[value] = struct{}{}
	}

	dummy := &ListNode{Next: head}
	prev := dummy
	for prev.Next != nil {
		if _, exists := values[prev.Next.Val]; exists {
			prev.Next = prev.Next.Next
		} else {
			prev = prev.Next
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
def modified_list(nums, head)
    values = nums.to_set
    dummy = ListNode.new(0, head)
    prev = dummy
    while prev.next
        if values.include?(prev.next.val)
            prev.next = prev.next.next
        else
            prev = prev.next
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
object Solution {
    def modifiedList(nums: Array[Int], head: ListNode): ListNode = {
        val values = nums.toSet
        val dummy = new ListNode(0, head)
        var prev = dummy
        while (prev.next != null) {
            if (values.contains(prev.next.x)) {
                prev.next = prev.next.next
            } else {
                prev = prev.next
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
impl Solution {
    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        use std::collections::HashSet;

        let values: HashSet<i32> = nums.into_iter().collect();
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut prev = &mut dummy;

        while prev.next.is_some() {
            if values.contains(&prev.next.as_ref().unwrap().val) {
                let next = prev.next.as_mut().unwrap().next.take();
                prev.next = next;
            } else {
                prev = prev.next.as_mut().unwrap();
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
; Definition for singly-linked list:
#|

; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))

|#

(define/contract (modified-list nums head)
  (-> (listof exact-integer?) (or/c list-node? #f) (or/c list-node? #f))
  (let ([values (list->set nums)])
    (define dummy (make-list-node 0))
    (set-list-node-next! dummy head)
    (let loop ([prev dummy])
      (define next (list-node-next prev))
      (when next
        (if (set-member? values (list-node-val next))
            (set-list-node-next! prev (list-node-next next))
            (loop next)))
      (when (and next (set-member? values (list-node-val next)))
        (loop prev)))
    (list-node-next dummy)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec modified_list(Nums :: [integer()], Head :: #list_node{} | null) -> #list_node{} | null.
modified_list(Nums, Head) ->
  Values = sets:from_list(Nums),
  Dummy = #list_node{val = 0, next = Head},
  modified_list_loop(Dummy, Values),
  Dummy#list_node.next.

modified_list_loop(Prev, Values) ->
  case Prev#list_node.next of
    null ->
      ok;
    Next ->
      case sets:is_element(Next#list_node.val, Values) of
        true ->
          Prev#list_node{next = Next#list_node.next},
          modified_list_loop(Prev, Values);
        false ->
          modified_list_loop(Next, Values)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
# Definition for singly-linked list.
#
# defmodule ListNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           next: ListNode.t() | nil
#         }
#   defstruct val: 0, next: nil
# end

defmodule Solution do
  @spec modified_list(nums :: [integer], head :: ListNode.t | nil) :: ListNode.t | nil
  def modified_list(nums, head) do
    values = MapSet.new(nums)
    dummy = %ListNode{val: 0, next: head}
    remove_nodes(dummy, values)
    dummy.next
  end

  defp remove_nodes(prev, values) do
    case prev.next do
      nil ->
        :ok

      next ->
        if MapSet.member?(values, next.val) do
          prev.next = next.next
          remove_nodes(prev, values)
        else
          remove_nodes(next, values)
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m + n) expected time, where m is the length of nums and n is the number of list nodes.
- **Space Complexity:** O(m) for the set of values from nums.
