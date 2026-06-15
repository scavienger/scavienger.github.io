---
layout: post
title: "Delete the Middle Node of a Linked List"
date: 2026-06-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Linked List", "Two Pointers"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *   \
        \  int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr)\
        \ {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int\
        \ x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\n\
        public:\n    ListNode* deleteMiddle(ListNode* head) {\n        if (head == nullptr\
        \ || head->next == nullptr) {\n            return nullptr;\n        }\n\n  \
        \      ListNode* slow = head;\n        ListNode* fast = head;\n        ListNode*\
        \ prev = nullptr;\n\n        while (fast != nullptr && fast->next != nullptr)\
        \ {\n            prev = slow;\n            slow = slow->next;\n            fast\
        \ = fast->next->next;\n        }\n\n        prev->next = slow->next;\n     \
        \   return head;\n    }\n};"
      java: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int\
        \ val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val\
        \ = val; this.next = next; }\n * }\n */\nclass Solution {\n    public ListNode\
        \ deleteMiddle(ListNode head) {\n        if (head == null || head.next == null)\
        \ {\n            return null;\n        }\n\n        ListNode slow = head;\n\
        \        ListNode fast = head;\n        ListNode prev = null;\n\n        while\
        \ (fast != null && fast.next != null) {\n            prev = slow;\n        \
        \    slow = slow.next;\n            fast = fast.next.next;\n        }\n\n  \
        \      prev.next = slow.next;\n        return head;\n    }\n}"
      python: "# Definition for singly-linked list.\n# class ListNode(object):\n#  \
        \   def __init__(self, val=0, next=None):\n#         self.val = val\n#     \
        \    self.next = next\nclass Solution(object):\n    def deleteMiddle(self, head):\n\
        \        \"\"\"\n        :type head: Optional[ListNode]\n        :rtype: Optional[ListNode]\n\
        \        \"\"\"\n        if not head or not head.next:\n            return None\n\
        \n        slow = head\n        fast = head\n        prev = None\n\n        while\
        \ fast and fast.next:\n            prev = slow\n            slow = slow.next\n\
        \            fast = fast.next.next\n\n        prev.next = slow.next\n      \
        \  return head"
      python3: "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self,\
        \ val=0, next=None):\n#         self.val = val\n#         self.next = next\n\
        class Solution:\n    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:\n\
        \        if not head or not head.next:\n            return None\n\n        slow\
        \ = head\n        fast = head\n        prev = None\n\n        while fast and\
        \ fast.next:\n            prev = slow\n            slow = slow.next\n      \
        \      fast = fast.next.next\n\n        prev.next = slow.next\n        return\
        \ head"
      c: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int\
        \ val;\n *     struct ListNode *next;\n * };\n */\nstruct ListNode* deleteMiddle(struct\
        \ ListNode* head) {\n    if (head == NULL || head->next == NULL) {\n       \
        \ return NULL;\n    }\n\n    struct ListNode* slow = head;\n    struct ListNode*\
        \ fast = head;\n    struct ListNode* prev = NULL;\n\n    while (fast != NULL\
        \ && fast->next != NULL) {\n        prev = slow;\n        slow = slow->next;\n\
        \        fast = fast->next->next;\n    }\n\n    prev->next = slow->next;\n \
        \   return head;\n}"
      csharp: "/**\n * Definition for singly-linked list.\n * public class ListNode\
        \ {\n *     public int val;\n *     public ListNode next;\n *     public ListNode(int\
        \ val=0, ListNode next=null) {\n *         this.val = val;\n *         this.next\
        \ = next;\n *     }\n * }\n */\npublic class Solution {\n    public ListNode\
        \ DeleteMiddle(ListNode head) {\n        if (head == null) return null;\n\n\
        \        ListNode dummy = new ListNode(0, head);\n        ListNode slow = dummy;\n\
        \        ListNode fast = head;\n\n        while (fast != null && fast.next !=\
        \ null) {\n            slow = slow.next;\n            fast = fast.next.next;\n\
        \        }\n\n        slow.next = slow.next.next;\n        return dummy.next;\n\
        \    }\n}"
      javascript: "/**\n * Definition for singly-linked list.\n * function ListNode(val,\
        \ next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next =\
        \ (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} head\n\
        \ * @return {ListNode}\n */\nvar deleteMiddle = function(head) {\n    if (!head)\
        \ return null;\n\n    const dummy = new ListNode(0, head);\n    let slow = dummy;\n\
        \    let fast = head;\n\n    while (fast !== null && fast.next !== null) {\n\
        \        slow = slow.next;\n        fast = fast.next.next;\n    }\n\n    slow.next\
        \ = slow.next.next;\n    return dummy.next;\n};"
      typescript: "/**\n * Definition for singly-linked list.\n * class ListNode {\n\
        \ *     val: number\n *     next: ListNode | null\n *     constructor(val?:\
        \ number, next?: ListNode | null) {\n *         this.val = (val===undefined\
        \ ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *  \
        \   }\n * }\n */\n\nfunction deleteMiddle(head: ListNode | null): ListNode |\
        \ null {\n    if (!head) return null;\n\n    const dummy = new ListNode(0, head);\n\
        \    let slow: ListNode = dummy;\n    let fast: ListNode | null = head;\n\n\
        \    while (fast !== null && fast.next !== null) {\n        slow = slow.next!;\n\
        \        fast = fast.next.next;\n    }\n\n    if (slow.next !== null) {\n  \
        \      slow.next = slow.next.next;\n    }\n\n    return dummy.next;\n}"
      php: "/**\n * Definition for a singly-linked list.\n * class ListNode {\n *  \
        \   public $val = 0;\n *     public $next = null;\n *     function __construct($val\
        \ = 0, $next = null) {\n *         $this->val = $val;\n *         $this->next\
        \ = $next;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ ListNode $head\n     * @return ListNode\n     */\n    function deleteMiddle($head)\
        \ {\n        if ($head === null) return null;\n\n        $dummy = new ListNode(0,\
        \ $head);\n        $slow = $dummy;\n        $fast = $head;\n\n        while\
        \ ($fast !== null && $fast->next !== null) {\n            $slow = $slow->next;\n\
        \            $fast = $fast->next->next;\n        }\n\n        $slow->next =\
        \ $slow->next->next;\n        return $dummy->next;\n    }\n}"
      swift: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     public var val: Int\n *     public var next: ListNode?\n *     public\
        \ init() { self.val = 0; self.next = nil; }\n *     public init(_ val: Int)\
        \ { self.val = val; self.next = nil; }\n *     public init(_ val: Int, _ next:\
        \ ListNode?) { self.val = val; self.next = next; }\n * }\n */\nclass Solution\
        \ {\n    func deleteMiddle(_ head: ListNode?) -> ListNode? {\n        guard\
        \ let head = head else {\n            return nil\n        }\n\n        let dummy\
        \ = ListNode(0, head)\n        var slow: ListNode? = dummy\n        var fast:\
        \ ListNode? = head\n\n        while fast != nil && fast?.next != nil {\n   \
        \         slow = slow?.next\n            fast = fast?.next?.next\n        }\n\
        \n        slow?.next = slow?.next?.next\n        return dummy.next\n    }\n}"
      kotlin: "/**\n * Example:\n * var li = ListNode(5)\n * var v = li.`val`\n * Definition\
        \ for singly-linked list.\n * class ListNode(var `val`: Int) {\n *     var next:\
        \ ListNode? = null\n * }\n */\nclass Solution {\n    fun deleteMiddle(head:\
        \ ListNode?): ListNode? {\n        if (head?.next == null) return null\n\n \
        \       val dummy = ListNode(0)\n        dummy.next = head\n        var slow:\
        \ ListNode? = dummy\n        var fast: ListNode? = head\n\n        while (fast\
        \ != null && fast.next != null) {\n            slow = slow?.next\n         \
        \   fast = fast.next?.next\n        }\n\n        slow?.next = slow?.next?.next\n\
        \        return dummy.next\n    }\n}"
      dart: "/**\n * Definition for singly-linked list.\n * class ListNode {\n *   int\
        \ val;\n *   ListNode? next;\n *   ListNode([this.val = 0, this.next]);\n *\
        \ }\n */\nclass Solution {\n  ListNode? deleteMiddle(ListNode? head) {\n   \
        \ if (head == null || head.next == null) return null;\n\n    ListNode dummy\
        \ = ListNode(0, head);\n    ListNode? slow = dummy;\n    ListNode? fast = head;\n\
        \n    while (fast != null && fast.next != null) {\n      slow = slow?.next;\n\
        \      fast = fast.next?.next;\n    }\n\n    slow?.next = slow?.next?.next;\n\
        \    return dummy.next;\n  }\n}"
      go: "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *\
        \     Val int\n *     Next *ListNode\n * }\n */\nfunc deleteMiddle(head *ListNode)\
        \ *ListNode {\n    if head == nil || head.Next == nil {\n        return nil\n\
        \    }\n\n    dummy := &ListNode{Val: 0, Next: head}\n    slow := dummy\n  \
        \  fast := head\n\n    for fast != nil && fast.Next != nil {\n        slow =\
        \ slow.Next\n        fast = fast.Next.Next\n    }\n\n    slow.Next = slow.Next.Next\n\
        \    return dummy.Next\n}"
      ruby: "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor\
        \ :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val =\
        \ val\n#         @next = _next\n#     end\n# end\n# @param {ListNode} head\n\
        # @return {ListNode}\ndef delete_middle(head)\n  return nil if head.nil? ||\
        \ head.next.nil?\n\n  dummy = ListNode.new(0, head)\n  slow = dummy\n  fast\
        \ = head\n\n  while fast != nil && fast.next != nil\n    slow = slow.next\n\
        \    fast = fast.next.next\n  end\n\n  slow.next = slow.next.next\n  dummy.next\n\
        end"
      scala: "/**\n * Definition for singly-linked list.\n * class ListNode(_x: Int\
        \ = 0, _next: ListNode = null) {\n *   var next: ListNode = _next\n *   var\
        \ x: Int = _x\n * }\n */\nobject Solution {\n  def deleteMiddle(head: ListNode):\
        \ ListNode = {\n    if (head == null || head.next == null) return null\n\n \
        \   val dummy = new ListNode(0, head)\n    var slow = dummy\n    var fast =\
        \ head\n\n    while (fast != null && fast.next != null) {\n      slow = slow.next\n\
        \      fast = fast.next.next\n    }\n\n    slow.next = slow.next.next\n    dummy.next\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn delete_middle(mut head: Option<Box<ListNode>>)\
        \ -> Option<Box<ListNode>> {\n        if head.is_none() {\n            return\
        \ None;\n        }\n        if head.as_ref().unwrap().next.is_none() {\n   \
        \         return None;\n        }\n\n        let mut n = 0;\n        {\n   \
        \         let mut curr = head.as_ref();\n            while let Some(node) =\
        \ curr {\n                n += 1;\n                curr = node.next.as_ref();\n\
        \            }\n        }\n\n        let mid = n / 2;\n        let mut curr\
        \ = head.as_mut();\n        for _ in 0..(mid - 1) {\n            curr = curr.unwrap().next.as_mut();\n\
        \        }\n\n        if let Some(node) = curr {\n            let mut node_to_delete\
        \ = node.next.take();\n            if let Some(mut nd) = node_to_delete {\n\
        \                node.next = nd.next.take();\n            }\n        }\n\n \
        \       head\n    }\n}"
      racket: "(define/contract (delete-middle head)\n  (-> (or/c list-node? #f) (or/c\
        \ list-node? #f))\n  (if (or (not head) (not (list-node-next head)))\n     \
        \ #f\n      (let* ([n (let loop ([curr head] [count 0])\n                  (if\
        \ curr (loop (list-node-next curr) (+ count 1)) count))]\n             [mid\
        \ (quotient n 2)])\n        (let loop ([curr head] [idx 0])\n          (if (=\
        \ idx (- mid 1))\n              (set-list-node-next! curr (list-node-next (list-node-next\
        \ curr)))\n              (loop (list-node-next curr) (+ idx 1))))\n        head)))"
      erlang: "-spec delete_middle(Head :: #list_node{} | null) -> #list_node{} | null.\n\
        delete_middle(null) -> null;\ndelete_middle(#list_node{next = null}) -> null;\n\
        delete_middle(Head) ->\n  Len = get_len(Head, 0),\n  MidIdx = Len div 2,\n \
        \ remove_at(Head, 0, MidIdx).\n\nget_len(null, Acc) -> Acc;\nget_len(#list_node{next\
        \ = Next}, Acc) -> get_len(Next, Acc + 1).\n\nremove_at(null, _, _) -> null;\n\
        remove_at(Node, Index, MidIdx) when Index =:= MidIdx ->\n  Node#list_node.next;\n\
        remove_at(Node, Index, MidIdx) ->\n  NextNode = remove_at(Node#list_node.next,\
        \ Index + 1, MidIdx),\n  Node#list_node{next = NextNode}."
      elixir: "defmodule Solution do\n  @spec delete_middle(head :: ListNode.t() | nil)\
        \ :: ListNode.t() | nil\n  def delete_middle(nil), do: nil\n  def delete_middle(%ListNode{next:\
        \ nil}), do: nil\n  def delete_middle(head) do\n    len = get_len(head, 0)\n\
        \    mid_idx = div(len, 2)\n    remove_at(head, 0, mid_idx)\n  end\n\n  defp\
        \ get_len(nil, acc), do: acc\n  defp get_len(%ListNode{next: next}, acc), do:\
        \ get_len(next, acc + 1)\n\n  defp remove_at(nil, _, _), do: nil\n  defp remove_at(node,\
        \ idx, mid_idx) when idx == mid_idx do\n    node.next\n  end\n  defp remove_at(node,\
        \ idx, mid_idx) do\n    %{node | next: remove_at(node.next, idx + 1, mid_idx)}\n\
        \  end\nend"
    approach: "To delete the middle node of a linked list, we employ the fast and slow\
      \ pointer technique to find the middle node efficiently in a single pass. We initialize\
      \ two pointers, slow and fast, at the head of the list. By moving the slow pointer\
      \ one step and the fast pointer two steps at each iteration, the slow pointer\
      \ will eventually point to the node at index floor(n/2) when the fast pointer\
      \ reaches the end of the list. \n\nTo perform the deletion, we also track the\
      \ node immediately preceding the slow pointer using a pointer named prev. Before\
      \ the traversal begins, we handle the base case where the list contains only a\
      \ single node, in which case we return null because removing the only node results\
      \ in an empty list. For lists with more than one node, once the middle node is\
      \ identified, we update the next pointer of the prev node to point to the node\
      \ following the slow pointer, effectively bypassing the middle node and removing\
      \ it from the sequence."
    time_complexity: O(n) where n is the number of nodes in the linked list. The algorithm
      traverses the list once using the two-pointer technique, where the fast pointer
      reaches the end of the list in approximately n/2 iterations.
    space_complexity: O(1) because the algorithm only uses a constant amount of extra
      space for the slow, fast, and prev pointers, regardless of the size of the input
      list.
    elapsed_time: 161.21046018600464
    model: gemini-3-flash-preview
    generated_at: '2026-06-15 03:00:09 '
