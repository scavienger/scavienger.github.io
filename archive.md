---
layout: page
title: Archive
permalink: /archive/
---

{% assign all_posts = site.posts | concat: site.daily | sort: 'date' | reverse %}
{% assign posts_by_month = all_posts | group_by_exp: "post", "post.date | date: '%Y-%m'" %}
{% assign default_month = posts_by_month.first.name %}

<p class="page-lead">Select a month to browse solved challenges and filter by difficulty.</p>

<section class="editorial-controls archive-controls">
  <div class="controls-left">
    <div class="month-select-wrap">
      <select id="archive-month-filter" class="month-select" aria-label="Select year and month">
        {% for m in posts_by_month %}
          <option value="{{ m.name }}"{% if m.name == default_month %} selected{% endif %}>
            {{ m.name }} ({{ m.items | size }})
          </option>
        {% endfor %}
        <option value="all">All Months ({{ all_posts | size }})</option>
      </select>
    </div>

    <div class="filter-pills" role="group" aria-label="Filter by difficulty">
      <button type="button" class="filter-pill active" data-difficulty="all">All</button>
      <button type="button" class="filter-pill" data-difficulty="easy">Easy</button>
      <button type="button" class="filter-pill" data-difficulty="medium">Medium</button>
      <button type="button" class="filter-pill" data-difficulty="hard">Hard</button>
    </div>
  </div>

  <div class="search-box">
    <svg class="search-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <circle cx="11" cy="11" r="8"></circle>
      <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
    </svg>
    <input
      type="search"
      id="archive-search"
      class="search-input"
      placeholder="Search title or topic..."
      aria-label="Search archive by title or topic"
    />
  </div>
</section>

<ul class="editorial-post-list" id="archive-post-list">
{% for post in all_posts %}
  {% assign post_month = post.date | date: "%Y-%m" %}
  {% assign diff_lower = post.difficulty | default: 'unknown' | downcase %}
  {% assign tags_joined = post.tags | join: ',' | downcase %}
  <li
    class="editorial-post-row"
    data-month="{{ post_month }}"
    data-difficulty="{{ diff_lower }}"
    data-title="{{ post.title | downcase | escape }}"
    data-tags="{{ tags_joined | escape }}"
    {% unless post_month == default_month %}style="display: none;"{% endunless %}
  >
    <a class="editorial-row-link" href="{{ post.url | relative_url }}">
      <time class="row-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
      <div class="row-main">
        <span class="row-title">{{ post.title | escape }}</span>
        {% if post.tags and post.tags.size > 0 %}
          <span class="row-tags">
            {% for tag in post.tags limit: 3 %}
              <span class="row-tag">{{ tag }}</span>
            {% endfor %}
          </span>
        {% endif %}
      </div>
      <div class="row-meta-right">
        {% if post.difficulty %}
          <span class="difficulty difficulty-{{ diff_lower }}">{{ post.difficulty }}</span>
        {% endif %}
        <span class="row-arrow" aria-hidden="true">→</span>
      </div>
    </a>
  </li>
{% endfor %}
</ul>

<div id="archive-no-results" class="no-results-message" style="display: none;">
  No matching challenges found.
</div>

<script>
(function () {
  var monthSelect = document.getElementById('archive-month-filter');
  var filterBtns = document.querySelectorAll('.archive-controls .filter-pill');
  var searchInput = document.getElementById('archive-search');
  var rows = Array.prototype.slice.call(document.querySelectorAll('#archive-post-list .editorial-post-row'));
  var emptyState = document.getElementById('archive-no-results');
  if (!rows.length) return;

  var activeDiff = 'all';

  function applyFilters() {
    var selectedMonth = monthSelect ? monthSelect.value : 'all';
    var query = (searchInput && searchInput.value || '').trim().toLowerCase();
    var visibleCount = 0;

    rows.forEach(function (row) {
      var monthMatch = selectedMonth === 'all' || row.getAttribute('data-month') === selectedMonth;
      var diffMatch = activeDiff === 'all' || row.getAttribute('data-difficulty') === activeDiff;
      var title = row.getAttribute('data-title') || '';
      var tags = row.getAttribute('data-tags') || '';
      var queryMatch = !query || title.indexOf(query) !== -1 || tags.indexOf(query) !== -1;

      var shouldShow = monthMatch && diffMatch && queryMatch;
      row.style.display = shouldShow ? '' : 'none';
      if (shouldShow) visibleCount++;
    });

    if (emptyState) {
      emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  if (monthSelect) {
    monthSelect.addEventListener('change', applyFilters);
  }

  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      activeDiff = btn.getAttribute('data-difficulty') || 'all';
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', applyFilters);
  }

  applyFilters();
})();
</script>
