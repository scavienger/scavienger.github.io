---
layout: page
title: Topics
permalink: /topics/
---

<p class="page-lead">Browse LeetCode problems organized by topic and algorithm tag.</p>

{% assign all_posts = site.posts | concat: site.daily | sort: 'date' | reverse %}
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

<div class="editorial-tag-cloud">
{% for tag in sorted_tags %}
  {% assign tag_posts = all_posts | where_exp: "post", "post.tags contains tag" %}
  <a href="#{{ tag | slugify }}" class="editorial-tag-chip">
    {{ tag }} <span class="tag-count">{{ tag_posts.size }}</span>
  </a>
{% endfor %}
</div>

{% for tag in sorted_tags %}
{% assign tag_posts = all_posts | where_exp: "post", "post.tags contains tag" %}
<section class="archive-year-section">
  <div class="section-heading-row">
    <h2 id="{{ tag | slugify }}" class="archive-year-heading">{{ tag }}</h2>
    <span class="section-count-badge">{{ tag_posts.size }}</span>
  </div>

  <ul class="editorial-post-list">
  {% for post in tag_posts %}
    <li class="editorial-post-row">
      <a class="editorial-row-link" href="{{ post.url | relative_url }}">
        <time class="row-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
        <div class="row-main">
          <span class="row-title">{{ post.title | escape }}</span>
        </div>
        <div class="row-meta-right">
          {% if post.difficulty %}
            <span class="difficulty difficulty-{{ post.difficulty | downcase }}">{{ post.difficulty }}</span>
          {% endif %}
          <span class="row-arrow" aria-hidden="true">→</span>
        </div>
      </a>
    </li>
  {% endfor %}
  </ul>
</section>
{% endfor %}

{% include dark-mode-toggle.html %}
