class FrequentHead:
    """Frequent Head means, basically the heading of the word. The naming comes from the HTML file that is parsed."""

    def __init__(self, ldoce_element):
        self.hwd = ""
        self.hyphenation = ""
        self.pron_codes = ""
        self.tool_tip = ""
        self.frequency = ""
        self.pos = ""
        self.grammar = ""
        self.british_pronunciation_link = ""
        self.american_pronunciation_link = ""

        try:
            self.hwd = ldoce_element.select_one(".Head .HWD").text
        except AttributeError:
            pass
        try:
            self.hyphenation = ldoce_element.select_one(".Head .HYPHENATION").text.strip()
        except AttributeError:
            pass
        try:
            self.pron_codes = ldoce_element.select_one(".Head .PronCodes").text.strip()
        except AttributeError:
            pass
        try:
            self.tool_tip = ldoce_element.select_one(".Head .tooltip").text.strip()
        except AttributeError:
            pass
        try:
            freq_ls = ldoce_element.select(".Head .FREQ")
            temp = []
            for freq in freq_ls:
                temp.append(freq.text.strip())
            self.frequency = "/".join(temp)
        except AttributeError:
            pass
        try:
            self.pos = ldoce_element.select_one(".Head .POS").text.strip()
        except AttributeError:
            pass
        try:
            self.grammar = ldoce_element.select_one(".Head .GRAM").text.strip()
        except AttributeError:
            pass
        try:
            self.british_pronunciation_link = ldoce_element.select_one(".Head .brefile").get("data-src-mp3")
        except AttributeError:
            pass
        try:
            self.american_pronunciation_link = ldoce_element.select_one(".Head .amefile").get("data-src-mp3")
        except AttributeError:
            pass
