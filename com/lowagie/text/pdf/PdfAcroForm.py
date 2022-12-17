def addCalculationOrder():
    '''returns None\n\n
    addCalculationOrder(final PdfFormField formField)\n
    '''
def setSigFlags():
    '''returns None\n\n
    setSigFlags(final int f)\n
    '''
def addFormField():
    '''returns None\n\n
    addFormField(final PdfFormField formField)\n
    '''
def addHtmlPostButton():
    '''returns PdfFormField\n\n
    addHtmlPostButton(final String name, final String caption, final String value, final String url, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addResetButton():
    '''returns PdfFormField\n\n
    addResetButton(final String name, final String caption, final String value, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addMap():
    '''returns PdfFormField\n\n
    addMap(final String name, final String value, final String url, final PdfContentByte appearance, final float llx, final float lly, final float urx, final float ury)\n
    '''
def setButtonParams():
    '''returns None\n\n
    setButtonParams(final PdfFormField button, final int characteristics, final String name, final String value)\n
    '''
def drawButton():
    '''returns None\n\n
    drawButton(final PdfFormField button, final String caption, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addHiddenField():
    '''returns PdfFormField\n\n
    addHiddenField(final String name, final String value)\n
    '''
def addSingleLineTextField():
    '''returns PdfFormField\n\n
    addSingleLineTextField(final String name, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addMultiLineTextField():
    '''returns PdfFormField\n\n
    addMultiLineTextField(final String name, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addSingleLinePasswordField():
    '''returns PdfFormField\n\n
    addSingleLinePasswordField(final String name, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def setTextFieldParams():
    '''returns None\n\n
    setTextFieldParams(final PdfFormField field, final String text, final String name, final float llx, final float lly, final float urx, final float ury)\n
    '''
def drawSingleLineOfText():
    '''returns None\n\n
    drawSingleLineOfText(final PdfFormField field, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def drawMultiLineOfText():
    '''returns None\n\n
    drawMultiLineOfText(final PdfFormField field, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addCheckBox():
    '''returns PdfFormField\n\n
    addCheckBox(final String name, final String value, final boolean status, final float llx, final float lly, final float urx, final float ury)\n
    '''
def setCheckBoxParams():
    '''returns None\n\n
    setCheckBoxParams(final PdfFormField field, final String name, final String value, final boolean status, final float llx, final float lly, final float urx, final float ury)\n
    '''
def drawCheckBoxAppearences():
    '''returns None\n\n
    drawCheckBoxAppearences(final PdfFormField field, final String value, final float llx, final float lly, final float urx, final float ury)\n
    '''
def getRadioGroup():
    '''returns PdfFormField\n\n
    getRadioGroup(final String name, final String defaultValue, final boolean noToggleToOff)\n
    '''
def addRadioGroup():
    '''returns None\n\n
    addRadioGroup(final PdfFormField radiogroup)\n
    '''
def addRadioButton():
    '''returns PdfFormField\n\n
    addRadioButton(final PdfFormField radiogroup, final String value, final float llx, final float lly, final float urx, final float ury)\n
    '''
def drawRadioAppearences():
    '''returns None\n\n
    drawRadioAppearences(final PdfFormField field, final String value, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addSelectList():
    '''returns PdfFormField\n\n
    addSelectList(final String name, final String[] options, final String defaultValue, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    addSelectList(final String name, final String[][] options, final String defaultValue, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addComboBox():
    '''returns PdfFormField\n\n
    addComboBox(final String name, final String[] options, String defaultValue, final boolean editable, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    addComboBox(final String name, final String[][] options, final String defaultValue, final boolean editable, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)\n
    '''
def setChoiceParams():
    '''returns None\n\n
    setChoiceParams(final PdfFormField field, final String name, final String defaultValue, final float llx, final float lly, final float urx, final float ury)\n
    '''
def addSignature():
    '''returns PdfFormField\n\n
    addSignature(final String name, final float llx, final float lly, final float urx, final float ury)\n
    '''
def setSignatureParams():
    '''returns None\n\n
    setSignatureParams(final PdfFormField field, final String name, final float llx, final float lly, final float urx, final float ury)\n
    '''
def drawSignatureAppearences():
    '''returns None\n\n
    drawSignatureAppearences(final PdfFormField field, final float llx, final float lly, final float urx, final float ury)\n
    '''
