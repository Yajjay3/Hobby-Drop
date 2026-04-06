import json
import re
from pathlib import Path
from urllib.parse import quote

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

DIRECT_PATTERNS = [
    (re.compile(r'the beatles.*(?:billboard hot 100|number[- ]one singles?)', re.I), 'https://en.wikipedia.org/wiki/The_Beatles%27_recording_legacy#Number-one_singles'),
    (re.compile(r'top five positions on the billboard hot 100', re.I), 'https://en.wikipedia.org/wiki/The_Beatles%27_recording_legacy#Chart_achievements'),
    (re.compile(r'rock and roll hall of fame', re.I), 'https://en.wikipedia.org/wiki/Rock_and_Roll_Hall_of_Fame'),
    (re.compile(r'ed sullivan show', re.I), 'https://en.wikipedia.org/wiki/The_Ed_Sullivan_Show'),
    (re.compile(r'abbey road', re.I), 'https://en.wikipedia.org/wiki/Abbey_Road'),
    (re.compile(r'sgt\.? pepper', re.I), 'https://en.wikipedia.org/wiki/Sgt._Pepper%27s_Lonely_Hearts_Club_Band'),
    (re.compile(r'white album', re.I), 'https://en.wikipedia.org/wiki/The_Beatles_(album)'),
    (re.compile(r'kurt cobain', re.I), 'https://en.wikipedia.org/wiki/Kurt_Cobain'),
    (re.compile(r'nirvana', re.I), 'https://en.wikipedia.org/wiki/Nirvana_(band)'),
    (re.compile(r'smells like teen spirit', re.I), 'https://www.youtube.com/results?search_query=Nirvana+Smells+Like+Teen+Spirit+live'),
    (re.compile(r'come as you are', re.I), 'https://www.youtube.com/results?search_query=Nirvana+Come+As+You+Are+live'),
    (re.compile(r'bohemian rhapsody', re.I), 'https://www.youtube.com/results?search_query=Queen+Bohemian+Rhapsody+live'),
    (re.compile(r'hotel california', re.I), 'https://www.youtube.com/results?search_query=Eagles+Hotel+California+live'),
    (re.compile(r'stairway to heaven', re.I), 'https://www.youtube.com/results?search_query=Led+Zeppelin+Stairway+to+Heaven+live'),
    (re.compile(r'free bird', re.I), 'https://www.youtube.com/results?search_query=Lynyrd+Skynyrd+Free+Bird+live'),
    (re.compile(r'layla', re.I), 'https://www.youtube.com/results?search_query=Eric+Clapton+Layla+live'),
    (re.compile(r'born to run', re.I), 'https://www.youtube.com/results?search_query=Bruce+Springsteen+Born+to+Run+live'),
]

MUSIC_TERMS = {
    'music', 'rock', 'band', 'beatles', 'punk', 'metal', 'jazz', 'blues', 'reggae',
    'hip hop', 'country', 'pop', 'disco', 'emo', 'song', 'album'
}

