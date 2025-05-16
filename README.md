<h1>Timmy_oAssistente</h1>
Timmy foi desenvolvido para ajudar em tarefas tanto básicas, mas também em tarefas mais complexas como fazer perguntas para o Gemini, analisar a tela, ou apenas partes específicas dela, fazer lembretes e/ou tocar músicas só pela voz, espero que faça um bom proveito do assistente!

<h1>Descrição 🤔</h1>

<strong>Assistente desativado / Assistente ativado </strong>

<img src="https://github.com/user-attachments/assets/281cd892-7a29-42b4-9750-e35db329fd38" width="300px">
<img src="https://github.com/user-attachments/assets/f2f3d3f1-bcf4-4355-b094-bf56a924db9c" width="300px">

# 🧠 Comandos do Assistente

## Descrição Geral 🗒️

Este é o manual de comandos do **assistente virtual Timmy**, desenvolvido para interagir com você por meio de comandos de voz ou texto. Cada comando ativa uma funcionalidade específica que vai desde informar a hora até tocar músicas, traduzir textos, criar lembretes, interagir com APIs e muito mais.

Abaixo, você encontrará uma lista detalhada de comandos disponíveis, com:

- 📝 **Descrição**: O que o comando faz.
- 🧩 **Função chamada**: Nome da função Python que é ativada.
- 💬 **Exemplo**: Como o comando pode ser falado ou digitado pelo usuário.

Esse formato permite que você entenda exatamente o que o assistente pode fazer e como usá-lo de forma prática e intuitiva.

---

## **‼️Atenção, todos os comandos precisam ser acompanhados da palavra assistente‼️** Ex: `assistente, que horas são`

## `ver_horas`
- 📝 **Descrição**: Informa as horas atuais.
- 🧩 **Função chamada**: `horas()`
- 💬 **Exemplo**: `que horas são agora?`

## `ver_data`
- 📝 **Descrição**: Informa a data atual.
- 🧩 **Função chamada**: `hoje()`
- 💬 **Exemplo**: `qual a data de hoje?`

## `aumentar_volume` *(Experimental)*
- 📝 **Descrição**: Aumenta o volume do sistema.
- 🧩 **Função chamada**: `aumentarVolume(passo=0.1)`
- 💬 **Exemplo**: `aumente o volume`

## `diminuir_volume` *(Experimental)*
- 📝 **Descrição**: Diminui o volume do sistema.
- 🧩 **Função chamada**: `diminuirVolume(passo=0.1)`
- 💬 **Exemplo**: `baixe o volume`

## `alternar_mudo` *(Experimental)*
- 📝 **Descrição**: Ativa ou desativa o mudo do sistema.
- 🧩 **Função chamada**: `alternar_mudo()`
- 💬 **Exemplo**: `ative o mudo`

## `aumentar_brilho`
- 📝 **Descrição**: Aumenta o brilho da tela.
- 🧩 **Função chamada**: `aumentarBrilho()`
- 💬 **Exemplo**: `aumentar brilho`

## `diminuir_brilho`
- 📝 **Descrição**: Diminui o brilho da tela.
- 🧩 **Função chamada**: `diminuirBrilho()`
- 💬 **Exemplo**: `diminuir brilho`

## `abrir_chatgpt`
- 📝 **Descrição**: Abre o ChatGPT no navegador.
- 🧩 **Função chamada**: `abrirGPT()`
- 💬 **Exemplo**: `abrir chat`

## `tocar_lofi`
- 📝 **Descrição**: Toca música Lofi.
- 🧩 **Função chamada**: `tocarLofi()`
- 💬 **Exemplo**: `tocar música relaxante`

## `tocar_musica_animada`
- 📝 **Descrição**: Toca uma música animada.
- 🧩 **Função chamada**: `tocarMusicaAnimada()`
- 💬 **Exemplo**: `tocar música animada`

## `abrir_cronometro`
- 📝 **Descrição**: Abre um cronômetro na tela.
- 🧩 **Função chamada**: `cronometro()`
- 💬 **Exemplo**: `cronômetro`

## `traduzir_texto`
- 📝 **Descrição**: Traduz um texto fornecido pelo usuário.
- 🧩 **Função chamada**: `traduzirTexto(texto)`
- 💬 **Exemplo**: `traduza esse texto`

