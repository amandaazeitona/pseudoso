class Despachante:
    # define atributos do despachante
    def __init__(self):
        self.quantidade_instrucoes = {}
        self.usuario_flag = {}
    
    
    # o despachante cria novos processos
    # se o processo estiver sendo executado pela primeira vez (nº instrução = 1) suas infos são printadas na tela
    def processo_despacha(self, processo, CPU):
        CPU.acquire()
        if processo.numero_instrucao == 1:
            print('\nDespachante')
            print('PID: ' + str(processo.PID))
            print('Blocos: ' + str(processo.blocos_em_memoria))
            print('Offset: ' + str(processo.offset))
            print('Prioridade: ' + str(processo.prioridade))
            print('Tempo: ' + str(processo.quantidade_instrucoes))
            print('Scanner: ' + str(processo.recursos['scanner']))
            print('Impressoras: ' + str(processo.recursos['cod_impressora']))
            print('Modem: ' + str(processo.recursos['modem']))
            print('Dispositivos SATA: ' + str(processo.recursos['cod_disco']))
            if processo.prioridade:
                self.usuario_flag[str(processo.PID)] = 1
            else:
                self.usuario_flag[str(processo.PID)] = 0
            self.quantidade_instrucoes[str(processo.PID)] = processo.quantidade_instrucoes
            
        CPU.release()

    # executa o sistema de arquivos (operações de arquivos que serão executadas)
    def sistema_arquivos_executa(self, disco):
        print('\nSistema de arquivos')
        resultados = disco.executa_operacoes(self.quantidade_instrucoes, self.usuario_flag)
        for index, resultado in enumerate(resultados):
            print('Operação ' + str(index) + ' : ' + resultado['status'])
            print(resultado['texto'])
        print('\nMapa do disco:')
        print(disco.blocos)
