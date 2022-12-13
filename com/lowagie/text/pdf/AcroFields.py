FIELD_TYPE_NONE = "int  0"
FIELD_TYPE_PUSHBUTTON = "int  1"
FIELD_TYPE_CHECKBOX = "int  2"
FIELD_TYPE_RADIOBUTTON = "int  3"
FIELD_TYPE_TEXT = "int  4"
FIELD_TYPE_LIST = "int  5"
FIELD_TYPE_COMBO = "int  6"
FIELD_TYPE_SIGNATURE = "int  7"
def getAppearanceStates():
'''public String[] getAppearanceStates(final String fieldName)
'''
pass
def getFieldType():
'''public int getFieldType(final String fieldName)
'''
pass
def exportAsFdf():
'''public void exportAsFdf(final FdfWriter writer)
'''
pass
def renameField():
'''public boolean renameField(final String oldName, String newName)
'''
pass
def getField():
'''public String getField(final String name)
'''
pass
def setFieldProperty():
'''public boolean setFieldProperty(final String field, final String name, final Object value, final int[] inst)
public boolean setFieldProperty(final String field, final String name, final int value, final int[] inst)
'''
pass
def setFields():
'''public void setFields(final FdfReader fdf)
public void setFields(final XfdfReader xfdf)
'''
pass
def setField():
'''public boolean setField(final String name, final String value)
public boolean setField(final String name, String value, final String display)
'''
pass
def getFields():
'''public HashMap getFields()
'''
pass
def getFieldItem():
'''public Item getFieldItem(final String name)
'''
pass
def getFieldPositions():
'''public float[] getFieldPositions(final String name)
'''
pass
def removeFieldsFromPage():
'''public boolean removeFieldsFromPage(final int page)
'''
pass
def removeField():
'''public boolean removeField(final String name, final int page)
public boolean removeField(final String name)
'''
pass
def isGenerateAppearances():
'''public boolean isGenerateAppearances()
'''
pass
def setGenerateAppearances():
'''public void setGenerateAppearances(final boolean generateAppearances)
'''
pass
def getSignatureNames():
'''public ArrayList getSignatureNames()
'''
pass
def getBlankSignatureNames():
'''public ArrayList getBlankSignatureNames()
'''
pass
def getSignatureDictionary():
'''public PdfDictionary getSignatureDictionary(final String name)
'''
pass
def signatureCoversWholeDocument():
'''public boolean signatureCoversWholeDocument(final String name)
'''
pass
def verifySignature():
'''public PdfPKCS7 verifySignature(final String name)
public PdfPKCS7 verifySignature(final String name, final String provider)
'''
pass
def getTotalRevisions():
'''public int getTotalRevisions()
'''
pass
def getRevision():
'''public int getRevision(final String field)
'''
pass
def extractRevision():
'''public InputStream extractRevision(final String field)
'''
pass
def getFieldCache():
'''public HashMap getFieldCache()
'''
pass
def setFieldCache():
'''public void setFieldCache(final HashMap fieldCache)
'''
pass
def Item():
'''public Item()
'''
pass
def InstHit():
'''public InstHit(final int[] inst)
'''
pass
def isHit():
'''public boolean isHit(final int n)
'''
pass
def read():
'''public int read()
public int read(final byte[] b, final int off, final int len)
'''
pass
def close():
'''public void close()
'''
pass
def compare():
'''public int compare(final Object o1, final Object o2)
'''
pass