## `ver_receitas_bebida`
- 📝 **Descrição**: Mostra a receita de uma bebida.
- 🧩 **Função chamada**: `receitaDrink(nome)`
- 💬 **Exemplo**: `receita de bebida`

## `ver_cotacoes`
- 📝 **Descrição**: Mostra cotações de moedas.
- 🧩 **Função chamada**: `obter_cotacoes()`
- 💬 **Exemplo**: `cotaçõesr`

## `ver_imagens_gato`
- 📝 **Descrição**: Mostra imagens de gatos.
- 🧩 **Função chamada**: `abrir_imagem_de_gato()`
- 💬 **Exemplo**: `ver imagem de gato`

## `fazer_lembrete`
- 📝 **Descrição**: Cria um lembrete baseado no comando.
- 🧩 **Função chamada**: `lembrete(comando)`
- 💬 **Exemplo**: `lembrete`

## `ver_clima`
- 📝 **Descrição**: Informa o clima atual.
- 🧩 **Função chamada**: `clima()`
- 💬 **Exemplo**: `como está o clima?`

## `lançar_moeda`
- 📝 **Descrição**: Lança uma moeda (cara ou coroa).
- 🧩 **Função chamada**: `jogarMoeda()`
- 💬 **Exemplo**: `jogue uma moeda`

## `agradecer`
- 📝 **Descrição**: Responde ao agradecimento.
- 🧩 **Função chamada**: `obrigado()`
- 💬 **Exemplo**: `valeu`

## `cumprimento`
- 📝 **Descrição**: Responde a um cumprimento.
- 🧩 **Função chamada**: `comoEsta()`
- 💬 **Exemplo**: `olá assistente`

## `ver_frase_motivacional`
- 📝 **Descrição**: Mostra uma frase motivacional.
- 🧩 **Função chamada**: `fraseMotivacional()`
- 💬 **Exemplo**: `diga uma frase motivaconal`

## `ver_curiosidade`
- 📝 **Descrição**: Mostra uma curiosidade aleatória.
- 🧩 **Função chamada**: `curiosidade()`
- 💬 **Exemplo**: `diga uma curiosidade`

## `ver_piada`
- 📝 **Descrição**: Conta uma piada.
- 🧩 **Função chamada**: `piadas()`
- 💬 **Exemplo**: `me conte uma piada`

## `ativar_assistente_ia`
- 📝 **Descrição**: Ativa o modo IA (chatBot).
- 🧩 **Função chamada**: `chatBot()`
- 💬 **Exemplo**: `ativar assistente inteligente`

## `ver_tela`
- 📝 **Descrição**: Retorna informações da tela.
- 🧩 **Função chamada**: `verTela(comando)`
- 💬 **Exemplo**: `analise minha tela + prompt (ex: qual é o preço)`

## `rotina_bom_dia`
- 📝 **Descrição**: Executa a rotina de bom dia.
- 🧩 **Função chamada**: `bomDia()`
- 💬 **Exemplo**: `bom dia, assistente`

## `rotina_boa_noite`
- 📝 **Descrição**: Executa a rotina de boa noite.
- 🧩 **Função chamada**: `boaNoite()`
- 💬 **Exemplo**: `boa noite, assistente`

## `rotina_lembrete_hidratacao`
- 📝 **Descrição**: Inicia lembretes de hidratação periódicos.
- 🧩 **Função chamada**: `hidratacao()`
- 💬 **Exemplo**: `ativar lembretes de hidratação`

## `desativar_lembrete_hidratacao`
- 📝 **Descrição**: Interrompe os lembretes de hidratação.
- 🧩 **Função chamada**: `falar("Hidratação interrompida!")`
- 💬 **Exemplo**: `parar os lembretes de hidratação`

## `pesquisar_maps`
- 📝 **Descrição**: Faz uma pesquisa no Google Maps.
- 🧩 **Função chamada**: `buscarMaps(comando)`
- 💬 **Exemplo**: `procurar no mapa + local (ex: restaurantes veganos)`

## `modo_repouso`
- 📝 **Descrição**: Coloca o assistente em modo de espera.
- 🧩 **Função chamada**: `modoRepouso()`
- 💬 **Exemplo**: `assistente descansar`

## `desligar` ou `sair`
- 📝 **Descrição**: Encerra o assistente.
- 🧩 **Função chamada**: `exit()`
- 💬 **Exemplo**: `sair do assistente`
