---
layout: post
title: "Create Binary Tree From Descriptions"
date: 2026-06-07 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Tree", "Binary Tree"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/create-binary-tree-from-descriptions/
ai_solutions:
  - solutions:
      cpp: "#include <unordered_map>\n#include <unordered_set>\n#include <vector>\n\n\
        /**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode() :\
        \ val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution\
        \ {\npublic:\n    TreeNode* createBinaryTree(std::vector<std::vector<int>>&\
        \ descriptions) {\n        std::unordered_map<int, TreeNode*> nodes;\n     \
        \   std::unordered_set<int> children;\n\n        for (const auto& desc : descriptions)\
        \ {\n            int parentVal = desc[0];\n            int childVal = desc[1];\n\
        \            bool isLeft = desc[2];\n\n            if (nodes.find(parentVal)\
        \ == nodes.end()) {\n                nodes[parentVal] = new TreeNode(parentVal);\n\
        \            }\n            if (nodes.find(childVal) == nodes.end()) {\n   \
        \             nodes[childVal] = new TreeNode(childVal);\n            }\n\n \
        \           if (isLeft) {\n                nodes[parentVal]->left = nodes[childVal];\n\
        \            } else {\n                nodes[parentVal]->right = nodes[childVal];\n\
        \            }\n            children.insert(childVal);\n        }\n\n      \
        \  for (const auto& desc : descriptions) {\n            if (children.find(desc[0])\
        \ == children.end()) {\n                return nodes[desc[0]];\n           \
        \ }\n        }\n\n        return nullptr;\n    }\n};"
      java: "import java.util.HashMap;\nimport java.util.HashSet;\nimport java.util.Map;\n\
        import java.util.Set;\n\n/**\n * Definition for a binary tree node.\n * public\
        \ class TreeNode {\n *     int val;\n *     TreeNode left;\n *     TreeNode\
        \ right;\n *     TreeNode() {}\n *     TreeNode(int val) { this.val = val; }\n\
        \ *     TreeNode(int val, TreeNode left, TreeNode right) {\n *         this.val\
        \ = val;\n *         this.left = left;\n *         this.right = right;\n * \
        \    }\n * }\n */\nclass Solution {\n    public TreeNode createBinaryTree(int[][]\
        \ descriptions) {\n        Map<Integer, TreeNode> nodes = new HashMap<>();\n\
        \        Set<Integer> children = new HashSet<>();\n\n        for (int[] desc\
        \ : descriptions) {\n            int parentVal = desc[0];\n            int childVal\
        \ = desc[1];\n            int isLeft = desc[2];\n\n            nodes.putIfAbsent(parentVal,\
        \ new TreeNode(parentVal));\n            nodes.putIfAbsent(childVal, new TreeNode(childVal));\n\
        \n            if (isLeft == 1) {\n                nodes.get(parentVal).left\
        \ = nodes.get(childVal);\n            } else {\n                nodes.get(parentVal).right\
        \ = nodes.get(childVal);\n            }\n            children.add(childVal);\n\
        \        }\n\n        for (int[] desc : descriptions) {\n            if (!children.contains(desc[0]))\
        \ {\n                return nodes.get(desc[0]);\n            }\n        }\n\n\
        \        return null;\n    }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n\
        \    def createBinaryTree(self, descriptions):\n        \"\"\"\n        :type\
        \ descriptions: List[List[int]]\n        :rtype: Optional[TreeNode]\n      \
        \  \"\"\"\n        nodes = {}\n        children = set()\n\n        for p, c,\
        \ is_left in descriptions:\n            if p not in nodes:\n               \
        \ nodes[p] = TreeNode(p)\n            if c not in nodes:\n                nodes[c]\
        \ = TreeNode(c)\n\n            if is_left:\n                nodes[p].left =\
        \ nodes[c]\n            else:\n                nodes[p].right = nodes[c]\n\n\
        \            children.add(c)\n\n        for p, c, is_left in descriptions:\n\
        \            if p not in children:\n                return nodes[p]\n\n    \
        \    return None"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nclass Solution:\n    def createBinaryTree(self,\
        \ descriptions: List[List[int]]) -> Optional[TreeNode]:\n        nodes = {}\n\
        \        children = set()\n\n        for p, c, is_left in descriptions:\n  \
        \          if p not in nodes:\n                nodes[p] = TreeNode(p)\n    \
        \        if c not in nodes:\n                nodes[c] = TreeNode(c)\n\n    \
        \        if is_left:\n                nodes[p].left = nodes[c]\n           \
        \ else:\n                nodes[p].right = nodes[c]\n\n            children.add(c)\n\
        \n        for p, c, is_left in descriptions:\n            if p not in children:\n\
        \                return nodes[p]\n\n        return None"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n\n/**\n * Definition for a binary\
        \ tree node.\n * struct TreeNode {\n *     int val;\n *     struct TreeNode\
        \ *left;\n *     struct TreeNode *right;\n * };\n */\nstruct TreeNode* createBinaryTree(int**\
        \ descriptions, int descriptionsSize, int* descriptionsColSize) {\n    struct\
        \ TreeNode** nodeMap = (struct TreeNode**)calloc(100001, sizeof(struct TreeNode*));\n\
        \    bool* hasParent = (bool*)calloc(100001, sizeof(bool));\n\n    for (int\
        \ i = 0; i < descriptionsSize; i++) {\n        int pVal = descriptions[i][0];\n\
        \        int cVal = descriptions[i][1];\n        int isLeft = descriptions[i][2];\n\
        \n        if (nodeMap[pVal] == NULL) {\n            nodeMap[pVal] = (struct\
        \ TreeNode*)malloc(sizeof(struct TreeNode));\n            nodeMap[pVal]->val\
        \ = pVal;\n            nodeMap[pVal]->left = NULL;\n            nodeMap[pVal]->right\
        \ = NULL;\n        }\n        if (nodeMap[cVal] == NULL) {\n            nodeMap[cVal]\
        \ = (struct TreeNode*)malloc(sizeof(struct TreeNode));\n            nodeMap[cVal]->val\
        \ = cVal;\n            nodeMap[cVal]->left = NULL;\n            nodeMap[cVal]->right\
        \ = NULL;\n        }\n\n        if (isLeft == 1) {\n            nodeMap[pVal]->left\
        \ = nodeMap[cVal];\n        } else {\n            nodeMap[pVal]->right = nodeMap[cVal];\n\
        \        }\n        hasParent[cVal] = true;\n    }\n\n    struct TreeNode* root\
        \ = NULL;\n    for (int i = 0; i < descriptionsSize; i++) {\n        int pVal\
        \ = descriptions[i][0];\n        if (!hasParent[pVal]) {\n            root =\
        \ nodeMap[pVal];\n            break;\n        }\n    }\n\n    free(hasParent);\n\
        \    free(nodeMap);\n    return root;\n}"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     }\n * }\n */\npublic class Solution {\n    public TreeNode\
        \ CreateBinaryTree(int[][] descriptions) {\n        Dictionary<int, TreeNode>\
        \ nodeMap = new Dictionary<int, TreeNode>();\n        HashSet<int> childNodes\
        \ = new HashSet<int>();\n\n        foreach (int[] d in descriptions) {\n   \
        \         int parentVal = d[0];\n            int childVal = d[1];\n        \
        \    bool isLeft = d[2] == 1;\n\n            if (!nodeMap.ContainsKey(parentVal))\
        \ {\n                nodeMap[parentVal] = new TreeNode(parentVal);\n       \
        \     }\n            if (!nodeMap.ContainsKey(childVal)) {\n               \
        \ nodeMap[childVal] = new TreeNode(childVal);\n            }\n\n           \
        \ if (isLeft) {\n                nodeMap[parentVal].left = nodeMap[childVal];\n\
        \            } else {\n                nodeMap[parentVal].right = nodeMap[childVal];\n\
        \            }\n\n            childNodes.Add(childVal);\n        }\n\n     \
        \   foreach (var entry in nodeMap) {\n            if (!childNodes.Contains(entry.Key))\
        \ {\n                return entry.Value;\n            }\n        }\n\n     \
        \   return null;\n    }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {number[][]} descriptions\n * @return\
        \ {TreeNode}\n */\nvar createBinaryTree = function(descriptions) {\n    const\
        \ nodeMap = new Map();\n    const children = new Set();\n\n    for (const [parentVal,\
        \ childVal, isLeft] of descriptions) {\n        if (!nodeMap.has(parentVal))\
        \ {\n            nodeMap.set(parentVal, new TreeNode(parentVal));\n        }\n\
        \        if (!nodeMap.has(childVal)) {\n            nodeMap.set(childVal, new\
        \ TreeNode(childVal));\n        }\n\n        const parentNode = nodeMap.get(parentVal);\n\
        \        const childNode = nodeMap.get(childVal);\n\n        if (isLeft ===\
        \ 1) {\n            parentNode.left = childNode;\n        } else {\n       \
        \     parentNode.right = childNode;\n        }\n\n        children.add(childVal);\n\
        \    }\n\n    for (const [val, node] of nodeMap) {\n        if (!children.has(val))\
        \ {\n            return node;\n        }\n    }\n\n    return null;\n};"
      typescript: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n\
        \ *     val: number\n *     left: TreeNode | null\n *     right: TreeNode |\
        \ null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode\
        \ | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left\
        \ = (left===undefined ? null : left)\n *         this.right = (right===undefined\
        \ ? null : right)\n *     }\n * }\n */\n\nfunction createBinaryTree(descriptions:\
        \ number[][]): TreeNode | null {\n    const nodeMap = new Map<number, TreeNode>();\n\
        \    const children = new Set<number>();\n\n    for (const [parentVal, childVal,\
        \ isLeft] of descriptions) {\n        if (!nodeMap.has(parentVal)) {\n     \
        \       nodeMap.set(parentVal, new TreeNode(parentVal));\n        }\n      \
        \  if (!nodeMap.has(childVal)) {\n            nodeMap.set(childVal, new TreeNode(childVal));\n\
        \        }\n\n        const parentNode = nodeMap.get(parentVal)!;\n        const\
        \ childNode = nodeMap.get(childVal)!;\n\n        if (isLeft === 1) {\n     \
        \       parentNode.left = childNode;\n        } else {\n            parentNode.right\
        \ = childNode;\n        }\n\n        children.add(childVal);\n    }\n\n    for\
        \ (const [val, node] of nodeMap.entries()) {\n        if (!children.has(val))\
        \ {\n            return node;\n        }\n    }\n\n    return null;\n}"
      php: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *    \
        \ public $val = null;\n *     public $left = null;\n *     public $right = null;\n\
        \ *     function __construct($val = 0, $left = null, $right = null) {\n *  \
        \       this.val = $val;\n *         this.left = $left;\n *         this.right\
        \ = $right;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ Integer[][] $descriptions\n     * @return TreeNode\n     */\n    function\
        \ createBinaryTree($descriptions) {\n        $nodeMap = [];\n        $children\
        \ = [];\n\n        foreach ($descriptions as $d) {\n            $pVal = $d[0];\n\
        \            $cVal = $d[1];\n            $isLeft = $d[2];\n\n            if\
        \ (!isset($nodeMap[$pVal])) {\n                $nodeMap[$pVal] = new TreeNode($pVal);\n\
        \            }\n            if (!isset($nodeMap[$cVal])) {\n               \
        \ $nodeMap[$cVal] = new TreeNode($cVal);\n            }\n\n            if ($isLeft\
        \ == 1) {\n                $nodeMap[$pVal]->left = $nodeMap[$cVal];\n      \
        \      } else {\n                $nodeMap[$pVal]->right = $nodeMap[$cVal];\n\
        \            }\n\n            $children[$cVal] = true;\n        }\n\n      \
        \  foreach ($nodeMap as $val => $node) {\n            if (!isset($children[$val]))\
        \ {\n                return $node;\n            }\n        }\n\n        return\
        \ null;\n    }\n}"
      swift: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     public var val: Int\n *     public var left: TreeNode?\n *     public\
        \ var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil;\
        \ self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left\
        \ = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?,\
        \ _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n\
        \ *         self.right = right\n *     }\n * }\n */\nclass Solution {\n    func\
        \ createBinaryTree(_ descriptions: [[Int]]) -> TreeNode? {\n        var nodeMap\
        \ = [Int: TreeNode]()\n        var children = Set<Int>()\n\n        for d in\
        \ descriptions {\n            let parentVal = d[0]\n            let childVal\
        \ = d[1]\n            let isLeft = d[2] == 1\n\n            if nodeMap[parentVal]\
        \ == nil {\n                nodeMap[parentVal] = TreeNode(parentVal)\n     \
        \       }\n            if nodeMap[childVal] == nil {\n                nodeMap[childVal]\
        \ = TreeNode(childVal)\n            }\n\n            let parentNode = nodeMap[parentVal]!\n\
        \            let childNode = nodeMap[childVal]!\n\n            if isLeft {\n\
        \                parentNode.left = childNode\n            } else {\n       \
        \         parentNode.right = childNode\n            }\n\n            children.insert(childVal)\n\
        \        }\n\n        for (val, node) in nodeMap {\n            if !children.contains(val)\
        \ {\n                return node\n            }\n        }\n\n        return\
        \ nil\n    }\n}"
      kotlin: "class Solution {\n    fun createBinaryTree(descriptions: Array<IntArray>):\
        \ TreeNode? {\n        val nodes = mutableMapOf<Int, TreeNode>()\n        val\
        \ children = mutableSetOf<Int>()\n\n        for (desc in descriptions) {\n \
        \           val parentVal = desc[0]\n            val childVal = desc[1]\n  \
        \          val isLeft = desc[2] == 1\n\n            val parentNode = nodes.getOrPut(parentVal)\
        \ { TreeNode(parentVal) }\n            val childNode = nodes.getOrPut(childVal)\
        \ { TreeNode(childVal) }\n\n            if (isLeft) {\n                parentNode.left\
        \ = childNode\n            } else {\n                parentNode.right = childNode\n\
        \            }\n            children.add(childVal)\n        }\n\n        for\
        \ (desc in descriptions) {\n            val parentVal = desc[0]\n          \
        \  if (!children.contains(parentVal)) {\n                return nodes[parentVal]\n\
        \            }\n        }\n\n        return null\n    }\n}"
      dart: "class Solution {\n  TreeNode? createBinaryTree(List<List<int>> descriptions)\
        \ {\n    Map<int, TreeNode> nodes = {};\n    Set<int> children = {};\n\n   \
        \ for (var desc in descriptions) {\n      int pVal = desc[0];\n      int cVal\
        \ = desc[1];\n      bool isLeft = desc[2] == 1;\n\n      TreeNode pNode = nodes.putIfAbsent(pVal,\
        \ () => TreeNode(pVal));\n      TreeNode cNode = nodes.putIfAbsent(cVal, ()\
        \ => TreeNode(cVal));\n\n      if (isLeft) {\n        pNode.left = cNode;\n\
        \      } else {\n        pNode.right = cNode;\n      }\n      children.add(cVal);\n\
        \    }\n\n    for (var desc in descriptions) {\n      int pVal = desc[0];\n\
        \      if (!children.contains(pVal)) {\n        return nodes[pVal];\n      }\n\
        \    }\n\n    return null;\n  }\n}"
      go: "func createBinaryTree(descriptions [][]int) *TreeNode {\n    nodes := make(map[int]*TreeNode)\n\
        \    isChild := make(map[int]bool)\n\n    for _, desc := range descriptions\
        \ {\n        pVal, cVal, isLeft := desc[0], desc[1], desc[2] == 1\n\n      \
        \  if _, exists := nodes[pVal]; !exists {\n            nodes[pVal] = &TreeNode{Val:\
        \ pVal}\n        }\n        if _, exists := nodes[cVal]; !exists {\n       \
        \     nodes[cVal] = &TreeNode{Val: cVal}\n        }\n\n        if isLeft {\n\
        \            nodes[pVal].Left = nodes[cVal]\n        } else {\n            nodes[pVal].Right\
        \ = nodes[cVal]\n        }\n        isChild[cVal] = true\n    }\n\n    for _,\
        \ desc := range descriptions {\n        pVal := desc[0]\n        if !isChild[pVal]\
        \ {\n            return nodes[pVal]\n        }\n    }\n\n    return nil\n}"
      ruby: "def create_binary_tree(descriptions)\n    nodes = {}\n    children = {}\n\
        \n    descriptions.each do |p_val, c_val, is_left|\n        nodes[p_val] ||=\
        \ TreeNode.new(p_val)\n        nodes[c_val] ||= TreeNode.new(c_val)\n\n    \
        \    if is_left == 1\n            nodes[p_val].left = nodes[c_val]\n       \
        \ else\n            nodes[p_val].right = nodes[c_val]\n        end\n       \
        \ children[c_val] = true\n    end\n\n    descriptions.each do |p_val, c_val,\
        \ is_left|\n        return nodes[p_val] unless children.has_key?(p_val)\n  \
        \  end\n\n    nil\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def createBinaryTree(descriptions:\
        \ Array[Array[Int]]): TreeNode = {\n        val nodes = mutable.Map[Int, TreeNode]()\n\
        \        val children = mutable.Set[Int]()\n\n        for (desc <- descriptions)\
        \ {\n            val pVal = desc(0)\n            val cVal = desc(1)\n      \
        \      val isLeft = desc(2) == 1\n\n            val pNode = nodes.getOrElseUpdate(pVal,\
        \ new TreeNode(pVal))\n            val cNode = nodes.getOrElseUpdate(cVal, new\
        \ TreeNode(cVal))\n\n            if (isLeft) {\n                pNode.left =\
        \ cNode\n            } else {\n                pNode.right = cNode\n       \
        \     }\n            children.add(cVal)\n        }\n\n        var root: TreeNode\
        \ = null\n        for (desc <- descriptions) {\n            val pVal = desc(0)\n\
        \            if (!children.contains(pVal)) {\n                root = nodes(pVal)\n\
        \            }\n        }\n        root\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\nuse std::collections::{HashMap,\
        \ HashSet};\n\nimpl Solution {\n    pub fn create_binary_tree(descriptions:\
        \ Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {\n        let mut nodes:\
        \ HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();\n        let mut children:\
        \ HashSet<i32> = HashSet::new();\n\n        for desc in &descriptions {\n  \
        \          let parent_val = desc[0];\n            let child_val = desc[1];\n\
        \            let is_left = desc[2] == 1;\n\n            let parent = nodes\n\
        \                .entry(parent_val)\n                .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(parent_val))))\n\
        \                .clone();\n            let child = nodes\n                .entry(child_val)\n\
        \                .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(child_val))))\n\
        \                .clone();\n\n            if is_left {\n                parent.borrow_mut().left\
        \ = Some(child);\n            } else {\n                parent.borrow_mut().right\
        \ = Some(child);\n            }\n            children.insert(child_val);\n \
        \       }\n\n        for desc in descriptions {\n            let parent_val\
        \ = desc[0];\n            if !children.contains(&parent_val) {\n           \
        \     return nodes.get(&parent_val).cloned();\n            }\n        }\n\n\
        \        None\n    }\n}"
      racket: "(define/contract (create-binary-tree descriptions)\n  (-> (listof (listof\
        \ exact-integer?)) (or/c tree-node? #f))\n  (let ([nodes (make-hash)]\n    \
        \    [children (mutable-set)])\n    (for ([desc descriptions])\n      (let*\
        \ ([p-val (first desc)]\n             [c-val (second desc)]\n             [is-left\
        \ (= (third desc) 1)])\n        (let ([p-node (hash-ref! nodes p-val (lambda\
        \ () (make-tree-node p-val)))]\n              [c-node (hash-ref! nodes c-val\
        \ (lambda () (make-tree-node c-val)))])\n          (if is-left\n           \
        \   (set-tree-node-left! p-node c-node)\n              (set-tree-node-right!\
        \ p-node c-node))\n          (set-add! children c-val))))\n    (let loop ([ds\
        \ descriptions])\n      (if (null? ds)\n          #f\n          (let ([p-val\
        \ (first (first ds))])\n            (if (not (set-member? children p-val))\n\
        \                (hash-ref nodes p-val)\n                (loop (rest ds))))))))"
      erlang: "create_binary_tree(Descriptions) ->\n  {Adj, Children} = lists:foldl(fun([P,\
        \ C, L], {AccAdj, AccChild}) ->\n    {Left, Right} = maps:get(P, AccAdj, {null,\
        \ null}),\n    NewAdj = case L of\n      1 -> maps:put(P, {C, Right}, AccAdj);\n\
        \      0 -> maps:put(P, {Left, C}, AccAdj)\n    end,\n    {NewAdj, sets:add_element(C,\
        \ AccChild)}\n  end, {maps:new(), sets:new()}, Descriptions),\n\n  RootVal =\
        \ find_root(Descriptions, Children),\n  build_tree(RootVal, Adj).\n\nfind_root([[P,\
        \ _, _] | T], Children) ->\n  case sets:is_element(P, Children) of\n    true\
        \ -> find_root(T, Children);\n    false -> P\n  end.\n\nbuild_tree(null, _)\
        \ -> null;\nbuild_tree(Val, Adj) ->\n  {LVal, RVal} = maps:get(Val, Adj, {null,\
        \ null}),\n  #tree_node{val = Val,\n             left = build_tree(LVal, Adj),\n\
        \             right = build_tree(RVal, Adj)}."
      elixir: "defmodule Solution do\n  @spec create_binary_tree(descriptions :: [[integer]])\
        \ :: TreeNode.t | nil\n  def create_binary_tree(descriptions) do\n    {adj,\
        \ children} = Enum.reduce(descriptions, {%{}, MapSet.new()}, fn [p, c, l], {adj_acc,\
        \ child_acc} ->\n      {left, right} = Map.get(adj_acc, p, {nil, nil})\n   \
        \   new_adj_val = if l == 1, do: {c, right}, else: {left, c}\n      {Map.put(adj_acc,\
        \ p, new_adj_val), MapSet.put(child_acc, c)}\n    end)\n\n    root_val = Enum.find_value(descriptions,\
        \ fn [p, _, _] ->\n      if !MapSet.member?(children, p), do: p, else: nil\n\
        \    end)\n\n    build_tree(root_val, adj)\n  end\n\n  defp build_tree(nil,\
        \ _), do: nil\n  defp build_tree(val, adj) do\n    {l_val, r_val} = Map.get(adj,\
        \ val, {nil, nil})\n    %TreeNode{\n      val: val,\n      left: build_tree(l_val,\
        \ adj),\n      right: build_tree(r_val, adj)\n    }\n  end\nend"
    approach: 'The algorithm constructs the binary tree by mapping each unique value
      to its corresponding TreeNode object using a hash map (or an array for languages
      with fixed value ranges). As we iterate through each description, we either retrieve
      the existing parent and child nodes from the map or create new ones if they have
      not been encountered yet. Based on the third element of each description, we assign
      the child node as either the left or right child of the parent node.


      To identify the root of the tree, we maintain a collection (like a hash set or
      boolean array) of all nodes that appear as a child in any description. Since the
      problem guarantees a valid binary tree, the root is the only node that appears
      as a parent but never as a child. After processing all descriptions to build the
      tree, we perform a second pass to find the node whose value is missing from the
      child collection, and we return its corresponding TreeNode object as the root.'
    time_complexity: O(N) where N is the number of descriptions. We process each description
      in the list once to create and link nodes, with each map/set operation taking
      constant time on average. A second iteration through the descriptions (or a scan
      of the parent values) allows us to identify the root node in linear time.
    space_complexity: O(N) where N is the number of descriptions. We store at most 2N
      unique nodes in a hash map and a set of up to N child nodes to distinguish the
      root. In the C solution, an array of size 100,001 is used to manage the potential
      range of node values, which remains O(N + V) where V is the value range, but effectively
      linear relative to the input size constraints.
    elapsed_time: 87.35974764823914
    model: gemini-3-flash-preview
    generated_at: '2026-06-07 02:50:03 '
