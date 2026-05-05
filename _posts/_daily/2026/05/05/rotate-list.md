---
layout: post
title: "Rotate List"
date: 2026-05-05 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Linked List", "Two Pointers"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/rotate-list/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *   \
        \  int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr)\
        \ {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int\
        \ x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\n\
        public:\n    ListNode* rotateRight(ListNode* head, int k) {\n        if (!head\
        \ || !head->next || k == 0) return head;\n\n        ListNode* tail = head;\n\
        \        int n = 1;\n        while (tail->next) {\n            tail = tail->next;\n\
        \            n++;\n        }\n\n        k %= n;\n        if (k == 0) return\
        \ head;\n\n        tail->next = head;\n        ListNode* newTail = head;\n \
        \       for (int i = 0; i < n - k - 1; i++) {\n            newTail = newTail->next;\n\
        \        }\n\n        ListNode* newHead = newTail->next;\n        newTail->next\
        \ = nullptr;\n        return newHead;\n    }\n};"
      java: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int\
        \ val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val\
        \ = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode\
        \ rotateRight(ListNode head, int k) {\n        if (head == null || head.next\
        \ == null || k == 0) return head;\n\n        ListNode tail = head;\n       \
        \ int n = 1;\n        while (tail.next != null) {\n            tail = tail.next;\n\
        \            n++;\n        }\n\n        k %= n;\n        if (k == 0) return\
        \ head;\n\n        tail.next = head;\n        ListNode newTail = head;\n   \
        \     for (int i = 0; i < n - k - 1; i++) {\n            newTail = newTail.next;\n\
        \        }\n\n        ListNode newHead = newTail.next;\n        newTail.next\
        \ = null;\n        return newHead;\n    }\n}"
      python: "# Definition for singly-linked list.\n# class ListNode(object):\n#  \
        \   def __init__(self, val=0, next=None):\n#         self.val = val\n#     \
        \    self.next = next\nclass Solution(object):\n    def rotateRight(self, head,\
        \ k):\n        \"\"\"\n        :type head: Optional[ListNode]\n        :type\
        \ k: int\n        :rtype: Optional[ListNode]\n        \"\"\"\n        if not\
        \ head or not head.next or k == 0:\n            return head\n\n        n = 1\n\
        \        tail = head\n        while tail.next:\n            tail = tail.next\n\
        \            n += 1\n\n        k %= n\n        if k == 0:\n            return\
        \ head\n\n        tail.next = head\n        new_tail = head\n        for _ in\
        \ range(n - k - 1):\n            new_tail = new_tail.next\n\n        new_head\
        \ = new_tail.next\n        new_tail.next = None\n        return new_head"
      python3: "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self,\
        \ val=0, next=None):\n#         self.val = val\n#         self.next = next\n\
        class Solution:\n    def rotateRight(self, head: Optional[ListNode], k: int)\
        \ -> Optional[ListNode]:\n        if not head or not head.next or k == 0:\n\
        \            return head\n\n        n = 1\n        tail = head\n        while\
        \ tail.next:\n            tail = tail.next\n            n += 1\n\n        k\
        \ %= n\n        if k == 0:\n            return head\n\n        tail.next = head\n\
        \        new_tail = head\n        for _ in range(n - k - 1):\n            new_tail\
        \ = new_tail.next\n\n        new_head = new_tail.next\n        new_tail.next\
        \ = None\n        return new_head"
      c: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int\
        \ val;\n *     struct ListNode *next;\n * };\n */\nstruct ListNode* rotateRight(struct\
        \ ListNode* head, int k) {\n    if (!head || !head->next || k == 0) return head;\n\
        \n    struct ListNode* tail = head;\n    int n = 1;\n    while (tail->next)\
        \ {\n        tail = tail->next;\n        n++;\n    }\n\n    k %= n;\n    if\
        \ (k == 0) return head;\n\n    tail->next = head;\n    struct ListNode* newTail\
        \ = head;\n    for (int i = 0; i < n - k - 1; i++) {\n        newTail = newTail->next;\n\
        \    }\n\n    struct ListNode* newHead = newTail->next;\n    newTail->next =\
        \ NULL;\n    return newHead;\n}"
      csharp: "/**\n * Definition for singly-linked list.\n * public class ListNode\
        \ {\n *     public int val;\n *     public ListNode next;\n *     public ListNode(int\
        \ val=0, ListNode next=null) {\n *         this.val = val;\n *         this.next\
        \ = next;\n *     }\n * }\n */\npublic class Solution {\n    public ListNode\
        \ RotateRight(ListNode head, int k) {\n        if (head == null || head.next\
        \ == null || k == 0) {\n            return head;\n        }\n\n        int length\
        \ = 1;\n        ListNode tail = head;\n        while (tail.next != null) {\n\
        \            tail = tail.next;\n            length++;\n        }\n\n       \
        \ k = k % length;\n        if (k == 0) {\n            return head;\n       \
        \ }\n\n        tail.next = head;\n        ListNode newTail = head;\n       \
        \ for (int i = 0; i < length - k - 1; i++) {\n            newTail = newTail.next;\n\
        \        }\n\n        ListNode newHead = newTail.next;\n        newTail.next\
        \ = null;\n\n        return newHead;\n    }\n}"
      javascript: "/**\n * Definition for singly-linked list.\n * function ListNode(val,\
        \ next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next =\
        \ (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} head\n\
        \ * @param {number} k\n * @return {ListNode}\n */\nvar rotateRight = function(head,\
        \ k) {\n    if (!head || !head.next || k === 0) {\n        return head;\n  \
        \  }\n\n    let length = 1;\n    let tail = head;\n    while (tail.next) {\n\
        \        tail = tail.next;\n        length++;\n    }\n\n    k = k % length;\n\
        \    if (k === 0) {\n        return head;\n    }\n\n    tail.next = head;\n\
        \    let newTail = head;\n    for (let i = 0; i < length - k - 1; i++) {\n \
        \       newTail = newTail.next;\n    }\n\n    let newHead = newTail.next;\n\
        \    newTail.next = null;\n\n    return newHead;\n};"
      typescript: "/**\n * Definition for singly-linked list.\n * class ListNode {\n\
        \ *     val: number\n *     next: ListNode | null\n *     constructor(val?:\
        \ number, next?: ListNode | null) {\n *         this.val = (val===undefined\
        \ ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *  \
        \   }\n * }\n */\n\nfunction rotateRight(head: ListNode | null, k: number):\
        \ ListNode | null {\n    if (!head || !head.next || k === 0) {\n        return\
        \ head;\n    }\n\n    let length = 1;\n    let tail: ListNode = head;\n    while\
        \ (tail.next) {\n        tail = tail.next;\n        length++;\n    }\n\n   \
        \ k = k % length;\n    if (k === 0) {\n        return head;\n    }\n\n    tail.next\
        \ = head;\n    let newTail: ListNode = head;\n    for (let i = 0; i < length\
        \ - k - 1; i++) {\n        newTail = newTail.next!;\n    }\n\n    let newHead\
        \ = newTail.next;\n    newTail.next = null;\n\n    return newHead;\n};"
      php: "/**\n * Definition for a singly-linked list.\n * class ListNode {\n *  \
        \   public $val = 0;\n *     public $next = null;\n *     function __construct($val\
        \ = 0, $next = null) {\n *         $this->val = $val;\n *         $this->next\
        \ = $next;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ ListNode $head\n     * @param Integer $k\n     * @return ListNode\n     */\n\
        \    function rotateRight($head, $k) {\n        if ($head === null || $head->next\
        \ === null || $k === 0) {\n            return $head;\n        }\n\n        $length\
        \ = 1;\n        $tail = $head;\n        while ($tail->next !== null) {\n   \
        \         $tail = $tail->next;\n            $length++;\n        }\n\n      \
        \  $k = $k % $length;\n        if ($k === 0) {\n            return $head;\n\
        \        }\n\n        $tail->next = $head;\n        $newTail = $head;\n    \
        \    for ($i = 0; $i < $length - $k - 1; $i++) {\n            $newTail = $newTail->next;\n\
        \        }\n\n        $newHead = $newTail->next;\n        $newTail->next = null;\n\
        \n        return $newHead;\n    }\n}"
      swift: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     public var val: Int\n *     public var next: ListNode?\n *     public\
        \ init() { self.val = 0; self.next = nil; }\n *     public init(_ val: Int)\
        \ { self.val = val; self.next = nil; }\n *     public init(_ val: Int, _ next:\
        \ ListNode?) { self.val = val; self.next = next; }\n * }\n */\nclass Solution\
        \ {\n    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {\n    \
        \    guard let head = head, head.next != nil, k > 0 else {\n            return\
        \ head\n        }\n\n        var length = 1\n        var tail = head\n     \
        \   while let next = tail.next {\n            tail = next\n            length\
        \ += 1\n        }\n\n        let rotateCount = k % length\n        if rotateCount\
        \ == 0 {\n            return head\n        }\n\n        tail.next = head\n \
        \       var newTail = head\n        let stepsToNewTail = length - rotateCount\
        \ - 1\n        for _ in 0..<stepsToNewTail {\n            if let next = newTail.next\
        \ {\n                newTail = next\n            }\n        }\n\n        let\
        \ newHead = newTail.next\n        newTail.next = nil\n\n        return newHead\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun rotateRight(head: ListNode?, k: Int): ListNode?\
        \ {\n        if (head == null || head.next == null || k == 0) return head\n\n\
        \        var n = 1\n        var tail: ListNode = head\n        while (tail.next\
        \ != null) {\n            tail = tail.next!!\n            n++\n        }\n\n\
        \        val rotateK = k % n\n        if (rotateK == 0) return head\n\n    \
        \    tail.next = head\n        var newTail: ListNode = head\n        for (i\
        \ in 0 until (n - rotateK - 1)) {\n            newTail = newTail.next!!\n  \
        \      }\n\n        val newHead = newTail.next\n        newTail.next = null\n\
        \n        return newHead\n    }\n}"
      dart: "class Solution {\n  ListNode? rotateRight(ListNode? head, int k) {\n  \
        \  if (head == null || head.next == null || k == 0) return head;\n\n    int\
        \ n = 1;\n    ListNode tail = head;\n    while (tail.next != null) {\n     \
        \ tail = tail.next!;\n      n++;\n    }\n\n    int rotateK = k % n;\n    if\
        \ (rotateK == 0) return head;\n\n    tail.next = head;\n    ListNode newTail\
        \ = head;\n    for (int i = 0; i < n - rotateK - 1; i++) {\n      newTail =\
        \ newTail.next!;\n    }\n\n    ListNode? newHead = newTail.next;\n    newTail.next\
        \ = null;\n\n    return newHead;\n  }\n}"
      go: "func rotateRight(head *ListNode, k int) *ListNode {\n    if head == nil ||\
        \ head.Next == nil || k == 0 {\n        return head\n    }\n\n    n := 1\n \
        \   tail := head\n    for tail.Next != nil {\n        tail = tail.Next\n   \
        \     n++\n    }\n\n    rotateK := k % n\n    if rotateK == 0 {\n        return\
        \ head\n    }\n\n    tail.Next = head\n    newTail := head\n    for i := 0;\
        \ i < n - rotateK - 1; i++ {\n        newTail = newTail.Next\n    }\n\n    newHead\
        \ := newTail.Next\n    newTail.Next = nil\n\n    return newHead\n}"
      ruby: "def rotate_right(head, k)\n    return head if head.nil? || head.next.nil?\
        \ || k == 0\n\n    n = 1\n    tail = head\n    while tail.next\n        tail\
        \ = tail.next\n        n += 1\n    end\n\n    rotate_k = k % n\n    return head\
        \ if rotate_k == 0\n\n    tail.next = head\n    new_tail = head\n    (n - rotate_k\
        \ - 1).times do\n        new_tail = new_tail.next\n    end\n\n    new_head =\
        \ new_tail.next\n    new_tail.next = nil\n\n    new_head\nend"
      scala: "object Solution {\n    def rotateRight(head: ListNode, k: Int): ListNode\
        \ = {\n        if (head == null || head.next == null || k == 0) return head\n\
        \n        var n = 1\n        var tail = head\n        while (tail.next != null)\
        \ {\n            tail = tail.next\n            n += 1\n        }\n\n       \
        \ val rotateK = k % n\n        if (rotateK == 0) return head\n\n        tail.next\
        \ = head\n        var newTail = head\n        for (i <- 0 until (n - rotateK\
        \ - 1)) {\n            newTail = newTail.next\n        }\n\n        val newHead\
        \ = newTail.next\n        newTail.next = null\n\n        newHead\n    }\n}"
      rust: "impl Solution {\n    pub fn rotate_right(head: Option<Box<ListNode>>, k:\
        \ i32) -> Option<Box<ListNode>> {\n        if head.is_none() || k == 0 {\n \
        \           return head;\n        }\n        let mut n = 0;\n        {\n   \
        \         let mut curr = &head;\n            while let Some(node) = curr {\n\
        \                n += 1;\n                curr = &node.next;\n            }\n\
        \        }\n        let k_eff = (k as usize) % n;\n        if k_eff == 0 {\n\
        \            return head;\n        }\n\n        let mut nodes = Vec::new();\n\
        \        let mut curr_head = head;\n        while let Some(mut node) = curr_head\
        \ {\n            let next = node.next.take();\n            nodes.push(node);\n\
        \            curr_head = next;\n        }\n\n        let split_idx = n - k_eff;\n\
        \        let mut tail_part = nodes.split_off(split_idx);\n        tail_part.extend(nodes);\n\
        \n        let mut result = None;\n        for mut node in tail_part.into_iter().rev()\
        \ {\n            node.next = result;\n            result = Some(node);\n   \
        \     }\n        result\n    }\n}"
      racket: "(define/contract (rotate-right head k)\n  (-> (or/c list-node? #f) exact-integer?\
        \ (or/c list-node? #f))\n  (if (or (not head) (not (list-node-next head)))\n\
        \      head\n      (let* ([nodes (let loop ([curr head] [acc '()])\n       \
        \               (if (not curr)\n                          (reverse acc)\n  \
        \                        (loop (list-node-next curr) (cons curr acc))))]\n \
        \            [n (length nodes)]\n             [k-eff (remainder k n)])\n   \
        \     (if (= k-eff 0)\n            head\n            (let* ([split-idx (- n\
        \ k-eff)]\n                   [new-tail (list-ref nodes (- split-idx 1))]\n\
        \                   [new-head (list-ref nodes split-idx)]\n                \
        \   [old-tail (list-ref nodes (- n 1))])\n              (set-list-node-next!\
        \ old-tail head)\n              (set-list-node-next! new-tail #f)\n        \
        \      new-head))))\n  )"
      erlang: "rotate_right(null, _) -> null;\nrotate_right(Head, K) ->\n    List =\
        \ to_list(Head),\n    Len = length(List),\n    RealK = K rem Len,\n    case\
        \ RealK of\n        0 -> Head;\n        _ ->\n            {Part1, Part2} = lists:split(Len\
        \ - RealK, List),\n            from_list(Part2 ++ Part1)\n    end.\n\nto_list(null)\
        \ -> [];\nto_list(#list_node{val = V, next = Next}) -> [V | to_list(Next)].\n\
        \nfrom_list([]) -> null;\nfrom_list([H | T]) -> #list_node{val = H, next = from_list(T)}."
      elixir: "defmodule Solution do\n  @spec rotate_right(head :: ListNode.t | nil,\
        \ k :: integer) :: ListNode.t | nil\n  def rotate_right(head, k) do\n    if\
        \ head == nil do\n      nil\n    else\n      list = to_list(head)\n      len\
        \ = length(list)\n      k_eff = rem(k, len)\n      if k_eff == 0 do\n      \
        \  head\n      else\n        {part1, part2} = Enum.split(list, len - k_eff)\n\
        \        from_list(part2 ++ part1)\n      end\n    end\n  end\n\n  defp to_list(nil),\
        \ do: []\n  defp to_list(%ListNode{val: v, next: next}), do: [v | to_list(next)]\n\
        \n  defp from_list([]), do: nil\n  defp from_list([h | t]), do: %ListNode{val:\
        \ h, next: from_list(t)}\nend"
    approach: 'The core logic of the algorithm relies on identifying the rotation as
      a cyclic shift, which can be efficiently handled by temporarily turning the singly-linked
      list into a circular linked list. First, we traverse the list to determine its
      length $n$ and keep a reference to the last node. Since rotating a list of length
      $n$ by $k$ positions is equivalent to rotating it by $k \pmod n$ positions, we
      compute the effective $k$. This step is crucial for handling cases where $k$ is
      much larger than $n$, ensuring the algorithm remains performant regardless of
      the magnitude of $k$.


      Once we have the total length and the effective $k$, we link the tail''s next
      pointer to the head, making the list circular. To find the new tail of the rotated
      list, we traverse $n - (k \pmod n) - 1$ steps from the original head. The node
      immediately following this new tail becomes the new head of our rotated list.
      Finally, we break the circular connection by setting the new tail''s next pointer
      to null and return the new head pointer. This approach ensures we only traverse
      the list twice at most, resulting in linear efficiency.'
    time_complexity: O(n) where $n$ is the number of nodes in the linked list. The algorithm
      performs one full traversal to find the length of the list and the tail node,
      and a partial traversal of at most $n-1$ nodes to find the new head position.
    space_complexity: O(1) because the rotation is performed entirely in-place. We only
      maintain a few auxiliary pointers to track the tail, the head, and the new split
      point, regardless of the size of the input list.
    elapsed_time: 156.22388815879822
    model: gemini-3-flash-preview
    generated_at: '2026-05-05 02:09:07 '
---

## Problem #61: Rotate List

**Difficulty:** Medium

**Topics:** Linked List, Two Pointers

## Problem Description

<p>Given the <code>head</code> of a linked&nbsp;list, rotate the list to the right by <code>k</code> places.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 450px; height: 191px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 305px; height: 350px;" />
<pre>
<strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 500]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core logic of the algorithm relies on identifying the rotation as a cyclic shift, which can be efficiently handled by temporarily turning the singly-linked list into a circular linked list. First, we traverse the list to determine its length $n$ and keep a reference to the last node. Since rotating a list of length $n$ by $k$ positions is equivalent to rotating it by $k \pmod n$ positions, we compute the effective $k$. This step is crucial for handling cases where $k$ is much larger than $n$, ensuring the algorithm remains performant regardless of the magnitude of $k$.

