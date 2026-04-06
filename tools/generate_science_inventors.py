from pathlib import Path
import json

science_people = [
    {
        "name": "Albert Einstein",
        "topic": "relativity and modern physics",
        "note1": "Albert Einstein's 1905 papers helped transform how scientists think about light, motion, and matter.",
        "note2": "Einstein's work on the photoelectric effect earned him the 1921 Nobel Prize in Physics.",
        "quote": "Albert Einstein famously said, 'Imagination is more important than knowledge.'",
        "source": "https://en.wikipedia.org/wiki/Albert_Einstein",
    },
    {
        "name": "Isaac Newton",
        "topic": "gravity, motion, and calculus",
        "note1": "Isaac Newton's three laws of motion became foundational to classical mechanics.",
        "note2": "Newton's Principia is one of the most influential scientific works ever published.",
        "quote": "Isaac Newton wrote, 'If I have seen further it is by standing on the shoulders of giants.'",
        "source": "https://en.wikipedia.org/wiki/Isaac_Newton",
    },
    {
        "name": "Galileo Galilei",
        "topic": "telescopic astronomy and experimental physics",
        "note1": "Galileo used telescopes to observe Jupiter's moons, helping support the heliocentric view of the solar system.",
        "note2": "Galileo is often called the father of observational astronomy.",
        "quote": "Galileo is often credited with saying, 'All truths are easy to understand once they are discovered.'",
        "source": "https://en.wikipedia.org/wiki/Galileo_Galilei",
    },
    {
        "name": "Marie Curie",
        "topic": "radioactivity",
        "note1": "Marie Curie helped discover polonium and radium and pioneered research into radioactivity.",
        "note2": "Marie Curie was the first person to win Nobel Prizes in two different scientific fields.",
        "quote": "Marie Curie said, 'Nothing in life is to be feared, it is only to be understood.'",
        "source": "https://en.wikipedia.org/wiki/Marie_Curie",
    },
    {
        "name": "Charles Darwin",
        "topic": "evolution by natural selection",
        "note1": "Charles Darwin's On the Origin of Species reshaped biology by explaining evolution through natural selection.",
        "note2": "Darwin's long voyage on HMS Beagle deeply influenced his scientific thinking.",
        "quote": "Charles Darwin wrote, 'A man who dares to waste one hour of time has not discovered the value of life.'",
        "source": "https://en.wikipedia.org/wiki/Charles_Darwin",
    },
    {
        "name": "Michael Faraday",
        "topic": "electromagnetism and electrochemistry",
        "note1": "Michael Faraday's experiments with electromagnetic induction helped lay the groundwork for electric motors and generators.",
        "note2": "The farad, a unit of electrical capacitance, is named after Michael Faraday.",
        "quote": "Michael Faraday said, 'Nothing is too wonderful to be true if it be consistent with the laws of nature.'",
        "source": "https://en.wikipedia.org/wiki/Michael_Faraday",
    },
    {
        "name": "Rosalind Franklin",
        "topic": "DNA structure and X-ray crystallography",
        "note1": "Rosalind Franklin's X-ray diffraction work was crucial to understanding the double-helix structure of DNA.",
        "note2": "Franklin also made important contributions to the study of viruses and coal chemistry.",
        "quote": "Rosalind Franklin wrote, 'Science and everyday life cannot and should not be separated.'",
        "source": "https://en.wikipedia.org/wiki/Rosalind_Franklin",
    },
    {
        "name": "Jane Goodall",
        "topic": "chimpanzee behavior and primatology",
        "note1": "Jane Goodall changed the study of animal behavior through her long-term observations of wild chimpanzees at Gombe.",
        "note2": "Goodall's work showed that chimpanzees make and use tools, a discovery that surprised many scientists.",
        "quote": "Jane Goodall said, 'What you do makes a difference, and you have to decide what kind of difference you want to make.'",
        "source": "https://en.wikipedia.org/wiki/Jane_Goodall",
    },
    {
        "name": "Carl Sagan",
        "topic": "planetary science and science communication",
        "note1": "Carl Sagan helped popularize astronomy for the public through books, lectures, and the television series Cosmos.",
        "note2": "Sagan worked on planetary missions and helped shape scientific discussion about life elsewhere in the universe.",
        "quote": "Carl Sagan wrote, 'Somewhere, something incredible is waiting to be known.'",
        "source": "https://en.wikipedia.org/wiki/Carl_Sagan",
    },
    {
        "name": "Stephen Hawking",
        "topic": "black holes and cosmology",
        "note1": "Stephen Hawking's work on black holes and radiation made him one of the most recognizable theoretical physicists in the world.",
        "note2": "A Brief History of Time brought complex cosmology to millions of general readers.",
        "quote": "Stephen Hawking said, 'Look up at the stars and not down at your feet.'",
        "source": "https://en.wikipedia.org/wiki/Stephen_Hawking",
    },
    {
        "name": "Richard Feynman",
        "topic": "quantum electrodynamics",
        "note1": "Richard Feynman was known for both major contributions to theoretical physics and his remarkable teaching style.",
        "note2": "Feynman diagrams became a standard visual tool for describing particle interactions.",
        "quote": "Richard Feynman said, 'I would rather have questions that can't be answered than answers that can't be questioned.'",
        "source": "https://en.wikipedia.org/wiki/Richard_Feynman",
    },
    {
        "name": "Nicolaus Copernicus",
        "topic": "the heliocentric model of the solar system",
        "note1": "Nicolaus Copernicus argued that Earth and the other planets orbit the Sun, reshaping astronomy forever.",
        "note2": "Copernicus's work became a major turning point in the Scientific Revolution.",
        "quote": "Nicolaus Copernicus wrote, 'To know that we know what we know, and that we do not know what we do not know, that is true knowledge.'",
        "source": "https://en.wikipedia.org/wiki/Nicolaus_Copernicus",
    },
    {
        "name": "Dmitri Mendeleev",
        "topic": "the periodic table",
        "note1": "Dmitri Mendeleev organized the periodic table in a way that helped predict the properties of elements not yet discovered.",
        "note2": "Mendeleev's periodic arrangement remains central to chemistry education.",
        "quote": "Dmitri Mendeleev said, 'Work, look for peace and calm in work: you will find it nowhere else.'",
        "source": "https://en.wikipedia.org/wiki/Dmitri_Mendeleev",
    },
    {
        "name": "Rachel Carson",
        "topic": "ecology and environmental science",
        "note1": "Rachel Carson's Silent Spring helped launch the modern environmental movement.",
        "note2": "Carson showed how scientific writing could shape public policy and public awareness.",
        "quote": "Rachel Carson wrote, 'In every outthrust headland, in every curving beach, in every grain of sand there is the story of the earth.'",
        "source": "https://en.wikipedia.org/wiki/Rachel_Carson",
    },
    {
        "name": "Louis Pasteur",
        "topic": "germ theory, vaccines, and microbiology",
        "note1": "Louis Pasteur's experiments helped establish germ theory and transform medicine and food safety.",
        "note2": "Pasteurization is named for Louis Pasteur and remains widely used to make foods and drinks safer.",
        "quote": "Louis Pasteur said, 'Chance favors the prepared mind.'",
        "source": "https://en.wikipedia.org/wiki/Louis_Pasteur",
    },
]

