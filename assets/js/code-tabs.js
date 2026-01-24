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

    // Hide non-Gemini AI solution cards in the UI
    filterAiSolutions();

    // Fit AI solution headers to a single line
    fitAiSolutionHeaders();
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

  function filterAiSolutions() {
    const cards = Array.from(document.querySelectorAll('.ai-solution-card'));
    if (cards.length === 0) return;

    const isGeminiCard = (card) => {
      const badge = card.querySelector('.ai-model-badge');
      const text = (badge ? badge.textContent : card.textContent || '').toLowerCase();
      return text.includes('gemini');
    };

    const geminiCards = cards.filter(isGeminiCard);
    const hideNonGemini = true;

    cards.forEach(card => {
      const isGemini = isGeminiCard(card);
      if (hideNonGemini && !isGemini) {
        card.style.display = 'none';
      }
      if (!geminiCards.length) {
        card.style.display = 'none';
      }
    });

    const separators = document.querySelectorAll('.ai-solution-separator, hr.ai-solution-separator');
    separators.forEach(sep => {
      const prev = sep.previousElementSibling;
      const next = sep.nextElementSibling;
      const prevHidden = prev && prev.classList && prev.classList.contains('ai-solution-card') && prev.style.display === 'none';
      const nextHidden = next && next.classList && next.classList.contains('ai-solution-card') && next.style.display === 'none';
      if (prevHidden || nextHidden) {
        sep.style.display = 'none';
      }
    });
  }

  function fitAiSolutionHeaders() {
    const targets = Array.from(document.querySelectorAll('h2, h3'))
      .filter(el => (el.textContent || '').toLowerCase().includes('ai-generated solution'));
    if (!targets.length) return;

    targets.forEach(el => {
      if (!el.dataset.originalFontSize) {
        const computed = window.getComputedStyle(el);
        el.dataset.originalFontSize = computed.fontSize;
      }
      el.style.whiteSpace = 'nowrap';
      el.style.overflow = 'hidden';
      el.style.textOverflow = 'clip';
      const minSize = 12;
      let size = parseFloat(el.dataset.originalFontSize);
      el.style.fontSize = `${size}px`;

      while (el.scrollWidth > el.clientWidth && size > minSize) {
        size -= 0.5;
        el.style.fontSize = `${size}px`;
      }
    });
  }

  let resizeTimer = null;
  window.addEventListener('resize', () => {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(() => {
      fitAiSolutionHeaders();
    }, 120);
  });

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCodeTabs);
  } else {
    initCodeTabs();
  }
})();
