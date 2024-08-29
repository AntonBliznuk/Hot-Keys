import webbrowser
from app.support import search_in_string

def open_my_url(url):
    """
    Opens the specified URL using Google Chrome if the URL contains 'rezka.ag'.
    Otherwise, it opens the URL using the default web browser.

    Arguments:
    url -- the URL to be opened
    """

    # Check if the URL contains the substring 'rezka.ag'
    if search_in_string(str(url), 'rezka.ag'):
        # Define the path to the Google Chrome application
        chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        # Register Google Chrome as a web browser option
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        # Open the URL using Google Chrome
        webbrowser.get('chrome').open(url)

    else:
        # Open the URL using the default web browser
        webbrowser.open(url)

    # Print a confirmation message
    print(f"Successfully opened the link ---> {url}")
    return

# Execute the function if this script is run as the main program
if __name__ == "__main__":
    # Open a specific URL
    open_my_url('https://rezka.ag/ua/series/thriller/47-sherlok-2010.html#t:56-s:1-e:2')
