from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    'science': {
        'hobby': 'Science',
        'entries': [
            ('Scientific method', 'The scientific method gives researchers a structured way to test ideas and examine evidence.', 'It became one of the core habits that helped science grow into a global process of discovery.', 'https://en.wikipedia.org/wiki/Scientific_method'),
            ('Periodic table', 'The periodic table organizes the chemical elements in a way that reveals repeating patterns in their behavior.', 'It remains one of the most recognizable visual tools in all of science.', 'https://en.wikipedia.org/wiki/Periodic_table'),
            ('DNA', 'DNA carries genetic information in living things and became one of the most important discoveries in modern science.', 'Its structure helped transform biology, medicine, and forensic work.', 'https://en.wikipedia.org/wiki/DNA'),
            ('Telescope', 'The telescope expanded human understanding of the universe by revealing distant objects in far more detail.', 'It became one of the most important instruments in the history of science.', 'https://en.wikipedia.org/wiki/Telescope'),
            ('Microscope', 'The microscope opened up entire hidden worlds by allowing people to study cells and tiny organisms.', 'Its use changed biology and medicine forever.', 'https://en.wikipedia.org/wiki/Microscope'),
            ('Albert Einstein', 'Albert Einstein became one of the most famous scientific thinkers of the modern era.', 'His work on relativity changed how people understand space, time, and gravity.', 'https://en.wikipedia.org/wiki/Albert_Einstein'),
            ('Marie Curie', 'Marie Curie became one of the most important pioneers in the study of radioactivity.', 'Her work made her one of the most celebrated scientists in history.', 'https://en.wikipedia.org/wiki/Marie_Curie'),
            ('Isaac Newton', 'Isaac Newton helped reshape science through his work on motion, gravity, and mathematics.', 'He remains one of the most influential figures in the history of physics.', 'https://en.wikipedia.org/wiki/Isaac_Newton'),
            ('Penicillin', 'The discovery of penicillin transformed medicine and became one of the great breakthroughs in scientific history.', 'Its use helped save countless lives by changing the treatment of infection.', 'https://en.wikipedia.org/wiki/Penicillin'),
            ('Hubble Space Telescope', 'The Hubble Space Telescope helped provide some of the most famous images ever associated with science.', 'Its observations deepened knowledge of galaxies, stars, and the age of the universe.', 'https://en.wikipedia.org/wiki/Hubble_Space_Telescope'),
        ],
    },
    'models': {
        'hobby': 'Fashion Models',
        'entries': [
            ('Supermodel', 'The term “supermodel” became a major part of fashion culture during the late 20th century.', 'It came to describe models whose fame extended well beyond the runway.', 'https://en.wikipedia.org/wiki/Supermodel'),
            ('Naomi Campbell', 'Naomi Campbell became one of the most famous fashion models in the world.', 'Her runway presence helped define the supermodel era.', 'https://en.wikipedia.org/wiki/Naomi_Campbell'),
            ('Cindy Crawford', 'Cindy Crawford became one of the signature faces of the supermodel era.', 'Her career helped connect modeling with mainstream media and advertising.', 'https://en.wikipedia.org/wiki/Cindy_Crawford'),
            ('Gisele Bündchen', 'Gisele Bündchen became one of the most recognizable fashion models of the 2000s.', 'Her success made her a global name in modeling and branding.', 'https://en.wikipedia.org/wiki/Gisele_B%C3%BCndchen'),
            ('Vogue', 'Vogue became one of the most important magazines in fashion and modeling culture.', 'Its covers and editorials helped shape model careers for generations.', 'https://en.wikipedia.org/wiki/Vogue_(magazine)'),
            ('Runway', 'Runway modeling became one of the defining ways fashion collections are presented to the public.', 'It remains one of the most visible parts of the modeling world.', 'https://en.wikipedia.org/wiki/Runway_(fashion)'),
            ('Fashion week', 'Fashion weeks in cities such as Paris, Milan, London, and New York became central events in the modeling calendar.', 'They are where many of the most influential runway moments take place.', 'https://en.wikipedia.org/wiki/Fashion_week'),
            ('Modeling agency', 'Modeling agencies help represent talent, book jobs, and shape careers in the fashion industry.', 'They became one of the key structures behind how the modeling world operates.', 'https://en.wikipedia.org/wiki/Modeling_agency'),
            ('Tyra Banks', 'Tyra Banks became known both for modeling success and for bringing fashion culture to a wider TV audience.', 'Her career helped connect runway fame with mainstream entertainment.', 'https://en.wikipedia.org/wiki/Tyra_Banks'),
            ('Kate Moss', 'Kate Moss became one of the most talked-about and influential fashion models of the 1990s and 2000s.', 'Her image helped shape changing trends in fashion photography and style.', 'https://en.wikipedia.org/wiki/Kate_Moss'),
        ],
    },
    'academy-awards': {
        'hobby': 'Academy Awards',
        'entries': [
            ('Academy Awards', 'The Academy Awards, often called the Oscars, became one of the most famous honors in the film industry.', 'Their annual ceremony turned into one of Hollywood’s biggest nights.', 'https://en.wikipedia.org/wiki/Academy_Awards'),
            ('Best Picture', 'Best Picture is one of the most closely watched categories at the Academy Awards.', 'Winning it often cements a film’s place in movie history.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'),
            ('Best Actor', 'The Academy Award for Best Actor honors one of the top leading performances of the year.', 'It remains one of the ceremony’s most discussed awards.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor'),
            ('Best Actress', 'The Academy Award for Best Actress recognizes a leading performance judged among the year’s strongest.', 'It is one of the core acting prizes of the Oscars.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actress'),
            ('Best Director', 'The Best Director Oscar often highlights the creative vision behind a major film achievement.', 'It became one of the most prestigious categories in the ceremony.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director'),
            ('Dolby Theatre', 'The Dolby Theatre in Hollywood has served as the modern home of the Academy Awards ceremony.', 'Its red carpet and stage became strongly tied to Oscar night imagery.', 'https://en.wikipedia.org/wiki/Dolby_Theatre'),
            ('Academy of Motion Picture Arts and Sciences', 'The Academy of Motion Picture Arts and Sciences organizes the Oscars and plays a major role in film recognition.', 'Its membership votes on many of the awards presented each year.', 'https://en.wikipedia.org/wiki/Academy_of_Motion_Picture_Arts_and_Sciences'),
            ('Oscar statuette', 'The Oscar statuette became one of the most recognizable trophies in entertainment.', 'Its design helped turn the award itself into a pop-culture symbol.', 'https://en.wikipedia.org/wiki/Academy_Awards#Oscar_statuette'),
            ('Red carpet', 'The Oscars red carpet became a major event for fashion, interviews, and celebrity attention before the ceremony begins.', 'It turned the lead-up to the awards into a cultural event of its own.', 'https://en.wikipedia.org/wiki/Red_carpet'),
            ('Best Original Song', 'Best Original Song celebrates music written specifically for a film.', 'It often creates some of the most memorable live performances during the Academy Awards telecast.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Original_Song'),
        ],
    },
    'comic-books': {
        'hobby': 'Comic Books',
        'entries': [
            ('Marvel Comics', 'Marvel Comics became one of the biggest names in the history of comic books.', 'Its heroes and shared universe helped shape modern superhero storytelling.', 'https://en.wikipedia.org/wiki/Marvel_Comics'),
            ('DC Comics', 'DC Comics helped define the superhero genre with some of the medium’s most famous characters.', 'Its long history made it central to comic-book culture.', 'https://en.wikipedia.org/wiki/DC_Comics'),
            ('Action Comics', 'Action Comics is one of the most famous comic-book titles ever published, especially because of Superman’s early appearances.', 'It remains a landmark name in the history of the medium.', 'https://en.wikipedia.org/wiki/Action_Comics'),
            ('Stan Lee', 'Stan Lee became one of the most recognizable creative figures associated with comic books.', 'His writing, editing, and public persona helped popularize the medium worldwide.', 'https://en.wikipedia.org/wiki/Stan_Lee'),
            ('Jack Kirby', 'Jack Kirby became one of the most influential artists and creators in comic-book history.', 'His visual imagination helped define countless characters and worlds.', 'https://en.wikipedia.org/wiki/Jack_Kirby'),
            ('Graphic novel', 'Graphic novels helped expand how readers and critics think about comics as a storytelling form.', 'The format became a major gateway for new audiences entering comic culture.', 'https://en.wikipedia.org/wiki/Graphic_novel'),
            ('Comic strip', 'Comic strips brought illustrated storytelling into newspapers and daily life long before superhero comics dominated the medium.', 'They remain an important branch of comic-book and comics history.', 'https://en.wikipedia.org/wiki/Comic_strip'),
            ('Manga', 'Manga became one of the most influential comic traditions in the world.', 'Its storytelling and art styles helped shape global comics culture beyond Japan.', 'https://en.wikipedia.org/wiki/Manga'),
            ('Comic-Con', 'Comic-Con conventions became major gathering places for comic-book fans, creators, and pop-culture communities.', 'They helped turn comics fandom into a large public event scene.', 'https://en.wikipedia.org/wiki/Comic-Con'),
            ('Golden Age of Comic Books', 'The Golden Age of Comic Books helped establish the superhero boom in American publishing.', 'It remains one of the most important eras in the history of the medium.', 'https://en.wikipedia.org/wiki/Golden_Age_of_Comic_Books'),
        ],
    },
    'dancing': {
        'hobby': 'Dancing',
        'entries': [
            ('Ballet', 'Ballet became one of the most formalized and internationally recognized dance traditions.', 'Its technique and stage history made it central to many conversations about dance.', 'https://en.wikipedia.org/wiki/Ballet'),
            ('Salsa', 'Salsa dancing became one of the most recognizable partner dance styles in the world.', 'Its rhythm and social energy helped it spread far beyond its original communities.', 'https://en.wikipedia.org/wiki/Salsa_(dance)'),
            ('Hip-hop dance', 'Hip-hop dance grew from street and club culture into one of the most influential modern dance styles.', 'Its movement vocabulary became central to music videos and live performance.', 'https://en.wikipedia.org/wiki/Hip-hop_dance'),
            ('Ballroom dance', 'Ballroom dance includes a range of partner styles performed socially and competitively.', 'It remains one of the best-known dance categories around the world.', 'https://en.wikipedia.org/wiki/Ballroom_dance'),
            ('Tap dance', 'Tap dance turned rhythm made by the feet into a major performance art form.', 'Its sound and speed made it one of the most distinctive styles in dance history.', 'https://en.wikipedia.org/wiki/Tap_dance'),
            ('Breakdancing', 'Breakdancing, or breaking, became one of the most recognizable street dance forms in global culture.', 'Its athletic moves helped make it a standout style in dance competition and pop culture.', 'https://en.wikipedia.org/wiki/Breakdancing'),
            ('Modern dance', 'Modern dance developed as a break from some of the rules of classical ballet.', 'It helped open up new expressive possibilities in stage movement.', 'https://en.wikipedia.org/wiki/Modern_dance'),
            ('Tango', 'Tango became one of the most famous partner dances in the world.', 'Its close hold, dramatic style, and music gave it a powerful place in dance culture.', 'https://en.wikipedia.org/wiki/Tango'),
            ('Waltz', 'The waltz became one of the classic partner dances associated with ballroom culture.', 'Its turning motion made it especially memorable in both social and formal dance settings.', 'https://en.wikipedia.org/wiki/Waltz'),
            ('Choreography', 'Choreography is the art of designing and arranging movement for dance performance.', 'It helps turn dance ideas into repeatable works on stage or screen.', 'https://en.wikipedia.org/wiki/Choreography'),
        ],
    },
    'mythology': {
        'hobby': 'Mythology',
        'entries': [
            ('Greek mythology', 'Greek mythology became one of the most widely studied and retold myth traditions in the world.', 'Its gods, heroes, and monsters shaped literature, art, and storytelling for centuries.', 'https://en.wikipedia.org/wiki/Greek_mythology'),
            ('Norse mythology', 'Norse mythology includes well-known figures such as Odin, Thor, and Loki.', 'Its stories helped shape modern fantasy and pop culture in major ways.', 'https://en.wikipedia.org/wiki/Norse_mythology'),
            ('Zeus', 'Zeus became one of the best-known gods in Greek mythology.', 'His role as ruler of the Olympians made him central to many mythic stories.', 'https://en.wikipedia.org/wiki/Zeus'),
            ('Athena', 'Athena is one of the most famous figures in Greek mythology, associated with wisdom and strategy.', 'She remained central to many classical myths and symbols.', 'https://en.wikipedia.org/wiki/Athena'),
            ('Odin', 'Odin became one of the leading gods in Norse mythology and one of the tradition’s most recognizable figures.', 'His role in wisdom, battle, and kingship helped keep his stories important across centuries.', 'https://en.wikipedia.org/wiki/Odin'),
            ('Thor', 'Thor became one of the most famous gods in Norse mythology thanks to his hammer and storm-related power.', 'He stayed prominent in both old legend and modern adaptation.', 'https://en.wikipedia.org/wiki/Thor'),
            ('Anubis', 'Anubis became one of the best-known deities associated with ancient Egyptian mythology.', 'His connection to the dead and the afterlife made him especially memorable.', 'https://en.wikipedia.org/wiki/Anubis'),
            ('Creation myth', 'Creation myths explain how the world, humanity, or the gods came into being in different traditions.', 'They are some of the most foundational stories in mythology.', 'https://en.wikipedia.org/wiki/Creation_myth'),
            ('Hero\'s journey', 'The hero’s journey became a popular way to describe mythic storytelling patterns across cultures.', 'It is often used to connect mythology with modern narrative structure.', 'https://en.wikipedia.org/wiki/Hero%27s_journey'),
            ('Mythological creature', 'Mythological creatures such as dragons, giants, and sea monsters helped make mythology vivid and memorable.', 'These beings remain some of the most recognizable parts of myth traditions.', 'https://en.wikipedia.org/wiki/Legendary_creature'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f'{subject} is one of the standout topics people often explore within {hobby}.',
    lambda subject, detail, extra, hobby: f'Readers interested in {hobby} regularly come across {subject}.',
    lambda subject, detail, extra, hobby: f'Learning about {subject} helps explain part of the lasting appeal of {hobby}.',
    lambda subject, detail, extra, hobby: f'{subject} remains one of the most recognizable examples connected with {hobby}.',
    lambda subject, detail, extra, hobby: f'Articles, documentaries, and fan discussions about {hobby} often highlight {subject}.',
    lambda subject, detail, extra, hobby: f'For many people, {subject} is a memorable entry point into {hobby}.',
    lambda subject, detail, extra, hobby: f'The story of {subject} helps show why {hobby} stays so interesting to revisit.',
    lambda subject, detail, extra, hobby: f'{subject} is frequently mentioned in guides and retrospectives about {hobby}.',
    lambda subject, detail, extra, hobby: f'One reason {hobby} feels rich and memorable is the presence of touchpoints like {subject}.',
    lambda subject, detail, extra, hobby: f'{subject} still stands out as a classic reference point within {hobby}.',
]

for file_key, config in BATCH.items():
    path = BASE / f'{file_key}.json'
    current = json.loads(path.read_text(encoding='utf-8'))
    current.setdefault('hobby', config['hobby'])
    current.setdefault('facts', [])
    existing_texts = {fact.get('text') for fact in current['facts']}

    for subject, detail, extra, source in config['entries']:
        for template in TEMPLATES:
            text = template(subject, detail, extra, config['hobby'])
            if text not in existing_texts:
                current['facts'].append({
                    'text': text,
                    'source': source,
                })
                existing_texts.add(text)

    path.write_text(json.dumps(current, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{file_key}\t{len(current["facts"])} facts')
