

import random
import string

def create_random_str(len_str=()):
    len_str = (random.randint(min_limit, max_limit))
    alpabet = string.ascii_lowercase
    rand_list = [random.choice(alpabet) for _ in range(len_str)]
    return "".join(rand_list)

min_limit = 5
max_limit = 7
str = create_random_str()
# print(str)

names = "arrow", "williams", "funny", "king"
domains = "com", "ua", "ru", "net"

def create_email ():
    new_email = create_email.join("new_name",".","number","@","str", "new_domain")


number = random.randint (100,999)

names = "arrow", "williams", "funny", "king"
new_name = random.choice (names)

domains = "com", "ua", "ru", "net"
new_domain = random.choice (domains)

print(new_email)