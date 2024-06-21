import rpyc

class ServerRPyC(rpyc.Service):
    def on_connect(self, conn):
        """ 
        Metodo quando um cliente se conecta ao servidor. 
        """
        print("Servidor conectado")

    def on_disconnect(self, conn):
        """ 
        Metodo quando um cliente se desconecta do servidor. 
        """
        print("Servidor desconectado")

    def exposed_void_operation(self):
        """ 
        Metodo void que não retorna nenhum valor. 
        """
        pass

    def exposed_long_operation(self, value):
        """ 
        Metodo que retorna o valor long recebido como argumento. 
        """
        return value

    def exposed_long_batch_operation(self, *args):
        """ 
        Metodo que recebe varios longs como argumentos e retorna a soma deles.
        """
        return sum(args)

    def exposed_string_operation(self, value):
        """ 
        Metodo que retorna a string recebida como argumento.
        """
        return value
    
    def exposed_json_operation(self, value):
        """ 
        Metodo que retorna o objeto JSON recebido como argumento.
        """
        return value

    def exposed_complex_operation(self, value):
        """ 
        Metodo que retorna o objeto complexo recebido como argumento.
        """
        return value


if __name__ == "__main__":
    # Inicia um servidor RPyC usando a classe ServerRPyC, na porta 18861
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(ServerRPyC, port=18861)
    server.start()
