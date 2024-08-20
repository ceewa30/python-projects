#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/Users/sivakumars/Documents/PythonProject/Mail_Merge_Project/Input/Names/invited_names.txt") as name:
    names = name.readlines()
    print(names)

with open("/Users/sivakumars/Documents/PythonProject/Mail_Merge_Project/Input/Letters/starting_letter.txt", 'r') as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace('[name]', stripped_name)
        with open(f"/Users/sivakumars/Documents/PythonProject/Mail_Merge_Project/Output/ReadyToSend/letter_for_{name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)