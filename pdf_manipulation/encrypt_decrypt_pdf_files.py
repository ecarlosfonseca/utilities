from PyPDF2 import PdfFileWriter, PdfFileReader

"""
Encrypting pdf with password
"""

# creating pdf writer, reader instances
writer = PdfFileWriter()

# reading the file
reader = PdfFileReader('normal_file.pdf')

# get all pages in writer
for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))

# encrypting file
writer.encrypt('password')

# creating the encripted file 
with open(f'encrypted_file.pdf', 'wb') as final_file:
    writer.write(final_file)
    file.close()

"""
Decrypting pdf with password
"""

# reading the encrypted file
reader = PdfFileReader('encrypted_file.pdf')

# checking encryption
if reader.isEncrypted:

    # decrypting file
    reader.decrypt("password")

    # reading all pages
    for page in range(reader.numPages):
        writer.addPage(reader.getPage(page))

    # creating decrypted file
    with open(f'decrypted_file.pdf', 'wb') as final_file:
        writer.write(final_file)
        final_file.close()
else:
    pass

