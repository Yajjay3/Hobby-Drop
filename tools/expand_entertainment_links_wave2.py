from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    'college-hockey': {
        'hobby': 'College Hockey',
        'entries': [
            ('Frozen Four', 'The Frozen Four is the championship weekend of the NCAA men’s ice hockey tournament.', 'It became one of the biggest annual events in college hockey.', 'https://en.wikipedia.org/wiki/Frozen_Four'),
            ('NCAA Division I men\'s ice hockey tournament', 'The NCAA Division I men’s ice hockey tournament decides the national champion in college hockey.', 'Its bracket format made it one of the key traditions of the sport.', 'https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_ice_hockey_tournament'),
            ('Beanpot', 'The Beanpot is a famous Boston college hockey tournament involving local rivals.', 'It became one of the sport’s best-known annual showcases.', 'https://en.wikipedia.org/wiki/Beanpot'),
            ('Hockey East', 'Hockey East is one of the major conferences in men’s and women’s college hockey.', 'Its teams have played a major role in recent national success.', 'https://en.wikipedia.org/wiki/Hockey_East_Association'),
            ('ECAC Hockey', 'ECAC Hockey is one of the oldest conferences connected with college hockey in the United States.', 'Its membership gave the sport deep roots in the Northeast.', 'https://en.wikipedia.org/wiki/ECAC_Hockey'),
            ('Michigan Wolverines men\'s ice hockey', 'Michigan built one of the most successful traditions in college hockey history.', 'Its titles and alumni made the program one of the sport’s standard-bearers.', 'https://en.wikipedia.org/wiki/Michigan_Wolverines_men%27s_ice_hockey'),
            ('North Dakota Fighting Hawks men\'s ice hockey', 'North Dakota developed one of the strongest fan cultures and histories in college hockey.', 'The program became one of the most recognizable in the NCAA game.', 'https://en.wikipedia.org/wiki/North_Dakota_Fighting_Hawks_men%27s_ice_hockey'),
            ('Boston University Terriers men\'s ice hockey', 'Boston University remains one of the best-known programs in college hockey.', 'Its city rivalry games and tournament runs helped define the sport for many fans.', 'https://en.wikipedia.org/wiki/Boston_University_Terriers_men%27s_ice_hockey'),
        ],
    },
    'college-basketball': {
        'hobby': 'College Basketball',
        'entries': [
            ('March Madness', 'March Madness became the popular nickname for the NCAA basketball tournament.', 'It is one of the most famous postseason events in American sports.', 'https://en.wikipedia.org/wiki/March_Madness'),
            ('NCAA Division I men\'s basketball tournament', 'The NCAA Division I men’s basketball tournament crowns the national champion through a single-elimination bracket.', 'Its upsets and buzzer-beaters made it central to college basketball culture.', 'https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_basketball_tournament'),
            ('Final Four', 'The Final Four represents the semifinal and championship weekend of the NCAA tournament.', 'It became one of the signature phrases in college basketball.', 'https://en.wikipedia.org/wiki/Final_Four'),
            ('Duke–North Carolina rivalry', 'The Duke–North Carolina rivalry became one of the most famous matchups in college basketball.', 'Its intensity and history made it a major draw for fans every season.', 'https://en.wikipedia.org/wiki/Duke%E2%80%93North_Carolina_rivalry'),
            ('Kentucky Wildcats men\'s basketball', 'Kentucky built one of the largest and most successful traditions in college basketball.', 'Its championships and fan support made it a constant presence in the sport.', 'https://en.wikipedia.org/wiki/Kentucky_Wildcats_men%27s_basketball'),
            ('UCLA Bruins men\'s basketball', 'UCLA became legendary in college basketball through its championship run under John Wooden.', 'The program’s success turned it into one of the sport’s benchmark teams.', 'https://en.wikipedia.org/wiki/UCLA_Bruins_men%27s_basketball'),
            ('John Wooden', 'John Wooden became one of the most respected coaches in the history of college basketball.', 'His leadership at UCLA shaped the sport for generations.', 'https://en.wikipedia.org/wiki/John_Wooden'),
            ('Cinderella team', 'A Cinderella team is an unexpected underdog that makes a deep run in the NCAA tournament.', 'That idea became one of the defining thrills of college basketball each March.', 'https://en.wikipedia.org/wiki/Cinderella_(sports)'),
        ],
    },
    'super-friends': {
        'hobby': 'Super Friends',
        'entries': [
            ('Super Friends', 'Super Friends was a long-running animated DC series produced by Hanna-Barbera.', 'It introduced many younger viewers to heroes like Superman, Batman, and Wonder Woman.', 'https://en.wikipedia.org/wiki/Super_Friends'),
            ('Hall of Justice', 'The Hall of Justice became one of the most recognizable headquarters in Super Friends.', 'Its design helped give the team a memorable home base for generations of viewers.', 'https://en.wikipedia.org/wiki/Hall_of_Justice'),
            ('Wonder Twins', 'The Wonder Twins became some of the most memorable original characters associated with Super Friends.', 'Their catchphrase made them especially easy for fans to remember.', 'https://en.wikipedia.org/wiki/Wonder_Twins'),
            ('Legion of Doom', 'The Legion of Doom gave Super Friends one of its most famous villain teams.', 'It remains one of the best-known animated groups of DC villains.', 'https://en.wikipedia.org/wiki/Legion_of_Doom'),
            ('Apache Chief', 'Apache Chief was one of the original hero characters introduced in the Super Friends cartoons.', 'He remains part of the show’s distinctive animated-era identity.', 'https://en.wikipedia.org/wiki/Apache_Chief'),
            ('Gleek', 'Gleek, the Wonder Twins’ space monkey, became one of the most recognizable side characters in Super Friends.', 'The character helped add humor and charm to the series.', 'https://en.wikipedia.org/wiki/Gleek'),
            ('Aquaman', 'Aquaman was a regular member of the Super Friends lineup and helped define the team’s animated roster.', 'His presence made the show feel like a true all-star DC gathering.', 'https://en.wikipedia.org/wiki/Aquaman'),
            ('Justice League', 'Super Friends helped bring a younger, animated version of the Justice League to television audiences.', 'It played a big role in how many fans first learned the team concept.', 'https://en.wikipedia.org/wiki/Justice_League'),
        ],
    },
    'voted-best-movies': {
        'hobby': 'Voted As The Best',
        'entries': [
            ('Citizen Kane', 'Citizen Kane is often listed near the top of major best-movie polls and rankings.', 'Its reputation made it a standard reference point in film criticism.', 'https://en.wikipedia.org/wiki/Citizen_Kane'),
            ('The Godfather', 'The Godfather became one of the films most frequently named among the greatest ever made.', 'Its influence on crime drama and popular culture kept it near the top of many lists.', 'https://en.wikipedia.org/wiki/The_Godfather'),
            ('Casablanca', 'Casablanca is regularly ranked among the most beloved and acclaimed classic films.', 'Its dialogue and performances helped it remain a fixture on all-time-great lists.', 'https://en.wikipedia.org/wiki/Casablanca_(film)'),
            ('Vertigo', 'Vertigo rose dramatically in critical rankings and has even topped some greatest-film polls.', 'Its visual style and psychological depth made it a major favorite among critics.', 'https://en.wikipedia.org/wiki/Vertigo_(film)'),
            ('AFI\'s 100 Years...100 Movies', 'AFI’s 100 Years...100 Movies became one of the best-known American film ranking projects.', 'It helped shape popular debate about which movies belong in the all-time top tier.', 'https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies'),
            ('Sight & Sound', 'Sight & Sound polls are among the most influential international movie rankings in film culture.', 'Directors and critics often treat them as a serious measure of long-term reputation.', 'https://en.wikipedia.org/wiki/Sight_%26_Sound'),
            ('The Shawshank Redemption', 'The Shawshank Redemption became one of the highest-rated films in popular audience-based rankings.', 'Its word-of-mouth reputation kept it near the top of viewer polls for years.', 'https://en.wikipedia.org/wiki/The_Shawshank_Redemption'),
            ('Seven Samurai', 'Seven Samurai remains one of the most admired films in world cinema and often appears on best-ever lists.', 'Its storytelling and influence reached far beyond Japanese film history.', 'https://en.wikipedia.org/wiki/Seven_Samurai'),
        ],
    },
    '2000s-movies': {
        'hobby': '2000s-2026 Movies',
        'entries': [
            ('The Lord of the Rings film trilogy', 'The Lord of the Rings trilogy became one of the defining achievements of 2000s blockbuster filmmaking.', 'Its scale and awards success helped define the era.', 'https://en.wikipedia.org/wiki/The_Lord_of_the_Rings_(film_series)'),
            ('Harry Potter films', 'The Harry Potter films became one of the most successful movie franchises of the 2000s and 2010s.', 'They kept fantasy cinema at the center of popular culture for years.', 'https://en.wikipedia.org/wiki/Harry_Potter_(film_series)'),
            ('The Dark Knight', 'The Dark Knight became one of the most discussed and acclaimed superhero films of the 2000s.', 'It helped shift expectations for how serious comic-book movies could be.', 'https://en.wikipedia.org/wiki/The_Dark_Knight'),
            ('Avatar', 'Avatar broke box-office records and became a landmark in modern visual-effects-driven filmmaking.', 'Its release made 3D cinema a major conversation again.', 'https://en.wikipedia.org/wiki/Avatar_(2009_film)'),
            ('Pirates of the Caribbean', 'Pirates of the Caribbean became one of the major adventure franchises of the 2000s.', 'Its mix of fantasy, humor, and spectacle made it a signature hit of the era.', 'https://en.wikipedia.org/wiki/Pirates_of_the_Caribbean_(film_series)'),
            ('Pixar', 'Pixar continued a remarkable run of animated hits throughout the 2000s and beyond.', 'Its films helped define modern family movie culture.', 'https://en.wikipedia.org/wiki/Pixar'),
            ('Marvel Cinematic Universe', 'The Marvel Cinematic Universe reshaped franchise filmmaking in the 2010s and 2020s.', 'Its interconnected storytelling became one of the defining trends of modern movies.', 'https://en.wikipedia.org/wiki/Marvel_Cinematic_Universe'),
            ('Streaming film releases', 'Streaming platforms changed how many people discover and watch new movies in the 2010s and 2020s.', 'That shift became one of the major industry stories of the modern era.', 'https://en.wikipedia.org/wiki/Streaming_media'),
        ],
    },
    '80s-movies': {
        'hobby': '80s Movies',
        'entries': [
            ('E.T. the Extra-Terrestrial', 'E.T. became one of the signature family blockbusters of the 1980s.', 'Its success helped define the emotional big-screen style of the era.', 'https://en.wikipedia.org/wiki/E.T._the_Extra-Terrestrial'),
            ('Back to the Future', 'Back to the Future became one of the most beloved science-fiction comedies of the 1980s.', 'Its time-travel story made it a lasting pop-culture favorite.', 'https://en.wikipedia.org/wiki/Back_to_the_Future'),
            ('Raiders of the Lost Ark', 'Raiders of the Lost Ark helped define 1980s adventure cinema.', 'Its pace, stunts, and hero made it one of the key films of the decade.', 'https://en.wikipedia.org/wiki/Raiders_of_the_Lost_Ark'),
            ('Ghostbusters', 'Ghostbusters mixed comedy and supernatural action into one of the most memorable films of the 1980s.', 'Its theme song and characters kept it firmly in pop culture.', 'https://en.wikipedia.org/wiki/Ghostbusters'),
            ('The Breakfast Club', 'The Breakfast Club became one of the best-known teen movies of the 1980s.', 'It is often used to represent the decade’s high-school film culture.', 'https://en.wikipedia.org/wiki/The_Breakfast_Club'),
            ('Die Hard', 'Die Hard became one of the defining action movies of the late 1980s.', 'Its success shaped the style of many action films that followed.', 'https://en.wikipedia.org/wiki/Die_Hard'),
            ('Top Gun', 'Top Gun became one of the most recognizable high-energy blockbusters of the 1980s.', 'Its soundtrack and flight scenes helped turn it into an era icon.', 'https://en.wikipedia.org/wiki/Top_Gun'),
            ('The Empire Strikes Back', 'The Empire Strikes Back is often cited as one of the strongest sequels ever made and a key 1980s film.', 'Its darker tone helped expand what blockbuster storytelling could do.', 'https://en.wikipedia.org/wiki/The_Empire_Strikes_Back'),
        ],
    },
    '70s-movies': {
        'hobby': '70s Movies',
        'entries': [
            ('Star Wars', 'Star Wars became one of the most transformative blockbusters of the 1970s.', 'Its success helped launch the modern franchise era in Hollywood.', 'https://en.wikipedia.org/wiki/Star_Wars_(film)'),
            ('Jaws', 'Jaws is often credited as one of the first modern summer blockbusters.', 'Its release changed how studios thought about marketing and seasonal moviegoing.', 'https://en.wikipedia.org/wiki/Jaws_(film)'),
            ('The Godfather', 'The Godfather became one of the defining films of 1970s cinema.', 'Its reputation made it a constant reference point for prestige filmmaking.', 'https://en.wikipedia.org/wiki/The_Godfather'),
            ('Rocky', 'Rocky became one of the great underdog films of the 1970s and started a long-running franchise.', 'Its best-picture win helped lock it into movie history.', 'https://en.wikipedia.org/wiki/Rocky'),
            ('Alien', 'Alien blended science fiction and horror into one of the decade’s most influential films.', 'Its atmosphere and creature design made it unforgettable to audiences.', 'https://en.wikipedia.org/wiki/Alien_(film)'),
            ('Apocalypse Now', 'Apocalypse Now became one of the most ambitious and discussed war films of the 1970s.', 'Its troubled production only added to its legend.', 'https://en.wikipedia.org/wiki/Apocalypse_Now'),
            ('Superman', 'Superman helped show that comic-book heroes could become major event movies.', 'It stands as one of the most important superhero films of the 1970s.', 'https://en.wikipedia.org/wiki/Superman_(1978_film)'),
            ('Saturday Night Fever', 'Saturday Night Fever became one of the most recognizable cultural films of the disco era.', 'Its soundtrack and style helped define late-1970s pop culture.', 'https://en.wikipedia.org/wiki/Saturday_Night_Fever'),
        ],
    },
    '90s-movies': {
        'hobby': '90s Movies',
        'entries': [
            ('Jurassic Park', 'Jurassic Park became one of the landmark visual-effects films of the 1990s.', 'Its dinosaurs helped change audience expectations for blockbuster realism.', 'https://en.wikipedia.org/wiki/Jurassic_Park_(film)'),
            ('Titanic', 'Titanic became one of the biggest box-office hits of the 1990s.', 'Its scale, romance, and awards success made it one of the decade’s defining movies.', 'https://en.wikipedia.org/wiki/Titanic_(1997_film)'),
            ('The Matrix', 'The Matrix became one of the most influential science-fiction films of the late 1990s.', 'Its ideas and action style reshaped movie language for years.', 'https://en.wikipedia.org/wiki/The_Matrix'),
            ('Toy Story', 'Toy Story launched Pixar’s era of fully computer-animated feature films.', 'Its success made it one of the most important family movies of the 1990s.', 'https://en.wikipedia.org/wiki/Toy_Story'),
            ('The Lion King', 'The Lion King became one of the signature animated films of the 1990s.', 'Its music and emotional story helped make it a Disney classic.', 'https://en.wikipedia.org/wiki/The_Lion_King'),
            ('Pulp Fiction', 'Pulp Fiction became one of the most talked-about independent-minded hits of the 1990s.', 'Its style and dialogue made it a landmark in modern film culture.', 'https://en.wikipedia.org/wiki/Pulp_Fiction'),
            ('Forrest Gump', 'Forrest Gump became one of the most recognizable and widely quoted films of the 1990s.', 'Its mix of history, humor, and sentiment helped it become a major hit.', 'https://en.wikipedia.org/wiki/Forrest_Gump'),
            ('Independence Day', 'Independence Day became one of the biggest event movies of the summer blockbuster era in the 1990s.', 'Its scale and alien-invasion spectacle made it a signature crowd-pleaser.', 'https://en.wikipedia.org/wiki/Independence_Day_(1996_film)'),
        ],
    },
    '60s-movies': {
        'hobby': '60s Movies',
        'entries': [
            ('The Sound of Music', 'The Sound of Music became one of the biggest and most beloved musical films of the 1960s.', 'Its songs and family story helped it remain a classic for generations.', 'https://en.wikipedia.org/wiki/The_Sound_of_Music_(film)'),
            ('Psycho', 'Psycho changed horror and suspense filmmaking in the 1960s with its shocks and style.', 'It remains one of Alfred Hitchcock’s most famous films.', 'https://en.wikipedia.org/wiki/Psycho_(1960_film)'),
            ('2001: A Space Odyssey', '2001: A Space Odyssey became one of the most influential science-fiction films of the 1960s.', 'Its ambition and visuals helped redefine what the genre could be.', 'https://en.wikipedia.org/wiki/2001:_A_Space_Odyssey_(film)'),
            ('The Graduate', 'The Graduate became one of the key American films of the late 1960s.', 'Its tone and soundtrack helped it capture the mood of its era.', 'https://en.wikipedia.org/wiki/The_Graduate'),
            ('Mary Poppins', 'Mary Poppins became one of Disney’s most enduring live-action musical hits of the 1960s.', 'Its songs and performances kept it central to family movie culture.', 'https://en.wikipedia.org/wiki/Mary_Poppins_(film)'),
            ('Goldfinger', 'Goldfinger helped establish many of the classic ingredients of the James Bond movie formula.', 'It remains one of the most iconic spy films of the 1960s.', 'https://en.wikipedia.org/wiki/Goldfinger_(film)'),
            ('The Good, the Bad and the Ugly', 'The Good, the Bad and the Ugly became one of the most famous westerns of the 1960s.', 'Its music and wide-screen style helped make it unforgettable.', 'https://en.wikipedia.org/wiki/The_Good,_the_Bad_and_the_Ugly'),
            ('West Side Story', 'West Side Story became one of the most acclaimed movie musicals of the early 1960s.', 'Its songs and choreography made it a standout of the decade.', 'https://en.wikipedia.org/wiki/West_Side_Story_(1961_film)'),
        ],
    },
    'seinfeld': {
        'hobby': 'Seinfeld',
        'entries': [
            ('Jerry Seinfeld', 'Jerry Seinfeld co-created and starred in Seinfeld, one of the defining sitcoms of the 1990s.', 'His observational style helped shape the show’s tone and voice.', 'https://en.wikipedia.org/wiki/Jerry_Seinfeld'),
            ('Larry David', 'Larry David co-created Seinfeld and was crucial to its offbeat comic structure.', 'His writing helped give the show its famously awkward and circular storylines.', 'https://en.wikipedia.org/wiki/Larry_David'),
            ('The Contest', '“The Contest” is often ranked among the most famous Seinfeld episodes ever made.', 'Its clever premise became part of sitcom history.', 'https://en.wikipedia.org/wiki/The_Contest'),
            ('Festivus', 'Festivus began as a Seinfeld joke but entered wider pop culture beyond the show.', 'It became one of the sitcom’s most lasting inventions.', 'https://en.wikipedia.org/wiki/Festivus'),
            ('Kramer', 'Cosmo Kramer became one of the show’s most memorable characters thanks to his entrances and odd ideas.', 'His unpredictability made him a standout part of Seinfeld’s humor.', 'https://en.wikipedia.org/wiki/Cosmo_Kramer'),
            ('Newman', 'Newman became one of Seinfeld’s most recognizable recurring characters and comic foils.', 'His rivalry with Jerry turned simple exchanges into classic sitcom moments.', 'https://en.wikipedia.org/wiki/Newman_(Seinfeld)'),
            ('Show about nothing', 'Seinfeld is often called “a show about nothing,” even though its humor comes from everyday frustrations and social rules.', 'That label became one of the most famous descriptions in TV comedy.', 'https://en.wikipedia.org/wiki/Seinfeld'),
            ('NBC Thursday lineup', 'Seinfeld became a cornerstone of NBC’s powerhouse Thursday-night comedy era.', 'Its popularity helped define network television in the 1990s.', 'https://en.wikipedia.org/wiki/Seinfeld'),
        ],
    },
    'south-park': {
        'hobby': 'South Park',
        'entries': [
            ('Trey Parker and Matt Stone', 'Trey Parker and Matt Stone created South Park and gave it its distinctive voice and satire.', 'Their style helped make the series unlike any other long-running animated comedy.', 'https://en.wikipedia.org/wiki/Trey_Parker_and_Matt_Stone'),
            ('South Park', 'South Park became one of Comedy Central’s defining series and one of the longest-running animated shows for adults.', 'Its blend of fast production and topical satire kept it relevant for years.', 'https://en.wikipedia.org/wiki/South_Park'),
            ('Kenny McCormick', 'Kenny became one of South Park’s most famous characters partly because of the recurring death gag.', 'That running joke became one of the show’s earliest trademarks.', 'https://en.wikipedia.org/wiki/Kenny_McCormick'),
            ('Eric Cartman', 'Eric Cartman became one of the most infamous and recognizable characters in animated comedy.', 'His behavior made him central to many of South Park’s most talked-about episodes.', 'https://en.wikipedia.org/wiki/Eric_Cartman'),
            ('Randy Marsh', 'Randy Marsh grew from a supporting parent into one of South Park’s biggest comedic forces.', 'Many later-era episodes turned him into a major spotlight character.', 'https://en.wikipedia.org/wiki/Randy_Marsh'),
            ('Spirit of Christmas', 'The short film Spirit of Christmas helped lead to the creation of South Park as a series.', 'It became an important part of the show’s origin story.', 'https://en.wikipedia.org/wiki/The_Spirit_of_Christmas_(short_films)'),
            ('South Park: Bigger, Longer & Uncut', 'The South Park movie brought the show’s humor to theaters in 1999.', 'It remains one of the most recognizable film spin-offs from an animated TV series.', 'https://en.wikipedia.org/wiki/South_Park:_Bigger,_Longer_%26_Uncut'),
            ('Satire', 'South Park became especially known for using satire to comment on politics, culture, and media.', 'That approach helped the show stand out in television comedy.', 'https://en.wikipedia.org/wiki/Satire'),
        ],
    },
    'bible': {
        'hobby': 'The Bible',
        'entries': [
            ('Genesis', 'Genesis is the first book of the Bible and includes creation stories, the flood, and the patriarchs.', 'It serves as one of the main starting points for readers exploring the Bible.', 'https://en.wikipedia.org/wiki/Book_of_Genesis'),
            ('Psalms', 'The Book of Psalms contains songs, prayers, and poems that became central to worship and devotion.', 'It remains one of the most widely read parts of the Bible.', 'https://en.wikipedia.org/wiki/Psalms'),
            ('Proverbs', 'Proverbs is known for short sayings and practical wisdom in the Hebrew Bible and Old Testament.', 'Its memorable lines made it one of the Bible’s most quoted books.', 'https://en.wikipedia.org/wiki/Book_of_Proverbs'),
            ('Moses', 'Moses became one of the central figures of the Bible through the Exodus story and the giving of the law.', 'His story shaped both Jewish and Christian tradition in lasting ways.', 'https://en.wikipedia.org/wiki/Moses'),
            ('King David', 'King David became one of the Bible’s most famous rulers and a central figure in many narratives and psalms.', 'His story helped connect kingship, poetry, and faith in the biblical tradition.', 'https://en.wikipedia.org/wiki/David'),
            ('Gospels', 'The four Gospels tell the life, teachings, death, and resurrection of Jesus in the New Testament.', 'They are among the most important books for understanding Christianity.', 'https://en.wikipedia.org/wiki/Gospel'),
            ('Apostle Paul', 'Paul’s letters make up a large part of the New Testament and shaped early Christian theology.', 'His missionary journeys became a major part of biblical history.', 'https://en.wikipedia.org/wiki/Paul_the_Apostle'),
            ('Sermon on the Mount', 'The Sermon on the Mount contains some of the best-known teachings of Jesus in the New Testament.', 'It remains one of the most frequently referenced passages in the Bible.', 'https://en.wikipedia.org/wiki/Sermon_on_the_Mount'),
        ],
    },
    'simpsons': {
        'hobby': 'The Simpsons',
        'entries': [
            ('The Simpsons', 'The Simpsons became the longest-running American scripted primetime television series.', 'Its longevity made it one of the most influential animated comedies ever made.', 'https://en.wikipedia.org/wiki/The_Simpsons'),
            ('Matt Groening', 'Matt Groening created The Simpsons and helped shape its visual style and tone.', 'His characters became some of the most recognizable in television history.', 'https://en.wikipedia.org/wiki/Matt_Groening'),
            ('Homer Simpson', 'Homer Simpson became one of the most iconic fathers in animated television.', 'His catchphrases and mistakes helped define the humor of the show.', 'https://en.wikipedia.org/wiki/Homer_Simpson'),
            ('Bart Simpson', 'Bart Simpson became one of the breakout animated characters of the early 1990s.', 'His attitude and slogans helped make him a pop-culture phenomenon.', 'https://en.wikipedia.org/wiki/Bart_Simpson'),
            ('Springfield', 'Springfield is the fictional hometown of the Simpson family and one of TV’s most famous settings.', 'Its flexible geography became part of the show’s running humor.', 'https://en.wikipedia.org/wiki/Springfield_(The_Simpsons)'),
            ('Treehouse of Horror', 'Treehouse of Horror became one of the best-known recurring traditions on The Simpsons.', 'These Halloween episodes let the show experiment with parody and fantasy.', 'https://en.wikipedia.org/wiki/Treehouse_of_Horror'),
            ('Couch gag', 'The Simpsons couch gag became one of the show’s most recognizable opening traditions.', 'It helped each episode begin with a quick extra joke or visual twist.', 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_couch_gags'),
            ('Guest stars', 'The Simpsons became famous for featuring a huge range of celebrity guest stars over the years.', 'That tradition helped keep the show tied to wider pop culture.', 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars'),
        ],
    },
    'x-men': {
        'hobby': 'X-Men',
        'entries': [
            ('Professor X', 'Professor X became one of the central leaders and mentors in X-Men stories.', 'His vision for coexistence shaped the team’s moral core.', 'https://en.wikipedia.org/wiki/Professor_X'),
            ('Wolverine', 'Wolverine became one of the most popular and recognizable X-Men characters.', 'His attitude, healing power, and claws made him a fan favorite for decades.', 'https://en.wikipedia.org/wiki/Wolverine_(character)'),
            ('Magneto', 'Magneto became one of the defining rivals in X-Men history.', 'His debates with Professor X gave the series much of its lasting dramatic tension.', 'https://en.wikipedia.org/wiki/Magneto_(Marvel_Comics)'),
            ('Storm', 'Storm became one of the most important and powerful members of the X-Men.', 'Her leadership and weather powers made her a standout in the team’s history.', 'https://en.wikipedia.org/wiki/Storm_(Marvel_Comics)'),
            ('Jean Grey', 'Jean Grey became one of the most important figures in major X-Men storylines, especially those involving the Phoenix.', 'Her story helped shape some of the franchise’s most famous arcs.', 'https://en.wikipedia.org/wiki/Jean_Grey'),
            ('X-Men: The Animated Series', 'X-Men: The Animated Series helped introduce the team to a huge television audience in the 1990s.', 'Its theme music and character lineup became especially memorable to fans.', 'https://en.wikipedia.org/wiki/X-Men_(TV_series)'),
            ('X-Men \’97', 'X-Men ’97 revived the animated version of the team for a new generation of viewers.', 'Its release showed how strong nostalgia for the earlier series remained.', 'https://en.wikipedia.org/wiki/X-Men_%2797'),
            ('Mutant metaphor', 'X-Men stories are often discussed as metaphors for prejudice, fear, and social conflict.', 'That thematic layer helped the series stand out from many other superhero teams.', 'https://en.wikipedia.org/wiki/X-Men'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f'{subject} is one of the standout topics fans often explore within {hobby}.',
    lambda subject, detail, extra, hobby: f'Readers and viewers interested in {hobby} often come across {subject} very quickly.',
    lambda subject, detail, extra, hobby: f'Learning about {subject} gives a better feel for why {hobby} remains so memorable.',
    lambda subject, detail, extra, hobby: f'{subject} remains one of the best-known reference points connected with {hobby}.',
    lambda subject, detail, extra, hobby: f'Articles, rankings, and fan discussions about {hobby} regularly highlight {subject}.',
    lambda subject, detail, extra, hobby: f'For many people, {subject} is an easy entry point into the wider world of {hobby}.',
    lambda subject, detail, extra, hobby: f'The story of {subject} helps explain part of the lasting appeal of {hobby}.',
    lambda subject, detail, extra, hobby: f'{subject} is frequently mentioned in retrospectives and guides about {hobby}.',
    lambda subject, detail, extra, hobby: f'One reason {hobby} stays fun to revisit is the presence of major touchpoints like {subject}.',
    lambda subject, detail, extra, hobby: f'{subject} still stands out as a classic example from {hobby}.',
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
