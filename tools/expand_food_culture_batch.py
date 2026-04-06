from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    'food': {
        'hobby': 'Food',
        'entries': [
            ('Bread', 'Bread has been one of the world\'s foundational foods for thousands of years.', 'Archaeological evidence suggests people were making bread long before the rise of large farming societies.', 'https://en.wikipedia.org/wiki/Bread'),
            ('Rice', 'Rice feeds billions of people and remains one of the most important staple foods on Earth.', 'It plays a central role in cuisines across Asia and far beyond.', 'https://en.wikipedia.org/wiki/Rice'),
            ('Coffee', 'Coffee became one of the world\'s most important beverages after spreading from East Africa and the Arabian world.', 'Its cultivation, trade, and café culture shaped social life across multiple continents.', 'https://en.wikipedia.org/wiki/Coffee'),
            ('Tea', 'Tea culture began in China and grew into one of the world\'s great food and drink traditions.', 'Different regions developed their own tea rituals, blends, and serving customs.', 'https://en.wikipedia.org/wiki/Tea'),
            ('Chocolate', 'Chocolate began as a cacao-based drink in Mesoamerica before becoming a global treat.', 'Its history connects Indigenous American food traditions with later global trade and dessert culture.', 'https://en.wikipedia.org/wiki/Chocolate'),
            ('Cheese', 'Cheese making stretches back thousands of years and produced countless regional styles.', 'It became one of the defining foods of many European, Middle Eastern, and global cuisines.', 'https://en.wikipedia.org/wiki/Cheese'),
            ('Olive oil', 'Olive oil is one of the signature ingredients of Mediterranean food traditions.', 'It has long been associated with cooking, trade, agriculture, and health-focused diets.', 'https://en.wikipedia.org/wiki/Olive_oil'),
            ('Sushi', 'Sushi evolved from preservation methods into one of the most famous dishes associated with Japan.', 'It later became one of the most internationally recognized forms of restaurant cuisine.', 'https://en.wikipedia.org/wiki/Sushi'),
            ('Pizza', 'Pizza became one of the world\'s most popular foods after growing from Italian roots into a global favorite.', 'Regional styles around the world now reflect different ingredients, traditions, and techniques.', 'https://en.wikipedia.org/wiki/Pizza'),
            ('Spices', 'Spices have shaped food, medicine, and international trade for centuries.', 'The search for spices helped drive exploration, empire, and changing global tastes.', 'https://en.wikipedia.org/wiki/Spice'),
        ],
    },
    'fast-food': {
        'hobby': 'Fast Food',
        'entries': [
            ('McDonald\'s', 'McDonald\'s became one of the best-known fast-food chains in the world after beginning in California.', 'Its menu, logo, and franchise model helped define modern fast food.', 'https://en.wikipedia.org/wiki/McDonald%27s'),
            ('Big Mac', 'The Big Mac became one of the signature burgers of the fast-food era.', 'It remains one of the most recognizable menu items in the global restaurant industry.', 'https://en.wikipedia.org/wiki/Big_Mac'),
            ('KFC', 'KFC grew from Harland Sanders\' fried chicken business into one of the world\'s biggest restaurant brands.', 'Its pressure-fried chicken and global expansion made it central to the history of fast food.', 'https://en.wikipedia.org/wiki/KFC'),
            ('Burger King', 'Burger King helped popularize flame-grilled burgers in the fast-food market.', 'The Whopper became its signature menu item and one of the best-known burgers in restaurant history.', 'https://en.wikipedia.org/wiki/Burger_King'),
            ('Wendy\'s', 'Wendy\'s became known for square burger patties and a menu built around fresh-never-frozen branding.', 'It remains one of the most famous American fast-food chains.', 'https://en.wikipedia.org/wiki/Wendy%27s'),
            ('Taco Bell', 'Taco Bell helped popularize Mexican-inspired fast food in the United States.', 'Its menu innovations made it one of the most recognizable quick-service brands in America.', 'https://en.wikipedia.org/wiki/Taco_Bell'),
            ('Subway', 'Subway built a global brand around made-to-order submarine sandwiches.', 'For years it expanded rapidly and became one of the world\'s largest fast-food chains by store count.', 'https://en.wikipedia.org/wiki/Subway_(restaurant)'),
            ('Pizza Hut', 'Pizza Hut became one of the dominant names in chain pizza and delivery culture.', 'Its red-roof restaurant design became a memorable part of U.S. roadside dining history.', 'https://en.wikipedia.org/wiki/Pizza_Hut'),
            ('Drive-through', 'The drive-through became one of the defining features of fast food and car culture.', 'It turned speed and convenience into central parts of the restaurant experience.', 'https://en.wikipedia.org/wiki/Drive-through'),
            ('Happy Meal', 'The Happy Meal combined fast food with toys and child-focused marketing.', 'It became one of the best-known kid-oriented products in restaurant history.', 'https://en.wikipedia.org/wiki/Happy_Meal'),
        ],
    },
    'world-food': {
        'hobby': 'World Food',
        'entries': [
            ('Paella', 'Paella from Valencia became one of the world\'s best-known Spanish dishes.', 'Its rice, saffron, and regional variations made it central to many conversations about world cuisine.', 'https://en.wikipedia.org/wiki/Paella'),
            ('Pho', 'Pho is one of Vietnam\'s most famous dishes and is known for its fragrant broth and noodles.', 'It became a major global ambassador for Vietnamese cooking.', 'https://en.wikipedia.org/wiki/Pho'),
            ('Biryani', 'Biryani blends Persian and South Asian influences into one of the best-loved rice dishes in the world.', 'Its many regional versions make it a highlight of Indian and neighboring cuisines.', 'https://en.wikipedia.org/wiki/Biryani'),
            ('Kimchi', 'Kimchi is one of Korea\'s most iconic foods and exists in many regional and seasonal styles.', 'Its fermentation traditions helped make it one of the most famous dishes in world food culture.', 'https://en.wikipedia.org/wiki/Kimchi'),
            ('Ceviche', 'Ceviche became one of the most famous seafood dishes associated with Latin America, especially Peru.', 'Its use of citrus and fresh fish made it a landmark of coastal cuisine.', 'https://en.wikipedia.org/wiki/Ceviche'),
            ('Dim sum', 'Dim sum is strongly associated with Cantonese cuisine and tea-house culture.', 'Its shared small plates helped make it one of the world\'s best-known communal dining traditions.', 'https://en.wikipedia.org/wiki/Dim_sum'),
            ('Falafel', 'Falafel became one of the great street foods of the Middle East.', 'It is now widely recognized around the world as a popular vegetarian option and cultural staple.', 'https://en.wikipedia.org/wiki/Falafel'),
            ('Tacos al pastor', 'Tacos al pastor became one of Mexico\'s most famous street foods.', 'Its history reflects the blending of Mexican and Lebanese culinary influences.', 'https://en.wikipedia.org/wiki/Al_pastor'),
            ('Gelato', 'Gelato represents the Italian style of ice cream and dessert craftsmanship.', 'It became one of the most recognizable sweet foods in global travel culture.', 'https://en.wikipedia.org/wiki/Gelato'),
            ('Poutine', 'Poutine from Quebec combines fries, cheese curds, and gravy into one of Canada\'s signature dishes.', 'It became a famous example of how local comfort food can gain international recognition.', 'https://en.wikipedia.org/wiki/Poutine'),
        ],
    },
    'world-culture': {
        'hobby': 'World Culture',
        'entries': [
            ('Lunar New Year', 'Lunar New Year is celebrated across many parts of East and Southeast Asia with family rituals, food, and renewal themes.', 'Its many regional traditions make it one of the most widely recognized seasonal celebrations in the world.', 'https://en.wikipedia.org/wiki/Lunar_New_Year'),
            ('Diwali', 'Diwali is often called the Festival of Lights and is celebrated by millions of people in India and worldwide.', 'Its lamps, sweets, gatherings, and rituals made it one of the best-known cultural festivals on Earth.', 'https://en.wikipedia.org/wiki/Diwali'),
            ('Day of the Dead', 'Día de los Muertos honors loved ones who have died and remains one of Mexico\'s most recognized cultural traditions.', 'Its altars, marigolds, art, and processions became globally known symbols of remembrance.', 'https://en.wikipedia.org/wiki/Day_of_the_Dead'),
            ('Nowruz', 'Nowruz marks the Persian New Year and the arrival of spring across Iran and many neighboring cultures.', 'Its deep roots made it one of the longest-lasting seasonal celebrations in world culture.', 'https://en.wikipedia.org/wiki/Nowruz'),
            ('Oktoberfest', 'Oktoberfest in Munich grew from a royal wedding celebration into the world\'s best-known beer festival.', 'It now draws visitors from around the globe and became a symbol of Bavarian culture.', 'https://en.wikipedia.org/wiki/Oktoberfest'),
            ('Rio Carnival', 'Rio Carnival became one of the largest and most famous festivals in the world.', 'Its samba parades and street celebrations helped make it a defining image of Brazilian culture.', 'https://en.wikipedia.org/wiki/Rio_Carnival'),
            ('Japanese tea ceremony', 'The Japanese tea ceremony emphasizes ritual, hospitality, and attention to detail.', 'It became one of the most admired examples of how everyday acts can become high cultural practice.', 'https://en.wikipedia.org/wiki/Japanese_tea_ceremony'),
            ('Flamenco', 'Flamenco from Spain combines singing, guitar, dance, and rhythmic performance.', 'It became one of the most famous artistic traditions associated with Spanish culture.', 'https://en.wikipedia.org/wiki/Flamenco'),
            ('Tango', 'Tango developed in Argentina and Uruguay and became one of the world\'s most famous partner dances.', 'Its music, movement, and style gave it a lasting place in international culture.', 'https://en.wikipedia.org/wiki/Tango'),
            ('Haka', 'The haka is a traditional Māori chant and dance from Aotearoa New Zealand.', 'It became globally familiar through ceremony, sport, and cultural performance.', 'https://en.wikipedia.org/wiki/Haka'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f"{subject} is one of the standout traditions or topics associated with {hobby}.",
    lambda subject, detail, extra, hobby: f"Readers and travelers interested in {hobby} often encounter {subject} very quickly.",
    lambda subject, detail, extra, hobby: f"Learning about {subject} helps explain part of the appeal and diversity of {hobby}.",
    lambda subject, detail, extra, hobby: f"For many people around the world, {subject} is a memorable part of {hobby}.",
    lambda subject, detail, extra, hobby: f"Documentaries, articles, and travel guides about {hobby} frequently highlight {subject}.",
    lambda subject, detail, extra, hobby: f"The story of {subject} connects directly to the broader traditions behind {hobby}.",
    lambda subject, detail, extra, hobby: f"{subject} is frequently used to introduce newcomers to the richness of {hobby}.",
    lambda subject, detail, extra, hobby: f"Many people associate {hobby} with cultural touchstones such as {subject}.",
    lambda subject, detail, extra, hobby: f"One reason {hobby} feels so vivid and memorable is the presence of traditions and foods such as {subject}.",
    lambda subject, detail, extra, hobby: f"From heritage to everyday life, {subject} plays a notable role in how {hobby} is experienced and described.",
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
