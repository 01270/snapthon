# snapthon
This package can make simple snapchat task

## What it can do
- Stories Downloader
- Get User Info

![alt text](https://i.ibb.co/tzF9yHH/image.png)

## Help

install requirements
```
pip install snapthon
```

Download Stories Example
```
from snapthon import Snapchat

snap = Snapchat("aboflah_1")
print(len(snap.stories())
snap.stories_downloader() # Saving videos and photos
# snap.stories_downloader(count=3) # Only save first 3 Stories
# snap.stories_downloader(count=3, folder='aboflah_1') # You can edit the path saving folder
```

Get User Info Example
```
from snapthon import Snapchat

snap = Snapchat("aboflah_1")
print(f'''
    Data the snapchat account:
    Title: {snap.title()}
    Bio: {snap.bio()}
    Address: {snap.address()}
    Website Url: {snap.websiteUrl()}
    Stories: {len(snap.stories())}
    _____
    has Curated Highlights {snap.hasCuratedHighlights()}
    has Spotlight Highlights: {snap.hasSpotlightHighlights()}
    ____
    Snap Code: {snap.snapcodeImageUrl()}
    Photo: {snap.profilePictureUrl()}
''')
```

Others
```
from snapthon import Snapchat

snap = Snapchat("aboflah_1")
print(snap.user_info['username']) # Get all user info as a dict
print(snap.stories()) # Get the stories full data dict ( photo - video - timestap )
```