---

## Problem #2095: Delete the Middle Node of a Linked List

**Difficulty:** Medium

**Topics:** Linked List, Two Pointers

## Problem Description

<p>You are given the <code>head</code> of a linked list. <strong>Delete</strong> the <strong>middle node</strong>, and return <em>the</em> <code>head</code> <em>of the modified linked list</em>.</p>

<p>The <strong>middle node</strong> of a linked list of size <code>n</code> is the <code>&lfloor;n / 2&rfloor;<sup>th</sup></code> node from the <b>start</b> using <strong>0-based indexing</strong>, where <code>&lfloor;x&rfloor;</code> denotes the largest integer less than or equal to <code>x</code>.</p>

<ul>
	<li>For <code>n</code> = <code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, and <code>5</code>, the middle nodes are <code>0</code>, <code>1</code>, <code>1</code>, <code>2</code>, and <code>2</code>, respectively.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg1drawio.png" style="width: 500px; height: 77px;" />
<pre>
<strong>Input:</strong> head = [1,3,4,7,1,2,6]
<strong>Output:</strong> [1,3,4,1,2,6]
<strong>Explanation:</strong>
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg2drawio.png" style="width: 250px; height: 43px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong>
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg3drawio.png" style="width: 150px; height: 58px;" />
<pre>
<strong>Input:</strong> head = [2,1]
<strong>Output:</strong> [2]
<strong>Explanation:</strong>
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. If a point with a speed s moves n units in a given time, a point with speed 2 * s will move 2 * n units at the same time. Can you use this to find the middle node of a linked list?