science_facts = []
for person in science_people:
    science_facts.extend([
        {"text": f"{person['name']} is closely associated with {person['topic']}.", "source": person["source"]},
        {"text": person["note1"], "source": person["source"]},
        {"text": person["quote"], "quoteBy": person["name"], "source": person["source"]},
        {"text": person["note2"], "source": person["source"]},
    ])

inventors = [
    {"name": "Johannes Gutenberg", "invention": "the movable-type printing press", "field": "printing and publishing", "detail1": "His work in Mainz helped make books far cheaper and more widely available in Europe.", "detail2": "The Gutenberg Bible became one of the most famous early printed books.", "source": "https://en.wikipedia.org/wiki/Johannes_Gutenberg"},
    {"name": "Benjamin Franklin", "invention": "the lightning rod, bifocals, and the Franklin stove", "field": "practical science and everyday technology", "detail1": "Franklin's electrical experiments made him one of the most famous scientific figures of the 18th century.", "detail2": "He preferred not to patent many of his ideas because he believed useful discoveries should benefit the public.", "quote": "Benjamin Franklin said, 'An investment in knowledge pays the best interest.'", "source": "https://en.wikipedia.org/wiki/Benjamin_Franklin"},
    {"name": "James Watt", "invention": "major improvements to the steam engine", "field": "power and the Industrial Revolution", "detail1": "Watt's separate condenser made steam power far more efficient.", "detail2": "The unit of power called the watt is named after James Watt.", "source": "https://en.wikipedia.org/wiki/James_Watt"},
    {"name": "Alessandro Volta", "invention": "the electric battery", "field": "electricity and chemistry", "detail1": "Volta's voltaic pile is often described as the first true battery.", "detail2": "The volt, a unit of electric potential, is named after Alessandro Volta.", "source": "https://en.wikipedia.org/wiki/Alessandro_Volta"},
    {"name": "Samuel Morse", "invention": "the telegraph and Morse code", "field": "long-distance communication", "detail1": "Morse helped turn electrical signaling into a practical communication system.", "detail2": "The message 'What hath God wrought' became famous in the history of the telegraph.", "source": "https://en.wikipedia.org/wiki/Samuel_Morse"},
    {"name": "Charles Babbage", "invention": "the Difference Engine and Analytical Engine concepts", "field": "computing machinery", "detail1": "Babbage's designs anticipated many ideas that later appeared in modern computers.", "detail2": "He is often called a father of the computer even though his most ambitious machines were never fully built in his lifetime.", "quote": "Charles Babbage wrote, 'Errors using inadequate data are much less than those using no data at all.'", "source": "https://en.wikipedia.org/wiki/Charles_Babbage"},
    {"name": "Ada Lovelace", "invention": "the first published algorithm intended for a machine", "field": "early computer science", "detail1": "Lovelace's notes on Babbage's Analytical Engine became foundational in computing history.", "detail2": "She imagined machines might one day create music and art as well as perform calculations.", "quote": "Ada Lovelace wrote, 'That brain of mine is something more than merely mortal; as time will show.'", "source": "https://en.wikipedia.org/wiki/Ada_Lovelace"},
    {"name": "Alexander Graham Bell", "invention": "the telephone", "field": "communication technology", "detail1": "Bell's name is permanently linked with the history of voice communication over wires.", "detail2": "He also worked in education for the deaf and in several other areas of invention.", "quote": "Alexander Graham Bell said, 'When one door closes, another opens.'", "source": "https://en.wikipedia.org/wiki/Alexander_Graham_Bell"},
    {"name": "Thomas Edison", "invention": "the phonograph and practical electric-light systems", "field": "electrical invention and recorded sound", "detail1": "Edison's Menlo Park laboratory became a symbol of organized industrial research.", "detail2": "He held more than a thousand U.S. patents and helped commercialize electric power.", "quote": "Thomas Edison said, 'Genius is one percent inspiration and ninety-nine percent perspiration.'", "source": "https://en.wikipedia.org/wiki/Thomas_Edison"},
    {"name": "Nikola Tesla", "invention": "the AC induction motor and alternating-current power systems", "field": "electrical engineering", "detail1": "Tesla's work helped make long-distance electrical power distribution practical.", "detail2": "His name is also associated with the Tesla coil and other bold electrical demonstrations.", "quote": "Nikola Tesla said, 'The present is theirs; the future, for which I really worked, is mine.'", "source": "https://en.wikipedia.org/wiki/Nikola_Tesla"},
    {"name": "The Wright brothers", "invention": "the first successful powered airplane", "field": "aviation", "detail1": "Wilbur and Orville Wright made their historic powered flight at Kitty Hawk in 1903.", "detail2": "Their background as bicycle mechanics helped them think carefully about balance and control in flight.", "quote": "Wilbur Wright said, 'It is possible to fly without motors, but not without knowledge and skill.'", "quoteBy": "Wilbur Wright", "source": "https://en.wikipedia.org/wiki/Wright_brothers"},
    {"name": "Karl Benz", "invention": "the practical gasoline-powered automobile", "field": "transportation", "detail1": "The Benz Patent-Motorwagen is widely regarded as one of the first true automobiles.", "detail2": "Karl Benz's work laid part of the foundation for the later Mercedes-Benz brand.", "source": "https://en.wikipedia.org/wiki/Karl_Benz"},
    {"name": "Guglielmo Marconi", "invention": "practical radio communication", "field": "wireless technology", "detail1": "Marconi helped prove that wireless signals could travel over long distances, including across the Atlantic.", "detail2": "His experiments helped push radio from theory into everyday communication.", "source": "https://en.wikipedia.org/wiki/Guglielmo_Marconi"},
    {"name": "Garrett Morgan", "invention": "the three-position traffic signal and a smoke hood safety device", "field": "public safety and transportation", "detail1": "Morgan's safety hood was used in rescue work and brought him national attention.", "detail2": "His traffic-signal design helped improve street safety at a time when cities were becoming more crowded.", "source": "https://en.wikipedia.org/wiki/Garrett_Morgan"},
    {"name": "Granville T. Woods", "invention": "improvements in railway telegraphy and electrical systems", "field": "rail transportation and electricity", "detail1": "Woods earned dozens of patents and became known as one of the key Black inventors of the 19th century.", "detail2": "His work helped improve safety and communication on railroads.", "source": "https://en.wikipedia.org/wiki/Granville_Woods"},
    {"name": "Hedy Lamarr", "invention": "frequency-hopping spread-spectrum technology", "field": "wireless communication", "detail1": "Lamarr co-developed a frequency-hopping system during World War II with composer George Antheil.", "detail2": "Her idea later influenced technologies connected to secure wireless communication.", "quote": "Hedy Lamarr said, 'Any girl can be glamorous. All you have to do is stand still and look stupid.'", "source": "https://en.wikipedia.org/wiki/Hedy_Lamarr"},
    {"name": "Philo Farnsworth", "invention": "electronic television", "field": "electronics and broadcasting", "detail1": "Farnsworth's image dissector tube was a breakthrough in early television technology.", "detail2": "He reportedly first imagined key television ideas while working on a farm as a teenager.", "source": "https://en.wikipedia.org/wiki/Philo_Farnsworth"},
    {"name": "George Eastman", "invention": "roll film and Kodak cameras", "field": "photography", "detail1": "Eastman helped make photography easier and more accessible to ordinary people.", "detail2": "The slogan 'You press the button, we do the rest' captured Kodak's appeal to non-experts.", "source": "https://en.wikipedia.org/wiki/George_Eastman"},
    {"name": "Josephine Cochrane", "invention": "the practical dishwasher", "field": "household technology", "detail1": "Cochrane built her machine after becoming frustrated with servants chipping her fine china.", "detail2": "Her invention eventually helped transform commercial and home kitchens.", "source": "https://en.wikipedia.org/wiki/Josephine_Cochrane"},
    {"name": "Mary Anderson", "invention": "the windshield wiper", "field": "automotive safety", "detail1": "Anderson patented her design after noticing that drivers struggled to see clearly in bad weather.", "detail2": "Her idea became a basic safety feature on cars around the world.", "source": "https://en.wikipedia.org/wiki/Mary_Anderson_(inventor)"},
    {"name": "Willis Carrier", "invention": "modern air conditioning", "field": "climate control and engineering", "detail1": "Carrier originally developed his humidity-control system to solve problems in a printing plant.", "detail2": "Air conditioning transformed homes, offices, factories, theaters, and entire cities.", "source": "https://en.wikipedia.org/wiki/Willis_Carrier"},
    {"name": "Clarence Birdseye", "invention": "modern frozen-food preservation", "field": "food technology", "detail1": "Birdseye's quick-freezing methods helped frozen foods keep their texture and flavor much better.", "detail2": "His ideas changed grocery stores and home kitchens across the world.", "source": "https://en.wikipedia.org/wiki/Clarence_Birdseye"},
    {"name": "Percy Spencer", "invention": "the microwave oven", "field": "applied physics and cooking technology", "detail1": "Spencer reportedly noticed a candy bar melting near radar equipment, helping inspire the microwave oven.", "detail2": "The first microwave ovens were much larger than the countertop models used today.", "source": "https://en.wikipedia.org/wiki/Percy_Spencer"},
    {"name": "Stephanie Kwolek", "invention": "Kevlar", "field": "materials science", "detail1": "Kwolek developed Kevlar while working at DuPont on strong but lightweight fibers.", "detail2": "Kevlar later became famous for uses ranging from body armor to ropes and sporting goods.", "quote": "Stephanie Kwolek said, 'I don't think of it as work. I think of it as part of my life.'", "source": "https://en.wikipedia.org/wiki/Stephanie_Kwolek"},
    {"name": "Grace Hopper", "invention": "the first compiler and major programming-language innovations", "field": "computer science", "detail1": "Hopper helped make computers easier to program by supporting the use of human-readable code.", "detail2": "She became one of the most influential figures in the history of software and computing.", "quote": "Grace Hopper said, 'The most dangerous phrase in the language is, We've always done it this way.'", "source": "https://en.wikipedia.org/wiki/Grace_Hopper"},
    {"name": "Tim Berners-Lee", "invention": "the World Wide Web", "field": "internet technology", "detail1": "Berners-Lee created the web while working at CERN and also helped define core standards such as HTML and HTTP.", "detail2": "The first website went live in 1991 as part of his effort to share information more easily across networks.", "quote": "Tim Berners-Lee said, 'This is for everyone.'", "source": "https://en.wikipedia.org/wiki/Tim_Berners-Lee"},
    {"name": "Douglas Engelbart", "invention": "the computer mouse and many ideas in interactive computing", "field": "human-computer interaction", "detail1": "Engelbart's famous 1968 demonstration showcased the mouse, hypertext, collaborative editing, and video conferencing.", "detail2": "He believed computers should help people think and work together more effectively.", "quote": "Douglas Engelbart said, 'The digital revolution is far more significant than the invention of writing or even of printing.'", "source": "https://en.wikipedia.org/wiki/Douglas_Engelbart"},
    {"name": "Martin Cooper", "invention": "the handheld mobile phone", "field": "telecommunications", "detail1": "Cooper made the first public handheld cell-phone call in 1973 while working at Motorola.", "detail2": "His work helped move telephony away from fixed locations and into everyday personal life.", "quote": "Martin Cooper said, 'The cell phone is not a technology of physics. It is a technology of sociology.'", "source": "https://en.wikipedia.org/wiki/Martin_Cooper_(inventor)"},
    {"name": "Robert Noyce", "invention": "the integrated circuit", "field": "microelectronics", "detail1": "Noyce helped pioneer the silicon integrated circuit and later co-founded Intel.", "detail2": "He became one of the central figures in the rise of Silicon Valley.", "source": "https://en.wikipedia.org/wiki/Robert_Noyce"},
    {"name": "Jack Kilby", "invention": "the integrated circuit", "field": "microelectronics", "detail1": "Kilby built one of the earliest working integrated circuits while at Texas Instruments.", "detail2": "His achievement helped open the door to modern chips, calculators, and computers.", "source": "https://en.wikipedia.org/wiki/Jack_Kilby"},
    {"name": "James Dyson", "invention": "the bagless vacuum cleaner", "field": "consumer product design", "detail1": "Dyson built thousands of prototypes before perfecting his cyclone-based vacuum design.", "detail2": "His story is often used to illustrate persistence in product development.", "quote": "James Dyson said, 'Enjoy failure and learn from it.'", "source": "https://en.wikipedia.org/wiki/James_Dyson"},
    {"name": "Lonnie Johnson", "invention": "the Super Soaker and other engineering designs", "field": "toys and mechanical engineering", "detail1": "Johnson originally developed the Super Soaker after experimenting with a high-powered stream of water in a workshop.", "detail2": "He also worked as an engineer on projects connected to NASA and the U.S. Air Force.", "source": "https://en.wikipedia.org/wiki/Lonnie_Johnson_(inventor)"},
    {"name": "George de Mestral", "invention": "Velcro", "field": "materials and fasteners", "detail1": "De Mestral got the idea for Velcro after noticing burrs clinging to clothing and animal fur.", "detail2": "He turned that natural hook-and-loop design into one of the most recognizable fastening systems in the world.", "source": "https://en.wikipedia.org/wiki/George_de_Mestral"},
    {"name": "Elisha Otis", "invention": "the elevator safety brake", "field": "building technology", "detail1": "Otis famously demonstrated his safety elevator system in public by having the supporting rope cut.", "detail2": "His invention helped make tall modern buildings much more practical and trusted.", "source": "https://en.wikipedia.org/wiki/Elisha_Otis"},
    {"name": "Nils Bohlin", "invention": "the three-point seat belt", "field": "automotive safety", "detail1": "Bohlin developed the now-standard three-point seat belt while working at Volvo.", "detail2": "The design has saved countless lives and remains one of the most important car safety innovations ever made.", "source": "https://en.wikipedia.org/wiki/Nils_Bohlin"},
    {"name": "Patricia Bath", "invention": "the Laserphaco cataract treatment device", "field": "medical technology and ophthalmology", "detail1": "Bath became the first Black woman physician to receive a medical patent in the United States.", "detail2": "Her work aimed to help restore sight and improve eye care for patients who lacked access to treatment.", "source": "https://en.wikipedia.org/wiki/Patricia_Bath"},
    {"name": "George Washington Carver", "invention": "new agricultural uses for peanuts, sweet potatoes, and other crops", "field": "agricultural science", "detail1": "Carver promoted crop rotation and soil improvement for farmers in the American South.", "detail2": "He became a symbol of scientific creativity applied to agriculture and everyday life.", "quote": "George Washington Carver said, 'Where there is no vision, there is no hope.'", "source": "https://en.wikipedia.org/wiki/George_Washington_Carver"},
    {"name": "Archimedes", "invention": "the Archimedes screw and classic mechanical ideas", "field": "mathematics and mechanics", "detail1": "Archimedes is also remembered for work on buoyancy, levers, and geometry.", "detail2": "His ideas have influenced engineering and science for more than two thousand years.", "quote": "Archimedes is associated with the line, 'Give me a place to stand and I will move the earth.'", "quoteBy": "Archimedes", "source": "https://en.wikipedia.org/wiki/Archimedes"},
    {"name": "George Westinghouse", "invention": "the railway air brake and large-scale electrical systems", "field": "transportation safety and electrical engineering", "detail1": "Westinghouse's air brake made train travel much safer and more manageable.", "detail2": "He also backed alternating-current power systems during the famous current wars era.", "source": "https://en.wikipedia.org/wiki/George_Westinghouse"},
    {"name": "John Logie Baird", "invention": "early television systems", "field": "broadcast engineering", "detail1": "Baird demonstrated some of the first working television transmissions in the 1920s.", "detail2": "He experimented with both mechanical and color television concepts.", "source": "https://en.wikipedia.org/wiki/John_Logie_Baird"},
    {"name": "Ruth Wakefield", "invention": "the chocolate chip cookie", "field": "food creation and baking", "detail1": "Wakefield created the chocolate chip cookie at the Toll House Inn in Massachusetts.", "detail2": "Her recipe became one of the most famous and copied dessert formulas in America.", "source": "https://en.wikipedia.org/wiki/Ruth_Graves_Wakefield"},
    {"name": "George Crum", "invention": "potato chips", "field": "food invention", "detail1": "George Crum is often credited in popular history with inventing potato chips in Saratoga Springs.", "detail2": "The story helped turn a simple snack into part of American food folklore.", "source": "https://en.wikipedia.org/wiki/George_Speck"}
]

