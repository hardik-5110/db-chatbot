from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap


def export_text_to_pdf(text,filename):
    c = canvas.Canvas(filename,pageCompression=A4)
    width,height = A4

    x_margin = 25
    y_margin = 25
    line_height = 14

    max_width = int((width-2*x_margin)/7)
    lines = []
    for paragraph in text.split("\n"):
        lines.extend(textwrap.wrap(paragraph, width=max_width))
        lines.append("")  

    y = height - y_margin
    for line in lines:
        if y < y_margin:
            c.showPage()
            y = height - y_margin
        c.drawString(x_margin, y, line)
        y -= line_height

    c.save()