# Importa os módulos necessários
import folium
import webbrowser

# Define a classe Map
class Map:
    # Define o construtor da classe, que recebe a localização central e o zoom inicial do mapa
    def __init__(self, center, zoom_start):
        self.center = center # Armazena a localização central do mapa
        self.zoom_start = zoom_start # Armazena o zoom inicial do mapa
    
    # Método para exibir o mapa
    def showMap(self):
        # Cria o objeto Map do folium
        my_map = folium.Map(location=self.center, zoom_start=self.zoom_start)

        # Adiciona marcadores ao mapa com suas respectivas informações
        folium.Marker(location=[-22.90517,-43.13245], popup='UFF (Casa do Adriano)', icon=folium.Icon(color='red')).add_to(my_map)
        folium.Marker(location=[-22.909765, -43.1163], popup='Baia de Guanabara / Águas da praia de Icaraí / Oxigenação da água : 8.20 PPM / Opacidade da água : 60%', icon=folium.Icon(color='red')).add_to(my_map)
        folium.Marker(location=[-22.9050, -43.2080], popup='Meu marcador 3', icon=folium.Icon(color='red')).add_to(my_map)

        # Salva o mapa em um arquivo HTML
        my_map.save("map.html")

        # Abre o arquivo HTML no navegador padrão do sistema
        webbrowser.open("map.html")

# Define as coordenadas da localização central do mapa
coords = [-22.9042977,-43.1165879]

# Cria uma instância da classe Map, passando as coordenadas e o zoom inicial
map = Map(center=coords, zoom_start=13)

# Exibe o mapa
map.showMap()
