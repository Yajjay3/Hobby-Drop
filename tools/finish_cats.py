#!/usr/bin/env python3
"""Finish cats.json - add 35 more facts to reach 366+."""
import json

path = 'extension/data/facts/cats.json'
with open(path) as f:
    data = json.load(f)

extra = [
    {"text": "The Khao Manee is a rare Thai breed with jewel-like eyes — one blue and one gold — considered extremely lucky in Thai culture.", "type": "did-you-know"},
    {"text": "Cats can jump approximately 5 feet vertically from a standstill — equivalent to a human jumping onto a two-story roof."},
    {"text": "The Peterbald is a hairless Russian breed created in 1994 by crossing a Don Sphynx with an Oriental Shorthair."},
    {"text": "Cats have over 20 different vocalizations including the purr, meow, chirp, trill, hiss, growl, and the silent meow."},
    {"text": "A cat named Room 8 lived at a Los Angeles elementary school from 1952 to 1968, becoming so famous he received fan mail.", "type": "did-you-know"},
    {"text": "The Kurilian Bobtail from the Russian Kuril Islands has a pom-pom-like tail, and each tail is as unique as a fingerprint."},
    {"text": "Cats can develop OCD-like behaviors including excessive grooming, repetitive pacing, and wool-sucking."},
    {"text": "Cat DNA is 95.6% identical to tiger DNA — your house cat shares a common ancestor with big cats from about 10.8 million years ago.", "type": "did-you-know"},
    {"text": "Cats produce a pheromone from glands in their cheeks called F3 — synthetic versions (Feliway) are sold to reduce feline stress."},
    {"text": "Cats can be averse to citrus scents — orange and lemon peels are commonly used as natural cat deterrents."},
    {"text": "A cat named Trim sailed around Australia with navigator Matthew Flinders in 1801-1803.", "type": "did-you-know"},
    {"text": "The Cat Writers Association has been giving awards to the best cat-related writing since 1993."},
    {"text": "Cats have a vestibular apparatus in their inner ear that gives them an exceptional sense of balance."},
    {"text": "The Cymric is essentially a long-haired Manx — like the Manx, it can be completely tailless or have a full tail."},
    {"text": "A cat named Dewey Readmore Books inspired a New York Times bestselling book after spending 19 years as a library cat.", "type": "did-you-know"},
    {"text": "Cats use their tails as a counterbalance when walking along narrow surfaces like fences and shelves."},
    {"text": "The Bengal cat gets its name from the Asian Leopard Cat scientific name Prionailurus bengalensis, not the Bengal tiger."},
    {"text": "Cats can learn to respond to sign language — deaf cats can be trained using hand signals just as effectively as verbal commands."},
    {"text": "A cat named Faith received the PDSA Silver Medal for staying with her kittens during WWII bombing raids in London.", "type": "did-you-know"},
    {"text": "The Sokoke is one of the rarest naturally occurring cat breeds, originating from the Arabuko-Sokoke Forest in Kenya."},
    {"text": "Cats have been shown to dream during REM sleep — their movements suggest they may dream about hunting."},
    {"text": "A cat named Scarlett became famous in 1996 for re-entering a burning Brooklyn building five times to rescue each of her kittens.", "type": "did-you-know"},
    {"text": "The Donskoy (Don Sphynx) is a Russian hairless breed unrelated to the Canadian Sphynx — they carry different hairlessness genes."},
    {"text": "Cats can detect ultrasonic frequencies up to 64 kHz, which allows them to hear rodent communication inaudible to humans."},
    {"text": "The world has an estimated 600 million domestic cats, with about 480 million being strays or feral."},
    {"text": "Cats rubbing their face on objects (bunting) deposits pheromones that create a familiar scent profile for their territory."},
    {"text": "The American Bobtail was developed in the 1960s from a wild-looking bobtailed tabby found on an Arizona reservation."},
    {"text": "Cats have been shown to have object permanence — they understand that objects still exist even when hidden from view.", "type": "did-you-know"},
    {"text": "A group of feral cats living together is called a colony, and they often have complex social hierarchies."},
    {"text": "The Ojos Azules breed has strikingly deep blue eyes regardless of coat color — discovered in New Mexico in 1984."},
    {"text": "Cats can spend up to 50% of their day in light sleep (dozing), ready to spring into action at any moment."},
    {"text": "The Lykoi or 'Werewolf Cat' naturally molts most of its fur and has a patchy coat that gives it a wolflike appearance.", "type": "did-you-know"},
    {"text": "The Burmilla was created by accident in 1981 when a Chinchilla Persian and Lilac Burmese mated in a UK household."},
    {"text": "Cat purrs have been connected to increased bone density in studies, leading NASA to research their healing properties."},
    {"text": "The average house cat's brain weighs about 30 grams — about 0.9% of body weight vs 2% for humans."},
]

data["facts"].extend(extra)
with open(path, 'w') as f:
    json.dump(data, f, ensure_ascii=False)
print(f"Cats total: {len(data['facts'])}")
