(function() {
  'use strict';

  const STORAGE_KEY = 'preferred-code-language';

  // Initialize all code tabs on the page
  function initCodeTabs() {
    const codeTabContainers = document.querySelectorAll('.code-tabs');

    codeTabContainers.forEach(container => {
      // Save language preference when user clicks a tab
      const labels = container.querySelectorAll('.tab-labels label');
      labels.forEach(label => {
        label.addEventListener('click', function() {
          const languageId = label.getAttribute('for');
          if (languageId) {
            const langKey = languageId.replace(/^lang-/, '').replace(/-\d+$/, '');
            localStorage.setItem(STORAGE_KEY, langKey);
          }
        });
      });
    });

    // Load user's preferred language
    loadPreferredLanguage();
  }

  // Load user's preferred language from localStorage
  function loadPreferredLanguage() {
    const preferredLang = localStorage.getItem(STORAGE_KEY);
    if (!preferredLang) return;

    // Find and activate radio button for preferred language
    const radioButtons = document.querySelectorAll(`input[id^="lang-${preferredLang}"]`);
    if (radioButtons.length > 0) {
      // Activate the first matching radio button (handles both suffixed and non-suffixed IDs)
      radioButtons[0].checked = true;
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCodeTabs);
  } else {
    initCodeTabs();
  }
})();
