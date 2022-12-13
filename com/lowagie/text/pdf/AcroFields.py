FIELD_TYPE_NONE = "int  0"
FIELD_TYPE_PUSHBUTTON = "int  1"
FIELD_TYPE_CHECKBOX = "int  2"
FIELD_TYPE_RADIOBUTTON = "int  3"
FIELD_TYPE_TEXT = "int  4"
FIELD_TYPE_LIST = "int  5"
FIELD_TYPE_COMBO = "int  6"
FIELD_TYPE_SIGNATURE = "int  7"
def getAppearanceStates():
    '''    public String[] getAppearanceStates(final String fieldName)
    '''
def getFieldType():
    '''    public int getFieldType(final String fieldName)
    '''
def exportAsFdf():
    '''    public void exportAsFdf(final FdfWriter writer)
    '''
def renameField():
    '''    public boolean renameField(final String oldName, String newName)
    '''
def getField():
    '''    public String getField(final String name)
    '''
def setFieldProperty():
    '''    public boolean setFieldProperty(final String field, final String name, final Object value, final int[] inst)
    public boolean setFieldProperty(final String field, final String name, final int value, final int[] inst)
    '''
def setFields():
    '''    public void setFields(final FdfReader fdf)
    public void setFields(final XfdfReader xfdf)
    '''
def setField():
    '''    public boolean setField(final String name, final String value)
    public boolean setField(final String name, String value, final String display)
    '''
def getFields():
    '''    public HashMap getFields()
    '''
def getFieldItem():
    '''    public Item getFieldItem(final String name)
    '''
def getFieldPositions():
    '''    public float[] getFieldPositions(final String name)
    '''
def removeFieldsFromPage():
    '''    public boolean removeFieldsFromPage(final int page)
    '''
def removeField():
    '''    public boolean removeField(final String name, final int page)
    public boolean removeField(final String name)
    '''
def isGenerateAppearances():
    '''    public boolean isGenerateAppearances()
    '''
def setGenerateAppearances():
    '''    public void setGenerateAppearances(final boolean generateAppearances)
    '''
def getSignatureNames():
    '''    public ArrayList getSignatureNames()
    '''
def getBlankSignatureNames():
    '''    public ArrayList getBlankSignatureNames()
    '''
def getSignatureDictionary():
    '''    public PdfDictionary getSignatureDictionary(final String name)
    '''
def signatureCoversWholeDocument():
    '''    public boolean signatureCoversWholeDocument(final String name)
    '''
def verifySignature():
    '''    public PdfPKCS7 verifySignature(final String name)
    public PdfPKCS7 verifySignature(final String name, final String provider)
    '''
def getTotalRevisions():
    '''    public int getTotalRevisions()
    '''
def getRevision():
    '''    public int getRevision(final String field)
    '''
def extractRevision():
    '''    public InputStream extractRevision(final String field)
    '''
def getFieldCache():
    '''    public HashMap getFieldCache()
    '''
def setFieldCache():
    '''    public void setFieldCache(final HashMap fieldCache)
    '''
def Item():
    '''    public Item()
    '''
def InstHit():
    '''    public InstHit(final int[] inst)
    '''
def isHit():
    '''    public boolean isHit(final int n)
    '''
def read():
    '''    public int read()
    public int read(final byte[] b, final int off, final int len)
    '''
def close():
    '''    public void close()
    '''
def compare():
    '''    public int compare(final Object o1, final Object o2)
    '''
