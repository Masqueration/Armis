# Armis
In order to run the tests suite, run Armis.py with the URL and credentials as args.

    python Armis.py URL USERNAME PASSWORD
    
    
<b>Login(object):</b>

<i>Holds Login page's text-field web-elements</i>

Tests:
- Wrong username (Enter invalid username, password -> login fails)
- Wrong password (Enter a valid username, wrong password -> login fails)
- Possitive login (Enter valid username and password -> login passes)


<b>Playlists(object):</b>

<i>Holds a record's list of playlist in which its enlisted</i>

Tests:
- Adding playlist - the record's list of playlists is updated with the new PL
- Adding playlist - assert addition to the user's side-bar playlists list
