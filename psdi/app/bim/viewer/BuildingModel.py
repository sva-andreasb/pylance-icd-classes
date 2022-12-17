TABLE_NAME = "String  \"BUILDINGMODEL\""
DOMAIN_BIMVIEWERTYPE = "String  \"BIMVIEWERTYPE\""
VIEWER_TYPE_VENDOR = "String  \"Vendor\""
RELATIONSHIP_BOOKMARK = "String  \"BOOKMARK\""
RELATIONSHIP_DOCLINKS = "String  \"DOCLINKS\""
RELATIONSHOP_SAVEDVIEWS = "String  \"SAVEDVIEWS\""
FIELD_ASSETVIEW = "String  \"ASSETVIEW\""
FIELD_ATTRIBUTECLASS = "String  \"ATTRIBUTECLASS\""
FIELD_ATTRIBUTENAME = "String  \"ATTRIBUTENAME\""
FIELD_DESCRIPTION = "String  \"DESCRIPTION\""
FIELD_LOCATION = "String  \"LOCATION\""
FIELD_SELMODE = "String  \"SELMODE\""
FIELD_LOCATIONVIEW = "String  \"LOCATIONVIEW\""
FIELD_LOOKUPVIEW = "String  \"LOOKUPVIEW\""
FIELD_LONGDESCRIPTION = "String  \"DESCRIPTION_LONGDESCRIPTION\""
FIELD_OBJECTKEY = "String  \"OBJECTKEY\""
FIELD_ORGID = "String  \"ORGID\""
FIELD_PARAMCLASS = "String  \"PARAMCLASS\""
FIELD_PARAMNAME = "String  \"PARAMNAME\""
FIELD_PRIORITY = "String  \"PRIORITY\""
FIELD_SITEID = "String  \"SITEID\""
FIELD_TITLE = "String  \"TITLE\""
FIELD_URL = "String  \"URL\""
FIELD_VIEWERTYPE = "String  \"VIEWERTYPE\""
FIELD_WORKORDERVIEW = "String  \"WORKORDERVIEW\""
FIELD_LATITUDEY = "String  \"LATITUDEY\""
FIELD_LONGITUDEX = "String  \"LONGITUDEX\""
FIELD_FORMATTEDADDRESS = "String  \"FORMATTEDADDRESS\""
def ():
    '''returns BuildingModel\n\n
    (final MboSet ms)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def getViewerType():
    '''returns String\n\n
    getViewerType()\n
    '''
def getLatitudeY():
    '''returns Double\n\n
    getLatitudeY()\n
    '''
def getLongitudeX():
    '''returns Double\n\n
    getLongitudeX()\n
    '''
def getAddressString():
    '''returns String\n\n
    getAddressString()\n
    '''
def isGISDataReadonly():
    '''returns boolean\n\n
    isGISDataReadonly()\n
    '''
def saveGISData():
    '''returns None\n\n
    saveGISData(final String address, final String lat, final String lng)\n
    '''
def hasCoords():
    '''returns Boolean\n\n
    hasCoords()\n
    '''