2. If you are given the middle node, the node before it, and the node after it, how can you modify the linked list?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To delete the middle node of a linked list, we employ the fast and slow pointer technique to find the middle node efficiently in a single pass. We initialize two pointers, slow and fast, at the head of the list. By moving the slow pointer one step and the fast pointer two steps at each iteration, the slow pointer will eventually point to the node at index floor(n/2) when the fast pointer reaches the end of the list. 

To perform the deletion, we also track the node immediately preceding the slow pointer using a pointer named prev. Before the traversal begins, we handle the base case where the list contains only a single node, in which case we return null because removing the only node results in an empty list. For lists with more than one node, once the middle node is identified, we update the next pointer of the prev node to point to the node following the slow pointer, effectively bypassing the middle node and removing it from the sequence.

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
    ListNode* deleteMiddle(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return nullptr;
        }

        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;

        while (fast != nullptr && fast->next != nullptr) {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }

        prev->next = slow->next;
        return head;
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
    public ListNode deleteMiddle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }

        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        prev.next = slow.next;
        return head;
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
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
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
struct ListNode* deleteMiddle(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return NULL;
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head;
    struct ListNode* prev = NULL;

    while (fast != NULL && fast->next != NULL) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    prev->next = slow->next;
    return head;
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
    public ListNode DeleteMiddle(ListNode head) {
        if (head == null) return null;

        ListNode dummy = new ListNode(0, head);
        ListNode slow = dummy;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        slow.next = slow.next.next;
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
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (!head) return null;

    const dummy = new ListNode(0, head);
    let slow = dummy;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    slow.next = slow.next.next;
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

function deleteMiddle(head: ListNode | null): ListNode | null {
    if (!head) return null;

    const dummy = new ListNode(0, head);
    let slow: ListNode = dummy;
    let fast: ListNode | null = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    if (slow.next !== null) {
        slow.next = slow.next.next;
    }

    return dummy.next;
}
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
     * @return ListNode
     */
    function deleteMiddle($head) {
        if ($head === null) return null;

        $dummy = new ListNode(0, $head);
        $slow = $dummy;
        $fast = $head;

        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        $slow->next = $slow->next->next;
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
    func deleteMiddle(_ head: ListNode?) -> ListNode? {
        guard let head = head else {
            return nil
        }

        let dummy = ListNode(0, head)
        var slow: ListNode? = dummy
        var fast: ListNode? = head

        while fast != nil && fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }

        slow?.next = slow?.next?.next
        return dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun deleteMiddle(head: ListNode?): ListNode? {
        if (head?.next == null) return null

        val dummy = ListNode(0)
        dummy.next = head
        var slow: ListNode? = dummy
        var fast: ListNode? = head

        while (fast != null && fast.next != null) {
            slow = slow?.next
            fast = fast.next?.next
        }

        slow?.next = slow?.next?.next
        return dummy.next
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  ListNode? deleteMiddle(ListNode? head) {
    if (head == null || head.next == null) return null;

    ListNode dummy = ListNode(0, head);
    ListNode? slow = dummy;
    ListNode? fast = head;

    while (fast != null && fast.next != null) {
      slow = slow?.next;
      fast = fast.next?.next;
    }

    slow?.next = slow?.next?.next;
    return dummy.next;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }

    dummy := &ListNode{Val: 0, Next: head}
    slow := dummy
    fast := head

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    slow.Next = slow.Next.Next
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
# @param {ListNode} head
# @return {ListNode}
def delete_middle(head)
  return nil if head.nil? || head.next.nil?

  dummy = ListNode.new(0, head)
  slow = dummy
  fast = head

  while fast != nil && fast.next != nil
    slow = slow.next
    fast = fast.next.next
  end

  slow.next = slow.next.next
  dummy.next
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
  def deleteMiddle(head: ListNode): ListNode = {
    if (head == null || head.next == null) return null

    val dummy = new ListNode(0, head)
    var slow = dummy
    var fast = head

    while (fast != null && fast.next != null) {
      slow = slow.next
      fast = fast.next.next
    }

    slow.next = slow.next.next
    dummy.next
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn delete_middle(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        }
        if head.as_ref().unwrap().next.is_none() {
            return None;
        }

        let mut n = 0;
        {
            let mut curr = head.as_ref();
            while let Some(node) = curr {
                n += 1;
                curr = node.next.as_ref();
            }
        }

        let mid = n / 2;
        let mut curr = head.as_mut();
        for _ in 0..(mid - 1) {
            curr = curr.unwrap().next.as_mut();
        }

        if let Some(node) = curr {
            let mut node_to_delete = node.next.take();
            if let Some(mut nd) = node_to_delete {
                node.next = nd.next.take();
            }
        }

        head
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (delete-middle head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (or (not head) (not (list-node-next head)))
      #f
      (let* ([n (let loop ([curr head] [count 0])
                  (if curr (loop (list-node-next curr) (+ count 1)) count))]
             [mid (quotient n 2)])
        (let loop ([curr head] [idx 0])
          (if (= idx (- mid 1))
              (set-list-node-next! curr (list-node-next (list-node-next curr)))
              (loop (list-node-next curr) (+ idx 1))))
        head)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec delete_middle(Head :: #list_node{} | null) -> #list_node{} | null.
delete_middle(null) -> null;
delete_middle(#list_node{next = null}) -> null;
delete_middle(Head) ->
  Len = get_len(Head, 0),
  MidIdx = Len div 2,
  remove_at(Head, 0, MidIdx).

get_len(null, Acc) -> Acc;
get_len(#list_node{next = Next}, Acc) -> get_len(Next, Acc + 1).

remove_at(null, _, _) -> null;
remove_at(Node, Index, MidIdx) when Index =:= MidIdx ->
  Node#list_node.next;
remove_at(Node, Index, MidIdx) ->
  NextNode = remove_at(Node#list_node.next, Index + 1, MidIdx),
  Node#list_node{next = NextNode}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec delete_middle(head :: ListNode.t() | nil) :: ListNode.t() | nil
  def delete_middle(nil), do: nil
  def delete_middle(%ListNode{next: nil}), do: nil
  def delete_middle(head) do
    len = get_len(head, 0)
    mid_idx = div(len, 2)
    remove_at(head, 0, mid_idx)
  end

  defp get_len(nil, acc), do: acc
  defp get_len(%ListNode{next: next}, acc), do: get_len(next, acc + 1)

  defp remove_at(nil, _, _), do: nil
  defp remove_at(node, idx, mid_idx) when idx == mid_idx do
    node.next
  end
  defp remove_at(node, idx, mid_idx) do
    %{node | next: remove_at(node.next, idx + 1, mid_idx)}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of nodes in the linked list. The algorithm traverses the list once using the two-pointer technique, where the fast pointer reaches the end of the list in approximately n/2 iterations.
- **Space Complexity:** O(1) because the algorithm only uses a constant amount of extra space for the slow, fast, and prev pointers, regardless of the size of the input list.
