# 🚀 LeetCode Solutions

Welcome! This repository features my solutions to various algorithmic problems from the **LeetCode** platform. It serves as a personal archive for practicing data structures, refining logic, and preparing for technical interviews.

---

## 🛠️ Language Selection

All problems are solved using **Python**. This language was chosen for its conciseness and clean readability, allowing me to completely focus on the core logic of the algorithms rather than getting distracted by complex syntax.

---

## 📋 Repository Content

### 🟨 45. Jump Game II
* **Solution Folder:** [`45-Jump-game-II`](./Python-variant-11/45-Jump-game-II/)
* **Difficulty:** Medium

> **Problem Summary:** 
> We are given an array of integers where each number represents the maximum jump length you can make from that specific position. The goal is to reach the very end of the array in the minimum number of jumps.

* **Solution Logic:** 
  This is solved using a greedy approach (*Greedy Algorithm*). At each step, we calculate which next available position will yield the farthest possible jump forward, and we select it. This allows us to determine the optimal path in just a single pass through the array.

---

### 🟩 121. Best Time to Buy and Sell Stock
* **Solution Folder:** [`121-Best-time-to-buy-and-sell-stock`](./Python-variant-11/121-Best-time-to-buy-and-sell-stock/)
* **Difficulty:** Easy

> **Problem Summary:** 
> A classic problem simulating stock market trading. Given an array of daily stock prices, we need to choose a single day to buy one stock and a different day in the future to sell that stock to maximize the total net profit.

* **Solution Logic:** 
  The problem is solved in a single pass through the prices array. We keep track of the lowest price observed so far, compare the current price with this minimum to calculate potential gains, and continuously update the maximum profit record on the fly.

---

### 🟩 1309. Decrypt String from Alphabet to Integer Mapping
* **Solution Folder:** [`1309-Decrypt-string-from-aplhabet-to-integer`](./Python-variant-11/1309-Decrypt-string-from-aplhabet-to-integer/)
* **Difficulty:** Easy

> **Problem Summary:** 
> We are given an encrypted string consisting of digits and hash characters (`#`). Characters `a` through `i` are mapped to digits `1` through `9` respectively. Characters `j` through `z` are mapped to two-digit numbers with a trailing hash symbol (e.g., `10#` to `26#`). The goal is to decrypt the string back into regular lowercase text.

* **Solution Logic:** 
  The easiest way to avoid confusion between single-digit and double-digit mappings is to read the string backwards from end to start. If we encounter a hash symbol (`#`), we extract the two digits preceding it and convert them into the corresponding letter; if there is no hash symbol, we simply process a single digit.
