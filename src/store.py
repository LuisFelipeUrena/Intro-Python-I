class Store:
    def __init__(self,name,departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        return f'welcome to {self.name}'        

class Department:
    def __init__(self,id,name,product):
        self.id = id
        self.name = name
        self.product = product
    
store  = Store('la sirena',3)
# loop forever while the user is browsing thru departments
# use the input function to prompt the user to select a kind of
# department to browse. 

while True:
    print('Welcome to the store')       