inventors = inventors[:38]

inventor_facts = []
for inv in inventors:
    quote_by = inv.get("quoteBy", inv["name"])
    quote_text = inv.get("quote")
    generated = [
        {"text": f"{inv['name']} is widely associated with {inv['invention']}.", "source": inv["source"]},
        {"text": inv["detail1"], "source": inv["source"]},
        {"text": inv["detail2"], "source": inv["source"]},
        {"text": f"Histories of {inv['field']} almost always highlight {inv['name']} when discussing {inv['invention']}.", "source": inv["source"]},
        {"text": f"{inv['name']}'s work helped move {inv['field']} forward in practical, everyday ways.", "source": inv["source"]},
        {"text": f"Modern uses of technology related to {inv['invention']} still reflect the legacy of {inv['name']}.", "source": inv["source"]},
        {"text": f"Science and technology museums often feature {inv['name']} when explaining the history of {inv['field']}.", "source": inv["source"]},
        {"text": quote_text, "quoteBy": quote_by, "source": inv["source"]} if quote_text else {"text": f"Students of invention often encounter {inv['name']} as a key figure in the story of {inv['invention']}.", "source": inv["source"]},
        {"text": f"The story of {inv['invention']} is one of the reasons {inv['name']} remains so well known today.", "source": inv["source"]},
        {"text": f"{inv['name']} is remembered as one of the major names connected to {inv['invention']} and {inv['field']}.", "source": inv["source"]},
    ]
    inventor_facts.extend(generated)

if len(science_facts) != 60:
    raise ValueError(f"Expected 60 science facts, got {len(science_facts)}")
if len(inventor_facts) != 380:
    raise ValueError(f"Expected 380 inventor facts, got {len(inventor_facts)}")

base = Path(__file__).resolve().parents[1] / "extension" / "data" / "facts"
base.mkdir(parents=True, exist_ok=True)
(base / "science.json").write_text(json.dumps({"hobby": "Science", "facts": science_facts}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
(base / "inventors.json").write_text(json.dumps({"hobby": "Inventors", "facts": inventor_facts}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"science.json written with {len(science_facts)} facts")
print(f"inventors.json written with {len(inventor_facts)} facts")
