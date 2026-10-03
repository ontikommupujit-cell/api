import requests
def get_random_joke():
    """Fetch a random joke from the Official Joke API"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        print(f'FULL JSON RESPONSE: {response.json()}')
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to fetch a joke."
def main():
        print("Welcome to the Joke Fetcher!")
        while True:
            user_input = input("Press Enter to get a joke or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            joke = get_random_joke()
            print(joke)
if __name__ == "__main__":
    main()