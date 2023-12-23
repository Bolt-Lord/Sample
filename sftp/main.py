import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def sftpExample():

    try:
        s = pysftp.Connection(host='aws-sftp.idp.com', username='qualtrics_htc_dvlinb@idp.com', password='V#mwd$%QgL%b48tB', cnopts=cnopts)
        print("Connection sucessful")
        remotepath='NPS/HEALTHCHECK/DVLP/INBOUND/'
        localpath=r'C:\Users\balasubramaniam.cs\OneDrive - IDP Education Ltd\Documents\Security check list V2.0.xlsx'
        s.chdir(remotepath)
        s.put(localpath, 'Security check list V2.0.xlsx')
        print("sftp sucess")

        s.close()

    except Exception as e:
        print(str(e))

sftpExample()
