CHANGED_TEXT = "[name]"

with open(file="invited_names.txt ") as name:
    name_list = name.readlines()


with open(file="starting_letter.txt ") as letter:
    letter_text = letter.read()

for each_name in name_list:
    each_name_file = each_name.strip()
    new_letter = letter_text.replace(CHANGED_TEXT, each_name_file)
    with open(file=f"letter_for_{each_name_file}.txt", mode="w") as output_letter:
        output_letter.write(new_letter)


