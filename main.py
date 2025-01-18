

PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as data:
    name_list=data.readlines()

with open("./Input/Letters/starting_letter.txt") as content:
    letter_content=content.read()
    for name in name_list:
        stripped_name=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as completed_letter:
            completed_letter.write(new_letter)
