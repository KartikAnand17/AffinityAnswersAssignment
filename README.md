AffinityAnswers Assignment
---
**User Tweet - degree of Profanity Calculator**
---

This assignment uses two datasets:
    1. User Tweets Data
    2. Racial Words Data

We follow a very simple approach to solve the problem.

    1. Tweet Preprocessing
        - Tokenized the tweet statement 
        - Removed any stop words from the list of tokens
        - Removed any punctuations present in the list of tokens

    2. Profanity Calculation 
        - Count the number of tokens that were present in the racial words data
        - Find the ratio of total count of racial words present in the list of tokens from the tweet to the total number of tokens present in the tweet:
                *degree of profanity = number of racial tokens / total number of tokens*

---
