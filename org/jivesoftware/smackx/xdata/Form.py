def ():
    '''returns Form\n\n
    (final DataForm dataForm)\n
    (final DataForm.Type type)\n
    '''
def addField():
    '''returns None\n\n
    addField(final FormField field)\n
    '''
def setAnswer():
    '''returns None\n\n
    setAnswer(final String variable, final String value)\n
    setAnswer(final String variable, final int value)\n
    setAnswer(final String variable, final long value)\n
    setAnswer(final String variable, final float value)\n
    setAnswer(final String variable, final double value)\n
    setAnswer(final String variable, final boolean value)\n
    setAnswer(final String variable, final List<? extends CharSequence> values)\n
    '''
def setDefaultAnswer():
    '''returns None\n\n
    setDefaultAnswer(final String variable)\n
    '''
def getFields():
    '''returns List<FormField>\n\n
    getFields()\n
    '''
def getField():
    '''returns FormField\n\n
    getField(final String variable)\n
    '''
def hasField():
    '''returns boolean\n\n
    hasField(final String variable)\n
    '''
def getInstructions():
    '''returns String\n\n
    getInstructions()\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def setInstructions():
    '''returns None\n\n
    setInstructions(final String instructions)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def getDataFormToSend():
    '''returns DataForm\n\n
    getDataFormToSend()\n
    '''
def createAnswerForm():
    '''returns Form\n\n
    createAnswerForm()\n
    '''
