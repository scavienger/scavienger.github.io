/**
 * Code Copy Button Functionality
 * Adds "Copy" buttons to all code blocks
 */

(function () {
  'use strict';

  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    // Find all code blocks with syntax highlighting (inside .highlight class)
    // Skip plain <pre> tags used in problem descriptions
    const codeBlocks = document.querySelectorAll('.highlight pre');

    codeBlocks.forEach((pre) => {
      // Skip if already wrapped
      if (pre.parentElement.classList.contains('code-block-wrapper')) {
        return;
      }

      // Create wrapper
      const wrapper = document.createElement('div');
      wrapper.className = 'code-block-wrapper';

      // Create copy button
      const button = document.createElement('button');
      button.className = 'copy-code-btn';
      button.textContent = '📋 Copy';
      button.setAttribute('aria-label', 'Copy code to clipboard');

      // Insert wrapper before pre element
      pre.parentNode.insertBefore(wrapper, pre);

      // Move pre into wrapper and add button
      wrapper.appendChild(pre);
      wrapper.appendChild(button);

      // Add click event
      button.addEventListener('click', function () {
        copyCodeToClipboard(pre, button);
      });
    });
  }

  /**
   * Copy code content to clipboard
   * @param {HTMLElement} codeBlock - The code block element
   * @param {HTMLElement} button - The copy button element
   */
  function copyCodeToClipboard(codeBlock, button) {
    // Get the code element inside pre
    const codeElement = codeBlock.querySelector('code');
    const code = codeElement ? codeElement.textContent : codeBlock.textContent;

    // Use modern Clipboard API if available
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(code).then(
        () => showCopySuccess(button),
        () => fallbackCopy(code, button)
      );
    } else {
      fallbackCopy(code, button);
    }
  }

  /**
   * Fallback copy method using textarea
   * @param {string} text - Text to copy
   * @param {HTMLElement} button - The copy button element
   */
  function fallbackCopy(text, button) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.left = '-999999px';
    textarea.style.top = '-999999px';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();

    try {
      const successful = document.execCommand('copy');
      if (successful) {
        showCopySuccess(button);
      } else {
        showCopyError(button);
      }
    } catch (err) {
      console.error('Failed to copy code:', err);
      showCopyError(button);
    }

    document.body.removeChild(textarea);
  }

  /**
   * Show visual feedback for successful copy
   * @param {HTMLElement} button - The copy button element
   */
  function showCopySuccess(button) {
    const originalText = button.textContent;
    button.classList.add('copied');
    button.textContent = '✅ Copied';

    setTimeout(() => {
      button.classList.remove('copied');
      button.textContent = originalText;
    }, 2000);
  }

  /**
   * Show visual feedback for copy error
   * @param {HTMLElement} button - The copy button element
   */
  function showCopyError(button) {
    const originalText = button.textContent;
    button.textContent = 'Failed';
    button.style.backgroundColor = '#ef4444';
    button.style.borderColor = '#dc2626';

    setTimeout(() => {
      button.textContent = originalText;
      button.style.backgroundColor = '';
      button.style.borderColor = '';
    }, 2000);
  }

  // Re-initialize when content dynamically loaded (e.g., for SPAs)
  if (typeof MutationObserver !== 'undefined') {
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.addedNodes.length) {
          const hasCodeBlocks = Array.from(mutation.addedNodes).some(node =>
            node.nodeType === 1 && (node.tagName === 'PRE' || node.querySelector('pre'))
          );
          if (hasCodeBlocks) {
            init();
          }
        }
      });
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }
})();
