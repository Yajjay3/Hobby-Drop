from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    'geography': {
        'hobby': 'Geography & USA Landmarks',
        'entries': [
            ('Grand Canyon', 'The Grand Canyon in Arizona was carved by the Colorado River and reveals layers of geological history.', 'Grand Canyon National Park is one of the most visited natural sites in the United States.', 'https://en.wikipedia.org/wiki/Grand_Canyon'),
            ('Yellowstone National Park', 'Yellowstone became the first national park in the United States in 1872.', 'The park is famous for geysers, wildlife, hot springs, and dramatic volcanic landscapes.', 'https://en.wikipedia.org/wiki/Yellowstone_National_Park'),
            ('Yosemite National Park', 'Yosemite is known for granite cliffs such as El Capitan and Half Dome.', 'Its waterfalls, giant sequoias, and valley views made it one of America\'s best-known parks.', 'https://en.wikipedia.org/wiki/Yosemite_National_Park'),
            ('Niagara Falls', 'Niagara Falls straddles the border between the United States and Canada.', 'It is one of North America\'s most famous waterfall destinations and a major hydroelectric site.', 'https://en.wikipedia.org/wiki/Niagara_Falls'),
            ('Great Lakes', 'The Great Lakes form the largest group of freshwater lakes on Earth by surface area.', 'Lake Superior, Lake Michigan, Lake Huron, Lake Erie, and Lake Ontario shape a huge part of North American geography.', 'https://en.wikipedia.org/wiki/Great_Lakes'),
            ('Mississippi River', 'The Mississippi River is one of the defining river systems of the United States.', 'Its watershed touches a large portion of the country and played a major role in trade and transportation.', 'https://en.wikipedia.org/wiki/Mississippi_River'),
            ('Rocky Mountains', 'The Rocky Mountains run from Canada into the western United States.', 'The range is central to the geography of states such as Colorado, Montana, and Wyoming.', 'https://en.wikipedia.org/wiki/Rocky_Mountains'),
            ('Denali', 'Denali in Alaska is the tallest peak in North America.', 'The mountain stands in Denali National Park and Preserve and remains a landmark of U.S. wilderness.', 'https://en.wikipedia.org/wiki/Denali'),
            ('Everglades', 'The Florida Everglades are one of the world\'s most distinctive wetland ecosystems.', 'They are home to alligators, mangroves, sawgrass marshes, and many endangered species.', 'https://en.wikipedia.org/wiki/Everglades'),
            ('Statue of Liberty', 'The Statue of Liberty in New York Harbor became a symbol of freedom and immigration.', 'It was a gift from France and has welcomed arrivals since the 19th century.', 'https://en.wikipedia.org/wiki/Statue_of_Liberty'),
            ('Golden Gate Bridge', 'San Francisco\'s Golden Gate Bridge is one of the most recognizable bridges in the world.', 'Its Art Deco design and international orange color made it an icon of the American West Coast.', 'https://en.wikipedia.org/wiki/Golden_Gate_Bridge'),
            ('Mount Rushmore', 'Mount Rushmore features the faces of four U.S. presidents carved into granite in South Dakota.', 'It is one of the most famous monuments connected to American history and identity.', 'https://en.wikipedia.org/wiki/Mount_Rushmore'),
        ],
    },
    'europe': {
        'hobby': 'Europe',
        'entries': [
            ('Eiffel Tower', 'The Eiffel Tower in Paris remains one of the most recognized landmarks in Europe.', 'Built for the 1889 Exposition Universelle, it became a global symbol of France and European travel.', 'https://en.wikipedia.org/wiki/Eiffel_Tower'),
            ('Colosseum', 'The Colosseum in Rome is one of the greatest surviving monuments of ancient Rome.', 'It once hosted gladiatorial contests and public spectacles before becoming a symbol of European history.', 'https://en.wikipedia.org/wiki/Colosseum'),
            ('Acropolis of Athens', 'The Acropolis of Athens preserves some of the most famous monuments of classical Greece.', 'Its hilltop temples, especially the Parthenon, are central to the story of European civilization.', 'https://en.wikipedia.org/wiki/Acropolis_of_Athens'),
            ('Stonehenge', 'Stonehenge in England is one of Europe\'s most famous prehistoric monuments.', 'Its origins and purpose continue to fascinate archaeologists, historians, and visitors.', 'https://en.wikipedia.org/wiki/Stonehenge'),
            ('Alps', 'The Alps stretch across several European countries and dominate much of central Europe\'s mountain scenery.', 'The range supports skiing, hiking, and some of the continent\'s most famous resort regions.', 'https://en.wikipedia.org/wiki/Alps'),
            ('Danube River', 'The Danube River passes through more countries than any other river in Europe.', 'It links Central and Eastern Europe and has long been important for trade and culture.', 'https://en.wikipedia.org/wiki/Danube'),
            ('Vatican City', 'Vatican City is the smallest independent state in the world and sits inside Rome.', 'It is the spiritual center of the Roman Catholic Church and home to St. Peter\'s Basilica.', 'https://en.wikipedia.org/wiki/Vatican_City'),
            ('Sagrada Família', 'Barcelona\'s Sagrada Família is one of the most famous churches in Europe.', 'Architect Antoni Gaudí\'s unfinished masterpiece has become a defining image of Spain.', 'https://en.wikipedia.org/wiki/Sagrada_Fam%C3%ADlia'),
            ('Louvre', 'The Louvre in Paris is among the most visited museums in the world.', 'Its collections, including the Mona Lisa and Venus de Milo, make it central to European art history.', 'https://en.wikipedia.org/wiki/Louvre'),
            ('Palace of Versailles', 'The Palace of Versailles became a symbol of French royal power before the French Revolution.', 'Its gardens, halls, and court culture made it one of Europe\'s most famous palaces.', 'https://en.wikipedia.org/wiki/Palace_of_Versailles'),
            ('Amsterdam canals', 'Amsterdam\'s canal ring is one of the best-known urban landscapes in Europe.', 'The canals reflect Dutch engineering, trade history, and the city\'s distinctive design.', 'https://en.wikipedia.org/wiki/Canals_of_Amsterdam'),
            ('Berlin Wall', 'The Berlin Wall became one of the most famous symbols of the Cold War in Europe.', 'Its fall in 1989 marked a turning point in the history of Germany and the continent.', 'https://en.wikipedia.org/wiki/Berlin_Wall'),
        ],
    },
    'asia': {
        'hobby': 'Asia',
        'entries': [
            ('Himalayas', 'The Himalayas are the highest mountain range on Earth and stretch across several Asian countries.', 'They include Mount Everest and shape climate, rivers, and cultures across a huge part of Asia.', 'https://en.wikipedia.org/wiki/Himalayas'),
            ('Mount Everest', 'Mount Everest sits on the border of Nepal and China and is the tallest mountain above sea level.', 'It is one of the best-known peaks on Earth and a major symbol of Asian geography.', 'https://en.wikipedia.org/wiki/Mount_Everest'),
            ('Silk Road', 'The Silk Road linked East Asia with the Middle East and Europe through long-distance trade.', 'Its routes helped spread goods, religions, technologies, and ideas across Asia.', 'https://en.wikipedia.org/wiki/Silk_Road'),
            ('Ganges', 'The Ganges River is one of South Asia\'s most important rivers in both geography and religion.', 'It supports hundreds of millions of people and holds major cultural significance in India and Bangladesh.', 'https://en.wikipedia.org/wiki/Ganges'),
            ('Mekong', 'The Mekong River flows through multiple countries in Southeast Asia.', 'Its waters and floodplains are crucial for farming, fishing, transportation, and regional culture.', 'https://en.wikipedia.org/wiki/Mekong'),
            ('Angkor Wat', 'Angkor Wat in Cambodia is one of the largest religious monuments in the world.', 'It stands as one of Asia\'s most famous temple complexes and a major symbol of Khmer history.', 'https://en.wikipedia.org/wiki/Angkor_Wat'),
            ('Petra', 'Petra in modern-day Jordan is famous for its rock-cut architecture and desert setting.', 'It remains one of West Asia\'s best-known archaeological sites and a UNESCO World Heritage Site.', 'https://en.wikipedia.org/wiki/Petra'),
            ('Great Wall of China', 'The Great Wall of China stretches across northern China and was built and rebuilt across many dynasties.', 'It is one of Asia\'s most famous historical landmarks and a symbol of imperial Chinese history.', 'https://en.wikipedia.org/wiki/Great_Wall_of_China'),
            ('Taj Mahal', 'The Taj Mahal in Agra is one of the most celebrated buildings in Asia.', 'This white marble mausoleum was built by the Mughal emperor Shah Jahan and became a global symbol of India.', 'https://en.wikipedia.org/wiki/Taj_Mahal'),
            ('Tokyo', 'Tokyo is one of Asia\'s great megacities and a major center of finance, technology, and culture.', 'Its scale and influence help illustrate the urban power of modern Asia.', 'https://en.wikipedia.org/wiki/Tokyo'),
            ('Singapore', 'Singapore is a city-state in Southeast Asia known for its port, skyline, and global economic role.', 'Its mix of finance, trade, food culture, and urban planning made it one of Asia\'s best-known cities.', 'https://en.wikipedia.org/wiki/Singapore'),
            ('Ha Long Bay', 'Ha Long Bay in Vietnam is famous for limestone islands rising from emerald waters.', 'It is one of Southeast Asia\'s best-known natural wonders and a major tourism destination.', 'https://en.wikipedia.org/wiki/H%E1%BA%A1_Long_Bay'),
        ],
    },
    'japan': {
        'hobby': 'Japan',
        'entries': [
            ('Mount Fuji', 'Mount Fuji is Japan\'s most famous peak and a long-standing national symbol.', 'Its near-perfect volcanic shape made it one of the most recognizable mountains in the world.', 'https://en.wikipedia.org/wiki/Mount_Fuji'),
            ('Tokyo', 'Tokyo is Japan\'s capital and one of the world\'s largest metropolitan areas.', 'The city combines skyscrapers, rail networks, food districts, pop culture, and historic shrines.', 'https://en.wikipedia.org/wiki/Tokyo'),
            ('Kyoto', 'Kyoto served as Japan\'s imperial capital for more than a thousand years.', 'Its temples, shrines, gardens, and traditional neighborhoods preserve a major part of Japanese heritage.', 'https://en.wikipedia.org/wiki/Kyoto'),
            ('Osaka', 'Osaka is known for food culture, commerce, nightlife, and a famously energetic urban identity.', 'It is often described as one of Japan\'s great culinary capitals.', 'https://en.wikipedia.org/wiki/Osaka'),
            ('Shinkansen', 'Japan\'s Shinkansen bullet trains are famous for speed, safety, and punctuality.', 'They became one of the most admired rail systems in the world and a symbol of postwar modernization.', 'https://en.wikipedia.org/wiki/Shinkansen'),
            ('Nara', 'Nara is famous for temples, deer parks, and some of Japan\'s earliest monumental Buddhist sites.', 'It was one of Japan\'s first permanent capitals and remains important to the country\'s history.', 'https://en.wikipedia.org/wiki/Nara,_Nara'),
            ('Himeji Castle', 'Himeji Castle is one of the best-preserved castles in Japan.', 'Its white exterior and defensive design made it one of the country\'s most admired historic buildings.', 'https://en.wikipedia.org/wiki/Himeji_Castle'),
            ('Hiroshima Peace Memorial', 'The Hiroshima Peace Memorial stands near the site of the 1945 atomic bombing.', 'It remains a major place of remembrance and a global symbol of peace advocacy.', 'https://en.wikipedia.org/wiki/Hiroshima_Peace_Memorial'),
            ('Fushimi Inari-taisha', 'Fushimi Inari-taisha in Kyoto is famous for its long paths of bright red torii gates.', 'The shrine is one of the most photographed religious sites in Japan.', 'https://en.wikipedia.org/wiki/Fushimi_Inari-taisha'),
            ('Sapporo', 'Sapporo is a major city on Hokkaido known for winter sports, beer, and its snow festival.', 'It shows the colder northern side of Japan\'s geography and culture.', 'https://en.wikipedia.org/wiki/Sapporo'),
            ('Okinawa', 'Okinawa has a subtropical climate and a cultural history that differs from mainland Japan.', 'Its islands are famous for beaches, coral waters, and the legacy of the former Ryukyu Kingdom.', 'https://en.wikipedia.org/wiki/Okinawa_Prefecture'),
            ('Tokyo Skytree', 'Tokyo Skytree is one of the tallest towers in the world and a major modern landmark in Japan.', 'It was built to serve broadcasting needs and became a major symbol of contemporary Tokyo.', 'https://en.wikipedia.org/wiki/Tokyo_Skytree'),
        ],
    },
    'india': {
        'hobby': 'India',
        'entries': [
            ('Taj Mahal', 'The Taj Mahal in Agra is one of India\'s best-known monuments and a UNESCO World Heritage Site.', 'Its white marble design helped make it one of the most famous buildings in the world.', 'https://en.wikipedia.org/wiki/Taj_Mahal'),
            ('Ganges', 'The Ganges River is one of India\'s most important waterways and sacred rivers.', 'Cities along its banks play a major role in religion, agriculture, and daily life.', 'https://en.wikipedia.org/wiki/Ganges'),
            ('Jaipur', 'Jaipur is known as the Pink City and is one of northern India\'s most famous historic destinations.', 'Its palaces, forts, and markets made it a highlight of the Golden Triangle travel route.', 'https://en.wikipedia.org/wiki/Jaipur'),
            ('Varanasi', 'Varanasi is one of the oldest continually inhabited cities in the world.', 'It is one of Hinduism\'s holiest cities and is closely tied to the Ganges.', 'https://en.wikipedia.org/wiki/Varanasi'),
            ('Red Fort', 'The Red Fort in Delhi was built by the Mughal emperor Shah Jahan in the 17th century.', 'It remains one of the most important monuments connected to India\'s Mughal past.', 'https://en.wikipedia.org/wiki/Red_Fort'),
            ('Gateway of India', 'The Gateway of India in Mumbai overlooks the Arabian Sea and became one of the city\'s signature monuments.', 'It is among the most recognizable colonial-era landmarks in India.', 'https://en.wikipedia.org/wiki/Gateway_of_India'),
            ('Kerala backwaters', 'Kerala\'s backwaters form a network of lagoons, lakes, and canals along India\'s southwest coast.', 'Houseboats and waterside villages made the region one of India\'s most famous travel landscapes.', 'https://en.wikipedia.org/wiki/Kerala_backwaters'),
            ('Himalayan region of India', 'India\'s Himalayan region includes major mountain destinations, pilgrimage sites, and high-altitude landscapes.', 'States and territories such as Himachal Pradesh, Uttarakhand, Ladakh, and Sikkim reflect this dramatic terrain.', 'https://en.wikipedia.org/wiki/Himalayas'),
            ('Diwali', 'Diwali is one of India\'s best-known festivals and is often called the Festival of Lights.', 'It is celebrated with lamps, gatherings, sweets, and regional traditions across the country.', 'https://en.wikipedia.org/wiki/Diwali'),
            ('Bollywood', 'Bollywood refers to the Hindi-language film industry centered in Mumbai.', 'It became one of the most prolific and influential film industries in the world.', 'https://en.wikipedia.org/wiki/Hindi_cinema'),
            ('Qutub Minar', 'Delhi\'s Qutub Minar is one of India\'s most famous towers and early Indo-Islamic monuments.', 'Its red sandstone design makes it a major landmark of medieval Indian history.', 'https://en.wikipedia.org/wiki/Qutb_Minar'),
            ('Indian Railways', 'Indian Railways is one of the world\'s largest rail networks.', 'Its reach across cities, villages, and landscapes makes it central to how India moves and connects.', 'https://en.wikipedia.org/wiki/Indian_Railways'),
        ],
    },
    'italy': {
        'hobby': 'Italy',
        'entries': [
            ('Rome', 'Rome is Italy\'s capital and one of the most historically influential cities in the world.', 'Its ruins, churches, piazzas, and public art made it a defining center of European history.', 'https://en.wikipedia.org/wiki/Rome'),
            ('Colosseum', 'The Colosseum in Rome remains one of Italy\'s most famous monuments.', 'It is a major symbol of the Roman Empire and of Italy\'s deep historical legacy.', 'https://en.wikipedia.org/wiki/Colosseum'),
            ('Venice', 'Venice is world-famous for canals, bridges, and lagoon geography.', 'Its unique urban layout made it one of Italy\'s most distinctive cities and travel icons.', 'https://en.wikipedia.org/wiki/Venice'),
            ('Florence', 'Florence played a central role in the Renaissance and in the history of art, architecture, and banking.', 'It remains one of Italy\'s most celebrated historic cities.', 'https://en.wikipedia.org/wiki/Florence'),
            ('Leaning Tower of Pisa', 'The Leaning Tower of Pisa is one of Italy\'s best-known landmarks.', 'Its famous tilt turned a medieval bell tower into a global symbol of Italian travel.', 'https://en.wikipedia.org/wiki/Leaning_Tower_of_Pisa'),
            ('Amalfi Coast', 'The Amalfi Coast is famous for dramatic cliffs, pastel towns, and Mediterranean views.', 'It is one of the most visited coastal landscapes in Italy.', 'https://en.wikipedia.org/wiki/Amalfi_Coast'),
            ('Milan', 'Milan is a major Italian center for fashion, finance, and design.', 'The city also houses historic sites such as the Duomo and Leonardo da Vinci\'s The Last Supper.', 'https://en.wikipedia.org/wiki/Milan'),
            ('Pompeii', 'Pompeii preserves one of the most remarkable archaeological records of everyday life in the Roman world.', 'The city was buried by the eruption of Mount Vesuvius in 79 CE.', 'https://en.wikipedia.org/wiki/Pompeii'),
            ('Sicily', 'Sicily is the largest island in the Mediterranean and has layered Greek, Roman, Arab, Norman, and Italian history.', 'Its landscapes, volcanoes, and cuisine give it a distinct place in Italy.', 'https://en.wikipedia.org/wiki/Sicily'),
            ('Cinque Terre', 'Cinque Terre is known for colorful villages perched along the Ligurian coast.', 'It became one of Italy\'s most photographed and celebrated coastal destinations.', 'https://en.wikipedia.org/wiki/Cinque_Terre'),
            ('Lake Como', 'Lake Como in northern Italy is famous for mountain scenery, villas, and resort towns.', 'It has long been associated with leisure travel and elegant lakeside culture.', 'https://en.wikipedia.org/wiki/Lake_Como'),
            ('Vatican City', 'Vatican City sits within Rome and is the spiritual center of the Roman Catholic Church.', 'Its presence adds another layer of historical and religious importance to Italy\'s capital.', 'https://en.wikipedia.org/wiki/Vatican_City'),
        ],
    },
    'greece': {
        'hobby': 'Greece',
        'entries': [
            ('Acropolis of Athens', 'The Acropolis of Athens is one of the most famous archaeological sites in the world.', 'Its temples overlook the city and symbolize the legacy of ancient Greece.', 'https://en.wikipedia.org/wiki/Acropolis_of_Athens'),
            ('Parthenon', 'The Parthenon is the best-known temple on the Acropolis and a symbol of classical architecture.', 'It has become one of the most recognizable structures associated with Greece.', 'https://en.wikipedia.org/wiki/Parthenon'),
            ('Santorini', 'Santorini is famous for whitewashed buildings, volcanic cliffs, and sunset views over the Aegean Sea.', 'It became one of the most iconic island destinations in Greece.', 'https://en.wikipedia.org/wiki/Santorini'),
            ('Crete', 'Crete is Greece\'s largest island and was the center of the Minoan civilization.', 'Its history, beaches, mountain villages, and archaeology make it one of the country\'s most varied regions.', 'https://en.wikipedia.org/wiki/Crete'),
            ('Delphi', 'Delphi was one of the most important sacred sites in ancient Greece.', 'The oracle of Delphi gave the site enormous religious and cultural significance.', 'https://en.wikipedia.org/wiki/Delphi'),
            ('Mount Olympus', 'Mount Olympus was the mythic home of the Greek gods in ancient tradition.', 'It is also Greece\'s highest mountain and a major natural landmark.', 'https://en.wikipedia.org/wiki/Mount_Olympus'),
            ('Athens', 'Athens is Greece\'s capital and one of the oldest cities in Europe.', 'Its history in philosophy, drama, politics, and architecture made it foundational to Western civilization.', 'https://en.wikipedia.org/wiki/Athens'),
            ('Meteora', 'Meteora is famous for monasteries perched on towering rock pillars in central Greece.', 'The site blends natural wonder with spiritual history and is one of Greece\'s most striking landscapes.', 'https://en.wikipedia.org/wiki/Meteora'),
            ('Mykonos', 'Mykonos is known for windmills, beaches, nightlife, and whitewashed Cycladic architecture.', 'It became one of the most internationally recognized Greek islands.', 'https://en.wikipedia.org/wiki/Mykonos'),
            ('Rhodes', 'Rhodes is famous for medieval walls, Old Town architecture, and its role in ancient Greek history.', 'It was once associated with the legendary Colossus of Rhodes, one of the Seven Wonders.', 'https://en.wikipedia.org/wiki/Rhodes'),
            ('Olympia', 'Olympia was the original site of the ancient Olympic Games.', 'Its ruins connect Greece directly to one of the most famous sporting traditions in world history.', 'https://en.wikipedia.org/wiki/Olympia,_Greece'),
            ('Thessaloniki', 'Thessaloniki is Greece\'s second-largest city and a major center of Byzantine history and culture.', 'Its waterfront, churches, and urban life give it a distinct role in modern Greece.', 'https://en.wikipedia.org/wiki/Thessaloniki'),
        ],
    },
    'egypt': {
        'hobby': 'Egypt',
        'entries': [
            ('Pyramids of Giza', 'The Pyramids of Giza are among the most famous ancient monuments in the world.', 'They remain central to the image of Egypt and to the study of ancient civilization.', 'https://en.wikipedia.org/wiki/Giza_pyramid_complex'),
            ('Great Sphinx of Giza', 'The Great Sphinx of Giza is one of Egypt\'s most recognizable ancient sculptures.', 'Its lion body and human head made it one of the enduring icons of Egyptian history.', 'https://en.wikipedia.org/wiki/Great_Sphinx_of_Giza'),
            ('Nile', 'The Nile River is the lifeline of Egypt and one of the most famous rivers in the world.', 'Its annual floods shaped agriculture, settlement, and state formation in ancient Egypt.', 'https://en.wikipedia.org/wiki/Nile'),
            ('Luxor Temple', 'Luxor Temple stands on the east bank of the Nile in the city of Luxor.', 'It remains one of Egypt\'s best-known temple complexes and a major tourist site.', 'https://en.wikipedia.org/wiki/Luxor_Temple'),
            ('Valley of the Kings', 'The Valley of the Kings served as a burial ground for pharaohs and nobles of the New Kingdom.', 'It is one of the most important archaeological areas connected to ancient Egypt.', 'https://en.wikipedia.org/wiki/Valley_of_the_Kings'),
            ('Abu Simbel', 'Abu Simbel is famous for its colossal rock temples built by Ramesses II.', 'The site was relocated in the 20th century to save it from flooding after the Aswan High Dam project.', 'https://en.wikipedia.org/wiki/Abu_Simbel'),
            ('Alexandria', 'Alexandria was founded by Alexander the Great and became one of the great cities of the ancient Mediterranean.', 'It later became famous for the ancient Library of Alexandria and its coastal setting.', 'https://en.wikipedia.org/wiki/Alexandria'),
            ('Cairo', 'Cairo is Egypt\'s capital and one of the largest cities in Africa and the Arab world.', 'Its museums, mosques, markets, and historic quarters make it central to understanding modern Egypt.', 'https://en.wikipedia.org/wiki/Cairo'),
            ('Karnak', 'Karnak is a vast temple complex near Luxor associated with the god Amun and other deities.', 'It remains one of the largest religious building sites ever created.', 'https://en.wikipedia.org/wiki/Karnak'),
            ('Aswan', 'Aswan sits in southern Egypt and has long been important for trade, Nile travel, and monumental engineering.', 'Its modern high dam changed water management across Egypt.', 'https://en.wikipedia.org/wiki/Aswan'),
            ('Red Sea coast of Egypt', 'Egypt\'s Red Sea coast is famous for beaches, coral reefs, and diving destinations.', 'It shows that Egypt is known for more than ancient monuments alone.', 'https://en.wikipedia.org/wiki/Red_Sea_Governorate'),
            ('Egyptian Museum', 'Cairo\'s museum collections, including the Egyptian Museum and newer Grand Egyptian Museum, preserve famous artifacts from pharaonic history.', 'These collections include treasures connected to Tutankhamun and many other rulers.', 'https://en.wikipedia.org/wiki/Egyptian_Museum'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f"{subject} is one of the most recognizable places or topics associated with {hobby}.",
    lambda subject, detail, extra, hobby: f"Travel guides about {hobby} frequently feature {subject}.",
    lambda subject, detail, extra, hobby: f"Learning about {subject} helps explain part of the geography, culture, or history of {hobby}.",
    lambda subject, detail, extra, hobby: f"For many visitors, {subject} stands out as a major highlight of {hobby}.",
    lambda subject, detail, extra, hobby: f"Maps, documentaries, and guidebooks about {hobby} often highlight {subject}.",
    lambda subject, detail, extra, hobby: f"The story of {subject} is closely tied to how many people understand {hobby}.",
    lambda subject, detail, extra, hobby: f"People around the world often associate {hobby} with places or traditions like {subject}.",
    lambda subject, detail, extra, hobby: f"{subject} is frequently mentioned when describing the diversity and appeal of {hobby}.",
    lambda subject, detail, extra, hobby: f"One reason {hobby} feels so memorable to travelers is the presence of places such as {subject}.",
    lambda subject, detail, extra, hobby: f"From tourism to history, {subject} plays a notable role in how {hobby} is presented to the world.",
]

for file_key, config in BATCH.items():
    path = BASE / f'{file_key}.json'
    current = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'hobby': config['hobby'], 'facts': []}
    current.setdefault('hobby', config['hobby'])
    current.setdefault('facts', [])
    existing_texts = {fact.get('text') for fact in current['facts']}

    for subject, detail, extra, source in config['entries']:
        for template in TEMPLATES:
            text = template(subject, detail, extra, config['hobby'])
            if text not in existing_texts:
                current['facts'].append({'text': text, 'source': source})
                existing_texts.add(text)

    path.write_text(json.dumps(current, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"{file_key}\t{len(current['facts'])} facts")
