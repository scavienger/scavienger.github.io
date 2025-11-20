(function() {
  'use strict';

  const STORAGE_KEY = 'theme-preference';
  const DARK_MODE_CLASS = 'dark-mode';
  const LIGHT_MODE_CLASS = 'light-mode';

  // Get initial theme from localStorage or system preference
  function getInitialTheme() {
    const savedTheme = localStorage.getItem(STORAGE_KEY);
    if (savedTheme) {
      return savedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  // Apply theme to body
  function applyTheme(theme) {
    document.body.classList.remove(DARK_MODE_CLASS, LIGHT_MODE_CLASS);
    if (theme === 'dark') {
      document.body.classList.add(DARK_MODE_CLASS);
    } else {
      document.body.classList.add(LIGHT_MODE_CLASS);
    }
  }

  // Toggle theme
  function toggleTheme() {
    const currentTheme = localStorage.getItem(STORAGE_KEY) || getInitialTheme();
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    localStorage.setItem(STORAGE_KEY, newTheme);
    applyTheme(newTheme);
  }

  // Apply theme on page load (before DOMContentLoaded for no flash)
  const initialTheme = getInitialTheme();
  applyTheme(initialTheme);

  // Set up toggle button when DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('dark-mode-toggle');
    if (toggleButton) {
      toggleButton.addEventListener('click', toggleTheme);
    }
  });

  // Listen for system theme changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
    // Only apply system theme if user hasn't set a preference
    if (!localStorage.getItem(STORAGE_KEY)) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });
})();
