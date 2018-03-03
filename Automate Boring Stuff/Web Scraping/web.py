# import webbrowser
#                                                       Simple browser open
# webbrowser.open("https://www.github.com/Kronostheus")
import requests


def req():
    # returns a Request object with the return value of the URL
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

    # raises stored HTTPError if there is one. If failed download shouldn't stop program
    #   raise_for_status() should be in a try/except statement
    res.raise_for_status()

    try:
        # wb means to write in binary mode so we can keep the Unicode encoding of the text
        playFile = open('Romeo_and_Juliet.txt', 'wb')

        # we can receive data in "chuncks". We can specify how large each chunk is (this case 100000 bytes)
        for chunck in res.iter_content(100000):
            playFile.write(chunck)

        playFile.close()
    except:
        raise Exception("Error while processing data")

# For now I'm going to skip the rest of the chapter. I might come back later
