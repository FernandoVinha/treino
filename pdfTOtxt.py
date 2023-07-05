import PyPDF2

def converter_pdf_para_txt(caminho_pdf, caminho_txt):
    with open(caminho_pdf, 'rb') as arquivo_pdf:
        leitor = PyPDF2.PdfReader(arquivo_pdf)
        total_paginas = len(leitor.pages)

        with open(caminho_txt, 'w') as arquivo_txt:
            for pagina in range(total_paginas):
                conteudo = leitor.pages[pagina].extract_text()
                arquivo_txt.write(conteudo)

    print(f'O PDF foi convertido para {caminho_txt} com sucesso!')

# Exemplo de uso
caminho_pdf = 'c.pdf'
caminho_txt = 'c.txt'
converter_pdf_para_txt(caminho_pdf, caminho_txt)
