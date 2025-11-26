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
    #hello
    def viewAllEvents(self, eventslist):
        print("\n=== ALL events ===")

        if len(eventslist) ==0:
            print("no events availabel check later for updates.")
            return
        
        for e in eventslist:
            print(e)