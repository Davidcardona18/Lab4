#David Cardona -  October 15, 2024
#Fixed variable name from authrs to authors.
#Corrected the for loop syntax to use author, date with .items().
#Updated the print statement to use an f-string for easier formatting.
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print(f"{author} died in {date}.")