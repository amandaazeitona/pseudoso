class Disco:

    def __init__(self, arquivos_lidos):
        self.blocos = [0]*arquivos_lidos['disco_blocos']
        self.arquivos = arquivos_lidos['arquivos']
        self.operacoes = arquivos_lidos['operacoes']
        self.tempo_processador = {}
        self.usuario_flag = {}
        self.arquivo_dono = {}
        self.__grava_arquivo_inicial()

    # encontra o primeiro espaço que caiba o arquivo recebido = first-fit
    def __procura_espaco_vazio(self, arquivo_tamanho):
        espaco_contiguo_vazio = 0
        espaco_vazio = 0
        for i in range(len(self.blocos)):
            if self.blocos[i]:
                espaco_vazio = 0
            else:
                espaco_vazio += 1
                if espaco_vazio > espaco_contiguo_vazio:
                    espaco_contiguo_vazio = espaco_vazio
                    if espaco_contiguo_vazio == arquivo_tamanho:
                        return i+1-arquivo_tamanho
        return (-1)

    # verifica qual o tempo de processador de um processo
    def __verifica_tempo_processador(self, PID):
        if self.tempo_processador[str(PID)] > 0:
            return(1)
        return(0)

    # serve pra que?
    def __verifica_processo(self, PID):
        if str(PID) in self.tempo_processador:
            return (1)
        return(0)

     # verifica se o processo é do tipo usuário ou núcleo
    def __eh_processo_usuario(self, PID):
        if self.usuario_flag[str(PID)]:
            return(1)
        return(0)

    # inicializa disco com arquivos iniciais?
    def __grava_arquivo_inicial(self):
        for arquivo in self.arquivos:
            for i in range(arquivo.inicio, arquivo.inicio+arquivo.tamanho):
                self.blocos[i] = arquivo.nome
        return 1

    # busca arquivos dentro do disco?
    def __procura_arquivo(self, nome):
        arquivo_tamanho = 0
        primeira_vez = 0
        arquivo_inicio = 0
        for i in range(len(self.blocos)):
            if(self.blocos[i] == nome):
                if not primeira_vez:
                    arquivo_inicio = i
                    primeira_vez = 1
                arquivo_tamanho += 1
        return(primeira_vez, arquivo_inicio, arquivo_tamanho)

    # grava qual processo é dono do arquivo recebido
    def __grava_arquivo_dono(self, PID, nome_arquivo):
        if nome_arquivo in self.arquivo_dono:
            return(0)
        else:
            self.arquivo_dono[nome_arquivo] = PID
            return(1)

    # verifica se o processo que tenta deletar é dono do arquivo
    def __eh_arquivo_dono(self, PID, nome_arquivo):
        if nome_arquivo in self.arquivo_dono:
            if self.arquivo_dono[nome_arquivo] == str(PID):
                return(1)
        return(0)

    # operação de inserir arquivo
    def __insere(self, operacao):
        offset = self.__procura_espaco_vazio(operacao.tamanho)
        if offset != -1:
            for i in range(offset, offset+operacao.tamanho):
                self.blocos[i] = operacao.nome
            return (offset)
        else:
            return (-1)

    # operação de deletar arquivo
    def __deleta(self, operacao):
        arquivo_encontrado, arquivo_inicio, arquivo_tamanho = self.__procura_arquivo(
            operacao.nome)
        if not arquivo_encontrado:
            ("O arquivo não existe!")
            return(0)
        for i in range(arquivo_inicio, arquivo_tamanho):
            self.blocos[i] = 0
        return(1)

    # ?
    def __executa_operacao(self, operacao):
        if self.__verifica_processo(operacao.PID):
            if self.__verifica_tempo_processador(operacao.PID):
                self.tempo_processador[str(operacao.PID)] -= 1
                if (not operacao.operacao_codigo and operacao.tamanho):
                    offset = self.__insere(operacao)
                    if not self.__grava_arquivo_dono(operacao.PID, operacao.nome):
                        return({'status': 'Falha', 'texto': 'Operação cancelada: existe um arquivo com o mesmo nome.'})
                    if offset != -1:
                        for bloco_ocupado in range(offset, offset+operacao.tamanho):
                            if bloco_ocupado == offset:
                                texto_blocos = 'blocos ' + str(bloco_ocupado)
                            else:
                                texto_blocos += ', ' + str(bloco_ocupado)
                        return({'status': 'Sucesso', 'texto': 'O arquivo ' + operacao.nome + ' foi criado pelo processo ' + str(operacao.PID) + ' | ' + texto_blocos + '.'})
                    else:
                        return({'status': 'Falha', 'texto': 'O arquivo '  + operacao.nome + ' não foi criado pelo processo ' + str(operacao.PID) + ' por falta de espaço.'})
                else:
                    if self.__eh_processo_usuario(operacao.PID):
                        if not self.__eh_arquivo_dono(operacao.PID, operacao.nome):
                            return({'status': 'Falha', 'texto': 'Operação cancelada: o processo não é dono do arquivo.'})
                    if self.__deleta(operacao):
                        return({'status': 'Sucesso', 'texto': 'O arquivo ' + operacao.nome + ' foi deletado pelo processo ' + str(operacao.PID) + '.'})
                    else:
                        return({'status': 'Falha', 'texto': 'O arquivo não existe!'})
            else:
                return({'status': 'Falha', 'texto': 'Operação não realizada: faltou tempo de processador'})
        else:
            return({'status': 'Falha', 'texto': 'O processo não existe!'})

    # ?
    def executa_operacoes(self, tempo_processador, usuario_flag):
        self.tempo_processador = tempo_processador
        self.usuario_flag = usuario_flag
        operacao_status = []
        for operacao in self.operacoes:
            operacao_status.append(self.__executa_operacao(operacao))
        return operacao_status
