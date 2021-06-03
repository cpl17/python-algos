from hash import AlgoHashTable
from gen_records import Generator


## Execution Code ## 

#Creates Hash Table and Generator
hash_table = AlgoHashTable(256)
gen = Generator()

#Fills buckets in Hash Table with key\value pairs from txt file
with open('data.txt') as f:
    if f.readline() == "":
        gen.generate_records(100)
    for line in f:
        key,value = line.split(':')
        hash_table.set_val(key,value)

#Test Methods
print(hash_table.get_val('charlesl15@gmail.com'))
print(hash_table.set_val('charlesl15@gmail.com','some new value'))
hash_table.del_item('charlesl15@gmail.com')
print(hash_table.get_val('charlesl15@gmail.com'))


