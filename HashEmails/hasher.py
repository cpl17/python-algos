#Creates a Hashtable with unique keys in each bucket

class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
        
    #Creates the Empty buckets

    def create_buckets(self):
        return [[] for _ in range(self.size)]
 

    # Uses built in hash fuction to create index of key
    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value) #update
        else:
            bucket.append((key,value))
    
    #Returns associated value with the key
    def get_val(self, key):

        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            return record_value
        else:
            return "No record found with that email address"

    #Deletes an item 
    def del_item(self, key):

        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
        else:
            return 'No record of provided email'


    # Represents object as concatenated string of buckets
    def __str__(self):
        return ''.join(str(item) for item in self.hash_table)