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

Route: `/tbr/<userid>?page=<page>`  
Verb: `GET`  
Returns:  
```json
{
    books: [
        string: bookId
    ],
    next_link: href
}
```