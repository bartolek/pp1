class University():
    def __init__(self):
        self.name = "UEK"
    def set_name(self, new_name):
        self.name = new_name
    def print_name(self):
        print(self.name)

        
Un = University()
Un.set_name("AGH")
Un.print_name()
