class Email:
    """Every email object has 3 instance attributes:
    the message, the sender name, and the recipient name.
    """

    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients,
    which is a dictionary that associates client names
    with client objects.
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of
        the client it is addressed to."""
        try:
            recipient = self.clients[email.recipient_name]
            recipient.inbox.append(email)
        except:
            return "We could not send the message :("
        return "Message Sent :)"

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds
        them to the clients instance attribute."""
        self.clients[client_name] = client

    def show_my_clients(self):
        print("My list of clients: ")
        for client in self.clients.keys():
            print(f"\t{client}")


class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server(which
    is used to send emails out to other clients), and inbox
    (a list of all emails the client has received)."""

    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server
        server.register_client(self, name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client."""
        email = Email(msg, self.name, recipient_name)
        return self.server.send(email)

    def show_my_emails(self):
        if len(self.inbox) >= 1:
            print(
                f"{self.name}'s inbox [Emails: {len(self.inbox)}] ~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            )
            for num, email in enumerate(self.inbox):
                print(
                    f"{num} => \tFrom: {email.sender_name}\n\tTo: {email.recipient_name}\n\tMessage: {email.msg}\n"
                )
        else:
            print(f"{self.name}'s mailbox is empty!")

    def delete_email(self, email_number):
        try:
            self.inbox.pop(email_number)
        except:
            return "Try deleting that email later $$"


server = Server()
c1 = Client(server, "Vipul")
c2 = Client(server, "Anne")
print(float(server))
print(repr(c1))
print(repr(c2))


# # sending some emails
# c1.compose("Hey, Anne! How ya doing?", "Anne")
# c1.compose("Reply me pls anneenennene", "Anne")
# c1.compose("mail to myself", "Vipul")
# c2.compose("Finally replying", "Vipul")

# # checking inboxes
# c2.show_my_emails()
# c1.show_my_emails()

# email deletion testing
# c1.delete_email(0)
# c2.delete_email(1)
# c2.show_my_emails()
# c1.show_my_emails()