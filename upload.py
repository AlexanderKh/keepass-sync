from config import dropbox_token, database_path
from dropbox import Dropbox

dropbox = Dropbox(dropbox_token)

response = dropbox.upload_file(database_path, '/test-upload.kdbx')

print(response)