---

## Problem #2196: Create Binary Tree From Descriptions

**Difficulty:** Medium

**Topics:** Array, Hash Table, Tree, Binary Tree

## Problem Description

<p>You are given a 2D integer array <code>descriptions</code> where <code>descriptions[i] = [parent<sub>i</sub>, child<sub>i</sub>, isLeft<sub>i</sub>]</code> indicates that <code>parent<sub>i</sub></code> is the <strong>parent</strong> of <code>child<sub>i</sub></code> in a <strong>binary</strong> tree of <strong>unique</strong> values. Furthermore,</p>

<ul>
	<li>If <code>isLeft<sub>i</sub> == 1</code>, then <code>child<sub>i</sub></code> is the left child of <code>parent<sub>i</sub></code>.</li>
	<li>If <code>isLeft<sub>i</sub> == 0</code>, then <code>child<sub>i</sub></code> is the right child of <code>parent<sub>i</sub></code>.</li>
</ul>

<p>Construct the binary tree described by <code>descriptions</code> and return <em>its <strong>root</strong></em>.</p>

<p>The test cases will be generated such that the binary tree is <strong>valid</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png" style="width: 300px; height: 236px;" />
<pre>
<strong>Input:</strong> descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
<strong>Output:</strong> [50,20,80,15,17,19]
<strong>Explanation:</strong> The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png" style="width: 131px; height: 300px;" />
<pre>
<strong>Input:</strong> descriptions = [[1,2,1],[2,3,0],[3,4,1]]
<strong>Output:</strong> [1,2,null,null,3,4]
<strong>Explanation:</strong> The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= descriptions.length &lt;= 10<sup>4</sup></code></li>
	<li><code>descriptions[i].length == 3</code></li>
	<li><code>1 &lt;= parent<sub>i</sub>, child<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= isLeft<sub>i</sub> &lt;= 1</code></li>
	<li>The binary tree described by <code>descriptions</code> is valid.</li>
