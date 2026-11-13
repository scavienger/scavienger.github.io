---
layout: page
title: Archive
permalink: /archive/
---

<p class="page-lead">Browse all LeetCode Daily Challenge problems solved on this blog.</p>

{% assign all_posts = site.posts | concat: site.daily | sort: 'date' | reverse %}
{% assign posts_by_year = all_posts | group_by_exp: "post", "post.date | date: '%Y'" %}

{% for year in posts_by_year %}
<section class="archive-year-section">
  <h2 class="archive-year-heading">{{ year.name }}</h2>

  {% assign posts_by_month = year.items | group_by_exp: "post", "post.date | date: '%B'" %}
  {% for month in posts_by_month %}
  <h3 class="archive-month-heading">{{ month.name }}</h3>

  <ul class="editorial-post-list">
  {% for post in month.items %}
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
  {% endfor %}
</section>
{% endfor %}

{% include dark-mode-toggle.html %}
