---
layout: page
title: Calendar
permalink: /calendar/
---

{::nomarkdown}
{% assign all_posts = site.posts | concat: site.daily | sort: 'date' | reverse %}
{% assign posts_by_year = all_posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% assign default_year = posts_by_year.first.name %}

<p class="page-lead">Visual activity heatmap by year and difficulty. Click any cell to open that day's solution.</p>

<div class="calendar-toolbar">
  <div class="calendar-year-tabs" id="calendar-year-tabs">
    {% for yr in posts_by_year %}
      <button type="button" class="filter-pill{% if yr.name == default_year %} active{% endif %}" data-year="{{ yr.name }}">
        {{ yr.name }} ({{ yr.items | size }})
      </button>
    {% endfor %}
  </div>

  <div class="calendar-legend" aria-label="Difficulty legend">
    <span class="legend-item"><span class="cal-cell level-none"></span>None</span>
    <span class="legend-item"><span class="cal-cell level-easy"></span>Easy</span>
    <span class="legend-item"><span class="cal-cell level-medium"></span>Medium</span>
    <span class="legend-item"><span class="cal-cell level-hard"></span>Hard</span>
  </div>
</div>

<div class="calendar-stats-strip" id="calendar-stats-strip"></div>

<div class="calendar-heatmap-card">
  <div class="calendar-months-row" id="calendar-months-row"></div>
  <div class="calendar-grid-wrap">
    <div class="calendar-weekdays" aria-hidden="true">
      <span></span>
      <span>Mon</span>
      <span></span>
      <span>Wed</span>
      <span></span>
      <span>Fri</span>
      <span></span>
    </div>
    <div class="calendar-grid" id="calendar-grid"></div>
  </div>
</div>

<div id="calendar-tooltip" class="calendar-tooltip" role="status" aria-live="polite" style="display: none;"></div>

<script id="calendar-posts-data" type="application/json">
[
{% for post in all_posts %}
  {
    "title": {{ post.title | jsonify }},
    "url": {{ post.url | relative_url | jsonify }},
    "date": {{ post.date | date: "%Y-%m-%d" | jsonify }},
    "difficulty": {{ post.difficulty | default: "" | jsonify }}
  }{% unless forloop.last %},{% endunless %}
{% endfor %}
]
</script>

