import http.client
import json


class Dropbox:
    def __init__(self, token):
        self.token = token

    def upload_file(self, file_path, dropbox_path, revision=None):
        connection = http.client.HTTPSConnection('content.dropboxapi.com')
        mode = {'.tag': 'update', 'update': revision} if revision else 'overwrite'
        dropbox_args = {
            'path': dropbox_path,
            'mode': mode,
            'autorename': False,
            'mute': False,
            'strict_conflict': False,
        }
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/octet-stream',
            'Dropbox-API-Arg': json.dumps(dropbox_args)
        }
        connection.request('POST', '/2/files/upload', body=open(file_path, 'rb'), headers=headers)

        return json.loads(connection.getresponse().read())
