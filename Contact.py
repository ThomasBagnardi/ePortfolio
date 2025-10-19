from threading import Lock

# Contact class 
class Contact:

    # Variable initialization
    _id_generator = 0
    _lock = Lock()

    def _init_(self, first_name=None, last_name=None, number=None, address=None):
        with Contact._lock:
            Contact._id_generator += 1
            self.contactID = str(Contact._id_generator)
        self.firstName = first_name
        self.lastName = last_name
        self.number = number
        self.address = address

        # CONSTRUCTOR
        # This constructor will take the variables initialized above as parameters.
        # Theses parameters will be used to generate a new ID for contactID.
        # 
        # First and last name if blank will be labeled NULL if null or blank.
        # This is both as a placeholder and to protect data integrity.
        # If either first or last name is longer than 10 characters, truncate to only take first 10.
        # 
        # For number if not 10 characters the placeholder '55555555555' will be used as a placeholder.
        #
        # Address also checks for blank or null and uses NULL for placeholder. If more than 30
        # characters truncate to only take first 30 characters.
        class Contact:
            id_generator = 0

            def _init_(self, first_name, last_name, number, address):
                # CONTACTID
                # Contact ID is generated when the constructor is called. This variable is set as final
                # with no other getter or setter with no way to change it.
                # The id_generator is static to prevent duplicates across all contacts, this validation process prevents infiltration
                # and protects user data from being exploited elsewhere.
                self.contactID = str(Contact.id_generator)
                Contact.id_generator += 1

                # FIRSTNAME
                if first_name is None or first_name == "":
                    self.firstName = "NULL"
                # loop truncates for first 10 characters, preventing the misuse of any personal data.
                elif len(first_name) > 10:
                    self.firstName = first_name[:10]
                else:
                    self.firstName = first_name

                # LASTNAME
                if last_name is None or last_name == "":
                    self.lastName = "NULL"
                # loop truncates for first 10 characters, preventing the misuse of any personal data.
                elif len(last_name) > 10:
                    self.lastName = last_name[:10]
                else:
                    self.lastName = last_name

                # NUMBER
                if number is None or number == "" or len(number) != 10:
                    self.number = "5555555555"
                else:
                    self.number = number

                # ADDRESS
                if address is None or address == "":
                    self.address = "NULL"
               # Loop truncates for first 30 characters, preventing the misuse of any personal data.
                elif len(address) > 30:
                   self.address = address[:30]
                else:
                   self.address = address

        # GETTERS

        def get_contact_id(self):
            return self.contactID

        def get_first_name(self):
            return self.firstName

        def get_last_name(self):
            return self.lastName

        def get_number(self):
            return self.number

        def get_address(self):
            return self.address

        # SETTERS
        # Setters follow the same rules as constructor.
        def set_first_name(self, first_name):
            if first_name is None or first_name == "":
                self.first_name = "NULL"
            # Loop truncates for first 10 characters, preventing the misuse of any personal data.
            elif len(first_name) > 10:
                self.first_name = first_name [0:10]
            else:
                self.first_name = first_name

        def set_last_name(self, last_name):
            if last_name is None or last_name == "":
                self.last_name = "NULL"
            # Loop truncates for first 10 characters preventing, the misuse of any personal data.
            elif len(last_name) > 10:
                self.last_name = last_name[0:10]
            else:
                self.last_name = last_name

        def set_number(self, number):
            if number is None or number == "" or len(number) != 10:
                self.number = "5555555555"
            else:
                self.number = number

        def set_address (self, address):
            if address is None or address == "":
                self.address = "NULL"
            # Loop truncates for first 30 characters, preventing the misuse of any personal data.
            elif len(address) > 30:
                self.address = address[0:30]
            else:
                self.address = address


