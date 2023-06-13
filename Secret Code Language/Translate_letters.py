dictionary = {
    "01": "a",
    "02": "b",
    "03": "c",
    "04": "d",
    "05": "e",
    "06": "f",
    "07": "g",
    "08": "h",
    "09": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "16": "p",
    "17": "q",
    "18": "r",
    "19": "s",
    "20": "t",
    "21": "u",
    "22": "v",
    "23": "w",
    "24": "x",
    "25": "y",
    "26": "z",
    "00": " "
}

def convert(text: str):
    for key, value in dictionary.items():
        if value == text:
            return key
    return ""  # Return an empty string if the text is not found in the dictionary

while True:
    txt = input("Write the text to convert: ")
    txt=txt.lower()
    converted_txt = ""
    for letter in txt:
        converted_letter = convert(letter)
        converted_txt += converted_letter
    print(converted_txt)
