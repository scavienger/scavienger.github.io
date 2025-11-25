---
layout: page
title: Topics
permalink: /topics/
---

# Problems by Topic

Browse LeetCode problems organized by topic/tag.

{% assign all_posts = site.posts | concat: site.daily %}
{% assign all_tags = "" | split: "" %}
{% for post in all_posts %}
  {% if post.tags %}
    {% for tag in post.tags %}
      {% unless all_tags contains tag %}
        {% assign all_tags = all_tags | push: tag %}
      {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign sorted_tags = all_tags | sort %}

<div class="tag-cloud">
{% for tag in sorted_tags %}
  {% assign tag_posts = all_posts | where_exp: "post", "post.tags contains tag" %}
  <a href="#{{ tag | slugify }}" class="tag-link">
    {{ tag }} <span class="tag-count">({{ tag_posts.size }})</span>
  </a>
{% endfor %}
</div>

---

{% for tag in sorted_tags %}
{% assign tag_posts = all_posts | where_exp: "post", "post.tags contains tag" %}

<h2 id="{{ tag | slugify }}">{{ tag }}</h2>

<ul class="post-list">
{% for post in tag_posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    {% if post.difficulty %}
      <span class="difficulty difficulty-{{ post.difficulty | downcase }}">{{ post.difficulty }}</span>
    {% endif %}
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>

{% endfor %}

<style>
  .tag-cloud {
    margin: 20px 0;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 5px;
  }

  .tag-link {
    display: inline-block;
    margin: 5px;
    padding: 8px 12px;
    background-color: #007bff;
    color: white !important;
    text-decoration: none;
    border-radius: 3px;
    font-size: 14px;
    transition: background-color 0.3s;
  }

  .tag-link:hover {
    background-color: #0056b3;
  }

  .tag-count {
    font-size: 12px;
    opacity: 0.8;
  }

  .post-list {
    list-style: none;
    padding-left: 0;
    margin-bottom: 40px;
  }

  .post-list li {
    margin-bottom: 10px;
    padding: 12px;
    border-left: 3px solid #007bff;
    background-color: #f8f9fa;
  }

  .post-meta {
    color: #666;
    font-size: 14px;
    margin-right: 10px;
  }

  .difficulty {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 3px;
    font-size: 12px;
    font-weight: bold;
    margin-right: 10px;
  }

  .difficulty-easy {
    background-color: #d4edda;
    color: #155724;
  }

  .difficulty-medium {
    background-color: #fff3cd;
    color: #856404;
  }

  .difficulty-hard {
    background-color: #f8d7da;
    color: #721c24;
  }

  .post-link {
    font-weight: 500;
  }

  h2 {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 2px solid #e8e8e8;
  }

  h2:first-of-type {
    margin-top: 0;
    padding-top: 0;
    border-top: none;
  }
</style>
