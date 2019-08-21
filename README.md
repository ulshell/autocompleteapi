# FullThrottle Labs Assignment

## Task completed

Implemented all the constraint and the results are not limited to just 25 but  
containing all  the matches in word_search.tsv file. Firstly ranked with exact
match and then based on their usage count and then at last smaller words are
ranked higher then longer words. Then results also incorporate match found
anywhere in string.

## Implemented add on feature
The input typed in input box interacts directly with api and shows results
dynamically.

## Usage

The application is hosted on  Heroku.
[http://autocompleteapi.herokuapp.com/](http://autocompleteapi.herokuapp.com/)

Type in input to see the result of matched text.

## JSON

http://autocompleteapi.herokuapp.com/search?word="word_to_be_searched"
