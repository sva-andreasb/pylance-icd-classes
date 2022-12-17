MBO_KPITEMPLATEMAIN = "String  \"KPITEMPLATEMAIN\""
CAUTIONMAX = "String  \"CAUTIONMAX\""
CAUTIONMIN = "String  \"CAUTIONMIN\""
ISACTIVE = "String  \"ISACTIVE\""
ISPUBLIC = "String  \"ISPUBLIC\""
KPITEMPLATEMAINID = "String  \"KPITEMPLATEMAINID\""
KPITEMPLATEMAINNUM = "String  \"KPITEMPLATEMAINNUM\""
KPITEMPLATENUM = "String  \"KPITEMPLATENUM\""
TARGET = "String  \"TARGET\""
RELATIONSHIP_VALUES = "String  \"KPITEMPLATEVARVALUES\""
def ():
    '''returns KPITemplateMain\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def validateTemplate():
    '''returns String\n\n
    validateTemplate()\n
    '''
def getVariableData():
    '''returns VariableData\n\n
    getVariableData(final String variable)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def copy():
    '''returns MboRemote\n\n
    copy(final MboSetRemote mboset, final long mboAddFlags)\n
    '''
def findValueForVariable():
    '''returns String\n\n
    findValueForVariable(final MboSetRemote mboset, final String varname)\n
    '''
