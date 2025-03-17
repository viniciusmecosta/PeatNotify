from utils.email_sender import EmailSender

class EmailService:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_notifications(self, email_objects, level):
        success_count, failure_count = 0, 0

        for email_obj in email_objects:
            name = email_obj.name
            email = email_obj.email

            if self.email_sender.send(name, email, level):
                success_count += 1
            else:
                failure_count += 1

        return success_count, failure_count
