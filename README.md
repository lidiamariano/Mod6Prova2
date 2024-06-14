# Módulo 6 - Prova 2 - Detecção de faces 
![video-ezgif com-video-to-gif-converter](https://github.com/lidiamariano/Mod6Prova2/assets/123901342/7488f338-bea5-4962-bbe1-f4d36708669a)

## 🔍 Descrição
Esse projeto é capaz de dividir um video em frames, detectar as faces encontradas pelo modelo em cada frame e juntar os frames detectados em um video `.mp4`
## 💻 Estrutura do projeto
- **divide_frames.py**: Código capaz de pegar um video e dividí-lo em frames
- **detecta_frames.py**: Utilização do haarcascade,modelo pré-treinado para detecção de faces, para detectar as faces presentes em cada um dos frames
- **monta_video.py**: Por meio da biblioteca Open CV é possível fazer a junção de cada frame detectado em um video .mp4
## ⚙️ Instrução de execução
### Pré-requisitos
- Open CV
### Instalação
1) Clonagem do repositório <br/>
`git clone https://github.com/lidiamariano/Mod6Prova2`
2) Instação das Dependências <br/>
`pip install -r requirements.txt`






