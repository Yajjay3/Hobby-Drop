from pathlib import Path
from urllib.parse import quote
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'


def wikiquote_url(name: str) -> str:
    return f"https://en.wikiquote.org/wiki/{quote(name.replace(' ', '_'))}"


def wiki_url(slug: str) -> str:
    return f"https://en.wikipedia.org/wiki/{slug}"


def possessive(name: str) -> str:
    return f"{name}'" if name.endswith('s') else f"{name}'s"


QUOTES = [
    ("Albert Einstein", "Imagination is more important than knowledge."),
    ("Isaac Newton", "If I have seen further it is by standing on the shoulders of giants."),
    ("Marie Curie", "Nothing in life is to be feared, it is only to be understood."),
    ("Galileo Galilei", "All truths are easy to understand once they are discovered."),
    ("Charles Darwin", "A man who dares to waste one hour of time has not discovered the value of life."),
    ("Franklin D. Roosevelt", "The only thing we have to fear is fear itself."),
    ("Abraham Lincoln", "Whatever you are, be a good one."),
    ("Theodore Roosevelt", "Do what you can, with what you have, where you are."),
    ("Eleanor Roosevelt", "No one can make you feel inferior without your consent."),
    ("Martin Luther King Jr.", "The time is always right to do what is right."),
    ("Nelson Mandela", "It always seems impossible until it's done."),
    ("Mahatma Gandhi", "Be the change that you wish to see in the world."),
    ("Maya Angelou", "If you don't like something, change it."),
    ("Helen Keller", "Life is either a daring adventure or nothing at all."),
    ("Amelia Earhart", "The most difficult thing is the decision to act."),
    ("Benjamin Franklin", "Well done is better than well said."),
    ("Thomas Edison", "Genius is one percent inspiration and ninety-nine percent perspiration."),
    ("Henry Ford", "Whether you think you can, or you think you can't — you're right."),
    ("Steve Jobs", "Stay hungry, stay foolish."),
    ("Walt Disney", "All our dreams can come true, if we have the courage to pursue them."),
    ("Fred Rogers", "Look for the helpers."),
    ("Jane Goodall", "What you do makes a difference, and you have to decide what kind of difference you want to make."),
    ("Carl Sagan", "Somewhere, something incredible is waiting to be known."),
    ("Stephen Hawking", "Intelligence is the ability to adapt to change."),
    ("Ralph Waldo Emerson", "Do not go where the path may lead, go instead where there is no path and leave a trail."),
    ("Socrates", "The unexamined life is not worth living."),
    ("Aristotle", "Knowing yourself is the beginning of all wisdom."),
    ("Lao Tzu", "A journey of a thousand miles begins with a single step."),
    ("Confucius", "It does not matter how slowly you go as long as you do not stop."),
    ("Marcus Aurelius", "The happiness of your life depends upon the quality of your thoughts."),
    ("Anne Frank", "How wonderful it is that nobody need wait a single moment before starting to improve the world."),
    ("Mother Teresa", "Peace begins with a smile."),
    ("Bruce Lee", "Be water, my friend."),
    ("Muhammad Ali", "Service to others is the rent you pay for your room here on Earth."),
    ("Dolly Parton", "If you don't like the road you're walking, start paving another one."),
    ("George Washington Carver", "Education is the key to unlock the golden door of freedom."),
    ("Harriet Tubman", "Every great dream begins with a dreamer."),
    ("Leonardo da Vinci", "Learning never exhausts the mind."),
    ("Winston Churchill", "Success is not final, failure is not fatal: it is the courage to continue that counts."),
    ("Babe Ruth", "Never let the fear of striking out keep you from playing the game."),
]

