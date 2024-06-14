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

## 🤓 Perguntas Técnicas
### 2.1:
**Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.**
O método escolhido foi o Haar Cascade ele é um algorítmo para detectar determinados objetos em imagens. Assim, a função de cascata é treinada em imagens positivas e negativas, em que as positivas indicam tudo aquilo que é o que queremos encontrar e as negativas são os objetos que não queremos encontrar. É possível treinar sua função de cascata de modo personalizado, para que ela identifique um objeto específico, apesar de que nesse projeto foi utilizado um modelo pré-treinado. Desse modo, Ele tenta calcular para cada janela(parte da imagem)  se ela é positiva ou negativa, ou seja, se aquela janela poderia ou não ser uma parte do objeto que estamos procurando detectar.
### 2.2
**Considere as seguintes alternativas para resolver o problema de detecção de faces: HAAR Cascade, CNN, NN Linear, Filtros de correlação cruzada
Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.**
1) Haar Cascade
2) CNN
3) Filtros de correlação cruzada
4) NN LInear<br/>
A ordem escolhida foi baseada principalmente na viabilidade de aplicação no projeto, visto o perído de tempo. Desse modo, o Haar Cascade foi escolhido principalmente pela rapidez e eficiência e por já ter um modelo pré-treinado de detecção de faces. Por outro lado, o CNN seria bastante eficiente, no entanto não tem a rapidez que o Haar Cascade consegue oferecer por ser um sistema de análise mais robusto devido ao fato de ter uma rede neural mais profunda. Em seguida, os Filtros de Correlação Cruzada funcionam com uma imagem de entrada com um filtro projetado, e também oferece uma invariância ao deslocamento incorporado, ou seja, se a imagem de entrada é transladada com relação às de treinamento, o pico de saída será deslocado do mesmo valor, essa feature é o que coloca esse modelo na frente do NN Linear, o qual funciona realizando uma multiplicação da matriz dos dados de entrada com a matriz de pesos e adicionando o termo de polarização.
### 2.3
**Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.**
1) Filtros de Correlação Cruzada
2) CNN
3) Haar Cascade
4) NN LInear<br/>
Para o critério de detecção de emoções, os Filtros de Correlação Cruzada se destacam, pois devido ao seu funcionamento de imagem de entrada com um filtro projetado, ficaria mais fácil classificar uma face trsite de uam feliz por exemplo. Já o Haar Cascade teria bem mais erros se fosse usado nessa situação, pois ele trabalha com o modelo de imagens positivas e negativas, de modo que para ele seria muito fácil confundir uma face feliz com uma triste, ou apenas uma face com qualquer outra emoção detectada.
### 2.4
**A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?**
Não. Na aplicação em questão uma possível solução seria treinar o modelo baseado nos resultados do modelo anterior, mas isso sendo feito de modo contínua por meio de uma iteração, assim, a cada predição seria relaizada uma nova predição baseada na anterior.

