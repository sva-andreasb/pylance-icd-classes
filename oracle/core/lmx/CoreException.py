UNIMPLEMENTED = "byte  1"
UNDERFLOW = "byte  2"
OVERFLOW = "byte  3"
INVALIDORLN = "byte  4"
BADFORMATORLN = "byte  5"
INVALIDORLD = "byte  6"
BADFORMATORLD = "byte  7"
BADYEAR = "byte  8"
BADDAYYEAR = "byte  9"
BADJULIANDATE = "byte  10"
INVALIDINPUTN = "byte  11"
NLSNOTSUPPORTED = "byte  12"
INVALIDINPUT = "byte  13"
CONVERSIONERROR = "byte  14"
def CoreException():
'''public CoreException()
public CoreException(final String message)
public CoreException(final byte ecode)
'''
pass
def setErrorCode():
'''public void setErrorCode(final byte ecode)
'''
pass
def getErrorCode():
'''public byte getErrorCode()
'''
pass
def getMessage():
'''public String getMessage()
public static String getMessage(final byte b)
'''
pass
