

def read_file_content(filename):
    content = ''
    
    with open(filename, 'r') as file:
        content = file.read()

    
    return content


def count_words():
    text = read_file_content("./story.txt")
    words = text.lower().split(' ')
    print(words)

    result_dict = {}

    for i in range(len(words)):
        if not words[i]:
            continue
        word = words[i].strip('\n?,.')
        
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1

    return result_dict

print(count_words())