Once we have the total length and the effective $k$, we link the tail's next pointer to the head, making the list circular. To find the new tail of the rotated list, we traverse $n - (k \pmod n) - 1$ steps from the original head. The node immediately following this new tail becomes the new head of our rotated list. Finally, we break the circular connection by setting the new tail's next pointer to null and return the new head pointer. This approach ensures we only traverse the list twice at most, resulting in linear efficiency.

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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;

        ListNode* tail = head;
        int n = 1;
        while (tail->next) {
            tail = tail->next;
            n++;
        }

        k %= n;
        if (k == 0) return head;

        tail->next = head;
        ListNode* newTail = head;
        for (int i = 0; i < n - k - 1; i++) {
            newTail = newTail->next;
        }

        ListNode* newHead = newTail->next;
        newTail->next = nullptr;
        return newHead;
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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;

        ListNode tail = head;
        int n = 1;
        while (tail.next != null) {
            tail = tail.next;
            n++;
        }

        k %= n;
        if (k == 0) return head;

        tail.next = head;
        ListNode newTail = head;
        for (int i = 0; i < n - k - 1; i++) {
            newTail = newTail.next;
        }

        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
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
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        tail.next = head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        tail.next = head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
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
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;

    struct ListNode* tail = head;
    int n = 1;
    while (tail->next) {
        tail = tail->next;
        n++;
    }

    k %= n;
    if (k == 0) return head;

    tail->next = head;
    struct ListNode* newTail = head;
    for (int i = 0; i < n - k - 1; i++) {
        newTail = newTail->next;
    }

    struct ListNode* newHead = newTail->next;
    newTail->next = NULL;
    return newHead;
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
    public ListNode RotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }

        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        k = k % length;
        if (k == 0) {
            return head;
        }

        tail.next = head;
        ListNode newTail = head;
        for (int i = 0; i < length - k - 1; i++) {
            newTail = newTail.next;
        }

        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
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
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (!head || !head.next || k === 0) {
        return head;
    }

    let length = 1;
    let tail = head;
    while (tail.next) {
        tail = tail.next;
        length++;
    }

    k = k % length;
    if (k === 0) {
        return head;
    }

    tail.next = head;
    let newTail = head;
    for (let i = 0; i < length - k - 1; i++) {
        newTail = newTail.next;
    }

    let newHead = newTail.next;
    newTail.next = null;

    return newHead;
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

