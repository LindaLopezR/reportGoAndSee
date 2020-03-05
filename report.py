
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
Address = "Adress Company"
Audit = "Nombre de la auditoria"
Status = "34%"
User = "Aaron Watters"
PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH = letter[0]

badIcon = Image('bad.png')
badIcon.drawHeight = 0.25*inch*badIcon.drawHeight / badIcon.drawWidth
badIcon.drawWidth = 0.25*inch
successIcon = Image('success.png')
successIcon.drawHeight = 0.25*inch*successIcon.drawHeight / successIcon.drawWidth
successIcon.drawWidth = 0.25*inch

colwidths = ( PAGE_WIDTH-( 3*inch ), 1*inch )

GRID_HEADER = TableStyle(
  [
    # Encabezado
    ('GRID', (0,0), (-1,-1), 1, colors.transparent),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lemonchiffon),
    ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('ALIGN', (1, 0), (-1,-0), 'CENTER'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
    ('TOPPADDING', (0, 0), (-1, 0), 15),
  ]
)
GRID_TASKS = TableStyle(
  [
    ('GRID', (0, 0), (-1,-1), 1, colors.transparent),
    ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.black),
    ('LINEABOVE',(0,0), (-1,0), 1.5, colors.black),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('ALIGN', (1, 0), (-1,-0), 'CENTER'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('TOPPADDING', (0, 0), (-1, 0), 12),
  ]
)
GRID_CONTENT = TableStyle(
  [
    ('GRID', (0, 0), (-1,-1), 1, colors.transparent),
    ('LINEBELOW', (0, 0), (-1, -1), 0.75, colors.gray),
    ('ALIGN', (1, 0), (-1, -0), 'CENTER'),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 12),
    ('TOPPADDING', (0, 1), (-1, -1), 12),
    ('LEFTPADDING', (0, 1), (-1, -1), 35)
  ]
)

# Formato de fecha
dbDtFormat = '%A, %d/%B/%Y %H:%M'
# locale.setlocale(locale.LC_ALL, '')
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
  canvas.setFont( 'Helvetica', 16 )
  canvas.drawImage( companyLogo, 65, PAGE_HEIGHT-108,
                      width=65, height=(65 * aspectCompany ) )
  canvas.drawString(150, PAGE_HEIGHT-85, Company)
  canvas.setFont( 'Helvetica', 12 )
  canvas.drawString(150, PAGE_HEIGHT-105, Address)
  canvas.line(50, 720, 550, 720)
  canvas.setFont( 'Helvetica', 16 )
  canvas.drawString(65, PAGE_HEIGHT-150, Audit)
  canvas.drawString(PAGE_WIDTH - (1.5 * inch), PAGE_HEIGHT-150, Status)
  # Foote3
  canvas.setFont( 'Helvetica', 10 )
  canvas.drawString( 65, inch * 1.05, 'Gemba Walks Statistics Report' )
  canvas.drawString( PAGE_WIDTH - (3.1 * inch), inch * 1.05, reportDate )
  canvas.line(50, 70, 550, 70)
  canvas.drawString( 65, inch * 0.70, 'Pag. %d' % doc.page )
  canvas.drawString( 250, inch * 0.70, 'iGo&See Report Generator' )
  canvas.drawImage( iGoSeeLogo, PAGE_WIDTH - (1.45 * inch), 0.55 * inch,
                      width=35, height=(35 * aspectiGoSee ) )
  canvas.restoreState()

def laterPages(canvas, doc):
  canvas.saveState()
  # Footer
  canvas.setFont( 'Helvetica', 10 )
  canvas.drawString( 65, inch * 1.05, 'Gemba Walks Statistics Report' )
  canvas.drawString( PAGE_WIDTH - (2.8 * inch), inch * 1.05, reportDate )
  canvas.line(50, 70, 550, 70)
  canvas.drawString( 65, 0.70 * inch, 'Pag. %d' % doc.page )
  canvas.drawImage( iGoSeeLogo, PAGE_WIDTH - (1.2 * inch), 0.55 * inch,
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

def tableList(item, styleTable, colTable, sep=0.3):
  s = Spacer(0.2*inch, sep*inch)
  Elements.append(s)
  t = Table( item, colTable )
  t.setStyle( styleTable )
  Elements.append(t)

# Ejemplo de location
evidenceImg = Image('evidence.jpg')
evidenceImg.drawHeight = 2*inch*evidenceImg.drawHeight / evidenceImg.drawWidth
evidenceImg.drawWidth = 2*inch

locations =  [
  ['Location #1', '30%'],
]
tasks = [
  ['Tarea #1', successIcon],
]
evidences = [
  [evidenceImg],
  ['Evidencia #2'],
]
# ----
  
header(User, sep=0.9, style=ParaStyle)
header(reportDate, sep=0.2, style=ParaStyle)
tableList(locations, GRID_HEADER, colwidths)
tableList(tasks, GRID_TASKS, colwidths, sep=0 )
tableList(evidences, GRID_CONTENT, ( PAGE_WIDTH-( 2*inch )), sep=0 )

go()
