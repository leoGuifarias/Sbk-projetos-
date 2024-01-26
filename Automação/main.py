import pandas as pd
from urllib import request, error
from PyPDF2 import PdfReader
import sys
from pathlib import Path



def readExcel(caminho_excel):
    dados_excel = pd.read_excel(caminho_excel,sheet_name=1, skiprows=2)
    for indice, linha in dados_excel.iterrows():
        Nr_Processo = linha[0]
        link = linha[1]
        if len(link) > 50:
            Nr_Processo = Nr_Processo.replace('-', '')
            Nr_Processo = Nr_Processo + '_' + str(indice)
            baixarArquivos(link,Nr_Processo)
        else:
            print("Link inválido {}".format(link))
            Informacao = "Url inválida {}".format(Nr_Processo)
            gerarTxt(Informacao)


def baixarArquivos(file_url,Nr_Processo):
    file = r'C:\Users\DELL\Desktop\KURRIER\{}.pdf'.format(Nr_Processo)
    try:
        request.urlretrieve(file_url, file)
        print(f"O arquivo foi baixado com sucesso em: {file}")
        Informacao = (f"O arquivo foi baixado com sucesso em: {file}")
        LerPdf(file)
        gerarTxt(Informacao)
        LerPdf(file)
    except error.URLError as e:
        print(f"Erro ao baixar o arquivo. Verifique a URL. Detalhes: {e}")
    except Exception as e:
        print(f"Erro desconhecido: {e}")



def gerarTxt(texto):
        #with open(arquivo_log + '.txt', 'a') as arquivo_log:
        with open('LogProcessamento_log.txt', 'a') as arquivo_log:
            arquivo_log.write(texto + '\n')


def gerarTxtInformacoes(texto):
    # with open(arquivo_log + '.txt', 'a') as arquivo_log:
    with open('Informacoes.txt', 'a') as arquivo_log:
        arquivo_log.write(texto + '\n')



def CriarTxt(texto,arquivo):
    with open(str(arquivo)+'.txt', 'a',encoding='utf-8') as arquivo_log:
        arquivo_log.write(texto + '\n')



def obter_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def LerPdf(file):
    with open(file, 'rb') as arquivo_pdf:
        leitor_pdf = PdfReader(arquivo_pdf)
        num_paginas = len(leitor_pdf.pages)
        textoCompleto = ''
        for pagina_numero in range(num_paginas):
            pagina = leitor_pdf.pages[pagina_numero]
            texto_pagina = pagina.extract_text()
            textoCompleto += texto_pagina
          
        caminho_path = Path(file)
        CriarTxt(textoCompleto,caminho_path)
        dados = f"Arquivo PDF {caminho_path.stem}.pdf contém {num_paginas} páginas e {len(textoCompleto)} caracteres."
        gerarTxtInformacoes(dados)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    readExcel(r"C:\Users\leonardo.farias\Desktop\POC BRADESCO\SBK CADASTRO AUTOMATICO 18.12.xlsx")




if __name__ == '__main__':
   pass