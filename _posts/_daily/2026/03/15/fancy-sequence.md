---
layout: post
title: "Fancy Sequence"
date: 2026-03-15 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Math", "Design", "Segment Tree"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/fancy-sequence/
ai_solutions:
  - solutions:
      cpp: "class Fancy {\n    long long mul = 1, add = 0;\n    std::vector<long long>\
        \ seq;\n    const int MOD = 1e9 + 7;\n\n    long long power(long long b, long\
        \ long e) {\n        long long res = 1;\n        b %= MOD;\n        while (e\
        \ > 0) {\n            if (e % 2 == 1) res = (res * b) % MOD;\n            b\
        \ = (b * b) % MOD;\n            e /= 2;\n        }\n        return res;\n  \
        \  }\n\n    long long modInverse(long long n) {\n        return power(n, MOD\
        \ - 2);\n    }\n\npublic:\n    Fancy() {}\n\n    void append(int val) {\n  \
        \      long long inv = modInverse(mul);\n        long long x = (((long long)val\
        \ - add) % MOD + MOD) % MOD;\n        seq.push_back((x * inv) % MOD);\n    }\n\
        \n    void addAll(int inc) {\n        add = (add + inc) % MOD;\n    }\n\n  \
        \  void multAll(int m) {\n        mul = (mul * m) % MOD;\n        add = (add\
        \ * m) % MOD;\n    }\n\n    int getIndex(int idx) {\n        if (idx >= seq.size())\
        \ return -1;\n        return (seq[idx] * mul + add) % MOD;\n    }\n};"
      java: "class Fancy {\n    private long mul = 1, add = 0;\n    private java.util.List<Long>\
        \ seq = new java.util.ArrayList<>();\n    private final int MOD = 1_000_000_007;\n\
        \n    private long power(long b, long e) {\n        long res = 1;\n        b\
        \ %= MOD;\n        while (e > 0) {\n            if (e % 2 == 1) res = (res *\
        \ b) % MOD;\n            b = (b * b) % MOD;\n            e /= 2;\n        }\n\
        \        return res;\n    }\n\n    public Fancy() {}\n\n    public void append(int\
        \ val) {\n        long inv = power(mul, MOD - 2);\n        long x = (((long)\
        \ val - add) % MOD + MOD) % MOD;\n        seq.add((x * inv) % MOD);\n    }\n\
        \n    public void addAll(int inc) {\n        add = (add + inc) % MOD;\n    }\n\
        \n    public void multAll(int m) {\n        mul = (mul * m) % MOD;\n       \
        \ add = (add * m) % MOD;\n    }\n\n    public int getIndex(int idx) {\n    \
        \    if (idx >= seq.size()) return -1;\n        return (int) ((seq.get(idx)\
        \ * mul + add) % MOD);\n    }\n}"
      python: "class Fancy(object):\n    def __init__(self):\n        self.seq = []\n\
        \        self.mul = 1\n        self.add = 0\n        self.mod = 1000000007\n\
        \n    def append(self, val):\n        inv = pow(self.mul, self.mod - 2, self.mod)\n\
        \        self.seq.append(((val - self.add) * inv) % self.mod)\n\n    def addAll(self,\
        \ inc):\n        self.add = (self.add + inc) % self.mod\n\n    def multAll(self,\
        \ m):\n        self.mul = (self.mul * m) % self.mod\n        self.add = (self.add\
        \ * m) % self.mod\n\n    def getIndex(self, idx):\n        if idx >= len(self.seq):\n\
        \            return -1\n        return (self.seq[idx] * self.mul + self.add)\
        \ % self.mod"
      python3: "class Fancy:\n    def __init__(self):\n        self.seq = []\n     \
        \   self.mul = 1\n        self.add = 0\n        self.mod = 1000000007\n\n  \
        \  def append(self, val: int) -> None:\n        inv = pow(self.mul, self.mod\
        \ - 2, self.mod)\n        self.seq.append(((val - self.add) * inv) % self.mod)\n\
        \n    def addAll(self, inc: int) -> None:\n        self.add = (self.add + inc)\
        \ % self.mod\n\n    def multAll(self, m: int) -> None:\n        self.mul = (self.mul\
        \ * m) % self.mod\n        self.add = (self.add * m) % self.mod\n\n    def getIndex(self,\
        \ idx: int) -> int:\n        if idx >= len(self.seq):\n            return -1\n\
        \        return (self.seq[idx] * self.mul + self.add) % self.mod"
      c: "#include <stdlib.h>\n\ntypedef struct {\n    long long *seq;\n    int size;\n\
        \    int capacity;\n    long long add;\n    long long mul;\n} Fancy;\n\nlong\
        \ long power(long long base, long long exp) {\n    long long res = 1;\n    base\
        \ %= 1000000007;\n    while (exp > 0) {\n        if (exp % 2 == 1) res = (res\
        \ * base) % 1000000007;\n        base = (base * base) % 1000000007;\n      \
        \  exp /= 2;\n    }\n    return res;\n}\n\nFancy* fancyCreate() {\n    Fancy*\
        \ obj = (Fancy*)malloc(sizeof(Fancy));\n    obj->seq = (long long*)malloc(1000\
        \ * sizeof(long long));\n    obj->size = 0;\n    obj->capacity = 1000;\n   \
        \ obj->add = 0;\n    obj->mul = 1;\n    return obj;\n}\n\nvoid fancyAppend(Fancy*\
        \ obj, int val) {\n    if (obj->size == obj->capacity) {\n        obj->capacity\
        \ *= 2;\n        obj->seq = (long long*)realloc(obj->seq, obj->capacity * sizeof(long\
        \ long));\n    }\n    long long inv = power(obj->mul, 1000000007 - 2);\n   \
        \ long long x = (((long long)val - obj->add) % 1000000007 + 1000000007) % 1000000007;\n\
        \    obj->seq[obj->size++] = (x * inv) % 1000000007;\n}\n\nvoid fancyAddAll(Fancy*\
        \ obj, int inc) {\n    obj->add = (obj->add + inc) % 1000000007;\n}\n\nvoid\
        \ fancyMultAll(Fancy* obj, int m) {\n    obj->mul = (obj->mul * m) % 1000000007;\n\
        \    obj->add = (obj->add * m) % 1000000007;\n}\n\nint fancyGetIndex(Fancy*\
        \ obj, int idx) {\n    if (idx >= obj->size) return -1;\n    long long res =\
        \ (obj->seq[idx] * obj->mul + obj->add) % 1000000007;\n    return (int)res;\n\
        }\n\nvoid fancyFree(Fancy* obj) {\n    free(obj->seq);\n    free(obj);\n}"
      csharp: "public class Fancy {\n    private long mul = 1, add = 0;\n    private\
        \ System.Collections.Generic.List<long> seq = new System.Collections.Generic.List<long>();\n\
        \    private const int MOD = 1000000007;\n\n    private long Power(long b, long\
        \ e) {\n        long res = 1;\n        b %= MOD;\n        while (e > 0) {\n\
        \            if (e % 2 == 1) res = (res * b) % MOD;\n            b = (b * b)\
        \ % MOD;\n            e /= 2;\n        }\n        return res;\n    }\n\n   \
        \ public Fancy() {}\n\n    public void Append(int val) {\n        long inv =\
        \ Power(mul, MOD - 2);\n        long x = ((val - add) % MOD + MOD) % MOD;\n\
        \        seq.Add((x * inv) % MOD);\n    }\n\n    public void AddAll(int inc)\
        \ {\n        add = (add + inc) % MOD;\n    }\n\n    public void MultAll(int\
        \ m) {\n        mul = (mul * m) % MOD;\n        add = (add * m) % MOD;\n   \
        \ }\n\n    public int GetIndex(int idx) {\n        if (idx >= seq.Count) return\
        \ -1;\n        return (int)((seq[idx] * mul + add) % MOD);\n    }\n}"
      javascript: "var Fancy = function() {\n    this.seq = [];\n    this.add = 0n;\n\
        \    this.mul = 1n;\n    this.mod = 1000000007n;\n};\n\nFancy.prototype.power\
        \ = function(b, e) {\n    let res = 1n;\n    b %= this.mod;\n    while (e >\
        \ 0n) {\n        if (e % 2n === 1n) res = (res * b) % this.mod;\n        b =\
        \ (b * b) % this.mod;\n        e /= 2n;\n    }\n    return res;\n};\n\nFancy.prototype.append\
        \ = function(val) {\n    let inv = this.power(this.mul, this.mod - 2n);\n  \
        \  let x = (((BigInt(val) - this.add) % this.mod + this.mod) % this.mod * inv)\
        \ % this.mod;\n    this.seq.push(x);\n};\n\nFancy.prototype.addAll = function(inc)\
        \ {\n    this.add = (this.add + BigInt(inc)) % this.mod;\n};\n\nFancy.prototype.multAll\
        \ = function(m) {\n    this.mul = (this.mul * BigInt(m)) % this.mod;\n    this.add\
        \ = (this.add * BigInt(m)) % this.mod;\n};\n\nFancy.prototype.getIndex = function(idx)\
        \ {\n    if (idx >= this.seq.length) return -1;\n    let res = (this.seq[idx]\
        \ * this.mul + this.add) % this.mod;\n    return Number(res);\n};"
      typescript: "class Fancy {\n    private mod: bigint = BigInt(1000000007);\n  \
        \  private seq: bigint[] = [];\n    private m: bigint = 1n;\n    private a:\
        \ bigint = 0n;\n    private invM: bigint = 1n;\n\n    constructor() {}\n\n \
        \   private power(a: bigint, b: bigint): bigint {\n        let res = 1n;\n \
        \       a %= this.mod;\n        while (b > 0n) {\n            if (b % 2n ===\
        \ 1n) res = (res * a) % this.mod;\n            a = (a * a) % this.mod;\n   \
        \         b /= 2n;\n        }\n        return res;\n    }\n\n    private modInverse(n:\
        \ bigint): bigint {\n        return this.power(n, this.mod - 2n);\n    }\n\n\
        \    append(val: number): void {\n        const v = BigInt(val);\n        const\
        \ stored = ((v - this.a + this.mod) % this.mod * this.invM) % this.mod;\n  \
        \      this.seq.push(stored);\n    }\n\n    addAll(inc: number): void {\n  \
        \      this.a = (this.a + BigInt(inc)) % this.mod;\n    }\n\n    multAll(m:\
        \ number): void {\n        const mi = BigInt(m);\n        this.m = (this.m *\
        \ mi) % this.mod;\n        this.a = (this.a * mi) % this.mod;\n        this.invM\
        \ = this.modInverse(this.m);\n    }\n\n    getIndex(idx: number): number {\n\
        \        if (idx >= this.seq.length) return -1;\n        const res = (this.seq[idx]\
        \ * this.m + this.a) % this.mod;\n        return Number(res);\n    }\n}"
      php: "class Fancy {\n    private $mod = 1000000007;\n    private $seq = [];\n\
        \    private $m = 1;\n    private $a = 0;\n    private $invM = 1;\n\n    function\
        \ __construct() {}\n\n    private function power($a, $b) {\n        $res = 1;\n\
        \        $base = $a % $this->mod;\n        while ($b > 0) {\n            if\
        \ ($b % 2 == 1) $res = ($res * $base) % $this->mod;\n            $base = ($base\
        \ * $base) % $this->mod;\n            $b = $b >> 1;\n        }\n        return\
        \ $res;\n    }\n\n    private function modInverse($n) {\n        return $this->power($n,\
        \ $this->mod - 2);\n    }\n\n    function append($val) {\n        $stored =\
        \ (($val - $this->a) % $this->mod + $this->mod) % $this->mod;\n        $stored\
        \ = ($stored * $this->invM) % $this->mod;\n        $this->seq[] = $stored;\n\
        \    }\n\n    function addAll($inc) {\n        $this->a = ($this->a + $inc)\
        \ % $this->mod;\n    }\n\n    function multAll($m) {\n        $this->m = ($this->m\
        \ * $m) % $this->mod;\n        $this->a = ($this->a * $m) % $this->mod;\n  \
        \      $this->invM = $this->modInverse($this->m);\n    }\n\n    function getIndex($idx)\
        \ {\n        if ($idx >= count($this->seq)) return -1;\n        $res = ($this->seq[$idx]\
        \ * $this->m + $this->a) % $this->mod;\n        return (int)$res;\n    }\n}"
      swift: "class Fancy {\n    private let mod: Int64 = 1000000007\n    private var\
        \ seq: [Int64] = []\n    private var m: Int64 = 1\n    private var a: Int64\
        \ = 0\n    private var invM: Int64 = 1\n\n    init() {}\n\n    private func\
        \ power(_ a: Int64, _ b: Int64) -> Int64 {\n        var res: Int64 = 1\n   \
        \     var base = a % mod\n        var exp = b\n        while exp > 0 {\n   \
        \         if exp % 2 == 1 { res = (res * base) % mod }\n            base = (base\
        \ * base) % mod\n            exp /= 2\n        }\n        return res\n    }\n\
        \n    private func modInverse(_ n: Int64) -> Int64 {\n        return power(n,\
        \ mod - 2)\n    }\n\n    func append(_ val: Int) {\n        let v = Int64(val)\n\
        \        let stored = ((v - a % mod + mod) % mod * invM) % mod\n        seq.append(stored)\n\
        \    }\n\n    func addAll(_ inc: Int) {\n        a = (a + Int64(inc)) % mod\n\
        \    }\n\n    func multAll(_ m: Int) {\n        let mi = Int64(m)\n        self.m\
        \ = (self.m * mi) % mod\n        self.a = (self.a * mi) % mod\n        self.invM\
        \ = modInverse(self.m)\n    }\n\n    func getIndex(_ idx: Int) -> Int {\n  \
        \      if idx >= seq.count { return -1 }\n        let res = (seq[idx] * m +\
        \ a) % mod\n        return Int(res)\n    }\n}"
      kotlin: "class Fancy() {\n    private val mod: Long = 1000000007L\n    private\
        \ var seq = mutableListOf<Long>()\n    private var m: Long = 1L\n    private\
        \ var a: Long = 0L\n    private var invM: Long = 1L\n\n    private fun power(a:\
        \ Long, b: Long): Long {\n        var res = 1L\n        var base = a % mod\n\
        \        var exp = b\n        while (exp > 0) {\n            if (exp % 2 ==\
        \ 1L) res = (res * base) % mod\n            base = (base * base) % mod\n   \
        \         exp /= 2\n        }\n        return res\n    }\n\n    private fun\
        \ modInverse(n: Long): Long {\n        return power(n, mod - 2)\n    }\n\n \
        \   fun append(`val`: Int) {\n        val v = `val`.toLong()\n        val stored\
        \ = ((v - a % mod + mod) % mod * invM) % mod\n        seq.add(stored)\n    }\n\
        \n    fun addAll(inc: Int) {\n        a = (a + inc.toLong()) % mod\n    }\n\n\
        \    fun multAll(m: Int) {\n        val mi = m.toLong()\n        this.m = (this.m\
        \ * mi) % mod\n        this.a = (this.a * mi) % mod\n        this.invM = modInverse(this.m)\n\
        \    }\n\n    fun getIndex(idx: Int): Int {\n        if (idx >= seq.size) return\
        \ -1\n        val res = (seq[idx] * m + a) % mod\n        return res.toInt()\n\
        \    }\n}"
      dart: "class Fancy {\n  final int _mod = 1000000007;\n  List<int> _seq = [];\n\
        \  int _m = 1;\n  int _a = 0;\n  int _invM = 1;\n\n  Fancy() {}\n\n  int _power(int\
        \ a, int b) {\n    int res = 1;\n    int base = a % _mod;\n    while (b > 0)\
        \ {\n      if (b % 2 == 1) res = (res * base) % _mod;\n      base = (base *\
        \ base) % _mod;\n      b ~/= 2;\n    }\n    return res;\n  }\n\n  int _modInverse(int\
        \ n) {\n    return _power(n, _mod - 2);\n  }\n\n  void append(int val) {\n \
        \   int stored = ((val - _a % _mod + _mod) % _mod * _invM) % _mod;\n    _seq.add(stored);\n\
        \  }\n\n  void addAll(int inc) {\n    _a = (_a + inc) % _mod;\n  }\n\n  void\
        \ multAll(int m) {\n    _m = (_m * m) % _mod;\n    _a = (_a * m) % _mod;\n \
        \   _invM = _modInverse(_m);\n  }\n\n  int getIndex(int idx) {\n    if (idx\
        \ >= _seq.length) return -1;\n    return (_seq[idx] * _m + _a) % _mod;\n  }\n\
        }"
      go: "type Fancy struct {\n\tmod  int64\n\tseq  []int64\n\tm    int64\n\ta    int64\n\
        \tinvM int64\n}\n\nfunc Constructor() Fancy {\n\treturn Fancy{\n\t\tmod:  1000000007,\n\
        \t\tseq:  []int64{},\n\t\tm:    1,\n\t\ta:    0,\n\t\tinvM: 1,\n\t}\n}\n\nfunc\
        \ (this *Fancy) power(a, b int64) int64 {\n\tres := int64(1)\n\tbase := a %\
        \ this.mod\n\tfor b > 0 {\n\t\tif b%2 == 1 {\n\t\t\tres = (res * base) % this.mod\n\
        \t\t}\n\t\tbase = (base * base) % this.mod\n\t\tb /= 2\n\t}\n\treturn res\n\
        }\n\nfunc (this *Fancy) modInverse(n int64) int64 {\n\treturn this.power(n,\
        \ this.mod-2)\n}\n\nfunc (this *Fancy) Append(val int) {\n\tv := int64(val)\n\
        \tstored := ((v - this.a%this.mod + this.mod) % this.mod * this.invM) % this.mod\n\
        \tthis.seq = append(this.seq, stored)\n}\n\nfunc (this *Fancy) AddAll(inc int)\
        \ {\n\tthis.a = (this.a + int64(inc)) % this.mod\n}\n\nfunc (this *Fancy) MultAll(m\
        \ int) {\n\tmi := int64(m)\n\tthis.m = (this.m * mi) % this.mod\n\tthis.a =\
        \ (this.a * mi) % this.mod\n\tthis.invM = this.modInverse(this.m)\n}\n\nfunc\
        \ (this *Fancy) GetIndex(idx int) int {\n\tif idx >= len(this.seq) {\n\t\treturn\
        \ -1\n\t}\n\tres := (this.seq[idx]*this.m + this.a) % this.mod\n\treturn int(res)\n\
        }"
      ruby: "class Fancy\n    def initialize()\n      @a = 1\n      @b = 0\n      @vals\
        \ = []\n      @mod = 1_000_000_007\n    end\n\n    def power(a, b)\n      res\
        \ = 1\n      base = a % @mod\n      while b > 0\n        res = (res * base)\
        \ % @mod if b % 2 == 1\n        base = (base * base) % @mod\n        b /= 2\n\
        \      end\n      res\n    end\n\n    def append(val)\n      inv_a = power(@a,\
        \ @mod - 2)\n      @vals << (((val - @b) % @mod + @mod) % @mod * inv_a) % @mod\n\
        \    end\n\n    def add_all(inc)\n      @b = (@b + inc) % @mod\n    end\n\n\
        \    def mult_all(m)\n      @a = (@a * m) % @mod\n      @b = (@b * m) % @mod\n\
        \    end\n\n    def get_index(idx)\n      idx >= @vals.length ? -1 : (@vals[idx]\
        \ * @a + @b) % @mod\n    end\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\n\nclass Fancy() {\n  private\
        \ var a: Long = 1\n  private var b: Long = 0\n  private val vals = new ArrayBuffer[Long]()\n\
        \  private val MOD: Long = 1000000007\n\n  private def power(base: Long, exp:\
        \ Long): Long = {\n    var res = 1L\n    var b = base % MOD\n    var e = exp\n\
        \    while (e > 0) {\n      if (e % 2 == 1) res = (res * b) % MOD\n      b =\
        \ (b * b) % MOD\n      e /= 2\n    }\n    res\n  }\n\n  def append(`val`: Int):\
        \ Unit = {\n    val invA = power(a, MOD - 2)\n    val valAdj = (((`val`.toLong\
        \ - b) % MOD + MOD) % MOD * invA) % MOD\n    vals.append(valAdj)\n  }\n\n  def\
        \ addAll(inc: Int): Unit = {\n    b = (b + inc.toLong) % MOD\n  }\n\n  def multAll(m:\
        \ Int): Unit = {\n    a = (a * m.toLong) % MOD\n    b = (b * m.toLong) % MOD\n\
        \  }\n\n  def getIndex(idx: Int): Int = {\n    if (idx >= vals.length) -1\n\
        \    else ((vals(idx) * a + b) % MOD).toInt\n  }\n}"
      rust: "struct Fancy {\n    a: i64,\n    b: i64,\n    vals: Vec<i64>,\n}\n\nimpl\
        \ Fancy {\n    fn new() -> Self {\n        Fancy { a: 1, b: 0, vals: Vec::new()\
        \ }\n    }\n\n    fn power(mut a: i64, mut b: i64) -> i64 {\n        let mut\
        \ res = 1;\n        let m = 1000000007;\n        a %= m;\n        while b >\
        \ 0 {\n            if b % 2 == 1 { res = (res * a) % m; }\n            a = (a\
        \ * a) % m;\n            b /= 2;\n        }\n        res\n    }\n\n    fn append(&mut\
        \ self, val: i32) {\n        let inv_a = Self::power(self.a, 1000000007 - 2);\n\
        \        let val_adj = (((val as i64 - self.b) % 1000000007 + 1000000007) %\
        \ 1000000007 * inv_a) % 1000000007;\n        self.vals.push(val_adj);\n    }\n\
        \n    fn add_all(&mut self, inc: i32) {\n        self.b = (self.b + inc as i64)\
        \ % 1000000007;\n    }\n\n    fn mult_all(&mut self, m: i32) {\n        self.a\
        \ = (self.a * m as i64) % 1000000007;\n        self.b = (self.b * m as i64)\
        \ % 1000000007;\n    }\n\n    fn get_index(&self, idx: i32) -> i32 {\n     \
        \   if (idx as usize) >= self.vals.len() {\n            return -1;\n       \
        \ }\n        let res = (self.vals[idx as usize] * self.a + self.b) % 1000000007;\n\
        \        res as i32\n    }\n}"
      racket: (define fancy% (class object% (super-new) (init-field) (define vals (make-vector
        100005)) (define a 1) (define b 0) (define len 0) (define (power base exp) (let
        loop ([base (modulo base 1000000007)] [exp exp] [res 1]) (if (= exp 0) res (loop
        (modulo (* base base) 1000000007) (quotient exp 2) (if (odd? exp) (modulo (*
        res base) 1000000007) res))))) (define/public (append val) (let* ([inv-a (power
        a (- 1000000007 2))] [val-adj (modulo (* (modulo (- val b) 1000000007) inv-a)
        1000000007)]) (vector-set! vals len val-adj) (set! len (+ len 1)))) (define/public
        (add-all inc) (set! b (modulo (+ b inc) 1000000007))) (define/public (mult-all
        m) (set! a (modulo (* a m) 1000000007)) (set! b (modulo (* b m) 1000000007)))
        (define/public (get-index idx) (if (>= idx len) -1 (modulo (+ (* (vector-ref
        vals idx) a) b) 1000000007)))))
      erlang: "power(A, B) -> power(A, B, 1).\npower(_A, 0, Res) -> Res;\npower(A, B,\
        \ Res) ->\n    NewRes = if B rem 2 == 1 -> (Res * A) rem 1000000007; true ->\
        \ Res end,\n    power((A * A) rem 1000000007, B div 2, NewRes).\n\nfancy_init_()\
        \ ->\n    erase(),\n    put(a, 1),\n    put(b, 0),\n    put(len, 0).\n\nfancy_append(Val)\
        \ ->\n    A = get(a),\n    B = get(b),\n    L = get(len),\n    InvA = power(A,\
        \ 1000000007 - 2),\n    ValAdj = ((((Val - B) rem 1000000007 + 1000000007) rem\
        \ 1000000007) * InvA) rem 1000000007,\n    put(L, ValAdj),\n    put(len, L +\
        \ 1).\n\nfancy_add_all(Inc) ->\n    put(b, (get(b) + Inc) rem 1000000007).\n\
        \nfancy_mult_all(M) ->\n    put(a, (get(a) * M) rem 1000000007),\n    put(b,\
        \ (get(b) * M) rem 1000000007).\n\nfancy_get_index(Idx) ->\n    L = get(len),\n\
        \    if\n        Idx >= L -> -1;\n        true -> (get(Idx) * get(a) + get(b))\
        \ rem 1000000007\n    end."
      elixir: "defmodule Fancy do\n  defp power(a, b), do: power(a, b, 1)\n  defp power(_a,\
        \ 0, res), do: res\n  defp power(a, b, res) do\n    new_res = if rem(b, 2) ==\
        \ 1, do: rem(res * a, 1000000007), else: res\n    power(rem(a * a, 1000000007),\
        \ div(b, 2), new_res)\n  end\n\n  def init_() do\n    Process.put(:a, 1)\n \
        \   Process.put(:b, 0)\n    Process.put(:len, 0)\n  end\n\n  def append(val)\
        \ do\n    a = Process.get(:a)\n    b = Process.get(:b)\n    l = Process.get(:len)\n\
        \    inv_a = power(a, 1000000007 - 2)\n    val_adj = rem(rem(rem(val - b, 1000000007)\
        \ + 1000000007, 1000000007) * inv_a, 1000000007)\n    Process.put(l, val_adj)\n\
        \    Process.put(:len, l + 1)\n  end\n\n  def add_all(inc) do\n    b = Process.get(:b)\n\
        \    Process.put(:b, rem(b + inc, 1000000007))\n  end\n\n  def mult_all(m) do\n\
        \    a = Process.get(:a)\n    b = Process.get(:b)\n    Process.put(:a, rem(a\
        \ * m, 1000000007))\n    Process.put(:b, rem(b * m, 1000000007))\n  end\n\n\
        \  def get_index(idx) do\n    l = Process.get(:len)\n    if idx >= l do\n  \
        \    -1\n    else\n      a = Process.get(:a)\n      b = Process.get(:b)\n  \
        \    val_adj = Process.get(idx)\n      rem(val_adj * a + b, 1000000007)\n  \
        \  end\n  end\nend"
    approach: 'To efficiently manage sequence operations, we maintain a global transformation
      state represented by two variables: a cumulative multiplier $M$ and a cumulative
      adder $A$. These represent the function $f(x) = (M \cdot x + A) \pmod{10^9+7}$
      applied to all elements currently in the sequence. When ''addAll(inc)'' is called,
      we update $A = (A + inc) \pmod{MOD}$. When ''multAll(m)'' is called, we update
      both $M = (M \cdot m) \pmod{MOD}$ and $A = (A \cdot m) \pmod{MOD}$. This allows
      ''addAll'' and ''multAll'' to run in $O(1)$ time by just updating the global state
      variables.


      When a new value ''val'' is appended, we cannot simply store it as-is because
      the current global transformation $(M, A)$ should not have affected it yet. Instead,
      we store a ''pre-transformed'' value $x$ such that $(x \cdot M + A) \equiv val
      \pmod{MOD}$. To find $x$, we compute $x = (val - A) \cdot M^{-1} \pmod{MOD}$.
      Since $MOD = 10^9+7$ is prime and $M$ is a product of integers in $[1, 100]$,
      $M$ is never a multiple of $MOD$ and its modular inverse exists. We calculate
      $M^{-1}$ using Fermat''s Little Theorem ($M^{MOD-2} \pmod{MOD}$). For ''getIndex(idx)'',
      we simply return $(seq[idx] \cdot M + A) \pmod{MOD}$.'
    time_complexity: O(N \log MOD) where N is the total number of operations. The 'addAll',
      'multAll', and 'getIndex' operations are O(1). The 'append' operation is O(\log
      MOD) due to the modular exponentiation required for finding the modular inverse.
      Given MOD is $10^9+7$, \log MOD is approximately 30.
    space_complexity: O(N) to store the sequence of values in a dynamic array or list.
    elapsed_time: 225.86436581611633
    model: gemini-3-flash-preview
    generated_at: '2026-03-15 01:49:31 '
