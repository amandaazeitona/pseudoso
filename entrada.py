from pathlib import Path

# lê arquivo files.txt
def files_leitura():
    from Arquivos.arquivo_modelo import Arquivo, ArquivoOperacao

    i = 0
    arquivos = []
    operacoes = []
    path = Path(__file__).parent / "files.txt"
    with path.open() as arquivo:
        for linha in arquivo:
            if(i < 2):
                if(i == 0):
                    disco_blocos = int(linha)
                else:
                    arquivos_numero = int(linha)
            elif(i < arquivos_numero + 2):
                arquivos.append(Arquivo(linha.split(', ')))
            else:
                operacoes.append(ArquivoOperacao(linha.split(', ')))
            i = i+1
    arquivos = {'disco_blocos': disco_blocos, 'arquivos_numero': arquivos_numero,
                'arquivos': arquivos, 'operacoes': operacoes}
    return(arquivos)

# lê arquivo processes.txt
def processes_leitura():
    from Processos.processo_modelo import Processo

    processos_objeto = []

    path = Path(__file__).parent / "processes.txt"
    with path.open() as arquivo:
        for processo in arquivo:
            processos_objeto.append(Processo(processo.split(', ')))
    return(processos_objeto)

