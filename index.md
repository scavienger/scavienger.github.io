---
layout: home
title: Home
---

# LeetCode Daily Challenge

Welcome to my automated LeetCode Daily Challenge blog!

Every day at 9:00 AM KST, this blog automatically fetches and posts the latest LeetCode Daily Question along with its solution.

## Statistics

{% assign easy_count = site.posts | where: "difficulty", "Easy" | size %}
{% assign medium_count = site.posts | where: "difficulty", "Medium" | size %}
{% assign hard_count = site.posts | where: "difficulty", "Hard" | size %}
{% assign total_count = site.posts | size %}

<div class="stats-container">
  <div class="stat-card">
    <div class="stat-number">{{ total_count }}</div>
    <div class="stat-label">Total Problems</div>
  </div>
  <div class="stat-card easy">
    <div class="stat-number">{{ easy_count }}</div>
    <div class="stat-label">Easy</div>
  </div>
  <div class="stat-card medium">
    <div class="stat-number">{{ medium_count }}</div>
    <div class="stat-label">Medium</div>
  </div>
  <div class="stat-card hard">
    <div class="stat-number">{{ hard_count }}</div>
    <div class="stat-label">Hard</div>
  </div>
</div>

## Quick Navigation

<div class="quick-links">
  <a href="{{ '/archive/' | relative_url }}" class="quick-link">📚 All Problems</a>
  <a href="{{ '/difficulties/' | relative_url }}" class="quick-link">🎯 By Difficulty</a>
  <a href="{{ '/topics/' | relative_url }}" class="quick-link">🏷️ By Topic</a>
</div>

## Recent Posts

<style>
  .stats-container {
    display: flex;
    gap: 15px;
    margin: 30px 0;
    flex-wrap: wrap;
  }

  .stat-card {
    flex: 1;
    min-width: 120px;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 8px;
    text-align: center;
    border: 2px solid #e0e0e0;
  }

  .stat-card.easy {
    background-color: #d4edda;
    border-color: #c3e6cb;
  }

  .stat-card.medium {
    background-color: #fff3cd;
    border-color: #ffeaa7;
  }

  .stat-card.hard {
    background-color: #f8d7da;
    border-color: #f5c6cb;
  }

  .stat-number {
    font-size: 36px;
    font-weight: bold;
    color: #333;
  }

  .stat-label {
    font-size: 14px;
    color: #666;
    margin-top: 5px;
  }

  .quick-links {
    display: flex;
    gap: 15px;
    margin: 30px 0;
    flex-wrap: wrap;
  }

  .quick-link {
    flex: 1;
    min-width: 150px;
    padding: 15px 20px;
    background-color: #007bff;
    color: white !important;
    text-decoration: none;
    border-radius: 5px;
    text-align: center;
    font-weight: 500;
    transition: background-color 0.3s;
  }

  .quick-link:hover {
    background-color: #0056b3;
  }
</style>
