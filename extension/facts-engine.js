/**
 * Facts Engine v2 — Local-first with Wikipedia "On This Day" bonus
 *
 * Architecture:
 *  - Each hobby has a JSON file at data/facts/{id}.json
 *  - Facts can be date-tagged (month+day) or general
 *  - On popup open: pick a date-tagged fact if today matches, else rotate daily
 *  - Also tries Wikimedia "On This Day" API as a bonus overlay
 */

const FactsEngine = (() => {
  /* ── helpers ─────────────────────────────────────────── */
  const today = () => {
    const d = new Date();
    return { month: d.getMonth() + 1, day: d.getDate(), year: d.getFullYear() };
  };

  const formatDate = () =>
    new Date().toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });

  const pad = (n) => String(n).padStart(2, '0');

  const dayOfYear = () => {
    const now = new Date();
    const start = new Date(now.getFullYear(), 0, 0);
    return Math.floor((now - start) / 86400000);
  };

  const buildLearnMoreUrl = (hobbyLabel, factText = '', artist = '', songTitle = '', quoteBy = '') => {
    const rawText = String(factText || '');
    const normalize = (value = '') => String(value)
      .toLowerCase()
      .replace(/["“”'’]/g, '')
      .replace(/&/g, ' ')
      .replace(/—/g, ' ')
      .replace(/[^a-z0-9\s:/().,!+-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();

    const toWikiUrl = (topic = '', anchor = '') => {
      const preserveLeadingThe = new Set([
        'the beatles', 'the who', 'the doors', 'the eagles', 'the simpsons', 'the godfather'
      ]);

      let cleaned = String(topic || '')
        .replace(/^['"“”]+|['"“”]+$/g, '')
        .replace(/[.,:;!?]+$/g, '')
        .trim();

      if (/^the\s+/i.test(cleaned) && !preserveLeadingThe.has(cleaned.toLowerCase())) {
        cleaned = cleaned.replace(/^the\s+/i, '').trim();
      }

      if (!cleaned) return '';
      const slug = cleaned.replace(/\s+/g, '_');
      return `https://en.wikipedia.org/wiki/${encodeURIComponent(slug)}${anchor ? `#${anchor}` : ''}`;
    };

    const toYouTubeSearch = (query = '') =>
      `https://www.youtube.com/results?search_query=${encodeURIComponent(query)}`;

    const extractQuotedTitle = (text = '') => {
      const match = text.match(/["“]([^"”]{2,100})["”]/);
      return match ? match[1].trim() : '';
    };

    const extractSubjectCandidate = (text = '') => {
      const cleaned = String(text || '')
        .replace(/^In\s+\d{3,4},\s*/i, '')
        .replace(/^On\s+[A-Z][a-z]+\s+\d{1,2},\s+\d{4},\s*/i, '')
        .replace(/^According to [^,]+,\s*/i, '')
        .trim();

      const subjectMatch = cleaned.match(/^(.{2,100}?)\s+(?:is|are|was|were|has|have|had|became|becomes|won|wins|said|says|wrote|writes|recorded|released|performed|formed|founded|created|invented|developed|discovered|opened|contains|includes|features|marks|marked|helped|changed|earned|spent|introduced|inspired|acquired|met|left|joined|signed|set|sets|took|takes|gave|give|tells|told|built|named|called|ran|run|grew|launched|saved|starred|appeared|centered|centres|reached|saw|turned)\b/i);
      const properNameMatch = cleaned.match(/\b([A-Z][A-Za-z0-9'’&().:-]*(?:\s+(?:[A-Z][A-Za-z0-9'’&().:-]*|of|the|and|for|to|in|on|at|with|vs\.?|\d{1,4})){1,7})\b/);
      if (!subjectMatch && !properNameMatch) return '';

      let candidate = (subjectMatch ? subjectMatch[1] : properNameMatch[1])
        .replace(/^['"“”]+|['"“”]+$/g, '')
        .replace(/\s+(?:in|on|at)\s+\d{4}$/i, '')
        .replace(/\s+on\s+[A-Z][a-z]+\s+\d{1,2}(?:,\s+\d{4})?$/i, '')
        .replace(/[.,:;!?]+$/g, '')
        .trim();

      if (candidate.length < 2 || candidate.length > 90) return '';
      if (/^(in|on|for|with|from|during)$/i.test(candidate)) return '';
      return candidate;
    };

    const combined = normalize(`${hobbyLabel} ${artist} ${songTitle} ${quoteBy} ${rawText}`);
    const isMusicContext = [
      'music', 'rock', 'band', 'beatles', 'punk', 'metal', 'jazz', 'blues',
      'reggae', 'hip hop', 'country', 'pop', 'disco', 'emo', 'song', 'album'
    ].some((term) => combined.includes(term));
    const isMovieOrTvContext = [
      'movie', 'movies', 'film', 'cinema', 'tv', 'show', 'streaming', 'episode', 'series'
    ].some((term) => combined.includes(term));

    if (artist && songTitle) {
      return toYouTubeSearch(`${artist} ${songTitle} live performance`);
    }

    const directLinks = [
      ['beatles 20 number one singles', 'https://en.wikipedia.org/wiki/The_Beatles%27_recording_legacy#Number-one_singles'],
      ['20 number-one singles on the billboard hot 100', 'https://en.wikipedia.org/wiki/The_Beatles%27_recording_legacy#Number-one_singles'],
      ['20 number one singles on the billboard hot 100', 'https://en.wikipedia.org/wiki/The_Beatles%27_recording_legacy#Number-one_singles'],
      ['top five positions on the billboard hot 100', 'https://en.wikipedia.org/wiki/The_Beatles%27_recording_legacy#Chart_achievements'],
      ['billboard hot 100', 'https://en.wikipedia.org/wiki/Billboard_Hot_100'],
      ['rock and roll hall of fame', 'https://en.wikipedia.org/wiki/Rock_and_Roll_Hall_of_Fame'],
      ['ed sullivan show', 'https://en.wikipedia.org/wiki/The_Ed_Sullivan_Show'],
      ['abbey road', 'https://en.wikipedia.org/wiki/Abbey_Road'],
      ['sgt pepper', 'https://en.wikipedia.org/wiki/Sgt._Pepper%27s_Lonely_Hearts_Club_Band'],
      ['white album', 'https://en.wikipedia.org/wiki/The_Beatles_(album)'],
      ['let it be', 'https://en.wikipedia.org/wiki/Let_It_Be_(album)'],
      ['kurt cobain', 'https://en.wikipedia.org/wiki/Kurt_Cobain'],
      ['nirvana', 'https://en.wikipedia.org/wiki/Nirvana_(band)'],
      ['smells like teen spirit', 'https://www.youtube.com/results?search_query=Nirvana+Smells+Like+Teen+Spirit+live'],
      ['come as you are', 'https://www.youtube.com/results?search_query=Nirvana+Come+As+You+Are+live'],
      ['bohemian rhapsody', 'https://www.youtube.com/results?search_query=Queen+Bohemian+Rhapsody+live'],
      ['hotel california', 'https://www.youtube.com/results?search_query=Eagles+Hotel+California+live'],
      ['stairway to heaven', 'https://www.youtube.com/results?search_query=Led+Zeppelin+Stairway+to+Heaven+live'],
      ['free bird', 'https://www.youtube.com/results?search_query=Lynyrd+Skynyrd+Free+Bird+live'],
      ['layla', 'https://www.youtube.com/results?search_query=Eric+Clapton+Layla+live'],
      ['born to run', 'https://www.youtube.com/results?search_query=Bruce+Springsteen+Born+to+Run+live'],
      ['action comics 1', 'https://en.wikipedia.org/wiki/Action_Comics_1'],
      ['detective comics 27', 'https://en.wikipedia.org/wiki/Detective_Comics_27'],
      ['detective comics 38', 'https://en.wikipedia.org/wiki/Robin_(character)'],
      ['batman begins', 'https://en.wikipedia.org/wiki/Batman_Begins'],
      ['the dark knight returns', 'https://en.wikipedia.org/wiki/The_Dark_Knight_Returns'],
      ['the dark knight rises', 'https://en.wikipedia.org/wiki/The_Dark_Knight_Rises'],
      ['batman the animated series', 'https://en.wikipedia.org/wiki/Batman:_The_Animated_Series'],
      ['the batman 2022', 'https://en.wikipedia.org/wiki/The_Batman_(film)'],
      ['superman ii', 'https://en.wikipedia.org/wiki/Superman_II'],
      ['all star superman', 'https://en.wikipedia.org/wiki/All-Star_Superman'],
      ['man of steel', 'https://en.wikipedia.org/wiki/Man_of_Steel_(film)'],
      ['wonder woman 2017', 'https://en.wikipedia.org/wiki/Wonder_Woman_(2017_film)'],
      ['justice league unlimited', 'https://en.wikipedia.org/wiki/Justice_League_Unlimited'],
      ['super friends', 'https://en.wikipedia.org/wiki/Super_Friends'],
      ['x men 97', 'https://en.wikipedia.org/wiki/X-Men_%2797'],
      ['x men the animated series', 'https://en.wikipedia.org/wiki/X-Men_(TV_series)'],
      ['days of future past', 'https://en.wikipedia.org/wiki/X-Men:_Days_of_Future_Past'],
      ['dark phoenix saga', 'https://en.wikipedia.org/wiki/The_Dark_Phoenix_Saga'],
      ['wolverine', 'https://en.wikipedia.org/wiki/Wolverine_(character)'],
      ['professor x', 'https://en.wikipedia.org/wiki/Professor_X'],
      ['magneto', 'https://en.wikipedia.org/wiki/Magneto_(Marvel_Comics)'],
      ['joker', 'https://en.wikipedia.org/wiki/Joker_(character)'],
      ['lex luthor', 'https://en.wikipedia.org/wiki/Lex_Luthor'],
      ['kryptonite', 'https://en.wikipedia.org/wiki/Kryptonite'],
      ['fortress of solitude', 'https://en.wikipedia.org/wiki/Fortress_of_Solitude'],
      ['gal gadot', 'https://en.wikipedia.org/wiki/Gal_Gadot'],
      ['christopher reeve', 'https://en.wikipedia.org/wiki/Christopher_Reeve'],
      ['kevin conroy', 'https://en.wikipedia.org/wiki/Kevin_Conroy'],
      ['stan lee', 'https://en.wikipedia.org/wiki/Stan_Lee'],
      ['jack kirby', 'https://en.wikipedia.org/wiki/Jack_Kirby']
    ];

    for (const [keyword, url] of directLinks) {
      if (combined.includes(keyword)) return url;
    }

    if (quoteBy && !isMusicContext) {
      const quoteUrl = toWikiUrl(quoteBy);
      if (quoteUrl) return quoteUrl;
    }

    const quotedTitle = extractQuotedTitle(rawText);
    if (quotedTitle) {
      if (isMusicContext) {
        const performer = artist || hobbyLabel || 'song';
        return toYouTubeSearch(`${performer} ${quotedTitle} live performance`);
      }
      if (isMovieOrTvContext) {
        return toWikiUrl(quotedTitle);
      }
      const quotedUrl = toWikiUrl(quotedTitle);
      if (quotedUrl) return quotedUrl;
    }

    const yearTitleMatch = rawText.match(/([A-Z][A-Za-z0-9&'’:!?,.\-]+(?:\s+[A-Z0-9][A-Za-z0-9&'’:!?,.\-]+){0,8})\s*\((?:19|20)\d{2}\)/);
    if (yearTitleMatch) {
      const titleUrl = toWikiUrl(yearTitleMatch[1]);
      if (titleUrl) return titleUrl;
    }

    const subjectCandidate = extractSubjectCandidate(rawText);
    if (subjectCandidate) {
      const subjectUrl = toWikiUrl(subjectCandidate);
      if (subjectUrl) return subjectUrl;
    }

    const fallbackProperNameMatch = rawText.match(/\b([A-Z][A-Za-z0-9'’&().:-]*(?:\s+(?:[A-Z][A-Za-z0-9'’&().:-]*|of|the|and|for|to|in|on|at|with|vs\.?|\d{1,4})){1,7})\b/);
    if (fallbackProperNameMatch) {
      const namedUrl = toWikiUrl(fallbackProperNameMatch[1]);
      if (namedUrl) return namedUrl;
    }

    if (artist && isMusicContext) {
      return toYouTubeSearch(`${artist} live performance`);
    }

    const hobbyDefaults = [
      ['the beatles', 'https://en.wikipedia.org/wiki/The_Beatles'],
      ['60s movies', 'https://en.wikipedia.org/wiki/1960s_in_film'],
      ['70s movies', 'https://en.wikipedia.org/wiki/1970s_in_film'],
      ['80s movies', 'https://en.wikipedia.org/wiki/1980s_in_film'],
      ['90s movies', 'https://en.wikipedia.org/wiki/1990s_in_film'],
      ['2000s 2026 movies', 'https://en.wikipedia.org/wiki/2000s_in_film'],
      ['general movie facts', 'https://en.wikipedia.org/wiki/Film'],
      ['action adventure', 'https://en.wikipedia.org/wiki/Action_film'],
      ['animated movies', 'https://en.wikipedia.org/wiki/Animation'],
      ['comedy movies', 'https://en.wikipedia.org/wiki/Comedy_film'],
      ['drama movies', 'https://en.wikipedia.org/wiki/Drama_(film_and_television)'],
      ['fantasy movies', 'https://en.wikipedia.org/wiki/Fantasy_film'],
      ['horror movies', 'https://en.wikipedia.org/wiki/Horror_film'],
      ['romantic comedies', 'https://en.wikipedia.org/wiki/Romantic_comedy'],
      ['documentaries', 'https://en.wikipedia.org/wiki/Documentary_film'],
      ['war movies', 'https://en.wikipedia.org/wiki/War_film'],
      ['western movies', 'https://en.wikipedia.org/wiki/Western_(genre)'],
      ['sports movies', 'https://en.wikipedia.org/wiki/Sports_film'],
      ['classic movies', 'https://en.wikipedia.org/wiki/Classical_Hollywood_cinema'],
      ['tv shows streaming', 'https://en.wikipedia.org/wiki/Television_show'],
      ['general music facts', 'https://en.wikipedia.org/wiki/Music'],
      ['famous quotes', 'https://en.wikiquote.org/wiki/Main_Page'],
      ['song lyrics', 'https://en.wikipedia.org/wiki/Lyric'],
      ['working out fitness', 'https://en.wikipedia.org/wiki/Physical_fitness'],
      ['biking cycling', 'https://en.wikipedia.org/wiki/Cycling'],
      ['swimming diving', 'https://en.wikipedia.org/wiki/Swimming_(sport)'],
      ['board games puzzles', 'https://en.wikipedia.org/wiki/Board_game'],
      ['video games', 'https://en.wikipedia.org/wiki/Video_game'],
      ['fashion models', 'https://en.wikipedia.org/wiki/Model_(person)'],
      ['crime mystery', 'https://en.wikipedia.org/wiki/Crime_fiction'],
      ['ghosts paranormal', 'https://en.wikipedia.org/wiki/Ghost'],
      ['hiking walking', 'https://en.wikipedia.org/wiki/Hiking'],
      ['water sports', 'https://en.wikipedia.org/wiki/Water_sport'],
      ['writing journaling', 'https://en.wikipedia.org/wiki/Journaling'],
      ['world culture', 'https://en.wikipedia.org/wiki/Culture'],
      ['food facts', 'https://en.wikipedia.org/wiki/Food'],
      ['fast food', 'https://en.wikipedia.org/wiki/Fast_food'],
      ['world food', 'https://en.wikipedia.org/wiki/World_cuisine'],
      ['superman', 'https://en.wikipedia.org/wiki/Superman'],
      ['batman', 'https://en.wikipedia.org/wiki/Batman'],
      ['wonder woman', 'https://en.wikipedia.org/wiki/Wonder_Woman'],
      ['spider man', 'https://en.wikipedia.org/wiki/Spider-Man'],
      ['x men', 'https://en.wikipedia.org/wiki/X-Men'],
      ['avengers', 'https://en.wikipedia.org/wiki/Avengers_(comics)'],
      ['hulk', 'https://en.wikipedia.org/wiki/Hulk'],
      ['green lantern', 'https://en.wikipedia.org/wiki/Green_Lantern'],
      ['the flash', 'https://en.wikipedia.org/wiki/Flash_(DC_Comics_character)'],
      ['super heroes', 'https://en.wikipedia.org/wiki/Superhero'],
      ['comic books', 'https://en.wikipedia.org/wiki/Comic_book'],
      ['science facts quotes', 'https://en.wikipedia.org/wiki/Science'],
      ['science', 'https://en.wikipedia.org/wiki/Science'],
      ['inventors', 'https://en.wikipedia.org/wiki/List_of_inventors_and_discoverers']
    ];

    for (const [keyword, url] of hobbyDefaults) {
      if (combined.includes(keyword)) return url;
    }

    const query = [quoteBy, artist, songTitle, hobbyLabel, rawText].filter(Boolean).join(' ').trim();
    return `https://en.wikipedia.org/wiki/Special:Search?search=${encodeURIComponent(query)}&go=Go`;
  };

  const extractMusicMeta = (fact = {}, hobbyLabel = '') => {
    const text = String(fact.text || '');
    const existingArtist = fact.artist || fact.band || '';
    const existingSongTitle = fact.songTitle || fact.song || '';
    const normalizedHobby = String(hobbyLabel || '').toLowerCase();
    const songArtistOverrides = {
      'smells like teen spirit': 'Nirvana',
      'come as you are': 'Nirvana',
      'something in the way': 'Nirvana',
      'heart-shaped box': 'Nirvana',
      'all apologies': 'Nirvana',
      'lithium': 'Nirvana',
    };

    const inferredIsLyric = Boolean(fact.isLyric || fact.type === 'lyric')
      || /^["“].{8,120}["”]/.test(text)
      || /lyrics?\s+from/i.test(text);

    const normalizeArtistForSong = (artistName = '', songName = '') => {
      const override = songArtistOverrides[String(songName || '').toLowerCase()];
      if (override) return override;
      if (normalizedHobby.includes('nirvana')) return 'Nirvana';
      return artistName;
    };

    if (existingArtist || existingSongTitle) {
      return {
        artist: inferredIsLyric ? normalizeArtistForSong(existingArtist, existingSongTitle) : '',
        songTitle: inferredIsLyric ? (existingSongTitle || '') : '',
        isLyric: inferredIsLyric && Boolean(existingArtist || existingSongTitle),
      };
    }

    const possessiveSongMatch = text.match(/([A-Z][A-Za-z0-9&./+\- ]+?)'s ['“]([^'”]+)['”]/);
    const bySongMatch = text.match(/['“]([^'”]+)['”] by ([A-Z][A-Za-z0-9&./+\- ]+)/);

    const parsedArtist = possessiveSongMatch
      ? possessiveSongMatch[1].trim()
      : bySongMatch
        ? bySongMatch[2].trim()
        : '';

    const parsedSongTitle = possessiveSongMatch
      ? possessiveSongMatch[2].trim()
      : bySongMatch
        ? bySongMatch[1].trim()
        : '';

    if (!inferredIsLyric) {
      return { artist: '', songTitle: '', isLyric: false };
    }

    return {
      artist: normalizeArtistForSong(parsedArtist, parsedSongTitle),
      songTitle: parsedSongTitle,
      isLyric: Boolean(parsedArtist || parsedSongTitle),
    };
  };

  const withLearnMoreSource = (fact, hobbyLabel) => {
    const musicMeta = extractMusicMeta(fact, hobbyLabel);
    return {
      ...fact,
      ...musicMeta,
      source: fact.source || buildLearnMoreUrl(hobbyLabel, fact.text, musicMeta.artist, musicMeta.songTitle, fact.quoteBy || ''),
    };
  };

  /* ── load local facts for a hobby ───────────────────── */
  let _cache = {};

  const loadFacts = async (hobbyId) => {
    if (_cache[hobbyId]) return _cache[hobbyId];
    try {
      const url = chrome.runtime.getURL(`data/facts/${hobbyId}.json`);
      const res = await fetch(url);
      if (!res.ok) return null;
      const data = await res.json();
      _cache[hobbyId] = data;
      return data;
    } catch (e) {
      console.warn('[DOD] Could not load facts for', hobbyId, e);
      return null;
    }
  };

  /* ── load & merge facts from multiple sources ───────── */
  const loadMergedFacts = async (sources) => {
    const key = sources.join('+');
    if (_cache[key]) return _cache[key];
    const allFacts = [];
    for (const src of sources) {
      const data = await loadFacts(src);
      if (data && data.facts) allFacts.push(...data.facts);
    }
    if (allFacts.length === 0) return null;
    const merged = { hobby: 'Merged', facts: allFacts };
    _cache[key] = merged;
    return merged;
  };

  const getTypeLabel = (fact = {}) => {
    if (fact.month) return '📅 On This Day';
    if (fact.type === 'did-you-know') return '💡 Did You Know?';
    if (fact.type === 'quote') return '💬 Famous Quote';
    if (fact.type === 'lyric' || fact.isLyric) return '🎵 Song Lyric';
    return 'Hobby Fact';
  };

  /* ── pick one fact from local data ──────────────────── */
  const pickLocalFact = (data, hobbyLabel = data.hobby || '') => {
    const { month, day } = today();
    const facts = data.facts || [];

    // 1. Look for a date-specific fact first
    const dated = facts.filter((f) => f.month === month && f.day === day);
    if (dated.length > 0) {
      const pick = dated[Math.floor(Math.random() * dated.length)];
      return withLearnMoreSource({
        ...pick,
        type: 'on-this-day',
        typeLabel: '📅 On This Day',
        text: pick.text,
        source: pick.source || null,
      }, hobbyLabel);
    }

    // 2. Use day-of-year as a stable index so user sees same fact all day
    const general = facts.filter((f) => !f.month);
    if (general.length === 0) return null;

    const idx = dayOfYear() % general.length;
    const pick = general[idx];
    return withLearnMoreSource({
      ...pick,
      type: pick.type || 'fun-fact',
      typeLabel: getTypeLabel(pick),
      text: pick.text,
      source: pick.source || null,
    }, hobbyLabel);
  };

  /* ── random fact (for "refresh" button) ─────────────── */
  const pickRandomFact = (data, hobbyLabel = data.hobby || '') => {
    const facts = data.facts || [];
    if (facts.length === 0) return null;
    const pick = facts[Math.floor(Math.random() * facts.length)];
    return withLearnMoreSource({
      ...pick,
      type: pick.month ? 'on-this-day' : pick.type || 'fun-fact',
      typeLabel: getTypeLabel(pick),
      text: pick.text,
      source: pick.source || null,
    }, hobbyLabel);
  };

  /* ── Wikipedia "On This Day" bonus ──────────────────── */
  const matchesHobby = (text, hobby) => {
    const stopWords = new Set([
      'the', 'and', 'for', 'with', 'from', 'your', 'more', 'fact', 'facts',
      'hobby', 'general', 'world', 'music', 'movies', 'movie', 'shows'
    ]);

    const normalizedHobby = String(hobby || '')
      .toLowerCase()
      .replace(/[^a-z0-9\s-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();

    const lower = String(text || '').toLowerCase();
    const keywords = normalizedHobby
      .split(/\s+/)
      .filter((w) => w.length > 3 && !stopWords.has(w));

    if (normalizedHobby && lower.includes(normalizedHobby)) return true;
    if (keywords.length === 0) return false;

    return keywords.some((w) => lower.includes(w));
  };

  const fetchOnThisDay = async (hobbyLabel) => {
    try {
      const { month, day } = today();
      const url = `https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/${pad(month)}/${pad(day)}`;
      const res = await fetch(url, { signal: AbortSignal.timeout(4000) });
      if (!res.ok) return null;
      const data = await res.json();
      const pool = [...(data.events || []), ...(data.selected || [])];
      const matches = pool.filter((item) => {
        const blob = `${item.text || ''} ${(item.pages || []).map((p) => p.title || '').join(' ')}`;
        return matchesHobby(blob, hobbyLabel);
      });
      if (matches.length === 0) return null;
      const pick = matches[Math.floor(Math.random() * matches.length)];
      const page = pick.pages && pick.pages[0];
      return withLearnMoreSource({
        type: 'on-this-day',
        typeLabel: '📅 On This Day',
        text: `In ${pick.year}, ${pick.text}`,
        source: page ? `https://en.wikipedia.org/wiki/${encodeURIComponent(page.title)}` : null,
      }, hobbyLabel);
    } catch {
      return null;
    }
  };

  /* ── fallback ───────────────────────────────────────── */
  const fallback = (hobbyLabel) => withLearnMoreSource({
    type: 'fun-fact',
    typeLabel: 'Hobby Fact',
    text: `We're still building our ${hobbyLabel} fact library! Check back soon for amazing daily facts.`,
    source: null,
  }, hobbyLabel);

  /* ── Public API ─────────────────────────────────────── */
  return {
    formatDate,
    buildLearnMoreUrl,
    isRelevantToHobby: matchesHobby,

    async getFact(hobbyId, hobbyLabel, refresh = false, sources = null) {
      // Load from multiple sources if provided, else single file
      const data = sources && sources.length
        ? await loadMergedFacts(sources)
        : await loadFacts(hobbyId);

      // Try Wikipedia "on this day" first (bonus — only if not refreshing)
      if (!refresh) {
        const otd = await fetchOnThisDay(hobbyLabel);
        if (otd) return otd;
      }

      // Local facts
      if (data) {
        const fact = refresh ? pickRandomFact(data, hobbyLabel) : pickLocalFact(data, hobbyLabel);
        if (fact) return fact;
      }

      return fallback(hobbyLabel);
    },

    async getHobbies() {
      const url = chrome.runtime.getURL('data/hobbies.json');
      const res = await fetch(url);
      return res.json();
    },
  };
})();
