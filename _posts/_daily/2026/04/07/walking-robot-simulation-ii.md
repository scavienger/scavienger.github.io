---
layout: post
title: "Walking Robot Simulation II"
date: 2026-04-07 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Design", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/walking-robot-simulation-ii/
ai_solutions:
  - solutions:
      cpp: "class Robot {\nprivate:\n    int width, height, pos, P;\n    bool moved;\n\
        \npublic:\n    Robot(int width, int height) : width(width), height(height),\
        \ pos(0), moved(false) {\n        P = 2 * (width + height - 2);\n    }\n\n \
        \   void step(int num) {\n        moved = true;\n        pos = (pos + num) %\
        \ P;\n    }\n\n    vector<int> getPos() {\n        if (pos <= width - 1) return\
        \ {pos, 0};\n        if (pos <= width + height - 2) return {width - 1, pos -\
        \ (width - 1)};\n        if (pos <= 2 * width + height - 3) return {width -\
        \ 1 - (pos - (width + height - 2)), height - 1};\n        return {0, height\
        \ - 1 - (pos - (2 * width + height - 3))};\n    }\n\n    string getDir() {\n\
        \        if (!moved) return \"East\";\n        if (pos == 0) return \"South\"\
        ;\n        if (pos <= width - 1) return \"East\";\n        if (pos <= width\
        \ + height - 2) return \"North\";\n        if (pos <= 2 * width + height - 3)\
        \ return \"West\";\n        return \"South\";\n    }\n};"
      java: "class Robot {\n    private int width, height, pos, P;\n    private boolean\
        \ moved;\n\n    public Robot(int width, int height) {\n        this.width =\
        \ width;\n        this.height = height;\n        this.pos = 0;\n        this.P\
        \ = 2 * (width + height - 2);\n        this.moved = false;\n    }\n\n    public\
        \ void step(int num) {\n        moved = true;\n        pos = (pos + num) % P;\n\
        \    }\n\n    public int[] getPos() {\n        if (pos <= width - 1) return\
        \ new int[]{pos, 0};\n        if (pos <= width + height - 2) return new int[]{width\
        \ - 1, pos - (width - 1)};\n        if (pos <= 2 * width + height - 3) return\
        \ new int[]{width - 1 - (pos - (width + height - 2)), height - 1};\n       \
        \ return new int[]{0, height - 1 - (pos - (2 * width + height - 3))};\n    }\n\
        \n    public String getDir() {\n        if (!moved) return \"East\";\n     \
        \   if (pos == 0) return \"South\";\n        if (pos <= width - 1) return \"\
        East\";\n        if (pos <= width + height - 2) return \"North\";\n        if\
        \ (pos <= 2 * width + height - 3) return \"West\";\n        return \"South\"\
        ;\n    }\n}"
      python: "class Robot(object):\n\n    def __init__(self, width, height):\n    \
        \    \"\"\"\n        :type width: int\n        :type height: int\n        \"\
        \"\"\n        self.w = width\n        self.h = height\n        self.pos = 0\n\
        \        self.P = 2 * (width + height - 2)\n        self.moved = False\n\n \
        \   def step(self, num):\n        \"\"\"\n        :type num: int\n        :rtype:\
        \ None\n        \"\"\"\n        self.moved = True\n        self.pos = (self.pos\
        \ + num) % self.P\n\n    def getPos(self):\n        \"\"\"\n        :rtype:\
        \ List[int]\n        \"\"\"\n        if 0 <= self.pos <= self.w - 1:\n     \
        \       return [self.pos, 0]\n        elif self.w <= self.pos <= self.w + self.h\
        \ - 2:\n            return [self.w - 1, self.pos - (self.w - 1)]\n        elif\
        \ self.w + self.h - 1 <= self.pos <= 2 * self.w + self.h - 3:\n            return\
        \ [self.w - 1 - (self.pos - (self.w + self.h - 2)), self.h - 1]\n        else:\n\
        \            return [0, self.h - 1 - (self.pos - (2 * self.w + self.h - 3))]\n\
        \n    def getDir(self):\n        \"\"\"\n        :rtype: str\n        \"\"\"\
        \n        if not self.moved:\n            return \"East\"\n        if self.pos\
        \ == 0:\n            return \"South\"\n        if 1 <= self.pos <= self.w -\
        \ 1:\n            return \"East\"\n        if self.w <= self.pos <= self.w +\
        \ self.h - 2:\n            return \"North\"\n        if self.w + self.h - 1\
        \ <= self.pos <= 2 * self.w + self.h - 3:\n            return \"West\"\n   \
        \     return \"South\""
      python3: "class Robot:\n\n    def __init__(self, width: int, height: int):\n \
        \       self.w = width\n        self.h = height\n        self.pos = 0\n    \
        \    self.P = 2 * (width + height - 2)\n        self.moved = False\n\n    def\
        \ step(self, num: int) -> None:\n        self.moved = True\n        self.pos\
        \ = (self.pos + num) % self.P\n\n    def getPos(self) -> List[int]:\n      \
        \  if self.pos <= self.w - 1:\n            return [self.pos, 0]\n        if\
        \ self.pos <= self.w + self.h - 2:\n            return [self.w - 1, self.pos\
        \ - (self.w - 1)]\n        if self.pos <= 2 * self.w + self.h - 3:\n       \
        \     return [self.w - 1 - (self.pos - (self.w + self.h - 2)), self.h - 1]\n\
        \        return [0, self.h - 1 - (self.pos - (2 * self.w + self.h - 3))]\n\n\
        \    def getDir(self) -> str:\n        if not self.moved:\n            return\
        \ \"East\"\n        if self.pos == 0:\n            return \"South\"\n      \
        \  if self.pos <= self.w - 1:\n            return \"East\"\n        if self.pos\
        \ <= self.w + self.h - 2:\n            return \"North\"\n        if self.pos\
        \ <= 2 * self.w + self.h - 3:\n            return \"West\"\n        return \"\
        South\""
      c: "#include <stdlib.h>\n#include <stdbool.h>\n\ntypedef struct {\n    int w;\n\
        \    int h;\n    int pos;\n    int P;\n    int moved;\n} Robot;\n\nRobot* robotCreate(int\
        \ width, int height) {\n    Robot* obj = (Robot*)malloc(sizeof(Robot));\n  \
        \  obj->w = width;\n    obj->h = height;\n    obj->pos = 0;\n    obj->P = 2\
        \ * (width + height - 2);\n    obj->moved = 0;\n    return obj;\n}\n\nvoid robotStep(Robot*\
        \ obj, int num) {\n    obj->moved = 1;\n    obj->pos = (obj->pos + num) % obj->P;\n\
        }\n\nint* robotGetPos(Robot* obj, int* retSize) {\n    *retSize = 2;\n    int*\
        \ res = (int*)malloc(2 * sizeof(int));\n    if (obj->pos <= obj->w - 1) {\n\
        \        res[0] = obj->pos;\n        res[1] = 0;\n    } else if (obj->pos <=\
        \ obj->w + obj->h - 2) {\n        res[0] = obj->w - 1;\n        res[1] = obj->pos\
        \ - (obj->w - 1);\n    } else if (obj->pos <= 2 * obj->w + obj->h - 3) {\n \
        \       res[0] = obj->w - 1 - (obj->pos - (obj->w + obj->h - 2));\n        res[1]\
        \ = obj->h - 1;\n    } else {\n        res[0] = 0;\n        res[1] = obj->h\
        \ - 1 - (obj->pos - (2 * obj->w + obj->h - 3));\n    }\n    return res;\n}\n\
        \nchar* robotGetDir(Robot* obj) {\n    if (!obj->moved) return \"East\";\n \
        \   if (obj->pos == 0) return \"South\";\n    if (obj->pos <= obj->w - 1) return\
        \ \"East\";\n    if (obj->pos <= obj->w + obj->h - 2) return \"North\";\n  \
        \  if (obj->pos <= 2 * obj->w + obj->h - 3) return \"West\";\n    return \"\
        South\";\n}\n\nvoid robotFree(Robot* obj) {\n    free(obj);\n}"
      csharp: "public class Robot {\n    private int w, h, p, pos;\n    private bool\
        \ moved;\n\n    public Robot(int width, int height) {\n        w = width;\n\
        \        h = height;\n        p = 2 * (w + h - 2);\n        pos = 0;\n     \
        \   moved = false;\n    }\n\n    public void Step(int num) {\n        moved\
        \ = true;\n        pos = (pos + num) % p;\n    }\n\n    public int[] GetPos()\
        \ {\n        int d = pos;\n        if (d <= w - 1) return new int[] { d, 0 };\n\
        \        if (d <= w + h - 2) return new int[] { w - 1, d - w + 1 };\n      \
        \  if (d <= 2 * w + h - 3) return new int[] { w - 1 - (d - (w + h - 2)), h -\
        \ 1 };\n        return new int[] { 0, h - 1 - (d - (2 * w + h - 3)) };\n   \
        \ }\n\n    public string GetDir() {\n        int d = pos;\n        if (d ==\
        \ 0) return moved ? \"South\" : \"East\";\n        if (d <= w - 1) return \"\
        East\";\n        if (d <= w + h - 2) return \"North\";\n        if (d <= 2 *\
        \ w + h - 3) return \"West\";\n        return \"South\";\n    }\n}"
      javascript: "/**\n * @param {number} width\n * @param {number} height\n */\nvar\
        \ Robot = function(width, height) {\n    this.w = width;\n    this.h = height;\n\
        \    this.p = 2 * (width + height - 2);\n    this.pos = 0;\n    this.moved =\
        \ false;\n};\n\n/** \n * @param {number} num\n * @return {void}\n */\nRobot.prototype.step\
        \ = function(num) {\n    this.moved = true;\n    this.pos = (this.pos + num)\
        \ % this.p;\n};\n\n/**\n * @return {number[]}\n */\nRobot.prototype.getPos =\
        \ function() {\n    let d = this.pos;\n    let {w, h} = this;\n    if (d <=\
        \ w - 1) return [d, 0];\n    if (d <= w + h - 2) return [w - 1, d - w + 1];\n\
        \    if (d <= 2 * w + h - 3) return [w - 1 - (d - (w + h - 2)), h - 1];\n  \
        \  return [0, h - 1 - (d - (2 * w + h - 3))];\n};\n\n/**\n * @return {string}\n\
        \ */\nRobot.prototype.getDir = function() {\n    let d = this.pos;\n    let\
        \ {w, h} = this;\n    if (d === 0) return this.moved ? \"South\" : \"East\"\
        ;\n    if (d <= w - 1) return \"East\";\n    if (d <= w + h - 2) return \"North\"\
        ;\n    if (d <= 2 * w + h - 3) return \"West\";\n    return \"South\";\n};"
      typescript: "class Robot {\n    private w: number;\n    private h: number;\n \
        \   private p: number;\n    private pos: number;\n    private moved: boolean;\n\
        \n    constructor(width: number, height: number) {\n        this.w = width;\n\
        \        this.h = height;\n        this.p = 2 * (width + height - 2);\n    \
        \    this.pos = 0;\n        this.moved = false;\n    }\n\n    step(num: number):\
        \ void {\n        this.moved = true;\n        this.pos = (this.pos + num) %\
        \ this.p;\n    }\n\n    getPos(): number[] {\n        const d = this.pos;\n\
        \        const { w, h } = this;\n        if (d <= w - 1) return [d, 0];\n  \
        \      if (d <= w + h - 2) return [w - 1, d - w + 1];\n        if (d <= 2 *\
        \ w + h - 3) return [w - 1 - (d - (w + h - 2)), h - 1];\n        return [0,\
        \ h - 1 - (d - (2 * w + h - 3))];\n    }\n\n    getDir(): string {\n       \
        \ const d = this.pos;\n        const { w, h } = this;\n        if (d === 0)\
        \ return this.moved ? \"South\" : \"East\";\n        if (d <= w - 1) return\
        \ \"East\";\n        if (d <= w + h - 2) return \"North\";\n        if (d <=\
        \ 2 * w + h - 3) return \"West\";\n        return \"South\";\n    }\n}"
      php: "class Robot {\n    private $w, $h, $p, $pos, $moved;\n    /**\n     * @param\
        \ Integer $width\n     * @param Integer $height\n     */\n    function __construct($width,\
        \ $height) {\n        $this->w = $width;\n        $this->h = $height;\n    \
        \    $this->p = 2 * ($width + $height - 2);\n        $this->pos = 0;\n     \
        \   $this->moved = false;\n    }\n\n    /**\n     * @param Integer $num\n  \
        \   * @return NULL\n     */\n    function step($num) {\n        $this->moved\
        \ = true;\n        $this->pos = ($this->pos + $num) % $this->p;\n    }\n\n \
        \   /**\n     * @return Integer[]\n     */\n    function getPos() {\n      \
        \  $d = $this->pos;\n        $w = $this->w;\n        $h = $this->h;\n      \
        \  if ($d <= $w - 1) return [$d, 0];\n        if ($d <= $w + $h - 2) return\
        \ [$w - 1, $d - $w + 1];\n        if ($d <= 2 * $w + $h - 3) return [$w - 1\
        \ - ($d - ($w + $h - 2)), $h - 1];\n        return [0, $h - 1 - ($d - (2 * $w\
        \ + $h - 3))];\n    }\n\n    /**\n     * @return String\n     */\n    function\
        \ getDir() {\n        $d = $this->pos;\n        if ($d == 0) return $this->moved\
        \ ? \"South\" : \"East\";\n        if ($d <= $this->w - 1) return \"East\";\n\
        \        if ($d <= $this->w + $this->h - 2) return \"North\";\n        if ($d\
        \ <= 2 * $this->w + $this->h - 3) return \"West\";\n        return \"South\"\
        ;\n    }\n}"
      swift: "class Robot {\n    private let w, h, p: Int\n    private var pos: Int\n\
        \    private var moved: Bool\n\n    init(_ width: Int, _ height: Int) {\n  \
        \      self.w = width\n        self.h = height\n        self.p = 2 * (width\
        \ + height - 2)\n        self.pos = 0\n        self.moved = false\n    }\n\n\
        \    func step(_ num: Int) {\n        self.moved = true\n        self.pos =\
        \ (self.pos + num) % self.p\n    }\n\n    func getPos() -> [Int] {\n       \
        \ let d = self.pos\n        if d <= w - 1 { return [d, 0] }\n        if d <=\
        \ w + h - 2 { return [w - 1, d - w + 1] }\n        if d <= 2 * w + h - 3 { return\
        \ [w - 1 - (d - (w + h - 2)), h - 1] }\n        return [0, h - 1 - (d - (2 *\
        \ w + h - 3))]\n    }\n\n    func getDir() -> String {\n        let d = self.pos\n\
        \        if d == 0 { return moved ? \"South\" : \"East\" }\n        if d <=\
        \ w - 1 { return \"East\" }\n        if d <= w + h - 2 { return \"North\" }\n\
        \        if d <= 2 * w + h - 3 { return \"West\" }\n        return \"South\"\
        \n    }\n}"
      kotlin: "class Robot(private val width: Int, private val height: Int) {\n    private\
        \ val p = 2 * (width + height - 2)\n    private var steps = 0\n    private var\
        \ moved = false\n\n    fun step(num: Int) {\n        moved = true\n        steps\
        \ = (steps + num) % p\n    }\n\n    fun getPos(): IntArray {\n        val s\
        \ = steps\n        return if (s < width) {\n            intArrayOf(s, 0)\n \
        \       } else if (s < width + height - 1) {\n            intArrayOf(width -\
        \ 1, s - (width - 1))\n        } else if (s < 2 * width + height - 2) {\n  \
        \          intArrayOf(width - 1 - (s - (width + height - 2)), height - 1)\n\
        \        } else {\n            intArrayOf(0, height - 1 - (s - (2 * width +\
        \ height - 3)))\n        }\n    }\n\n    fun getDir(): String {\n        if\
        \ (!moved) return \"East\"\n        val s = steps\n        if (s == 0) return\
        \ \"South\"\n        if (s < width) return \"East\"\n        if (s < width +\
        \ height - 1) return \"North\"\n        if (s < 2 * width + height - 2) return\
        \ \"West\"\n        return \"South\"\n    }\n}"
      dart: "class Robot {\n  int width;\n  int height;\n  int p;\n  int steps = 0;\n\
        \  bool moved = false;\n\n  Robot(this.width, this.height) : p = 2 * (width\
        \ + height - 2);\n\n  void step(int num) {\n    moved = true;\n    steps = (steps\
        \ + num) % p;\n  }\n\n  List<int> getPos() {\n    int s = steps;\n    if (s\
        \ < width) {\n      return [s, 0];\n    } else if (s < width + height - 1) {\n\
        \      return [width - 1, s - (width - 1)];\n    } else if (s < 2 * width +\
        \ height - 2) {\n      return [width - 1 - (s - (width + height - 2)), height\
        \ - 1];\n    } else {\n      return [0, height - 1 - (s - (2 * width + height\
        \ - 3))];\n    }\n  }\n\n  String getDir() {\n    if (!moved) return \"East\"\
        ;\n    int s = steps;\n    if (s == 0) return \"South\";\n    if (s < width)\
        \ {\n      return \"East\";\n    } else if (s < width + height - 1) {\n    \
        \  return \"North\";\n    } else if (s < 2 * width + height - 2) {\n      return\
        \ \"West\";\n    } else {\n      return \"South\";\n    }\n  }\n}"
      go: "type Robot struct {\n    width  int\n    height int\n    p      int\n   \
        \ steps  int\n    moved  bool\n}\n\nfunc Constructor(width int, height int)\
        \ Robot {\n    return Robot{\n        width:  width,\n        height: height,\n\
        \        p:      2 * (width + height - 2),\n        steps:  0,\n        moved:\
        \  false,\n    }\n}\n\nfunc (this *Robot) Step(num int) {\n    this.moved =\
        \ true\n    this.steps = (this.steps + num) % this.p\n}\n\nfunc (this *Robot)\
        \ GetPos() []int {\n    s := this.steps\n    if s < this.width {\n        return\
        \ []int{s, 0}\n    } else if s < this.width+this.height-1 {\n        return\
        \ []int{this.width - 1, s - (this.width - 1)}\n    } else if s < 2*this.width+this.height-2\
        \ {\n        return []int{this.width - 1 - (s - (this.width + this.height -\
        \ 2)), this.height - 1}\n    } else {\n        return []int{0, this.height -\
        \ 1 - (s - (2*this.width + this.height - 3))}\n    }\n}\n\nfunc (this *Robot)\
        \ GetDir() string {\n    if !this.moved {\n        return \"East\"\n    }\n\
        \    s := this.steps\n    if s == 0 {\n        return \"South\"\n    }\n   \
        \ if s < this.width {\n        return \"East\"\n    } else if s < this.width+this.height-1\
        \ {\n        return \"North\"\n    } else if s < 2*this.width+this.height-2\
        \ {\n        return \"West\"\n    } else {\n        return \"South\"\n    }\n\
        }"
      ruby: "class Robot\n    def initialize(width, height)\n        @width = width\n\
        \        @height = height\n        @p = 2 * (width + height - 2)\n        @steps\
        \ = 0\n        @moved = false\n    end\n\n    def step(num)\n        @moved\
        \ = true\n        @steps = (@steps + num) % @p\n    end\n\n    def get_pos()\n\
        \        s = @steps\n        if s < @width\n            [s, 0]\n        elsif\
        \ s < @width + @height - 1\n            [@width - 1, s - (@width - 1)]\n   \
        \     elsif s < 2 * @width + @height - 2\n            [@width - 1 - (s - (@width\
        \ + @height - 2)), @height - 1]\n        else\n            [0, @height - 1 -\
        \ (s - (2 * @width + @height - 3))]\n        end\n    end\n\n    def get_dir()\n\
        \        return \"East\" unless @moved\n        s = @steps\n        return \"\
        South\" if s == 0\n        if s < @width\n            \"East\"\n        elsif\
        \ s < @width + @height - 1\n            \"North\"\n        elsif s < 2 * @width\
        \ + @height - 2\n            \"West\"\n        else\n            \"South\"\n\
        \        end\n    end\nend"
      scala: "class Robot(_width: Int, _height: Int) {\n    private val width = _width\n\
        \    private val height = _height\n    private val p = 2 * (width + height -\
        \ 2)\n    private var steps = 0\n    private var moved = false\n\n    def step(num:\
        \ Int): Unit = {\n        moved = true\n        steps = (steps + num) % p\n\
        \    }\n\n    def getPos(): Array[Int] = {\n        val s = steps\n        if\
        \ (s < width) {\n            Array(s, 0)\n        } else if (s < width + height\
        \ - 1) {\n            Array(width - 1, s - (width - 1))\n        } else if (s\
        \ < 2 * width + height - 2) {\n            Array(width - 1 - (s - (width + height\
        \ - 2)), height - 1)\n        } else {\n            Array(0, height - 1 - (s\
        \ - (2 * width + height - 3)))\n        }\n    }\n\n    def getDir(): String\
        \ = {\n        if (!moved) return \"East\"\n        val s = steps\n        if\
        \ (s == 0) return \"South\"\n        if (s < width) {\n            \"East\"\n\
        \        } else if (s < width + height - 1) {\n            \"North\"\n     \
        \   } else if (s < 2 * width + height - 2) {\n            \"West\"\n       \
        \ } else {\n            \"South\"\n        }\n    }\n}"
      rust: "struct Robot {\n    w: i32,\n    h: i32,\n    p: i32,\n    pos: i32,\n\
        \    moved: bool,\n}\n\nimpl Robot {\n    fn new(width: i32, height: i32) ->\
        \ Self {\n        Robot {\n            w: width,\n            h: height,\n \
        \           p: 2 * (width + height - 2),\n            pos: 0,\n            moved:\
        \ false,\n        }\n    }\n\n    fn step(&mut self, num: i32) {\n        self.moved\
        \ = true;\n        self.pos = (self.pos + num) % self.p;\n    }\n\n    fn get_pos(&self)\
        \ -> Vec<i32> {\n        let s = self.pos;\n        let w = self.w;\n      \
        \  let h = self.h;\n        if s <= w - 1 {\n            vec![s, 0]\n      \
        \  } else if s <= w + h - 2 {\n            vec![w - 1, s - w + 1]\n        }\
        \ else if s <= 2 * w + h - 3 {\n            vec![w - 1 - (s - (w + h - 2)),\
        \ h - 1]\n        } else {\n            vec![0, h - 1 - (s - (2 * w + h - 3))]\n\
        \        }\n    }\n\n    fn get_dir(&self) -> String {\n        let s = self.pos;\n\
        \        let w = self.w;\n        let h = self.h;\n        if s == 0 && self.moved\
        \ {\n            return \"South\".to_string();\n        }\n        if s <= w\
        \ - 1 {\n            \"East\".to_string()\n        } else if s <= w + h - 2\
        \ {\n            \"North\".to_string()\n        } else if s <= 2 * w + h - 3\
        \ {\n            \"West\".to_string()\n        } else {\n            \"South\"\
        .to_string()\n        }\n    }\n}"
      racket: "(define robot%\n  (class object%\n    (super-new)\n\n    (init-field\n\
        \      width\n      height)\n\n    (define p (* 2 (+ width height -2)))\n  \
        \  (define pos 0)\n    (define moved #f)\n\n    (define/public (step num)\n\
        \      (set! moved #t)\n      (set! pos (remainder (+ pos num) p)))\n\n    (define/public\
        \ (get-pos)\n      (cond\n        [(<= pos (- width 1)) (list pos 0)]\n    \
        \    [(<= pos (- (+ width height) 2)) (list (- width 1) (- pos (- width 1)))]\n\
        \        [(<= pos (- (+ (* 2 width) height) 3)) (list (- (- width 1) (- pos\
        \ (- (+ width height) 2))) (- height 1))]\n        [else (list 0 (- (- height\
        \ 1) (- pos (- (+ (* 2 width) height) 3))))]))\n\n    (define/public (get-dir)\n\
        \      (cond\n        [(and (= pos 0) moved) \"South\"]\n        [(<= pos (-\
        \ width 1)) \"East\"]\n        [(<= pos (- (+ width height) 2)) \"North\"]\n\
        \        [(<= pos (- (+ (* 2 width) height) 3)) \"West\"]\n        [else \"\
        South\"]))))"
      erlang: "-spec robot_init_(Width :: integer(), Height :: integer()) -> any().\n\
        robot_init_(Width, Height) ->\n  put(robot_width, Width),\n  put(robot_height,\
        \ Height),\n  put(robot_p, 2 * (Width + Height - 2)),\n  put(robot_pos, 0),\n\
        \  put(robot_moved, false),\n  ok.\n\n-spec robot_step(Num :: integer()) ->\
        \ any().\nrobot_step(Num) ->\n  P = get(robot_p),\n  Pos = get(robot_pos),\n\
        \  put(robot_pos, (Pos + Num) rem P),\n  put(robot_moved, true),\n  ok.\n\n\
        -spec robot_get_pos() -> [integer()].\nrobot_get_pos() ->\n  W = get(robot_width),\n\
        \  H = get(robot_height),\n  S = get(robot_pos),\n  if\n    S =< W - 1 -> [S,\
        \ 0];\n    S =< W + H - 2 -> [W - 1, S - W + 1];\n    S =< 2 * W + H - 3 ->\
        \ [W - 1 - (S - (W + H - 2)), H - 1];\n    true -> [0, H - 1 - (S - (2 * W +\
        \ H - 3))]\n  end.\n\n-spec robot_get_dir() -> unicode:unicode_binary().\nrobot_get_dir()\
        \ ->\n  W = get(robot_width),\n  H = get(robot_height),\n  S = get(robot_pos),\n\
        \  Moved = get(robot_moved),\n  if\n    S =:= 0, Moved =:= true -> <<\"South\"\
        >>;\n    S =< W - 1 -> <<\"East\">>;\n    S =< W + H - 2 -> <<\"North\">>;\n\
        \    S =< 2 * W + H - 3 -> <<\"West\">>;\n    true -> <<\"South\">>\n  end."
      elixir: "defmodule Robot do\n  @spec init_(width :: integer, height :: integer)\
        \ :: any\n  def init_(width, height) do\n    Process.put(:robot_width, width)\n\
        \    Process.put(:robot_height, height)\n    Process.put(:robot_p, 2 * (width\
        \ + height - 2))\n    Process.put(:robot_pos, 0)\n    Process.put(:robot_moved,\
        \ false)\n  end\n\n  @spec step(num :: integer) :: any\n  def step(num) do\n\
        \    p = Process.get(:robot_p)\n    pos = Process.get(:robot_pos)\n    Process.put(:robot_pos,\
        \ rem(pos + num, p))\n    Process.put(:robot_moved, true)\n  end\n\n  @spec\
        \ get_pos() :: [integer]\n  def get_pos() do\n    w = Process.get(:robot_width)\n\
        \    h = Process.get(:robot_height)\n    s = Process.get(:robot_pos)\n    cond\
        \ do\n      s <= w - 1 -> [s, 0]\n      s <= w + h - 2 -> [w - 1, s - w + 1]\n\
        \      s <= 2 * w + h - 3 -> [w - 1 - (s - (w + h - 2)), h - 1]\n      true\
        \ -> [0, h - 1 - (s - (2 * w + h - 3))]\n    end\n  end\n\n  @spec get_dir()\
        \ :: String.t\n  def get_dir() do\n    w = Process.get(:robot_width)\n    h\
        \ = Process.get(:robot_height)\n    s = Process.get(:robot_pos)\n    moved =\
        \ Process.get(:robot_moved)\n    cond do\n      s == 0 and moved -> \"South\"\
        \n      s <= w - 1 -> \"East\"\n      s <= w + h - 2 -> \"North\"\n      s <=\
        \ 2 * w + h - 3 -> \"West\"\n      true -> \"South\"\n    end\n  end\nend"
    approach: The robot's movement is confined to the perimeter of the grid, traveling
      in a counterclockwise direction. By calculating the total perimeter length $P
      = 2 \cdot (width + height - 2)$, any instruction to move $num$ steps can be simplified
      using $num \pmod P$. This reduction is possible because the robot's position and
      direction eventually cycle every $P$ steps. We track the total number of steps
      moved or the current perimeter index to determine the robot's state efficiently
      in $O(1)$ time.
    time_complexity: O(1) for all operations. The initialization, `step`, `getPos`,
      and `getDir` methods only involve basic arithmetic, modulo operations, and conditional
      checks, all of which execute in constant time regardless of the grid size or the
      number of steps.
    space_complexity: O(1). The solution only requires a few integer variables to store
      the grid dimensions, the current perimeter position, and a boolean flag to handle
      the initial state. No additional data structures or memory scaling with input
      are needed.
    elapsed_time: 603.0870795249939
    model: gemini-3-flash-preview
    generated_at: '2026-04-07 01:57:59 '
