
import sys
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
PAGE_HEIGHT=defaultPageSize[1]

styles = getSampleStyleSheet()

Company = "Company name"
Audit = "Nombre de la auditoria"
User = "Aaron Watters"


from reportlab.lib.units import inch

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.drawString(200, PAGE_HEIGHT-108, Company)
    canvas.line(50, 700, 550, 700)
    canvas.line(50, 80, 550, 80)
    canvas.drawString(inch, 0.75 * inch, "Page" )
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.line(50, 80, 550, 80)
    canvas.drawString(inch, 0.75 * inch, "Page" )
    canvas.restoreState()

def go():
    Elements.insert(0,Spacer(0,inch))
    doc = SimpleDocTemplate('report.pdf')
    doc.build(Elements,onFirstPage=myFirstPage, onLaterPages=myLaterPages)

Elements = []

HeaderStyle = styles["Heading1"] # XXXX
ParaStyle = styles["Normal"]

def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
    s = Spacer(0.2*inch, sep*inch)
    Elements.append(s)
    para = klass(txt, style)
    Elements.append(para)

header(Audit, sep=0.2, style=HeaderStyle)
header(User, sep=0.2, style=ParaStyle)
header("Fecha", sep=0.2, style=ParaStyle)

go()