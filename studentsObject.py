import pandas as pd
from src.infos import alunos_infos
from src.layout import create_report
dados_corrigidos = './assets/ranking.csv'
dados_brutos = './assets/dados_brutos.csv'
gabarito = './assets/gabarito_oficial.csv'
df_dadoscorrigido = pd.read_csv(dados_corrigidos)
df_dados_brutos = pd.read_csv(dados_brutos,dtype={'cpf': str})
df_gabarito = pd.read_csv(gabarito)

#print(df_dados_brutos.iloc[0,2])

media_geral ={
    "matemática":4.7,
    "portugues":6,
    "quimica":2.1,
    "história":2.7,
    "geografia":2.7,
    "física":1.4,
    "biologia":2.5,
    "filo-soci":1.14,
    "total_média":23.5
}





for linha in range(1,df_dadoscorrigido.shape[0]):
    tabela = []
    data = {}
    cpf_aluno = (df_dadoscorrigido.iloc[linha,0])
    nome_aluno = alunos_infos[cpf_aluno]
    data['name'] = nome_aluno
    data['cpf'] = cpf_aluno
    data['objective_score'] = df_dadoscorrigido.iloc[linha,1]
    data['subjects'] = [
        ["Matemática", f"{str(df_dadoscorrigido.iloc[linha,2])}/13", media_geral["matemática"]],
        ["Física", f"{str(df_dadoscorrigido.iloc[linha,7])}/6", media_geral["física"]],
        ["Português", f"{str(df_dadoscorrigido.iloc[linha,3])}/10", media_geral["portugues"]],
        ["Química", f"{str(df_dadoscorrigido.iloc[linha,4])}/5" , media_geral["quimica"]],
        ["Biologia", f"{str(df_dadoscorrigido.iloc[linha,8])}/5", media_geral["biologia"]],
        ["Geografia", f"{str(df_dadoscorrigido.iloc[linha,6])}/4", media_geral["geografia"]],
        ["História", f"{str(df_dadoscorrigido.iloc[linha,5])}/5" , media_geral["história"]],
        ["Filosofia-Sociologia", f"{str(df_dadoscorrigido.iloc[linha,9])}/2", media_geral["filo-soci"]],
        ["Total",f"{str(df_dadoscorrigido.iloc[linha,1])}/50",media_geral["total_média"]]
    ]
    linhaEstudante = df_dados_brutos.index[df_dados_brutos['cpf'] == cpf_aluno].to_list()
    print(cpf_aluno)
    print(linhaEstudante[0])
    for coluna in range(2,52):
        resposta = df_dados_brutos.iloc[linhaEstudante[0],coluna]
        gabarito = df_gabarito.iloc[coluna-2,0]
        if resposta == "NAO DETECTADO":
            resposta = "-"
        else:
            if resposta==gabarito:
                resposta = f'{resposta} ✔'
            else:
                resposta = f'{resposta} ✖'
        questoes = [str(coluna-1),gabarito,resposta]
        tabela.append(questoes)
    
    data['questions'] = tabela
    filepdf = f'./pdfoutput/{cpf_aluno}.pdf'
    create_report(data,filepdf)

print('concluido')    


