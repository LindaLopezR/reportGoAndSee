
import sys
import locale
from reportlab.platypus import *
from reportlab.lib import utils
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from time import *
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

styles = getSampleStyleSheet()

Company = "Company name"
Audit = "Nombre de la auditoria"
Status = "34%"
User = "Aaron Watters"
PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH = letter[0]
colwidths = ( PAGE_WIDTH-( 3*inch ), 1*inch )
data = (
    ( 'Tarea #1:', 'Completa' ),
    ( 'Tarea #2:', 'Completa' ),
    ( 'Tarea #3:', 'Completa' ),
    ( 'Tarea #4:', 'Completa' ),
)
GRID_STYLE = TableStyle(
    [('GRID', (0,0), (-1,-1), 0.25, colors.black),
    ('ALIGN', (1,1), (-1,-1), 'CENTER')]
)

# Formato de fecha
dbDtFormat = '%A, %d/%B/%Y %H:%M'
locale.setlocale(locale.LC_TIME, '')
reportDate = strftime(dbDtFormat, localtime() )

# Medidas logos
companyLogo = utils.ImageReader('company.png')
iGoSeeLogo = utils.ImageReader('logo.png')
companyLogo_width, companyLogo_height = companyLogo.getSize()
iGoSeeLogo_width, iGoSeeLogo_height = iGoSeeLogo.getSize()
aspectCompany = companyLogo_height / float(companyLogo_width)
aspectiGoSee = iGoSeeLogo_height / float(iGoSeeLogo_width)

def firstPage(canvas, doc):
    canvas.saveState()
    # Header
    canvas.setFont( 'Times-Roman', 16 )
    canvas.drawImage( companyLogo, 65, PAGE_HEIGHT-108,
                        width=65, height=(65 * aspectCompany ) )
    canvas.drawString(150, PAGE_HEIGHT-90, Company)
    canvas.line(50, 720, 550, 720)
    canvas.drawString(65, PAGE_HEIGHT-150, Audit)
    canvas.drawString(PAGE_WIDTH - (1.5 * inch), PAGE_HEIGHT-150, Status)
    # Foote3
    canvas.setFont( 'Times-Roman', 10 )
    canvas.drawString( 65, inch * 1.05, 'Gemba Walks Statistics Report' )
    canvas.drawString( PAGE_WIDTH - (2.8 * inch), inch * 1.05, reportDate )
    canvas.line(50, 70, 550, 70)
    canvas.drawString( 65, inch * 0.70, 'Pag. %d' % doc.page )
    canvas.drawString( 250, inch * 0.70, 'iGo&See Report Generator' )
    canvas.drawImage( iGoSeeLogo, PAGE_WIDTH - (1.7 * inch), 0.55 * inch,
                        width=35, height=(35 * aspectiGoSee ) )
    canvas.restoreState()

def laterPages(canvas, doc):
    canvas.saveState()
    # Footer
    canvas.setFont( 'Times-Roman', 10 )
    canvas.drawString( 65, inch * 1.05, 'Gemba Walks Statistics Report' )
    canvas.drawString( PAGE_WIDTH - (2.8 * inch), inch * 1.05, reportDate )
    canvas.line(50, 70, 550, 70)
    
    canvas.drawString( 65, 0.70 * inch, 'Pag. %d' % doc.page )
    canvas.drawImage( iGoSeeLogo, PAGE_WIDTH - (1.7 * inch), 0.55 * inch,
                        width=35, height=(35 * aspectiGoSee ) )
    canvas.restoreState()

def go():
    Elements.insert(0, Spacer(0,inch))
    doc = SimpleDocTemplate('report.pdf', rightMargin=60, leftMargin=60, topMargin=30, bottomMargin=75)
    doc.build(Elements, onFirstPage=firstPage, onLaterPages=laterPages)

Elements = []
# Estilos titulos
HeaderStyle = styles["Heading1"]
ParaStyle = styles["Normal"]

def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
    s = Spacer(0.2*inch, sep*inch)
    Elements.append(s)
    para = klass(txt, style)
    Elements.append(para)

def headerAudit(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
    s = Spacer(0.2*inch, sep*inch)
    Elements.append(s)
    para = klass(txt, style)
    Elements.append(para)

def tableList(item, colwidths, sep=0.3):
    s = Spacer(0.2*inch, sep*inch)
    Elements.append(s)
    t=Table(item)
    t = Table( data, colwidths )
    t.setStyle( GRID_STYLE )
    Elements.append(t)
    
header(User, sep=0.9, style=ParaStyle)
header(reportDate, sep=0.2, style=ParaStyle)
tableList(data, colwidths)

go()