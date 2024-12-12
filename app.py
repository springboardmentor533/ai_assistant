from groq import Groq


client = Groq(api_key="") #enter your api key here or for better code practices use .env and get the key from env

def exercise_planner(user_input):
    prompt= f"""
        You are helpful Gym Coach and experienced exercise planner
        This is the body part i want to train :{user_input}
        
        You response shoule be max of 6 exercises
        with 10-12 repetition of each exercise
        Just exercise and it's repetitons

        Example
        # body part: Biceps
        # results:
        # Bicep Curls x 10

        
"""

    results = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":prompt,
            }
        ],

        model="llama-3.3-70b-versatile",
        
    )

    print(results.choices[0].message.content)


user_input = input("Enter which body part you want to train ?")
exercise_planner(user_input)

