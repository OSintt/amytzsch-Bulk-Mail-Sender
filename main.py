from colorama import *
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import time
def emailbomber():
    SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)
    file = open('./correos.txt', "r")
    for mails in file:
        mails = mails.strip('\n')
        try:
            message = MIMEText('DOMADOS POR OSINT // @calitzsch')
            message['to'] = mails
            message['subject'] = f'FOLLOW @calitzsch on ig'
            create_message = {'raw': base64.urlsafe_b64encode(
                message.as_bytes()).decode()}
            service.users().messages().send(
                userId="me", body=create_message).execute()
            print(F'sent message to {mails}')
            time.sleep(2.5)
        except HTTPError:
            print(F'An error occurred with {mails}')
            pass
        except Exception as e:
            print(F'An error occurred with {mails}')
            pass


emailbomber()
