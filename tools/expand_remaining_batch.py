from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    'academy-awards': {
        'hobby': 'Academy Awards',
        'entries': [
            ('Best Picture', 'Best Picture is the Academy Awards category most closely associated with overall film prestige.', 'Winning Best Picture can permanently change how a movie is remembered and marketed.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'),
            ('Best Director', 'Best Director recognizes the filmmaker judged to have delivered the strongest overall direction in a given year.', 'The category often shapes conversations about authorship, style, and industry respect.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director'),
            ('Walt Disney', 'Walt Disney won more competitive Oscars than any other individual in Academy Awards history.', 'His record remains one of the most famous statistics connected to the ceremony.', 'https://en.wikipedia.org/wiki/Walt_Disney'),
            ('Katharine Hepburn', 'Katharine Hepburn holds the acting record with four Academy Awards.', 'Her wins made her one of the most honored performers in Oscar history.', 'https://en.wikipedia.org/wiki/Katharine_Hepburn'),
            ('Meryl Streep', 'Meryl Streep holds the record for the most acting nominations at the Oscars.', 'Her long run of recognition turned her into one of the ceremony\'s defining names.', 'https://en.wikipedia.org/wiki/Meryl_Streep'),
            ('Ben-Hur', 'Ben-Hur helped set the Oscar record by winning 11 Academy Awards.', 'Its sweep made it one of the most successful films ever in awards history.', 'https://en.wikipedia.org/wiki/Ben-Hur_(1959_film)'),
            ('Titanic', 'Titanic tied the all-time Oscar win record with 11 Academy Awards.', 'Its combination of box-office success and awards dominance made it a historic phenomenon.', 'https://en.wikipedia.org/wiki/Titanic_(1997_film)'),
            ('The Lord of the Rings: The Return of the King', 'The Lord of the Rings: The Return of the King matched the 11-Oscar record and won every category in which it was nominated.', 'Its clean sweep became one of the most celebrated triumphs in Academy Awards history.', 'https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Return_of_the_King'),
            ('Parasite', 'Parasite became the first non-English-language film to win Best Picture at the Academy Awards.', 'That victory marked one of the most historic moments in Oscar history.', 'https://en.wikipedia.org/wiki/Parasite_(film)'),
            ('Hattie McDaniel', 'Hattie McDaniel became the first Black person to win an Academy Award when she won for Gone with the Wind.', 'Her victory remains a landmark moment in both film and civil-rights history.', 'https://en.wikipedia.org/wiki/Hattie_McDaniel'),
            ('Moonlight', 'Moonlight won Best Picture in one of the most dramatic finales in Oscars history after the famous envelope mix-up.', 'The film\'s win became one of the ceremony\'s most unforgettable live-TV moments.', 'https://en.wikipedia.org/wiki/Moonlight_(2016_film)'),
            ('Best Animated Feature', 'Best Animated Feature was introduced in 2001 to give animation a dedicated top-level Oscar category.', 'The addition acknowledged how important animated filmmaking had become globally.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Animated_Feature'),
            ('International Feature Film', 'The International Feature Film category helped increase the visibility of world cinema at the Oscars.', 'Its evolution reflected the Academy\'s growing global outlook.', 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_International_Feature_Film'),
            ('AMPAS', 'The Academy of Motion Picture Arts and Sciences is the organization that presents the Oscars each year.', 'Its membership spans multiple filmmaking branches including actors, directors, writers, and craftspeople.', 'https://en.wikipedia.org/wiki/Academy_of_Motion_Picture_Arts_and_Sciences'),
            ('Dolby Theatre', 'The Dolby Theatre in Hollywood has long served as the primary home of the modern Academy Awards ceremony.', 'Its stage and red carpet became central images of Oscar night.', 'https://en.wikipedia.org/wiki/Dolby_Theatre'),
        ],
    },
    'bible': {
        'hobby': 'The Bible',
        'entries': [
            ('Genesis 1:1', 'Genesis 1:1 opens with the words, "In the beginning God created the heaven and the earth."', 'That opening line is one of the best-known starting passages in all of scripture.', 'https://www.biblegateway.com/passage/?search=Genesis+1%3A1&version=KJV'),
            ('Genesis 1:3', 'Genesis 1:3 records the creation phrase, "Let there be light."', 'This verse became one of the Bible\'s most recognizable lines about creation and order.', 'https://www.biblegateway.com/passage/?search=Genesis+1%3A3&version=KJV'),
            ('Psalm 23', 'Psalm 23 begins with David\'s famous words, "The Lord is my shepherd; I shall not want."', 'The psalm remains one of the most quoted passages for comfort and trust.', 'https://www.biblegateway.com/passage/?search=Psalm+23&version=KJV'),
            ('Proverbs 3:5', 'Proverbs 3:5 says, "Trust in the Lord with all thine heart."', 'The verse is traditionally associated with wisdom teaching linked to Solomon.', 'https://www.biblegateway.com/passage/?search=Proverbs+3%3A5&version=KJV'),
            ('Ecclesiastes 3:1', 'Ecclesiastes 3:1 says, "To every thing there is a season, and a time to every purpose under the heaven."', 'Its phrasing became one of the most widely recognized poetic passages in the Bible.', 'https://www.biblegateway.com/passage/?search=Ecclesiastes+3%3A1&version=KJV'),
            ('Isaiah 40:31', 'Isaiah 40:31 promises that those who wait on the Lord "shall renew their strength."', 'The verse is frequently quoted for encouragement and endurance.', 'https://www.biblegateway.com/passage/?search=Isaiah+40%3A31&version=KJV'),
            ('Micah 6:8', 'Micah 6:8 calls people to "do justly, and to love mercy, and to walk humbly" with God.', 'It remains one of the best-known summary statements about ethical living in the Hebrew Bible.', 'https://www.biblegateway.com/passage/?search=Micah+6%3A8&version=KJV'),
            ('Matthew 5:9', 'In Matthew 5:9, Jesus says, "Blessed are the peacemakers."', 'This Beatitude is one of the most quoted lines from the Sermon on the Mount.', 'https://www.biblegateway.com/passage/?search=Matthew+5%3A9&version=KJV'),
            ('John 3:16', 'John 3:16 says, "For God so loved the world," making it one of the most quoted verses in the New Testament.', 'Many readers treat it as a concise summary of Christian belief.', 'https://www.biblegateway.com/passage/?search=John+3%3A16&version=KJV'),
            ('John 11:35', 'John 11:35 simply says, "Jesus wept," and is famous for being one of the shortest verses in many English translations.', 'Its brevity gave it unusual recognition even beyond regular Bible readers.', 'https://www.biblegateway.com/passage/?search=John+11%3A35&version=KJV'),
            ('John 14:6', 'In John 14:6, Jesus says, "I am the way, the truth, and the life."', 'That verse became one of the central identity statements quoted from the Gospels.', 'https://www.biblegateway.com/passage/?search=John+14%3A6&version=KJV'),
            ('1 Corinthians 13', 'Paul\'s teaching in 1 Corinthians 13 is among the Bible\'s most famous passages on love.', 'Lines from that chapter are often read at weddings and other ceremonies.', 'https://www.biblegateway.com/passage/?search=1+Corinthians+13&version=KJV'),
            ('Philippians 4:13', 'Paul writes in Philippians 4:13, "I can do all things through Christ which strengtheneth me."', 'It remains one of the most widely quoted encouragement verses in the New Testament.', 'https://www.biblegateway.com/passage/?search=Philippians+4%3A13&version=KJV'),
            ('Galatians 5:22-23', 'Galatians 5:22-23 lists the fruit of the Spirit, including love, joy, peace, and self-control.', 'The passage is regularly used to teach Christian character and spiritual growth.', 'https://www.biblegateway.com/passage/?search=Galatians+5%3A22-23&version=KJV'),
            ('Revelation 21:4', 'Revelation 21:4 promises that God "shall wipe away all tears from their eyes."', 'This verse is often quoted for hope, restoration, and the promise of a renewed creation.', 'https://www.biblegateway.com/passage/?search=Revelation+21%3A4&version=KJV'),
        ],
    },
    'college-basketball': {
        'hobby': 'College Basketball',
        'entries': [
            ('March Madness', 'March Madness became the nickname for the NCAA basketball tournaments and their annual drama.', 'The phrase now defines one of the most famous stretches in American sports.', 'https://en.wikipedia.org/wiki/March_Madness'),
            ('Final Four', 'The Final Four refers to the last four teams remaining in the NCAA tournament.', 'Reaching the Final Four is one of the biggest measures of college basketball success.', 'https://en.wikipedia.org/wiki/Final_Four'),
            ('John Wooden', 'John Wooden built UCLA into the sport\'s most famous dynasty by winning 10 national championships in 12 years.', 'His influence on college basketball remains enormous decades later.', 'https://en.wikipedia.org/wiki/John_Wooden'),
            ('UCLA Bruins', 'The UCLA Bruins became the defining dynasty program of men\'s college basketball.', 'Their historic title run under Wooden still shapes every modern comparison.', 'https://en.wikipedia.org/wiki/UCLA_Bruins_men%27s_basketball'),
            ('Duke–North Carolina rivalry', 'The Duke–North Carolina rivalry is one of the most famous in all of college sports.', 'Its games often carry conference, national, and emotional stakes all at once.', 'https://en.wikipedia.org/wiki/Duke%E2%80%93North_Carolina_rivalry'),
            ('Kentucky Wildcats', 'Kentucky built one of the deepest traditions in college basketball through championships, stars, and fan support.', 'Rupp Arena and Big Blue Nation became iconic parts of the sport.', 'https://en.wikipedia.org/wiki/Kentucky_Wildcats_men%27s_basketball'),
            ('Kansas Jayhawks', 'Kansas remains one of the sport\'s foundational powers and traces its history back to James Naismith.', 'Its program is deeply tied to the origins of basketball itself.', 'https://en.wikipedia.org/wiki/Kansas_Jayhawks_men%27s_basketball'),
            ('UConn Huskies', 'UConn became a modern powerhouse in both men\'s and women\'s college basketball.', 'The program\'s championship success made it one of the sport\'s premier brands.', 'https://en.wikipedia.org/wiki/UConn_Huskies_men%27s_basketball'),
            ('One Shining Moment', 'One Shining Moment became the signature song-and-highlight montage that closes the men\'s NCAA tournament broadcast.', 'For many fans, it signals the emotional end of March Madness every year.', 'https://en.wikipedia.org/wiki/One_Shining_Moment'),
            ('Cinderella team', 'A Cinderella team is a lower-seeded school that makes an unexpected NCAA tournament run.', 'Those surprise stories are a major reason the tournament remains so beloved.', 'https://en.wikipedia.org/wiki/Cinderella_(sports)'),
            ('Naismith Awards', 'The Naismith Awards honor top players and coaches in college basketball.', 'The name links the modern sport back to basketball inventor James Naismith.', 'https://en.wikipedia.org/wiki/Naismith_College_Player_of_the_Year'),
            ('Three-point line', 'The three-point line permanently changed college basketball strategy after arriving in the 1980s.', 'It opened the floor and made late comebacks more explosive and dramatic.', 'https://en.wikipedia.org/wiki/Three-point_field_goal'),
            ('Shot clock', 'The shot clock was adopted to keep teams from stalling and to increase pace in college basketball.', 'Its presence helped reshape how offenses and defenses manage possessions.', 'https://en.wikipedia.org/wiki/Shot_clock'),
            ('Selection Sunday', 'Selection Sunday reveals the NCAA tournament bracket and instantly launches national debate.', 'It is one of the most watched bracket-building events in U.S. sports.', 'https://en.wikipedia.org/wiki/Selection_Sunday'),
            ('Women\'s NCAA tournament', 'The women\'s NCAA tournament has grown rapidly in visibility, attendance, and cultural impact.', 'Its recent surge helped expand the national profile of college basketball as a whole.', 'https://en.wikipedia.org/wiki/NCAA_Division_I_women%27s_basketball_tournament'),
        ],
    },
    'college-hockey': {
        'hobby': 'College Hockey',
        'entries': [
            ('Frozen Four', 'The Frozen Four is the final stage of the NCAA men\'s ice hockey tournament.', 'Its championship weekend is the sport\'s biggest annual college showcase.', 'https://en.wikipedia.org/wiki/Frozen_Four'),
            ('Hobey Baker Award', 'The Hobey Baker Award honors the top player in NCAA men\'s hockey each season.', 'Winning it places a player among the most celebrated names in college hockey.', 'https://en.wikipedia.org/wiki/Hobey_Baker_Award'),
            ('Beanpot', 'The Beanpot is the famous annual Boston tournament featuring Boston College, Boston University, Harvard, and Northeastern.', 'Its local bragging rights make it one of the sport\'s most beloved traditions.', 'https://en.wikipedia.org/wiki/Beanpot'),
            ('Michigan Wolverines', 'Michigan built one of the richest traditions in college hockey with national titles and NHL-bound talent.', 'The program is a central name in almost any overview of the sport.', 'https://en.wikipedia.org/wiki/Michigan_Wolverines_men%27s_ice_hockey'),
            ('Minnesota Golden Gophers', 'Minnesota remains one of the flagship programs in college hockey history.', 'Its fan support and player pipeline helped shape the sport\'s identity.', 'https://en.wikipedia.org/wiki/Minnesota_Golden_Gophers_men%27s_ice_hockey'),
            ('North Dakota Fighting Hawks', 'North Dakota built one of the most respected programs in NCAA hockey with passionate support and sustained success.', 'Its home atmosphere is often mentioned among the best in the sport.', 'https://en.wikipedia.org/wiki/North_Dakota_Fighting_Hawks_men%27s_ice_hockey'),
            ('Denver Pioneers', 'Denver has become one of the winningest and most decorated programs in college hockey.', 'Its championships keep it near the center of any national-title conversation.', 'https://en.wikipedia.org/wiki/Denver_Pioneers_men%27s_ice_hockey'),
            ('Boston College Eagles', 'Boston College turned itself into a modern college-hockey power with repeated Frozen Four success.', 'The program is especially associated with elite recruiting and postseason consistency.', 'https://en.wikipedia.org/wiki/Boston_College_Eagles_men%27s_ice_hockey'),
            ('Boston University Terriers', 'Boston University is one of the sport\'s most tradition-rich programs and a staple of the Beanpot.', 'The Terriers have produced many major professional players over the years.', 'https://en.wikipedia.org/wiki/Boston_University_Terriers_men%27s_ice_hockey'),
            ('World Junior pipeline', 'College hockey became a major development path for players who also star in the World Junior Championship.', 'That crossover strengthened the sport\'s link to international competition.', 'https://en.wikipedia.org/wiki/World_Junior_Ice_Hockey_Championships'),
            ('Big Ten hockey', 'The creation of Big Ten hockey reshaped conference alignment and scheduling in the sport.', 'Realignment changed rivalries and recruiting geography across the NCAA.', 'https://en.wikipedia.org/wiki/Big_Ten_Conference_ice_hockey'),
            ('Single-elimination tournament', 'The NCAA hockey tournament is single elimination, which gives the sport strong upset potential every spring.', 'One hot goalie can completely change a championship run.', 'https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_ice_hockey_tournament'),
            ('Outdoor games', 'Outdoor college hockey games at football stadiums became major event spectacles in the 2000s and 2010s.', 'Those games blended nostalgia, school spirit, and winter pageantry.', 'https://en.wikipedia.org/wiki/Outdoor_ice_hockey'),
            ('Student sections', 'Student sections are a huge part of college hockey culture, with songs, chants, and constant noise.', 'Their atmosphere helps make many campus rinks feel unusually intense for amateur sports.', 'https://en.wikipedia.org/wiki/College_hockey_in_the_United_States'),
            ('Olympic and NHL paths', 'College hockey feeds both professional leagues and Olympic rosters, especially for American players.', 'That dual pathway gives the sport an unusual mix of school identity and elite development.', 'https://en.wikipedia.org/wiki/College_hockey_in_the_United_States'),
        ],
    },
    'comic-books': {
        'hobby': 'Comic Books',
        'entries': [
            ('Action Comics #1', 'Action Comics #1 introduced Superman and is often treated as the beginning of the superhero boom.', 'It remains one of the most famous and valuable comic books ever printed.', 'https://en.wikipedia.org/wiki/Action_Comics_1'),
            ('Detective Comics #27', 'Detective Comics #27 introduced Batman and helped cement DC\'s early importance in comics history.', 'Its place in comic-book collecting and superhero mythology is enormous.', 'https://en.wikipedia.org/wiki/Detective_Comics_27'),
            ('Fantastic Four', 'Fantastic Four helped kick off Marvel\'s modern age of superhero storytelling in the early 1960s.', 'The team\'s family dynamics gave superhero comics a different emotional texture.', 'https://en.wikipedia.org/wiki/Fantastic_Four'),
            ('Spider-Man', 'Spider-Man became one of the most beloved comic-book heroes because his problems felt both heroic and everyday.', 'Peter Parker helped make Marvel\'s style of flawed superheroes widely relatable.', 'https://en.wikipedia.org/wiki/Spider-Man'),
            ('X-Men', 'X-Men used mutant powers and prejudice themes to explore fear, identity, and social conflict.', 'That metaphorical depth helped make the franchise one of comics\' richest worlds.', 'https://en.wikipedia.org/wiki/X-Men'),
            ('Watchmen', 'Watchmen pushed superhero comics toward darker and more formally ambitious storytelling.', 'Its structure and themes made it a permanent reference point in comic criticism.', 'https://en.wikipedia.org/wiki/Watchmen'),
            ('The Dark Knight Returns', 'The Dark Knight Returns helped redefine Batman for a darker modern era.', 'Frank Miller\'s work became one of the most influential superhero comics of the 1980s.', 'https://en.wikipedia.org/wiki/Batman:_The_Dark_Knight_Returns'),
            ('Maus', 'Maus became the first graphic novel to win a Pulitzer Prize.', 'Art Spiegelman\'s work showed that comics could carry major historical and literary weight.', 'https://en.wikipedia.org/wiki/Maus'),
            ('Sandman', 'The Sandman blended mythology, fantasy, horror, and literary ambition into one of comics\' most admired series.', 'Neil Gaiman\'s title helped expand perceptions of what mainstream comics could do.', 'https://en.wikipedia.org/wiki/The_Sandman_(comic_book)'),
            ('Akira', 'Akira became one of the most internationally influential manga titles of the modern era.', 'Its success helped many readers discover the scale and power of Japanese comics.', 'https://en.wikipedia.org/wiki/Akira_(manga)'),
            ('Manga', 'Manga became one of the biggest forces in global comics publishing and reading culture.', 'Its success reshaped bookstore shelves, fandom, and adaptation trends worldwide.', 'https://en.wikipedia.org/wiki/Manga'),
            ('Comic-Con', 'Comic-Con International grew into one of the most famous fan conventions connected to comics and pop culture.', 'Its rise showed how central comic-book fandom had become to entertainment culture.', 'https://en.wikipedia.org/wiki/San_Diego_Comic-Con'),
            ('Comics Code Authority', 'The Comics Code Authority heavily shaped mainstream American comics for decades after 1954.', 'Its restrictions affected what kinds of stories publishers felt comfortable printing.', 'https://en.wikipedia.org/wiki/Comics_Code_Authority'),
            ('Graphic novel', 'The term graphic novel helped many readers approach longer comic works as complete books rather than only serialized issues.', 'The format opened space for memoir, journalism, literary fiction, and more.', 'https://en.wikipedia.org/wiki/Graphic_novel'),
            ('Saga', 'Saga became one of the most acclaimed modern creator-owned comics of the 21st century.', 'Its success showed that readers still strongly support original worlds outside superhero universes.', 'https://en.wikipedia.org/wiki/Saga_(comics)'),
        ],
    },
    'dancing': {
        'hobby': 'Dancing',
        'entries': [
            ('Ballet', 'Ballet became one of the world\'s most influential formal dance traditions.', 'Its discipline, pointe work, and storytelling shaped stage dance globally.', 'https://en.wikipedia.org/wiki/Ballet'),
            ('Modern dance', 'Modern dance emerged partly in rebellion against the strict rules of classical ballet.', 'Its emphasis on expression and grounded movement changed 20th-century performance.', 'https://en.wikipedia.org/wiki/Modern_dance'),
            ('Martha Graham', 'Martha Graham became one of the most influential pioneers of modern dance.', 'Her technique and choreography still shape dance training around the world.', 'https://en.wikipedia.org/wiki/Martha_Graham'),
            ('Tap dance', 'Tap dance combines rhythm, percussion, and fast footwork into a distinct performance style.', 'Its roots connect African and European movement traditions in American culture.', 'https://en.wikipedia.org/wiki/Tap_dance'),
            ('Breakdancing', 'Breakdancing grew out of hip-hop culture in the Bronx and became one of street dance\'s biggest global forms.', 'Its athletic moves later carried the style all the way to the Olympics.', 'https://en.wikipedia.org/wiki/Breakdancing'),
            ('Salsa', 'Salsa dance developed through Cuban and Puerto Rican influences and flourished in New York\'s Latin music scene.', 'Its social energy made it one of the most popular partner dances in the world.', 'https://en.wikipedia.org/wiki/Salsa_(dance)'),
            ('Tango', 'Tango developed in Argentina and Uruguay and became one of the world\'s most famous partner dances.', 'Its music, embrace, and dramatic style gave it a lasting place in global dance culture.', 'https://en.wikipedia.org/wiki/Tango'),
            ('Flamenco', 'Flamenco blends singing, guitar, clapping, and dance into one of Spain\'s most iconic art forms.', 'Its emotional intensity made it instantly recognizable worldwide.', 'https://en.wikipedia.org/wiki/Flamenco'),
            ('Samba', 'Samba is closely associated with Brazil and the spectacle of Rio Carnival.', 'Its rhythm and motion helped make it one of the best-known dance traditions in the world.', 'https://en.wikipedia.org/wiki/Samba_(Brazilian_dance)'),
            ('Waltz', 'The waltz was once considered scandalous because partners danced in a close embrace.', 'Over time it became one of the most enduring ballroom dance forms.', 'https://en.wikipedia.org/wiki/Waltz'),
            ('Kathak', 'Kathak is a classical dance from India known for spins, storytelling, and intricate footwork.', 'It remains one of the major pillars of Indian classical dance.', 'https://en.wikipedia.org/wiki/Kathak'),
            ('Bharatanatyam', 'Bharatanatyam is one of the oldest classical dance traditions of India.', 'Its gestures, rhythm, and expressiveness made it one of the most respected stage forms in the world.', 'https://en.wikipedia.org/wiki/Bharatanatyam'),
            ('Hula', 'Hula uses movement and chant to tell stories within Hawaiian tradition.', 'It remains one of the best-known dance forms linked to place, memory, and ritual.', 'https://en.wikipedia.org/wiki/Hula'),
            ('Contemporary dance', 'Contemporary dance blends elements of ballet, modern dance, jazz, and improvisation.', 'Its flexibility made it a major force in current stage choreography.', 'https://en.wikipedia.org/wiki/Contemporary_dance'),
            ('International Dance Day', 'International Dance Day celebrates dance as a universal language every year on April 29.', 'The occasion highlights just how many cultures treat dance as a central art form.', 'https://en.wikipedia.org/wiki/International_Dance_Day'),
        ],
    },
    'models': {
        'hobby': 'Fashion Models',
        'entries': [
            ('Twiggy', 'Twiggy became one of the defining modeling faces of the 1960s.', 'Her look helped shape an entire era of fashion imagery.', 'https://en.wikipedia.org/wiki/Twiggy'),
            ('Naomi Campbell', 'Naomi Campbell became one of the biggest supermodels in modern fashion history.', 'Her runway presence and barrier-breaking magazine covers made her a landmark figure.', 'https://en.wikipedia.org/wiki/Naomi_Campbell'),
            ('Cindy Crawford', 'Cindy Crawford helped define the supermodel era with high-profile campaigns and magazine covers.', 'Her image became synonymous with 1990s fashion celebrity.', 'https://en.wikipedia.org/wiki/Cindy_Crawford'),
            ('Linda Evangelista', 'Linda Evangelista became famous for her versatility and commanding editorial presence.', 'She remains one of the names most associated with the classic supermodel era.', 'https://en.wikipedia.org/wiki/Linda_Evangelista'),
            ('Christy Turlington', 'Christy Turlington became a major fashion icon through editorial work, runway appearances, and beauty campaigns.', 'Her elegance helped make her a lasting reference point in modeling history.', 'https://en.wikipedia.org/wiki/Christy_Turlington'),
            ('Claudia Schiffer', 'Claudia Schiffer rose to global fame and became one of the most recognized models of the 1990s.', 'Her campaigns and covers made her a central figure of the supermodel generation.', 'https://en.wikipedia.org/wiki/Claudia_Schiffer'),
            ('Tyra Banks', 'Tyra Banks helped break barriers for Black models in fashion magazines and major campaigns.', 'She later expanded her influence into television, business, and media.', 'https://en.wikipedia.org/wiki/Tyra_Banks'),
            ('Kate Moss', 'Kate Moss became a defining face of 1990s fashion and helped popularize a very different model aesthetic.', 'Her influence reached both runway and street style culture.', 'https://en.wikipedia.org/wiki/Kate_Moss'),
            ('Gisele Bündchen', 'Gisele Bündchen became one of the highest-earning and most globally recognized models of the 2000s.', 'Her success helped usher in a new era of international supermodel branding.', 'https://en.wikipedia.org/wiki/Gisele_B%C3%BCndchen'),
            ('Iman', 'Iman became a major fashion and beauty icon while also expanding into entrepreneurship.', 'Her career showed how modeling could lead to lasting influence beyond the runway.', 'https://en.wikipedia.org/wiki/Iman_(model)'),
            ('Heidi Klum', 'Heidi Klum turned modeling success into a broad entertainment and business career.', 'Her name became especially linked to both fashion and mainstream television.', 'https://en.wikipedia.org/wiki/Heidi_Klum'),
            ('Adriana Lima', 'Adriana Lima became one of the most recognizable runway and lingerie models of her era.', 'Her long high-profile run made her a defining face in 2000s fashion imagery.', 'https://en.wikipedia.org/wiki/Adriana_Lima'),
            ('Fashion Week', 'Fashion Week in New York, London, Milan, and Paris remains central to the modeling world.', 'Those events showcase how runway presentation helps shape seasonal style trends.', 'https://en.wikipedia.org/wiki/Fashion_week'),
            ('Vogue', 'Vogue magazine became one of the most important publication platforms for fashion models and editorial photography.', 'Appearing on its cover is often treated as a major career milestone.', 'https://en.wikipedia.org/wiki/Vogue_(magazine)'),
            ('Runway walk', 'The runway walk is a specialized performance skill that can vary greatly from one designer to another.', 'A model\'s posture, timing, and attitude often matter as much as still photography.', 'https://en.wikipedia.org/wiki/Model_(person)'),
        ],
    },
    'mythology': {
        'hobby': 'Mythology',
        'entries': [
            ('Zeus', 'Zeus became the king of the gods in Greek mythology and ruler of the sky and thunder.', 'He is one of the first names many people think of when mythology is mentioned.', 'https://en.wikipedia.org/wiki/Zeus'),
            ('Athena', 'Athena represented wisdom, strategy, and craft in Greek mythology.', 'Her place as both warrior and thinker made her one of the most admired classical deities.', 'https://en.wikipedia.org/wiki/Athena'),
            ('Thor', 'Thor became one of the most famous gods in Norse mythology through his hammer Mjolnir and storm powers.', 'His stories helped keep Norse myth central in modern pop culture.', 'https://en.wikipedia.org/wiki/Thor'),
            ('Odin', 'Odin stands at the center of Norse mythology as a god of wisdom, war, and poetry.', 'His search for knowledge made him one of myth\'s most layered figures.', 'https://en.wikipedia.org/wiki/Odin'),
            ('Loki', 'Loki became one of mythology\'s best-known trickster figures through Norse stories of chaos and cunning.', 'His unpredictable role helped make him one of the most discussed gods in modern retellings.', 'https://en.wikipedia.org/wiki/Loki'),
            ('Medusa', 'Medusa turned into one of mythology\'s most recognizable figures through stories of danger, tragedy, and transformation.', 'Her snake-haired image remains one of the most enduring symbols in classical myth.', 'https://en.wikipedia.org/wiki/Medusa'),
            ('Minotaur', 'The Minotaur stands at the center of the Greek tale of the Labyrinth and Theseus.', 'That monster-and-maze story remains one of mythology\'s great symbolic adventures.', 'https://en.wikipedia.org/wiki/Minotaur'),
            ('Phoenix', 'The phoenix became a universal symbol of rebirth because of legends about rising from ashes.', 'Its mythic power carried far beyond the cultures where the story first appeared.', 'https://en.wikipedia.org/wiki/Phoenix_(mythology)'),
            ('Anansi', 'Anansi stories from West Africa made the spider trickster one of the great mythic storytellers of the world.', 'His tales traveled widely and shaped folklore across the African diaspora.', 'https://en.wikipedia.org/wiki/Anansi'),
            ('Amaterasu', 'Amaterasu holds a central place in Japanese mythology as the sun goddess.', 'Her stories remain vital to Shinto tradition and Japanese cultural memory.', 'https://en.wikipedia.org/wiki/Amaterasu'),
            ('Osiris', 'Osiris became one of the key figures of Egyptian mythology through stories of death, judgment, and renewal.', 'His myth helped shape Egyptian ideas about the afterlife.', 'https://en.wikipedia.org/wiki/Osiris'),
            ('Isis', 'Isis became one of the most revered goddesses in Egyptian mythology and later beyond Egypt as well.', 'Her links to magic, devotion, and restoration gave her wide influence.', 'https://en.wikipedia.org/wiki/Isis'),
            ('Hercules', 'Hercules became one of the best-known heroes of classical mythology through his famous labors.', 'His stories of strength and suffering still appear in countless retellings.', 'https://en.wikipedia.org/wiki/Hercules'),
            ('King Arthur', 'King Arthur blends history, folklore, and mythology into one of the great legendary traditions of Britain.', 'Stories of Camelot, Merlin, and the Round Table remain major mythic touchstones.', 'https://en.wikipedia.org/wiki/King_Arthur'),
            ('Ragnarök', 'Ragnarök describes the catastrophic final battle and renewal of the world in Norse mythology.', 'It remains one of the most dramatic end-of-the-world stories in mythic literature.', 'https://en.wikipedia.org/wiki/Ragnar%C3%B6k'),
        ],
    },
    'science': {
        'hobby': 'Science',
        'entries': [
            ('Albert Einstein', 'Albert Einstein helped transform modern physics through relativity and work on light and matter.', 'His name became almost synonymous with scientific genius in popular culture.', 'https://en.wikipedia.org/wiki/Albert_Einstein'),
            ('Isaac Newton', 'Isaac Newton laid the foundations of classical mechanics and universal gravitation.', 'His laws of motion remained central to physics education for centuries.', 'https://en.wikipedia.org/wiki/Isaac_Newton'),
            ('Marie Curie', 'Marie Curie became a pioneering scientist in the study of radioactivity.', 'She was the first person to win Nobel Prizes in two different scientific fields.', 'https://en.wikipedia.org/wiki/Marie_Curie'),
            ('Charles Darwin', 'Charles Darwin reshaped biology through the theory of evolution by natural selection.', 'On the Origin of Species became one of the most influential books in scientific history.', 'https://en.wikipedia.org/wiki/Charles_Darwin'),
            ('Galileo Galilei', 'Galileo Galilei helped transform astronomy through telescopic observation and experimental thinking.', 'He is often called the father of observational astronomy.', 'https://en.wikipedia.org/wiki/Galileo_Galilei'),
            ('Nikola Tesla', 'Nikola Tesla became famous for major contributions to alternating current electrical systems.', 'His legacy continues to fascinate both engineers and popular culture alike.', 'https://en.wikipedia.org/wiki/Nikola_Tesla'),
            ('Rosalind Franklin', 'Rosalind Franklin\'s X-ray work was crucial to understanding the structure of DNA.', 'Her scientific role is now recognized as vital to one of biology\'s biggest breakthroughs.', 'https://en.wikipedia.org/wiki/Rosalind_Franklin'),
            ('Carl Sagan', 'Carl Sagan helped popularize science through books, television, and cosmic perspective.', 'His ability to make the universe feel both vast and personal inspired generations of readers.', 'https://en.wikipedia.org/wiki/Carl_Sagan'),
            ('Stephen Hawking', 'Stephen Hawking became one of the world\'s best-known theoretical physicists through his work on black holes and cosmology.', 'His writing and public presence brought difficult ideas to wide audiences.', 'https://en.wikipedia.org/wiki/Stephen_Hawking'),
            ('Richard Feynman', 'Richard Feynman became famous for his work in quantum electrodynamics and for his energetic teaching style.', 'His lectures and stories helped make advanced physics feel unusually vivid.', 'https://en.wikipedia.org/wiki/Richard_Feynman'),
            ('Hubble Space Telescope', 'The Hubble Space Telescope transformed astronomy by sending back extraordinarily detailed images of the universe.', 'Its discoveries helped refine our understanding of cosmic distance, age, and structure.', 'https://en.wikipedia.org/wiki/Hubble_Space_Telescope'),
            ('DNA', 'DNA carries the genetic instructions used in the growth and function of living organisms.', 'Understanding its structure became one of the central achievements of modern biology.', 'https://en.wikipedia.org/wiki/DNA'),
            ('Black hole', 'Black holes became one of science\'s most famous and fascinating cosmic concepts.', 'They sit at the intersection of gravity, relativity, and some of the biggest unsolved questions in physics.', 'https://en.wikipedia.org/wiki/Black_hole'),
            ('Periodic table', 'The periodic table organizes chemical elements in a way that reveals powerful patterns in matter.', 'It remains one of the most recognizable tools in all of science education.', 'https://en.wikipedia.org/wiki/Periodic_table'),
            ('Photosynthesis', 'Photosynthesis allows plants and some other organisms to turn light into usable chemical energy.', 'The process supports much of life on Earth by helping generate oxygen and food chains.', 'https://en.wikipedia.org/wiki/Photosynthesis'),
        ],
    },
    'super-friends': {
        'hobby': 'Super Friends',
        'entries': [
            ('Hall of Justice', 'The Hall of Justice became one of the most recognizable headquarters in superhero animation.', 'Its design helped give Super Friends a visual identity all its own.', 'https://en.wikipedia.org/wiki/Hall_of_Justice'),
            ('Wonder Twins', 'The Wonder Twins quickly became pop-culture icons after joining Super Friends.', 'Their transformation powers and catchphrase made them unforgettable to many viewers.', 'https://en.wikipedia.org/wiki/Wonder_Twins'),
            ('Legion of Doom', 'The Legion of Doom gave Super Friends one of the great all-villain teams in animated superhero history.', 'Their swamp-like headquarters became nearly as memorable as the heroes\' base.', 'https://en.wikipedia.org/wiki/Legion_of_Doom'),
            ('Challenge of the Super Friends', 'Challenge of the Super Friends is the version many fans remember most vividly because of its hero-versus-villain format.', 'It brought together major DC heroes and villains in a larger event style.', 'https://en.wikipedia.org/wiki/Challenge_of_the_Superfriends'),
            ('Marvin and Wendy', 'Marvin and Wendy were created for the cartoon to help younger viewers connect with the stories.', 'Their presence showed how strongly the series was designed for Saturday-morning adventure.', 'https://en.wikipedia.org/wiki/Wendy,_Marvin_and_Wonder_Dog'),
            ('Wonder Dog', 'Wonder Dog added extra comic relief and kid-friendly energy to the early version of Super Friends.', 'The character became one of the more unusual pieces of the show\'s original lineup.', 'https://en.wikipedia.org/wiki/Wendy,_Marvin_and_Wonder_Dog'),
            ('Casey Kasem as Robin', 'Casey Kasem voiced Robin on Super Friends before becoming even more famous as a radio host.', 'His performance helped define the boy wonder for many cartoon fans.', 'https://en.wikipedia.org/wiki/Casey_Kasem'),
            ('Danny Dark as Superman', 'Danny Dark became one of the defining animated voices of Superman through Super Friends.', 'For many viewers, his voice was inseparable from the character.', 'https://en.wikipedia.org/wiki/Danny_Dark'),
            ('Meanwhile, at the Hall of Justice', 'The phrase "Meanwhile, at the Hall of Justice" became one of the show\'s most recognizable narration setups.', 'It remains a nostalgic line for generations of superhero-cartoon fans.', 'https://en.wikipedia.org/wiki/Hall_of_Justice'),
            ('Hanna-Barbera', 'Hanna-Barbera produced Super Friends and helped translate DC\'s biggest heroes into animated TV form.', 'The studio\'s style shaped how an entire generation first encountered the Justice League.', 'https://en.wikipedia.org/wiki/Hanna-Barbera'),
        ],
    },
    'x-men': {
        'hobby': 'X-Men',
        'entries': [
            ('Professor X', 'Professor X leads the X-Men with a vision of coexistence between mutants and humans.', 'His school for gifted youngsters became one of Marvel\'s defining institutions.', 'https://en.wikipedia.org/wiki/Professor_X'),
            ('Magneto', 'Magneto remains one of the most layered comic-book antagonists because his goals and methods are so morally complicated.', 'His conflict with Professor X sits at the heart of many of the franchise\'s best stories.', 'https://en.wikipedia.org/wiki/Magneto_(Marvel_Comics)'),
            ('Storm', 'Storm became one of the most powerful and admired mutant heroes in Marvel history.', 'Her leadership and weather powers made her central to the team\'s identity.', 'https://en.wikipedia.org/wiki/Storm_(Marvel_Comics)'),
            ('Wolverine', 'Wolverine turned into one of the most popular X-Men because of his ferocity, healing factor, and moral complexity.', 'His catchphrases and claws made him one of Marvel\'s biggest breakout stars.', 'https://en.wikipedia.org/wiki/Wolverine_(character)'),
            ('Dark Phoenix Saga', 'The Dark Phoenix Saga is widely considered one of the greatest comic-book storylines ever written.', 'Its emotional stakes made it a defining chapter in X-Men history.', 'https://en.wikipedia.org/wiki/The_Dark_Phoenix_Saga'),
            ('Days of Future Past', 'Days of Future Past became one of the franchise\'s most influential time-travel stories.', 'Its dystopian vision helped shape later X-Men comics, cartoons, and films.', 'https://en.wikipedia.org/wiki/Days_of_Future_Past'),
            ('X-Men: The Animated Series', 'X-Men: The Animated Series introduced millions of viewers to the team in the 1990s.', 'Its theme music and faithful story arcs helped make it one of the most beloved superhero cartoons ever.', 'https://en.wikipedia.org/wiki/X-Men:_The_Animated_Series'),
            ('Nightcrawler', 'Nightcrawler became a fan favorite because of his teleportation, faith, and gentle personality.', 'The contrast between his demonic appearance and kind spirit made him especially memorable.', 'https://en.wikipedia.org/wiki/Nightcrawler_(character)'),
            ('Rogue', 'Rogue\'s ability to absorb memories and powers made her one of the franchise\'s most emotionally complex characters.', 'Her struggle with physical touch gave many of her stories unusual depth.', 'https://en.wikipedia.org/wiki/Rogue_(Marvel_Comics)'),
            ('Gambit', 'Gambit added swagger and kinetic-card combat to the X-Men lineup in the late 20th century.', 'His Cajun accent and charged playing cards helped make him a 1990s favorite.', 'https://en.wikipedia.org/wiki/Gambit_(Marvel_Comics)'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f"{subject} is one of the standout topics people mention when discussing {hobby}.",
    lambda subject, detail, extra, hobby: f"Any overview of {hobby} usually includes {subject}.",
    lambda subject, detail, extra, hobby: f"{subject} helped define the legacy and reputation of {hobby}.",
    lambda subject, detail, extra, hobby: f"Fans exploring {hobby} are often encouraged to learn about {subject}.",
    lambda subject, detail, extra, hobby: f"The story of {hobby} is hard to explain without mentioning {subject}.",
    lambda subject, detail, extra, hobby: f"Retrospectives and fan discussions about {hobby} frequently return to {subject}.",
    lambda subject, detail, extra, hobby: f"For many fans, {subject} captures part of why {hobby} stays so memorable.",
    lambda subject, detail, extra, hobby: f"Lists, articles, and guides about {hobby} often highlight {subject}.",
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
    print(f'{file_key}\t{len(current["facts"])} facts')
