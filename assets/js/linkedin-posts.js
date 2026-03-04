// Social post card expand/collapse logic
// Works on rendered HTML content (markdownify output), not raw character count.
// Falls back gracefully when JS is disabled — full content remains visible.

(function () {
  var MAX_HEIGHT = 220; // px — collapsed height

  function initCard(card) {
    if (!card) return;

    var contentEl = card.querySelector('[data-linkedin-content]');
    if (!contentEl) return;

    var toggleBtn = card.querySelector('[data-linkedin-toggle]');
    if (!toggleBtn) return;

    // Measure natural height
    var fullHeight = contentEl.scrollHeight;
    if (fullHeight <= MAX_HEIGHT) return;

    // Collapse
    contentEl.style.maxHeight = MAX_HEIGHT + 'px';
    contentEl.style.overflow = 'hidden';
    contentEl.style.maskImage = 'linear-gradient(to bottom, black 60%, transparent 100%)';
    contentEl.style.webkitMaskImage = 'linear-gradient(to bottom, black 60%, transparent 100%)';

    toggleBtn.style.display = 'inline-block';
    toggleBtn.textContent = 'Read more';
    toggleBtn.setAttribute('aria-expanded', 'false');
    toggleBtn.setAttribute('aria-label', 'Read more of this post');

    toggleBtn.addEventListener('click', function () {
      var expanded = toggleBtn.getAttribute('aria-expanded') === 'true';

      if (expanded) {
        contentEl.style.maxHeight = MAX_HEIGHT + 'px';
        contentEl.style.maskImage = 'linear-gradient(to bottom, black 60%, transparent 100%)';
        contentEl.style.webkitMaskImage = 'linear-gradient(to bottom, black 60%, transparent 100%)';
        toggleBtn.textContent = 'Read more';
        toggleBtn.setAttribute('aria-expanded', 'false');
        toggleBtn.setAttribute('aria-label', 'Read more of this post');
      } else {
        contentEl.style.maxHeight = fullHeight + 'px';
        contentEl.style.maskImage = 'none';
        contentEl.style.webkitMaskImage = 'none';
        toggleBtn.textContent = 'Show less';
        toggleBtn.setAttribute('aria-expanded', 'true');
        toggleBtn.setAttribute('aria-label', 'Show less of this post');
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var cards = document.querySelectorAll('[data-linkedin-card]');
    for (var i = 0; i < cards.length; i++) {
      initCard(cards[i]);
    }
  });
})();
