# User defined params

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

import os
import requests
IMAGES_LINK:str = "https://platform.virdocs.com/rscontent/epub/id1/id2/OEBPS/images/page-.jpg"
JPEG_DOWNLOAD_DIR:str = "downloads/"

session = requests.Session()
# Set the authentication cookies
session.cookies.update(COOKIES)

def download_image_jpg(image_link:str):
    ret = session.get(image_link)
    if ret.status_code != 200:
        print(f"Failed to download from {image_link}: code {ret.status_code}")
        return None
    image_data = session.get(ret.url)
    return image_data.content
    
def main():
    if not os.path.exists(JPEG_DOWNLOAD_DIR):
        os.mkdir(JPEG_DOWNLOAD_DIR)
    id1:str = str(BOOK_IDS[0])
    id2:str = str(BOOK_IDS[1])
    
    page_start:int = int(PAGE_RANGE[0])
    page_finish:int = int(PAGE_RANGE[1])
    
    images_link = IMAGES_LINK \
                                .replace("id1", id1)\
                                .replace("id2", id2)
    book_page_dir = os.path.join(JPEG_DOWNLOAD_DIR, f"{id1}_{id2}")
    pdf_path = os.path.join(JPEG_DOWNLOAD_DIR,  f"{id1}_{id2}.pdf")
    if not os.path.exists(book_page_dir):
        os.mkdir(book_page_dir)
        
    downloaded_images_list = []
        
    for page_number in range(page_start, page_finish + 1):
        image_link:str = images_link.replace("page-", f"page-{page_number}")
        print(image_link)
        image_data = download_image_jpg(image_link)
        if image_data is None:
            continue
        jpeg_file_path:str = os.path.join(book_page_dir, f"page_{page_number}.jpg")
        with open(jpeg_file_path, "wb") as file_handle:
            file_handle.write(image_data)
        if SAVE_AS_PDF:
            from PIL import Image
            downloaded_images_list.append(Image.open(jpeg_file_path))
    
    if SAVE_AS_PDF:
        downloaded_images_list[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=downloaded_images_list[1:])
    
if __name__ == "__main__":
    main()