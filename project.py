import dropbox

class FileUploader : 
    def __init__(self, access_token):
        self.access_token = access_token
    def uploadFile(self, src, dest):
        dbx = dropbox.Dropbox(self.access_token)
        with open(src, 'rb') as f:
            dbx.files_upload(f.read(), dest)

def main():
    access_token = 'mMf2p7N20QoAAAAAAAAAAaTi-MOcAaulgdAkDBR4BjewjrvGxyTIsV0jeNgmQpeQ'
    uploader = FileUploader(access_token)
    src = input('Enter Source:')
    dest = input('Enter destination:')
    uploader.uploadFile(src, dest)
    print('File Transferred Successfuly!')

main()