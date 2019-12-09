class Music():
    def __init__(self, wykonawca, tytuł, album, rok):
        self.wykonawca = wykonawca
        self.tytuł = tytuł
        self.album = album
        self.rok = rok
    def __str__(self):
        return f"Wykonawca: {self.wykonawca} \nUtwór: {self.tytuł} \nAlbum: {self.album} \nRok: {self.rok}\n"
    


print(Music("Dawid Podsiadło", "Nie ma fal", "Małomiasteczkowy", "2018"))
print(Music("Twenty One Pilots", "Trench", "Chlorine", "2018"))
print(Music("Twenty One PIlots", "Blurryface", "Ride", "2015"))