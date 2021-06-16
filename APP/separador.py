import os

class Organizador():
    def __init__(self):
        self.diretorio_on = False
        self.imagens = ['.png','.jpg','.jpeg']
        self.videos = ['.mov','.mp4']
        self.documentos = ['.pdf','.docx','.py','.pyw','.txt']
    def create_directory(self,directory):
        if os.path.isdir(directory):
            for i in ('/Imagens','/Videos','/Documentos','/Outros'):
                try:
                    os.mkdir(directory+i)
                except:
                    ...
            self.diretorio_on = True
            self.diretorio = directory
            self.start()

        else:
            self.diretorio_on = False

    def start(self):
        if self.diretorio_on:
            lista = os.listdir(self.diretorio)
            for i in lista:
                if os.path.isfile(f'{self.diretorio}/{i}'):
                    try:
                        if i[i.index('.'):].lower() in self.imagens:
                            os.replace(f'{self.diretorio}/{i}',f'{self.diretorio}/Imagens/{i}')
                        elif i[i.index('.'):].lower() in self.videos:
                            os.replace(f'{self.diretorio}/{i}',f'{self.diretorio}/Videos/{i}')
                        elif i[i.index('.'):].lower() in self.documentos:
                            os.replace(f'{self.diretorio}/{i}',f'{self.diretorio}/Documentos/{i}')
                        else:
                            os.replace(f'{self.diretorio}/{i}',f'{self.diretorio}/Outros/{i}')
                    except:
                        ...

