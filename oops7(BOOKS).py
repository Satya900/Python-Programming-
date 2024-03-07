class Books :
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre
    
    def book(self):
        print("{} is the book written by {} and this belong to {} genre".format(self.title,self.author,self.genre))

book1 = Books("To kill a mockingbird","Harper Lee","Classic")
book2 = Books("The Great Gatsby","F.scott Fitzgerald","Fiction")
print(book1.book());
print(book2.book())