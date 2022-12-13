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
def PdfFormField():
'''public PdfFormField(final PdfWriter writer, final float llx, final float lly, final float urx, final float ury, final PdfAction action)
'''
pass
def setWidget():
'''public void setWidget(final Rectangle rect, final PdfName highlight)
'''
pass
def createEmpty():
'''public static PdfFormField createEmpty(final PdfWriter writer)
'''
pass
def setButton():
'''public void setButton(final int flags)
'''
pass
def createPushButton():
'''public static PdfFormField createPushButton(final PdfWriter writer)
'''
pass
def createCheckBox():
'''public static PdfFormField createCheckBox(final PdfWriter writer)
'''
pass
def createRadioButton():
'''public static PdfFormField createRadioButton(final PdfWriter writer, final boolean noToggleToOff)
'''
pass
def createTextField():
'''public static PdfFormField createTextField(final PdfWriter writer, final boolean multiline, final boolean password, final int maxLen)
'''
pass
def createList():
'''public static PdfFormField createList(final PdfWriter writer, final String[] options, final int topIndex)
public static PdfFormField createList(final PdfWriter writer, final String[][] options, final int topIndex)
'''
pass
def createCombo():
'''public static PdfFormField createCombo(final PdfWriter writer, final boolean edit, final String[] options, final int topIndex)
public static PdfFormField createCombo(final PdfWriter writer, final boolean edit, final String[][] options, final int topIndex)
'''
pass
def createSignature():
'''public static PdfFormField createSignature(final PdfWriter writer)
'''
pass
def getParent():
'''public PdfFormField getParent()
'''
pass
def addKid():
'''public void addKid(final PdfFormField field)
'''
pass
def setFieldFlags():
'''public int setFieldFlags(final int flags)
'''
pass
def setValueAsString():
'''public void setValueAsString(final String s)
'''
pass
def setValueAsName():
'''public void setValueAsName(final String s)
'''
pass
def setValue():
'''public void setValue(final PdfSignature sig)
'''
pass
def setDefaultValueAsString():
'''public void setDefaultValueAsString(final String s)
'''
pass
def setDefaultValueAsName():
'''public void setDefaultValueAsName(final String s)
'''
pass
def setFieldName():
'''public void setFieldName(final String s)
'''
pass
def setUserName():
'''public void setUserName(final String s)
'''
pass
def setMappingName():
'''public void setMappingName(final String s)
'''
pass
def setQuadding():
'''public void setQuadding(final int v)
'''
pass
def shallowDuplicate():
'''public static PdfAnnotation shallowDuplicate(final PdfAnnotation annot)
'''
pass
