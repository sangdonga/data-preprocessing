import os
import io
from googleapiclient.http import MediaIoBaseDownload

import auth

ID_FOLDER = '0Byg9v6xOCZYBflJ5UXcydFVLclN2ZUk4NmQwQ1UwQnlRWldEdVVjeDFCRGxvUEhkcjVBQUE'

service = auth.main()


def get_file_in_folder(folderid):
    results = service.files().list(
        pageSize=1000,
        q="\'" + folderid + "\'" + " in parents",
        fields="nextPageToken, files(id, name, mimeType)").execute()
    return results.get('files', [])


def downloaders(fid, fname):
    request = service.files().get_media(fileId=fid)
    # fh = io.BytesIO()
    fh = io.FileIO("data/"+fname, mode='w')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    if done:
        with open('crawled/id.txt', mode='a', encoding='utf8') as f:
            f.write(fid + '\n')
            f.close()


def downloaded(fid):
    with open('crawled/id.txt', mode='r', encoding='utf8') as f:
        for line in f:
            if fid == line.rstrip():
                return True
        f.close()
    return False


if __name__ == '__main__':
    files = get_file_in_folder(ID_FOLDER)
    for file in files:
        if not downloaded(file['id']):
            downloaders(file['id'], file['name'])
        else:
            print("File:" + file['name'] + " downloaded")
