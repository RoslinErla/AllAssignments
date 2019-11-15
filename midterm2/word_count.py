# Skrifið Python forrit sem biður notandann að slá inn nafn skrár
#  sem inniheldur runu orða (eina setningu) í hverri línu.  
# Forritið prentar út fjölda orða í inntaksskránni.  
# Ef komma, punktur, upphrópunarmerki eða spurningamerki (, . ! ?) 
# standa næst við orð þá teljast þessi greinarmerki sérstök orð. 
#  Gera má ráð fyrir að þetta séu einu greinarmerkin og ef þau koma fyrir í skrá þá standa þau 
# alltaf næst við orð (ekkert bil á undan greinarmerkjum).
# Dæmi: Þessi runa 
# university,
# er þá tvö orð ("university" og ",")
# Ef inntaksskrá finnst ekki þá skal forritið skrifa út viðeigandi villuskilaboð (sjá í dæmi fyrir neðan). 
# Í útfærslunni ykkar megið þið ekki nota neina import setningu.

def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        print("Filename {} not found!".format(filename))

def read_file_and_count_words(filename):
    punctuation = [",", ".", "!", "?"]
    word_counter = 0
    for word in filename:	# process each line/word
        word = word.strip() # strip leading and trailing white space
        word = word.split(" ")
        for elements in word:
            word_counter += 1
            if elements[-1] in punctuation:
                word_counter += 1
    print(word_counter)


def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    if file_object:
        read_file_and_count_words(file_object)
        file_object.close()


main()