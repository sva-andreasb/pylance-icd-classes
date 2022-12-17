TABLE_NAME = "String  \"BIMFILTER\""
RELATIONSHIP_ENTRYLIST = "String  \"ENTRYLIST\""
DOMAIN_BIMFILTERTYPE = "String  \"BIMFILTERTYPE\""
FIELD_FILTERNAME = "String  \"FILTERNAME\""
FIELD_FILTERTYPE = "String  \"FILTERTYPE\""
FIELD_ORGID = "String  \"ORGID\""
FIELD_SITEID = "String  \"SITEID\""
FIELD_DESCRIPTION = "String  \"DESCRIPTION\""
FILTER_TYPE_UNKNOWN = "int  0"
FILTER_TYPE_INCLUDE = "int  1"
FILTER_TYPE_EXCLUDE = "int  2"
def ():
    '''returns BIMFilter\n\n
    (final MboSet ms)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def getFilterType():
    '''returns int\n\n
    getFilterType()\n
    '''
