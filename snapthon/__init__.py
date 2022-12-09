import requests
from re import search
from json import loads
from imghdr import what
from os import rename

headers = {
    'authority': 'www.snapchat.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.youtube.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'viewport-width': '927',
}

class Snapchat:
    def __init__(self, username) -> None:
        self.username = username
        self.data = dict()
        self.get_json()
        
    def get_json(self) -> dict:
        response = requests.get('https://www.snapchat.com/add/' + self.username, headers=headers)
        if not response.ok: raise ValueError("Snapchat account not found 404")
        javascript = search('<script.+\"application/json\">((\n|.)+)</script>', response.text)
        self.data = loads(javascript.group(1)) if javascript else None

    @property
    def user_info(self) -> dict: return self.data['props']['pageProps']['userProfile']['publicProfileInfo']
    @property
    def highlights(self) -> dict: return self.data['props']['pageProps']['curatedHighlights']
        
    def address(self): return self.user_info['address']
    def hasSpotlightHighlights(self): return self.user_info['hasSpotlightHighlights']
    def hasCuratedHighlights(self): return self.user_info['hasCuratedHighlights']
    def snapcodeImageUrl(self): return self.user_info['snapcodeImageUrl']
    def profilePictureUrl(self): return self.user_info['profilePictureUrl']
    def websiteUrl(self): return self.user_info['websiteUrl']
    def bio(self): return self.user_info['bio']
    def title(self): return self.user_info['title']
    def stories(self) -> list:
        result = []
        for i in self.highlights:
            for j in i['snapList']:
                result.append({'time': j['timestampInSec'], 
                                'photo': j['snapUrls']['mediaPreviewUrl'], 
                                'video': j['snapUrls']['mediaUrl']})
        return result
    
    def stories_downloader(self, count=None, folder=None) -> None:
        for e, i in enumerate(self.stories(), 1):
            if e == (count+1 if count else count): break
            folder = str(str(folder) + r'/' if folder else '')
            with open((folder + fr'{e}.snap').strip(), 'wb') as save: 
                save.write(requests.get(i['video'], params={'uc': '12'}, headers=headers).content)
            rename((folder + fr'{e}.snap').strip(), (folder + fr'{e}.').strip() +
                ('mp4' if not what((folder+fr'{e}.snap').strip()) else str(what(folder+fr'{e}.snap').strip())))