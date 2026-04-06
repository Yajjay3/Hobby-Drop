from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1] / 'extension' / 'data' / 'facts'

BATCH = {
    'us-history': {
        'hobby': 'U.S. History',
        'entries': [
            ('Declaration of Independence', 'The Declaration of Independence announced the American colonies\' break from British rule in 1776.', 'It remains one of the most important documents in U.S. political history.', 'https://en.wikipedia.org/wiki/United_States_Declaration_of_Independence'),
            ('U.S. Constitution', 'The U.S. Constitution was written in 1787 and created the federal framework still used today.', 'It is the oldest written national constitution still in force.', 'https://en.wikipedia.org/wiki/United_States_Constitution'),
            ('Louisiana Purchase', 'The Louisiana Purchase of 1803 nearly doubled the size of the United States.', 'It became one of the most important territorial acquisitions in American history.', 'https://en.wikipedia.org/wiki/Louisiana_Purchase'),
            ('Lewis and Clark Expedition', 'The Lewis and Clark Expedition explored the newly acquired western lands from 1804 to 1806.', 'Its journey helped expand U.S. knowledge of the continent\'s geography and peoples.', 'https://en.wikipedia.org/wiki/Lewis_and_Clark_Expedition'),
            ('Gettysburg Address', 'Abraham Lincoln delivered the Gettysburg Address during the Civil War in 1863.', 'The speech became one of the most famous statements of American democracy and sacrifice.', 'https://en.wikipedia.org/wiki/Gettysburg_Address'),
            ('Transcontinental Railroad', 'The transcontinental railroad linked the country by rail in 1869.', 'Its completion changed commerce, migration, and travel across the United States.', 'https://en.wikipedia.org/wiki/First_transcontinental_railroad'),
            ('Great Depression', 'The Great Depression reshaped American politics, economics, and daily life after 1929.', 'It became one of the defining crises in the history of the United States.', 'https://en.wikipedia.org/wiki/Great_Depression_in_the_United_States'),
            ('New Deal', 'Franklin D. Roosevelt\'s New Deal launched major federal relief, recovery, and reform programs.', 'Its agencies and policies changed the role of the federal government in U.S. life.', 'https://en.wikipedia.org/wiki/New_Deal'),
            ('Pearl Harbor', 'The attack on Pearl Harbor brought the United States into World War II in December 1941.', 'It became one of the most consequential surprise attacks in American history.', 'https://en.wikipedia.org/wiki/Attack_on_Pearl_Harbor'),
            ('Civil Rights Act of 1964', 'The Civil Rights Act of 1964 outlawed segregation and discrimination in major areas of public life.', 'It became one of the most important laws of the modern civil-rights era.', 'https://en.wikipedia.org/wiki/Civil_Rights_Act_of_1964'),
            ('Apollo 11', 'Apollo 11 put the first humans on the Moon in 1969.', 'The mission became a landmark of U.S. science, engineering, and Cold War history.', 'https://en.wikipedia.org/wiki/Apollo_11'),
            ('Watergate scandal', 'The Watergate scandal led to Richard Nixon\'s resignation in 1974.', 'It remains one of the most famous political scandals in U.S. history.', 'https://en.wikipedia.org/wiki/Watergate_scandal'),
        ],
    },
    'presidents': {
        'hobby': 'U.S. Presidents',
        'entries': [
            ('George Washington', 'George Washington became the first president of the United States in 1789.', 'He set many early precedents for the presidency and the federal government.', 'https://en.wikipedia.org/wiki/George_Washington'),
            ('Thomas Jefferson', 'Thomas Jefferson oversaw the Louisiana Purchase and promoted the ideals of the Declaration of Independence.', 'He remains one of the most influential early presidents in American history.', 'https://en.wikipedia.org/wiki/Thomas_Jefferson'),
            ('Abraham Lincoln', 'Abraham Lincoln led the United States through the Civil War and pushed toward the abolition of slavery.', 'He is often ranked among the most consequential presidents in U.S. history.', 'https://en.wikipedia.org/wiki/Abraham_Lincoln'),
            ('Theodore Roosevelt', 'Theodore Roosevelt became known for conservation, trust-busting, and energetic presidential leadership.', 'His presidency helped expand the public role of the executive branch.', 'https://en.wikipedia.org/wiki/Theodore_Roosevelt'),
            ('Franklin D. Roosevelt', 'Franklin D. Roosevelt is the only U.S. president elected to four terms.', 'He led the country through the Great Depression and most of World War II.', 'https://en.wikipedia.org/wiki/Franklin_D._Roosevelt'),
            ('Harry S. Truman', 'Harry Truman became president at the end of World War II and shaped the early Cold War.', 'His administration is closely tied to the Marshall Plan, NATO, and major postwar decisions.', 'https://en.wikipedia.org/wiki/Harry_S._Truman'),
            ('Dwight D. Eisenhower', 'Dwight D. Eisenhower was a former Allied commander before becoming president.', 'His years in office are associated with the Interstate Highway System and Cold War stability.', 'https://en.wikipedia.org/wiki/Dwight_D._Eisenhower'),
            ('John F. Kennedy', 'John F. Kennedy inspired a generation with his New Frontier message and Cold War leadership.', 'His presidency remains one of the most closely studied and remembered in modern U.S. history.', 'https://en.wikipedia.org/wiki/John_F._Kennedy'),
            ('Lyndon B. Johnson', 'Lyndon B. Johnson signed landmark civil-rights and social-welfare legislation.', 'His presidency is also deeply connected to the Vietnam War era.', 'https://en.wikipedia.org/wiki/Lyndon_B._Johnson'),
            ('Richard Nixon', 'Richard Nixon opened relations with China but resigned after the Watergate scandal.', 'He remains one of the most controversial figures in presidential history.', 'https://en.wikipedia.org/wiki/Richard_Nixon'),
            ('Ronald Reagan', 'Ronald Reagan, a former actor and governor of California, became the 40th president of the United States.', 'His presidency shaped conservative politics and late-Cold War policy for decades.', 'https://en.wikipedia.org/wiki/Ronald_Reagan'),
            ('Barack Obama', 'Barack Obama became the first Black president in U.S. history.', 'His presidency is closely associated with the Affordable Care Act and major shifts in American political culture.', 'https://en.wikipedia.org/wiki/Barack_Obama'),
        ],
    },
    'wars': {
        'hobby': 'Wars & Battles',
        'entries': [
            ('Battle of Marathon', 'The Battle of Marathon in 490 BC became one of the most famous clashes of the ancient world.', 'It is often remembered as a landmark event in the Greco-Persian Wars.', 'https://en.wikipedia.org/wiki/Battle_of_Marathon'),
            ('Battle of Thermopylae', 'The Battle of Thermopylae made the Spartan stand against Persia legendary.', 'It remains one of the most famous last stands in military history.', 'https://en.wikipedia.org/wiki/Battle_of_Thermopylae'),
            ('Battle of Hastings', 'The Battle of Hastings in 1066 transformed English history when William the Conqueror defeated Harold II.', 'It stands as one of the defining battles of the medieval world.', 'https://en.wikipedia.org/wiki/Battle_of_Hastings'),
            ('Battle of Waterloo', 'The Battle of Waterloo ended Napoleon\'s rule in 1815.', 'It became one of the most iconic turning points in European military history.', 'https://en.wikipedia.org/wiki/Battle_of_Waterloo'),
            ('Battle of Gettysburg', 'Gettysburg is often considered the turning point of the American Civil War.', 'The battle remains one of the most studied engagements in U.S. military history.', 'https://en.wikipedia.org/wiki/Battle_of_Gettysburg'),
            ('World War I', 'World War I introduced trench warfare, poison gas, and industrial-scale destruction on an enormous scale.', 'The war redrew empires and transformed the politics of the 20th century.', 'https://en.wikipedia.org/wiki/World_War_I'),
            ('D-Day', 'D-Day was the Allied invasion of Normandy on June 6, 1944.', 'It became one of the most famous military operations in modern history.', 'https://en.wikipedia.org/wiki/Normandy_landings'),
            ('Battle of Stalingrad', 'The Battle of Stalingrad is widely seen as one of the decisive turning points of World War II.', 'Its scale, brutality, and outcome changed the course of the war in Europe.', 'https://en.wikipedia.org/wiki/Battle_of_Stalingrad'),
            ('Korean War', 'The Korean War ended in an armistice rather than a peace treaty.', 'Its unresolved legacy continues to shape East Asian politics and military strategy.', 'https://en.wikipedia.org/wiki/Korean_War'),
            ('Vietnam War', 'The Vietnam War deeply affected politics, society, and culture in both Vietnam and the United States.', 'It remains one of the most debated conflicts of the modern era.', 'https://en.wikipedia.org/wiki/Vietnam_War'),
            ('Persian Gulf War', 'The Persian Gulf War in 1990–1991 was fought after Iraq invaded Kuwait.', 'The conflict showed the power of modern coalition warfare and precision-guided weapons.', 'https://en.wikipedia.org/wiki/Gulf_War'),
            ('Battle of Midway', 'The Battle of Midway in 1942 shifted the naval balance in the Pacific during World War II.', 'It is often described as one of the most decisive sea battles in history.', 'https://en.wikipedia.org/wiki/Battle_of_Midway'),
        ],
    },
    'law': {
        'hobby': 'Law & Justice',
        'entries': [
            ('Magna Carta', 'The Magna Carta of 1215 became an enduring symbol of limits on royal power and of legal rights.', 'Its legacy influenced constitutional ideas far beyond medieval England.', 'https://en.wikipedia.org/wiki/Magna_Carta'),
            ('United States Constitution', 'The U.S. Constitution established the framework of the federal government and separation of powers.', 'It is one of the most influential legal documents in modern history.', 'https://en.wikipedia.org/wiki/United_States_Constitution'),
            ('Bill of Rights', 'The Bill of Rights added the first ten amendments to the U.S. Constitution.', 'These amendments protect core civil liberties such as speech, religion, and due process.', 'https://en.wikipedia.org/wiki/United_States_Bill_of_Rights'),
            ('Marbury v. Madison', 'Marbury v. Madison helped establish the principle of judicial review in the United States.', 'The case gave the Supreme Court lasting power to strike down unconstitutional laws.', 'https://en.wikipedia.org/wiki/Marbury_v._Madison'),
            ('Brown v. Board of Education', 'Brown v. Board of Education declared racial segregation in public schools unconstitutional.', 'It became one of the central legal victories of the civil-rights movement.', 'https://en.wikipedia.org/wiki/Brown_v._Board_of_Education'),
            ('Miranda v. Arizona', 'Miranda v. Arizona led to the famous police warning about the right to remain silent and the right to counsel.', 'The decision became one of the most recognized rulings in American criminal procedure.', 'https://en.wikipedia.org/wiki/Miranda_v._Arizona'),
            ('Gideon v. Wainwright', 'Gideon v. Wainwright affirmed the right of criminal defendants to legal counsel in serious cases.', 'It became a major case in the history of procedural justice in the United States.', 'https://en.wikipedia.org/wiki/Gideon_v._Wainwright'),
            ('Civil Rights Act of 1964', 'The Civil Rights Act of 1964 outlawed major forms of discrimination in public life.', 'It stands as one of the foundational laws of modern American civil-rights law.', 'https://en.wikipedia.org/wiki/Civil_Rights_Act_of_1964'),
            ('Voting Rights Act of 1965', 'The Voting Rights Act of 1965 targeted discriminatory barriers to voting.', 'It became one of the most important federal laws ever passed to protect democratic participation.', 'https://en.wikipedia.org/wiki/Voting_Rights_Act_of_1965'),
            ('Roe v. Wade', 'Roe v. Wade became one of the most debated Supreme Court decisions in American legal history.', 'Its legacy shaped decades of political and constitutional conflict over abortion rights.', 'https://en.wikipedia.org/wiki/Roe_v._Wade'),
            ('Obergefell v. Hodges', 'Obergefell v. Hodges recognized a constitutional right to same-sex marriage in the United States.', 'The ruling became a landmark in modern equal-protection and civil-rights law.', 'https://en.wikipedia.org/wiki/Obergefell_v._Hodges'),
            ('Supreme Court of the United States', 'The Supreme Court is the highest court in the United States.', 'Its decisions have shaped civil rights, federal power, criminal justice, and constitutional interpretation.', 'https://en.wikipedia.org/wiki/Supreme_Court_of_the_United_States'),
        ],
    },
    'roman-history': {
        'hobby': 'Roman History',
        'entries': [
            ('Roman Republic', 'The Roman Republic shaped ideas of citizenship, senate rule, and imperial expansion before the rise of the emperors.', 'Its political conflicts and institutions remain central to the study of Roman history.', 'https://en.wikipedia.org/wiki/Roman_Republic'),
            ('Julius Caesar', 'Julius Caesar became one of the most famous figures of the late Roman Republic.', 'His career, conquest of Gaul, and assassination changed the course of Roman history.', 'https://en.wikipedia.org/wiki/Julius_Caesar'),
            ('Augustus', 'Augustus became the first Roman emperor and established the Principate.', 'His long reign marked the transition from republic to imperial rule.', 'https://en.wikipedia.org/wiki/Augustus'),
            ('Colosseum', 'The Colosseum became one of the best-known monuments of ancient Rome.', 'It reflects the scale of public entertainment and imperial building in Roman society.', 'https://en.wikipedia.org/wiki/Colosseum'),
            ('Roman Forum', 'The Roman Forum served as the civic heart of ancient Rome.', 'Politics, religion, law, and public ceremony all played out in and around this space.', 'https://en.wikipedia.org/wiki/Roman_Forum'),
            ('Hadrian\'s Wall', 'Hadrian\'s Wall marked the northern frontier of Roman Britain.', 'It remains one of the most famous surviving frontier works from the Roman Empire.', 'https://en.wikipedia.org/wiki/Hadrian%27s_Wall'),
            ('Pompeii', 'Pompeii preserves a remarkable snapshot of Roman urban life before the eruption of Mount Vesuvius.', 'Its ruins became essential to understanding daily life in the Roman world.', 'https://en.wikipedia.org/wiki/Pompeii'),
            ('Pantheon', 'The Pantheon in Rome is one of the best-preserved buildings from antiquity.', 'Its dome and design continue to influence architecture around the world.', 'https://en.wikipedia.org/wiki/Pantheon,_Rome'),
            ('Pax Romana', 'The Pax Romana refers to a long period of relative stability across much of the Roman Empire.', 'It is often associated with imperial consolidation, law, trade, and infrastructure.', 'https://en.wikipedia.org/wiki/Pax_Romana'),
            ('Roman roads', 'Roman roads helped connect cities, frontiers, and military outposts across a vast empire.', 'Their construction and planning became one of the most admired engineering achievements of ancient Rome.', 'https://en.wikipedia.org/wiki/Roman_roads'),
            ('Constantine the Great', 'Constantine the Great played a central role in the Christianization of the Roman Empire.', 'His reign also included the founding of Constantinople as a new imperial capital.', 'https://en.wikipedia.org/wiki/Constantine_the_Great'),
            ('Fall of the Western Roman Empire', 'The fall of the Western Roman Empire in the 5th century became one of the classic turning points in European history.', 'Historians still debate how and why Roman power in the West came apart.', 'https://en.wikipedia.org/wiki/Fall_of_the_Western_Roman_Empire'),
        ],
    },
    'egyptian-history': {
        'hobby': 'Egyptian History',
        'entries': [
            ('Narmer', 'Narmer is often associated with the early unification of Upper and Lower Egypt.', 'His reign stands near the beginning of dynastic Egyptian history.', 'https://en.wikipedia.org/wiki/Narmer'),
            ('Old Kingdom of Egypt', 'The Old Kingdom is the era most closely associated with the building of the great pyramids.', 'It became one of the foundational periods of ancient Egyptian history.', 'https://en.wikipedia.org/wiki/Old_Kingdom_of_Egypt'),
            ('Pyramids of Giza', 'The Pyramids of Giza are among the most famous monuments in the ancient world.', 'They remain central to how many people imagine Egyptian history.', 'https://en.wikipedia.org/wiki/Giza_pyramid_complex'),
            ('Hatshepsut', 'Hatshepsut became one of the most famous female pharaohs of ancient Egypt.', 'Her reign is known for trade, monumental building, and royal self-presentation.', 'https://en.wikipedia.org/wiki/Hatshepsut'),
            ('Akhenaten', 'Akhenaten is remembered for his dramatic religious reforms centered on the Aten.', 'His reign remains one of the most unusual and debated episodes in Egyptian history.', 'https://en.wikipedia.org/wiki/Akhenaten'),
            ('Tutankhamun', 'Tutankhamun became globally famous after the discovery of his tomb in 1922.', 'The treasures from his burial helped drive worldwide fascination with ancient Egypt.', 'https://en.wikipedia.org/wiki/Tutankhamun'),
            ('Ramesses II', 'Ramesses II ruled for decades and became one of the best-known pharaohs in Egyptian history.', 'His monuments and inscriptions appear across major temple sites in Egypt.', 'https://en.wikipedia.org/wiki/Ramesses_II'),
            ('Rosetta Stone', 'The Rosetta Stone became essential to deciphering ancient Egyptian hieroglyphs.', 'Its discovery transformed the study of Egyptian history and language.', 'https://en.wikipedia.org/wiki/Rosetta_Stone'),
            ('Cleopatra', 'Cleopatra VII became one of the most famous rulers of the ancient Mediterranean world.', 'Her life connected the final era of pharaonic Egypt with Roman power politics.', 'https://en.wikipedia.org/wiki/Cleopatra'),
            ('Nile River', 'The Nile shaped settlement, farming, religion, and kingship across Egyptian history.', 'Ancient Egypt is often described as a civilization built around the rhythms of the Nile.', 'https://en.wikipedia.org/wiki/Nile'),
            ('Valley of the Kings', 'The Valley of the Kings became the burial site for many New Kingdom pharaohs.', 'Its tombs remain some of the most important sources for ancient Egyptian history.', 'https://en.wikipedia.org/wiki/Valley_of_the_Kings'),
            ('Abu Simbel', 'The temples of Abu Simbel show the monumental ambition of Ramesses II\'s reign.', 'They remain among the most striking sites connected to ancient Egyptian state power.', 'https://en.wikipedia.org/wiki/Abu_Simbel'),
        ],
    },
}

