from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    'geography': {
        'hobby': 'Geography',
        'entries': [
            ('Equator', 'The Equator divides Earth into the Northern and Southern Hemispheres and is one of the key reference lines in geography.', 'Many world geography lessons begin with the Equator because it helps explain climate zones and latitude.', 'https://en.wikipedia.org/wiki/Equator'),
            ('Prime Meridian', 'The Prime Meridian serves as the starting point for measuring longitude and time around the globe.', 'It became one of the central reference lines used in mapping and navigation.', 'https://en.wikipedia.org/wiki/Prime_meridian'),
            ('Time zones', 'Time zones help organize the world into regions that keep similar clock times despite Earth’s rotation.', 'They show how geography affects daily life, travel, and communication.', 'https://en.wikipedia.org/wiki/Time_zone'),
            ('Archipelago', 'An archipelago is a chain or group of islands, and many famous regions of the world fit that description.', 'Studying archipelagos helps explain trade, settlement, and coastal culture.', 'https://en.wikipedia.org/wiki/Archipelago'),
            ('Atlas', 'An atlas is a collection of maps that helps people compare places, borders, landforms, and routes.', 'Atlases became one of the most familiar tools for learning world geography.', 'https://en.wikipedia.org/wiki/Atlas'),
            ('Volcano', 'Volcanoes help shape landscapes and are one of the most dramatic features studied in physical geography.', 'They connect geography with tectonic activity, hazards, and fertile land.', 'https://en.wikipedia.org/wiki/Volcano'),
            ('River delta', 'A river delta forms where a river slows and deposits sediment near a larger body of water.', 'Deltas often became major centers of farming, trade, and settlement.', 'https://en.wikipedia.org/wiki/River_delta'),
            ('Continents', 'The continents are one of the most basic ways people organize and study the surface of Earth.', 'Even the number and definition of continents can vary by educational tradition.', 'https://en.wikipedia.org/wiki/Continent'),
        ],
    },
    'asia': {
        'hobby': 'Asia',
        'entries': [
            ('Himalayas', 'The Himalayas stretch across Asia and include some of the highest mountains on Earth.', 'They strongly shaped climate, travel, and settlement across the continent.', 'https://en.wikipedia.org/wiki/Himalayas'),
            ('Silk Road', 'The Silk Road connected major parts of Asia with Europe and Africa through trade and cultural exchange.', 'It helped move goods, beliefs, and technologies across enormous distances.', 'https://en.wikipedia.org/wiki/Silk_Road'),
            ('Gobi Desert', 'The Gobi Desert is one of Asia’s great deserts and spans parts of northern China and Mongolia.', 'Its landscape makes it one of the most recognizable geographic regions in Asia.', 'https://en.wikipedia.org/wiki/Gobi_Desert'),
            ('Mekong River', 'The Mekong River supports millions of people across mainland Southeast Asia.', 'It is one of the most important waterways in the region for food and transport.', 'https://en.wikipedia.org/wiki/Mekong'),
            ('South Asia', 'South Asia includes countries such as India, Pakistan, Bangladesh, Nepal, and Sri Lanka.', 'It is one of the most densely populated and culturally rich regions in the world.', 'https://en.wikipedia.org/wiki/South_Asia'),
            ('East Asia', 'East Asia includes countries such as China, Japan, and the Koreas and has long been a major center of world civilization.', 'Its history, economies, and cities made it one of the most influential regions in the modern world.', 'https://en.wikipedia.org/wiki/East_Asia'),
            ('Southeast Asia', 'Southeast Asia is known for its island chains, tropical climate, trade history, and cultural diversity.', 'It links the Indian and Pacific Oceans through some of the world’s busiest sea routes.', 'https://en.wikipedia.org/wiki/Southeast_Asia'),
            ('Monsoon', 'Monsoon patterns affect weather, farming, and daily life in large parts of Asia every year.', 'They are one of the most important seasonal forces shaping the continent.', 'https://en.wikipedia.org/wiki/Monsoon'),
        ],
    },
    'egypt': {
        'hobby': 'Egypt',
        'entries': [
            ('Nile River', 'The Nile River made large-scale settlement in Egypt possible and remains central to the country’s geography.', 'For thousands of years, Egyptian life depended on the Nile’s water and fertile floodplain.', 'https://en.wikipedia.org/wiki/Nile'),
            ('Cairo', 'Cairo is Egypt’s capital and one of the largest cities in Africa and the Middle East.', 'Its size, history, and culture make it one of the best-known cities in the region.', 'https://en.wikipedia.org/wiki/Cairo'),
            ('Pyramids of Giza', 'The Pyramids of Giza are among the most famous structures ever built in Egypt.', 'They remain one of the most recognizable landmarks on Earth.', 'https://en.wikipedia.org/wiki/Giza_pyramid_complex'),
            ('Suez Canal', 'The Suez Canal links the Mediterranean Sea to the Red Sea and is one of the world’s most important shipping routes.', 'Its location gave Egypt major strategic importance in global trade.', 'https://en.wikipedia.org/wiki/Suez_Canal'),
            ('Alexandria', 'Alexandria became one of the most important cities of the ancient Mediterranean world.', 'It remained a major Egyptian port and cultural center long after its founding.', 'https://en.wikipedia.org/wiki/Alexandria'),
            ('Valley of the Kings', 'The Valley of the Kings became the burial site for many pharaohs of ancient Egypt.', 'It is one of the most famous archaeological regions in the country.', 'https://en.wikipedia.org/wiki/Valley_of_the_Kings'),
            ('Abu Simbel', 'Abu Simbel is known for its massive rock-cut temples built during the reign of Ramesses II.', 'The site became famous again in modern times after a huge relocation project saved it from flooding.', 'https://en.wikipedia.org/wiki/Abu_Simbel'),
            ('Sahara', 'Egypt occupies part of the Sahara, the largest hot desert on Earth.', 'This desert setting makes the Nile corridor even more important in Egyptian geography.', 'https://en.wikipedia.org/wiki/Sahara'),
        ],
    },
    'europe': {
        'hobby': 'Europe',
        'entries': [
            ('Alps', 'The Alps are one of Europe’s great mountain systems and stretch across several countries.', 'They shape weather, tourism, transport, and regional culture across the continent.', 'https://en.wikipedia.org/wiki/Alps'),
            ('Danube', 'The Danube River flows through more countries than any other river in Europe.', 'It helped connect central and eastern parts of the continent for centuries.', 'https://en.wikipedia.org/wiki/Danube'),
            ('European Union', 'The European Union became one of the most important political and economic groupings in modern Europe.', 'Its member states cooperate across trade, travel, and shared policy.', 'https://en.wikipedia.org/wiki/European_Union'),
            ('Mediterranean Sea', 'The Mediterranean Sea links southern Europe with North Africa and the Middle East.', 'Its coastlines shaped trade, empire, and travel for thousands of years.', 'https://en.wikipedia.org/wiki/Mediterranean_Sea'),
            ('Renaissance', 'The Renaissance began in Europe and transformed art, learning, and intellectual life.', 'It became one of the most influential cultural movements in world history.', 'https://en.wikipedia.org/wiki/Renaissance'),
            ('Balkans', 'The Balkans are one of Europe’s most historically complex and culturally varied regions.', 'Their geography helped shape trade routes, conflicts, and identities over time.', 'https://en.wikipedia.org/wiki/Balkans'),
            ('Nordic countries', 'The Nordic countries are often grouped together because of geography, culture, and shared historical ties.', 'They are frequently highlighted in discussions of northern Europe.', 'https://en.wikipedia.org/wiki/Nordic_countries'),
            ('Gothic architecture', 'Gothic architecture became one of the most recognizable building styles in medieval Europe.', 'Its cathedrals, arches, and stained glass still define many European cityscapes.', 'https://en.wikipedia.org/wiki/Gothic_architecture'),
        ],
    },
    'greece': {
        'hobby': 'Greece',
        'entries': [
            ('Acropolis of Athens', 'The Acropolis of Athens is one of the most famous ancient sites in Greece.', 'It stands as a lasting symbol of Greek history, architecture, and civic life.', 'https://en.wikipedia.org/wiki/Acropolis_of_Athens'),
            ('Parthenon', 'The Parthenon became one of the defining monuments of classical Greece.', 'Its design still influences how people imagine ancient Greek architecture.', 'https://en.wikipedia.org/wiki/Parthenon'),
            ('Aegean Sea', 'The Aegean Sea links many of Greece’s islands with the mainland.', 'Its waters helped shape Greek trade, travel, and identity for centuries.', 'https://en.wikipedia.org/wiki/Aegean_Sea'),
            ('Athens', 'Athens is Greece’s capital and one of the world’s most historically important cities.', 'It is central to conversations about democracy, philosophy, and classical civilization.', 'https://en.wikipedia.org/wiki/Athens'),
            ('Olympia', 'Olympia was the ancient site of the Olympic Games in Greece.', 'It became one of the best-known places in the history of sport and religion.', 'https://en.wikipedia.org/wiki/Olympia,_Greece'),
            ('Delphi', 'Delphi was famous in the ancient Greek world for its sanctuary and oracle.', 'It remained one of the most important sacred sites in Greek history.', 'https://en.wikipedia.org/wiki/Delphi'),
            ('Crete', 'Crete is Greece’s largest island and was home to the ancient Minoan civilization.', 'Its long history makes it one of the most important islands in the eastern Mediterranean.', 'https://en.wikipedia.org/wiki/Crete'),
            ('Santorini', 'Santorini became world-famous for its dramatic cliffs, white buildings, and volcanic setting.', 'It is one of the Greek islands most often associated with travel photography and tourism.', 'https://en.wikipedia.org/wiki/Santorini'),
        ],
    },
    'india': {
        'hobby': 'India',
        'entries': [
            ('Ganges', 'The Ganges is one of the most important rivers in India for both daily life and religious tradition.', 'It is often one of the first landmarks people associate with the geography of India.', 'https://en.wikipedia.org/wiki/Ganges'),
            ('Taj Mahal', 'The Taj Mahal is one of the most famous monuments in India and a symbol recognized around the world.', 'Its architecture and story made it one of the best-known landmarks in South Asia.', 'https://en.wikipedia.org/wiki/Taj_Mahal'),
            ('Indian monsoon', 'The Indian monsoon plays a major role in agriculture, water supply, and seasonal life across the country.', 'It is one of the biggest climate patterns shaping India each year.', 'https://en.wikipedia.org/wiki/Monsoon_of_South_Asia'),
            ('Bollywood', 'Bollywood became one of the most influential and widely recognized film industries in the world.', 'It is often used as a shorthand reference for the global reach of Indian cinema.', 'https://en.wikipedia.org/wiki/Hindi_cinema'),
            ('Himalayas', 'Northern India shares part of the Himalayan mountain system, one of the most dramatic landscapes on Earth.', 'These mountains affect weather, borders, travel, and cultural history.', 'https://en.wikipedia.org/wiki/Himalayas'),
            ('Jaipur', 'Jaipur is one of India’s most famous historic cities and is often called the Pink City.', 'It stands out for its planned layout, forts, and architecture.', 'https://en.wikipedia.org/wiki/Jaipur'),
            ('Indian Railways', 'Indian Railways is one of the largest rail networks in the world.', 'Its scale makes it a major part of how people understand travel and infrastructure in India.', 'https://en.wikipedia.org/wiki/Indian_Railways'),
            ('Constitution of India', 'The Constitution of India created the framework for the world’s largest democracy.', 'It remains one of the most important documents in modern Indian political life.', 'https://en.wikipedia.org/wiki/Constitution_of_India'),
        ],
    },
    'italy': {
        'hobby': 'Italy',
        'entries': [
            ('Rome', 'Rome is Italy’s capital and one of the most historically influential cities in the world.', 'Its ancient ruins and public spaces make it central to the story of Italy.', 'https://en.wikipedia.org/wiki/Rome'),
            ('Venice', 'Venice is famous for its canals, bridges, and long history as a maritime republic.', 'It became one of the most distinctive and recognizable cities in Italy.', 'https://en.wikipedia.org/wiki/Venice'),
            ('Colosseum', 'The Colosseum remains one of Italy’s best-known monuments from the Roman world.', 'It is often one of the first landmarks people think of when they picture Italy.', 'https://en.wikipedia.org/wiki/Colosseum'),
            ('Florence', 'Florence played a major role in the Renaissance and in the history of Italian art.', 'Its museums and architecture make it one of Italy’s most important cultural cities.', 'https://en.wikipedia.org/wiki/Florence'),
            ('Vatican City', 'Vatican City sits inside Rome and is the center of the Roman Catholic Church.', 'Its tiny size contrasts with its enormous religious and cultural influence.', 'https://en.wikipedia.org/wiki/Vatican_City'),
            ('Pompeii', 'Pompeii became world-famous after being preserved by the eruption of Mount Vesuvius.', 'Its remains offer one of the clearest looks at everyday life in the ancient Roman world.', 'https://en.wikipedia.org/wiki/Pompeii'),
            ('Sicily', 'Sicily is the largest island in the Mediterranean and has a long history of cultural exchange.', 'Its position helped make it a crossroads of trade and empire.', 'https://en.wikipedia.org/wiki/Sicily'),
            ('Milan', 'Milan is one of Italy’s leading cities for business, fashion, and design.', 'It is often highlighted as a major modern counterpoint to the country’s older historic centers.', 'https://en.wikipedia.org/wiki/Milan'),
        ],
    },
    'japan': {
        'hobby': 'Japan',
        'entries': [
            ('Shinkansen', 'Japan’s Shinkansen became one of the world’s most famous high-speed rail systems.', 'It is often used as an example of efficient transport and technological ambition.', 'https://en.wikipedia.org/wiki/Shinkansen'),
            ('Mount Fuji', 'Mount Fuji is one of the most recognizable natural landmarks in Japan.', 'Its shape and cultural significance made it a lasting national symbol.', 'https://en.wikipedia.org/wiki/Mount_Fuji'),
            ('Kyoto', 'Kyoto is known for temples, shrines, gardens, and long-standing cultural traditions in Japan.', 'It is often highlighted as one of the country’s great historic cities.', 'https://en.wikipedia.org/wiki/Kyoto'),
            ('Tokyo', 'Tokyo is Japan’s capital and one of the largest metropolitan areas in the world.', 'Its scale and energy make it central to modern images of Japan.', 'https://en.wikipedia.org/wiki/Tokyo'),
            ('Cherry blossom', 'Cherry blossom season became one of the most beloved and recognizable traditions in Japan.', 'The yearly bloom is closely tied to travel, art, and seasonal celebration.', 'https://en.wikipedia.org/wiki/Cherry_blossom'),
            ('Tea ceremony', 'The Japanese tea ceremony emphasizes ritual, hospitality, and attention to detail.', 'It became one of the best-known examples of Japanese cultural practice.', 'https://en.wikipedia.org/wiki/Japanese_tea_ceremony'),
            ('Hokkaido', 'Hokkaido stands out in Japan for its northern location, climate, and landscapes.', 'It is often noted for winter sports, national parks, and regional identity.', 'https://en.wikipedia.org/wiki/Hokkaido'),
            ('Osaka', 'Osaka is one of Japan’s major cities and is known for commerce, food, and lively urban culture.', 'It plays a major role in the country’s economic and cultural life.', 'https://en.wikipedia.org/wiki/Osaka'),
        ],
    },
    'roman-history': {
        'hobby': 'Roman History',
        'entries': [
            ('Roman Republic', 'The Roman Republic shaped ideas about citizenship, law, and government before the empire took over.', 'Its institutions remain a major topic in the study of Roman history.', 'https://en.wikipedia.org/wiki/Roman_Republic'),
            ('Julius Caesar', 'Julius Caesar became one of the most famous figures in Roman history through war, politics, and reform.', 'His assassination marked one of the great turning points in the Roman world.', 'https://en.wikipedia.org/wiki/Julius_Caesar'),
            ('Augustus', 'Augustus became Rome’s first emperor and helped establish the long-lasting imperial system.', 'His reign is often treated as the start of the Roman Empire in its full form.', 'https://en.wikipedia.org/wiki/Augustus'),
            ('Colosseum', 'The Colosseum became one of the great public monuments of the Roman Empire.', 'It still serves as one of the most famous reminders of Roman engineering and spectacle.', 'https://en.wikipedia.org/wiki/Colosseum'),
            ('Roman roads', 'Roman roads helped armies, merchants, and officials move efficiently across the empire.', 'Their scale made them one of the great infrastructure achievements of Roman history.', 'https://en.wikipedia.org/wiki/Roman_roads'),
            ('Aqueduct', 'Roman aqueducts moved water over long distances and became a hallmark of Roman engineering.', 'They allowed cities to grow with a more reliable water supply.', 'https://en.wikipedia.org/wiki/Roman_aqueduct'),
            ('Hadrian’s Wall', 'Hadrian’s Wall marked a major frontier of Roman Britain.', 'It remains one of the most famous Roman construction projects in northern Europe.', 'https://en.wikipedia.org/wiki/Hadrian%27s_Wall'),
            ('Pax Romana', 'The Pax Romana describes a long period of relative peace and stability under Roman rule.', 'It is often used to explain how the empire could expand and connect such wide territories.', 'https://en.wikipedia.org/wiki/Pax_Romana'),
        ],
    },
    'law': {
        'hobby': 'Law & Justice',
        'entries': [
            ('Magna Carta', 'Magna Carta became one of the most famous documents in the history of law and constitutional government.', 'It is often cited when discussing limits on power and the rule of law.', 'https://en.wikipedia.org/wiki/Magna_Carta'),
            ('Common law', 'Common law developed through court decisions and precedent rather than through one single legal code.', 'It became one of the major legal traditions used in several countries.', 'https://en.wikipedia.org/wiki/Common_law'),
            ('Civil law', 'Civil law systems rely heavily on written legal codes and are widely used around the world.', 'They form one of the major legal traditions studied in comparative law.', 'https://en.wikipedia.org/wiki/Civil_law_(legal_system)'),
            ('Due process', 'Due process protects fair treatment through the normal legal system, especially in criminal and constitutional cases.', 'It is one of the core concepts people learn when studying rights and justice.', 'https://en.wikipedia.org/wiki/Due_process'),
            ('Jury trial', 'A jury trial allows ordinary citizens to play a direct role in deciding legal disputes or criminal guilt.', 'It remains one of the best-known features of some legal systems.', 'https://en.wikipedia.org/wiki/Jury_trial'),
            ('Precedent', 'Legal precedent means earlier court decisions can guide later cases with similar issues.', 'This idea became central in many systems influenced by common law.', 'https://en.wikipedia.org/wiki/Precedent'),
            ('Supreme Court', 'Supreme courts often sit at the top of a country’s legal system and make major constitutional decisions.', 'They are frequently at the center of public debates about law and rights.', 'https://en.wikipedia.org/wiki/Supreme_court'),
            ('Separation of powers', 'Separation of powers divides government authority among branches so no single part controls everything.', 'It is one of the most important ideas in constitutional law.', 'https://en.wikipedia.org/wiki/Separation_of_powers'),
        ],
    },
    'egyptian-history': {
        'hobby': 'Egyptian History',
        'entries': [
            ('Tutankhamun', 'Tutankhamun became one of the most famous pharaohs after his tomb was discovered largely intact in 1922.', 'His burial treasures helped spark worldwide fascination with Egyptian history.', 'https://en.wikipedia.org/wiki/Tutankhamun'),
            ('Cleopatra', 'Cleopatra VII became one of the most famous rulers associated with the end of ancient Egyptian independence.', 'Her life linked Egyptian history with the Roman world in dramatic fashion.', 'https://en.wikipedia.org/wiki/Cleopatra'),
            ('Hieroglyphs', 'Hieroglyphs were one of the writing systems used in ancient Egypt.', 'They remain one of the most recognizable symbols of Egyptian civilization.', 'https://en.wikipedia.org/wiki/Egyptian_hieroglyphs'),
            ('Rosetta Stone', 'The Rosetta Stone helped scholars decode ancient Egyptian writing in the modern era.', 'Its discovery changed the study of Egyptian history forever.', 'https://en.wikipedia.org/wiki/Rosetta_Stone'),
            ('Hatshepsut', 'Hatshepsut was one of the most successful female pharaohs in ancient Egyptian history.', 'Her reign is often highlighted for trade, building, and political authority.', 'https://en.wikipedia.org/wiki/Hatshepsut'),
            ('Ramesses II', 'Ramesses II became one of the most famous and long-ruling pharaohs of ancient Egypt.', 'His building projects and military reputation kept his name prominent for centuries.', 'https://en.wikipedia.org/wiki/Ramesses_II'),
            ('Book of the Dead', 'The Book of the Dead was a collection of funerary texts used to help guide the dead in the afterlife.', 'It remains one of the best-known parts of ancient Egyptian belief.', 'https://en.wikipedia.org/wiki/Book_of_the_Dead'),
            ('Old Kingdom', 'The Old Kingdom is often called the Age of the Pyramids in ancient Egyptian history.', 'It included the period when some of Egypt’s most famous monuments were built.', 'https://en.wikipedia.org/wiki/Old_Kingdom_of_Egypt'),
        ],
    },
    'wars': {
        'hobby': 'Wars & Battles',
        'entries': [
            ('World War I', 'World War I reshaped borders, empires, and international politics in the early 20th century.', 'Its trench warfare and alliances made it one of the most studied conflicts in history.', 'https://en.wikipedia.org/wiki/World_War_I'),
            ('World War II', 'World War II became the largest and deadliest conflict in modern history.', 'Its global scale changed technology, diplomacy, and political power around the world.', 'https://en.wikipedia.org/wiki/World_War_II'),
            ('Battle of Gettysburg', 'The Battle of Gettysburg is often treated as one of the turning points of the American Civil War.', 'It became one of the most famous battles ever fought on U.S. soil.', 'https://en.wikipedia.org/wiki/Battle_of_Gettysburg'),
            ('D-Day', 'D-Day marked the Allied landings in Normandy during World War II.', 'It remains one of the best-known military operations in modern history.', 'https://en.wikipedia.org/wiki/Normandy_landings'),
            ('Napoleonic Wars', 'The Napoleonic Wars spread conflict across much of Europe in the early 1800s.', 'They reshaped borders and helped define the modern era of European warfare.', 'https://en.wikipedia.org/wiki/Napoleonic_Wars'),
            ('Battle of Midway', 'The Battle of Midway became one of the most important naval battles in the Pacific during World War II.', 'It is often described as a strategic turning point against Japan.', 'https://en.wikipedia.org/wiki/Battle_of_Midway'),
            ('Treaty of Versailles', 'The Treaty of Versailles formally ended World War I but left behind major tensions.', 'It is often discussed as a key factor in the unstable years that followed.', 'https://en.wikipedia.org/wiki/Treaty_of_Versailles'),
            ('Civil War', 'The American Civil War became one of the most transformative conflicts in United States history.', 'It decided the future of the Union and the end of slavery in the country.', 'https://en.wikipedia.org/wiki/American_Civil_War'),
        ],
    },
    'presidents': {
        'hobby': 'U.S. Presidents',
        'entries': [
            ('George Washington', 'George Washington became the first president of the United States and helped define the office.', 'Many early traditions of the presidency took shape during his administration.', 'https://en.wikipedia.org/wiki/George_Washington'),
            ('Abraham Lincoln', 'Abraham Lincoln led the country during the Civil War and is one of the most studied presidents in U.S. history.', 'His presidency is closely linked to the preservation of the Union and emancipation.', 'https://en.wikipedia.org/wiki/Abraham_Lincoln'),
            ('Theodore Roosevelt', 'Theodore Roosevelt became known for energy, reform, and conservation during his presidency.', 'He remains one of the most recognizable figures in the history of the office.', 'https://en.wikipedia.org/wiki/Theodore_Roosevelt'),
            ('Franklin D. Roosevelt', 'Franklin D. Roosevelt guided the United States through the Great Depression and most of World War II.', 'He was elected four times, more than any other U.S. president.', 'https://en.wikipedia.org/wiki/Franklin_D._Roosevelt'),
            ('John F. Kennedy', 'John F. Kennedy remains one of the most discussed presidents of the television era.', 'His presidency is closely tied to the space race, Cold War tension, and public image.', 'https://en.wikipedia.org/wiki/John_F._Kennedy'),
            ('White House', 'The White House serves as the home and workplace of the president of the United States.', 'It became one of the most recognizable buildings in American political life.', 'https://en.wikipedia.org/wiki/White_House'),
            ('Air Force One', 'Air Force One is the call sign used for U.S. Air Force aircraft carrying the president.', 'It became one of the most recognizable symbols of presidential travel and security.', 'https://en.wikipedia.org/wiki/Air_Force_One'),
            ('22nd Amendment', 'The 22nd Amendment limits U.S. presidents to two elected terms in office.', 'It was adopted after Franklin D. Roosevelt’s unprecedented four-term presidency.', 'https://en.wikipedia.org/wiki/Twenty-second_Amendment_to_the_United_States_Constitution'),
        ],
    },
    'us-history': {
        'hobby': 'U.S. History',
        'entries': [
            ('Declaration of Independence', 'The Declaration of Independence announced the colonies’ break from British rule in 1776.', 'It remains one of the foundational texts in U.S. history.', 'https://en.wikipedia.org/wiki/United_States_Declaration_of_Independence'),
            ('U.S. Constitution', 'The U.S. Constitution created the framework for the federal government of the United States.', 'It became one of the most influential governing documents in modern history.', 'https://en.wikipedia.org/wiki/Constitution_of_the_United_States'),
            ('Lewis and Clark Expedition', 'The Lewis and Clark Expedition explored land acquired in the Louisiana Purchase and mapped routes to the west.', 'It became one of the most famous journeys in early U.S. history.', 'https://en.wikipedia.org/wiki/Lewis_and_Clark_Expedition'),
            ('Transcontinental Railroad', 'The transcontinental railroad connected the eastern and western United States by rail.', 'Its completion transformed travel, business, and migration across the country.', 'https://en.wikipedia.org/wiki/First_transcontinental_railroad'),
            ('Ellis Island', 'Ellis Island became one of the main entry points for immigrants arriving in the United States.', 'Its story remains central to many family histories and migration narratives.', 'https://en.wikipedia.org/wiki/Ellis_Island'),
            ('New Deal', 'The New Deal introduced major federal programs during the Great Depression.', 'It changed the relationship between government and everyday life in the United States.', 'https://en.wikipedia.org/wiki/New_Deal'),
            ('Civil Rights Act of 1964', 'The Civil Rights Act of 1964 became one of the most important laws in modern U.S. history.', 'It outlawed discrimination in several major areas of public life.', 'https://en.wikipedia.org/wiki/Civil_Rights_Act_of_1964'),
            ('Apollo 11', 'Apollo 11 put the first humans on the Moon and became a defining moment in U.S. history.', 'The mission remains one of the country’s best-known technological achievements.', 'https://en.wikipedia.org/wiki/Apollo_11'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f'{subject} is one of the first topics that comes up when people explore {hobby}.',
    lambda subject, detail, extra, hobby: f'Learning about {subject} gives a stronger feel for the depth and variety inside {hobby}.',
    lambda subject, detail, extra, hobby: f'Books, documentaries, and reference guides on {hobby} often highlight {subject}.',
    lambda subject, detail, extra, hobby: f'{subject} remains one of the most widely recognized examples connected with {hobby}.',
    lambda subject, detail, extra, hobby: f'For many readers, {subject} is a memorable entry point into {hobby}.',
    lambda subject, detail, extra, hobby: f'The story of {subject} helps explain why {hobby} stays so interesting to learn about.',
    lambda subject, detail, extra, hobby: f'{subject} is frequently mentioned in discussions, lessons, and articles about {hobby}.',
    lambda subject, detail, extra, hobby: f'One reason {hobby} feels so rich is that it includes major touchpoints like {subject}.',
    lambda subject, detail, extra, hobby: f'Readers interested in {hobby} often come across {subject} very quickly.',
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
