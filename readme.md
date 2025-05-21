# Goodreads API

An API to access data from Goodreads, as Goodreads themselves no longer provide a public API

## API Documentation

### Routes

Route: `/`  
Verb:  `GET`  
Returns:  
```
hello
```  

Route: `/tbr/<int:userid>?page=<page>`  
Verb: `GET`  
Returns:  
```json
{
    'books': [
        'string': 'bookId'
    ],
    'next_link': 'href'
}
```

Route: `/book/<str:bookid>`  
Verb: `GET`  
Returns:  
```json
{	
    'author_link':	string,
    'author_name':	string,
    'book_rating':	string, number from 0-5,
    'rating_count':	string, number >= 0,
    'review_count':	string, number >= 0
    'series_entry':	string | null
    'series_link':	string | null
    'series_name':	string | null
    'title':	    string
}