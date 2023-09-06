# Readshelf PDF Zipper

## Requirements

Python
Pillow(for PDF zipping)
`pip install Pillow`
requests(for downloading)
`pip install requests`

## Usage

1. Purchase, or rent the book on redshelf
2. Open the book on a browser of your choice online(chrome is being used in the example)
3. Toggle inspection mode on your browser.
4. On "Elements" tab of the inspector, search ".jpg". You should find something similar to 
```<img src="../images/page-69.jpg" alt="Image for page with label 69" />```
5. Right-click on `../images/page-69.jpg`, select "copy link address"
6. You should obtain an address similar to `https://platform.virdocs.com/rscontent/epub/2409870/2573894/OEBPS/images/page-69.jpg`. Here, `2409870` and `2573894` are the book ids that we will use in the script. Copy them and set the `BOOK_IDS` of the script, correspondingly.
7. Switch to "Applications" tab of the inspector. Select "Cookies" under the "Storage" divider. Then select `https://platform.virdocs.com/` under "Cookies".
8. For all cookies shown on the right hand side of the inspection, copy the name and value into the `COOKIES` section of the script.
9. The top of the script should look like the following:
```python
# whether to save the downloaded .jpegs as a pdf
SAVE_AS_PDF:bool = True
# 2 ids of the book, found through element inspection 
BOOK_IDS = [2409870, 2573894]
# page range of the book you wish to download
PAGE_RANGE = [1, 10]
# cookies for session-based .jpeg access authentication
COOKIES = {
    'AMP_MKTG_d698e26b82':'waefawefawef',
    'csrftoken':'32tgeaedafsdf',
    'csrftoken':'aewfawef',
    'sessionid':'11111',
}
```

10. Run the script, and profit.