PERSON_SEARCH_STR = "String  \"personid like :1 OR LOWER(displayname) like :2 OR LOWER(firstname) like :3 OR LOWER(lastname) like :4 OR personid in (select personid from email where LOWER(emailaddress) like :5 and isprimary=1) OR personid in (select personid from maxuser where LOWER(loginid) like :6)\""
def ():
    '''returns CDUIGetUserOutboundProc\n\n
    ()\n
    '''
def search():
    '''returns None\n\n
    search(final MboSetRemote mboSet, final String text)\n
    '''
