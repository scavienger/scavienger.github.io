(function () {
  'use strict';

  var SOLVED_KEY = 'leetcode-solved-urls';
  var BOOKMARK_KEY = 'leetcode-bookmarked-urls';

  function readSet(key) {
    try {
      var raw = localStorage.getItem(key);
      if (!raw) return new Set();
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? new Set(parsed) : new Set();
    } catch (e) {
      return new Set();
    }
  }

  function writeSet(key, set) {
    try {
      localStorage.setItem(key, JSON.stringify(Array.from(set)));
    } catch (e) {
      // Ignore storage quota / privacy mode errors
    }
  }

  function normalizeUrl(url) {
    if (!url) return '';
    return String(url).trim();
  }

  function dispatchChange() {
    document.dispatchEvent(new CustomEvent('leetcode:bookmarks-changed'));
  }

  function syncButton(btn, active, type) {
    btn.classList.toggle('is-active', active);
    btn.setAttribute('aria-pressed', active ? 'true' : 'false');

    var labelEl = btn.querySelector('.btn-label');
    if (labelEl) {
      if (type === 'solved') {
        labelEl.textContent = active ? 'Solved' : 'Mark Solved';
      } else {
        labelEl.textContent = active ? 'Bookmarked' : 'Bookmark';
      }
    }

    var iconEl = btn.querySelector('.btn-icon');
    if (iconEl && type === 'bookmark') {
      iconEl.textContent = active ? '★' : '☆';
    }
  }

  function syncAll() {
    var solved = readSet(SOLVED_KEY);
    var bookmarked = readSet(BOOKMARK_KEY);

    document.querySelectorAll('[data-solved-btn]').forEach(function (btn) {
      var url = normalizeUrl(btn.getAttribute('data-url'));
      syncButton(btn, solved.has(url), 'solved');
    });

    document.querySelectorAll('[data-bookmark-btn]').forEach(function (btn) {
      var url = normalizeUrl(btn.getAttribute('data-url'));
      syncButton(btn, bookmarked.has(url), 'bookmark');
    });
  }

  function toggleItem(key, url) {
    var normalized = normalizeUrl(url);
    if (!normalized) return false;
    var set = readSet(key);
    var nextState = !set.has(normalized);
    if (nextState) {
      set.add(normalized);
    } else {
      set.delete(normalized);
    }
    writeSet(key, set);
    syncAll();
    dispatchChange();
    return nextState;
  }

  document.addEventListener('click', function (e) {
    var solvedBtn = e.target.closest('[data-solved-btn]');
    if (solvedBtn) {
      e.preventDefault();
      e.stopPropagation();
      toggleItem(SOLVED_KEY, solvedBtn.getAttribute('data-url'));
      return;
    }

    var bookmarkBtn = e.target.closest('[data-bookmark-btn]');
    if (bookmarkBtn) {
      e.preventDefault();
      e.stopPropagation();
      toggleItem(BOOKMARK_KEY, bookmarkBtn.getAttribute('data-url'));
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', syncAll);
  } else {
    syncAll();
  }

  window.LeetCodeBookmarks = {
    getSolvedSet: function () { return readSet(SOLVED_KEY); },
    getBookmarkedSet: function () { return readSet(BOOKMARK_KEY); },
    isSolved: function (url) { return readSet(SOLVED_KEY).has(normalizeUrl(url)); },
    isBookmarked: function (url) { return readSet(BOOKMARK_KEY).has(normalizeUrl(url)); },
    toggleSolved: function (url) { return toggleItem(SOLVED_KEY, url); },
    toggleBookmarked: function (url) { return toggleItem(BOOKMARK_KEY, url); },
    syncAll: syncAll
  };
})();
