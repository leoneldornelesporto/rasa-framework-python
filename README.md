## Assistente para previsão do tempo
Chatbot de exemplo para iniciantes em RASA. O assistente pode realizar a previsão do tempo. Ele é integrado com uma [API de previsão do tempo](http://servicos.cptec.inpe.br).



### Organização do projeto
Os arquivos e diretórios do projeto estão organizados da seguinte maneira:

```
    actions/            // Arquivos python com ações customizadas
    data/
        - nlu/          // Intenções e entidades          
        - stories/      // Histórias e fluxos de conversa
    helpers/            // Funções úteis e constantes
    models/             // Arquivos com os modelos treinados de NLU
    tests/              // Testes com o assistente
    config.yml          // Configurações do assistente
    credentials.yml     // Credenciais de acesso às plataformas de chat e voice
    domain.yml          // Arquivo que instancia as intenções, entidades e ações do assistente
    endpoints.yml       // Endpoints que o bot pode utilizar
```

### Instruções de instalação
Para executar o chatbot, antes é necessário seguir esses passos:
 1. Instalar o RASA: [link](https://rasa.com/docs/rasa/user-guide/installation/);
 2. Instalar o RASA-SDK: [link](https://rasa.com/docs/rasa/api/rasa-sdk/#installation);
 3. Instalar spaCy (dependência): [link](https://rasa.com/docs/rasa/user-guide/installation/#dependencies-for-spacy)
 4. Instalar o RASA X (opcional): [link](https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide/);

 - Após isso, no mesmo terminal execute o comando `rasa run actions` para executar o servidor de ações do RASA;
 - Em outro terminal paralelo, execute o comando `rasa train && rasa shell` para treinar e testar o bot no terminal.
 - Para montar as stories, realize o comando `rasa interactive`, para mapear cada intent e entity das frases, e serve para ajustar se estiver com algum detalhe faltando na intent.

### Instruções para fazer o deploy no telegram
Para você implantar o bot no telegram, você deve fazer o seguinte:
 1. Acessar o seu telegram [link](https://web.telegram.org/) e criar uma conta
 2. Precisara dar um nome ao bot, qualquernome_bot, o final do nome sempre deve terminar com bot.
 3. Depois de cadastrado no telegram, o mesmo gerará um token e esse token e o nome no bot que precisaremos para colocar em nossas configurações.

No access_token, colocamos o id gerado pelo telegram.
No verify, colocamos o nome que criamos no telegram
O webhook_url, você precisará baixar o ngrok [link](https://ngrok.com/) para cria um endpoint público, onde o telegram se comunicará com nossa máquina.
Depois de baixado o ngrok, vai clicando duas vezes no executável dele, abrirá um cmd onde executaremos o seguinte comando:
ngrok http 5005
Onde aparecerá um link parecido com esse aqui, https://ed6bef0bcba6.ngrok.io.
Copie esse link para o webhook_url, lembrando que essa tag deve ser colocado dentro do arquivo config.

```
telegram:
    access_token: "1269323847:AAFmK_-xDaunY48Jst-lNIiieDJia-8gAeY"
    verify: "leonel_porto_bot"
    webhook_url: "https://ed6bef0bcba6.ngrok.io/webhooks/telegram/webhook"
```

### Instruções para fazer o deploy no webchat
Para você implantar o bot no webchat, você deve fazer o seguinte:
 1. Rodar o ngrok com o comando ngrok http 5005
 2. Pegar o link que é gerado no ngrok https://7d6769c6962f.ngrok.io.
 3. E colocar no script abaixo na tag socketUrl.
 4. E escrever o title e o subtitle do bot.


```
<script src="https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.min.js"></script>
<script>
  WebChat.default.init({
    selector: "#webchat",
    initPayload: "/start",
    customData: {"language": "pt"},
    socketUrl: "https://7d6769c6962f.ngrok.io/",
    socketPath: "/socket.io/",
    title: "Predict Time Rasa ChatBot",
    subtitle: "Predict Time",
  })
</script>
```
 