class Fila:

    # define atributos da fila de processos
    # init função construtora
    def __init__(self):
        self.fila_nucleo = []
        self.fila_usuario = {"prioridade1": [], "prioridade2": [], "prioridade3": []}

    # para evitar starvation atualizamos a prioridade dos processos
    # quando o processo fica muito tempo sem ser utilizado a sua prioridade vai aumenta = aging
    # prioridade = 0 (núcleo); prioridade 1, 2, 3 (usuário); quanto menor o número maior a prioridade;
    def __atualiza_prioridade(self):
        prio2to1 = self.fila_usuario['prioridade2']#fila 2 vira prioridade 1
        prio3to2 = self.fila_usuario['prioridade3']#fila 3 vira prioridade 2
        self.fila_usuario['prioridade1'].extend(prio2to1)
        self.fila_usuario['prioridade2'] = prio3to2
        self.fila_usuario['prioridade3'] = []
    
    # insere processo na fila de processos
    def insere_processo(self, processo, memoria):
        if((processo.prioridade == 0) and (len(self.fila_nucleo) < 1000)):
            if memoria.aloca_processo_nucleo(processo):
                self.fila_nucleo.append(processo)
        elif((processo.prioridade == 1) and (len(self.fila_usuario["prioridade1"]) < 1000)):
            if memoria.aloca_processo_usuario(processo):
                self.fila_usuario["prioridade1"].append(processo)
        elif((processo.prioridade == 2) and (len(self.fila_usuario["prioridade2"]) < 1000)):
            if memoria.aloca_processo_usuario(processo):
                self.fila_usuario["prioridade2"].append(processo)
        elif((processo.prioridade == 3) and (len(self.fila_usuario["prioridade3"]) < 1000)):
            if memoria.aloca_processo_usuario(processo):
                self.fila_usuario["prioridade3"].append(processo)
        else:
            print("Não há espaço na fila.")
            return(0)
        return(1)

    # remove processo da fila de processos
    # quando um processo é removido da fila a prioridade de todos os processos é atualizada
    def remove_processo(self, memoria):
        if(len(self.fila_nucleo) > 0):
            processo = self.fila_nucleo.pop(0)#nao existe prioridade p processo de núcleo
           
            return(processo)
        elif(len(self.fila_usuario['prioridade1']) > 0):
            processo = self.fila_usuario['prioridade1'].pop(0)
            self.__atualiza_prioridade()
            return(processo)
        elif(len(self.fila_usuario['prioridade2']) > 0):
            processo = self.fila_usuario['prioridade2'].pop(0)
            self.__atualiza_prioridade()
            return(processo)
        elif(len(self.fila_usuario['prioridade3']) > 0):
            processo = self.fila_usuario['prioridade3'].pop(0)
            self.__atualiza_prioridade()
            return(processo)
        else:
            return(0)
