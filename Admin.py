class Admin():
    def __init__(self):
        self.adminID = None
        self.adminPassword = None

    def setAdminID(self, adminID):
        self.adminID = adminID

    def getAdminID(self):
        return self.adminID

    def setAdminPassword(self, adminPassword):
        self.adminPassword = adminPassword

    def getAdminPassword(self):
        return self.adminPassword