function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if (!head || !head.next || k === 0) {
        return head;
    }

    let length = 1;
    let tail: ListNode = head;
    while (tail.next) {
        tail = tail.next;
        length++;
    }

    k = k % length;
    if (k === 0) {
        return head;
    }

    tail.next = head;
    let newTail: ListNode = head;
    for (let i = 0; i < length - k - 1; i++) {
        newTail = newTail.next!;
    }

    let newHead = newTail.next;
    newTail.next = null;

    return newHead;
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
     * @param Integer $k
     * @return ListNode
     */
    function rotateRight($head, $k) {
        if ($head === null || $head->next === null || $k === 0) {
            return $head;
        }

        $length = 1;
        $tail = $head;
        while ($tail->next !== null) {
            $tail = $tail->next;
            $length++;
        }

        $k = $k % $length;
        if ($k === 0) {
            return $head;
        }

        $tail->next = $head;
        $newTail = $head;
        for ($i = 0; $i < $length - $k - 1; $i++) {
            $newTail = $newTail->next;
        }

        $newHead = $newTail->next;
        $newTail->next = null;

        return $newHead;
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
    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {
        guard let head = head, head.next != nil, k > 0 else {
            return head
        }

        var length = 1
        var tail = head
        while let next = tail.next {
            tail = next
            length += 1
        }

        let rotateCount = k % length
        if rotateCount == 0 {
            return head
        }

        tail.next = head
        var newTail = head
        let stepsToNewTail = length - rotateCount - 1
        for _ in 0..<stepsToNewTail {
            if let next = newTail.next {
                newTail = next
            }
        }

        let newHead = newTail.next
        newTail.next = nil

        return newHead
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun rotateRight(head: ListNode?, k: Int): ListNode? {
        if (head == null || head.next == null || k == 0) return head

        var n = 1
        var tail: ListNode = head
        while (tail.next != null) {
            tail = tail.next!!
            n++
        }

        val rotateK = k % n
        if (rotateK == 0) return head

        tail.next = head
        var newTail: ListNode = head
        for (i in 0 until (n - rotateK - 1)) {
            newTail = newTail.next!!
        }

        val newHead = newTail.next
        newTail.next = null

        return newHead
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  ListNode? rotateRight(ListNode? head, int k) {
    if (head == null || head.next == null || k == 0) return head;

    int n = 1;
    ListNode tail = head;
    while (tail.next != null) {
      tail = tail.next!;
      n++;
    }

    int rotateK = k % n;
    if (rotateK == 0) return head;

    tail.next = head;
    ListNode newTail = head;
    for (int i = 0; i < n - rotateK - 1; i++) {
      newTail = newTail.next!;
    }

    ListNode? newHead = newTail.next;
    newTail.next = null;

    return newHead;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil || k == 0 {
        return head
    }

    n := 1
    tail := head
    for tail.Next != nil {
        tail = tail.Next
        n++
    }

    rotateK := k % n
    if rotateK == 0 {
        return head
    }

    tail.Next = head
    newTail := head
    for i := 0; i < n - rotateK - 1; i++ {
        newTail = newTail.Next
    }

    newHead := newTail.Next
    newTail.Next = nil

    return newHead
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def rotate_right(head, k)
    return head if head.nil? || head.next.nil? || k == 0

    n = 1
    tail = head
    while tail.next
        tail = tail.next
        n += 1
    end

    rotate_k = k % n
    return head if rotate_k == 0

    tail.next = head
    new_tail = head
    (n - rotate_k - 1).times do
        new_tail = new_tail.next
    end

    new_head = new_tail.next
    new_tail.next = nil

    new_head
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def rotateRight(head: ListNode, k: Int): ListNode = {
        if (head == null || head.next == null || k == 0) return head

        var n = 1
        var tail = head
        while (tail.next != null) {
            tail = tail.next
            n += 1
        }

        val rotateK = k % n
        if (rotateK == 0) return head

        tail.next = head
        var newTail = head
        for (i <- 0 until (n - rotateK - 1)) {
            newTail = newTail.next
        }

        val newHead = newTail.next
        newTail.next = null

        newHead
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn rotate_right(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if head.is_none() || k == 0 {
            return head;
        }
        let mut n = 0;
        {
            let mut curr = &head;
            while let Some(node) = curr {
                n += 1;
                curr = &node.next;
            }
        }
        let k_eff = (k as usize) % n;
        if k_eff == 0 {
            return head;
        }

        let mut nodes = Vec::new();
        let mut curr_head = head;
        while let Some(mut node) = curr_head {
            let next = node.next.take();
            nodes.push(node);
            curr_head = next;
        }

        let split_idx = n - k_eff;
        let mut tail_part = nodes.split_off(split_idx);
        tail_part.extend(nodes);

        let mut result = None;
        for mut node in tail_part.into_iter().rev() {
            node.next = result;
            result = Some(node);
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (rotate-right head k)
  (-> (or/c list-node? #f) exact-integer? (or/c list-node? #f))
  (if (or (not head) (not (list-node-next head)))
      head
      (let* ([nodes (let loop ([curr head] [acc '()])
                      (if (not curr)
                          (reverse acc)
                          (loop (list-node-next curr) (cons curr acc))))]
             [n (length nodes)]
             [k-eff (remainder k n)])
        (if (= k-eff 0)
            head
            (let* ([split-idx (- n k-eff)]
                   [new-tail (list-ref nodes (- split-idx 1))]
                   [new-head (list-ref nodes split-idx)]
                   [old-tail (list-ref nodes (- n 1))])
              (set-list-node-next! old-tail head)
              (set-list-node-next! new-tail #f)
              new-head))))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
rotate_right(null, _) -> null;
rotate_right(Head, K) ->
    List = to_list(Head),
    Len = length(List),
    RealK = K rem Len,
    case RealK of
        0 -> Head;
        _ ->
            {Part1, Part2} = lists:split(Len - RealK, List),
            from_list(Part2 ++ Part1)
    end.

to_list(null) -> [];
to_list(#list_node{val = V, next = Next}) -> [V | to_list(Next)].

from_list([]) -> null;
from_list([H | T]) -> #list_node{val = H, next = from_list(T)}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec rotate_right(head :: ListNode.t | nil, k :: integer) :: ListNode.t | nil
  def rotate_right(head, k) do
    if head == nil do
      nil
    else
      list = to_list(head)
      len = length(list)
      k_eff = rem(k, len)
      if k_eff == 0 do
        head
      else
        {part1, part2} = Enum.split(list, len - k_eff)
        from_list(part2 ++ part1)
      end
    end
  end

  defp to_list(nil), do: []
  defp to_list(%ListNode{val: v, next: next}), do: [v | to_list(next)]

  defp from_list([]), do: nil
  defp from_list([h | t]), do: %ListNode{val: h, next: from_list(t)}
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where $n$ is the number of nodes in the linked list. The algorithm performs one full traversal to find the length of the list and the tail node, and a partial traversal of at most $n-1$ nodes to find the new head position.
- **Space Complexity:** O(1) because the rotation is performed entirely in-place. We only maintain a few auxiliary pointers to track the tail, the head, and the new split point, regardless of the size of the input list.
