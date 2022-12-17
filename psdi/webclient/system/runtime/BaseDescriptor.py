DESCRIPTORCLASS_CONTROLDESCRIPTOR = "String  \"psdi.webclient.system.runtime.ControlDescriptor\""
DESCRIPTORCLASS_COMPONENTDESCRIPTOR = "String  \"psdi.webclient.system.runtime.ComponentDescriptor\""
DESCRIPTORATTRIBUTE_CLASS = "String  \"class\""
DESCRIPTORATTRIBUTE_HANDLER = "String  \"instance-class\""
DESCRIPTORATTRIBUTE_NAME = "String  \"name\""
DESCRIPTORATTRIBUTE_SHORTNAME = "String  \"short-name\""
DESCRIPTORATTRIBUTE_DESCRIPTORCLASS = "String  \"descriptor-class\""
DESCRIPTORATTRIBUTE_DEFAULT = "String  \"default\""
DESCRIPTORATTRIBUTE_TYPE = "String  \"type\""
DESCRIPTORTAG_CONTROLDESCRIPTOR = "String  \"control-descriptor\""
DESCRIPTORTAG_CONTAINER = "String  \"containers\""
DESCRIPTORTAG_COMPONENTDESCRIPTOR = "String  \"component-descriptor\""
DESCRIPTORTAG_COMPONENTLIST = "String  \"component-list\""
DESCRIPTORTAG_CHILDCONTROLS = "String  \"child-controls\""
DESCRIPTORTAG_COMPONENTS = "String  \"components\""
DESCRIPTORTAG_DEFAULTVALUE = "String  \"default-value\""
DESCRIPTORTAG_DESCRIPTION = "String  \"description\""
DESCRIPTORTAG_FLAG = "String  \"flag\""
DESCRIPTORTAG_PROPERTY = "String  \"property\""
DESCRIPTORTAG_PROPERTYLIST = "String  \"property-list\""
DESCRIPTORTAG_VALUE = "String  \"value\""
DESCRIPTORTAG_VALUELIST = "String  \"value-list\""
DESCRIPTORTAG_BINDLIST = "String  \"bindlist\""
DESCRIPTORTAG_ATTRIBUTE = "String  \"attribute\""
DESCRIPTORTAG_LABEL = "String  \"label\""
DESCRIPTORTAG_INPUTMODE = "String  \"inputmode\""
DESCRIPTORTAG_TEMPLATE = "String  \"template\""
DESCRIPTORTAG_USERAGENT = "String  \"user-agent\""
DESCRIPTORTAG_RENDERCONTROLS = "String  \"rendercontrols\""
DESCRIPTORTYPE_MENU = "String  \"menu\""
DESCRIPTORTYPE_TABLE = "String  \"table\""
DATATYPE_BOOLEAN = "String  \"xsd:boolean\""
DATATYPE_STRING = "String  \"xsd:string\""
DATATYPE_INTEGER = "String  \"xsd:integer\""
DATATYPE_POSITVE_INTEGER = "String  \"xsd:positiveInteger\""
DESCRIPTORTYPE_DIALOG = "String  \"dialog\""
DESCRIPTORTYPE_ACTION = "String  \"action\""
DESCRIPTORTYPE_MODELESSDIALOG = "String  \"modelessdialog\""
DESCRIPTORTYPE_MOVABLEWINDOWDIALOG = "String  \"moveablewindow\""
DESCRIPTORTYPE_MESSAGEBOX = "String  \"messagebox\""
DESCRIPTORTYPE_PAGE = "String  \"page\""
DESCRIPTORTYPE_POPUP = "String  \"popup\""
DESCRIPTORTYPE_PRESENTATION = "String  \"presentation\""
DESCRIPTORTYPE_RECORDHOVER = "String  \"recordhover\""
INSTANCECLASS_CONTROLINSTANCE = "String  \"psdi.webclient.system.controller.ControlInstance\""
INSTANCECLASS_COMPONENTINSTANCE = "String  \"psdi.webclient.system.controller.ComponentInstance\""
def getElement():
    '''returns Element\n\n
    getElement()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getShortName():
    '''returns String\n\n
    getShortName()\n
    '''
def getInstance():
    '''returns BaseInstance\n\n
    getInstance(final WebClientSession wcs)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final Object key)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Element controlElement)\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final String key)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
