import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from string import punctuation

# Preprocessing and Tokenization
def tokenizer(data) -> list:
    """
    Preprocessing the Tweets

    Use predefined stopwords from nltk package
    Use predefined punctuation from string package
    Tokenize the tweet -> remove all stopwords -> remove all punctuation
    
    Args:
        data (csv file): tweets data file 

    Returns:
        list: list of lists containing tokenized tweets

    """
    words = []
    stop_words = set(stopwords.words('english')) 
    punctuation_marks = set(punctuation)
    file = open(data,'r')
    for sentence in file.readlines():
        word_list = word_tokenize(sentence)
        word_list = [word for word in word_list if word not in stop_words and word not in punctuation_marks]
        words.append(word_list)
    return words

def profanity_calculator(words:list) -> int:
    """

    Calculates degree of profanity given a set of racial words and a tweet

    Args:
        words (list): list of words from a single tweet

    Returns:
        int: degree of profanity
    """

    #count the number of racial words present in the list of words
    profanity_sum = sum(1 for word in words if word in racial_words)
    #calculate degree of profanity as the ratio of racial words present to the total number of words present 
    degree = profanity_sum / len(words)
    return degree

def main():
    global racial_words
    racial_words = [] #to store the list of racial words

    #insert path to racial words text file here 
    racial_words_file_path = '/Users/kartik/Desktop/racist_data.txt'
    
    with open(racial_words_file_path,'r' ) as racial_words_file:
        contents = racial_words_file.read()
        racial_words = contents.split(',') 
        racial_words = [ word.strip() for word in racial_words ] #removing any trailing white spaces from each word 

    #insert the path to tweets dataset here
    tweet_file_path = '/Users/kartik/Desktop/data.txt'

    #preprocess the tweets data file
    tokenized_file = tokenizer(tweet_file_path)
    
    df = pd.DataFrame()
    df['tokenized_tweet'] = pd.Series(tokenized_file)

    #calculating profanity for each tokenized tweet in the dataset 
    df['degree'] = [profanity_calculator(row) for row in df['tokenized_tweet']]

    #insert the output file path as the parameter
    output_file_path = '/Users/kartik/Desktop/output.csv'

    #save the resultant dataFrame as a csv
    df.to_csv(output_file_path)


if __name__ == '__main__':
        main()



  