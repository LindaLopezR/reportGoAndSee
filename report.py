
import sys
import locale
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from time import *
from reportlab.rl_config import defaultPageSize

styles = getSampleStyleSheet()

Company = "Company name"
Audit = "Nombre de la auditoria"
User = "Aaron Watters"
PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH = letter[0]

from reportlab.lib.units import inch

def firstPage(canvas, doc):
    canvas.saveState()
    # Header
    canvas.setFont( 'Times-Roman', 9 )
    canvas.drawString(200, PAGE_HEIGHT-108, Company)
    canvas.line(50, 700, 550, 700)
    # Footer
    canvas.line(50, 80, 550, 80)
    canvas.drawString( 65, 0.75 * inch, 'Page %d' % doc.page )
    canvas.drawRightString( PAGE_WIDTH-inch, 0.75 * inch, reportDate )
    canvas.restoreState()

def laterPages(canvas, doc):
    canvas.saveState()
    # Footer
    canvas.line(50, 80, 550, 80)
    canvas.drawString( 65, 0.75 * inch, 'Page %d' % doc.page )
    canvas.drawRightString( PAGE_WIDTH-inch, 0.75 * inch, reportDate )
    canvas.restoreState()

def go():
    Elements.insert(0,Spacer(0,inch))
    doc = SimpleDocTemplate('report.pdf')
    doc.build(Elements,onFirstPage=firstPage, onLaterPages=laterPages)

Elements = []
# Estilos titulos
HeaderStyle = styles["Heading1"]
ParaStyle = styles["Normal"]
# Formato de fecha
dbDtFormat = '%A, %d/%B/%Y %H:%M'
locale.setlocale(locale.LC_TIME, '')
reportDate = strftime(dbDtFormat, localtime() )

def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
    s = Spacer(0.2*inch, sep*inch)
    Elements.append(s)
    para = klass(txt, style)
    Elements.append(para)

header(Audit, sep=0.2, style=HeaderStyle)
header(User, sep=0.2, style=ParaStyle)
header(reportDate, sep=0.2, style=ParaStyle)

go()