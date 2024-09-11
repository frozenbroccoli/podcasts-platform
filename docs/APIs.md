# Documentation of the APIs

## Search API

### What does it return?

The top `200` paginated results of an itunes
podcasts search, the page size being `20`.

### How to call it?

Make a GET request to the endpoint `{{base_url}}/podcasts/search/?query={{query}}&page={{page}}`.

### Can I get an ordered response?

The query parameter key for ordering is `ordering`.
Currently supported values are `newest`, `oldest`, `mostTracks`, `leastTracks`. 
Search results are ordered by popularity by default.

### Can I search on only the title or the author?

Searching for various attributes are currently
supported. The query parameter key for that is
`attr`. The possible values are `titleTerm`, `languageTerm`, `authorTerm`, `genreIndex`,
        `artistTerm`, `ratingIndex`, `keywordsTerm`, and `descriptionTerm`.
