# Armis
In order to run the tests suite, run Armis.py with the URL and credentials as args.

    python Armis.py URL USERNAME PASSWORD
    
Specifically

    python Armis.py 'https://www.orfium.com/' 'Homework' 'Armis1234'
    
    
<b>Login(object):</b>

<i>Holds Login page's text-field web-elements</i>

Tests:
- Wrong username (Enter invalid username, password -> login fails)
- Wrong password (Enter a valid username, wrong password -> login fails)
- Possitive login (Enter valid username and password -> login passes)


<b>Playlists(object):</b>

<i>Holds a record's list of playlists in which its enlisted</i>

<u>Tests:</u>
- Adding playlist - the record's list of playlists is updated with the new PL
- Adding playlist - assert addition to the user's side-bar playlists list
