---
layout: post
title: "Maximum Twin Sum of a Linked List"
date: 2026-06-14 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Linked List", "Two Pointers", "Stack"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *   \
        \  int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr)\
        \ {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int\
        \ x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\n\
        public:\n    int pairSum(ListNode* head) {\n        ListNode* slow = head;\n\
        \        ListNode* fast = head;\n        while (fast != nullptr && fast->next\
        \ != nullptr) {\n            slow = slow->next;\n            fast = fast->next->next;\n\
        \        }\n\n        ListNode* prev = nullptr;\n        ListNode* curr = slow;\n\
        \        while (curr != nullptr) {\n            ListNode* nextNode = curr->next;\n\
        \            curr->next = prev;\n            prev = curr;\n            curr\
        \ = nextNode;\n        }\n\n        int maxVal = 0;\n        ListNode* first\
        \ = head;\n        ListNode* second = prev;\n        while (second != nullptr)\
        \ {\n            maxVal = std::max(maxVal, first->val + second->val);\n    \
        \        first = first->next;\n            second = second->next;\n        }\n\
        \n        return maxVal;\n    }\n};"
      java: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int\
        \ val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val\
        \ = val; this.next = next; }\n * }\n */\nclass Solution {\n    public int pairSum(ListNode\
        \ head) {\n        ListNode slow = head;\n        ListNode fast = head;\n  \
        \      while (fast != null && fast.next != null) {\n            slow = slow.next;\n\
        \            fast = fast.next.next;\n        }\n\n        ListNode prev = null;\n\
        \        ListNode curr = slow;\n        while (curr != null) {\n           \
        \ ListNode nextNode = curr.next;\n            curr.next = prev;\n          \
        \  prev = curr;\n            curr = nextNode;\n        }\n\n        int maxVal\
        \ = 0;\n        ListNode first = head;\n        ListNode second = prev;\n  \
        \      while (second != null) {\n            maxVal = Math.max(maxVal, first.val\
        \ + second.val);\n            first = first.next;\n            second = second.next;\n\
        \        }\n\n        return maxVal;\n    }\n}"
      python: "# Definition for singly-linked list.\n# class ListNode(object):\n#  \
        \   def __init__(self, val=0, next=None):\n#         self.val = val\n#     \
        \    self.next = next\nclass Solution(object):\n    def pairSum(self, head):\n\
        \        \"\"\"\n        :type head: Optional[ListNode]\n        :rtype: int\n\
        \        \"\"\"\n        slow = head\n        fast = head\n        while fast\
        \ and fast.next:\n            slow = slow.next\n            fast = fast.next.next\n\
        \n        prev = None\n        curr = slow\n        while curr:\n          \
        \  next_node = curr.next\n            curr.next = prev\n            prev = curr\n\
        \            curr = next_node\n\n        max_sum = 0\n        first = head\n\
        \        second = prev\n        while second:\n            max_sum = max(max_sum,\
        \ first.val + second.val)\n            first = first.next\n            second\
        \ = second.next\n\n        return max_sum"
      python3: "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self,\
        \ val=0, next=None):\n#         self.val = val\n#         self.next = next\n\
        class Solution:\n    def pairSum(self, head: Optional[ListNode]) -> int:\n \
        \       slow = head\n        fast = head\n        while fast and fast.next:\n\
        \            slow = slow.next\n            fast = fast.next.next\n\n       \
        \ prev = None\n        curr = slow\n        while curr:\n            next_node\
        \ = curr.next\n            curr.next = prev\n            prev = curr\n     \
        \       curr = next_node\n\n        max_sum = 0\n        first, second = head,\
        \ prev\n        while second:\n            max_sum = max(max_sum, first.val\
        \ + second.val)\n            first = first.next\n            second = second.next\n\
        \n        return max_sum"
      c: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int\
        \ val;\n *     struct ListNode *next;\n * };\n */\nint pairSum(struct ListNode*\
        \ head) {\n    struct ListNode *slow = head;\n    struct ListNode *fast = head;\n\
        \n    while (fast != NULL && fast->next != NULL) {\n        slow = slow->next;\n\
        \        fast = fast->next->next;\n    }\n\n    struct ListNode *prev = NULL;\n\
        \    struct ListNode *curr = slow;\n    while (curr != NULL) {\n        struct\
        \ ListNode *nextNode = curr->next;\n        curr->next = prev;\n        prev\
        \ = curr;\n        curr = nextNode;\n    }\n\n    int maxVal = 0;\n    struct\
        \ ListNode *p1 = head;\n    struct ListNode *p2 = prev;\n    while (p2 != NULL)\
        \ {\n        int sum = p1->val + p2->val;\n        if (sum > maxVal) {\n   \
        \         maxVal = sum;\n        }\n        p1 = p1->next;\n        p2 = p2->next;\n\
        \    }\n\n    return maxVal;\n}"
      csharp: "/**\n * Definition for singly-linked list.\n * public class ListNode\
        \ {\n *     public int val;\n *     public ListNode next;\n *     public ListNode(int\
        \ val=0, ListNode next=null) {\n *         this.val = val;\n *         this.next\
        \ = next;\n *     }\n * }\n */\npublic class Solution {\n    public int PairSum(ListNode\
        \ head) {\n        ListNode slow = head;\n        ListNode fast = head;\n  \
        \      while (fast != null && fast.next != null) {\n            slow = slow.next;\n\
        \            fast = fast.next.next;\n        }\n\n        ListNode prev = null;\n\
        \        ListNode curr = slow;\n        while (curr != null) {\n           \
        \ ListNode nextNode = curr.next;\n            curr.next = prev;\n          \
        \  prev = curr;\n            curr = nextNode;\n        }\n\n        int maxVal\
        \ = 0;\n        ListNode first = head;\n        ListNode second = prev;\n  \
        \      while (second != null) {\n            maxVal = System.Math.Max(maxVal,\
        \ first.val + second.val);\n            first = first.next;\n            second\
        \ = second.next;\n        }\n\n        return maxVal;\n    }\n}"
      javascript: "/**\n * Definition for singly-linked list.\n * function ListNode(val,\
        \ next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next =\
        \ (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} head\n\
        \ * @return {number}\n */\nvar pairSum = function(head) {\n    let slow = head;\n\
        \    let fast = head;\n    while (fast !== null && fast.next !== null) {\n \
        \       slow = slow.next;\n        fast = fast.next.next;\n    }\n\n    let\
        \ prev = null;\n    let curr = slow;\n    while (curr !== null) {\n        let\
        \ nextNode = curr.next;\n        curr.next = prev;\n        prev = curr;\n \
        \       curr = nextNode;\n    }\n\n    let maxVal = 0;\n    let first = head;\n\
        \    let second = prev;\n    while (second !== null) {\n        maxVal = Math.max(maxVal,\
        \ first.val + second.val);\n        first = first.next;\n        second = second.next;\n\
        \    }\n\n    return maxVal;\n};"
      typescript: "/**\n * Definition for singly-linked list.\n * class ListNode {\n\
        \ *     val: number\n *     next: ListNode | null\n *     constructor(val?:\
        \ number, next?: ListNode | null) {\n *         this.val = (val===undefined\
        \ ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *  \
        \   }\n * }\n */\n\nfunction pairSum(head: ListNode | null): number {\n    let\
        \ slow = head;\n    let fast = head;\n    while (fast !== null && fast.next\
        \ !== null) {\n        slow = slow!.next;\n        fast = fast.next.next;\n\
        \    }\n\n    let prev: ListNode | null = null;\n    let curr = slow;\n    while\
        \ (curr !== null) {\n        let nextNode: ListNode | null = curr.next;\n  \
        \      curr.next = prev;\n        prev = curr;\n        curr = nextNode;\n \
        \   }\n\n    let maxVal = 0;\n    let first = head;\n    let second = prev;\n\
        \    while (second !== null) {\n        maxVal = Math.max(maxVal, first!.val\
        \ + second.val);\n        first = first!.next;\n        second = second.next;\n\
        \    }\n\n    return maxVal;\n};"
      php: "/**\n * Definition for a singly-linked list.\n * class ListNode {\n *  \
        \   public $val = 0;\n *     public $next = null;\n *     function __construct($val\
        \ = 0, $next = null) {\n *         $this->val = $val;\n *         $this->next\
        \ = $next;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ ListNode $head\n     * @return Integer\n     */\n    function pairSum($head)\
        \ {\n        $slow = $head;\n        $fast = $head;\n        while ($fast !==\
        \ null && $fast->next !== null) {\n            $slow = $slow->next;\n      \
        \      $fast = $fast->next->next;\n        }\n\n        $prev = null;\n    \
        \    $curr = $slow;\n        while ($curr !== null) {\n            $nextNode\
        \ = $curr->next;\n            $curr->next = $prev;\n            $prev = $curr;\n\
        \            $curr = $nextNode;\n        }\n\n        $maxVal = 0;\n       \
        \ $first = $head;\n        $second = $prev;\n        while ($second !== null)\
        \ {\n            $currentSum = $first->val + $second->val;\n            if ($currentSum\
        \ > $maxVal) {\n                $maxVal = $currentSum;\n            }\n    \
        \        $first = $first->next;\n            $second = $second->next;\n    \
        \    }\n\n        return $maxVal;\n    }\n}"
      swift: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     public var val: Int\n *     public var next: ListNode?\n *     public\
        \ init() { self.val = 0; self.next = nil; }\n *     public init(_ val: Int)\
        \ { self.val = val; self.next = nil; }\n *     public init(_ val: Int, _ next:\
        \ ListNode?) { self.val = val; self.next = next; }\n * }\n */\nclass Solution\
        \ {\n    func pairSum(_ head: ListNode?) -> Int {\n        var slow = head\n\
        \        var fast = head\n        while fast != nil && fast?.next != nil {\n\
        \            slow = slow?.next\n            fast = fast?.next?.next\n      \
        \  }\n\n        var prev: ListNode? = nil\n        var curr = slow\n       \
        \ while curr != nil {\n            let nextNode = curr?.next\n            curr?.next\
        \ = prev\n            prev = curr\n            curr = nextNode\n        }\n\n\
        \        var maxVal = 0\n        var first = head\n        var second = prev\n\
        \        while second != nil {\n            let currentSum = (first?.val ??\
        \ 0) + (second?.val ?? 0)\n            if currentSum > maxVal {\n          \
        \      maxVal = currentSum\n            }\n            first = first?.next\n\
        \            second = second?.next\n        }\n\n        return maxVal\n   \
        \ }\n}"
      kotlin: "class Solution {\n    fun pairSum(head: ListNode?): Int {\n        var\
        \ slow = head\n        var fast = head\n        while (fast != null && fast.next\
        \ != null) {\n            slow = slow?.next\n            fast = fast.next?.next\n\
        \        }\n\n        var prev: ListNode? = null\n        var curr = slow\n\
        \        while (curr != null) {\n            val nextNode = curr.next\n    \
        \        curr.next = prev\n            prev = curr\n            curr = nextNode\n\
        \        }\n\n        var first = head\n        var second = prev\n        var\
        \ maxVal = 0\n        while (second != null) {\n            val sum = first!!.`val`\
        \ + second.`val`\n            if (sum > maxVal) {\n                maxVal =\
        \ sum\n            }\n            first = first.next\n            second = second.next\n\
        \        }\n        return maxVal\n    }\n}"
      dart: "class Solution {\n  int pairSum(ListNode? head) {\n    ListNode? slow =\
        \ head;\n    ListNode? fast = head;\n    while (fast != null && fast.next !=\
        \ null) {\n      slow = slow?.next;\n      fast = fast.next?.next;\n    }\n\n\
        \    ListNode? prev = null;\n    ListNode? curr = slow;\n    while (curr !=\
        \ null) {\n      ListNode? nextNode = curr.next;\n      curr.next = prev;\n\
        \      prev = curr;\n      curr = nextNode;\n    }\n\n    ListNode? first =\
        \ head;\n    ListNode? second = prev;\n    int maxVal = 0;\n    while (second\
        \ != null) {\n      int sum = first!.val + second!.val;\n      if (sum > maxVal)\
        \ {\n        maxVal = sum;\n      }\n      first = first.next;\n      second\
        \ = second.next;\n    }\n    return maxVal;\n  }\n}"
      go: "func pairSum(head *ListNode) int {\n    slow, fast := head, head\n    for\
        \ fast != nil && fast.Next != nil {\n        slow = slow.Next\n        fast\
        \ = fast.Next.Next\n    }\n\n    var prev *ListNode\n    curr := slow\n    for\
        \ curr != nil {\n        nextNode := curr.Next\n        curr.Next = prev\n \
        \       prev = curr\n        curr = nextNode\n    }\n\n    first, second :=\
        \ head, prev\n    maxVal := 0\n    for second != nil {\n        sum := first.Val\
        \ + second.Val\n        if sum > maxVal {\n            maxVal = sum\n      \
        \  }\n        first = first.Next\n        second = second.Next\n    }\n    return\
        \ maxVal\n}"
      ruby: "def pair_sum(head)\n    slow = head\n    fast = head\n    while fast &&\
        \ fast.next\n        slow = slow.next\n        fast = fast.next.next\n    end\n\
        \n    prev = nil\n    curr = slow\n    while curr\n        next_node = curr.next\n\
        \        curr.next = prev\n        prev = curr\n        curr = next_node\n \
        \   end\n\n    first = head\n    second = prev\n    max_val = 0\n    while second\n\
        \        sum = first.val + second.val\n        max_val = sum if sum > max_val\n\
        \        first = first.next\n        second = second.next\n    end\n    max_val\n\
        end"
      scala: "object Solution {\n    def pairSum(head: ListNode): Int = {\n        var\
        \ slow = head\n        var fast = head\n        while (fast != null && fast.next\
        \ != null) {\n            slow = slow.next\n            fast = fast.next.next\n\
        \        }\n\n        var prev: ListNode = null\n        var curr: ListNode\
        \ = slow\n        while (curr != null) {\n            val nextNode = curr.next\n\
        \            curr.next = prev\n            prev = curr\n            curr = nextNode\n\
        \        }\n\n        var first = head\n        var second = prev\n        var\
        \ maxVal = 0\n        while (second != null) {\n            val sum = first.x\
        \ + second.x\n            if (sum > maxVal) {\n                maxVal = sum\n\
        \            }\n            first = first.next\n            second = second.next\n\
        \        }\n        maxVal\n    }\n}"
      rust: "impl Solution {\n    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32\
        \ {\n        let mut vals = Vec::new();\n        let mut curr = &head;\n   \
        \     while let Some(node) = curr {\n            vals.push(node.val);\n    \
        \        curr = &node.next;\n        }\n        let n = vals.len();\n      \
        \  let mut max_sum = 0;\n        for i in 0..(n / 2) {\n            let sum\
        \ = vals[i] + vals[n - 1 - i];\n            if sum > max_sum {\n           \
        \     max_sum = sum;\n            }\n        }\n        max_sum\n    }\n}"
      racket: "(define/contract (pair-sum head)\n  (-> (or/c list-node? #f) exact-integer?)\n\
        \  (define (to-list curr acc)\n    (if (not curr)\n        (reverse acc)\n \
        \       (to-list (list-node-next curr) (cons (list-node-val curr) acc))))\n\
        \  (let* ([vl (to-list head '())]\n         [v (list->vector vl)]\n        \
        \ [n (vector-length v)]\n         [half (/ n 2)])\n    (let loop ([i 0] [max-s\
        \ 0])\n      (if (< i half)\n          (loop (+ i 1) (max max-s (+ (vector-ref\
        \ v i) (vector-ref v (- n 1 i)))))\n          max-s))))"
      erlang: "pair_sum(Head) ->\n  Vals = get_vals(Head, []),\n  Len = length(Vals),\n\
        \  {First, Second} = lists:split(Len div 2, Vals),\n  RevSecond = lists:reverse(Second),\n\
        \  Sums = lists:zipwith(fun(A, B) -> A + B end, First, RevSecond),\n  lists:max(Sums).\n\
        \nget_vals(null, Acc) -> lists:reverse(Acc);\nget_vals(Node, Acc) -> get_vals(Node#list_node.next,\
        \ [Node#list_node.val | Acc])."
      elixir: "defmodule Solution do\n  @spec pair_sum(head :: ListNode.t | nil) ::\
        \ integer\n  def pair_sum(head) do\n    vals = get_vals(head, [])\n    len =\
        \ length(vals)\n    {first, second} = Enum.split(vals, div(len, 2))\n    rev_second\
        \ = Enum.reverse(second)\n    Enum.zip(first, rev_second)\n    |> Enum.map(fn\
        \ {a, b} -> a + b end)\n    |> Enum.max()\n  end\n\n  defp get_vals(nil, acc),\
        \ do: Enum.reverse(acc)\n  defp get_vals(node, acc), do: get_vals(node.next,\
        \ [node.val | acc])\nend"
    approach: 'The algorithm identifies the maximum twin sum by splitting the linked
      list into two halves and reversing the second half. Since the twins are located
      at symmetric distances from the start and end of the list, we use a slow and fast
      pointer approach to find the middle node efficiently. The slow pointer moves one
      step at a time while the fast pointer moves two steps; when the fast pointer reaches
      the end, the slow pointer points to the start of the second half of the list.


      Once the second half is identified, we reverse it in-place using a standard iterative
      linked list reversal technique. After reversal, we have two separate sub-lists:
      the first half starting from the original head and the second half starting from
      the new head of the reversed segment. We iterate through both pointers simultaneously,
      calculating the sum of values at each step and updating the maximum sum encountered.
      This approach avoids using extra space beyond a few pointers, maintaining the
      original values while reorganizing the list structure.'
    time_complexity: O(n) where n is the number of nodes in the linked list. Finding
      the middle takes n/2 steps, reversing the second half takes n/2 steps, and calculating
      the twin sums takes another n/2 steps, resulting in linear time overall.
    space_complexity: O(1) because the algorithm modifies the linked list in-place to
      reverse the second half. No auxiliary data structures like arrays or stacks are
      used, regardless of the input size.
    elapsed_time: 183.01071858406067
    model: gemini-3-flash-preview
    generated_at: '2026-06-14 02:55:39 '
