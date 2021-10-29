class Fila:
    def __init__(self):
        self.fila_nucleo = []
        self.fila_usuario = {"prioridade1": [], "prioridade2": [], "prioridade3": []}

    # para evitar starvation = aging
    def __atualiza_prioridade(self):
        self.fila_usuario['prioridade1'].extend(self.fila_usuario['prioridade2'])
        self.fila_usuario['prioridade2'] = self.fila_usuario['prioridade3']
        self.fila_usuario['prioridade3'] = []
    
    # insere processo na fila
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

    # quando um processo é removido da fila (a fila andou) as prioridades são atualizadas
    def remove_processo(self, memoria):
        if(len(self.fila_nucleo) > 0):
            processo = self.fila_nucleo.pop(0)
            self.__atualiza_prioridade()
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
