def addCalculationOrder():
    '''public void addCalculationOrder(final PdfFormField formField)
    '''
def setSigFlags():
    '''public void setSigFlags(final int f)
    '''
def addFormField():
    '''public void addFormField(final PdfFormField formField)
    '''
def addHtmlPostButton():
    '''public PdfFormField addHtmlPostButton(final String name, final String caption, final String value, final String url, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def addResetButton():
    '''public PdfFormField addResetButton(final String name, final String caption, final String value, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def addMap():
    '''public PdfFormField addMap(final String name, final String value, final String url, final PdfContentByte appearance, final float llx, final float lly, final float urx, final float ury)
    '''
def setButtonParams():
    '''public void setButtonParams(final PdfFormField button, final int characteristics, final String name, final String value)
    '''
def drawButton():
    '''public void drawButton(final PdfFormField button, final String caption, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def addHiddenField():
    '''public PdfFormField addHiddenField(final String name, final String value)
    '''
def addSingleLineTextField():
    '''public PdfFormField addSingleLineTextField(final String name, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def addMultiLineTextField():
    '''public PdfFormField addMultiLineTextField(final String name, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def addSingleLinePasswordField():
    '''public PdfFormField addSingleLinePasswordField(final String name, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def setTextFieldParams():
    '''public void setTextFieldParams(final PdfFormField field, final String text, final String name, final float llx, final float lly, final float urx, final float ury)
    '''
def drawSingleLineOfText():
    '''public void drawSingleLineOfText(final PdfFormField field, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def drawMultiLineOfText():
    '''public void drawMultiLineOfText(final PdfFormField field, final String text, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def addCheckBox():
    '''public PdfFormField addCheckBox(final String name, final String value, final boolean status, final float llx, final float lly, final float urx, final float ury)
    '''
def setCheckBoxParams():
    '''public void setCheckBoxParams(final PdfFormField field, final String name, final String value, final boolean status, final float llx, final float lly, final float urx, final float ury)
    '''
def drawCheckBoxAppearences():
    '''public void drawCheckBoxAppearences(final PdfFormField field, final String value, final float llx, final float lly, final float urx, final float ury)
    '''
def getRadioGroup():
    '''public PdfFormField getRadioGroup(final String name, final String defaultValue, final boolean noToggleToOff)
    '''
def addRadioGroup():
    '''public void addRadioGroup(final PdfFormField radiogroup)
    '''
def addRadioButton():
    '''public PdfFormField addRadioButton(final PdfFormField radiogroup, final String value, final float llx, final float lly, final float urx, final float ury)
    '''
def drawRadioAppearences():
    '''public void drawRadioAppearences(final PdfFormField field, final String value, final float llx, final float lly, final float urx, final float ury)
    '''
def addSelectList():
    '''public PdfFormField addSelectList(final String name, final String[] options, final String defaultValue, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    public PdfFormField addSelectList(final String name, final String[][] options, final String defaultValue, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def addComboBox():
    '''public PdfFormField addComboBox(final String name, final String[] options, String defaultValue, final boolean editable, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    public PdfFormField addComboBox(final String name, final String[][] options, final String defaultValue, final boolean editable, final BaseFont font, final float fontSize, final float llx, final float lly, final float urx, final float ury)
    '''
def setChoiceParams():
    '''public void setChoiceParams(final PdfFormField field, final String name, final String defaultValue, final float llx, final float lly, final float urx, final float ury)
    '''
def addSignature():
    '''public PdfFormField addSignature(final String name, final float llx, final float lly, final float urx, final float ury)
    '''
def setSignatureParams():
    '''public void setSignatureParams(final PdfFormField field, final String name, final float llx, final float lly, final float urx, final float ury)
    '''
def drawSignatureAppearences():
    '''public void drawSignatureAppearences(final PdfFormField field, final float llx, final float lly, final float urx, final float ury)
    '''
