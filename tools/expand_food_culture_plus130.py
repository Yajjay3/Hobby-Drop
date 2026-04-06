from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

EXTRA_BATCH = {
    'food': {
        'hobby': 'Food',
        'entries': [
            ('Pasta', 'Pasta became one of the defining foods of Italian cuisine before spreading into kitchens around the world.', 'Different pasta shapes and sauces reflect regional traditions that turned a simple staple into countless classic dishes.', 'https://en.wikipedia.org/wiki/Pasta'),
            ('Noodles', 'Noodles have been eaten in many parts of the world for centuries and appear in countless regional dishes.', 'From hand-pulled strands to instant cups, noodle traditions show how a basic food can take many forms.', 'https://en.wikipedia.org/wiki/Noodle'),
            ('Fermentation', 'Fermentation helps create foods such as yogurt, kimchi, cheese, and sourdough bread.', 'It is one of the oldest techniques people developed for preserving food and building flavor.', 'https://en.wikipedia.org/wiki/Fermentation_in_food_processing'),
            ('Barbecue', 'Barbecue traditions differ widely across regions, from low-and-slow smoking to open-fire grilling.', 'Its methods and sauces became some of the most debated and celebrated topics in food culture.', 'https://en.wikipedia.org/wiki/Barbecue'),
            ('Curry', 'Curry became a global food idea with many local interpretations across South Asia and beyond.', 'The word can describe different spiced dishes rather than one single recipe.', 'https://en.wikipedia.org/wiki/Curry'),
            ('Chili peppers', 'Chili peppers originated in the Americas before spreading around the world through global trade.', 'They transformed cuisines in Asia, Africa, and Europe after the Columbian Exchange.', 'https://en.wikipedia.org/wiki/Chili_pepper'),
            ('Street food', 'Street food offers one of the most immediate and local ways to experience a region\'s cooking.', 'Markets and carts often turn simple foods into some of the most memorable meals people eat while traveling.', 'https://en.wikipedia.org/wiki/Street_food'),
            ('Ice cream', 'Ice cream evolved from older frozen desserts into one of the world\'s favorite sweet treats.', 'Its many styles, flavors, and serving traditions made it a major part of dessert culture.', 'https://en.wikipedia.org/wiki/Ice_cream'),
            ('Maize', 'Maize, also called corn, became one of the most important crops and food sources in the world.', 'Its history is deeply tied to the agricultural knowledge of Indigenous peoples of the Americas.', 'https://en.wikipedia.org/wiki/Maize'),
            ('Salt', 'Salt shaped food preservation, seasoning, and trade for much of recorded history.', 'It mattered so much to cooking and survival that whole trade routes grew around it.', 'https://en.wikipedia.org/wiki/Salt'),
            ('Dumplings', 'Dumplings appear in many cuisines, from East Asian jiaozi to Eastern European pierogi and Central Asian manti.', 'They show how similar food ideas can develop into very different local traditions.', 'https://en.wikipedia.org/wiki/Dumpling'),
            ('Ramen', 'Ramen grew into one of Japan\'s most famous noodle dishes and a major part of global food culture.', 'Its broths, toppings, and regional styles made it a favorite topic for cooks and diners alike.', 'https://en.wikipedia.org/wiki/Ramen'),
        ],
    },
    'fast-food': {
        'hobby': 'Fast Food',
        'entries': [
            ('French fries', 'French fries became one of the most common side dishes in fast-food restaurants around the world.', 'Their crispy texture and portability made them a perfect fit for quick-service dining.', 'https://en.wikipedia.org/wiki/French_fries'),
            ('Chicken nuggets', 'Chicken nuggets helped turn bite-sized fried chicken into a fast-food staple.', 'They became one of the most familiar kids\' meal and combo-menu items in quick-service restaurants.', 'https://en.wikipedia.org/wiki/Chicken_nugget'),
            ('Combo meal', 'The combo meal became a key part of fast-food marketing by bundling an entrée, side, and drink.', 'It made ordering faster while encouraging signature pairings and upsizing.', 'https://en.wikipedia.org/wiki/Value_meal'),
            ('Chipotle', 'Chipotle Mexican Grill helped popularize the fast-casual restaurant model in the United States.', 'Its assembly-line burrito format became highly influential in modern quick-service dining.', 'https://en.wikipedia.org/wiki/Chipotle_Mexican_Grill'),
            ('Shake Shack', 'Shake Shack grew from a New York hot dog cart into an internationally recognized burger chain.', 'Its rise showed how premium ingredients could fit into the fast-casual world.', 'https://en.wikipedia.org/wiki/Shake_Shack'),
            ('Panda Express', 'Panda Express brought American Chinese fast food to malls, airports, and quick-service diners across the United States.', 'Orange chicken became one of its best-known menu items.', 'https://en.wikipedia.org/wiki/Panda_Express'),
            ('Dunkin\'', 'Dunkin\' helped make coffee-and-doughnut stops part of daily fast-service culture.', 'Its focus on speed and convenience made it a commuter favorite for decades.', 'https://en.wikipedia.org/wiki/Dunkin%27'),
            ('Starbucks', 'Starbucks expanded café culture into a global quick-service coffee network.', 'Its size and customization model influenced how people think about grab-and-go drinks.', 'https://en.wikipedia.org/wiki/Starbucks'),
            ('Jack in the Box', 'Jack in the Box became known for late-night menus and drive-thru convenience.', 'It was one of the early chains built heavily around car culture.', 'https://en.wikipedia.org/wiki/Jack_in_the_Box'),
            ('A&W Restaurants', 'A&W Restaurants traces its roots to the era of roadside stands and root beer service.', 'It became one of the oldest surviving fast-food chains in the United States.', 'https://en.wikipedia.org/wiki/A%26W_Restaurants'),
            ('Little Caesars', 'Little Caesars became famous for its Hot-N-Ready model and speedy pizza pickup.', 'Its low-cost, high-volume strategy made it a major player in quick pizza service.', 'https://en.wikipedia.org/wiki/Little_Caesars'),
            ('Food delivery', 'Fast food adapted quickly to delivery apps and digital ordering in the 21st century.', 'Mobile ordering changed how people access quick meals without stepping inside a restaurant.', 'https://en.wikipedia.org/wiki/Online_food_ordering'),
        ],
    },
    'world-food': {
        'hobby': 'World Food',
        'entries': [
            ('Ramen', 'Ramen became one of Japan\'s most recognizable dishes and later a global comfort food favorite.', 'Its broths, noodles, and toppings vary by region and helped make it a star of world cuisine.', 'https://en.wikipedia.org/wiki/Ramen'),
            ('Jollof rice', 'Jollof rice is one of West Africa\'s best-known dishes and an important part of many celebrations.', 'Friendly debates about whose version is best helped make it especially famous around the world.', 'https://en.wikipedia.org/wiki/Jollof_rice'),
            ('Empanada', 'Empanadas appear in many countries with different fillings, shapes, and baking traditions.', 'They became one of the most recognizable hand-held foods in world cuisine.', 'https://en.wikipedia.org/wiki/Empanada'),
            ('Shawarma', 'Shawarma became one of the great street foods of the Middle East and later many other regions.', 'Its rotating spit cooking method made it both distinctive and widely imitated.', 'https://en.wikipedia.org/wiki/Shawarma'),
            ('Laksa', 'Laksa is a spicy noodle dish strongly associated with Southeast Asian food culture.', 'Its many regional versions help show the diversity of Malaysian, Singaporean, and Peranakan cooking.', 'https://en.wikipedia.org/wiki/Laksa'),
            ('Samosa', 'Samosas became famous across South Asia, the Middle East, and parts of Africa as a savory pastry snack.', 'Their portability and variety of fillings helped them travel widely across cultures.', 'https://en.wikipedia.org/wiki/Samosa'),
            ('Okonomiyaki', 'Okonomiyaki is a Japanese savory pancake with strong regional identities, especially in Osaka and Hiroshima.', 'Its name roughly suggests cooking it the way you like it, which fits its flexible toppings and style.', 'https://en.wikipedia.org/wiki/Okonomiyaki'),
            ('Adobo', 'Adobo is one of the dishes most closely associated with the Philippines.', 'Its soy, vinegar, and garlic-based flavor profile made it a global ambassador for Filipino cooking.', 'https://en.wikipedia.org/wiki/Philippine_adobo'),
            ('Goulash', 'Goulash became one of the best-known dishes tied to Hungarian food traditions.', 'Its paprika-rich stew style made it recognizable far beyond Central Europe.', 'https://en.wikipedia.org/wiki/Goulash'),
            ('Satay', 'Satay, with its grilled skewers and dipping sauces, became one of Southeast Asia\'s most recognizable foods.', 'It is especially associated with Indonesia but appears in several neighboring cuisines as well.', 'https://en.wikipedia.org/wiki/Satay'),
            ('Croissant', 'The croissant became one of the best-known pastries connected with French bakery culture.', 'Its flaky layers helped make it a breakfast icon in cafés around the world.', 'https://en.wikipedia.org/wiki/Croissant'),
            ('Manti', 'Manti are dumplings found across parts of Central Asia, the Caucasus, and the Middle East.', 'They show how one food idea can travel and take on different local forms across regions.', 'https://en.wikipedia.org/wiki/Manti_(food)'),
        ],
    },
    'world-culture': {
        'hobby': 'World Culture',
        'entries': [
            ('Holi', 'Holi is famous for colorful powders, music, and joyful spring celebrations across India and beyond.', 'It became one of the most visually recognizable festivals in world culture.', 'https://en.wikipedia.org/wiki/Holi'),
            ('Hanami', 'Hanami in Japan centers on gathering to appreciate cherry blossoms each spring.', 'The tradition shows how seasonal beauty can shape social life and cultural memory.', 'https://en.wikipedia.org/wiki/Hanami'),
            ('Carnival of Venice', 'The Carnival of Venice became world-famous for elaborate masks and historical costume traditions.', 'Its imagery remains one of the most recognizable symbols of festive European culture.', 'https://en.wikipedia.org/wiki/Carnival_of_Venice'),
            ('Midsummer', 'Midsummer celebrations across northern Europe highlight bonfires, flowers, dancing, and long daylight hours.', 'They remain a vivid example of seasonal tradition in world culture.', 'https://en.wikipedia.org/wiki/Midsummer'),
            ('San Fermín', 'San Fermín in Pamplona is globally known for the running of the bulls as well as music, parades, and religious tradition.', 'Its annual festivities became one of Spain\'s most recognized cultural events.', 'https://en.wikipedia.org/wiki/San_Ferm%C3%ADn'),
            ('Naadam', 'Naadam in Mongolia celebrates wrestling, horse racing, and archery as traditional national sports.', 'It remains one of the clearest expressions of Mongolian heritage and public celebration.', 'https://en.wikipedia.org/wiki/Naadam'),
            ('Kwanzaa', 'Kwanzaa was created in 1966 as a celebration of African American culture, community, and values.', 'Its candles, symbols, and shared principles made it a distinct modern cultural tradition.', 'https://en.wikipedia.org/wiki/Kwanzaa'),
            ('Batik', 'Batik is a wax-resist dyeing tradition associated especially with Indonesia and recognized by UNESCO.', 'Its patterns and textile artistry made it one of the world\'s best-known fabric traditions.', 'https://en.wikipedia.org/wiki/Batik'),
            ('Capoeira', 'Capoeira from Brazil blends martial arts, dance, music, and rhythm into one cultural practice.', 'Its movement and call-and-response performance style gave it a lasting global presence.', 'https://en.wikipedia.org/wiki/Capoeira'),
            ('Mariachi', 'Mariachi music became one of the best-known artistic traditions associated with Mexico.', 'Its instruments, clothing, and performance style made it instantly recognizable in world culture.', 'https://en.wikipedia.org/wiki/Mariachi'),
            ('Fado', 'Fado is a Portuguese music tradition known for emotional singing and themes of longing and fate.', 'Its mood and sound helped it become one of Portugal\'s strongest cultural signatures.', 'https://en.wikipedia.org/wiki/Fado'),
            ('Finnish sauna', 'Sauna culture is so central to Finland that it became one of the country\'s defining social traditions.', 'The practice shows how everyday habits can become a meaningful part of national culture.', 'https://en.wikipedia.org/wiki/Finnish_sauna'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f'{subject} is one of the best-known topics people encounter when exploring {hobby}.',
    lambda subject, detail, extra, hobby: f'Guides, articles, and documentaries about {hobby} often highlight {subject}.',
    lambda subject, detail, extra, hobby: f'Learning about {subject} gives a deeper look at the range and history within {hobby}.',
    lambda subject, detail, extra, hobby: f'{subject} shows how varied and memorable {hobby} can be across different regions.',
    lambda subject, detail, extra, hobby: f'Many travelers and readers remember {subject} as a standout part of {hobby}.',
    lambda subject, detail, extra, hobby: f'The story of {subject} helps connect history, identity, and everyday life inside {hobby}.',
    lambda subject, detail, extra, hobby: f'Books and travel features on {hobby} regularly return to {subject}.',
    lambda subject, detail, extra, hobby: f'The popularity of {subject} helped introduce many newcomers to {hobby}.',
    lambda subject, detail, extra, hobby: f'{subject} remains a classic example used when people talk about {hobby}.',
    lambda subject, detail, extra, hobby: f'Discussions of {hobby} often circle back to {subject} because of its lasting influence and recognition.',
]

for file_key, config in EXTRA_BATCH.items():
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
