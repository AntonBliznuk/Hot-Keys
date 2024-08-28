import webbrowser
from app.support import search_in_string


def open_my_url(url):

    if search_in_string(str(url), 'rezka.ag'):
        chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)

    else:
        webbrowser.open(url)

    print(f"Successfully opened the link ---> {url}")
    return



if __name__ == "__main__":
    open_my_url('https://rezka.ag/ua/series/thriller/47-sherlok-2010.html#t:56-s:1-e:2')