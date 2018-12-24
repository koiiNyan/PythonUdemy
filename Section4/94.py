# Remove the "s" from "https" and add another forward slash next to the
# existing slash, so the content looks like in the expected output.
#
# Expected output:
#
# http://www.google.com
# http://www.yahoo.com
# http://www.stackoverflow.com
# http://www.pythonhow.com


with open('urls.txt', 'r') as file:
    text = file.readlines()

with open('urls_corr.txt', 'w') as file:
    for line in text:
        line_replace = line.replace('s', '')
        line_add_replace = line_replace[:5] + '/' + line[6:]
        file.write(line_add_replace)
