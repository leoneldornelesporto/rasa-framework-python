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