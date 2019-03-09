"""
This function takes in the sample spam and non-spam dictionaries and the list of unique words
to output a dictionary of each word's prior probability for the posterior calculation later.
"""


def make_prob_dict(spam_dict, ham_dict, wordList, ngood, nbad):
    dict_prob = {}
    for item in wordList:
        if item in ham_dict.keys():
            g = 2 * ham_dict[item]
        else:
            g = 0
        if item in spam_dict.keys():
            b = spam_dict[item]
        else:
            b = 0
        if g + b > 1:
            prob = max(0.01, min(0.99, min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
        else:
            prob = 0
        dict_prob[item] = prob
    return dict_prob


"""
This function takes in the sample spam and non-spam token lists 
to create the dictionaries of each unique word counts,
and feed it into make_prob_dict function.
"""


def create_filter(spam_corpus, ham_corpus):
    dict_spam_corpus = {}
    dict_ham_corpus = {}
    words = []

    nbad = 0
    for corpus in spam_corpus:
        nbad += 1
        for word in corpus:
            if word not in words:
                words.append(word)
            if word not in dict_spam_corpus.keys():
                dict_spam_corpus[word] = 1
            else:
                dict_spam_corpus[word] += 1

    ngood = 0
    for corpus in ham_corpus:
        ngood += 1
        for word in corpus:
            if word not in words:
                words.append(word)
            if word not in dict_ham_corpus.keys():
                dict_ham_corpus[word] = 1
            else:
                dict_ham_corpus[word] += 1

    return make_prob_dict(dict_spam_corpus, dict_ham_corpus, words, ngood, nbad)


"""
This function takes in the corpus to be tested and the dictionary of prior probabilities, 
to output binary value indicating whether the input corpus is a spam or not.
"""


def to_spam_or_not_to_spam(corpus, filt):
    for word in corpus:
        if word not in filt.keys():
            filt[word] = 0.4
    kernel = 1
    complement_prob = 1
    for word in corpus:
        kernel *= filt[word]
        complement_prob *= 1 - filt[word]
    marginal = kernel + complement_prob
    final = kernel / marginal
    if final > 0.9:
        return True
    else:
        return False


# sample tokens
bad_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
good_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

# the tokens to be tested
sample_corpus = ["I", "am", "spam"]

# create the filter (dictionary of prior probabilities)
hash_filter = create_filter(bad_corpus, good_corpus)

print(hash_filter)

# test the corpus of interest
if to_spam_or_not_to_spam(sample_corpus, hash_filter):
    print("It's a spam.")
else:
    print("It's not a spam.")
