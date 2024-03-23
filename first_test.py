import cmd

class AirBnBCLI(cmd.Cmd):
    prompt = 'AirBnB> '

    def do_list_properties(self, args):
        """List all available properties"""
        # Logic to retrieve and display properties
        print("Listing all properties...")

    def do_book_property(self, args):
        """Book a property"""
        # Logic to book a property
        print("Booking property...")

    def do_quit(self, args):
        """Exit the program"""
        print("Exiting...")
        return True

if __name__ == '__main__':
    cli = AirBnBCLI()
    cli.cmdloop("Welcome to the AirBnB clone project!")
