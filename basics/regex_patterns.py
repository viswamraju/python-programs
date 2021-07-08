import re


def find_ip(ip):
    pattern = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-1][0-9]?)''')
    ips = re.search(pattern, ip)
    if ips:
        print(ips.group())
    else:
        print("Not found")

def search_for_string(search_string, input_string):
    pattern = re.compile(search_string)
    match = re.search(pattern, input_string)
    if match:
        print(match.group())
    else:
        print("Not found")


def found_a_pattern(input_string):
    # any thing in paranthesis
    pattern = re.compile("(\(.*\))")
    match = re.search(pattern, input_string)
    if match:
        print(match.group())
    else:
        print("Not found")


def case_sensitive_search(pattern, input_string, case=False):
    if case:
        pattern = re.compile(pattern)
    else:
        pattern = re.compile(pattern, re.IGNORECASE)
    match = re.search(pattern, input_string)
    if match:
        print(match.group())
    else:
        print("Not found")



# case_sensitive_search("[a-z]+\.[a-z]{1,3}", "My website is google.com. Another one is Yahoo.com")

def find_phoneNumber(in_str):
    pattern = re.compile("(\d{3}-\d{3}-\d{3})\D")
    match = re.search(pattern, in_str)
    if match:
        print(match.group())
    else:
        print("Not found")

# find_phoneNumber("My phone is 123-238-456 5")

def find_salutation(input_str):
    pattern = re.compile("(M(r|s)\.?\s\w+)")
    match = re.match(pattern, input_str)
    if match:
        print(match.group())
    else:
        print("Not found")

# find_salutation("Mr viswam raju")

def find_email(pattern, input_str):
    pattern = re.compile(pattern)
    match = re.findall(pattern, input_str)
    if match:
        print(match)
    else:
        print("Not found")

# find_email("[a-zA-Z]+@[a-z]+\.\w+", "My mail address is viswamraju@gmail.com and my another email is "
#                                         "vbogaraj@cisco.com")

def match_url(pattern, input_str):
    pattern = re.compile(pattern)
    match = re.findall(pattern, input_str)
    if match:
        print(match)
    else:
        print("Not found")

match_url("https?:\/\/www\.\w+\.(\w+)", "Urls: https://www.facebook.com,  http://www.google.in")



