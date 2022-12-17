def ():
    '''returns FTPClient\n\n
    (final String ftpUrl, final String username, final String password, final String changeToDir, final boolean makeDir)\n
    '''
def put():
    '''returns None\n\n
    put(final String serverFileName, final byte[] fileData)\n
    '''
def get():
    '''returns byte[]\n\n
    get(final String serverFileName, final boolean delete)\n
    '''
def getAllFiles():
    '''returns List\n\n
    getAllFiles(final int batchSize, final boolean delete)\n
    '''
