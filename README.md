# YouTube Music Service

O YouTube Music Service é um microserviço desenvolvido em Python com o framework Flask que permite pesquisar músicas no YouTube e retornar os resultados encontrados. O projeto segue uma arquitetura limpa (clean architecture), garantindo uma separação clara das responsabilidades e facilitando a manutenção e testabilidade do código.

## Pré-requisitos

Antes de começar, verifique se o seguinte software está instalado em seu sistema:

* Python 3.x
* pip (gerenciador de pacotes do Python)

### Instalação

1. Clone este repositório para o seu ambiente local:

```shell

git clone https://github.com/seu-usuario/youtube-music-service.git
```
    
1. Acesse o diretório do projeto:

```shell

cd youtube-music-service
```
1. Crie um ambiente virtual para isolar as dependências do projeto:

```shell

python3 -m venv venv
```
1. Ative o ambiente virtual:

Para Linux/MacOS:

```shell

source venv/bin/activate
```
Para Windows (PowerShell):

```shell

.\venv\Scripts\Activate.ps1
```
1. Instale as dependências do projeto:

```shell

pip install -r requirements.txt
```

## Configuração

Antes de executar o serviço, você precisa configurar a chave de API do YouTube. Siga as etapas abaixo:

<ol>
    <li>Acesse o <a href="https://console.developers.google.com/">Google Developers Console.</a></li>
    <li>Crie um novo projeto ou selecione um projeto existente.</li>
    <li>Ative a API do YouTube e obtenha uma chave de API.</li>
    <li>Copie a chave de API e crie um arquivo .env na raiz do projeto.</li>
    <li>No arquivo <b>.env</b>, defina a chave de API como a variável de ambiente <b>YOUTUBE_API_KEY</b>:</li>
</ol>

```makefile

YOUTUBE_API_KEY=SUA_CHAVE_DE_API_DO_YOUTUBE
```

Certifique-se de substituir **'SUA_CHAVE_DE_API_DO_YOUTUBE'** pela chave de API válida do YouTube que você obteve anteriormente.

## Carregando as variáveis de ambiente

O serviço usará o pacote **'python-dotenv'** para carregar automaticamente as variáveis de ambiente do arquivo **'.env'**. Certifique-se de ter instalado o pacote **'python-dotenv'** seguindo as instruções de instalação mencionadas anteriormente.

## Execução

Após configurar as variáveis de ambiente, você pode iniciar o serviço executando o seguinte comando:

```shell

python app.py
```
O serviço estará disponível em **'http://localhost:5000/youtube'**.

Certifique-se de que o ambiente virtual esteja ativado antes de executar o serviço.

## API

### Pesquisar músicas

**'GET /youtube/search?query={termo de pesquisa}'**

Esta rota permite pesquisar músicas no YouTube com base no termo de pesquisa fornecido. O serviço retornará uma lista de vídeos encontrados, incluindo o título e o ID do vídeo.

### Exemplo de requisição:

```sql

GET /youtube/search?query=music
```

### Exemplo de resposta:

```json

{
  "videos": [
    {
      "title": "Video 1",
      "video_id": "123",
      "video_url": "https://www.youtube.com/watch?v=123"
    },
    {
      "title": "Video 2",
      "video_id": "456",
      "video_url": "https://www.youtube.com/watch?v=456"
    }
  ]
}
```

### Testes

Para executar os testes unitários do projeto, você pode usar o seguinte comando:

```shell

python -m unittest discover tests
```

Certifique-se de que o ambiente virtual esteja ativado antes de executar os testes.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a **MIT License**.