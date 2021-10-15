from errors import *

domains = {"com", "bg", "org", "net"}

email = input()
while email:
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    email_list = email.split("@")
    if len(email_list) > 2:
        raise MustContainOneAtSymbolError("Email must contain one @ symbol")

    name, domain_name = email_list
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." not in domain_name:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    domain_parts = domain_name.split(".")
    domain = domain_parts[-1]
    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if "" in domain_parts:
        raise InvalidDomainError("Incorrect subdomain name")

    print("Email is valid")
    email = input()





