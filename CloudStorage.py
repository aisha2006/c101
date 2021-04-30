import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.Av5Prtlu_maoy87pC3qtzS6oNKWVMHUofLqP01EZmLsGdE46TS6jh6L9Hoiyg1NTLI0GFQD-IO3_kfV4CMYity8yJoZpOk2d4xtysofBMphxEE205BgczDu4ZFGpb0cJFIDm5ck"
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to transfer to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved successfully")
if __name__ == '__main__':
    main()
