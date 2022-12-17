DEFAULT_CONTENT_TYPE = "String  \"application/octet-stream\""
DEFAULT_CHARSET = "String  \"ISO-8859-1\""
DEFAULT_TRANSFER_ENCODING = "String  \"binary\""
def ():
    '''returns FilePart\n\n
    (final String name, final PartSource partSource, final String contentType, final String charset)\n
    (final String name, final PartSource partSource)\n
    (final String name, final File file)\n
    (final String name, final File file, final String contentType, final String charset)\n
    (final String name, final String fileName, final File file)\n
    (final String name, final String fileName, final File file, final String contentType, final String charset)\n
    '''
