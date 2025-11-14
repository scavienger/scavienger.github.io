---
layout: page
title: By Difficulty
permalink: /difficulties/
---

# Problems by Difficulty

Browse LeetCode problems organized by difficulty level.

---

## Easy

{% assign easy_posts = site.posts | where: "difficulty", "Easy" %}
{% if easy_posts.size > 0 %}
<ul class="post-list">
{% for post in easy_posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% if post.tags and post.tags.size > 0 %}
      <div class="tags">
        {% for tag in post.tags limit:3 %}
          <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
    {% endif %}
  </li>
{% endfor %}
</ul>
<p class="count">Total: {{ easy_posts.size }} problems</p>
{% else %}
<p class="no-posts">No Easy problems yet.</p>
{% endif %}

---

## Medium

{% assign medium_posts = site.posts | where: "difficulty", "Medium" %}
{% if medium_posts.size > 0 %}
<ul class="post-list">
{% for post in medium_posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% if post.tags and post.tags.size > 0 %}
      <div class="tags">
        {% for tag in post.tags limit:3 %}
          <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
    {% endif %}
  </li>
{% endfor %}
</ul>
<p class="count">Total: {{ medium_posts.size }} problems</p>
{% else %}
<p class="no-posts">No Medium problems yet.</p>
{% endif %}

---

## Hard

{% assign hard_posts = site.posts | where: "difficulty", "Hard" %}
{% if hard_posts.size > 0 %}
<ul class="post-list">
{% for post in hard_posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% if post.tags and post.tags.size > 0 %}
      <div class="tags">
        {% for tag in post.tags limit:3 %}
          <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
    {% endif %}
  </li>
{% endfor %}
</ul>
<p class="count">Total: {{ hard_posts.size }} problems</p>
{% else %}
<p class="no-posts">No Hard problems yet.</p>
{% endif %}

<style>
  .post-list {
    list-style: none;
    padding-left: 0;
  }

  .post-list li {
    margin-bottom: 15px;
    padding: 15px;
    background-color: #f8f9fa;
    border-radius: 5px;
  }

  .post-meta {
    color: #666;
    font-size: 14px;
    margin-right: 10px;
  }

  .post-link {
    font-weight: 500;
    font-size: 16px;
  }

  .tags {
    margin-top: 8px;
  }

  .tag {
    display: inline-block;
    background-color: #e0e0e0;
    padding: 3px 8px;
    margin-right: 5px;
    border-radius: 3px;
    font-size: 12px;
    color: #333;
  }

  .count {
    font-weight: bold;
    color: #555;
    margin-top: 10px;
  }

  .no-posts {
    color: #999;
    font-style: italic;
  }
</style>
