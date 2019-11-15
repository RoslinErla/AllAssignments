class Item():
    def __init__(self,name,category):
        """Inits Item with the name and the category."""

        self.__name = name
        self.__category = category
    
    def __str__(self):
        """Creates a formatted string of the name and category."""

        return "Name: {}, Category: {}".format(self.__name,self.__category)
    
    def set_name(self, name):
        """Updates the name into the desired one."""

        self.__name = name
    
    def set_category(self, category):
        """Updates the category into the desired one."""

        self.__category = category

class Catalog():
    def __init__(self, name,):
        """Inits Catalog with the name of the catalog and a empty list."""

        self.__name = name
        self.__collection = list()
    
    def add(self, item):
        """Adds the item to the collection list."""
        
        self.__collection.append(item)

    def __str__(self):
        """Creates a string of the catalog name and the items in the collection list."""

        return_string = ("Catalog {}:\n".format(self.__name)) #Formatted string of the catalog name

        for items in self.__collection: 
            return_string += "\t" + items.__str__() + "\n" #Add the item to the return string with the tap and newline
        
        length = len(return_string)-1 #The length of the whole thing except the last newline.
        return_string = return_string[0:length] #Took out the last newline so we don't print it again

        return return_string
    

    def remove(self, item):
        """Removes the desired item."""
        self.__collection.remove(item)

    def set_name(self, name):
        """Updates the catalog name into a new desired one."""
        self.__name = name

    def find_item_by_name(self, name):
        """Checks if a name is in the collection list
           if it is we return the item connected to it
           else we return None."""

        for item in self.__collection:
            if item._Item__name == name:
                return item

    def clear(self):
        """Clears the collection list we had and leaves us with an empty list"""

        self.__collection = list()



