import random


#  запрос
def req_rand_question():
    responses = """
make a list: of interesting and useful Prompts: to Unleash AI's Potential
"""
    lines = responses.strip().split('\n')
    return random.choice(lines)


#  история
def req_rand_history():
    responses = """
Write a narrative on loss and war from the viewpoint of a dog.
Make original and motivational phrases that will inspire others to act and achieve their goals. Original and thought-provoking, these statements ought to compel readers to reflect thoroughly on the strength of their own potential and the opportunities open to them. To deliver your message in a unique and interesting way, think about employing a number of various quotes styles and formats. You should also feel free to try out new words and expressions.
Come up with fresh ideas for coffee mug designs. A brand-new approach to holding hot liquids.
Write a lengthy poem about a group of construction vehicles cooperating to find a solution. It ought to rhyme.
Create a children’s book about an elephant who rides a train for the first time.
Write a story about the first person to build a telescope and the moment she raises her potent creation to the sky and sees the stars for what they truly are.
Do a flash fiction piece on the Battle of Hattin.
Continue the narrative while introducing a villain who is vanquished.
Complete the dialogue between a California family law attorney in the example below.
People may now think of queries and replies in novel and creative ways thanks to new AI text systems. What are some crucial inquiries we may pose to these text-based AIs that would yield original and admirable insights into humanity? Make six specific questions that don’t contain the phrase “AI.”
"""
    lines = responses.strip().split('\n')
    return random.choice(lines)


#  медицина
def req_rand_medicine():
    responses = """
List eight items sold at the grocery store that are generally considered to be inexpensive, surprisingly nutritious, and underrated.
Describe six effective yoga poses or stretches for back and neck pain
Can you suggest some self-care activities for stress relief?
What are some mindfulness exercises for reducing anxiety?
Easy and beginner-friendly fitness routines for a working professional
I need motivation to < achieve a specific task or goal>
What are some ways to cultivate a growth mindset?
I need help staying motivated at work. Can you give me advice on how to stay focused and motivated?
Come up with 10 nutritious meals that can be prepared within half an hour or less.
Create a 30-day exercise program that will assist me in dropping 2 lbs every week.
Offer a detailed explanation of the benefits and risks of alternative medicine practices, such as acupuncture and herbal remedies.
"""
    lines = responses.strip().split('\n')
    return random.choice(lines)


#  комедия
def req_rand_comedy():
    responses = """
Tell me a joke about [topic of your choice]
Send a pun-filled happy birthday message to my friend Alex.
Write a sequel/prequel about the 'X' movie
Create a new playlist of new song names from 'X'
write a script for a movie with 'X' and 'X'
Explain [topic of your choice] in a funny way
Give me an example of a proposal message for a girl
Write a short story where an Eraser is the main character.
How much wood could a woodchuck chuck if a woodchuck could chuck wood?
Make Eminem-style jokes about Max Payne.
You are a text video game where you give me options ( A, B, C, D) as my choices. The scene is Narnia. I start out with 100 health.
Come up with a 14-day itinerary for a trip to Germany. The first suggested attraction should be “Take a tour of the Reichstag Building in Berlin.
Write a formal complaint email to United Airlines about my delayed baggage from my flight on Tuesday, January 17th, from New York to Los Angeles.
Translate the following text into Portuguese: <paste text below>
Write hilarious fan fiction about the Twilight saga.
"""
    lines = responses.strip().split('\n')
    return random.choice(lines)


#  лирика
def req_rand_Lyrics():
    responses = """
Write a poem about love and loss, using metaphors and imagery to evoke emotion
Create a song lyrics about chasing dreams and overcoming obstacles
Generate a short story about a musician who discovers their true passion
Write a script for a music video that tells a story of heartbreak and redemption
Create a sonnet about the beauty of nature, using vivid imagery and rhyme
Generate a monologue for a play about a struggling artist trying to make it in the music industry
Write a song about the power of friendship and support
Create a poem about the fleeting nature of time, using personification and allusion
Generate a short poetry about a band that reunites after years apart
Write a script for a musical about the rise and fall of a legendary musician
Create a song lyrics about the beauty and the pain of falling in love
Generate a monologue for a play about the struggles of being a musician
Write a poem about the beauty of music, using vivid imagery and metaphor
Create a song lyrics about the importance of being true to oneself
Generate a short story about a musician who overcomes personal demons to find success
Write a script for a music video that tells a story of self-discovery and empowerment
Create a sonnet about the beauty of the stars and the night sky, using metaphor and imagery
"""
    lines = responses.strip().split('\n')
    return random.choice(lines)


#  факт факты
def req_rand_facts():
    responses = """
Tell me an interesting fact about space.
What is a surprising fact about animals?
Give me a fascinating historical fact.
Tell me something intriguing about technology.
What is an unusual fact about the human body?
Give me a surprising fact about the natural world.
Tell me a fun fact about a famous person.
What is an interesting fact about the brain?
Give me a unique fact about art or literature.
Tell me something remarkable about ancient civilizations.
What is a little-known fact about the ocean?
Give me an amazing fact about the universe.
Tell me an intriguing fact about the human mind.
What is a surprising fact about the animal kingdom?
Give me an interesting fact about science or discoveries.
Tell me a fascinating fact about a specific country or culture.
What is a unique fact about the human body?
Give me a little-known fact about historical figures.
Tell me a fun fact about inventions or innovations.
What is an unusual fact about the natural world?
What is an interesting fact about ancient civilizations?
Give me a fascinating fact about the human brain.
Tell me something remarkable about famous landmarks.
What is a unique fact about the world of music?
Give me an intriguing fact about the field of medicine.
Tell me an unusual fact about natural disasters.
What is a fun fact about the world of sports?
Give me an amazing fact about the development of technology.
Tell me a little-known fact about the human body.
What is an interesting fact about the history of art?
Give me a surprising fact about the world of insects.
Tell me a fascinating fact about the universe.
What is a unique fact about the world of fashion?
Give me an intriguing fact about historical events.
Tell me an unusual fact about the human senses.
What is a fun fact about the world of literature?
Give me an amazing fact about the animal kingdom.
Tell me a little-known fact about scientific discoveries.
What is an interesting fact about cultural traditions?
"""
    lines = responses.strip().split('\n')
    return random.choice(lines)