DEFAULT_HOBBY_LINKS = {
    'the beatles': 'https://en.wikipedia.org/wiki/The_Beatles',
    '60s movies': 'https://en.wikipedia.org/wiki/1960s_in_film',
    '70s movies': 'https://en.wikipedia.org/wiki/1970s_in_film',
    '80s movies': 'https://en.wikipedia.org/wiki/1980s_in_film',
    '90s movies': 'https://en.wikipedia.org/wiki/1990s_in_film',
    '2000s 2026 movies': 'https://en.wikipedia.org/wiki/2000s_in_film',
    'general movie facts': 'https://en.wikipedia.org/wiki/Film',
    'action adventure': 'https://en.wikipedia.org/wiki/Action_film',
    'animated movies': 'https://en.wikipedia.org/wiki/Animation',
    'comedy movies': 'https://en.wikipedia.org/wiki/Comedy_film',
    'drama movies': 'https://en.wikipedia.org/wiki/Drama_(film_and_television)',
    'fantasy movies': 'https://en.wikipedia.org/wiki/Fantasy_film',
    'horror movies': 'https://en.wikipedia.org/wiki/Horror_film',
    'romantic comedies': 'https://en.wikipedia.org/wiki/Romantic_comedy',
    'documentaries': 'https://en.wikipedia.org/wiki/Documentary_film',
    'war movies': 'https://en.wikipedia.org/wiki/War_film',
    'western movies': 'https://en.wikipedia.org/wiki/Western_(genre)',
    'sports movies': 'https://en.wikipedia.org/wiki/Sports_film',
    'classic movies': 'https://en.wikipedia.org/wiki/Classical_Hollywood_cinema',
    'tv shows streaming': 'https://en.wikipedia.org/wiki/Television_show',
    'general music facts': 'https://en.wikipedia.org/wiki/Music',
    'working out fitness': 'https://en.wikipedia.org/wiki/Physical_fitness',
    'biking cycling': 'https://en.wikipedia.org/wiki/Cycling',
    'swimming diving': 'https://en.wikipedia.org/wiki/Swimming_(sport)',
    'board games puzzles': 'https://en.wikipedia.org/wiki/Board_game',
    'video games': 'https://en.wikipedia.org/wiki/Video_game',
    'fashion models': 'https://en.wikipedia.org/wiki/Model_(person)',
    'crime mystery': 'https://en.wikipedia.org/wiki/Crime_fiction',
    'ghosts paranormal': 'https://en.wikipedia.org/wiki/Ghost',
    'hiking walking': 'https://en.wikipedia.org/wiki/Hiking',
    'water sports': 'https://en.wikipedia.org/wiki/Water_sport',
    'writing journaling': 'https://en.wikipedia.org/wiki/Journaling',
    'world culture': 'https://en.wikipedia.org/wiki/Culture',
    'food facts': 'https://en.wikipedia.org/wiki/Food',
    'fast food': 'https://en.wikipedia.org/wiki/Fast_food',
    'world food': 'https://en.wikipedia.org/wiki/World_cuisine',
    'science facts quotes': 'https://en.wikipedia.org/wiki/Science',
    'inventors': 'https://en.wikipedia.org/wiki/List_of_inventors_and_discoverers',
}


def normalize(value=''):
    value = str(value).lower().replace('&', ' ').replace('—', ' ')
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9\s:/().,!+\-]', ' ', value)).strip()


def wiki_url(topic=''):
    preserve_leading_the = {'the beatles', 'the who', 'the doors', 'the eagles', 'the simpsons', 'the godfather'}
    cleaned = str(topic or '').strip().strip('"“”\'').rstrip('.,:;!?')
    if not cleaned:
        return ''
    if cleaned.lower().startswith('the ') and cleaned.lower() not in preserve_leading_the:
        cleaned = re.sub(r'^(?:The|the)\s+', '', cleaned)
    slug = re.sub(r'\s+', '_', cleaned)
    return f'https://en.wikipedia.org/wiki/{quote(slug, safe="()_:-")}'


def youtube_url(query=''):
    return f'https://www.youtube.com/results?search_query={quote(query)}'


def extract_quoted_title(text=''):
    m = re.search(r'["“]([^"”]{2,100})["”]', text)
    return m.group(1).strip() if m else ''


def extract_subject_candidate(text=''):
    cleaned = re.sub(r'^In\s+\d{3,4},\s*', '', str(text or '').strip(), flags=re.I)
    cleaned = re.sub(r'^On\s+[A-Z][a-z]+\s+\d{1,2},\s+\d{4},\s*', '', cleaned, flags=re.I)
    cleaned = re.sub(r'^According to [^,]+,\s*', '', cleaned, flags=re.I)
    m = re.match(r'^(.{2,100}?)\s+(?:is|are|was|were|has|have|had|became|becomes|won|wins|said|says|wrote|writes|recorded|released|performed|formed|founded|created|invented|developed|discovered|opened|contains|includes|features|marks|marked|helped|changed|earned|spent|introduced|inspired|acquired|met|left|joined|signed|set|sets|took|takes|gave|give|tells|told|built|named|called|ran|run|grew|launched|saved|starred|appeared|centered|centres|reached|saw|turned)\b', cleaned, flags=re.I)
    if m:
        candidate = m.group(1).strip().strip('"“”\'')
    else:
        proper = re.search(r'\b([A-Z][A-Za-z0-9\'’&().:-]*(?:\s+(?:[A-Z][A-Za-z0-9\'’&().:-]*|of|the|and|for|to|in|on|at|with|vs\.?|\d{1,4})){1,7})\b', cleaned)
        if not proper:
            return ''
        candidate = proper.group(1).strip().strip('"“”\'')
    candidate = re.sub(r'\s+(?:in|on|at)\s+\d{4}$', '', candidate, flags=re.I)
    candidate = re.sub(r'\s+on\s+[A-Z][a-z]+\s+\d{1,2}(?:,\s+\d{4})?$', '', candidate, flags=re.I)
    candidate = candidate.rstrip('.,:;!?')
    if len(candidate) < 2 or len(candidate) > 90:
        return ''
    return candidate


