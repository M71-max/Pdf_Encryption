from PyPDF2 import PdfFileWriter, PdfFileReader

try:
    out = PdfFileWriter()

    file_path = input("Enter file name along with the path (E:\All Storage\Desktop\test_123.pdf): ")
    output_file = input("Enter output file name : ")
    file = PdfFileReader(file_path)

    num = file.numPages
    for pages in range(num):
        page = file.getPage(pages)
        out.addPage(page)

    password = input("Enter the password for your PDF file: ")
    out.encrypt(password)

    with open("output_file", "wb") as fl:
        out.write(fl)

except:
    print("Error! Either check your source location or try again.")
finally:
    print("\n Task successfully executed.")