---

## Problem #1622: Fancy Sequence

**Difficulty:** Hard

**Topics:** Math, Design, Segment Tree

## Problem Description

<p>Write an API that generates fancy sequences using the <code>append</code>, <code>addAll</code>, and <code>multAll</code> operations.</p>

<p>Implement the <code>Fancy</code> class:</p>

<ul>
	<li><code>Fancy()</code> Initializes the object with an empty sequence.</li>
	<li><code>void append(val)</code> Appends an integer <code>val</code> to the end of the sequence.</li>
	<li><code>void addAll(inc)</code> Increments all existing values in the sequence by an integer <code>inc</code>.</li>
	<li><code>void multAll(m)</code> Multiplies all existing values in the sequence by an integer <code>m</code>.</li>
	<li><code>int getIndex(idx)</code> Gets the current value at index <code>idx</code> (0-indexed) of the sequence <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>. If the index is greater or equal than the length of the sequence, return <code>-1</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Fancy&quot;, &quot;append&quot;, &quot;addAll&quot;, &quot;append&quot;, &quot;multAll&quot;, &quot;getIndex&quot;, &quot;addAll&quot;, &quot;append&quot;, &quot;multAll&quot;, &quot;getIndex&quot;, &quot;getIndex&quot;, &quot;getIndex&quot;]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
