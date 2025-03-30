# import pandas

# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#
#
# def generate_phonetic():
#     word = input("Enter the word").strip().upper()
#     try:
#         phonetic_code = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, letters only no number is allowed.")
#         generate_phonetic()
#     else:
#         print(phonetic_code)
#
#
# generate_phonetic()

# import json
# import os
#
# website = "google.com"
# email = "yadavrajesh5612@gmail.com"
# password = "1234567890"
#
# json_obj = {"website": website, "email": email, "password":password}
# json_path = "data.json"
#
# if os.path.exists(json_path) and os.path.getsize(json_path):
#     with open(json_path, "r") as f:
#         try:
#             data = json.load(f)
#         except json.decoder.JSONDecodeError:
#             data = []
# else:
#     data = []
#
# data.append(json_obj)
# with open(json_path, "w") as f:
#     json.dump(data, f, indent=4)
