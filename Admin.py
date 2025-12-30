import Questions


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

    def view_all_events(self, events_list):
        print("\n=== ALL events ===")

        if len(events_list) == 0:
            print("no events available check later for updates.")
            return

        for e in events_list:
            print(e)

    def view_questions(self):
        # View and respond to user questions
        questions = Questions.get_unanswered_questions()

        if not questions:
            print("\nNo new questions from users.")
            return

        print(f"\n=== User Questions ({len(questions)} unanswered) ===")
        for q in questions:
            print(f"\nQuestion ID: {q['id']}")
            print(f"From: {q['user']}")
            print(f"Question: {q['question']}")
            print(f"Time: {q['timestamp']}")

            response = input("\nType response (or press Enter to skip, 'delete' to remove): ")

            if response.strip().lower() == "delete":
                if Questions.delete_question(q['id']):
                    print("Question deleted!")
                else:
                    print("Failed to delete question.")
            elif response.strip():
                if Questions.respond_to_question(q['id'], response):
                    print("Response sent!")
                else:
                    print("Failed to send response.")
            else:
                print("Skipped this question.")