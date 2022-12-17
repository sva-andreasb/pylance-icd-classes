TYPE_CHECK = "int  1"
TYPE_CIRCLE = "int  2"
TYPE_CROSS = "int  3"
TYPE_DIAMOND = "int  4"
TYPE_SQUARE = "int  5"
TYPE_STAR = "int  6"
def ():
    '''returns RadioCheckField\n\n
    (final PdfWriter writer, final Rectangle box, final String fieldName, final String onValue)\n
    '''
def getCheckType():
    '''returns int\n\n
    getCheckType()\n
    '''
def setCheckType():
    '''returns None\n\n
    setCheckType(int checkType)\n
    '''
def getOnValue():
    '''returns String\n\n
    getOnValue()\n
    '''
def setOnValue():
    '''returns None\n\n
    setOnValue(final String onValue)\n
    '''
def isChecked():
    '''returns boolean\n\n
    isChecked()\n
    '''
def setChecked():
    '''returns None\n\n
    setChecked(final boolean checked)\n
    '''
def getAppearance():
    '''returns PdfAppearance\n\n
    getAppearance(final boolean isRadio, final boolean on)\n
    '''
def getAppearanceRadioCircle():
    '''returns PdfAppearance\n\n
    getAppearanceRadioCircle(final boolean on)\n
    '''
def getRadioGroup():
    '''returns PdfFormField\n\n
    getRadioGroup(final boolean noToggleToOff, final boolean radiosInUnison)\n
    '''
def getRadioField():
    '''returns PdfFormField\n\n
    getRadioField()\n
    '''
def getCheckField():
    '''returns PdfFormField\n\n
    getCheckField()\n
    '''
