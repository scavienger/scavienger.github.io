---
layout: page
title: By Difficulty
permalink: /difficulties/
---

<p class="page-lead">Browse LeetCode problems organized by difficulty level.</p>

{% assign all_posts = site.posts | concat: site.daily | sort: 'date' | reverse %}

{% assign levels = "Easy,Medium,Hard" | split: "," %}
{% for level in levels %}
  {% assign level_posts = all_posts | where: "difficulty", level %}
  <section class="archive-year-section">
    <div class="section-heading-row">
      <h2 class="archive-year-heading">{{ level }}</h2>
      <span class="section-count-badge">{{ level_posts.size }} problems</span>
    </div>

    {% if level_posts.size > 0 %}
    <ul class="editorial-post-list">
      {% for post in level_posts %}
      <li class="editorial-post-row">
        <a class="editorial-row-link" href="{{ post.url | relative_url }}">
          <time class="row-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
          <div class="row-main">
            <span class="row-title">{{ post.title | escape }}</span>
            {% if post.tags and post.tags.size > 0 %}
            <span class="row-tags">
              {% for tag in post.tags limit:3 %}
                <span class="row-tag">{{ tag }}</span>
              {% endfor %}
            </span>
            {% endif %}
          </div>
          <div class="row-meta-right">
            <span class="difficulty difficulty-{{ level | downcase }}">{{ level }}</span>
            <span class="row-arrow" aria-hidden="true">→</span>
          </div>
        </a>
      </li>
      {% endfor %}
    </ul>
    {% else %}
    <p class="no-posts">No {{ level }} problems yet.</p>
    {% endif %}
  </section>
{% endfor %}

{% include dark-mode-toggle.html %}
