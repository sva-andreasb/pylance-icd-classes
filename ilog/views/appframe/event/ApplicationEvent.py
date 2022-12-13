APPLICATION_FIRST = "int  100"
DOCUMENT_CREATED = "int  100"
DOCUMENT_CLOSING = "int  101"
DOCUMENT_CLOSED = "int  102"
DOCUMENT_ACTIVATED = "int  103"
DOCUMENT_DEACTIVATED = "int  104"
DOCUMENT_SAVED = "int  105"
DOCUMENT_TEMPLATE_ACTIVATED = "int  106"
DOCUMENT_TEMPLATE_DEACTIVATED = "int  107"
DOCUMENT_VIEW_CREATED = "int  108"
DOCUMENT_VIEW_INITIALIZED = "int  109"
DOCUMENT_VIEW_CLOSING = "int  110"
DOCUMENT_VIEW_CLOSED = "int  111"
DOCUMENT_VIEW_ACTIVATED = "int  112"
DOCUMENT_VIEW_DEACTIVATED = "int  113"
VIEW_CONTAINER_CREATING = "int  114"
VIEW_CONTAINER_CREATED = "int  115"
VIEW_CONTAINER_ACTIVATED = "int  116"
VIEW_CONTAINER_DEACTIVATED = "int  117"
VIEW_CONTAINER_CLOSING = "int  118"
VIEW_CONTAINER_CLOSED = "int  119"
APPLICATION_INITIALIZING_SETTINGS = "int  120"
APPLICATION_INITIALIZED = "int  121"
APPLICATION_CLOSING = "int  122"
APPLICATION_SAVING_SETTINGS = "int  123"
MAIN_WINDOW_INITIALIZED = "int  124"
APPLICATION_CLOSED = "int  125"
DOCUMENT_INITIALIZING = "int  126"
def ApplicationEvent():
'''public ApplicationEvent(final int b, final IlvDocument ilvDocument)
public ApplicationEvent(final int b, final IlvDocumentView ilvDocumentView)
public ApplicationEvent(final int b, final IlvDocument a, final IlvDocumentView c, final IlvDocumentTemplate d)
public ApplicationEvent(final int b, final IlvDocument a, final IlvDocumentView ilvDocumentView, final IlvViewContainer e, final IlvDocumentTemplate d)
public ApplicationEvent(final int b, final IlvViewContainer ilvViewContainer)
public ApplicationEvent(final int b, final IlvDocumentTemplate ilvDocumentTemplate)
public ApplicationEvent(final int b, final IlvApplication ilvApplication)
'''
pass
def getDocument():
'''public IlvDocument getDocument()
'''
pass
def setDocument():
'''public void setDocument(final IlvDocument a)
'''
pass
def getID():
'''public int getID()
'''
pass
def getView():
'''public IlvDocumentView getView()
'''
pass
def setView():
'''public void setView(final IlvDocumentView c)
'''
pass
def getViewContainer():
'''public IlvViewContainer getViewContainer()
'''
pass
def getDocumentTemplate():
'''public IlvDocumentTemplate getDocumentTemplate()
'''
pass
def getDocumentTemplateName():
'''public String getDocumentTemplateName()
'''
pass
def getApplication():
'''public IlvApplication getApplication()
'''
pass
