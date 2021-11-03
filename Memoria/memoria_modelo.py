import threading

# define os atributos da memória ram (onde são armazenados os processos que estão na fila de pronto)
class Memoria:
    def __init__(self, memoria_tamanho):
        self.memoria = [None]*memoria_tamanho
        self.usuario_offset = 64
        self.nucleo_offset = 0
        self.PID = 0
        self.memoria_controle = threading.Lock()
        self.memoria_cheia_usuario = threading.Lock()
        self.memoria_cheia_nucleo = threading.Lock()
        self.memoria_cheia_nucleo.acquire()
        self.memoria_cheia_usuario.acquire()

    # verifica se o processo recebido pela função cabe na memória ram
    def __verifica_espaco_memoria(self, offset, processo_tamanho, nucleo=0):
        if(nucleo and (processo_tamanho > 64)):
            return(0)
        elif(processo_tamanho+offset > len(self.memoria)):
            return(0)
        else:
            for index in range(offset, processo_tamanho+offset):
                if self.memoria[index] is not None:
                    if nucleo:
                        self.memoria_cheia_nucleo.acquire()
                    else:
                        self.memoria_cheia_usuario.acquire()
                    return(1)
        return(1)
    
    # grava processo do tipo usuário na memória ram
    # verifica se a memória ram está sendo utilizada por um processo por vez
    def aloca_processo_usuario(self, processo):
        self.memoria_controle.acquire()
        if self.__verifica_espaco_memoria(self.usuario_offset, processo.blocos_em_memoria):
            processo.PID = self.PID
            for index in range(self.usuario_offset, self.usuario_offset+processo.blocos_em_memoria):
                self.memoria[index] = processo.PID
            processo.offset = self.usuario_offset
            self.usuario_offset = self.usuario_offset+processo.blocos_em_memoria
            self.PID += 1
        else:
            print('Não foi possível alocar o processo em memória.')
            self.memoria_controle.release()
            return(0)
        self.memoria_controle.release()
        return(1)

    # apaga processo recebido pela função da memória ram (coloca 0's nas áreas ocupadas pelo processo)
    def desaloca_processo_usuario(self, processo):
        self.memoria_controle.acquire()
        primeira_vez = 1
        for index, espaco in enumerate(self.memoria):
            if espaco == processo.PID:
                self.memoria[index] = None
                if primeira_vez:
                    self.usuario_offset = index
                    primeira_vez = 0
        if self.memoria_cheia_usuario.locked():
            self.memoria_cheia_usuario.release()
        self.memoria_controle.release()

    # grava processo do tipo nucleo na memória ram
    # verifica se a memória ram está sendo utilizada por um processo por vez
    def aloca_processo_nucleo(self, processo):
        self.memoria_controle.acquire()
        if self.__verifica_espaco_memoria(self.nucleo_offset, processo.blocos_em_memoria, 1):
            processo.PID = self.PID
            for index in range(self.nucleo_offset, self.nucleo_offset+processo.blocos_em_memoria):
                self.memoria[index] = processo.PID 
            processo.offset = self.nucleo_offset
            self.nucleo_offset = self.nucleo_offset+processo.blocos_em_memoria
            self.PID += 1
        else:
            print('Não foi possível alocar o processo em memória.')
            self.memoria_controle.release()
            return(0)
        self.memoria_controle.release()
        return(1)

    # apaga processo recebido pela função da memória ram (coloca 0's nas áreas ocupadas pelo processo)
    def desaloca_processo_nucleo(self, processo):
        self.memoria_controle.acquire()
        primeira_vez = 1
        for index, espaco in enumerate(self.memoria):
            if espaco == processo.PID:
                self.memoria[index] = None
                if primeira_vez:
                    self.nucleo_offset = index
                    primeira_vez = 0
        if self.memoria_cheia_nucleo.locked():
            self.memoria_cheia_nucleo.release()
        self.memoria_controle.release()
