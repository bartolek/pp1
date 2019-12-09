class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        x=0
        message2 = " "
        for i in message:
            if x==0:
                message2+=i.upper()
                x+=1
            else:
                message2+=i
        self.message = message
    def __str__(self):
        print(f"{self.message}")
        
m = Message()
m.set_message("CZeść!")