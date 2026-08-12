---
title: SukhaRakshak AI
summary: India's first AI-powered anticipatory drought advisory system, delivering personalised text and voice advisories in more than 20 Indian languages through a chatbot interface.
status: Operational
flagship: true
weight: 96
deliverables:
  - D5
tags:
  - Drought
  - Early warning
  - Agriculture
  - Machine learning
  - Climate services
  - Earth observation
regions:
  - India
  - South Asia
organisation: IWMI, with ICAR and ICAR-CRIDA
problem: >-
  Drought advice usually arrives as a bulletin: regional, technical, in one
  language, and describing conditions that already exist. A smallholder needs
  something else — what is likely to happen where they farm, what to do about it,
  and in a language and format they can actually use.
capabilities:
  - title: Anticipatory, not just observational
    description: Monitors drought as it emerges and predicts where conditions are heading, then translates both into specific local action.
  - title: Advisories in 20+ Indian languages
    description: Text and voice advisories in more than 20 Indian languages, so access does not depend on literacy or on English.
  - title: Conversational interface
    description: A chatbot that answers questions and returns customised advisories, rather than requiring the user to interpret a map.
  - title: Grounded in local contingency plans
    description: Advice is tied to localised agricultural contingency plans rather than generic guidance.
workflow:
  - stage: Input data
    detail: SADMS drought indicators, Google Earth Engine satellite data, and global forecast systems including NOAA GEFS and CFS.
  - stage: Drought state and outlook
    detail: Current drought conditions combined with probabilistic weather forecasts to anticipate where conditions are heading.
  - stage: AI reasoning layer
    detail: A large language model with retrieval-augmented generation over localised agricultural contingency plans.
  - stage: Language layer
    detail: Text and voice generation in over 20 Indian languages, via AI4Bharat and Sarvam AI.
  - stage: Delivery
    detail: Chatbot interface serving smallholder farmers, extension workers and local authorities.
outputs:
  - Personalised drought advisories, text and voice
  - Crop diversification and water-saving recommendations
  - Livestock preparedness guidance
related_tools:
  - sadms
  - aware
links:
  - label: SukhaRakshak AI
    url: https://dms.iwmi.org/sukharakshak-ai/
    kind: Web application
  - label: "Can we outpace the next drought in India? (IWMI)"
    url: https://www.iwmi.org/blogs/outpacing-the-next-drought-in-india/
    kind: Publication
  - label: "User consultation workshop on SukhaRakshak AI (CGSpace)"
    url: https://cgspace.cgiar.org/items/f55b5ab8-cfd3-4d50-a56f-245eefd90da6
    kind: Publication
---

## About SukhaRakshak AI

SukhaRakshak AI — "drought protector" — is India's first anticipatory, AI-powered
drought advisory system, developed by IWMI with the **Indian Council of
Agricultural Research (ICAR)** and **ICAR-CRIDA**.

It brings together artificial intelligence, satellite Earth observation,
probabilistic weather forecasts and localised agricultural contingency plans, and
delivers the result as a personalised advisory rather than a map for the user to
interpret.

The distinction that matters: it **monitors drought as it emerges and predicts
where conditions are heading**, then converts both into specific, local action.

## Reaching people who bulletins miss

Advisories are delivered as **text and voice in more than 20 Indian languages**,
through integration with **AI4Bharat** and **Sarvam AI**. Voice matters as much
as translation — it makes the system usable by rural users with limited literacy,
who are among those most exposed to drought and least served by conventional
advisory channels.

Users include smallholder farmers, agricultural extension workers and local
authorities. Advice covers anticipatory decisions such as crop diversification,
water-saving practices and livestock preparedness.

## How it is built

The system uses retrieval-augmented generation over agricultural contingency
plans, with a large language model providing the conversational layer. Data
inputs include [SADMS]({{ site.baseurl }}/tools/sadms/), Google Earth Engine and
global forecast systems including NOAA GEFS and CFS.

## Relationship to the S2S programme

SukhaRakshak AI is the last-mile channel for the programme's drought products:
it issues district-level drought triggers over SMS and WhatsApp, reaching users
that the dashboard-based platforms do not.

*Content on this page is drawn from IWMI and ICAR descriptions of the system.
Sources are linked above.*
