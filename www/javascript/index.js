function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function volume() {
  const buttonVolume = document.getElementById("buttonVolume");
  const iconVolume = document.getElementById("iconeVolume");
  const painelVolume = document.getElementById("painelVolume");

  // Alterna entre classe volume-button e volume-painel
  if (buttonVolume.classList.contains("volume-button")) {
    iconVolume.classList.add("desligado");
    buttonVolume.classList.replace("volume-button", "volume-painel");
    painelVolume.classList.remove("desligado");
  } else {
    iconVolume.classList.remove("desligado");
    buttonVolume.classList.replace("volume-painel", "volume-button");
    painelVolume.classList.add("desligado");
  }
}

let textoAtual = "";

async function receberTexto() {
  const boxText = document.getElementById("text");

  while (true) {
    var novoTexto = await eel.enviarTexto()();

    if (novoTexto && novoTexto !== textoAtual) {
      textoAtual = novoTexto;
      boxText.textContent = novoTexto;
    }

    await sleep(1000);
  }
}

function ativarBotaoMic(ativado) {
  const botaoMic = document.getElementById("botaoMic");

  if (ativado === true) {
    botaoMic.classList.replace("desativado", "mic");
  } else {
    botaoMic.classList.replace("mic", "desativado");
  }
}

function ativarAssistente() {
  const iconPlay = document.getElementById("iconPlay");
  const circle = document.getElementById("circle");
  const status = document.getElementById("status");

  if (iconPlay.classList.contains("fa-play")) {
    var ativado = true;
    iconPlay.classList.replace("fa-play", "fa-pause");
    circle.classList.add("active");
    status.textContent = "Ativado";
    eel.iniciar_assistente()();
    ativarBotaoMic(ativado);
  } else {
    iconPlay.classList.replace("fa-pause", "fa-play");
    circle.classList.remove("active");
    status.textContent = "Desativado";
    ativarBotaoMic(ativado);
  }
}

function trocarMic() {
  const iconPlay = document.getElementById("iconMic");

  if (iconPlay.classList.contains("fa-microphone")) {
    iconPlay.classList.replace("fa-microphone", "fa-microphone-slash");
    eel.parar_assistente()();
  } else {
    iconPlay.classList.replace("fa-microphone-slash", "fa-microphone");
  }
}

receberTexto();

const volumeInput = document.querySelector(".inputVolume");

volumeInput.addEventListener("input", () => {
  const valorAtual = volumeInput.value;
  console.log("Volume atual:", valorAtual);
  eel.receberVolume(valorAtual); // envia o valor para o Python
});
