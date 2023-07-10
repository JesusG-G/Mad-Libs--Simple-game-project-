import random


def get_input(word_type: str):
    user_input: str = input(f"Enter {word_type}: ")
    return user_input

def story_result():
    
    story_selected = random.randint(0,2)
    match story_selected:
        case 0:
            things_1 = get_input("things (plural)")
            person = get_input("a person")
            adjective = get_input("an adjective")
            place = get_input("a place")
            food = get_input("a food")
            things_2 = get_input("things (plural)")
            feeling = get_input("a feeling")
            celebrity_name = get_input("a celibrity")
            song_title = get_input("a song name")
            verb = get_input("a verb")
            story = f"""
            I just got back from a pizza party with {person}. 
            Can you believe we got to eat {adjective} pizza in {place}?! 
            Everyone got to choose their own toppings. 
            I made ‘{food} and {things_1}’ pizza, which is my favorite! 
            They even stuffed the crust with {things_2}. 
            How {feeling}! If that wasn’t good enough already, {celebrity_name} was there singing {song_title}. 
            I was so inspired by the music, I had to get up out of my seat and {verb}.
                """
        case 1:
            occupation_job = get_input("a occupation (job)")
            noun_4 = get_input("a noun")
            verb_2 = get_input("a verb")
            adjective_2 = get_input("an adjective")
            verb_1 = get_input("a verb")
            noun_1 = get_input("a noun")
            adjective_1 = get_input("an adjective")
            noun_3 = get_input("a noun")
            verb_3 = get_input("a verb")
            noun_2 = get_input("a noun")
            story = f"""
            Today a {occupation_job} named {noun_4} came to our school to talk to us about her job. 
            She said the most important skill you need to know to do her job is to be able to {verb_2} around (a) {adjective_1} {noun_3}. 
            She said it was easy for her to learn her job because she loved to {verb_1} when she was my age-and that helps a lot! 
            If you’re considering her profession, I hope you can be near (a) {adjective_2} {noun_1}. 
            That’s very important! If you get too distracted in that situation you won’t be able to {verb_3} next to (a) {noun_2}!    
            """
        case 2:
            food = get_input("a food")
            person = get_input("a person")
            place = get_input("a place")
            animal = get_input("an animal")
            profession = get_input("a profession")
            things_2 = get_input("things (plural)")
            feeling = get_input("a feeling")
            clothing = get_input("a piece of clothing")
            verb = get_input('a verb (ending in "ing")')
            things_2 = get_input("things (plural)")
            story = f"""
            Say ‘{food}’, the photographer said as the camera flashed! {person} and I had gone to {place} to get our photos taken today. 
            The first photo we really wanted was a picture of us dressed as {animal} pretending to be a {profession}. 
            When we saw the proofs of it, I was a bit {feeling} because it looked different than in my head. (I hadn’t imagined so many {things_1} behind us). 
            However, the second photo was exactly what I wanted. 
            We both looked like {things_2} wearing {clothing} and {verb}-exactly what I had in mind!
            """

    return story

if __name__ == "__main__":
    print("""
        Mad Libs is a word game where one player prompts another for a list of words to substitute for blanks in a story; these word substitutions have a humorous effect when the resulting story is then read aloud. 
        The game is especially popular with American children and is frequently played as a party game or as a pastime.
        """)
    result = story_result()
    print(result)