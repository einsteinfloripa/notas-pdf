#CODIGO GERADO PELO CHATGPT:
from reportlab.lib.pagesizes import A4

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image


# Função para criar um relatório PDF


média_geral ={
    "matemática":4.7,
    "portugues":6,
    "quimica":2.1,
    "história":2.7,
    "geografia":2.7,
    "física":1.4,
    "biologia":2.5,
    "filo-soci":1.14,
    "total_média":23.5
}\
    

def create_report(data, filename):
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    
    #adicionando imagem
    image = Image("./assets/udesc.png")
    image.drawHeight = 150  # altura da imagem
    image.drawWidth = 200   # largura da imagem
    image.hAlign = 'CENTER' # alinha a imagem ao centro
    elements.append(image)
    
    # Título
    
    # Dados do Aluno
    student_info = [
        ["Nome", data['name']],
        ["CPF", data['cpf']],
    ]
    table = Table(student_info, colWidths=[100, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    
    # Desempenho por Matéria
    estilo = styles['Heading2']
    estilo.alignment = 1
    elements.append(Paragraph("Desempenho por Matéria", estilo))
    subject_data = [["Matéria", "Totais de acerto: ", "Média geral"]] + data['subjects']
    
    table = Table(subject_data, colWidths=[100, 200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Resultado por questão
    question_results = [["Questão", "Gabarito", "Aluno"]] + data['questions']
    
    table = Table(question_results, colWidths=[50, 50, 50, 50, 50, 50])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Salvar PDF
    pdf.build(elements)

# Dados de exemplo

data = {
    'name': 'Sofia Silveira Yukimura Lopez',
    'cpf': '111.177.339-47',
    'objective_score': 29,
    'subjects': [
        ["Matemática", "2", "4,61"],
        ["Física", "4", "3,17"],
        ["Química", "4", "2,89"],
        ["Biologia", "3", "3,81"],
        ["Geografia", "2", "2,47"],
        ["História", "4", "2,32"],
        ["Literatura", "4", "3,30"],
        ["Português", "6", "4,96"],
        ["Total",'29',média_geral["total_média"]]
    ],
    'questions': [
        ["1", "A", "D"],
        ["2", "ANULADA", "E"],
        ["3", "D", "C"],
        ["4", "C", "D"],
        ["5", "C", "B"],
        ["6", "D", "B"],
        ["7", "ANULADA", "C"],
        ["8", "C", "D"],
        ["9", "C", ""],
        ["10", "A", "B"],
        ["11", "B", "D"],
        ["12", "C", ""],
        ["13", "D", "B"],
        ["14", "D", "E"],
        ["15", "C", "C"],
        ["16", "C", "C"],
        ["17", "E", "E"],
        ["18", "B", "D"],
        ["19", "C", "D"],
        ["20", "A", "A"],
        ["21", "E", "C"],
        ["22", "C", "C"],
        ["23", "E", "E"],
        ["24", "C", "C"],
        ["25", "B", "A"],
        ["26", "A", "A"],
        ["27", "C", "B"],
        ["28", "C", "B"],
        ["29", "D", "D"],
        ["30", "C", "C"],
        ["31", "C", "B"],
        ["32", "D", "D"],
        ["33", "ANULADA", "C"],
        ["34", "C", "D"],
        ["35", "D", "D"],
        ["36", "B", "C"],
        ["37", "D", "B"],
        ["38", "D", "B"],
        ["39", "D", "C"],
        ["40", "C", "C"],
        ["41", "A", "A"],
        ["42", "C", "C"],
        ["43", "D", "D"],
        ["44", "B", "D"],
        ["45", "B", "E"],
        ["46", "A", "A"],
        ["47", "B", "B"],
        ["48", "B", "B"],
        ["49", "D", "C"],
        ["50", "C", "C"],
        ["51", "E", "E"],
        ["52", "A", "A"],
        ["53", "B", "B"],
        ["54", "A", "D"],
        ["55", "B", "B"],
        ["56", "B", "A"],
        ["57", "D", "C"],
        ["58", "D", "D"],
        ["59", "E", "E"],
        ["60", "E", "D"]
    ]
}

# Cria o relatório PDF
path = "./pdfoutput/"
create_report(data, './pdfoutput/relatorio.pdf')
