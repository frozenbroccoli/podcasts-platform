# Documentation of the APIs

## Search API

### What does it return?

The top `200` paginated results of an itunes
podcasts search, the page size being `20`.

### How to call it?

Make a GET request to the endpoint `{{base_url}}/podcasts/search/?query={{query}}&page={{page}}`.

### Can I get an ordered response?

So far, we have ordering by release date. Ordering can 
be newest to oldest or the reverse. To get the newest release
first, call `{{base_url}}/podcasts/search/?query={{query}}&ordering=newest&page={{page}}`.

For the opposite, call `{{base_url}}/podcasts/search/?query={{query}}&ordering=oldest&page={{page}}`

### Next order of business

1. Sort/filter based on rating.
