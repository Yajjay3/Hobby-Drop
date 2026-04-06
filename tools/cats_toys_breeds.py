#!/usr/bin/env python3
"""Add cat toys and international breeds facts."""
import json

path = 'extension/data/facts/cats.json'
with open(path) as f:
    data = json.load(f)

extra = [
    # CAT TOYS & ENRICHMENT
    {"text": "The laser pointer is one of the most popular cat toys, but experts recommend ending play with a physical toy so cats get the satisfaction of 'catching' something."},
    {"text": "Feather wands (like Da Bird) mimic the movement of birds in flight and trigger a cat's natural hunting instincts more effectively than most toys.", "type": "did-you-know"},
    {"text": "Catnip toys work because the chemical nepetalactone in catnip binds to receptors in a cat's nose, triggering a euphoric response lasting about 10 minutes."},
    {"text": "Puzzle feeders and food-dispensing toys help prevent obesity and boredom in indoor cats by making them 'hunt' for their meals."},
    {"text": "The classic ball-in-a-track toy (like Catit Senses) keeps cats entertained for hours because it mimics the unpredictable movement of prey."},
    {"text": "Crinkle balls are irresistible to many cats because the crinkling sound mimics the rustling of small prey animals in leaves and grass.", "type": "did-you-know"},
    {"text": "Cat tunnels satisfy a cat's instinct to hide, ambush, and explore — they're one of the most universally loved cat toys."},
    {"text": "The 'fishing rod' style toy was inspired by actual fly fishing and is considered the gold standard for interactive cat play."},
    {"text": "Silvervine sticks from East Asia are a popular alternative to catnip toys — they affect about 80% of cats, including many who don't respond to catnip."},
    {"text": "Automated laser toys like the FroliCat can keep cats entertained when owners are away, though vets recommend supervised interactive play as primary exercise."},
    {"text": "Kicker toys (long, body-pillow shaped toys) let cats grab with their front paws and 'bunny kick' with their hind legs — mimicking how they take down prey.", "type": "did-you-know"},
    {"text": "Cat wheels (giant hamster wheels for cats) have become popular for high-energy breeds like Bengals and Savannahs — some cats run for hours."},
    {"text": "Simple cardboard boxes remain one of the most beloved 'toys' for cats — studies show boxes reduce stress by providing a secure hiding spot."},
    {"text": "Motorized mouse toys that dart and change direction simulate real prey behavior and can keep cats engaged much longer than stationary toys."},
    {"text": "Cat trees and scratching posts are not just toys but essential furniture — they satisfy climbing, scratching, and territorial marking instincts.", "type": "did-you-know"},
    {"text": "Window-mounted bird feeders ('cat TV') provide endless entertainment for indoor cats and satisfy their bird-watching instincts."},
    {"text": "Valerian root toys produce a similar euphoric effect to catnip in many cats and work on some cats that are immune to catnip."},
    {"text": "Interactive treat-dispensing balls help slow down fast eaters and provide mental stimulation — a key need for indoor cats."},

    # BREEDS FROM DIFFERENT COUNTRIES
    {"text": "The Thai cat (Wichien Maat) is Thailand's oldest breed, predating the Western Siamese — ancient manuscripts describe them as 'diamonds of the moon.'"},
    {"text": "The Van Kedisi from Turkey is a pure white cat with odd-colored eyes (one blue, one amber) — it's considered a national treasure.", "type": "did-you-know"},
    {"text": "The Aegean cat from Greece is one of the oldest natural breeds, developed on the Cycladic Islands, and is the only breed native to Greece."},
    {"text": "The Brazilian Shorthair is the first cat breed developed in Brazil, recognized from street cats that evolved naturally over centuries."},
    {"text": "The Arabian Mau is native to the Arabian Peninsula and has adapted to desert life — it's been a natural breed for over 1,000 years."},
    {"text": "The Suphalak from Thailand is one of the rarest breeds in the world — ancient Thai manuscripts describe it as having a coat 'the color of copper.'", "type": "did-you-know"},
    {"text": "The Cyprus cat (Saint Helen cat) may be the earliest example of human-cat companionship, with evidence dating back 9,500 years on the island."},
    {"text": "The Dragon Li (Chinese Li Hua) is China's only recognized native breed — depictions of similar cats appear in ancient Chinese art.", "type": "did-you-know"},
    {"text": "The Korean Bobtail is a natural breed found on the Korean Peninsula for centuries, valued as mousers in traditional Korean homes."},
    {"text": "The Australian Mist was developed in Australia in the 1970s by crossing Burmese, Abyssinian, and domestic tabbies to create a uniquely Australian breed."},
    {"text": "The Kuril Islands between Russia and Japan are home to the Kurilian Bobtail, which developed naturally in isolation for centuries."},
    {"text": "The Sokoke from Kenya was discovered by Jeni Slater in the Arabuko-Sokoke Forest in 1978 — local Giriama people had known the cats for generations.", "type": "did-you-know"},
    {"text": "The Neva Masquerade is a color-pointed variant of the Siberian cat from Russia, named after the Neva River in Saint Petersburg."},
    {"text": "The Raas cat from Indonesia developed naturally on Raas Island in the Java Sea and is extremely rare outside Indonesia."},
    {"text": "The Persian cat, though associated with Iran, was actually developed to its modern form by British breeders in the 1800s using cats from Persia and Turkey."},
    {"text": "The Chartreux is believed to have been bred by Carthusian monks in France since the Middle Ages — they were prized for their mousing abilities.", "type": "did-you-know"},
    {"text": "The Burmese cat traces its entire modern lineage to a single cat named Wong Mau, imported from Rangoon, Burma to San Francisco in 1930."},
    {"text": "The Toyger was created by American breeder Judy Sugden in the 1980s to raise awareness about tiger conservation through its miniature tiger appearance."},
]

data["facts"].extend(extra)
with open(path, 'w') as f:
    json.dump(data, f, ensure_ascii=False)
print(f"Cats total: {len(data['facts'])}")