</ul>


## Hints

1. Could you represent and store the descriptions more efficiently?

2. Could you find the root node?

3. The node that is not a child in any of the descriptions is the root node.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm constructs the binary tree by mapping each unique value to its corresponding TreeNode object using a hash map (or an array for languages with fixed value ranges). As we iterate through each description, we either retrieve the existing parent and child nodes from the map or create new ones if they have not been encountered yet. Based on the third element of each description, we assign the child node as either the left or right child of the parent node.

To identify the root of the tree, we maintain a collection (like a hash set or boolean array) of all nodes that appear as a child in any description. Since the problem guarantees a valid binary tree, the root is the only node that appears as a parent but never as a child. After processing all descriptions to build the tree, we perform a second pass to find the node whose value is missing from the child collection, and we return its corresponding TreeNode object as the root.

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
#include <unordered_map>
#include <unordered_set>
#include <vector>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* createBinaryTree(std::vector<std::vector<int>>& descriptions) {
        std::unordered_map<int, TreeNode*> nodes;
        std::unordered_set<int> children;

        for (const auto& desc : descriptions) {
            int parentVal = desc[0];
            int childVal = desc[1];
            bool isLeft = desc[2];

            if (nodes.find(parentVal) == nodes.end()) {
                nodes[parentVal] = new TreeNode(parentVal);
            }
            if (nodes.find(childVal) == nodes.end()) {
                nodes[childVal] = new TreeNode(childVal);
            }

            if (isLeft) {
                nodes[parentVal]->left = nodes[childVal];
            } else {
                nodes[parentVal]->right = nodes[childVal];
            }
            children.insert(childVal);
        }

        for (const auto& desc : descriptions) {
            if (children.find(desc[0]) == children.end()) {
                return nodes[desc[0]];
            }
        }

        return nullptr;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> nodes = new HashMap<>();
        Set<Integer> children = new HashSet<>();

        for (int[] desc : descriptions) {
            int parentVal = desc[0];
            int childVal = desc[1];
            int isLeft = desc[2];

            nodes.putIfAbsent(parentVal, new TreeNode(parentVal));
            nodes.putIfAbsent(childVal, new TreeNode(childVal));

            if (isLeft == 1) {
                nodes.get(parentVal).left = nodes.get(childVal);
            } else {
                nodes.get(parentVal).right = nodes.get(childVal);
            }
            children.add(childVal);
        }

        for (int[] desc : descriptions) {
            if (!children.contains(desc[0])) {
                return nodes.get(desc[0]);
            }
        }

        return null;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()

        for p, c, is_left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            children.add(c)

        for p, c, is_left in descriptions:
            if p not in children:
                return nodes[p]

        return None
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for p, c, is_left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)

            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            children.add(c)

        for p, c, is_left in descriptions:
            if p not in children:
                return nodes[p]

        return None
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* createBinaryTree(int** descriptions, int descriptionsSize, int* descriptionsColSize) {
    struct TreeNode** nodeMap = (struct TreeNode**)calloc(100001, sizeof(struct TreeNode*));
    bool* hasParent = (bool*)calloc(100001, sizeof(bool));

    for (int i = 0; i < descriptionsSize; i++) {
        int pVal = descriptions[i][0];
        int cVal = descriptions[i][1];
        int isLeft = descriptions[i][2];

        if (nodeMap[pVal] == NULL) {
            nodeMap[pVal] = (struct TreeNode*)malloc(sizeof(struct TreeNode));
            nodeMap[pVal]->val = pVal;
            nodeMap[pVal]->left = NULL;
            nodeMap[pVal]->right = NULL;
        }
        if (nodeMap[cVal] == NULL) {
            nodeMap[cVal] = (struct TreeNode*)malloc(sizeof(struct TreeNode));
            nodeMap[cVal]->val = cVal;
            nodeMap[cVal]->left = NULL;
            nodeMap[cVal]->right = NULL;
        }

        if (isLeft == 1) {
            nodeMap[pVal]->left = nodeMap[cVal];
        } else {
            nodeMap[pVal]->right = nodeMap[cVal];
        }
        hasParent[cVal] = true;
    }

    struct TreeNode* root = NULL;
    for (int i = 0; i < descriptionsSize; i++) {
        int pVal = descriptions[i][0];
        if (!hasParent[pVal]) {
            root = nodeMap[pVal];
            break;
        }
    }

    free(hasParent);
    free(nodeMap);
    return root;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public TreeNode CreateBinaryTree(int[][] descriptions) {
        Dictionary<int, TreeNode> nodeMap = new Dictionary<int, TreeNode>();
        HashSet<int> childNodes = new HashSet<int>();

        foreach (int[] d in descriptions) {
            int parentVal = d[0];
            int childVal = d[1];
            bool isLeft = d[2] == 1;

            if (!nodeMap.ContainsKey(parentVal)) {
                nodeMap[parentVal] = new TreeNode(parentVal);
            }
            if (!nodeMap.ContainsKey(childVal)) {
                nodeMap[childVal] = new TreeNode(childVal);
            }

            if (isLeft) {
                nodeMap[parentVal].left = nodeMap[childVal];
            } else {
                nodeMap[parentVal].right = nodeMap[childVal];
            }

            childNodes.Add(childVal);
        }

        foreach (var entry in nodeMap) {
            if (!childNodes.Contains(entry.Key)) {
                return entry.Value;
            }
        }

        return null;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) {
    const nodeMap = new Map();
    const children = new Set();

    for (const [parentVal, childVal, isLeft] of descriptions) {
        if (!nodeMap.has(parentVal)) {
            nodeMap.set(parentVal, new TreeNode(parentVal));
        }
        if (!nodeMap.has(childVal)) {
            nodeMap.set(childVal, new TreeNode(childVal));
        }

        const parentNode = nodeMap.get(parentVal);
        const childNode = nodeMap.get(childVal);

        if (isLeft === 1) {
            parentNode.left = childNode;
        } else {
            parentNode.right = childNode;
        }

        children.add(childVal);
    }

    for (const [val, node] of nodeMap) {
        if (!children.has(val)) {
            return node;
        }
    }

    return null;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function createBinaryTree(descriptions: number[][]): TreeNode | null {
    const nodeMap = new Map<number, TreeNode>();
    const children = new Set<number>();

    for (const [parentVal, childVal, isLeft] of descriptions) {
        if (!nodeMap.has(parentVal)) {
            nodeMap.set(parentVal, new TreeNode(parentVal));
        }
        if (!nodeMap.has(childVal)) {
            nodeMap.set(childVal, new TreeNode(childVal));
        }

        const parentNode = nodeMap.get(parentVal)!;
        const childNode = nodeMap.get(childVal)!;

        if (isLeft === 1) {
            parentNode.left = childNode;
        } else {
            parentNode.right = childNode;
        }

        children.add(childVal);
    }

    for (const [val, node] of nodeMap.entries()) {
        if (!children.has(val)) {
            return node;
        }
    }

    return null;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         this.val = $val;
 *         this.left = $left;
 *         this.right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param Integer[][] $descriptions
     * @return TreeNode
     */
    function createBinaryTree($descriptions) {
        $nodeMap = [];
        $children = [];

        foreach ($descriptions as $d) {
            $pVal = $d[0];
            $cVal = $d[1];
            $isLeft = $d[2];

            if (!isset($nodeMap[$pVal])) {
                $nodeMap[$pVal] = new TreeNode($pVal);
            }
            if (!isset($nodeMap[$cVal])) {
                $nodeMap[$cVal] = new TreeNode($cVal);
            }

            if ($isLeft == 1) {
                $nodeMap[$pVal]->left = $nodeMap[$cVal];
            } else {
                $nodeMap[$pVal]->right = $nodeMap[$cVal];
            }

            $children[$cVal] = true;
        }

        foreach ($nodeMap as $val => $node) {
            if (!isset($children[$val])) {
                return $node;
            }
        }

        return null;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func createBinaryTree(_ descriptions: [[Int]]) -> TreeNode? {
        var nodeMap = [Int: TreeNode]()
        var children = Set<Int>()

        for d in descriptions {
            let parentVal = d[0]
            let childVal = d[1]
            let isLeft = d[2] == 1

            if nodeMap[parentVal] == nil {
                nodeMap[parentVal] = TreeNode(parentVal)
            }
            if nodeMap[childVal] == nil {
                nodeMap[childVal] = TreeNode(childVal)
            }

            let parentNode = nodeMap[parentVal]!
            let childNode = nodeMap[childVal]!

            if isLeft {
                parentNode.left = childNode
            } else {
                parentNode.right = childNode
            }

            children.insert(childVal)
        }

        for (val, node) in nodeMap {
            if !children.contains(val) {
                return node
            }
        }

        return nil
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun createBinaryTree(descriptions: Array<IntArray>): TreeNode? {
        val nodes = mutableMapOf<Int, TreeNode>()
        val children = mutableSetOf<Int>()

        for (desc in descriptions) {
            val parentVal = desc[0]
            val childVal = desc[1]
            val isLeft = desc[2] == 1

            val parentNode = nodes.getOrPut(parentVal) { TreeNode(parentVal) }
            val childNode = nodes.getOrPut(childVal) { TreeNode(childVal) }

            if (isLeft) {
                parentNode.left = childNode
            } else {
                parentNode.right = childNode
            }
            children.add(childVal)
        }

        for (desc in descriptions) {
            val parentVal = desc[0]
            if (!children.contains(parentVal)) {
                return nodes[parentVal]
            }
        }

        return null
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  TreeNode? createBinaryTree(List<List<int>> descriptions) {
    Map<int, TreeNode> nodes = {};
    Set<int> children = {};

    for (var desc in descriptions) {
      int pVal = desc[0];
      int cVal = desc[1];
      bool isLeft = desc[2] == 1;

      TreeNode pNode = nodes.putIfAbsent(pVal, () => TreeNode(pVal));
      TreeNode cNode = nodes.putIfAbsent(cVal, () => TreeNode(cVal));

      if (isLeft) {
        pNode.left = cNode;
      } else {
        pNode.right = cNode;
      }
      children.add(cVal);
    }

    for (var desc in descriptions) {
      int pVal = desc[0];
      if (!children.contains(pVal)) {
        return nodes[pVal];
      }
    }

    return null;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func createBinaryTree(descriptions [][]int) *TreeNode {
    nodes := make(map[int]*TreeNode)
    isChild := make(map[int]bool)

    for _, desc := range descriptions {
        pVal, cVal, isLeft := desc[0], desc[1], desc[2] == 1

        if _, exists := nodes[pVal]; !exists {
            nodes[pVal] = &TreeNode{Val: pVal}
        }
        if _, exists := nodes[cVal]; !exists {
            nodes[cVal] = &TreeNode{Val: cVal}
        }

        if isLeft {
            nodes[pVal].Left = nodes[cVal]
        } else {
            nodes[pVal].Right = nodes[cVal]
        }
        isChild[cVal] = true
    }

    for _, desc := range descriptions {
        pVal := desc[0]
        if !isChild[pVal] {
            return nodes[pVal]
        }
    }

    return nil
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def create_binary_tree(descriptions)
    nodes = {}
    children = {}

    descriptions.each do |p_val, c_val, is_left|
        nodes[p_val] ||= TreeNode.new(p_val)
        nodes[c_val] ||= TreeNode.new(c_val)

        if is_left == 1
            nodes[p_val].left = nodes[c_val]
        else
            nodes[p_val].right = nodes[c_val]
        end
        children[c_val] = true
    end

    descriptions.each do |p_val, c_val, is_left|
        return nodes[p_val] unless children.has_key?(p_val)
    end

    nil
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def createBinaryTree(descriptions: Array[Array[Int]]): TreeNode = {
        val nodes = mutable.Map[Int, TreeNode]()
        val children = mutable.Set[Int]()

        for (desc <- descriptions) {
            val pVal = desc(0)
            val cVal = desc(1)
            val isLeft = desc(2) == 1

            val pNode = nodes.getOrElseUpdate(pVal, new TreeNode(pVal))
            val cNode = nodes.getOrElseUpdate(cVal, new TreeNode(cVal))

            if (isLeft) {
                pNode.left = cNode
            } else {
                pNode.right = cNode
            }
            children.add(cVal)
        }

        var root: TreeNode = null
        for (desc <- descriptions) {
            val pVal = desc(0)
            if (!children.contains(pVal)) {
                root = nodes(pVal)
            }
        }
        root
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut nodes: HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        let mut children: HashSet<i32> = HashSet::new();

        for desc in &descriptions {
            let parent_val = desc[0];
            let child_val = desc[1];
            let is_left = desc[2] == 1;

            let parent = nodes
                .entry(parent_val)
                .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(parent_val))))
                .clone();
            let child = nodes
                .entry(child_val)
                .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(child_val))))
                .clone();

            if is_left {
                parent.borrow_mut().left = Some(child);
            } else {
                parent.borrow_mut().right = Some(child);
            }
            children.insert(child_val);
        }

        for desc in descriptions {
            let parent_val = desc[0];
            if !children.contains(&parent_val) {
                return nodes.get(&parent_val).cloned();
            }
        }

        None
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (create-binary-tree descriptions)
  (-> (listof (listof exact-integer?)) (or/c tree-node? #f))
  (let ([nodes (make-hash)]
        [children (mutable-set)])
    (for ([desc descriptions])
      (let* ([p-val (first desc)]
             [c-val (second desc)]
             [is-left (= (third desc) 1)])
        (let ([p-node (hash-ref! nodes p-val (lambda () (make-tree-node p-val)))]
              [c-node (hash-ref! nodes c-val (lambda () (make-tree-node c-val)))])
          (if is-left
              (set-tree-node-left! p-node c-node)
              (set-tree-node-right! p-node c-node))
          (set-add! children c-val))))
    (let loop ([ds descriptions])
      (if (null? ds)
          #f
          (let ([p-val (first (first ds))])
            (if (not (set-member? children p-val))
                (hash-ref nodes p-val)
                (loop (rest ds))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
create_binary_tree(Descriptions) ->
  {Adj, Children} = lists:foldl(fun([P, C, L], {AccAdj, AccChild}) ->
    {Left, Right} = maps:get(P, AccAdj, {null, null}),
    NewAdj = case L of
      1 -> maps:put(P, {C, Right}, AccAdj);
      0 -> maps:put(P, {Left, C}, AccAdj)
    end,
    {NewAdj, sets:add_element(C, AccChild)}
  end, {maps:new(), sets:new()}, Descriptions),

  RootVal = find_root(Descriptions, Children),
  build_tree(RootVal, Adj).

find_root([[P, _, _] | T], Children) ->
  case sets:is_element(P, Children) of
    true -> find_root(T, Children);
    false -> P
  end.

build_tree(null, _) -> null;
build_tree(Val, Adj) ->
  {LVal, RVal} = maps:get(Val, Adj, {null, null}),
  #tree_node{val = Val,
             left = build_tree(LVal, Adj),
             right = build_tree(RVal, Adj)}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec create_binary_tree(descriptions :: [[integer]]) :: TreeNode.t | nil
  def create_binary_tree(descriptions) do
    {adj, children} = Enum.reduce(descriptions, {%{}, MapSet.new()}, fn [p, c, l], {adj_acc, child_acc} ->
      {left, right} = Map.get(adj_acc, p, {nil, nil})
      new_adj_val = if l == 1, do: {c, right}, else: {left, c}
      {Map.put(adj_acc, p, new_adj_val), MapSet.put(child_acc, c)}
    end)

    root_val = Enum.find_value(descriptions, fn [p, _, _] ->
      if !MapSet.member?(children, p), do: p, else: nil
    end)

    build_tree(root_val, adj)
  end

  defp build_tree(nil, _), do: nil
  defp build_tree(val, adj) do
    {l_val, r_val} = Map.get(adj, val, {nil, nil})
    %TreeNode{
      val: val,
      left: build_tree(l_val, adj),
      right: build_tree(r_val, adj)
    }
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the number of descriptions. We process each description in the list once to create and link nodes, with each map/set operation taking constant time on average. A second iteration through the descriptions (or a scan of the parent values) allows us to identify the root node in linear time.
- **Space Complexity:** O(N) where N is the number of descriptions. We store at most 2N unique nodes in a hash map and a set of up to N child nodes to distinguish the root. In the C solution, an array of size 100,001 is used to manage the potential range of node values, which remains O(N + V) where V is the value range, but effectively linear relative to the input size constraints.
