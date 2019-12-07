class ebook():
    def __init__(self, title, author, max, curr):
        self.is_on = False
        self.title = title
        self.author = author
        self.pagemax = max
        self.pagecurr = curr
    def open_ebook(self):
        self.is_on = True
    def close_ebook(self):
        self.is_on = False
    def page_up(self):
        if self.is_on==True:
            self.pagecurr+=1
        else:
            print("Książka jest zamknięta")
    def info(self):
        print(f"Tytuł: {self.title}, Autor: {self.author} \nNumer Strony: {self.pagecurr}/{self.pagemax}")


        

