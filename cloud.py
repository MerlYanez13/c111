import dropbox
class transferdata:
    def __init__(self, accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self, fromfile, tofile):
        DBX=dropbox.Dropbox(self.accesstoken)
        F=open(fromfile,'rb')
        DBX.files_upload(F.read(),tofile)

def main():
    accesstoken="sl.A5S3LTpMcwoiptjwZkPOdTiwpQc9HnFrBa9G3tAVC1unGJbeDpcrgs0Ya7mtk1BnC:\Users\mdmur\OneDrive\Desktop\Whitehat.jrhcfAy8d_UFOFAf_RRSvbPW8o6UwqYFvAnTkRMLzSvCd0Wfqj-0yzrESEoFJG-j8BWzSIYp2bDtC3"
    Transferdata=transferdata(accesstoken)
    file1=input("input your source file: ")
    file2=input("Input your destination file: ")
    Transferdata.uploadfile(file1,file2)
    print("file moved")

main()