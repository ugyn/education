def spin_words(sentence):
    input = sentence.split()
    output = ''
    for word in input:
        if len(word) >= 5:
            output += word[::-1] + ' '
        else:
            output += word + ' '
        
    return output[:-1]