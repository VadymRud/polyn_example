from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, FileResponse, Http404
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import Context
import pdfkit
import codecs
import os
from django.utils.encoding import smart_str
# from weasyprint import HTML
#
def html_to_pdf_view(request):
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }

    template = get_template("documentes/index.html")
    data = [1,2,3]
    context = Context({"paragraphs": data})  # data is the context data that is sent to the html file to render the output.
    html = template.render(context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf', options=options)
    try:
        return FileResponse(open('out.pdf', 'rb'), content_type='application/pdf')
        os.remove("out.pdf")  # remove the locally created pdf file.
    except FileNotFoundError:
        raise Http404()

    #return response  # returns the response.