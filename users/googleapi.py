from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

import filetype
from django.conf import settings

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_496032033985-mm80t6kdnvc2acrq9t40v6ah398okmr4.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=62741)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

def listFiles():
    creds = obtainCreds()
    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

class DriveApi(object):
    def uploadFile(self, folder_id, upload_path, link_type, title):
        directory = os.path.join(settings.BASE_DIR, 'users')
        os.chdir(directory)
        creds = obtainCreds()
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
        'name':title,
        #'mimeType': obtainMimeType()
        'parents':[folder_id]
        }

        media = MediaFileUpload(upload_path,
                            obtainMimeType(upload_path),
                            resumable=True)
        file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields=f'{link_type}, id').execute()
        user_permission = {
        'type': 'anyone',
        'role': 'reader',
        }

        service.permissions().create( fileId=file.get('id'),
                                        body=user_permission
                                                        ).execute()
        #print 'File ID: %s' % file.get('webViewLink')
        return file

    def deleteFile(self, drive_id):
        directory = os.path.join(settings.BASE_DIR, 'users')
        os.chdir(directory)
        creds = obtainCreds()
        service = build('drive', 'v3', credentials=creds)
        file = service.files().delete(fileId=drive_id).execute()
        #print 'File ID: %s' % file.get('webViewLink')
        return file

def searchFolder():
    creds = obtainCreds()
    service = build('drive', 'v3', credentials=creds)
    page_token = None
    while True:
        response = service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                            spaces='drive',
                                            fields='nextPageToken, files(name, id)',
                                            pageToken=page_token).execute()
        for folder in response.get('files', []):
            # Process change
            
            print ( 'Found file: %s (%s)' % (folder['name'], folder.get('id')) )
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

    return folder
    
def createFolder():
    creds = obtainCreds()
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {
    'name': 'Invoices',
    'mimeType': 'application/vnd.google-apps.folder'
    }
    file = service.files().create(body=file_metadata,
                                        fields='id').execute()
    print ( 'Folder ID: %s' % file.get('id') )

def obtainCreds():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_496032033985-mm80t6kdnvc2acrq9t40v6ah398okmr4.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=62741)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def obtainMimeType(upload_path):
    kind = filetype.guess(upload_path)
    if kind is None:
        print('Cannot guess file type!')
        return

    #print('File extension: %s' % kind.extension)
    #print('File MIME type: %s' % kind.mime)
    return kind.mime


if __name__ == '__main__':
    main()