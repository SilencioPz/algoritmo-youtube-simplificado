#Por ser Orientado a Objeto (O.O.), tem a classe Video
class Video:
    def __init__(self, titulo, visualizacoes, likes, dislikes, comentarios):
        self.titulo = titulo
        self.visualizacoes = visualizacoes
        self.likes = likes
        self.dislikes = dislikes
        self.comentarios = comentarios

#Esta é a Classe Usuário, em que o algoritmo verificará o que é + acessado
class User:
    def __init__(self, historico):
        self.historico = historico  # Tudo o que você assiste

def videosRecomendados(videos, usuario):
    # Filtra o que você não assistiu
    videosNaoAssistidos = [video for video in videos if video.titulo not in usuario.historico]

    # Ordena vídeos não assistidos views (+ populares)
    videosOrdenados = sorted(videosNaoAssistidos, key=lambda video: video.visualizacoes, reverse=True)

    # Recomenda os 5 vídeos mais populares
    videosRecomendados = videosOrdenados[:5]

    return videosRecomendados

# Criando alguns vídeos
video1 = Video("Video 1", 30, 10, 5, 3)
video2 = Video("Video 2", 50, 20, 10, 8)
video3 = Video("Video 3", 100, 50, 17, 12)
video4 = Video("Video 4", 500, 150, 22, 100)
video5 = Video("Video 5", 1000, 250, 112, 225)

# Lista de todos os vídeos
videos = [video1, video2, video3, video4, video5]

# Usuário já assistiu vídeos 1 e 3
usuario = User(["Video 1", "Video 3"])

# Obtendo vídeos recomendados
recomendados = videosRecomendados(videos, usuario)

# Imprimindo os títulos dos vídeos recomendados
print('Vídeos recomendados: ')
for video in recomendados:
    print(video.titulo)