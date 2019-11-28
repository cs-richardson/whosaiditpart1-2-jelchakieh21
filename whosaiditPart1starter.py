# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase

def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
#shake_dict and aust_dict is defining the dictionaries and starting them out
#as empty dictionaries.

shake_dict = {}
aust_dict = {}

def get_counts(filename, result_dict):

    count = 0
    
    file_obj = open(filename, "r")

    for line in file_obj:
        line_lst = line.split(" ")
        for word in line_lst:
            lowerWord = word.lower()
            normalWord = normalize(lowerWord)
            if normalWord in result_dict:
                result_dict[normalWord] += 1
                count = count + 1
            else:
                result_dict[normalWord] = 1
                count = count + 1

        result_dict["_total"] = count
    return result_dict

# Get the counts for the two shortened versions
# of the texts

shakespeare_counts = get_counts("hamlet.txt", shake_dict)
austen_counts = get_counts("pride-and-prejudice.txt", aust_dict)

# Check the contents of the dictionaries and print them with
#their corresponding counts.

for keys,values in shake_dict.items():
    print(keys, ":", values)

for keys,values in aust_dict.items():
    print(keys, ":", values)


