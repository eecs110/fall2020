---
layout: two-column
title: Working with Yelp & Spotify Data
description:
  - Practicing working with dictionaries
  - Practice reading / writing from files
  - Practice querying a REST API
type: lecture
draft: 1
num: 25
due_date: 2020-11-16
---

## Background
In this week's lab, you will be getting a preview of [Project 2](../assignments/p2). This includes:

1. Installing some python dependencies using PIP
2. Updating your `apis/authentication.py` file so that it uses the course API master token
3. Practicing using some of the modules that have been provided for you inside of the apis directory

Please complete the following steps:

## Step 1: Setup
Complete Steps A, B, C, and D in the "Setup" section of [Project 2](../assignments/p2#setup-please-read-carefully). If you have set everything up correctly, running the `tests/run_verification.py` python file will display the following output:

```bash
test_token (test_authentication.TestAuthentication) ... ok
test_get_key (test_authentication.TestAuthentication) ... ok
test_malformed_query_yields_errors (test_authentication.TestAuthentication) ... ok
test__issue_get_request_only_one (test_spotify.TestSpotify) ... 
ok
test_execute_business_queries_just_one_simplified (test_yelp.TestYelp) ... 
ok
test_can_import_sendgrid (test_sendgrid.TestSendgrid) ... ok
test_can_import_sendgrid_api_module (test_sendgrid.TestSendgrid) ... ok

----------------------------------------------------------------------
Ran 7 tests in 5.935s

OK
```

## Step 2
When you're done, complete one of the two options listed below:

### Yelp Option
Create a brand new file called `lab06.py` directly inside of your `project02` folder (the location matters). Your directory structure should look like this:

```bash
├── apis
├── music_finder.py
├── restaurant_finder.py
├── tests
└── lab06.py
```

Next, paste the following code into your `lab06.py` file and run it.

```python
from apis import yelp

businesses = yelp.get_businesses()
print(businesses)
```

You should see some Evanston restaurants print to the screen (as a list of dictionaries).

#### Practice Outputting Dictionary Values
1. Output just the `name` of each business to the screen
2. Output the `name`, `rating`, and `review_count` to the screen

**TIP:** You can use the string's build-in `format` function to create nice columns:

```python
template = '{name:<30}{rating:>10}{review_count:>20}'

print('-' * 60)
print(template.format(name='NAME', rating='RATING', review_count='REVIEW COUNT'))
print('-' * 60)
print(template.format(name='Giordannos Pizza', rating=3.5, review_count=280))
print(template.format(name='Lou Malnati\'s Pizza', rating=3.7, review_count=190))
print('-' * 60)
```
The greater than / less than signs refer to whether the output is left or right justified, and the number refers to the column width.

There is also a helper function inside of the `apis.yelp` module that can help you output businesses to the screen using a "Data Frame" which you are welcome to modify: 

```python
yelp.print_formatted_businesses_table(businesses)
```

#### Practice Querying
When you're done outputting the data, open the `apis/yelp.py` and navigate down to the `get_businesses` function definition. Note all of the keyword  (optional) parameters that the function accepts. 

Next, go back to your `lab06.py` file and modify the get_businesses(...) function call by:
1. Use the various keyword arguments (`price`, `category`, and/or `location`) to change which results get displayed.
2. Use the `sort_by` keyword argument to change the sort order.

{:.blockquote-no-margin}
> **NOTE:** You can also learn more about the yelp module by typing: **`help(apis.yelp)`**

### Spotify Option
Create a brand new file called `lab06.py` directly inside of your `project02` folder (the location matters). Your directory structure should look like this:

```bash
├── apis
├── music_finder.py
├── restaurant_finder.py
├── tests
└── lab06.py
```

Next, paste the following code into your `lab06.py` file and run it.

```python
from apis import spotify
artists = spotify.get_artists('Beyonce')
print(artists)
```

You should see some search results relating to Beyonce print to the screen (as a list of dictionaries).

#### Practice Outputting Dictionary Values
1. Output just the `name` of each artist to
2. Output the `name`, `genres`, and `share_url` to the screen

**TIP:** You can use the string's build-in `format` function to create nice columns:

```python
template = '{name:<30}{id:<25}{genres:<35}'

print('-' * 90)
print(template.format(name='NAME', id='ID', genres='GENRES'))
print('-' * 90)
print(template.format(name='Beyoncé', id='6vWDO969PvNqNYHIOW5v0m', genres='dance pop, pop, r&b'))
print(template.format(name='Beyonce as Shine', id='3mjguRNN96bC8zvaTwHoqE', genres=''))
print('-' * 90)
```

The greater than / less than signs refer to whether the output is left or right justified, and the number refers to the column width. The code above outputs like this:

```bash
------------------------------------------------------------------------------------------
NAME                          ID                       GENRES                             
------------------------------------------------------------------------------------------
Beyoncé                       6vWDO969PvNqNYHIOW5v0m   dance pop, pop, r&b                
Beyonce as Shine              3mjguRNN96bC8zvaTwHoqE                                      
------------------------------------------------------------------------------------------
```


#### Practice Querying
When you're done outputting the data, open the `apis/spotify.py` file and navigate down to the `get_similar_tracks` function definition. Note all of the keyword  (optional) parameters that the function accepts. 

While each parameter is technically optional, this function needs some seed data in order to give you song recommendations. Up to 5 seed values may be provided in any combination of seed_artists, seed_tracks and seed_genres. In other words: <br>`len(artist_ids) + len(track_ids) + len(genres)` must be between 1 and 5.

Next, go back to your `lab06.py` file and try invoking the `spotify.get_similar_tracks` function as follows:

```python
track_recommendations = spotify.get_similar_tracks(artist_ids=['6vWDO969PvNqNYHIOW5v0m'])
print(track_recommendations)
```
* Try passing in different Artist IDs
* Try passing in a list of genres (see the `apis.spotify.get_genres_abridged` function to get some valid genre categories).

There is also a helper function inside of the `apis.spotify` module that can help you output the tracks to the screen using a "Data Frame" which you are welcome to modify: 

```python
spotify.print_formatted_tracklist_table(track_recommendations)
```

If you still have time, please experiment with some of the other built-in functions: 
* get_tracks
* get_top_tracks_by_artist
* get_related_artists
* get_playlists


## What to Turn In
When you're done, turn in your `lab06.py` file on Canvas (optional if you attended lab).
