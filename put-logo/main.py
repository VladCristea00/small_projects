import PyPDF2

template = PyPDF2.PdfFileReader(open('plan_alimentar.pdf', 'rb'))
logo = PyPDF2.PdfFileReader(open('vladcristea-logo2.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(logo.getPage(0))
    output.addPage(page)

    with open('logo_output.pdf', 'wb') as file:
        output.write(file)
