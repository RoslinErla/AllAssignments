import string

def open_file():
    filename = input("Enter name of mapping file: ")
    try:
        file_object = open(filename, "r")
        return file_object
    except:
        return None

def read_file(file_object):
    abbrev_dict = dict()
    for line in file_object:
        line= line.strip()
        key,value = line.split(":")
        abbrev_dict[key] = value
    return abbrev_dict

def translate_message(message, a_dict):
    temp_msg = ""
    word_list = message.split()
    last_letter = ""
    
    for word in word_list:

        if word[-1] in string.punctuation:
            last_letter += word[-1]
            word = word[:-1]

        if word in a_dict:
            temp_msg = temp_msg + " " + a_dict[word]
        else:
            temp_msg = temp_msg + " " + word
        
        if last_letter != "":
            temp_msg += last_letter
            last_letter = ""

    return temp_msg[1:]



def main():
    file_object = open_file()
    if file_object:
        abbrev_dict = read_file(file_object)
        message = input("Enter a message: ")
        while message != "q":
            new_message = translate_message(message, abbrev_dict)
            print(new_message)
            message = input("Enter a message: ")
    file_object.close()

main()