class Admin():
    def __init__(self):
        self.admin_id = None
        self.admin_password = None

    def set_admin_id(self, admin_id):
        self.admin_id = admin_id

    def get_admin_id(self):
        return self.admin_id

    def set_admin_password(self, admin_password):
        self.admin_password = admin_password

    def get_admin_password(self):
        return self.admin_password
    #hello
    def view_all_events(self, events_list):
        print("\n=== ALL events ===")

        if len(events_list) ==0:
            print("no events availabel check later for updates.")
            return
        
        for e in events_list:
            print(e)