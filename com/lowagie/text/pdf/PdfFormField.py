FF_READ_ONLY = "int  1"
FF_REQUIRED = "int  2"
FF_NO_EXPORT = "int  4"
FF_NO_TOGGLE_TO_OFF = "int  16384"
FF_RADIO = "int  32768"
FF_PUSHBUTTON = "int  65536"
FF_MULTILINE = "int  4096"
FF_PASSWORD = "int  8192"
FF_COMBO = "int  131072"
FF_EDIT = "int  262144"
FF_FILESELECT = "int  1048576"
FF_MULTISELECT = "int  2097152"
FF_DONOTSPELLCHECK = "int  4194304"
FF_DONOTSCROLL = "int  8388608"
FF_COMB = "int  16777216"
FF_RADIOSINUNISON = "int  33554432"
Q_LEFT = "int  0"
Q_CENTER = "int  1"
Q_RIGHT = "int  2"
MK_NO_ICON = "int  0"
MK_NO_CAPTION = "int  1"
MK_CAPTION_BELOW = "int  2"
MK_CAPTION_ABOVE = "int  3"
MK_CAPTION_RIGHT = "int  4"
MK_CAPTION_LEFT = "int  5"
MK_CAPTION_OVERLAID = "int  6"
MULTILINE = "boolean  true"
SINGLELINE = "boolean  false"
PLAINTEXT = "boolean  false"
PASSWORD = "boolean  true"
def ():
    '''returns PdfFormField\n\n
    (final PdfWriter writer, final float llx, final float lly, final float urx, final float ury, final PdfAction action)\n
    '''
def setWidget():
    '''returns None\n\n
    setWidget(final Rectangle rect, final PdfName highlight)\n
    '''
def setButton():
    '''returns None\n\n
    setButton(final int flags)\n
    '''
def getParent():
    '''returns PdfFormField\n\n
    getParent()\n
    '''
def addKid():
    '''returns None\n\n
    addKid(final PdfFormField field)\n
    '''
def setFieldFlags():
    '''returns int\n\n
    setFieldFlags(final int flags)\n
    '''
def setValueAsString():
    '''returns None\n\n
    setValueAsString(final String s)\n
    '''
def setValueAsName():
    '''returns None\n\n
    setValueAsName(final String s)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final PdfSignature sig)\n
    '''
def setDefaultValueAsString():
    '''returns None\n\n
    setDefaultValueAsString(final String s)\n
    '''
def setDefaultValueAsName():
    '''returns None\n\n
    setDefaultValueAsName(final String s)\n
    '''
def setFieldName():
    '''returns None\n\n
    setFieldName(final String s)\n
    '''
def setUserName():
    '''returns None\n\n
    setUserName(final String s)\n
    '''
def setMappingName():
    '''returns None\n\n
    setMappingName(final String s)\n
    '''
def setQuadding():
    '''returns None\n\n
    setQuadding(final int v)\n
    '''
