(function () {
  'use strict';

  var cachedPosts = null;
  var fetchPromise = null;
  var activeIndex = -1;
  var currentMatches = [];

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function getModal() {
    return document.getElementById('search-palette-modal');
  }

  function loadPosts(modal) {
    if (cachedPosts) return Promise.resolve(cachedPosts);
    if (fetchPromise) return fetchPromise;

    var url = (modal && modal.getAttribute('data-search-url')) || '/search.json';
    fetchPromise = fetch(url)
      .then(function (res) {
        if (!res.ok) throw new Error('Failed to load search index');
        return res.json();
      })
      .then(function (data) {
        cachedPosts = Array.isArray(data) ? data : [];
        return cachedPosts;
      })
      .catch(function () {
        fetchPromise = null;
        return [];
      });
    return fetchPromise;
  }

  function renderResults(query) {
    var resultsEl = document.getElementById('search-palette-results');
    if (!resultsEl) return;

    if (!cachedPosts) {
      resultsEl.innerHTML = '<div class="search-palette-empty">Loading problems...</div>';
      return;
    }

    var q = (query || '').trim().toLowerCase();
    var matches;
    if (!q) {
      matches = cachedPosts.slice(0, 8);
    } else {
      matches = cachedPosts.filter(function (item) {
        var title = (item.title || '').toLowerCase();
        var diff = (item.difficulty || '').toLowerCase();
        var date = (item.date || '').toLowerCase();
        var tags = Array.isArray(item.tags) ? item.tags.join(' ').toLowerCase() : '';
        return title.indexOf(q) !== -1 || tags.indexOf(q) !== -1 || diff.indexOf(q) !== -1 || date.indexOf(q) !== -1;
      }).slice(0, 15);
    }

    currentMatches = matches;
    activeIndex = matches.length > 0 ? 0 : -1;

    if (matches.length === 0) {
      resultsEl.innerHTML = '<div class="search-palette-empty">No matching challenges found.</div>';
      return;
    }

    resultsEl.innerHTML = matches.map(function (item, idx) {
      var diffLower = (item.difficulty || '').toLowerCase();
      var tagsHtml = Array.isArray(item.tags) && item.tags.length > 0
        ? '<span class="search-result-tags">' + item.tags.slice(0, 3).map(escapeHtml).join(' · ') + '</span>'
        : '';
      var diffHtml = item.difficulty
        ? '<span class="difficulty difficulty-' + escapeHtml(diffLower) + '">' + escapeHtml(item.difficulty) + '</span>'
        : '';
      return (
        '<a href="' + escapeHtml(item.url) + '" class="search-palette-item' + (idx === 0 ? ' is-selected' : '') + '" data-index="' + idx + '">' +
          '<div class="search-result-main">' +
            '<span class="search-result-date">' + escapeHtml(item.date) + '</span>' +
            '<span class="search-result-title">' + escapeHtml(item.title) + '</span>' +
            tagsHtml +
          '</div>' +
          '<div class="search-result-right">' + diffHtml + '</div>' +
        '</a>'
      );
    }).join('');
  }

  function updateActiveItem(nextIndex) {
    var resultsEl = document.getElementById('search-palette-results');
    if (!resultsEl || currentMatches.length === 0) return;

    if (nextIndex < 0) nextIndex = currentMatches.length - 1;
    if (nextIndex >= currentMatches.length) nextIndex = 0;
    activeIndex = nextIndex;

    var items = resultsEl.querySelectorAll('.search-palette-item');
    items.forEach(function (el, idx) {
      el.classList.toggle('is-selected', idx === activeIndex);
    });

    if (items[activeIndex]) {
      items[activeIndex].scrollIntoView({ block: 'nearest' });
    }
  }

  function openPalette() {
    var modal = getModal();
    if (!modal) return;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('search-palette-open');

    var input = document.getElementById('search-palette-input');
    if (input) {
      input.value = '';
      setTimeout(function () { input.focus(); }, 10);
    }

    loadPosts(modal).then(function () {
      renderResults(input ? input.value : '');
    });
  }

  function closePalette() {
    var modal = getModal();
    if (!modal) return;
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('search-palette-open');
  }

  function isEditableTarget(target) {
    if (!target) return false;
    var tag = target.tagName;
    return tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || target.isContentEditable;
  }

  document.addEventListener('keydown', function (e) {
    var modal = getModal();
    var isOpen = modal && modal.classList.contains('is-open');

    if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) {
      e.preventDefault();
      if (isOpen) {
        closePalette();
      } else {
        openPalette();
      }
      return;
    }

    if (!isOpen && e.key === '/' && !isEditableTarget(e.target)) {
      e.preventDefault();
      openPalette();
      return;
    }

    if (!isOpen) return;

    if (e.key === 'Escape') {
      e.preventDefault();
      closePalette();
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      updateActiveItem(activeIndex + 1);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      updateActiveItem(activeIndex - 1);
    } else if (e.key === 'Enter' && activeIndex >= 0 && currentMatches[activeIndex]) {
      e.preventDefault();
      window.location.href = currentMatches[activeIndex].url;
    }
  });

  document.addEventListener('click', function (e) {
    if (e.target.closest('#search-palette-trigger')) {
      e.preventDefault();
      openPalette();
      return;
    }
    if (e.target.closest('[data-search-close]')) {
      e.preventDefault();
      closePalette();
    }
  });

  document.addEventListener('input', function (e) {
    if (e.target && e.target.id === 'search-palette-input') {
      renderResults(e.target.value);
    }
  });

  window.openSearchPalette = openPalette;
  window.closeSearchPalette = closePalette;
})();