def build_url(hobby, fact):
    text = str(fact.get('text', ''))
    artist = str(fact.get('artist', '') or fact.get('band', ''))
    song = str(fact.get('songTitle', '') or fact.get('song', ''))
    quote_by = str(fact.get('quoteBy', ''))
    combined = normalize(f'{hobby} {artist} {song} {quote_by} {text}')
    is_music = any(term in combined for term in MUSIC_TERMS)

    if artist and song:
        return youtube_url(f'{artist} {song} live performance')

    for pattern, url in DIRECT_PATTERNS:
        if pattern.search(text) or pattern.search(f'{hobby} {text}'):
            return url

    if quote_by and not is_music:
        direct = wiki_url(quote_by)
        if direct:
            return direct

    quoted = extract_quoted_title(text)
    if quoted:
        if is_music:
            performer = artist or hobby or 'song'
            return youtube_url(f'{performer} {quoted} live performance')
        return wiki_url(quoted)

    year_title = re.search(r'([A-Z][A-Za-z0-9&\'’:!?,.\-]+(?:\s+[A-Z0-9][A-Za-z0-9&\'’:!?,.\-]+){0,8})\s*\((?:19|20)\d{2}\)', text)
    if year_title:
        return wiki_url(year_title.group(1))

    subject = extract_subject_candidate(text)
    if subject:
        return wiki_url(subject)

    proper = re.search(r'\b([A-Z][A-Za-z0-9\'’&().:-]*(?:\s+(?:[A-Z][A-Za-z0-9\'’&().:-]*|of|the|and|for|to|in|on|at|with|vs\.?|\d{1,4})){1,7})\b', text)
    if proper:
        return wiki_url(proper.group(1))

    if artist and is_music:
        return youtube_url(f'{artist} live performance')

    normalized_hobby = normalize(hobby)
    for key, url in DEFAULT_HOBBY_LINKS.items():
        if key in normalized_hobby:
            return url

    return wiki_url(hobby) or 'https://en.wikipedia.org/wiki/Main_Page'


def main():
    updated_files = 0
    updated_facts = 0
    for path in sorted(BASE.glob('*.json')):
        data = json.loads(path.read_text(encoding='utf-8'))
        changed = False
        hobby = data.get('hobby', path.stem.replace('-', ' ').title())
        generic_sources = {
            '',
            wiki_url(hobby),
            wiki_url(re.sub(r'^(?:The|the)\s+', '', hobby)),
            wiki_url(path.stem.replace('-', ' ').title()),
        }
        for fact in data.get('facts', []):
            current = fact.get('source', '') or ''
            should_refresh = (
                (not current)
                or ('Special:Search' in current)
                or (current in generic_sources)
                or (current.startswith('https://en.wikipedia.org/wiki/The_') and 'The_Beatles' not in current and 'The_Who' not in current and 'The_Doors' not in current and 'The_Godfather' not in current)
            )
            if should_refresh:
                new_source = build_url(hobby, fact)
                if new_source and new_source != current:
                    fact['source'] = new_source
                    updated_facts += 1
                    changed = True
        if changed:
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
            updated_files += 1
    print(f'updated_files\t{updated_files}')
    print(f'updated_facts\t{updated_facts}')


if __name__ == '__main__':
    main()