QUOTE_TEMPLATES = [
    lambda speaker, quote_text: f'"{quote_text}" — {speaker}',
    lambda speaker, quote_text: f'{speaker} said, "{quote_text}"',
    lambda speaker, quote_text: f'One of {possessive(speaker)} best-known lines is "{quote_text}"',
    lambda speaker, quote_text: f'"{quote_text}" is one of the lines people most associate with {speaker}.',
    lambda speaker, quote_text: f'Many quote collections highlight {possessive(speaker)} words: "{quote_text}"',
    lambda speaker, quote_text: f'{speaker} is often remembered for saying, "{quote_text}"',
    lambda speaker, quote_text: f'A well-known quote from {speaker} is "{quote_text}"',
    lambda speaker, quote_text: f'{possessive(speaker)} "{quote_text}" is still widely shared today.',
    lambda speaker, quote_text: f'Readers still turn to {speaker} for the line, "{quote_text}"',
    lambda speaker, quote_text: f'"{quote_text}" remains one of {possessive(speaker)} most recognizable sayings.',
]

SONGS = [
    ("The Beatles", "Hey Jude", "Hey Jude", "Hey_Jude"),
    ("The Beatles", "Let It Be", "Let It Be", "Let_It_Be_(song)"),
    ("The Beatles", "Here Comes the Sun", "Here Comes the Sun", "Here_Comes_the_Sun"),
    ("The Beatles", "Yesterday", "Yesterday", "Yesterday_(Beatles_song)"),
    ("John Lennon", "Imagine", "Imagine", "Imagine_(John_Lennon_song)"),
    ("Queen", "Bohemian Rhapsody", "Bohemian Rhapsody", "Bohemian_Rhapsody"),
    ("Eagles", "Hotel California", "Hotel California", "Hotel_California_(Eagles_song)"),
    ("Led Zeppelin", "Stairway to Heaven", "Stairway to Heaven", "Stairway_to_Heaven"),
    ("Bruce Springsteen", "Born to Run", "Born to Run", "Born_to_Run_(song)"),
    ("Lynyrd Skynyrd", "Free Bird", "Free Bird", "Free_Bird"),
    ("Dolly Parton", "Jolene", "Jolene", "Jolene"),
    ("Dolly Parton", "I Will Always Love You", "I Will Always Love You", "I_Will_Always_Love_You"),
    ("Johnny Cash", "Ring of Fire", "Ring of Fire", "Ring_of_Fire"),
    ("Bob Marley & The Wailers", "One Love", "One Love", "One_Love/People_Get_Ready"),
    ("Bob Marley & The Wailers", "No Woman, No Cry", "No Woman, No Cry", "No_Woman,_No_Cry"),
    ("Aretha Franklin", "Respect", "Respect", "Respect_(song)"),
    ("Prince", "Purple Rain", "Purple Rain", "Purple_Rain_(song)"),
    ("Michael Jackson", "Billie Jean", "Billie Jean", "Billie_Jean"),
    ("Madonna", "Like a Prayer", "Like a Prayer", "Like_a_Prayer_(song)"),
    ("ABBA", "Dancing Queen", "Dancing Queen", "Dancing_Queen"),
    ("Bee Gees", "Stayin' Alive", "Stayin' Alive", "Stayin'_Alive"),
    ("Bon Jovi", "Livin' on a Prayer", "Livin' on a Prayer", "Livin'_on_a_Prayer"),
    ("Guns N' Roses", "Sweet Child o' Mine", "Sweet Child o' Mine", "Sweet_Child_o'_Mine"),
    ("Journey", "Don't Stop Believin'", "Don't Stop Believin'", "Don't_Stop_Believin'"),
    ("U2", "With or Without You", "With or Without You", "With_or_Without_You"),
    ("The Police", "Every Breath You Take", "Every Breath You Take", "Every_Breath_You_Take"),
    ("Oasis", "Wonderwall", "Wonderwall", "Wonderwall_(song)"),
    ("Nirvana", "Smells Like Teen Spirit", "Smells Like Teen Spirit", "Smells_Like_Teen_Spirit"),
    ("R.E.M.", "Losing My Religion", "Losing My Religion", "Losing_My_Religion"),
    ("Blink-182", "All the Small Things", "All the Small Things", "All_the_Small_Things"),
    ("The Killers", "Mr. Brightside", "Mr. Brightside", "Mr._Brightside"),
    ("Kelly Clarkson", "Since U Been Gone", "Since U Been Gone", "Since_U_Been_Gone"),
    ("Adele", "Rolling in the Deep", "Rolling in the Deep", "Rolling_in_the_Deep"),
    ("Katy Perry", "Firework", "Firework", "Firework_(song)"),
    ("Taylor Swift", "Shake It Off", "Shake It Off", "Shake_It_Off"),
    ("Rihanna", "Umbrella", "Umbrella", "Umbrella_(song)"),
    ("Shakira", "Hips Don't Lie", "Hips Don't Lie", "Hips_Don't_Lie"),
    ("John Denver", "Take Me Home, Country Roads", "Country Roads", "Take_Me_Home,_Country_Roads"),
    ("Billy Joel", "Piano Man", "Piano Man", "Piano_Man_(song)"),
    ("Whitney Houston", "I Wanna Dance with Somebody", "I Wanna Dance with Somebody", "I_Wanna_Dance_with_Somebody_(Who_Loves_Me)"),
]