---

## Problem #2069: Walking Robot Simulation II

**Difficulty:** Medium

**Topics:** Design, Simulation

## Problem Description

<p>A <code>width x height</code> grid is on an XY-plane with the <strong>bottom-left</strong> cell at <code>(0, 0)</code> and the <strong>top-right</strong> cell at <code>(width - 1, height - 1)</code>. The grid is aligned with the four cardinal directions (<code>&quot;North&quot;</code>, <code>&quot;East&quot;</code>, <code>&quot;South&quot;</code>, and <code>&quot;West&quot;</code>). A robot is <strong>initially</strong> at cell <code>(0, 0)</code> facing direction <code>&quot;East&quot;</code>.</p>

<p>The robot can be instructed to move for a specific number of <strong>steps</strong>. For each step, it does the following.</p>

<ol>
	<li>Attempts to move <strong>forward one</strong> cell in the direction it is facing.</li>
	<li>If the cell the robot is <strong>moving to</strong> is <strong>out of bounds</strong>, the robot instead <strong>turns</strong> 90 degrees <strong>counterclockwise</strong> and retries the step.</li>
</ol>

<p>After the robot finishes moving the number of steps required, it stops and awaits the next instruction.</p>

<p>Implement the <code>Robot</code> class:</p>

<ul>
	<li><code>Robot(int width, int height)</code> Initializes the <code>width x height</code> grid with the robot at <code>(0, 0)</code> facing <code>&quot;East&quot;</code>.</li>
	<li><code>void step(int num)</code> Instructs the robot to move forward <code>num</code> steps.</li>
	<li><code>int[] getPos()</code> Returns the current cell the robot is at, as an array of length 2, <code>[x, y]</code>.</li>
	<li><code>String getDir()</code> Returns the current direction of the robot, <code>&quot;North&quot;</code>, <code>&quot;East&quot;</code>, <code>&quot;South&quot;</code>, or <code>&quot;West&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="example-1" src="https://assets.leetcode.com/uploads/2021/10/09/example-1.png" style="width: 498px; height: 268px;" />
