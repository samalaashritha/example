#PROJECT-3
#get user email address
email=input("what is your mail address?:").strip()
#slice out user name
user=email[:email.index("@")]
#slice domain name
domain=email[email.index("@") +1:]
#format message
output="your username is {} and your domain is {}".format(user,domain)
#display output message
print(output)