<strong>Output</strong>
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

<strong>Explanation</strong>
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -&gt; [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -&gt; [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -&gt; [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -&gt; [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= val, inc, m &lt;= 100</code></li>
	<li><code>0 &lt;= idx &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>10<sup>5</sup></code> calls total will be made to <code>append</code>, <code>addAll</code>, <code>multAll</code>, and <code>getIndex</code>.</li>
</ul>


## Hints

1. Use two arrays to save the cumulative multipliers at each time point and cumulative sums adjusted by the current multiplier.

2. The function getIndex(idx) ask to the current value modulo 10^9+7. Use modular inverse and both arrays to calculate this value.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To efficiently manage sequence operations, we maintain a global transformation state represented by two variables: a cumulative multiplier $M$ and a cumulative adder $A$. These represent the function $f(x) = (M \cdot x + A) \pmod{10^9+7}$ applied to all elements currently in the sequence. When 'addAll(inc)' is called, we update $A = (A + inc) \pmod{MOD}$. When 'multAll(m)' is called, we update both $M = (M \cdot m) \pmod{MOD}$ and $A = (A \cdot m) \pmod{MOD}$. This allows 'addAll' and 'multAll' to run in $O(1)$ time by just updating the global state variables.

When a new value 'val' is appended, we cannot simply store it as-is because the current global transformation $(M, A)$ should not have affected it yet. Instead, we store a 'pre-transformed' value $x$ such that $(x \cdot M + A) \equiv val \pmod{MOD}$. To find $x$, we compute $x = (val - A) \cdot M^{-1} \pmod{MOD}$. Since $MOD = 10^9+7$ is prime and $M$ is a product of integers in $[1, 100]$, $M$ is never a multiple of $MOD$ and its modular inverse exists. We calculate $M^{-1}$ using Fermat's Little Theorem ($M^{MOD-2} \pmod{MOD}$). For 'getIndex(idx)', we simply return $(seq[idx] \cdot M + A) \pmod{MOD}$.

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
class Fancy {
    long long mul = 1, add = 0;
    std::vector<long long> seq;
    const int MOD = 1e9 + 7;

    long long power(long long b, long long e) {
        long long res = 1;
        b %= MOD;
        while (e > 0) {
            if (e % 2 == 1) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e /= 2;
        }
        return res;
    }

    long long modInverse(long long n) {
        return power(n, MOD - 2);
    }

public:
    Fancy() {}

    void append(int val) {
        long long inv = modInverse(mul);
        long long x = (((long long)val - add) % MOD + MOD) % MOD;
        seq.push_back((x * inv) % MOD);
    }

    void addAll(int inc) {
        add = (add + inc) % MOD;
    }

    void multAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }

    int getIndex(int idx) {
        if (idx >= seq.size()) return -1;
        return (seq[idx] * mul + add) % MOD;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Fancy {
    private long mul = 1, add = 0;
    private java.util.List<Long> seq = new java.util.ArrayList<>();
    private final int MOD = 1_000_000_007;

    private long power(long b, long e) {
        long res = 1;
        b %= MOD;
        while (e > 0) {
            if (e % 2 == 1) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e /= 2;
        }
        return res;
    }

    public Fancy() {}

    public void append(int val) {
        long inv = power(mul, MOD - 2);
        long x = (((long) val - add) % MOD + MOD) % MOD;
        seq.add((x * inv) % MOD);
    }

    public void addAll(int inc) {
        add = (add + inc) % MOD;
    }

    public void multAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }

    public int getIndex(int idx) {
        if (idx >= seq.size()) return -1;
        return (int) ((seq.get(idx) * mul + add) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Fancy(object):
    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0
        self.mod = 1000000007

    def append(self, val):
        inv = pow(self.mul, self.mod - 2, self.mod)
        self.seq.append(((val - self.add) * inv) % self.mod)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.mod

    def multAll(self, m):
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Fancy:
    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0
        self.mod = 1000000007

    def append(self, val: int) -> None:
        inv = pow(self.mul, self.mod - 2, self.mod)
        self.seq.append(((val - self.add) * inv) % self.mod)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

typedef struct {
    long long *seq;
    int size;
    int capacity;
    long long add;
    long long mul;
} Fancy;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= 1000000007;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % 1000000007;
        base = (base * base) % 1000000007;
        exp /= 2;
    }
    return res;
}

Fancy* fancyCreate() {
    Fancy* obj = (Fancy*)malloc(sizeof(Fancy));
    obj->seq = (long long*)malloc(1000 * sizeof(long long));
    obj->size = 0;
    obj->capacity = 1000;
    obj->add = 0;
    obj->mul = 1;
    return obj;
}

void fancyAppend(Fancy* obj, int val) {
    if (obj->size == obj->capacity) {
        obj->capacity *= 2;
        obj->seq = (long long*)realloc(obj->seq, obj->capacity * sizeof(long long));
    }
    long long inv = power(obj->mul, 1000000007 - 2);
    long long x = (((long long)val - obj->add) % 1000000007 + 1000000007) % 1000000007;
    obj->seq[obj->size++] = (x * inv) % 1000000007;
}

void fancyAddAll(Fancy* obj, int inc) {
    obj->add = (obj->add + inc) % 1000000007;
}

void fancyMultAll(Fancy* obj, int m) {
    obj->mul = (obj->mul * m) % 1000000007;
    obj->add = (obj->add * m) % 1000000007;
}

int fancyGetIndex(Fancy* obj, int idx) {
    if (idx >= obj->size) return -1;
    long long res = (obj->seq[idx] * obj->mul + obj->add) % 1000000007;
    return (int)res;
}

void fancyFree(Fancy* obj) {
    free(obj->seq);
    free(obj);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Fancy {
    private long mul = 1, add = 0;
    private System.Collections.Generic.List<long> seq = new System.Collections.Generic.List<long>();
    private const int MOD = 1000000007;

    private long Power(long b, long e) {
        long res = 1;
        b %= MOD;
        while (e > 0) {
            if (e % 2 == 1) res = (res * b) % MOD;
            b = (b * b) % MOD;
            e /= 2;
        }
        return res;
    }

    public Fancy() {}

    public void Append(int val) {
        long inv = Power(mul, MOD - 2);
        long x = ((val - add) % MOD + MOD) % MOD;
        seq.Add((x * inv) % MOD);
    }

    public void AddAll(int inc) {
        add = (add + inc) % MOD;
    }

    public void MultAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }

    public int GetIndex(int idx) {
        if (idx >= seq.Count) return -1;
        return (int)((seq[idx] * mul + add) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var Fancy = function() {
    this.seq = [];
    this.add = 0n;
    this.mul = 1n;
    this.mod = 1000000007n;
};

Fancy.prototype.power = function(b, e) {
    let res = 1n;
    b %= this.mod;
    while (e > 0n) {
        if (e % 2n === 1n) res = (res * b) % this.mod;
        b = (b * b) % this.mod;
        e /= 2n;
    }
    return res;
};

Fancy.prototype.append = function(val) {
    let inv = this.power(this.mul, this.mod - 2n);
    let x = (((BigInt(val) - this.add) % this.mod + this.mod) % this.mod * inv) % this.mod;
    this.seq.push(x);
};

Fancy.prototype.addAll = function(inc) {
    this.add = (this.add + BigInt(inc)) % this.mod;
};

Fancy.prototype.multAll = function(m) {
    this.mul = (this.mul * BigInt(m)) % this.mod;
    this.add = (this.add * BigInt(m)) % this.mod;
};

Fancy.prototype.getIndex = function(idx) {
    if (idx >= this.seq.length) return -1;
    let res = (this.seq[idx] * this.mul + this.add) % this.mod;
    return Number(res);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class Fancy {
    private mod: bigint = BigInt(1000000007);
    private seq: bigint[] = [];
    private m: bigint = 1n;
    private a: bigint = 0n;
    private invM: bigint = 1n;

    constructor() {}

    private power(a: bigint, b: bigint): bigint {
        let res = 1n;
        a %= this.mod;
        while (b > 0n) {
            if (b % 2n === 1n) res = (res * a) % this.mod;
            a = (a * a) % this.mod;
            b /= 2n;
        }
        return res;
    }

    private modInverse(n: bigint): bigint {
        return this.power(n, this.mod - 2n);
    }

    append(val: number): void {
        const v = BigInt(val);
        const stored = ((v - this.a + this.mod) % this.mod * this.invM) % this.mod;
        this.seq.push(stored);
    }

    addAll(inc: number): void {
        this.a = (this.a + BigInt(inc)) % this.mod;
    }

    multAll(m: number): void {
        const mi = BigInt(m);
        this.m = (this.m * mi) % this.mod;
        this.a = (this.a * mi) % this.mod;
        this.invM = this.modInverse(this.m);
    }

    getIndex(idx: number): number {
        if (idx >= this.seq.length) return -1;
        const res = (this.seq[idx] * this.m + this.a) % this.mod;
        return Number(res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Fancy {
    private $mod = 1000000007;
    private $seq = [];
    private $m = 1;
    private $a = 0;
    private $invM = 1;

    function __construct() {}

    private function power($a, $b) {
        $res = 1;
        $base = $a % $this->mod;
        while ($b > 0) {
            if ($b % 2 == 1) $res = ($res * $base) % $this->mod;
            $base = ($base * $base) % $this->mod;
            $b = $b >> 1;
        }
        return $res;
    }

    private function modInverse($n) {
        return $this->power($n, $this->mod - 2);
    }

    function append($val) {
        $stored = (($val - $this->a) % $this->mod + $this->mod) % $this->mod;
        $stored = ($stored * $this->invM) % $this->mod;
        $this->seq[] = $stored;
    }

    function addAll($inc) {
        $this->a = ($this->a + $inc) % $this->mod;
    }

    function multAll($m) {
        $this->m = ($this->m * $m) % $this->mod;
        $this->a = ($this->a * $m) % $this->mod;
        $this->invM = $this->modInverse($this->m);
    }

    function getIndex($idx) {
        if ($idx >= count($this->seq)) return -1;
        $res = ($this->seq[$idx] * $this->m + $this->a) % $this->mod;
        return (int)$res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Fancy {
    private let mod: Int64 = 1000000007
    private var seq: [Int64] = []
    private var m: Int64 = 1
    private var a: Int64 = 0
    private var invM: Int64 = 1

    init() {}

    private func power(_ a: Int64, _ b: Int64) -> Int64 {
        var res: Int64 = 1
        var base = a % mod
        var exp = b
        while exp > 0 {
            if exp % 2 == 1 { res = (res * base) % mod }
            base = (base * base) % mod
            exp /= 2
        }
        return res
    }

    private func modInverse(_ n: Int64) -> Int64 {
        return power(n, mod - 2)
    }

    func append(_ val: Int) {
        let v = Int64(val)
        let stored = ((v - a % mod + mod) % mod * invM) % mod
        seq.append(stored)
    }

    func addAll(_ inc: Int) {
        a = (a + Int64(inc)) % mod
    }

    func multAll(_ m: Int) {
        let mi = Int64(m)
        self.m = (self.m * mi) % mod
        self.a = (self.a * mi) % mod
        self.invM = modInverse(self.m)
    }

    func getIndex(_ idx: Int) -> Int {
        if idx >= seq.count { return -1 }
        let res = (seq[idx] * m + a) % mod
        return Int(res)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Fancy() {
    private val mod: Long = 1000000007L
    private var seq = mutableListOf<Long>()
    private var m: Long = 1L
    private var a: Long = 0L
    private var invM: Long = 1L

    private fun power(a: Long, b: Long): Long {
        var res = 1L
        var base = a % mod
        var exp = b
        while (exp > 0) {
            if (exp % 2 == 1L) res = (res * base) % mod
            base = (base * base) % mod
            exp /= 2
        }
        return res
    }

    private fun modInverse(n: Long): Long {
        return power(n, mod - 2)
    }

    fun append(`val`: Int) {
        val v = `val`.toLong()
        val stored = ((v - a % mod + mod) % mod * invM) % mod
        seq.add(stored)
    }

    fun addAll(inc: Int) {
        a = (a + inc.toLong()) % mod
    }

    fun multAll(m: Int) {
        val mi = m.toLong()
        this.m = (this.m * mi) % mod
        this.a = (this.a * mi) % mod
        this.invM = modInverse(this.m)
    }

    fun getIndex(idx: Int): Int {
        if (idx >= seq.size) return -1
        val res = (seq[idx] * m + a) % mod
        return res.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Fancy {
  final int _mod = 1000000007;
  List<int> _seq = [];
  int _m = 1;
  int _a = 0;
  int _invM = 1;

  Fancy() {}

  int _power(int a, int b) {
    int res = 1;
    int base = a % _mod;
    while (b > 0) {
      if (b % 2 == 1) res = (res * base) % _mod;
      base = (base * base) % _mod;
      b ~/= 2;
    }
    return res;
  }

  int _modInverse(int n) {
    return _power(n, _mod - 2);
  }

  void append(int val) {
    int stored = ((val - _a % _mod + _mod) % _mod * _invM) % _mod;
    _seq.add(stored);
  }

  void addAll(int inc) {
    _a = (_a + inc) % _mod;
  }

  void multAll(int m) {
    _m = (_m * m) % _mod;
    _a = (_a * m) % _mod;
    _invM = _modInverse(_m);
  }

  int getIndex(int idx) {
    if (idx >= _seq.length) return -1;
    return (_seq[idx] * _m + _a) % _mod;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
type Fancy struct {
	mod  int64
	seq  []int64
	m    int64
	a    int64
	invM int64
}

func Constructor() Fancy {
	return Fancy{
		mod:  1000000007,
		seq:  []int64{},
		m:    1,
		a:    0,
		invM: 1,
	}
}

func (this *Fancy) power(a, b int64) int64 {
	res := int64(1)
	base := a % this.mod
	for b > 0 {
		if b%2 == 1 {
			res = (res * base) % this.mod
		}
		base = (base * base) % this.mod
		b /= 2
	}
	return res
}

func (this *Fancy) modInverse(n int64) int64 {
	return this.power(n, this.mod-2)
}

func (this *Fancy) Append(val int) {
	v := int64(val)
	stored := ((v - this.a%this.mod + this.mod) % this.mod * this.invM) % this.mod
	this.seq = append(this.seq, stored)
}

func (this *Fancy) AddAll(inc int) {
	this.a = (this.a + int64(inc)) % this.mod
}

func (this *Fancy) MultAll(m int) {
	mi := int64(m)
	this.m = (this.m * mi) % this.mod
	this.a = (this.a * mi) % this.mod
	this.invM = this.modInverse(this.m)
}

func (this *Fancy) GetIndex(idx int) int {
	if idx >= len(this.seq) {
		return -1
	}
	res := (this.seq[idx]*this.m + this.a) % this.mod
	return int(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Fancy
    def initialize()
      @a = 1
      @b = 0
      @vals = []
      @mod = 1_000_000_007
    end

    def power(a, b)
      res = 1
      base = a % @mod
      while b > 0
        res = (res * base) % @mod if b % 2 == 1
        base = (base * base) % @mod
        b /= 2
      end
      res
    end

    def append(val)
      inv_a = power(@a, @mod - 2)
      @vals << (((val - @b) % @mod + @mod) % @mod * inv_a) % @mod
    end

    def add_all(inc)
      @b = (@b + inc) % @mod
    end

    def mult_all(m)
      @a = (@a * m) % @mod
      @b = (@b * m) % @mod
    end

    def get_index(idx)
      idx >= @vals.length ? -1 : (@vals[idx] * @a + @b) % @mod
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

class Fancy() {
  private var a: Long = 1
  private var b: Long = 0
  private val vals = new ArrayBuffer[Long]()
  private val MOD: Long = 1000000007

  private def power(base: Long, exp: Long): Long = {
    var res = 1L
    var b = base % MOD
    var e = exp
    while (e > 0) {
      if (e % 2 == 1) res = (res * b) % MOD
      b = (b * b) % MOD
      e /= 2
    }
    res
  }

  def append(`val`: Int): Unit = {
    val invA = power(a, MOD - 2)
    val valAdj = (((`val`.toLong - b) % MOD + MOD) % MOD * invA) % MOD
    vals.append(valAdj)
  }

  def addAll(inc: Int): Unit = {
    b = (b + inc.toLong) % MOD
  }

  def multAll(m: Int): Unit = {
    a = (a * m.toLong) % MOD
    b = (b * m.toLong) % MOD
  }

  def getIndex(idx: Int): Int = {
    if (idx >= vals.length) -1
    else ((vals(idx) * a + b) % MOD).toInt
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Fancy {
    a: i64,
    b: i64,
    vals: Vec<i64>,
}

impl Fancy {
    fn new() -> Self {
        Fancy { a: 1, b: 0, vals: Vec::new() }
    }

    fn power(mut a: i64, mut b: i64) -> i64 {
        let mut res = 1;
        let m = 1000000007;
        a %= m;
        while b > 0 {
            if b % 2 == 1 { res = (res * a) % m; }
            a = (a * a) % m;
            b /= 2;
        }
        res
    }

    fn append(&mut self, val: i32) {
        let inv_a = Self::power(self.a, 1000000007 - 2);
        let val_adj = (((val as i64 - self.b) % 1000000007 + 1000000007) % 1000000007 * inv_a) % 1000000007;
        self.vals.push(val_adj);
    }

    fn add_all(&mut self, inc: i32) {
        self.b = (self.b + inc as i64) % 1000000007;
    }

    fn mult_all(&mut self, m: i32) {
        self.a = (self.a * m as i64) % 1000000007;
        self.b = (self.b * m as i64) % 1000000007;
    }

    fn get_index(&self, idx: i32) -> i32 {
        if (idx as usize) >= self.vals.len() {
            return -1;
        }
        let res = (self.vals[idx as usize] * self.a + self.b) % 1000000007;
        res as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define fancy% (class object% (super-new) (init-field) (define vals (make-vector 100005)) (define a 1) (define b 0) (define len 0) (define (power base exp) (let loop ([base (modulo base 1000000007)] [exp exp] [res 1]) (if (= exp 0) res (loop (modulo (* base base) 1000000007) (quotient exp 2) (if (odd? exp) (modulo (* res base) 1000000007) res))))) (define/public (append val) (let* ([inv-a (power a (- 1000000007 2))] [val-adj (modulo (* (modulo (- val b) 1000000007) inv-a) 1000000007)]) (vector-set! vals len val-adj) (set! len (+ len 1)))) (define/public (add-all inc) (set! b (modulo (+ b inc) 1000000007))) (define/public (mult-all m) (set! a (modulo (* a m) 1000000007)) (set! b (modulo (* b m) 1000000007))) (define/public (get-index idx) (if (>= idx len) -1 (modulo (+ (* (vector-ref vals idx) a) b) 1000000007)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
power(A, B) -> power(A, B, 1).
power(_A, 0, Res) -> Res;
power(A, B, Res) ->
    NewRes = if B rem 2 == 1 -> (Res * A) rem 1000000007; true -> Res end,
    power((A * A) rem 1000000007, B div 2, NewRes).

fancy_init_() ->
    erase(),
    put(a, 1),
    put(b, 0),
    put(len, 0).

fancy_append(Val) ->
    A = get(a),
    B = get(b),
    L = get(len),
    InvA = power(A, 1000000007 - 2),
    ValAdj = ((((Val - B) rem 1000000007 + 1000000007) rem 1000000007) * InvA) rem 1000000007,
    put(L, ValAdj),
    put(len, L + 1).

fancy_add_all(Inc) ->
    put(b, (get(b) + Inc) rem 1000000007).

fancy_mult_all(M) ->
    put(a, (get(a) * M) rem 1000000007),
    put(b, (get(b) * M) rem 1000000007).

fancy_get_index(Idx) ->
    L = get(len),
    if
        Idx >= L -> -1;
        true -> (get(Idx) * get(a) + get(b)) rem 1000000007
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Fancy do
  defp power(a, b), do: power(a, b, 1)
  defp power(_a, 0, res), do: res
  defp power(a, b, res) do
    new_res = if rem(b, 2) == 1, do: rem(res * a, 1000000007), else: res
    power(rem(a * a, 1000000007), div(b, 2), new_res)
  end

  def init_() do
    Process.put(:a, 1)
    Process.put(:b, 0)
    Process.put(:len, 0)
  end

  def append(val) do
    a = Process.get(:a)
    b = Process.get(:b)
    l = Process.get(:len)
    inv_a = power(a, 1000000007 - 2)
    val_adj = rem(rem(rem(val - b, 1000000007) + 1000000007, 1000000007) * inv_a, 1000000007)
    Process.put(l, val_adj)
    Process.put(:len, l + 1)
  end

  def add_all(inc) do
    b = Process.get(:b)
    Process.put(:b, rem(b + inc, 1000000007))
  end

  def mult_all(m) do
    a = Process.get(:a)
    b = Process.get(:b)
    Process.put(:a, rem(a * m, 1000000007))
    Process.put(:b, rem(b * m, 1000000007))
  end

  def get_index(idx) do
    l = Process.get(:len)
    if idx >= l do
      -1
    else
      a = Process.get(:a)
      b = Process.get(:b)
      val_adj = Process.get(idx)
      rem(val_adj * a + b, 1000000007)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \log MOD) where N is the total number of operations. The 'addAll', 'multAll', and 'getIndex' operations are O(1). The 'append' operation is O(\log MOD) due to the modular exponentiation required for finding the modular inverse. Given MOD is $10^9+7$, \log MOD is approximately 30.
- **Space Complexity:** O(N) to store the sequence of values in a dynamic array or list.
