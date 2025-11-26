class Admin():
    def __init__(self):
        self.adminID = None
        self.adminPassword = None

    def set_admin_id(self, adminID):
        self.adminID = adminID

    def get_admin_id(self):
        return self.adminID

    def set_admin_password(self, adminPassword):
        self.adminPassword = adminPassword

    def get_admin_password(self):
        return self.adminPassword
    #hello
    def view_all_events(self, eventslist):
        print("\n=== ALL events ===")

        if len(eventslist) ==0:
            print("no events availabel check later for updates.")
            return
        
        for e in eventslist:
            print(e)