<pre>
<strong>Input</strong>
[&quot;Robot&quot;, &quot;step&quot;, &quot;step&quot;, &quot;getPos&quot;, &quot;getDir&quot;, &quot;step&quot;, &quot;step&quot;, &quot;step&quot;, &quot;getPos&quot;, &quot;getDir&quot;]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
<strong>Output</strong>
[null, null, null, [4, 0], &quot;East&quot;, null, null, null, [1, 2], &quot;West&quot;]

<strong>Explanation</strong>
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return &quot;East&quot;
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces <strong>North</strong> (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return &quot;West&quot;

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= width, height &lt;= 100</code></li>
	<li><code>1 &lt;= num &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>step</code>, <code>getPos</code>, and <code>getDir</code>.</li>
</ul>


## Hints

1. The robot only moves along the perimeter of the grid. Can you think if modulus can help you quickly compute which cell it stops at?

2. After the robot moves one time, whenever the robot stops at some cell, it will always face a specific direction. i.e., The direction it faces is determined by the cell it stops at.

3. Can you precompute what direction it faces when it stops at each cell along the perimeter, and reuse the results?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The robot's movement is confined to the perimeter of the grid, traveling in a counterclockwise direction. By calculating the total perimeter length $P = 2 \cdot (width + height - 2)$, any instruction to move $num$ steps can be simplified using $num \pmod P$. This reduction is possible because the robot's position and direction eventually cycle every $P$ steps. We track the total number of steps moved or the current perimeter index to determine the robot's state efficiently in $O(1)$ time.

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
class Robot {
private:
    int width, height, pos, P;
    bool moved;

public:
    Robot(int width, int height) : width(width), height(height), pos(0), moved(false) {
        P = 2 * (width + height - 2);
    }

    void step(int num) {
        moved = true;
        pos = (pos + num) % P;
    }

    vector<int> getPos() {
        if (pos <= width - 1) return {pos, 0};
        if (pos <= width + height - 2) return {width - 1, pos - (width - 1)};
        if (pos <= 2 * width + height - 3) return {width - 1 - (pos - (width + height - 2)), height - 1};
        return {0, height - 1 - (pos - (2 * width + height - 3))};
    }

    string getDir() {
        if (!moved) return "East";
        if (pos == 0) return "South";
        if (pos <= width - 1) return "East";
        if (pos <= width + height - 2) return "North";
        if (pos <= 2 * width + height - 3) return "West";
        return "South";
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Robot {
    private int width, height, pos, P;
    private boolean moved;

    public Robot(int width, int height) {
        this.width = width;
        this.height = height;
        this.pos = 0;
        this.P = 2 * (width + height - 2);
        this.moved = false;
    }

    public void step(int num) {
        moved = true;
        pos = (pos + num) % P;
    }

    public int[] getPos() {
        if (pos <= width - 1) return new int[]{pos, 0};
        if (pos <= width + height - 2) return new int[]{width - 1, pos - (width - 1)};
        if (pos <= 2 * width + height - 3) return new int[]{width - 1 - (pos - (width + height - 2)), height - 1};
        return new int[]{0, height - 1 - (pos - (2 * width + height - 3))};
    }

    public String getDir() {
        if (!moved) return "East";
        if (pos == 0) return "South";
        if (pos <= width - 1) return "East";
        if (pos <= width + height - 2) return "North";
        if (pos <= 2 * width + height - 3) return "West";
        return "South";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.w = width
        self.h = height
        self.pos = 0
        self.P = 2 * (width + height - 2)
        self.moved = False

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.moved = True
        self.pos = (self.pos + num) % self.P

    def getPos(self):
        """
        :rtype: List[int]
        """
        if 0 <= self.pos <= self.w - 1:
            return [self.pos, 0]
        elif self.w <= self.pos <= self.w + self.h - 2:
            return [self.w - 1, self.pos - (self.w - 1)]
        elif self.w + self.h - 1 <= self.pos <= 2 * self.w + self.h - 3:
            return [self.w - 1 - (self.pos - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.h - 1 - (self.pos - (2 * self.w + self.h - 3))]

    def getDir(self):
        """
        :rtype: str
        """
        if not self.moved:
            return "East"
        if self.pos == 0:
            return "South"
        if 1 <= self.pos <= self.w - 1:
            return "East"
        if self.w <= self.pos <= self.w + self.h - 2:
            return "North"
        if self.w + self.h - 1 <= self.pos <= 2 * self.w + self.h - 3:
            return "West"
        return "South"
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.P = 2 * (width + height - 2)
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.P

    def getPos(self) -> List[int]:
        if self.pos <= self.w - 1:
            return [self.pos, 0]
        if self.pos <= self.w + self.h - 2:
            return [self.w - 1, self.pos - (self.w - 1)]
        if self.pos <= 2 * self.w + self.h - 3:
            return [self.w - 1 - (self.pos - (self.w + self.h - 2)), self.h - 1]
        return [0, self.h - 1 - (self.pos - (2 * self.w + self.h - 3))]

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        if self.pos == 0:
            return "South"
        if self.pos <= self.w - 1:
            return "East"
        if self.pos <= self.w + self.h - 2:
            return "North"
        if self.pos <= 2 * self.w + self.h - 3:
            return "West"
        return "South"
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int w;
    int h;
    int pos;
    int P;
    int moved;
} Robot;

Robot* robotCreate(int width, int height) {
    Robot* obj = (Robot*)malloc(sizeof(Robot));
    obj->w = width;
    obj->h = height;
    obj->pos = 0;
    obj->P = 2 * (width + height - 2);
    obj->moved = 0;
    return obj;
}

void robotStep(Robot* obj, int num) {
    obj->moved = 1;
    obj->pos = (obj->pos + num) % obj->P;
}

int* robotGetPos(Robot* obj, int* retSize) {
    *retSize = 2;
    int* res = (int*)malloc(2 * sizeof(int));
    if (obj->pos <= obj->w - 1) {
        res[0] = obj->pos;
        res[1] = 0;
    } else if (obj->pos <= obj->w + obj->h - 2) {
        res[0] = obj->w - 1;
        res[1] = obj->pos - (obj->w - 1);
    } else if (obj->pos <= 2 * obj->w + obj->h - 3) {
        res[0] = obj->w - 1 - (obj->pos - (obj->w + obj->h - 2));
        res[1] = obj->h - 1;
    } else {
        res[0] = 0;
        res[1] = obj->h - 1 - (obj->pos - (2 * obj->w + obj->h - 3));
    }
    return res;
}

char* robotGetDir(Robot* obj) {
    if (!obj->moved) return "East";
    if (obj->pos == 0) return "South";
    if (obj->pos <= obj->w - 1) return "East";
    if (obj->pos <= obj->w + obj->h - 2) return "North";
    if (obj->pos <= 2 * obj->w + obj->h - 3) return "West";
    return "South";
}

void robotFree(Robot* obj) {
    free(obj);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Robot {
    private int w, h, p, pos;
    private bool moved;

    public Robot(int width, int height) {
        w = width;
        h = height;
        p = 2 * (w + h - 2);
        pos = 0;
        moved = false;
    }

    public void Step(int num) {
        moved = true;
        pos = (pos + num) % p;
    }

    public int[] GetPos() {
        int d = pos;
        if (d <= w - 1) return new int[] { d, 0 };
        if (d <= w + h - 2) return new int[] { w - 1, d - w + 1 };
        if (d <= 2 * w + h - 3) return new int[] { w - 1 - (d - (w + h - 2)), h - 1 };
        return new int[] { 0, h - 1 - (d - (2 * w + h - 3)) };
    }

    public string GetDir() {
        int d = pos;
        if (d == 0) return moved ? "South" : "East";
        if (d <= w - 1) return "East";
        if (d <= w + h - 2) return "North";
        if (d <= 2 * w + h - 3) return "West";
        return "South";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} width
 * @param {number} height
 */
var Robot = function(width, height) {
    this.w = width;
    this.h = height;
    this.p = 2 * (width + height - 2);
    this.pos = 0;
    this.moved = false;
};

/** 
 * @param {number} num
 * @return {void}
 */
Robot.prototype.step = function(num) {
    this.moved = true;
    this.pos = (this.pos + num) % this.p;
};

/**
 * @return {number[]}
 */
Robot.prototype.getPos = function() {
    let d = this.pos;
    let {w, h} = this;
    if (d <= w - 1) return [d, 0];
    if (d <= w + h - 2) return [w - 1, d - w + 1];
    if (d <= 2 * w + h - 3) return [w - 1 - (d - (w + h - 2)), h - 1];
    return [0, h - 1 - (d - (2 * w + h - 3))];
};

/**
 * @return {string}
 */
Robot.prototype.getDir = function() {
    let d = this.pos;
    let {w, h} = this;
    if (d === 0) return this.moved ? "South" : "East";
    if (d <= w - 1) return "East";
    if (d <= w + h - 2) return "North";
    if (d <= 2 * w + h - 3) return "West";
    return "South";
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class Robot {
    private w: number;
    private h: number;
    private p: number;
    private pos: number;
    private moved: boolean;

    constructor(width: number, height: number) {
        this.w = width;
        this.h = height;
        this.p = 2 * (width + height - 2);
        this.pos = 0;
        this.moved = false;
    }

    step(num: number): void {
        this.moved = true;
        this.pos = (this.pos + num) % this.p;
    }

    getPos(): number[] {
        const d = this.pos;
        const { w, h } = this;
        if (d <= w - 1) return [d, 0];
        if (d <= w + h - 2) return [w - 1, d - w + 1];
        if (d <= 2 * w + h - 3) return [w - 1 - (d - (w + h - 2)), h - 1];
        return [0, h - 1 - (d - (2 * w + h - 3))];
    }

    getDir(): string {
        const d = this.pos;
        const { w, h } = this;
        if (d === 0) return this.moved ? "South" : "East";
        if (d <= w - 1) return "East";
        if (d <= w + h - 2) return "North";
        if (d <= 2 * w + h - 3) return "West";
        return "South";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Robot {
    private $w, $h, $p, $pos, $moved;
    /**
     * @param Integer $width
     * @param Integer $height
     */
    function __construct($width, $height) {
        $this->w = $width;
        $this->h = $height;
        $this->p = 2 * ($width + $height - 2);
        $this->pos = 0;
        $this->moved = false;
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function step($num) {
        $this->moved = true;
        $this->pos = ($this->pos + $num) % $this->p;
    }

    /**
     * @return Integer[]
     */
    function getPos() {
        $d = $this->pos;
        $w = $this->w;
        $h = $this->h;
        if ($d <= $w - 1) return [$d, 0];
        if ($d <= $w + $h - 2) return [$w - 1, $d - $w + 1];
        if ($d <= 2 * $w + $h - 3) return [$w - 1 - ($d - ($w + $h - 2)), $h - 1];
        return [0, $h - 1 - ($d - (2 * $w + $h - 3))];
    }

    /**
     * @return String
     */
    function getDir() {
        $d = $this->pos;
        if ($d == 0) return $this->moved ? "South" : "East";
        if ($d <= $this->w - 1) return "East";
        if ($d <= $this->w + $this->h - 2) return "North";
        if ($d <= 2 * $this->w + $this->h - 3) return "West";
        return "South";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Robot {
    private let w, h, p: Int
    private var pos: Int
    private var moved: Bool

    init(_ width: Int, _ height: Int) {
        self.w = width
        self.h = height
        self.p = 2 * (width + height - 2)
        self.pos = 0
        self.moved = false
    }

    func step(_ num: Int) {
        self.moved = true
        self.pos = (self.pos + num) % self.p
    }

    func getPos() -> [Int] {
        let d = self.pos
        if d <= w - 1 { return [d, 0] }
        if d <= w + h - 2 { return [w - 1, d - w + 1] }
        if d <= 2 * w + h - 3 { return [w - 1 - (d - (w + h - 2)), h - 1] }
        return [0, h - 1 - (d - (2 * w + h - 3))]
    }

    func getDir() -> String {
        let d = self.pos
        if d == 0 { return moved ? "South" : "East" }
        if d <= w - 1 { return "East" }
        if d <= w + h - 2 { return "North" }
        if d <= 2 * w + h - 3 { return "West" }
        return "South"
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Robot(private val width: Int, private val height: Int) {
    private val p = 2 * (width + height - 2)
    private var steps = 0
    private var moved = false

    fun step(num: Int) {
        moved = true
        steps = (steps + num) % p
    }

    fun getPos(): IntArray {
        val s = steps
        return if (s < width) {
            intArrayOf(s, 0)
        } else if (s < width + height - 1) {
            intArrayOf(width - 1, s - (width - 1))
        } else if (s < 2 * width + height - 2) {
            intArrayOf(width - 1 - (s - (width + height - 2)), height - 1)
        } else {
            intArrayOf(0, height - 1 - (s - (2 * width + height - 3)))
        }
    }

    fun getDir(): String {
        if (!moved) return "East"
        val s = steps
        if (s == 0) return "South"
        if (s < width) return "East"
        if (s < width + height - 1) return "North"
        if (s < 2 * width + height - 2) return "West"
        return "South"
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Robot {
  int width;
  int height;
  int p;
  int steps = 0;
  bool moved = false;

  Robot(this.width, this.height) : p = 2 * (width + height - 2);

  void step(int num) {
    moved = true;
    steps = (steps + num) % p;
  }

  List<int> getPos() {
    int s = steps;
    if (s < width) {
      return [s, 0];
    } else if (s < width + height - 1) {
      return [width - 1, s - (width - 1)];
    } else if (s < 2 * width + height - 2) {
      return [width - 1 - (s - (width + height - 2)), height - 1];
    } else {
      return [0, height - 1 - (s - (2 * width + height - 3))];
    }
  }

  String getDir() {
    if (!moved) return "East";
    int s = steps;
    if (s == 0) return "South";
    if (s < width) {
      return "East";
    } else if (s < width + height - 1) {
      return "North";
    } else if (s < 2 * width + height - 2) {
      return "West";
    } else {
      return "South";
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
type Robot struct {
    width  int
    height int
    p      int
    steps  int
    moved  bool
}

func Constructor(width int, height int) Robot {
    return Robot{
        width:  width,
        height: height,
        p:      2 * (width + height - 2),
        steps:  0,
        moved:  false,
    }
}

func (this *Robot) Step(num int) {
    this.moved = true
    this.steps = (this.steps + num) % this.p
}

func (this *Robot) GetPos() []int {
    s := this.steps
    if s < this.width {
        return []int{s, 0}
    } else if s < this.width+this.height-1 {
        return []int{this.width - 1, s - (this.width - 1)}
    } else if s < 2*this.width+this.height-2 {
        return []int{this.width - 1 - (s - (this.width + this.height - 2)), this.height - 1}
    } else {
        return []int{0, this.height - 1 - (s - (2*this.width + this.height - 3))}
    }
}

func (this *Robot) GetDir() string {
    if !this.moved {
        return "East"
    }
    s := this.steps
    if s == 0 {
        return "South"
    }
    if s < this.width {
        return "East"
    } else if s < this.width+this.height-1 {
        return "North"
    } else if s < 2*this.width+this.height-2 {
        return "West"
    } else {
        return "South"
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Robot
    def initialize(width, height)
        @width = width
        @height = height
        @p = 2 * (width + height - 2)
        @steps = 0
        @moved = false
    end

    def step(num)
        @moved = true
        @steps = (@steps + num) % @p
    end

    def get_pos()
        s = @steps
        if s < @width
            [s, 0]
        elsif s < @width + @height - 1
            [@width - 1, s - (@width - 1)]
        elsif s < 2 * @width + @height - 2
            [@width - 1 - (s - (@width + @height - 2)), @height - 1]
        else
            [0, @height - 1 - (s - (2 * @width + @height - 3))]
        end
    end

    def get_dir()
        return "East" unless @moved
        s = @steps
        return "South" if s == 0
        if s < @width
            "East"
        elsif s < @width + @height - 1
            "North"
        elsif s < 2 * @width + @height - 2
            "West"
        else
            "South"
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
class Robot(_width: Int, _height: Int) {
    private val width = _width
    private val height = _height
    private val p = 2 * (width + height - 2)
    private var steps = 0
    private var moved = false

    def step(num: Int): Unit = {
        moved = true
        steps = (steps + num) % p
    }

    def getPos(): Array[Int] = {
        val s = steps
        if (s < width) {
            Array(s, 0)
        } else if (s < width + height - 1) {
            Array(width - 1, s - (width - 1))
        } else if (s < 2 * width + height - 2) {
            Array(width - 1 - (s - (width + height - 2)), height - 1)
        } else {
            Array(0, height - 1 - (s - (2 * width + height - 3)))
        }
    }

    def getDir(): String = {
        if (!moved) return "East"
        val s = steps
        if (s == 0) return "South"
        if (s < width) {
            "East"
        } else if (s < width + height - 1) {
            "North"
        } else if (s < 2 * width + height - 2) {
            "West"
        } else {
            "South"
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Robot {
    w: i32,
    h: i32,
    p: i32,
    pos: i32,
    moved: bool,
}

impl Robot {
    fn new(width: i32, height: i32) -> Self {
        Robot {
            w: width,
            h: height,
            p: 2 * (width + height - 2),
            pos: 0,
            moved: false,
        }
    }

    fn step(&mut self, num: i32) {
        self.moved = true;
        self.pos = (self.pos + num) % self.p;
    }

    fn get_pos(&self) -> Vec<i32> {
        let s = self.pos;
        let w = self.w;
        let h = self.h;
        if s <= w - 1 {
            vec![s, 0]
        } else if s <= w + h - 2 {
            vec![w - 1, s - w + 1]
        } else if s <= 2 * w + h - 3 {
            vec![w - 1 - (s - (w + h - 2)), h - 1]
        } else {
            vec![0, h - 1 - (s - (2 * w + h - 3))]
        }
    }

    fn get_dir(&self) -> String {
        let s = self.pos;
        let w = self.w;
        let h = self.h;
        if s == 0 && self.moved {
            return "South".to_string();
        }
        if s <= w - 1 {
            "East".to_string()
        } else if s <= w + h - 2 {
            "North".to_string()
        } else if s <= 2 * w + h - 3 {
            "West".to_string()
        } else {
            "South".to_string()
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define robot%
  (class object%
    (super-new)

    (init-field
      width
      height)

    (define p (* 2 (+ width height -2)))
    (define pos 0)
    (define moved #f)

    (define/public (step num)
      (set! moved #t)
      (set! pos (remainder (+ pos num) p)))

    (define/public (get-pos)
      (cond
        [(<= pos (- width 1)) (list pos 0)]
        [(<= pos (- (+ width height) 2)) (list (- width 1) (- pos (- width 1)))]
        [(<= pos (- (+ (* 2 width) height) 3)) (list (- (- width 1) (- pos (- (+ width height) 2))) (- height 1))]
        [else (list 0 (- (- height 1) (- pos (- (+ (* 2 width) height) 3))))]))

    (define/public (get-dir)
      (cond
        [(and (= pos 0) moved) "South"]
        [(<= pos (- width 1)) "East"]
        [(<= pos (- (+ width height) 2)) "North"]
        [(<= pos (- (+ (* 2 width) height) 3)) "West"]
        [else "South"]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec robot_init_(Width :: integer(), Height :: integer()) -> any().
robot_init_(Width, Height) ->
  put(robot_width, Width),
  put(robot_height, Height),
  put(robot_p, 2 * (Width + Height - 2)),
  put(robot_pos, 0),
  put(robot_moved, false),
  ok.

-spec robot_step(Num :: integer()) -> any().
robot_step(Num) ->
  P = get(robot_p),
  Pos = get(robot_pos),
  put(robot_pos, (Pos + Num) rem P),
  put(robot_moved, true),
  ok.

-spec robot_get_pos() -> [integer()].
robot_get_pos() ->
  W = get(robot_width),
  H = get(robot_height),
  S = get(robot_pos),
  if
    S =< W - 1 -> [S, 0];
    S =< W + H - 2 -> [W - 1, S - W + 1];
    S =< 2 * W + H - 3 -> [W - 1 - (S - (W + H - 2)), H - 1];
    true -> [0, H - 1 - (S - (2 * W + H - 3))]
  end.

-spec robot_get_dir() -> unicode:unicode_binary().
robot_get_dir() ->
  W = get(robot_width),
  H = get(robot_height),
  S = get(robot_pos),
  Moved = get(robot_moved),
  if
    S =:= 0, Moved =:= true -> <<"South">>;
    S =< W - 1 -> <<"East">>;
    S =< W + H - 2 -> <<"North">>;
    S =< 2 * W + H - 3 -> <<"West">>;
    true -> <<"South">>
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Robot do
  @spec init_(width :: integer, height :: integer) :: any
  def init_(width, height) do
    Process.put(:robot_width, width)
    Process.put(:robot_height, height)
    Process.put(:robot_p, 2 * (width + height - 2))
    Process.put(:robot_pos, 0)
    Process.put(:robot_moved, false)
  end

  @spec step(num :: integer) :: any
  def step(num) do
    p = Process.get(:robot_p)
    pos = Process.get(:robot_pos)
    Process.put(:robot_pos, rem(pos + num, p))
    Process.put(:robot_moved, true)
  end

  @spec get_pos() :: [integer]
  def get_pos() do
    w = Process.get(:robot_width)
    h = Process.get(:robot_height)
    s = Process.get(:robot_pos)
    cond do
      s <= w - 1 -> [s, 0]
      s <= w + h - 2 -> [w - 1, s - w + 1]
      s <= 2 * w + h - 3 -> [w - 1 - (s - (w + h - 2)), h - 1]
      true -> [0, h - 1 - (s - (2 * w + h - 3))]
    end
  end

  @spec get_dir() :: String.t
  def get_dir() do
    w = Process.get(:robot_width)
    h = Process.get(:robot_height)
    s = Process.get(:robot_pos)
    moved = Process.get(:robot_moved)
    cond do
      s == 0 and moved -> "South"
      s <= w - 1 -> "East"
      s <= w + h - 2 -> "North"
      s <= 2 * w + h - 3 -> "West"
      true -> "South"
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1) for all operations. The initialization, `step`, `getPos`, and `getDir` methods only involve basic arithmetic, modulo operations, and conditional checks, all of which execute in constant time regardless of the grid size or the number of steps.
- **Space Complexity:** O(1). The solution only requires a few integer variables to store the grid dimensions, the current perimeter position, and a boolean flag to handle the initial state. No additional data structures or memory scaling with input are needed.
