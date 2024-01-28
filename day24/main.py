with open('./input/names/invited_names.txt') as namelist:
    names = namelist.read().split()

with open('./input/letters/starting_letter.txt') as letter:
    content = letter.read()
    for name in names:
        new_letter = content.replace('[name]', name)
        with open(f'./output/readytosend/letter_for_{name}.txt','w') as customletter:
            customletter.write(new_letter)
