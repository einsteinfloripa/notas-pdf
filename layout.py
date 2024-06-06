#CODIGO GERADO PELO CHATGPT:
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
# Função para criar um relatório PDF
def create_report(data, filename):
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []
    
    # Título
    title = Paragraph("Relatório de Desempenho", styles['Title'])
    elements.append(title)
    
    # Dados do Aluno
    student_info = [
        ["Nome", data['name']],
        ["CPF", data['cpf']],
        ["Sala", data['room']]
    ]
    
    table = Table(student_info, colWidths=[100, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Pontuação Objetiva
    elements.append(Paragraph("Pontuação Objetiva", styles['Heading2']))
    elements.append(Paragraph(f"{data['objective_score']} / 60", styles['Normal']))
    
    # Desempenho por Matéria
    elements.append(Paragraph("Desempenho por Matéria", styles['Heading2']))
    subject_data = [["Matéria", "Você", "Geral"]] + data['subjects']
    
    table = Table(subject_data, colWidths=[100, 200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Resultado por questão
    elements.append(Paragraph("Resultado por questão", styles['Heading2']))
    question_results = [["Questão", "Gabarito", "Aluno", "Questão", "Gabarito", "Aluno"]] + data['questions']
    
    table = Table(question_results, colWidths=[50, 50, 50, 50, 50, 50])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Salvar PDF
    pdf.build(elements)

# Dados de exemplo
data = {
    'name': 'Sofia Silveira Yukimura Lopez',
    'cpf': '111.177.339-47',
    'room': 'Nise',
    'objective_score': 29,
    'subjects': [
        ["Matemática", "2", "4,61"],
        ["Física", "4", "3,17"],
        ["Química", "4", "2,89"],
        ["Biologia", "3", "3,81"],
        ["Geografia", "2", "2,47"],
        ["História", "4", "2,32"],
        ["Literatura", "4", "3,30"],
        ["Português", "6", "4,96"]
    ],
    'questions': [
        ["1", "A", "D", "14", "D", "E"],
        ["2", "ANULADA", "E", "15", "C", "C"],
        ["3", "D", "C", "16", "C", "C"],
        ["4", "C", "D", "17", "E", "E"],
        ["5", "C", "B", "18", "B", "D"],
        ["6", "D", "B", "19", "C", "D"],
        ["7", "ANULADA", "C", "20", "A", "A"],
        ["8", "C", "D", "21", "E", "C"],
        ["9", "C", "", "22", "C", "C"],
        ["10", "A", "B", "23", "E", "E"],
        ["11", "B", "D", "24", "C", "C"],
        ["12", "C", "", "25", "B", "A"],
        ["13", "D", "B", "26", "A", "A"],
        ["27", "C", "B", "39", "D", "C"],
        ["28", "C", "B", "40", "C", "C"],
        ["29", "D", "D", "41", "A", "A"],
        ["30", "C", "C", "42", "C", "C"],
        ["31", "C", "B", "43", "D", "D"],
        ["32", "D", "D", "44", "B", "D"],
        ["33", "ANULADA", "C", "45", "B", "E"],
        ["34", "C", "D", "46", "A", "A"],
        ["35", "D", "D", "47", "B", "B"],
        ["36", "B", "C", "48", "B", "B"],
        ["37", "D", "B", "49", "D", "C"],
        ["38", "D", "B", "50", "C", "C"],
        ["51", "E", "E", "57", "D", "C"],
        ["52", "A", "A", "58", "D", "D"],
        ["53", "B", "B", "59", "E", "E"],
        ["54", "A", "D", "60", "E", "D"],
        ["55", "B", "B", "", "", ""],
        ["56", "B", "A", "", "", ""],
    ]
}

# Cria o relatório PDF
path = "./pdfoutput/"
create_report(data, './pdfoutput/relatorio.pdf')
