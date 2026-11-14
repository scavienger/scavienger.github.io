---
layout: page
title: Topics
permalink: /topics/
---

{::nomarkdown}
{% assign all_posts = site.posts | concat: site.daily | sort: 'date' | reverse %}
{% assign total_posts = all_posts | size %}
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

<p class="page-lead">Select a topic to view matching challenges and their share of the {{ total_posts }} total problems.</p>

<div class="editorial-tag-cloud" id="topic-cloud">
{% for tag in sorted_tags %}
  {% assign tag_posts = all_posts | where_exp: "post", "post.tags contains tag" %}
  <button
    type="button"
    class="editorial-tag-chip"
    data-tag="{{ tag | escape }}"
    data-slug="{{ tag | slugify }}"
    data-count="{{ tag_posts.size }}"
  >
    <span>{{ tag }}</span>
    <span class="tag-count">{{ tag_posts.size }}</span>
  </button>
{% endfor %}
</div>

<div id="topic-empty-state" class="topic-empty-state">
  Select any topic above to inspect its problems.
</div>

<section id="topic-results-section" class="topic-results-section" style="display: none;">
  <div class="topic-summary-card">
    <div class="topic-summary-top">
      <h2 id="selected-topic-title" class="topic-summary-title"></h2>
      <div class="topic-summary-metrics">
        <span id="selected-topic-ratio" class="topic-ratio-pill"></span>
        <span id="selected-topic-percent" class="topic-percent-text"></span>
      </div>
    </div>
    <div class="topic-progress-track" aria-hidden="true">
      <div id="selected-topic-bar" class="topic-progress-fill" style="width: 0%;"></div>
    </div>
  </div>

  <ul class="editorial-post-list" id="topic-post-list"></ul>
</section>

<script id="topics-posts-data" type="application/json">
[
{% for post in all_posts %}
  {
    "title": {{ post.title | jsonify }},
    "url": {{ post.url | relative_url | jsonify }},
    "date": {{ post.date | date: "%Y-%m-%d" | jsonify }},
    "difficulty": {{ post.difficulty | default: "" | jsonify }},
    "tags": {{ post.tags | default: empty | jsonify }}
  }{% unless forloop.last %},{% endunless %}
{% endfor %}
]
</script>

<script>
(function () {
  var dataEl = document.getElementById('topics-posts-data');
  if (!dataEl) return;
  var allPosts = JSON.parse(dataEl.textContent || '[]');
  var totalCount = allPosts.length;

  var buttons = Array.prototype.slice.call(document.querySelectorAll('#topic-cloud .editorial-tag-chip'));
  var emptyState = document.getElementById('topic-empty-state');
  var resultsSection = document.getElementById('topic-results-section');
  var titleEl = document.getElementById('selected-topic-title');
  var ratioEl = document.getElementById('selected-topic-ratio');
  var percentEl = document.getElementById('selected-topic-percent');
  var barEl = document.getElementById('selected-topic-bar');
  var listEl = document.getElementById('topic-post-list');

  var activeSlug = null;

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderTopic(btn) {
    var slug = btn.getAttribute('data-slug');
    var tagName = btn.getAttribute('data-tag');

    if (activeSlug === slug) {
      activeSlug = null;
      buttons.forEach(function (b) { b.classList.remove('active'); });
      resultsSection.style.display = 'none';
      emptyState.style.display = 'block';
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, '', window.location.pathname);
      }
      return;
    }

    activeSlug = slug;
    buttons.forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-slug') === slug);
    });

    var matched = allPosts.filter(function (p) {
      return Array.isArray(p.tags) && p.tags.indexOf(tagName) !== -1;
    });

    var pct = totalCount > 0 ? ((matched.length / totalCount) * 100).toFixed(1) : '0.0';
    titleEl.textContent = tagName;
    ratioEl.textContent = matched.length + ' / ' + totalCount + ' problems';
    percentEl.textContent = pct + '%';
    barEl.style.width = pct + '%';

    listEl.innerHTML = matched.map(function (p) {
      var diffLower = (p.difficulty || '').toLowerCase();
      var diffBadge = p.difficulty
        ? '<span class="difficulty difficulty-' + escapeHtml(diffLower) + '">' + escapeHtml(p.difficulty) + '</span>'
        : '';
      return (
        '<li class="editorial-post-row">' +
          '<a class="editorial-row-link" href="' + escapeHtml(p.url) + '">' +
            '<time class="row-date">' + escapeHtml(p.date) + '</time>' +
            '<div class="row-main"><span class="row-title">' + escapeHtml(p.title) + '</span></div>' +
            '<div class="row-meta-right">' + diffBadge + '<span class="row-arrow" aria-hidden="true">→</span></div>' +
          '</a>' +
        '</li>'
      );
    }).join('');

    emptyState.style.display = 'none';
    resultsSection.style.display = 'block';

    if (window.history && window.history.replaceState) {
      window.history.replaceState(null, '', '#' + slug);
    }
  }

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      renderTopic(btn);
    });
  });

  if (window.location.hash) {
    var initialSlug = window.location.hash.slice(1);
    var targetBtn = buttons.find(function (b) { return b.getAttribute('data-slug') === initialSlug; });
    if (targetBtn) {
      renderTopic(targetBtn);
    }
  }
})();
</script>
{:/nomarkdown}
