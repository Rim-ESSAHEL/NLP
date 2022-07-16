from bs4 import BeautifulSoup
import re, string, unicodedata
import nltk
import contractions
nltk.download('wordnet')
nltk.download('omw-1.4')
import string





def replace_contractions(text):
    """Replace contractions in string of text"""
    new_text = contractions.fix(text)
    # print("Contractions handled ...")
    return new_text


def remove_URL(text):
    """Remove URLs from text"""
    new_text = re.sub(r"http\S+", "", text)
    # print('Urls removed ...')
    return new_text

def remove_html_tags(text):
    """Remove html tags from text"""
    new_text = BeautifulSoup(text, "html.parser").get_text() 
    # print('Html tags removed ...')
    return new_text

def remove_digits(text):
    new_text = re.sub(r'[0-9]+', '', text)
    # print("Digits removed ...")
    return new_text


def tokenize(text):
    words = nltk.word_tokenize(text)
    # print("Text tokenized ...")
    return words



def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    # print("Non-ASCII characters removed ...")
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    # print("Text lowercased ...")
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    # print("Punctuation removed ...")
    return new_words


def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in nltk.corpus.stopwords.words('english'):
            new_words.append(word)
    # print("Stopwords removed ...")
    return new_words



def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = nltk.stem.PorterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    # print('Stemming')
    return stems

    
def lemmatize_words(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer =  nltk.stem.WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word)
        lemma = lemmatizer.lemmatize(lemma, 'v')
        lemmas.append(lemma)
        
    # print("Lematizing")
    return lemmas


def remove_punctuations_from_string(text):
    new_string = text.translate(str.maketrans('', '', string.punctuation))
    return new_string
