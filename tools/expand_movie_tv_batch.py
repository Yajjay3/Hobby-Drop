from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    '60s-movies': {
        'hobby': '60s Movies',
        'entries': [
            ('Psycho', "Alfred Hitchcock's Psycho (1960) changed horror cinema with its editing, suspense, and shocking structure.", 'Its shower scene became one of the most discussed sequences in film history.', 'https://en.wikipedia.org/wiki/Psycho_(1960_film)'),
            ('West Side Story', 'West Side Story (1961) brought Broadway energy and tragic romance to the big screen.', 'It won the Academy Award for Best Picture for films released in 1961.', 'https://en.wikipedia.org/wiki/West_Side_Story_(1961_film)'),
            ('Lawrence of Arabia', 'Lawrence of Arabia (1962) became famous for its epic scale and desert cinematography.', 'David Lean\'s film is still cited as one of the grandest historical epics ever made.', 'https://en.wikipedia.org/wiki/Lawrence_of_Arabia_(film)'),
            ('Dr. No', 'Dr. No (1962) introduced Sean Connery as James Bond and launched a historic film franchise.', 'The movie established many of the spy-series ingredients audiences still expect from Bond.', 'https://en.wikipedia.org/wiki/Dr._No_(film)'),
            ('To Kill a Mockingbird', 'To Kill a Mockingbird (1962) brought Harper Lee\'s novel to the screen with Gregory Peck as Atticus Finch.', 'Peck won the Academy Award for Best Actor for the role.', 'https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird_(film)'),
            ('Mary Poppins', 'Mary Poppins (1964) wowed audiences by blending live action, animation, and musical fantasy.', 'Julie Andrews won the Academy Award for Best Actress for her performance.', 'https://en.wikipedia.org/wiki/Mary_Poppins_(film)'),
            ('The Sound of Music', 'The Sound of Music (1965) became one of the most beloved movie musicals of all time.', 'Its songs and Alpine imagery helped turn it into a multigenerational favorite.', 'https://en.wikipedia.org/wiki/The_Sound_of_Music_(film)'),
            ('The Good, the Bad and the Ugly', 'The Good, the Bad and the Ugly (1966) helped define the spaghetti western style.', 'Sergio Leone\'s direction and Ennio Morricone\'s score made it a lasting classic.', 'https://en.wikipedia.org/wiki/The_Good,_the_Bad_and_the_Ugly'),
            ('Bonnie and Clyde', 'Bonnie and Clyde (1967) helped push violence and antihero storytelling into mainstream American cinema.', 'The film is often treated as a key step toward the New Hollywood era.', 'https://en.wikipedia.org/wiki/Bonnie_and_Clyde_(film)'),
            ('The Graduate', 'The Graduate (1967) became a landmark of youth alienation and changing social values.', 'Its use of Simon & Garfunkel songs made the soundtrack nearly as famous as the story.', 'https://en.wikipedia.org/wiki/The_Graduate'),
            ('Night of the Living Dead', 'Night of the Living Dead (1968) reshaped horror and helped define the modern zombie movie.', 'George A. Romero\'s low-budget classic became one of the most influential horror films ever made.', 'https://en.wikipedia.org/wiki/Night_of_the_Living_Dead'),
            ('2001: A Space Odyssey', '2001: A Space Odyssey (1968) stunned audiences with ambitious visuals and philosophical science fiction.', 'Stanley Kubrick\'s film remains a benchmark for cinematic scale and visual effects.', 'https://en.wikipedia.org/wiki/2001:_A_Space_Odyssey_(film)'),
            ('Planet of the Apes', 'Planet of the Apes (1968) mixed science fiction, social commentary, and a famous twist ending.', 'Its makeup work helped audiences believe in a world ruled by apes.', 'https://en.wikipedia.org/wiki/Planet_of_the_Apes_(1968_film)'),
            ('Easy Rider', 'Easy Rider (1969) became one of the defining counterculture films of the decade.', 'Its success showed that a rebellious low-budget road movie could become a major hit.', 'https://en.wikipedia.org/wiki/Easy_Rider'),
            ('Butch Cassidy and the Sundance Kid', 'Butch Cassidy and the Sundance Kid (1969) gave Paul Newman and Robert Redford one of cinema\'s great pairings.', 'The film blended western adventure with charm, humor, and a memorable ending.', 'https://en.wikipedia.org/wiki/Butch_Cassidy_and_the_Sundance_Kid'),
        ],
    },
    '70s-movies': {
        'hobby': '70s Movies',
        'entries': [
            ('The Godfather', 'The Godfather (1972) became one of the most acclaimed crime dramas in movie history.', 'Its performances, dialogue, and visual style helped make it a permanent fixture on greatest-film lists.', 'https://en.wikipedia.org/wiki/The_Godfather'),
            ('The Godfather Part II', 'The Godfather Part II (1974) is one of the rare sequels widely seen as the equal of the original.', 'It won the Academy Award for Best Picture and deepened the Corleone family saga.', 'https://en.wikipedia.org/wiki/The_Godfather_Part_II'),
            ('The Exorcist', 'The Exorcist (1973) brought horror to the center of mainstream film culture.', 'It became the first horror film ever nominated for the Academy Award for Best Picture.', 'https://en.wikipedia.org/wiki/The_Exorcist'),
            ('Jaws', 'Jaws (1975) is widely credited with helping create the modern summer blockbuster.', 'Steven Spielberg\'s shark thriller changed how studios marketed big theatrical releases.', 'https://en.wikipedia.org/wiki/Jaws_(film)'),
            ('One Flew Over the Cuckoo\'s Nest', 'One Flew Over the Cuckoo\'s Nest (1975) won the Academy Awards for Picture, Director, Actor, Actress, and Screenplay.', 'That sweep placed it in a very small group of Oscar giants.', 'https://en.wikipedia.org/wiki/One_Flew_Over_the_Cuckoo%27s_Nest_(film)'),
            ('Rocky', 'Rocky (1976) turned Sylvester Stallone into a star and became a classic underdog story.', 'The movie won the Academy Award for Best Picture and launched a long-running franchise.', 'https://en.wikipedia.org/wiki/Rocky'),
            ('Taxi Driver', 'Taxi Driver (1976) gave the decade one of its darkest and most unforgettable character studies.', 'Martin Scorsese and Robert De Niro helped turn the film into a New Hollywood touchstone.', 'https://en.wikipedia.org/wiki/Taxi_Driver'),
            ('Star Wars', 'Star Wars (1977) transformed visual effects, merchandising, and blockbuster storytelling.', 'George Lucas\'s space adventure reshaped the future of mainstream cinema.', 'https://en.wikipedia.org/wiki/Star_Wars_(film)'),
            ('Saturday Night Fever', 'Saturday Night Fever (1977) helped turn disco culture into a global movie and music event.', 'John Travolta\'s performance became one of the iconic star turns of the decade.', 'https://en.wikipedia.org/wiki/Saturday_Night_Fever'),
            ('Superman: The Movie', 'Superman: The Movie (1978) convinced audiences that comic-book heroes could work in serious big-budget films.', 'Christopher Reeve\'s performance helped define the screen image of Superman for a generation.', 'https://en.wikipedia.org/wiki/Superman_(1978_film)'),
            ('Halloween', 'Halloween (1978) helped define the slasher template with a tiny budget and massive cultural impact.', 'John Carpenter\'s film turned Michael Myers into one of horror\'s signature villains.', 'https://en.wikipedia.org/wiki/Halloween_(1978_film)'),
            ('Alien', 'Alien (1979) fused science fiction and horror into one of the most enduring movie franchises ever made.', 'Ridley Scott\'s claustrophobic style and H. R. Giger\'s creature design gave it lasting power.', 'https://en.wikipedia.org/wiki/Alien_(film)'),
            ('Apocalypse Now', 'Apocalypse Now (1979) became famous both for its war imagery and its notoriously difficult production.', 'Francis Ford Coppola\'s Vietnam epic remains one of the defining films of the 1970s.', 'https://en.wikipedia.org/wiki/Apocalypse_Now'),
            ('Chinatown', 'Chinatown (1974) remains one of the most admired neo-noir films in American cinema.', 'Its screenplay and ending made it a favorite among critics and film students alike.', 'https://en.wikipedia.org/wiki/Chinatown_(1974_film)'),
            ('Network', 'Network (1976) satirized television, media outrage, and ratings culture with unusual sharpness.', 'Its famous line about being mad as hell became part of American pop culture.', 'https://en.wikipedia.org/wiki/Network_(1976_film)'),
        ],
    },
    '80s-movies': {
        'hobby': '80s Movies',
        'entries': [
            ('Raiders of the Lost Ark', 'Raiders of the Lost Ark (1981) introduced Indiana Jones in one of the great adventure films of the era.', 'Its pacing, stunts, and serial-inspired energy helped define 1980s blockbuster fun.', 'https://en.wikipedia.org/wiki/Raiders_of_the_Lost_Ark'),
            ('E.T. the Extra-Terrestrial', 'E.T. the Extra-Terrestrial (1982) became a massive worldwide hit and a defining family film.', 'Steven Spielberg\'s story of friendship and wonder held the box-office record for years.', 'https://en.wikipedia.org/wiki/E.T._the_Extra-Terrestrial'),
            ('Blade Runner', 'Blade Runner (1982) became one of the most influential science-fiction films ever, especially after its initial theatrical run.', 'Its neon cityscapes and questions about humanity shaped decades of later sci-fi.', 'https://en.wikipedia.org/wiki/Blade_Runner'),
            ('The Empire Strikes Back', 'The Empire Strikes Back (1980) deepened the Star Wars saga with darker storytelling and one of cinema\'s most famous reveals.', 'Many fans still rank it as the strongest entry in the original trilogy.', 'https://en.wikipedia.org/wiki/The_Empire_Strikes_Back'),
            ('Ghostbusters', 'Ghostbusters (1984) blended supernatural comedy and blockbuster spectacle in a way that clicked instantly with audiences.', 'The film\'s theme song, logo, and cast helped turn it into an 1980s phenomenon.', 'https://en.wikipedia.org/wiki/Ghostbusters'),
            ('The Karate Kid', 'The Karate Kid (1984) made mentor-student training scenes a lasting part of pop culture.', 'Mr. Miyagi and Daniel LaRusso became one of the best-known pairs in sports-movie history.', 'https://en.wikipedia.org/wiki/The_Karate_Kid'),
            ('Back to the Future', 'Back to the Future (1985) became one of the most beloved time-travel adventures ever made.', 'Its mix of comedy, science fiction, and heart gave the decade one of its biggest classics.', 'https://en.wikipedia.org/wiki/Back_to_the_Future'),
            ('The Breakfast Club', 'The Breakfast Club (1985) became a defining teen movie of the John Hughes era.', 'Its detention-room conversations helped turn it into a generational favorite.', 'https://en.wikipedia.org/wiki/The_Breakfast_Club'),
            ('Top Gun', 'Top Gun (1986) made Tom Cruise a megastar and became a signature film of the 1980s blockbuster style.', 'Its aerial action, soundtrack, and image of cool became instantly recognizable.', 'https://en.wikipedia.org/wiki/Top_Gun'),
            ('Aliens', 'Aliens (1986) expanded the world of Alien by shifting the series toward high-intensity action.', 'James Cameron\'s sequel is one of the most respected follow-ups in movie history.', 'https://en.wikipedia.org/wiki/Aliens_(film)'),
            ('Die Hard', 'Die Hard (1988) reshaped action movies by making its hero vulnerable, funny, and trapped in one location.', 'Bruce Willis\'s John McClane became an action icon almost immediately.', 'https://en.wikipedia.org/wiki/Die_Hard'),
            ('Who Framed Roger Rabbit', 'Who Framed Roger Rabbit (1988) dazzled audiences with its blend of live action and animation.', 'The film showed how technically ambitious comedy could still feel playful and accessible.', 'https://en.wikipedia.org/wiki/Who_Framed_Roger_Rabbit'),
            ('Batman', 'Batman (1989) proved that a darker comic-book movie could become a massive mainstream event.', 'Tim Burton\'s version changed the tone of superhero films going into the 1990s.', 'https://en.wikipedia.org/wiki/Batman_(1989_film)'),
            ('The Little Mermaid', 'The Little Mermaid (1989) helped launch the Disney Renaissance in animated features.', 'Its songs and character work set the stage for many Disney hits that followed.', 'https://en.wikipedia.org/wiki/The_Little_Mermaid_(1989_film)'),
            ('The Terminator', 'The Terminator (1984) introduced one of science fiction and action cinema\'s most durable franchises.', 'James Cameron\'s low-budget thriller helped make Arnold Schwarzenegger an even bigger star.', 'https://en.wikipedia.org/wiki/The_Terminator'),
        ],
    },
    '90s-movies': {
        'hobby': '90s Movies',
        'entries': [
            ('Goodfellas', 'Goodfellas (1990) became one of the most acclaimed crime films ever made.', 'Its narration, editing, and energy influenced generations of filmmakers.', 'https://en.wikipedia.org/wiki/Goodfellas'),
            ('The Silence of the Lambs', 'The Silence of the Lambs (1991) won the Academy Awards for Picture, Director, Actor, Actress, and Screenplay.', 'It remains one of the rare thrillers to win Best Picture.', 'https://en.wikipedia.org/wiki/The_Silence_of_the_Lambs_(film)'),
            ('Terminator 2: Judgment Day', 'Terminator 2: Judgment Day (1991) pushed visual effects and blockbuster action to a new level.', 'Its liquid-metal T-1000 became an early showcase for breakthrough CGI.', 'https://en.wikipedia.org/wiki/Terminator_2:_Judgment_Day'),
            ('Jurassic Park', 'Jurassic Park (1993) changed visual effects by combining animatronics with believable digital dinosaurs.', 'Steven Spielberg\'s film turned its prehistoric creatures into a global movie event.', 'https://en.wikipedia.org/wiki/Jurassic_Park_(film)'),
            ('Schindler\'s List', 'Schindler\'s List (1993) won the Academy Award for Best Picture and Best Director for Steven Spielberg.', 'Its emotional power made it one of the most respected historical dramas of the decade.', 'https://en.wikipedia.org/wiki/Schindler%27s_List'),
            ('Pulp Fiction', 'Pulp Fiction (1994) helped redefine the commercial possibilities of independent cinema.', 'Quentin Tarantino\'s nonlinear storytelling and dialogue made it instantly recognizable.', 'https://en.wikipedia.org/wiki/Pulp_Fiction'),
            ('Forrest Gump', 'Forrest Gump (1994) became a huge hit by blending sentiment, comedy, and American history.', 'It won the Academy Award for Best Picture and several other Oscars.', 'https://en.wikipedia.org/wiki/Forrest_Gump'),
            ('The Lion King', 'The Lion King (1994) became one of the Disney Renaissance\'s biggest animated triumphs.', 'Its music and characters made it a multigenerational favorite.', 'https://en.wikipedia.org/wiki/The_Lion_King'),
            ('Toy Story', 'Toy Story (1995) was the first fully computer-animated feature film.', 'Its success launched Pixar as one of the most important animation studios in the world.', 'https://en.wikipedia.org/wiki/Toy_Story'),
            ('Titanic', 'Titanic (1997) became a historic box-office sensation and tied the record with 11 Academy Awards.', 'James Cameron\'s epic romance and disaster film dominated late-1990s movie culture.', 'https://en.wikipedia.org/wiki/Titanic_(1997_film)'),
            ('The Matrix', 'The Matrix (1999) changed action filmmaking with bullet time, cyberpunk style, and philosophical science fiction.', 'Its visual language quickly spread through movies, TV, and advertising.', 'https://en.wikipedia.org/wiki/The_Matrix'),
            ('Saving Private Ryan', 'Saving Private Ryan (1998) became famous for its intense and realistic D-Day opening sequence.', 'Its war scenes influenced later combat films and TV series for years.', 'https://en.wikipedia.org/wiki/Saving_Private_Ryan'),
            ('Fight Club', 'Fight Club (1999) grew from a divisive release into one of the era\'s biggest cult films.', 'Its twist and social commentary kept audiences debating it long after release.', 'https://en.wikipedia.org/wiki/Fight_Club'),
            ('The Blair Witch Project', 'The Blair Witch Project (1999) showed how a tiny budget and clever marketing could create a giant hit.', 'Its success changed conversations about found-footage horror and viral promotion.', 'https://en.wikipedia.org/wiki/The_Blair_Witch_Project'),
            ('Clueless', 'Clueless (1995) became one of the defining teen comedies of the 1990s.', 'Its fashion, slang, and Beverly Hills setting helped it become a lasting pop-culture favorite.', 'https://en.wikipedia.org/wiki/Clueless_(film)'),
        ],
    },
    '2000s-movies': {
        'hobby': '2000s-2026 Movies',
        'entries': [
            ('Gladiator', 'Gladiator (2000) revived the historical epic for a new era and won the Academy Award for Best Picture.', 'Russell Crowe\'s performance and Hans Zimmer\'s score helped make it a major hit.', 'https://en.wikipedia.org/wiki/Gladiator_(2000_film)'),
            ('The Lord of the Rings: The Fellowship of the Ring', 'The Lord of the Rings: The Fellowship of the Ring (2001) showed that large-scale fantasy could work as prestige blockbuster cinema.', 'Peter Jackson\'s Middle-earth adaptation became a cornerstone of 21st-century filmmaking.', 'https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Fellowship_of_the_Ring'),
            ('The Lord of the Rings: The Return of the King', 'The Lord of the Rings: The Return of the King (2003) swept the Academy Awards with 11 wins.', 'Its success helped cement the trilogy as one of the defining film achievements of the century.', 'https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Return_of_the_King'),
            ('Harry Potter and the Philosopher\'s Stone', 'Harry Potter and the Philosopher\'s Stone (2001) launched one of the biggest screen franchises of the modern era.', 'The wizarding world became a major part of global movie culture for a decade.', 'https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone_(film)'),
            ('The Dark Knight', 'The Dark Knight (2008) helped elevate comic-book films in critical and awards discussions.', 'Heath Ledger\'s Joker performance became one of the most talked-about turns of the era.', 'https://en.wikipedia.org/wiki/The_Dark_Knight_(film)'),
            ('Avatar', 'Avatar (2009) became a landmark for 3D exhibition and motion-capture spectacle.', 'James Cameron\'s science-fiction epic grew into one of the highest-grossing films ever made.', 'https://en.wikipedia.org/wiki/Avatar_(2009_film)'),
            ('Iron Man', 'Iron Man (2008) launched the Marvel Cinematic Universe with Robert Downey Jr. as Tony Stark.', 'Its success changed the shape of franchise filmmaking for years to come.', 'https://en.wikipedia.org/wiki/Iron_Man_(2008_film)'),
            ('Inception', 'Inception (2010) proved that an original high-concept blockbuster could still become a major global hit.', 'Its dream-layer structure made it one of the most discussed films of the decade.', 'https://en.wikipedia.org/wiki/Inception'),
            ('Mad Max: Fury Road', 'Mad Max: Fury Road (2015) was praised for combining practical stunt work with modern visual effects.', 'Its relentless pace and visual storytelling made it a standout action film.', 'https://en.wikipedia.org/wiki/Mad_Max:_Fury_Road'),
            ('Get Out', 'Get Out (2017) showed that horror could also function as sharp social commentary and awards-level filmmaking.', 'Jordan Peele won the Academy Award for Best Original Screenplay for the film.', 'https://en.wikipedia.org/wiki/Get_Out'),
            ('Parasite', 'Parasite (2019) became the first non-English-language film to win the Academy Award for Best Picture.', 'Bong Joon-ho\'s thriller-drama became a worldwide critical and commercial success.', 'https://en.wikipedia.org/wiki/Parasite_(film)'),
            ('Top Gun: Maverick', 'Top Gun: Maverick (2022) became a major theatrical event and a huge global box-office hit.', 'Its success reminded studios how powerful crowd-pleasing big-screen movies could still be.', 'https://en.wikipedia.org/wiki/Top_Gun:_Maverick'),
            ('Barbie', 'Barbie (2023) turned a toy brand into one of the biggest pop-culture movie events of the decade.', 'Greta Gerwig\'s film helped create the larger Barbenheimer phenomenon.', 'https://en.wikipedia.org/wiki/Barbie_(film)'),
            ('Oppenheimer', 'Oppenheimer (2023) won the Academy Award for Best Picture and became a rare large-scale success for a serious historical drama.', 'Christopher Nolan\'s film showed audiences still embraced ambitious adult storytelling in theaters.', 'https://en.wikipedia.org/wiki/Oppenheimer_(film)'),
            ('Dune: Part Two', 'Dune: Part Two (2024) continued Denis Villeneuve\'s acclaimed adaptation of Frank Herbert\'s science-fiction world.', 'The film strengthened the return of large-scale serious sci-fi on the big screen.', 'https://en.wikipedia.org/wiki/Dune:_Part_Two'),
        ],
    },
    'voted-best-movies': {
        'hobby': 'Voted Best Movies',
        'entries': [
            ('Citizen Kane', 'Citizen Kane (1941) is regularly voted among the greatest films ever made.', 'Its structure, camerawork, and storytelling changed what many critics expected from cinema.', 'https://en.wikipedia.org/wiki/Citizen_Kane'),
            ('Casablanca', 'Casablanca (1942) remains one of the most beloved and quoted films in Hollywood history.', 'Its romance and wartime setting keep it near the top of many best-movie polls.', 'https://en.wikipedia.org/wiki/Casablanca_(film)'),
            ('The Godfather', 'The Godfather is a permanent presence on many greatest-film rankings and audience lists.', 'Its reputation has stayed strong across critics, filmmakers, and general viewers alike.', 'https://en.wikipedia.org/wiki/The_Godfather'),
            ('Lawrence of Arabia', 'Lawrence of Arabia is often singled out when people discuss the greatest screen epics ever made.', 'Its scale and visual ambition helped it become a fixture of all-time polls.', 'https://en.wikipedia.org/wiki/Lawrence_of_Arabia_(film)'),
            ('2001: A Space Odyssey', '2001: A Space Odyssey appears on many lists of the greatest science-fiction and greatest overall films.', 'Stanley Kubrick\'s work is still treated as a benchmark of cinematic ambition.', 'https://en.wikipedia.org/wiki/2001:_A_Space_Odyssey_(film)'),
            ('Schindler\'s List', 'Schindler\'s List is frequently voted among the most powerful and important films ever made.', 'Its awards success and emotional force keep it high on many rankings.', 'https://en.wikipedia.org/wiki/Schindler%27s_List'),
            ('The Shawshank Redemption', 'The Shawshank Redemption became a huge audience favorite and often tops user-voted movie lists.', 'Its reputation grew steadily after release through television and home viewing.', 'https://en.wikipedia.org/wiki/The_Shawshank_Redemption'),
            ('Seven Samurai', 'Seven Samurai is often cited as one of the greatest action and adventure films ever made.', 'Akira Kurosawa\'s classic influenced everything from westerns to modern ensemble blockbusters.', 'https://en.wikipedia.org/wiki/Seven_Samurai'),
            ('Psycho', 'Psycho is a regular presence on greatest-horror and greatest-film lists alike.', 'Its suspense, editing, and audacity gave it lasting critical prestige.', 'https://en.wikipedia.org/wiki/Psycho_(1960_film)'),
            ('Singin\' in the Rain', 'Singin\' in the Rain is often voted the greatest movie musical ever made.', 'Its joyful choreography and self-aware Hollywood satire made it a perennial favorite.', 'https://en.wikipedia.org/wiki/Singin%27_in_the_Rain'),
            ('Vertigo', 'Vertigo climbed to the top of several major critics\' polls in the 21st century.', 'Alfred Hitchcock\'s mystery became one of the most studied films in world cinema.', 'https://en.wikipedia.org/wiki/Vertigo_(film)'),
            ('The Wizard of Oz', 'The Wizard of Oz remains one of the most beloved family films ever released.', 'Its songs, color imagery, and fantasy world keep it near the top of classic-movie rankings.', 'https://en.wikipedia.org/wiki/The_Wizard_of_Oz_(1939_film)'),
            ('Pulp Fiction', 'Pulp Fiction appears on many lists of the best modern American movies.', 'Its influence on dialogue, editing, and indie filmmaking keeps it in all-time conversations.', 'https://en.wikipedia.org/wiki/Pulp_Fiction'),
            ('The Lord of the Rings: The Return of the King', 'The Lord of the Rings: The Return of the King is often voted among the best fantasy films ever made.', 'Its Oscar success and emotional payoff gave it a lasting place on fan and critic lists.', 'https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Return_of_the_King'),
            ('The Dark Knight', 'The Dark Knight is one of the modern films most frequently voted onto all-time audience rankings.', 'Its impact helped superhero movies gain more respect in broader film discussions.', 'https://en.wikipedia.org/wiki/The_Dark_Knight_(film)'),
        ],
    },
    'seinfeld': {
        'hobby': 'Seinfeld',
        'entries': [
            ('The Contest', 'The Contest is widely considered one of the smartest and boldest sitcom episodes ever produced.', 'Its writing and comic restraint helped make it a permanent Seinfeld landmark.', 'https://en.wikipedia.org/wiki/The_Contest'),
            ('The Chinese Restaurant', 'The Chinese Restaurant turned waiting for a table into a classic example of Seinfeld\'s everyday absurdity.', 'The episode became famous for showing how compelling a story about almost nothing could be.', 'https://en.wikipedia.org/wiki/The_Chinese_Restaurant'),
            ('The Puffy Shirt', 'The Puffy Shirt became one of Seinfeld\'s best-known episodes by turning a tiny misunderstanding into chaos.', 'Its pirate-style shirt became one of the show\'s most memorable visual jokes.', 'https://en.wikipedia.org/wiki/The_Puffy_Shirt'),
            ('The Opposite', 'The Opposite is often praised as one of the strongest sitcom season finales ever made.', 'George\'s decision to do the opposite of every instinct became a classic comic premise.', 'https://en.wikipedia.org/wiki/The_Opposite'),
            ('The Soup Nazi', 'The Soup Nazi introduced one of the most famous recurring characters in television comedy.', 'The line "No soup for you!" escaped the show and entered everyday pop culture.', 'https://en.wikipedia.org/wiki/The_Soup_Nazi'),
            ('Festivus', 'Festivus became a real-world pop-culture tradition after appearing in Seinfeld.', 'Frank Costanza\'s fictional holiday remains one of the show\'s most lasting inventions.', 'https://en.wikipedia.org/wiki/Festivus'),
            ('Frank Costanza', 'Frank Costanza became one of Seinfeld\'s great late-series additions thanks to Jerry Stiller\'s explosive performance.', 'His outbursts and stories gave the series a fresh layer of absurd family energy.', 'https://en.wikipedia.org/wiki/Frank_Costanza'),
            ('Newman', 'Newman turned a recurring neighbor role into one of sitcom history\'s most beloved annoyances.', 'Wayne Knight\'s delivery made the character instantly memorable.', 'https://en.wikipedia.org/wiki/Newman_(Seinfeld)'),
            ('Elaine Benes', 'Elaine Benes helped redefine how women were written in major TV comedies during the 1990s.', 'Julia Louis-Dreyfus gave the show one of its sharpest and funniest perspectives.', 'https://en.wikipedia.org/wiki/Elaine_Benes'),
            ('George Costanza', 'George Costanza became one of television\'s all-time great comedy characters.', 'His insecurity, scheming, and total lack of self-awareness powered many of Seinfeld\'s best stories.', 'https://en.wikipedia.org/wiki/George_Costanza'),
            ('Cosmo Kramer', 'Cosmo Kramer gave the show its wild physical-comedy energy through entrances, schemes, and total unpredictability.', 'Michael Richards\' performance helped make Kramer a sitcom legend.', 'https://en.wikipedia.org/wiki/Cosmo_Kramer'),
            ('The Marine Biologist', 'The Marine Biologist is remembered for one of George Costanza\'s greatest monologues.', 'Its closing speech about a beached whale became one of the show\'s signature moments.', 'https://en.wikipedia.org/wiki/The_Marine_Biologist'),
            ('Yada yada yada', 'The phrase "yada yada yada" became a mainstream expression after Seinfeld popularized it.', 'The show had a remarkable ability to turn tiny speech habits into enduring catchphrases.', 'https://en.wikipedia.org/wiki/The_Yada_Yada'),
            ('Serenity now', 'The phrase "Serenity now!" became another classic Seinfeld quote through Frank Costanza\'s explosive delivery.', 'It remains one of the show\'s best examples of mock self-help turning into total panic.', 'https://en.wikipedia.org/wiki/The_Serenity_Now'),
            ('The Junior Mint', 'The Junior Mint episode showed Seinfeld\'s talent for turning a ridiculous accident into comic legend.', 'Its title alone is enough for many fans to remember the entire story.', 'https://en.wikipedia.org/wiki/The_Junior_Mint'),
        ],
    },
    'south-park': {
        'hobby': 'South Park',
        'entries': [
            ('The Spirit of Christmas', 'The Spirit of Christmas short film helped launch South Park before the series officially began.', 'Its early viral spread on the internet played a major role in the show\'s rise.', 'https://en.wikipedia.org/wiki/The_Spirit_of_Christmas_(short_films)'),
            ('Eric Cartman', 'Eric Cartman became one of television\'s most outrageous and unforgettable comedy characters.', 'His selfishness and unpredictability gave South Park many of its darkest laughs.', 'https://en.wikipedia.org/wiki/Eric_Cartman'),
            ('Kenny McCormick', 'Kenny McCormick became famous for repeatedly dying in early South Park episodes.', 'That running gag turned him into one of the most recognizable animated TV characters of the era.', 'https://en.wikipedia.org/wiki/Kenny_McCormick'),
            ('Butters Stotch', 'Butters Stotch grew from a side character into one of South Park\'s breakout fan favorites.', 'His innocence often made him the perfect contrast to the show\'s chaos.', 'https://en.wikipedia.org/wiki/Butters_Stotch'),
            ('Chef', 'Chef became one of the show\'s earliest beloved supporting characters, voiced by Isaac Hayes.', 'His musical advice scenes gave the series a distinct comic rhythm.', 'https://en.wikipedia.org/wiki/Chef_(South_Park)'),
            ('South Park: Bigger, Longer & Uncut', 'South Park: Bigger, Longer & Uncut successfully turned the TV series into a theatrical movie.', 'The film even earned an Academy Award nomination for the song "Blame Canada."', 'https://en.wikipedia.org/wiki/South_Park:_Bigger,_Longer_%26_Uncut'),
            ('Scott Tenorman Must Die', 'Scott Tenorman Must Die is often cited as a turning point in how dark Cartman\'s character could become.', 'Many fans see it as one of the show\'s boldest and most memorable episodes.', 'https://en.wikipedia.org/wiki/Scott_Tenorman_Must_Die'),
            ('Trapped in the Closet', 'Trapped in the Closet became one of South Park\'s most controversial and widely discussed episodes.', 'Its satire of Scientology showed how directly the show was willing to challenge public figures and beliefs.', 'https://en.wikipedia.org/wiki/Trapped_in_the_Closet_(South_Park)'),
            ('Make Love, Not Warcraft', 'Make Love, Not Warcraft won an Emmy and became one of South Park\'s most celebrated pop-culture parodies.', 'The episode captured gaming obsession with unusual accuracy and comic timing.', 'https://en.wikipedia.org/wiki/Make_Love,_Not_Warcraft'),
            ('Casa Bonita', 'Casa Bonita became a legendary South Park location through an episode centered on Butters and Cartman.', 'The episode later inspired Trey Parker and Matt Stone to buy and restore the real restaurant.', 'https://en.wikipedia.org/wiki/Casa_Bonita_(South_Park)'),
            ('South Park Studios', 'South Park Studios helped the series thrive online by giving fans an official digital home for episodes and clips.', 'The show adapted to internet culture earlier than many major television comedies.', 'https://en.wikipedia.org/wiki/South_Park_Studios'),
            ('Trey Parker and Matt Stone', 'Trey Parker and Matt Stone became famous for producing many episodes in only a few days.', 'That speed allowed South Park to satirize current events while they were still dominating headlines.', 'https://en.wikipedia.org/wiki/Trey_Parker_and_Matt_Stone'),
            ('Primus theme song', 'The South Park theme song was originally performed by Primus, giving the show an instantly odd and memorable opening.', 'The music helped signal the series\' irreverent tone from the first seconds.', 'https://en.wikipedia.org/wiki/South_Park_(theme_song)'),
            ('Stan Marsh', 'Stan Marsh often serves as one of South Park\'s emotional anchors in the middle of the show\'s absurdity.', 'His reactions help ground stories that otherwise spiral into chaos.', 'https://en.wikipedia.org/wiki/Stan_Marsh'),
            ('Kyle Broflovski', 'Kyle Broflovski gave South Park one of its sharpest skeptical voices and strongest moral centers.', 'His friendship and conflict with Cartman produced many of the show\'s classic exchanges.', 'https://en.wikipedia.org/wiki/Kyle_Broflovski'),
        ],
    },
    'simpsons': {
        'hobby': 'The Simpsons',
        'entries': [
            ('Matt Groening', 'Matt Groening created The Simpsons and based several family names on his own relatives.', 'That personal starting point helped launch one of television\'s biggest cultural institutions.', 'https://en.wikipedia.org/wiki/Matt_Groening'),
            ('Homer Simpson', 'Homer Simpson became one of the most recognizable TV fathers in popular culture.', 'His voice, catchphrases, and disasters helped define the show\'s comic identity.', 'https://en.wikipedia.org/wiki/Homer_Simpson'),
            ('Bart Simpson', 'Bart Simpson drove the early wave of Simpsons mania with attitude, skateboards, and catchphrases.', 'For many viewers, Bart was the show\'s first breakout star.', 'https://en.wikipedia.org/wiki/Bart_Simpson'),
            ('Lisa Simpson', 'Lisa Simpson gave the series a thoughtful, idealistic, and often musical voice.', 'Her intelligence and conscience helped balance the chaos around the rest of the family.', 'https://en.wikipedia.org/wiki/Lisa_Simpson'),
            ('Marge Simpson', 'Marge Simpson became the stabilizing force of the family while still getting many of the show\'s funniest moments.', 'Her towering blue hair made her one of animation\'s most distinctive silhouettes.', 'https://en.wikipedia.org/wiki/Marge_Simpson'),
            ('Treehouse of Horror', 'Treehouse of Horror became the show\'s annual excuse to parody horror, science fiction, and fantasy classics.', 'Those episodes remain a favorite seasonal tradition for many fans.', 'https://en.wikipedia.org/wiki/Treehouse_of_Horror'),
            ('Who Shot Mr. Burns?', 'Who Shot Mr. Burns? turned The Simpsons into a national TV mystery in the mid-1990s.', 'The cliffhanger became one of the most talked-about event episodes in the show\'s history.', 'https://en.wikipedia.org/wiki/Who_Shot_Mr._Burns%3F'),
            ('Sideshow Bob', 'Sideshow Bob became one of the show\'s most beloved recurring villains thanks to Kelsey Grammer\'s voice work.', 'His theatrical schemes gave the series some of its sharpest parody episodes.', 'https://en.wikipedia.org/wiki/Sideshow_Bob'),
            ('Itchy & Scratchy', 'Itchy & Scratchy works as a violent cartoon parody inside the larger world of The Simpsons.', 'The fake show became one of Springfield\'s funniest recurring jokes.', 'https://en.wikipedia.org/wiki/Itchy_%26_Scratchy'),
            ('The Simpsons Movie', 'The Simpsons Movie successfully brought Springfield to theaters in 2007.', 'Spider-Pig quickly became one of the film\'s biggest crowd-pleasing jokes.', 'https://en.wikipedia.org/wiki/The_Simpsons_Movie'),
            ('Springfield', 'The location of Springfield is deliberately ambiguous, which became one of the show\'s longest-running jokes.', 'That mystery let the town feel like an everywhere-and-nowhere version of America.', 'https://en.wikipedia.org/wiki/Springfield_(The_Simpsons)'),
            ('Couch gag', 'The couch gag gives the animators a fresh way to reinvent the opening credits from episode to episode.', 'These short sequences became one of the show\'s most flexible comic traditions.', 'https://en.wikipedia.org/wiki/The_Simpsons_opening_sequence'),
            ('D\'oh!', 'Homer\'s frustrated "D\'oh!" became so famous that it was eventually added to dictionaries.', 'Very few cartoon catchphrases have entered everyday language that successfully.', 'https://en.wikipedia.org/wiki/D%27oh!'),
            ('Ned Flanders', 'Ned Flanders became so influential as a comic stereotype that the term "Flanderization" grew from his example.', 'The character showed how the series could exaggerate a side role into a cultural reference point.', 'https://en.wikipedia.org/wiki/Ned_Flanders'),
            ('Krusty the Clown', 'Krusty the Clown helped the show parody celebrity culture, children\'s entertainment, and local TV fame.', 'His chaotic career added another layer to Springfield\'s comic world.', 'https://en.wikipedia.org/wiki/Krusty_the_Clown'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f"{subject} is one of the signature titles or subjects people mention when discussing {hobby}.",
    lambda subject, detail, extra, hobby: f"Any overview of {hobby} usually makes room for {subject}.",
    lambda subject, detail, extra, hobby: f"{subject} helped define the tone and reputation of {hobby}.",
    lambda subject, detail, extra, hobby: f"Fans exploring {hobby} are often encouraged to start with {subject}.",
    lambda subject, detail, extra, hobby: f"The legacy of {hobby} is hard to explain without mentioning {subject}.",
    lambda subject, detail, extra, hobby: f"Critical conversations about {hobby} often return to {subject}.",
    lambda subject, detail, extra, hobby: f"For many fans, {subject} captures part of why {hobby} remains so memorable.",
    lambda subject, detail, extra, hobby: f"Lists, retrospectives, and fan rankings about {hobby} frequently include {subject}.",
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
