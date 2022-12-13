def getInstance():
    '''public static synchronized UserPersister getInstance()
    '''
def addUser():
    '''public synchronized void addUser(final String adminPassword, final String user, final String password)
    '''
def deleteUser():
    '''public synchronized void deleteUser(final String adminPassword, final String user)
    '''
def changePassword():
    '''public synchronized void changePassword(final String userName, final String oldPassword, final String newPassword, final String retypeNewPassword)
    '''
def validPassword():
    '''public boolean validPassword(final String userName, final String password)
    '''
def main():
    '''public static void main(final String[] args)
    '''
