import re
emails_with_new_lines = []
f = open('contracts.txt', 'r+')
content = f.read()

emails = re.findall(r"\S+@\S+", content)
for email in emails:
    emails_with_new_lines.append(email + "\n")

out = open("Clean_Emails.txt", "w")


out.writelines(emails_with_new_lines)

f.close()
out.close()