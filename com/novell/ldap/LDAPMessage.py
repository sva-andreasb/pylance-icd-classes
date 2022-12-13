BIND_REQUEST = "int  0"
BIND_RESPONSE = "int  1"
UNBIND_REQUEST = "int  2"
SEARCH_REQUEST = "int  3"
SEARCH_RESPONSE = "int  4"
SEARCH_RESULT = "int  5"
MODIFY_REQUEST = "int  6"
MODIFY_RESPONSE = "int  7"
ADD_REQUEST = "int  8"
ADD_RESPONSE = "int  9"
DEL_REQUEST = "int  10"
DEL_RESPONSE = "int  11"
MODIFY_RDN_REQUEST = "int  12"
MODIFY_RDN_RESPONSE = "int  13"
COMPARE_REQUEST = "int  14"
COMPARE_RESPONSE = "int  15"
ABANDON_REQUEST = "int  16"
SEARCH_RESULT_REFERENCE = "int  19"
EXTENDED_REQUEST = "int  23"
EXTENDED_RESPONSE = "int  24"
INTERMEDIATE_RESPONSE = "int  25"
def getControls():
'''public LDAPControl[] getControls()
'''
pass
def getMessageID():
'''public int getMessageID()
'''
pass
def getType():
'''public int getType()
'''
pass
def isRequest():
'''public boolean isRequest()
'''
pass
def toString():
'''public String toString()
'''
pass
def setTag():
'''public void setTag(final String stringTag)
'''
pass
def getTag():
'''public String getTag()
'''
pass
def writeDSML():
'''public void writeDSML(final OutputStream outputStream)
'''
pass
def readDSML():
'''public static Object readDSML(final InputStream inputStream)
'''
pass
def writeExternal():
'''public void writeExternal(final ObjectOutput objectOutput)
'''
pass
def readExternal():
'''public void readExternal(final ObjectInput objectInput)
'''
pass
