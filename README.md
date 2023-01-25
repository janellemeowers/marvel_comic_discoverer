# marvel_comic_discoverer

A Python and Flask app that uses the Marvel Developer API to find a random comic the user can read based on a character.

As a Marvel fan, I was excited to discover their own API, and make this fun web app that will hopefully inspire comic reading, or at least display some cool art!

Tools: Python, Flask, hashlib, os

Challenges & what I learned:

- When there is more than one way to do something, or make an API call, which way is the right way? Sometimes the fastest way may work initially, but isn't going to work for later in your proejct or give you ALL the right information. 
I had to experiment with character IDs, comic IDs, to find the right results so I could display the title/description, URL and image/path.
- Marvel requires the API key and timestamp to be hashed with hashm5, which I wasn't familiar with. Starting with Stack Overflow and hashlib docs, it took a few iterations to get it right.

-Other challenges: Sometimes the first character in the search result is not the full listing for their character, rather a nickname or variant, so I had to find the result with more comics available.
-Also had to experiment with Flash messages for the error message.
-API keys are hidden with dotenv.

-Unfortunately Marvel does not allow calls from domains outside Marvel, so I cannot upload this to a site like Render.

*Must sign up for API keys on Marvel Site to use:
<a href="https://developer.marvel.com/docs">Documentation</>


<img width="1264" alt="Screenshot 2023-01-24 at 10 48 00 PM" src="https://user-images.githubusercontent.com/51424392/214501955-cfaa06fc-d0b6-4ca0-981c-4c1a27fba84b.png">

<img width="1310" alt="Screenshot 2023-01-24 at 11 43 36 PM" src="https://user-images.githubusercontent.com/51424392/214507568-917ba8b1-ce00-4245-ba98-3aa157ef8430.png">