TEMPLATES = [
    lambda subject, detail, extra, hobby: detail,
    lambda subject, detail, extra, hobby: extra,
    lambda subject, detail, extra, hobby: f"{subject} is one of the most important topics associated with {hobby}.",
    lambda subject, detail, extra, hobby: f"Books, documentaries, and classrooms that cover {hobby} frequently highlight {subject}.",
    lambda subject, detail, extra, hobby: f"Learning about {subject} helps explain a major part of {hobby}.",
    lambda subject, detail, extra, hobby: f"For many readers, {subject} stands out as one of the defining subjects in {hobby}.",
    lambda subject, detail, extra, hobby: f"The story of {subject} is closely tied to the broader themes of {hobby}.",
    lambda subject, detail, extra, hobby: f"{subject} is often used to introduce students to the history and significance of {hobby}.",
    lambda subject, detail, extra, hobby: f"Many surveys of {hobby} return again and again to the importance of {subject}.",
    lambda subject, detail, extra, hobby: f"From public memory to scholarship, {subject} plays a notable role in how people understand {hobby}.",
    lambda subject, detail, extra, hobby: f"One reason {hobby} remains so compelling is the lasting significance of {subject}.",
    lambda subject, detail, extra, hobby: f"The legacy of {subject} continues to shape how {hobby} is discussed today.",
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
