# define os atributos dos arquivos
# init função construtora
class Arquivo:
    def __init__(self, arquivo_dados):
        self.nome = arquivo_dados[0]
        self.inicio = int(arquivo_dados[1])
        self.tamanho = int(arquivo_dados[2])


# define os atributos das operações de arquivos (cria e deleta)
class ArquivoOperacao:
    def __init__(self, operacao_dados):
        self.PID = int(operacao_dados[0])
        self.operacao_codigo = int(operacao_dados[1])
        self.nome = operacao_dados[2].rstrip()
        if(len(operacao_dados) == 4):
            self.tamanho = int(operacao_dados[3])
        else:
            self.tamanho = 0
