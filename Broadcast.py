# Importa os módulos necessários
import http.server
import socketserver
from os import path

# Define as variáveis de configuração do servidor
my_host_name = 'localhost' # Define o nome do host
my_port = 8888 # Define a porta a ser usada pelo servidor
my_html_folder_path = '' # Define o caminho da pasta que contém os arquivos HTML

my_home_page_file_path = 'map.html' # Define o caminho do arquivo HTML que será a página inicial

# Define a classe MyHttpRequestHandler para lidar com as requisições HTTP
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    # Método para definir os cabeçalhos HTTP
    def _set_headers(self):
        self.send_response(200) # Define o código de resposta HTTP como 200 (OK)
        self.send_header('Content-Type', 'text/html') # Define o tipo de conteúdo como HTML
        self.send_header('Content-Length', path.getsize(self.getPath())) # Define o tamanho do conteúdo
        self.end_headers()

    # Método para obter o caminho do arquivo solicitado
    def getPath(self):
        if self.path == '/': # Se não foi especificado um arquivo, utiliza a página inicial
            content_path = path.join(my_html_folder_path, my_home_page_file_path)
        else:
            # Remove o parâmetro da URL e o primeiro caractere (/)
            content_path = path.join(my_html_folder_path, str(self.path).split('?')[0][1:])
        return content_path

    # Método para obter o conteúdo do arquivo
    def getContent(self, content_path):
        with open(content_path, mode='r', encoding='utf-8') as f:
            content = f.read() # Lê o conteúdo do arquivo
        return bytes(content, 'utf-8') # Retorna o conteúdo em bytes

    # Método para lidar com as requisições GET
    def do_GET(self):
        self._set_headers() # Define os cabeçalhos HTTP
        self.wfile.write(self.getContent(self.getPath())) # Envia o conteúdo do arquivo solicitado

# Cria uma instância da classe MyHttpRequestHandler
my_handler = MyHttpRequestHandler

# Cria um servidor HTTP na porta e host especificados, com o manipulador de requisições definido anteriormente
with socketserver.TCPServer(("", my_port), my_handler) as httpd:
    print("Http Server Serving at port", my_port) # Imprime uma mensagem indicando que o servidor está sendo executado
    httpd.serve_forever() # Inicia o servidor e aguarda as requisições
