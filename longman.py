from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
from definition import Definition

ua = UserAgent()  # This creates a fake user agent.
headers = {
    "User-Agent": str(ua.chrome)
}

while True:
    word = input("\nEnter a word: ").strip()
    url = f"https://www.ldoceonline.com/dictionary/{word}"
    response_source_code = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(response_source_code, "html.parser")
    df = Definition(soup)

    player_flag = True
    try:
        num = int(input("Type a number : "))
    except ValueError:
        print("You should type a number for example pronunciations, which is grater than 0.")
        try:
            num = int(input("Type a number : "))
        except ValueError:
            print("You should have enter a number. Now you broke the program. Don't do that again.")
            break

    while player_flag:
        df.get_examples_with_link(number=num)
        try:
            num = int(input("Type a number or -1 for replay main pronunciation, 0 for quit or something else for replaying examples: "))
        except ValueError:
            pass

        if num == 0:
            player_flag = False
        if num == -1:
            df.driver.get(df.main_pronunciation_link)

    df.driver.quit()