---

## Problem #2130: Maximum Twin Sum of a Linked List

**Difficulty:** Medium

**Topics:** Linked List, Two Pointers, Stack

## Problem Description

<p>In a linked list of size <code>n</code>, where <code>n</code> is <strong>even</strong>, the <code>i<sup>th</sup></code> node (<strong>0-indexed</strong>) of the linked list is known as the <strong>twin</strong> of the <code>(n-1-i)<sup>th</sup></code> node, if <code>0 &lt;= i &lt;= (n / 2) - 1</code>.</p>

<ul>
	<li>For example, if <code>n = 4</code>, then node <code>0</code> is the twin of node <code>3</code>, and node <code>1</code> is the twin of node <code>2</code>. These are the only nodes with twins for <code>n = 4</code>.</li>
</ul>

<p>The <strong>twin sum </strong>is defined as the sum of a node and its twin.</p>

<p>Given the <code>head</code> of a linked list with even length, return <em>the <strong>maximum twin sum</strong> of the linked list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/03/eg1drawio.png" style="width: 250px; height: 70px;" />
<pre>
<strong>Input:</strong> head = [5,4,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong>
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/03/eg2drawio.png" style="width: 250px; height: 70px;" />
<pre>
<strong>Input:</strong> head = [4,2,2,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/03/eg3drawio.png" style="width: 200px; height: 88px;" />
<pre>
<strong>Input:</strong> head = [1,100000]
<strong>Output:</strong> 100001
<strong>Explanation:</strong>
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is an <strong>even</strong> integer in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. How can "reversing" a part of the linked list help find the answer?

2. We know that the nodes of the first half are twins of nodes in the second half, so try dividing the linked list in half and reverse the second half.

3. How can two pointers be used to find every twin sum optimally?

4. Use two different pointers pointing to the first nodes of the two halves of the linked list. The second pointer will point to the first node of the reversed half, which is the (n-1-i)th node in the original linked list. By moving both pointers forward at the same time, we find all twin sums.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm identifies the maximum twin sum by splitting the linked list into two halves and reversing the second half. Since the twins are located at symmetric distances from the start and end of the list, we use a slow and fast pointer approach to find the middle node efficiently. The slow pointer moves one step at a time while the fast pointer moves two steps; when the fast pointer reaches the end, the slow pointer points to the start of the second half of the list.

Once the second half is identified, we reverse it in-place using a standard iterative linked list reversal technique. After reversal, we have two separate sub-lists: the first half starting from the original head and the second half starting from the new head of the reversed segment. We iterate through both pointers simultaneously, calculating the sum of values at each step and updating the maximum sum encountered. This approach avoids using extra space beyond a few pointers, maintaining the original values while reorganizing the list structure.

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
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* prev = nullptr;
        ListNode* curr = slow;
        while (curr != nullptr) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }

        int maxVal = 0;
        ListNode* first = head;
        ListNode* second = prev;
        while (second != nullptr) {
            maxVal = std::max(maxVal, first->val + second->val);
            first = first->next;
            second = second->next;
        }

        return maxVal;
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
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        int maxVal = 0;
        ListNode first = head;
        ListNode second = prev;
        while (second != null) {
            maxVal = Math.max(maxVal, first.val + second.val);
            first = first.next;
            second = second.next;
        }

        return maxVal;
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
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        max_sum = 0
        first = head
        second = prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
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
int pairSum(struct ListNode* head) {
    struct ListNode *slow = head;
    struct ListNode *fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode *prev = NULL;
    struct ListNode *curr = slow;
    while (curr != NULL) {
        struct ListNode *nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }

    int maxVal = 0;
    struct ListNode *p1 = head;
    struct ListNode *p2 = prev;
    while (p2 != NULL) {
        int sum = p1->val + p2->val;
        if (sum > maxVal) {
            maxVal = sum;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    return maxVal;
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
    public int PairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode prev = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        int maxVal = 0;
        ListNode first = head;
        ListNode second = prev;
        while (second != null) {
            maxVal = System.Math.Max(maxVal, first.val + second.val);
            first = first.next;
            second = second.next;
        }

        return maxVal;
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
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function(head) {
    let slow = head;
    let fast = head;
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let prev = null;
    let curr = slow;
    while (curr !== null) {
        let nextNode = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextNode;
    }

    let maxVal = 0;
    let first = head;
    let second = prev;
    while (second !== null) {
        maxVal = Math.max(maxVal, first.val + second.val);
        first = first.next;
        second = second.next;
    }

    return maxVal;
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

function pairSum(head: ListNode | null): number {
    let slow = head;
    let fast = head;
    while (fast !== null && fast.next !== null) {
        slow = slow!.next;
        fast = fast.next.next;
    }

    let prev: ListNode | null = null;
    let curr = slow;
    while (curr !== null) {
        let nextNode: ListNode | null = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextNode;
    }

    let maxVal = 0;
    let first = head;
    let second = prev;
    while (second !== null) {
        maxVal = Math.max(maxVal, first!.val + second.val);
        first = first!.next;
        second = second.next;
    }

    return maxVal;
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
     * @param ListNode $head
     * @return Integer
     */
    function pairSum($head) {
        $slow = $head;
        $fast = $head;
        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        $prev = null;
        $curr = $slow;
        while ($curr !== null) {
            $nextNode = $curr->next;
            $curr->next = $prev;
            $prev = $curr;
            $curr = $nextNode;
        }

        $maxVal = 0;
        $first = $head;
        $second = $prev;
        while ($second !== null) {
            $currentSum = $first->val + $second->val;
            if ($currentSum > $maxVal) {
                $maxVal = $currentSum;
            }
            $first = $first->next;
            $second = $second->next;
        }

        return $maxVal;
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
    func pairSum(_ head: ListNode?) -> Int {
        var slow = head
        var fast = head
        while fast != nil && fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }

        var prev: ListNode? = nil
        var curr = slow
        while curr != nil {
            let nextNode = curr?.next
            curr?.next = prev
            prev = curr
            curr = nextNode
        }

        var maxVal = 0
        var first = head
        var second = prev
        while second != nil {
            let currentSum = (first?.val ?? 0) + (second?.val ?? 0)
            if currentSum > maxVal {
                maxVal = currentSum
            }
            first = first?.next
            second = second?.next
        }

        return maxVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun pairSum(head: ListNode?): Int {
        var slow = head
        var fast = head
        while (fast != null && fast.next != null) {
            slow = slow?.next
            fast = fast.next?.next
        }

        var prev: ListNode? = null
        var curr = slow
        while (curr != null) {
            val nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        }

        var first = head
        var second = prev
        var maxVal = 0
        while (second != null) {
            val sum = first!!.`val` + second.`val`
            if (sum > maxVal) {
                maxVal = sum
            }
            first = first.next
            second = second.next
        }
        return maxVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int pairSum(ListNode? head) {
    ListNode? slow = head;
    ListNode? fast = head;
    while (fast != null && fast.next != null) {
      slow = slow?.next;
      fast = fast.next?.next;
    }

    ListNode? prev = null;
    ListNode? curr = slow;
    while (curr != null) {
      ListNode? nextNode = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nextNode;
    }

    ListNode? first = head;
    ListNode? second = prev;
    int maxVal = 0;
    while (second != null) {
      int sum = first!.val + second!.val;
      if (sum > maxVal) {
        maxVal = sum;
      }
      first = first.next;
      second = second.next;
    }
    return maxVal;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func pairSum(head *ListNode) int {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    var prev *ListNode
    curr := slow
    for curr != nil {
        nextNode := curr.Next
        curr.Next = prev
        prev = curr
        curr = nextNode
    }

    first, second := head, prev
    maxVal := 0
    for second != nil {
        sum := first.Val + second.Val
        if sum > maxVal {
            maxVal = sum
        }
        first = first.Next
        second = second.Next
    }
    return maxVal
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def pair_sum(head)
    slow = head
    fast = head
    while fast && fast.next
        slow = slow.next
        fast = fast.next.next
    end

    prev = nil
    curr = slow
    while curr
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    end

    first = head
    second = prev
    max_val = 0
    while second
        sum = first.val + second.val
        max_val = sum if sum > max_val
        first = first.next
        second = second.next
    end
    max_val
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def pairSum(head: ListNode): Int = {
        var slow = head
        var fast = head
        while (fast != null && fast.next != null) {
            slow = slow.next
            fast = fast.next.next
        }

        var prev: ListNode = null
        var curr: ListNode = slow
        while (curr != null) {
            val nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        }

        var first = head
        var second = prev
        var maxVal = 0
        while (second != null) {
            val sum = first.x + second.x
            if (sum > maxVal) {
                maxVal = sum
            }
            first = first.next
            second = second.next
        }
        maxVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let mut vals = Vec::new();
        let mut curr = &head;
        while let Some(node) = curr {
            vals.push(node.val);
            curr = &node.next;
        }
        let n = vals.len();
        let mut max_sum = 0;
        for i in 0..(n / 2) {
            let sum = vals[i] + vals[n - 1 - i];
            if sum > max_sum {
                max_sum = sum;
            }
        }
        max_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (pair-sum head)
  (-> (or/c list-node? #f) exact-integer?)
  (define (to-list curr acc)
    (if (not curr)
        (reverse acc)
        (to-list (list-node-next curr) (cons (list-node-val curr) acc))))
  (let* ([vl (to-list head '())]
         [v (list->vector vl)]
         [n (vector-length v)]
         [half (/ n 2)])
    (let loop ([i 0] [max-s 0])
      (if (< i half)
          (loop (+ i 1) (max max-s (+ (vector-ref v i) (vector-ref v (- n 1 i)))))
          max-s))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
pair_sum(Head) ->
  Vals = get_vals(Head, []),
  Len = length(Vals),
  {First, Second} = lists:split(Len div 2, Vals),
  RevSecond = lists:reverse(Second),
  Sums = lists:zipwith(fun(A, B) -> A + B end, First, RevSecond),
  lists:max(Sums).

get_vals(null, Acc) -> lists:reverse(Acc);
get_vals(Node, Acc) -> get_vals(Node#list_node.next, [Node#list_node.val | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec pair_sum(head :: ListNode.t | nil) :: integer
  def pair_sum(head) do
    vals = get_vals(head, [])
    len = length(vals)
    {first, second} = Enum.split(vals, div(len, 2))
    rev_second = Enum.reverse(second)
    Enum.zip(first, rev_second)
    |> Enum.map(fn {a, b} -> a + b end)
    |> Enum.max()
  end

  defp get_vals(nil, acc), do: Enum.reverse(acc)
  defp get_vals(node, acc), do: get_vals(node.next, [node.val | acc])
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of nodes in the linked list. Finding the middle takes n/2 steps, reversing the second half takes n/2 steps, and calculating the twin sums takes another n/2 steps, resulting in linear time overall.
- **Space Complexity:** O(1) because the algorithm modifies the linked list in-place to reverse the second half. No auxiliary data structures like arrays or stacks are used, regardless of the input size.
