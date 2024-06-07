# 📹 Youtube Video Summarizer

Este projeto é uma aplicação web desenvolvida com Streamlit que permite resumir vídeos do YouTube. Ele extrai a transcrição do vídeo e usa o modelo Generative AI da Google para gerar um resumo em pontos importantes.

##  Funcionalidades

-  Entrada de URL do YouTube.
-  Exibição da thumbnail do vídeo.
-  Extração da transcrição do vídeo.
-  Geração de resumo com Google Generative AI.

## ⚙️ Requisitos

-  Python 3.x
-  Streamlit
-  python-dotenv
-  google-generativeai
-  youtube-transcript-api

## 🛠️ Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/matcgoes/youtube-video-transcribe.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd youtube-video-transcribe
    ```
3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate # Para Linux/Mac
    .\venv\Scripts\activate  # Para Windows
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Crie um arquivo `.env` no diretório raiz do projeto e adicione a chave de API da Google:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## 🚀 Uso 

1. Execute a aplicação:
    ```bash
    streamlit run app.py
    ```
2. Abra o navegador e acesse `http://localhost:8501`.
3. Insira a URL do vídeo do YouTube que deseja resumir.
4. Clique no botão "Summarize it!" para gerar o resumo.