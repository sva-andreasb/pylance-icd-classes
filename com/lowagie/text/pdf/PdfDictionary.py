def ():
    '''returns PdfDictionary\n\n
    ()\n
    (final PdfName type)\n
    '''
def toPdf():
    '''returns None\n\n
    toPdf(final PdfWriter writer, final OutputStream os)\n
    '''
def put():
    '''returns PdfObject\n\n
    put(final PdfName key, final PdfObject value)\n
    '''
def putEx():
    '''returns PdfObject\n\n
    putEx(final PdfName key, final PdfObject value)\n
    '''
def putDel():
    '''returns PdfObject\n\n
    putDel(final PdfName key, final PdfObject value)\n
    '''
def remove():
    '''returns PdfObject\n\n
    remove(final PdfName key)\n
    '''
def get():
    '''returns PdfObject\n\n
    get(final PdfName key)\n
    '''
def isDictionaryType():
    '''returns boolean\n\n
    isDictionaryType(final PdfName type)\n
    '''
def isFont():
    '''returns boolean\n\n
    isFont()\n
    '''
def isPage():
    '''returns boolean\n\n
    isPage()\n
    '''
def isPages():
    '''returns boolean\n\n
    isPages()\n
    '''
def isCatalog():
    '''returns boolean\n\n
    isCatalog()\n
    '''
def isOutlineTree():
    '''returns boolean\n\n
    isOutlineTree()\n
    '''
def merge():
    '''returns None\n\n
    merge(final PdfDictionary other)\n
    '''
def mergeDifferent():
    '''returns None\n\n
    mergeDifferent(final PdfDictionary other)\n
    '''
def getKeys():
    '''returns Set\n\n
    getKeys()\n
    '''
def putAll():
    '''returns None\n\n
    putAll(final PdfDictionary dic)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final PdfName key)\n
    '''
