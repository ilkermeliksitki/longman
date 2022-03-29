from selenium import webdriver
import time
from frequent_head import FrequentHead

driver_path = r"C:\Users\ASUS\Documents\Programming\Python\Personal\WebDrivers\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
# https://stackoverflow.com/questions/47392423/python-selenium-devtools-listening-on-ws-127-0-0-1


class Definition:
    """Responsible for printing the definition and the examples of the searched word."""

    def __init__(self, soup):
        self.driver = webdriver.Chrome(driver_path, options=options)
        self.links = {}
        self.pronunciation_flag = True
        self.main_pronunciation_link = ""

        ldoce = soup.select(".ldoceEntry")
        """ldoceEntries are the main part for each definition for the word."""
        count = 1
        for ldoce_element in ldoce:
            fh = FrequentHead(ldoce_element)
            senses = ldoce_element.select(".Sense")
            for sense in senses:
                def_ = sense.select_one(".DEF")
                sign_post = sense.select_one(".SIGNPOST")
                try:
                    sign_post = sign_post.text + " - "
                except AttributeError:
                    sign_post = ""
                try:
                    def_ = def_.text
                except AttributeError:
                    pass
                if f"{sign_post}{def_}" != "None":
                    frequent_head_ls = [fh.hwd, fh.pos, fh.frequency, fh.pron_codes, fh.grammar, fh.tool_tip]
                    temp = [i for i in frequent_head_ls if len(i) > 0]
                    frequent_head_part = " ".join(temp)

                    print(
                        f"{count}: {frequent_head_part}\n"
                        f"{sign_post.lstrip()}{def_.strip()}"
                    )

                    if self.pronunciation_flag:
                        """This part is dealing with the first appeared audio."""
                        try:
                            self.driver.get(fh.british_pronunciation_link)
                        except:
                            print("\nThe main pronunciation audio file is not found.\n")

                        """This is created in order to replay the main pronunciation of the word."""
                        self.main_pronunciation_link = fh.british_pronunciation_link
                        self.pronunciation_flag = False

                    examples = sense.select(".EXAMPLE")

                    temp_ls = []
                    for example in examples:
                        print(f"\t{example.text.strip()}")
                        """Some audio files does not appear. That's why there is try-except."""
                        try:
                        	exafile = example.select_one(".exafile").get("data-src-mp3")
                        except AttributeError:
                        	continue
                        temp_ls.append(exafile)
                    self.links[count] = temp_ls

                    print("#---------------------------------------------------------------------#")
                    count += 1

    def get_examples_with_link(self, number):
        try:
            if len(self.links[number]) > 0:
                for link in self.links[number]:
                    self.driver.get(link)
                    time.sleep(4)
            else:
                print("There is no file to play.")
        except KeyError:
            if number > 0:
                print("A problem occurred while playing example sounds.")
