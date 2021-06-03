from random import choice
from string import ascii_lowercase as letters

class Generator():

    def __init__(self) -> None:
        self.domains = ['@yahoo.com','@gmail.com', '@aol.com']
        self.quotes = ['quote1', 'quote2', 'quote3', 'quote4']


    def generate_name(self):
        return ''.join(choice(letters) for i in range(10))

    def get_domain(self,list_of_domains):
        return choice(list_of_domains)

    def get_quotes(self,list_of_quotes):
        return choice(list_of_quotes)

    def generate_records(self, total_records):
        with open('data.txt','a') as to_write:
            for num in range(total_records):
                key = self.generate_name() + self.get_domain(self.domains)
                value = self.get_quotes(self.quotes)
                to_write.write(key + ':' + value + "\n")
            to_write.write('charlesl15@gmail.com:quote5\n')