<script>
(function () {
  var dataEl = document.getElementById('calendar-posts-data');
  if (!dataEl) return;
  var posts = JSON.parse(dataEl.textContent || '[]');

  var byDate = {};
  posts.forEach(function (p) {
    if (p.date) byDate[p.date] = p;
  });

  var yearTabs = Array.prototype.slice.call(document.querySelectorAll('#calendar-year-tabs .filter-pill'));
  var gridEl = document.getElementById('calendar-grid');
  var monthsEl = document.getElementById('calendar-months-row');
  var statsEl = document.getElementById('calendar-stats-strip');
  var tooltipEl = document.getElementById('calendar-tooltip');

  function pad2(n) {
    return n < 10 ? '0' + n : String(n);
  }

  function formatDateUTC(dt) {
    return dt.getUTCFullYear() + '-' + pad2(dt.getUTCMonth() + 1) + '-' + pad2(dt.getUTCDate());
  }

  function renderYear(yearNum) {
    var jan1 = new Date(Date.UTC(yearNum, 0, 1));
    var dec31 = new Date(Date.UTC(yearNum, 11, 31));
    var start = new Date(jan1.getTime());
    start.setUTCDate(start.getUTCDate() - start.getUTCDay());

    var end = new Date(dec31.getTime());
    end.setUTCDate(end.getUTCDate() + (6 - end.getUTCDay()));

    var monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var weeksHtml = [];
    var monthLabels = [];
    var lastMonth = -1;

    var totalYear = 0;
    var easyCount = 0;
    var medCount = 0;
    var hardCount = 0;

    var cur = new Date(start.getTime());
    var weekIdx = 0;
    while (cur <= end) {
      var cellsHtml = [];
      var weekMonth = -1;
      for (var d = 0; d < 7; d++) {
        var inYear = cur.getUTCFullYear() === yearNum;
        var iso = formatDateUTC(cur);
        if (inYear && weekMonth === -1 && cur.getUTCDate() <= 7) {
          weekMonth = cur.getUTCMonth();
        }
        if (!inYear) {
          cellsHtml.push('<span class="cal-cell is-outside"></span>');
        } else {
          var post = byDate[iso];
          if (post) {
            totalYear++;
            var diff = (post.difficulty || '').toLowerCase();
            if (diff === 'easy') easyCount++;
            else if (diff === 'medium') medCount++;
            else if (diff === 'hard') hardCount++;
            var levelClass = diff ? 'level-' + diff : 'level-easy';
            cellsHtml.push(
              '<a class="cal-cell ' + levelClass + '" href="' + post.url + '" ' +
              'data-date="' + iso + '" data-title="' + post.title.replace(/"/g, '&quot;') + '" data-diff="' + (post.difficulty || '') + '" ' +
              'aria-label="' + iso + ': ' + post.title.replace(/"/g, '&quot;') + '"></a>'
            );
          } else {
            cellsHtml.push('<span class="cal-cell level-none" data-date="' + iso + '"></span>');
          }
        }
        cur.setUTCDate(cur.getUTCDate() + 1);
      }

      if (weekMonth !== -1 && weekMonth !== lastMonth) {
        monthLabels.push({ week: weekIdx, label: monthNames[weekMonth] });
        lastMonth = weekMonth;
      }

      weeksHtml.push('<div class="calendar-week">' + cellsHtml.join('') + '</div>');
      weekIdx++;
    }

    gridEl.innerHTML = weeksHtml.join('');

    monthsEl.innerHTML = '';
    monthLabels.forEach(function (m) {
      var span = document.createElement('span');
      span.className = 'calendar-month-label';
      span.textContent = m.label;
      span.style.left = (m.week * 15 + 34) + 'px';
      monthsEl.appendChild(span);
    });

    statsEl.innerHTML =
      '<span><strong>' + totalYear + '</strong> solved in ' + yearNum + '</span>' +
      '<span class="stat-divider">·</span>' +
      '<span class="stat-easy-txt">' + easyCount + ' Easy</span>' +
      '<span class="stat-divider">·</span>' +
      '<span class="stat-medium-txt">' + medCount + ' Medium</span>' +
      '<span class="stat-divider">·</span>' +
      '<span class="stat-hard-txt">' + hardCount + ' Hard</span>';
  }

  gridEl.addEventListener('mouseover', function (e) {
    var cell = e.target.closest('.cal-cell');
    if (!cell || cell.classList.contains('is-outside')) return;
    var date = cell.getAttribute('data-date');
    var title = cell.getAttribute('data-title');
    var diff = cell.getAttribute('data-diff');
    if (!date) return;

    tooltipEl.textContent = title ? (date + ' · ' + title + (diff ? ' (' + diff + ')' : '')) : (date + ' · No post');
    tooltipEl.style.display = 'block';
    var rect = cell.getBoundingClientRect();
    tooltipEl.style.left = Math.min(window.innerWidth - 260, Math.max(12, rect.left)) + 'px';
    tooltipEl.style.top = (rect.top - 36) + 'px';
  });

  gridEl.addEventListener('mouseout', function (e) {
    if (e.target.closest('.cal-cell')) {
      tooltipEl.style.display = 'none';
    }
  });

  yearTabs.forEach(function (btn) {
    btn.addEventListener('click', function () {
      yearTabs.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      renderYear(parseInt(btn.getAttribute('data-year'), 10));
    });
  });

  if (yearTabs.length > 0) {
    renderYear(parseInt(yearTabs[0].getAttribute('data-year'), 10));
  }
})();
</script>
{:/nomarkdown}
