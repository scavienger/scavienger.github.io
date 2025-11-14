---
layout: page
title: Archive
permalink: /archive/
---

# All Problems

Browse all LeetCode Daily Challenge problems solved on this blog.

{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}

{% for year in posts_by_year %}
## {{ year.name }}

{% assign posts_by_month = year.items | group_by_exp: "post", "post.date | date: '%B'" %}
{% for month in posts_by_month %}
### {{ month.name }}

<ul class="post-list">
{% for post in month.items %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d" }}</span>
    {% if post.difficulty %}
      <span class="difficulty difficulty-{{ post.difficulty | downcase }}">{{ post.difficulty }}</span>
    {% endif %}
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
{% endfor %}
{% endfor %}

<style>
  .post-list {
    list-style: none;
    padding-left: 0;
  }

  .post-list li {
    margin-bottom: 10px;
    padding: 10px;
    border-left: 3px solid #e8e8e8;
  }

  .post-meta {
    color: #828282;
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
</style>