LYRIC_TEMPLATES = [
    lambda artist, song, hook: f'The title hook "{hook}" is one of the most recognizable parts of {possessive(artist)} "{song}".',
    lambda artist, song, hook: f'Fans often sing along the moment "{hook}" comes around in {possessive(artist)} "{song}".',
    lambda artist, song, hook: f'"{song}" by {artist} is closely tied to the repeated line "{hook}".',
    lambda artist, song, hook: f'One of the best-known moments in {possessive(artist)} "{song}" is the phrase "{hook}".',
    lambda artist, song, hook: f'The refrain "{hook}" helped make "{song}" easy for listeners to remember.',
    lambda artist, song, hook: f'Many listeners instantly connect "{hook}" with {possessive(artist)} "{song}".',
    lambda artist, song, hook: f'The repeated title line "{hook}" gives "{song}" much of its sing-along appeal.',
    lambda artist, song, hook: f'When people think of "{song}", the hook "{hook}" is often the first line they remember.',
    lambda artist, song, hook: f'A signature lyric moment in "{song}" is the phrase "{hook}".',
    lambda artist, song, hook: f'"{hook}" is the kind of chorus line that helped "{song}" stick in pop culture.',
]


def build_quotes_file():
    facts = []
    seen = set()
    for speaker, quote_text in QUOTES:
        source = wikiquote_url(speaker)
        for template in QUOTE_TEMPLATES:
            text = template(speaker, quote_text)
            if text not in seen:
                facts.append({
                    'text': text,
                    'type': 'quote',
                    'quoteBy': speaker,
                    'source': source,
                })
                seen.add(text)
    return {
        'hobby': 'Famous Quotes',
        'facts': facts[:380],
    }


def build_lyrics_file():
    facts = []
    seen = set()
    for artist, song, hook, slug in SONGS:
        source = wiki_url(slug)
        for template in LYRIC_TEMPLATES:
            text = template(artist, song, hook)
            if text not in seen:
                facts.append({
                    'text': text,
                    'type': 'lyric',
                    'isLyric': True,
                    'artist': artist,
                    'songTitle': song,
                    'source': source,
                })
                seen.add(text)
    return {
        'hobby': 'Song Lyrics',
        'facts': facts[:380],
    }


quotes_data = build_quotes_file()
lyrics_data = build_lyrics_file()

(BASE / 'famous-quotes.json').write_text(json.dumps(quotes_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
(BASE / 'song-lyrics.json').write_text(json.dumps(lyrics_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('famous-quotes', len(quotes_data['facts']))
print('song-lyrics', len(lyrics_data['facts']))
