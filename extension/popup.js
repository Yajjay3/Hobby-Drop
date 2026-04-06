/**
 * Popup controller for Hobby Drop v3 — Accordion UI
 */
(() => {
  // ── DOM refs ──────────────────────────────────────────────────
  const setupScreen = document.getElementById('setup-screen');
  const factScreen = document.getElementById('fact-screen');
  const loading = document.getElementById('loading');
  const hobbyList = document.getElementById('hobby-list');
  const emojiStrip = document.getElementById('emoji-strip');
  const customizeEmojisBtn = document.getElementById('customize-emojis-btn');
  const premiumNote = document.getElementById('premium-note');
  const topReadyWrap = document.getElementById('top-ready-wrap');
  const readyBtn = document.getElementById('ready-btn');
  const selectionStatus = document.getElementById('selection-status');
  const selectionHeading = document.getElementById('selection-heading');
  const expandAllBtn = document.getElementById('expand-all-btn');
  const collapseAllBtn = document.getElementById('collapse-all-btn');

  const changeBtn = document.getElementById('change-btn');
  const refreshBtn = document.getElementById('refresh-btn');
  const premiumButtons = document.querySelectorAll('.premium-btn');

  const hobbyLabel = document.getElementById('hobby-label');
  const dateBadge = document.getElementById('date-badge');
  const factType = document.getElementById('fact-type');
  const factText = document.getElementById('fact-text');
  const factCredit = document.getElementById('fact-credit');
  const factSource = document.getElementById('fact-source');

  // ── Helpers ───────────────────────────────────────────────────
  const show = (el) => el.classList.remove('hidden');
  const hide = (el) => el.classList.add('hidden');

  const DEFAULT_TOP_EMOJIS = '🎬 🎵 🎸 🏆 📺 🎨 🎣 📚 🧙';
  const EXTPAY_EXTENSION_ID = 'hobby-drop';
  const PREMIUM_TEST_MODE = false;
  const extpay = typeof ExtPay === 'function' ? ExtPay(EXTPAY_EXTENSION_ID) : null;
  let selectedHobbies = [];
  let isPremiumMode = false;

  const isSelectedHobby = (hobbyId) =>
    selectedHobbies.some((item) => item.id === hobbyId);

  const openPremiumPage = async () => {
    if (!extpay) {
      window.alert('Premium checkout is temporarily unavailable. Please try again shortly.');
      return;
    }

    try {
      await extpay.openPaymentPage();
    } catch (error) {
      console.error('Unable to open ExtensionPay checkout:', error);
      window.alert('Unable to open the secure payment page right now. Please try again in a moment.');
    }
  };

  const showPremiumDetails = async (openCheckout = false) => {
    const message = 'Premium features ($1.99/month or $19.99/year):\n• Select as many hobbies as you like\n• Receive a new fact each day from one of your selected hobbies\n• Use links to learn more about the daily fact and hobby\n• Click Next Fact and move through selected category facts in minutes\n• Upload your own hobby emoji at the top to personalize your experience\n\nFree features:\n• Select one hobby\n• Receive a new fact a day for a year';

    if (!openCheckout) {
      window.alert(message);
      return;
    }

    const nextStep = isPremiumMode
      ? '\n\nYour premium account is active. Open the billing page to manage it?'
      : '\n\nOpen the secure payment page to upgrade now?';

    if (window.confirm(message + nextStep)) {
      await openPremiumPage();
    }
  };

  const syncPremiumStatus = async () => {
    if (PREMIUM_TEST_MODE) {
      isPremiumMode = true;
      await chrome.storage.sync.set({ isPremium: true });
      return true;
    }

    if (!extpay) {
      isPremiumMode = false;
      return false;
    }

    try {
      const user = await extpay.getUser();
      isPremiumMode = Boolean(user?.paid);

      await chrome.storage.sync.set({
        isPremium: isPremiumMode,
        premiumPlanInterval: user?.plan?.interval || null,
        premiumEmail: user?.email || null,
      });

      return isPremiumMode;
    } catch (error) {
      console.warn('ExtensionPay status check failed:', error);
      const stored = await chrome.storage.sync.get('isPremium');
      isPremiumMode = Boolean(stored.isPremium);
      return isPremiumMode;
    }
  };

  const syncPremiumUI = () => {
    if (topReadyWrap) {
      if (isPremiumMode) {
        show(topReadyWrap);
      } else {
        hide(topReadyWrap);
      }
    }

    if (premiumNote) {
      premiumNote.textContent = isPremiumMode
        ? 'Premium is active: mix hobbies, use Learn More links, refresh facts anytime, and personalize your emoji strip.'
        : 'Free mode: pick 1 hobby and get 1 fact each day. Premium unlocks hobby mixing, Learn More links, Next Fact, and emoji personalization.';
    }

    if (selectionHeading) {
      selectionHeading.textContent = isPremiumMode
        ? 'Select One Or More Hobbies'
        : 'Select One Hobby';
    }

    if (customizeEmojisBtn) {
      customizeEmojisBtn.textContent = isPremiumMode
        ? '😀 Customize Top Emojis'
        : '🔒 Customize Top Emojis (Premium)';
      customizeEmojisBtn.classList.toggle('premium-locked-control', !isPremiumMode);
    }

    if (refreshBtn) {
      refreshBtn.textContent = isPremiumMode ? '🔄 Next Fact' : '🔒 Next Fact (Premium)';
      refreshBtn.classList.toggle('premium-locked-control', !isPremiumMode);
    }

    premiumButtons.forEach((btn) => {
      btn.textContent = isPremiumMode ? '⭐ Manage Premium' : '⭐ Get Premium';
    });
  };

  const updateReadyState = () => {
    if (!readyBtn || !selectionStatus) return;

    if (!isPremiumMode) {
      readyBtn.disabled = true;
      selectionStatus.textContent = 'Premium lets you mix multiple hobbies before you start.';
      return;
    }

    readyBtn.disabled = selectedHobbies.length === 0;

    if (selectedHobbies.length === 0) {
      selectionStatus.textContent = 'Select one or more hobbies, then tap ready.';
      return;
    }

    const label = selectedHobbies.length === 1 ? 'hobby' : 'hobbies';
    selectionStatus.textContent = `${selectedHobbies.length} ${label} selected.`;
  };

  const setRowExpanded = (row, expanded) => {
    const body = row.querySelector('.accordion-body, .accordion-section-body');
    const arrow = row.querySelector('.accordion-arrow');
    const header = row.querySelector('.accordion-header, .accordion-section-toggle');

    if (!body || !arrow) return;

    body.classList.toggle('hidden', !expanded);
    arrow.textContent = expanded ? '▾' : '▸';
    if (header) header.classList.toggle('expanded', expanded);
  };

  const toggleAllAccordions = (expanded) => {
    if (!hobbyList) return;
    hobbyList.querySelectorAll('.accordion-item, .accordion-section').forEach((row) => {
      setRowExpanded(row, expanded);
    });
  };

  const startSingleHobby = async (hobbyId, hobbyName, sources) => {
    selectedHobbies = [{ id: hobbyId, name: hobbyName, sources }];

    await chrome.storage.sync.set({
      hobbyId,
      hobbyName,
      hobbyQueryName: hobbyName,
      hobbySources: sources,
      selectedHobbies,
    });
    await chrome.storage.local.remove(['cachedFact', 'cachedDate', 'cachedHobby']);
    showFactScreen(hobbyId, hobbyName, hobbyName);
  };

  const toggleHobbySelection = (hobbyId, hobbyName, sources, row) => {
    if (isSelectedHobby(hobbyId)) {
      selectedHobbies = selectedHobbies.filter((item) => item.id !== hobbyId);
    } else {
      selectedHobbies = [...selectedHobbies, { id: hobbyId, name: hobbyName, sources }];
    }

    row.classList.toggle('selected', isSelectedHobby(hobbyId));
    updateReadyState();
  };

  const todayKey = () => {
    const d = new Date();
    return `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()}`;
  };

  // ── Collect all source IDs from a node recursively ────────────
  const collectSources = (node) => {
    if (!node.categories || node.categories.length === 0) {
      return [node.id];
    }
    const sources = [];
    // If the node has its own id that maps to a fact file, include it
    for (const cat of node.categories) {
      sources.push(...collectSources(cat));
    }
    return sources;
  };

  // ── Build accordion HTML ──────────────────────────────────────
  const buildAccordion = (items, level = 0) => {
    const container = document.createElement('div');
    container.className = `accordion-level level-${level}`;

    items.forEach((item) => {
      const hasChildren = item.categories && item.categories.length > 0;
      const isSectionLabel = item.id === 'top-choices' || item.id === 'more-hobbies';
      const row = document.createElement('div');
      row.className = isSectionLabel ? 'accordion-section' : 'accordion-item';
      if (!isSectionLabel && isSelectedHobby(item.id)) row.classList.add('selected');

      if (isSectionLabel) {
        const sectionToggle = document.createElement('button');
        sectionToggle.type = 'button';
        sectionToggle.className = 'accordion-section-toggle';

        const arrow = document.createElement('span');
        arrow.className = 'accordion-arrow';
        const startExpanded = item.id === 'top-choices';
        arrow.textContent = startExpanded ? '▾' : '▸';

        const sectionLabel = document.createElement('span');
        sectionLabel.className = 'accordion-section-label';
        sectionLabel.textContent = item.label;

        sectionToggle.appendChild(arrow);
        sectionToggle.appendChild(sectionLabel);
        if (startExpanded) sectionToggle.classList.add('expanded');
        row.appendChild(sectionToggle);

        if (hasChildren) {
          const sectionBody = document.createElement('div');
          sectionBody.className = startExpanded ? 'accordion-section-body' : 'accordion-section-body hidden';
          sectionBody.appendChild(buildAccordion(item.categories, level));
          row.appendChild(sectionBody);

          sectionToggle.addEventListener('click', () => {
            const shouldExpand = sectionBody.classList.contains('hidden');
            setRowExpanded(row, shouldExpand);
          });
        }

        container.appendChild(row);
        return;
      }

      // Header row
      const header = document.createElement('div');
      header.className = `accordion-header level-${level}`;

      if (hasChildren) {
        const arrow = document.createElement('span');
        arrow.className = 'accordion-arrow';
        arrow.textContent = '▸';
        header.appendChild(arrow);
      }

      const icon = document.createElement('span');
      icon.className = 'accordion-icon';
      icon.textContent = item.icon || '';

      const label = document.createElement('span');
      label.className = 'accordion-label';
      label.textContent = item.label;

      if (item.icon) header.appendChild(icon);
      header.appendChild(label);

      // Click on label = toggle for premium, or start immediately in free mode
      label.addEventListener('click', async (e) => {
        e.stopPropagation();
        const sources = collectSources(item);

        if (isPremiumMode) {
          toggleHobbySelection(item.id, item.label, sources, row);
        } else {
          await startSingleHobby(item.id, item.label, sources);
        }
      });

      // Click on arrow or header area = toggle children
      if (hasChildren) {
        const toggleArea = header;
        toggleArea.addEventListener('click', (e) => {
          // Only toggle if clicking header area (not the label which selects)
          if (e.target === label) return;
          e.stopPropagation();
          const body = row.querySelector('.accordion-body');
          const arrow = header.querySelector('.accordion-arrow');
          if (body.classList.contains('hidden')) {
            body.classList.remove('hidden');
            arrow.textContent = '▾';
            header.classList.add('expanded');
          } else {
            body.classList.add('hidden');
            arrow.textContent = '▸';
            header.classList.remove('expanded');
          }
        });
      }

      row.appendChild(header);

      // Children
      if (hasChildren) {
        const body = document.createElement('div');
        body.className = 'accordion-body hidden';
        body.appendChild(buildAccordion(item.categories, level + 1));
        row.appendChild(body);
      }

      container.appendChild(row);
    });

    return container;
  };

  // ── Populate hobby list ───────────────────────────────────────
  const populateHobbies = async () => {
    const catalog = await FactsEngine.getHobbies();
    const accordion = buildAccordion(catalog.hobbies, 0);
    hobbyList.innerHTML = '';
    hobbyList.appendChild(accordion);
  };

  // ── Start facts for the selected hobbies ──────────────────────
  const startSelectedHobbies = async () => {
    if (!isPremiumMode || selectedHobbies.length === 0) return;

    const hobbySources = [...new Set(selectedHobbies.flatMap((item) => item.sources || []))];
    const hobbyId = selectedHobbies.map((item) => item.id).sort().join('+');
    const hobbyName = selectedHobbies.length === 1 ? selectedHobbies[0].name : 'Your Hobby Mix';
    const hobbyQueryName = selectedHobbies.map((item) => item.name).join(', ');

    await chrome.storage.sync.set({
      hobbyId,
      hobbyName,
      hobbyQueryName,
      hobbySources,
      selectedHobbies,
    });
    await chrome.storage.local.remove(['cachedFact', 'cachedDate', 'cachedHobby']);
    showFactScreen(hobbyId, hobbyName, hobbyQueryName);
  };

  // ── Display a fact ────────────────────────────────────────────
  const renderFact = (fact) => {
    factType.textContent = fact.typeLabel;
    factType.className = 'fact-type ' + fact.type;
    factText.textContent = fact.text;

    if (factCredit) {
      const creditParts = [];
      const shouldShowLyricCredit = Boolean(fact.isLyric && (fact.artist || fact.songTitle));
      const shouldShowQuoteCredit = Boolean(!fact.isLyric && fact.quoteBy);

      if (shouldShowLyricCredit) {
        if (fact.artist) creditParts.push(`Artist: ${fact.artist}`);
        if (fact.songTitle) creditParts.push(`Song: ${fact.songTitle}`);
      } else if (shouldShowQuoteCredit) {
        creditParts.push(`Said by: ${fact.quoteBy}`);
      }

      if (creditParts.length > 0) {
        factCredit.textContent = creditParts.join(' • ');
        show(factCredit);
      } else {
        hide(factCredit);
      }
    }

    const fallbackSource = FactsEngine.buildLearnMoreUrl(
      hobbyLabel?.textContent || 'Hobby Drop',
      fact.text || '',
      fact.artist || '',
      fact.songTitle || '',
      fact.quoteBy || ''
    );
    const learnMoreUrl = fact.source || fallbackSource;

    if (learnMoreUrl) {
      if (isPremiumMode) {
        factSource.href = learnMoreUrl;
        factSource.textContent = 'Link To Learn More!';
        factSource.classList.remove('premium-locked-link');
      } else {
        factSource.href = '#';
        factSource.textContent = '🔒 Link To Learn More! (Premium)';
        factSource.classList.add('premium-locked-link');
      }
      show(factSource);
    } else {
      hide(factSource);
    }
  };

  // ── Fetch + cache today's fact ────────────────────────────────
  const loadFact = async (hobbyId, hobbyName, hobbyQueryName = hobbyName, forceRefresh = false) => {
    show(loading);

    if (!forceRefresh) {
      const cached = await chrome.storage.local.get(['cachedFact', 'cachedDate', 'cachedHobby']);
      const cachedFact = cached.cachedFact;
      const cachedLooksRelevant = !cachedFact || cachedFact.type !== 'on-this-day'
        || FactsEngine.isRelevantToHobby(cachedFact.text || '', hobbyQueryName || hobbyName);

      if (cachedFact && cached.cachedDate === todayKey() && cached.cachedHobby === hobbyId && cachedLooksRelevant) {
        renderFact(cachedFact);
        hide(loading);
        return;
      }

      if (cachedFact && cached.cachedDate === todayKey() && cached.cachedHobby === hobbyId && !cachedLooksRelevant) {
        await chrome.storage.local.remove(['cachedFact', 'cachedDate', 'cachedHobby']);
      }
    }

    const sources = await chrome.storage.sync.get('hobbySources').then((r) => r.hobbySources || null);
    const fact = await FactsEngine.getFact(hobbyId, hobbyQueryName || hobbyName, forceRefresh, sources);
    renderFact(fact);

    await chrome.storage.local.set({
      cachedFact: fact,
      cachedDate: todayKey(),
      cachedHobby: hobbyId,
    });

    hide(loading);
  };

  // ── Show fact screen ──────────────────────────────────────────
  const showFactScreen = (hobbyId, hobbyName, hobbyQueryName = hobbyName) => {
    hobbyLabel.textContent = hobbyName;
    dateBadge.textContent = FactsEngine.formatDate();
    hide(setupScreen);
    show(factScreen);
    loadFact(hobbyId, hobbyName, hobbyQueryName);
  };

  // ── Events ────────────────────────────────────────────────────
  changeBtn.addEventListener('click', () => {
    hide(factScreen);
    show(setupScreen);
    updateReadyState();
  });

  if (readyBtn) {
    readyBtn.addEventListener('click', async () => {
      await startSelectedHobbies();
    });
  }

  refreshBtn.addEventListener('click', async () => {
    if (!isPremiumMode) {
      await showPremiumDetails(true);
      return;
    }

    const { hobbyId, hobbyName, hobbyQueryName } = await chrome.storage.sync.get([
      'hobbyId',
      'hobbyName',
      'hobbyQueryName',
    ]);
    if (hobbyId) loadFact(hobbyId, hobbyName, hobbyQueryName || hobbyName, true);
  });

  if (expandAllBtn) {
    expandAllBtn.addEventListener('click', () => {
      show(hobbyList);
      toggleAllAccordions(true);
    });
  }

  if (collapseAllBtn) {
    collapseAllBtn.addEventListener('click', () => {
      show(hobbyList);
      toggleAllAccordions(false);
    });
  }

  premiumButtons.forEach((btn) => {
    btn.addEventListener('click', async () => {
      await showPremiumDetails(true);
    });
  });

  if (factSource) {
    factSource.addEventListener('click', async (event) => {
      if (!isPremiumMode) {
        event.preventDefault();
        await showPremiumDetails(true);
      }
    });
  }

  chrome.storage.sync.get('customTopEmojis', ({ customTopEmojis }) => {
    if (emojiStrip) {
      emojiStrip.textContent = (customTopEmojis || DEFAULT_TOP_EMOJIS).trim();
    }
  });

  if (customizeEmojisBtn) {
    customizeEmojisBtn.addEventListener('click', async () => {
      if (!isPremiumMode) {
        await showPremiumDetails(true);
        return;
      }

      const current = emojiStrip?.textContent?.trim() || DEFAULT_TOP_EMOJIS;
      const updated = window.prompt('Enter the hobby emojis you want at the top:', current);
      if (updated === null) return;
      const finalValue = (updated.trim() || DEFAULT_TOP_EMOJIS);
      await chrome.storage.sync.set({ customTopEmojis: finalValue });
      if (emojiStrip) emojiStrip.textContent = finalValue;
    });
  }

  // ── Init ──────────────────────────────────────────────────────
  const init = async () => {
    const {
      selectedHobbies: savedSelections,
      hobbyId,
      hobbyName,
      hobbyQueryName,
    } = await chrome.storage.sync.get([
      'selectedHobbies',
      'hobbyId',
      'hobbyName',
      'hobbyQueryName',
    ]);

    await syncPremiumStatus();

    selectedHobbies = Array.isArray(savedSelections)
      ? (isPremiumMode ? savedSelections : savedSelections.slice(0, 1))
      : [];

    if (!isPremiumMode) {
      const firstSelection = selectedHobbies[0];
      if (firstSelection) {
        await chrome.storage.sync.set({
          selectedHobbies: [firstSelection],
          hobbyId: firstSelection.id,
          hobbyName: firstSelection.name,
          hobbyQueryName: firstSelection.name,
          hobbySources: firstSelection.sources || [firstSelection.id],
        });
      } else if (hobbyId && String(hobbyId).includes('+')) {
        await chrome.storage.sync.remove(['hobbyId', 'hobbyName', 'hobbyQueryName', 'hobbySources']);
      }
    }

    syncPremiumUI();
    await populateHobbies();
    updateReadyState();

    if (hobbyId && hobbyName) {
      showFactScreen(hobbyId, hobbyName, hobbyQueryName || hobbyName);
    } else {
      show(setupScreen);
    }
  };

  init();
})();
