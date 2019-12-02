class University():
    def __init__(self):
        self.name = "UEK"
        self.fullname = "Uniwersytet Ekonomiczny w Krakowie"
    def set_name(self, new_name):
        self.name = new_name
    def set_fullname(self, new_name):
        self.fullname = new_name
    def print_name(self):
        print(self.name)
    def print_fullname(self):
        print(self.fullname)

        
Un = University()
Un.set_name("AGH")
Un.set_fullname("Akademia Górniczo Hutnicza")
Un.print_name()
Un.print_fullname()
