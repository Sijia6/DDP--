import string
def word_filter_counter(text, filter_words):
    text = text.lower()
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(translator)
    words = text.split()
    
    filter_word_counts = {word: words.count(word) for word in filter_words}
    
    return filter_word_counts

print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  
