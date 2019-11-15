#Write a program that asks the user for email addresses, 
# one at a time (until the user inputs 'q'), 
# puts them into a list and then prints out a list of tuples of usernames and domains.

def get_emails():
    email_list = []
    email = input("Email address: ")
    while email != "q":
        email_list.append(email)
        email = input("Email address: ")
    return email_list

def get_names_and_domains(emails):
    email_list = []
    for elements in emails:
        elements = elements.replace("@"," ")
        email, domain = elements.split()
        new_tuple = (email, domain)
        email_list.append(new_tuple)
    return email_list


email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)