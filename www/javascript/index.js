function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function receberTexto() {
  const boxText = document.getElementById("text")
  while (true) {
    var texto = await eel.enviarTexto()();
    boxText.textContent = texto

    await sleep(1000);
  }
}

function trocarPlay() {
  const iconPlay = document.getElementById("iconPlay");
  const circle = document.getElementById("circle");
  const status = document.getElementById("status");

  if (iconPlay.classList.contains("fa-play")) {
    var ativado = true
    iconPlay.classList.replace("fa-play", "fa-pause");
    circle.classList.add("active");
    status.textContent = "Ativado";
    eel.iniciar_assistente()();
  } else {
    iconPlay.classList.replace("fa-pause", "fa-play");
    circle.classList.remove("active");
    status.textContent = "Desativado";
    eel.parar_assistente()();
  }
}

function trocarMic() {
  const iconPlay = document.getElementById("iconMic");

  if (iconPlay.classList.contains("fa-microphone")) {
    iconPlay.classList.replace("fa-microphone", "fa-microphone-slash");
  } else {
    iconPlay.classList.replace("fa-microphone-slash", "fa-microphone");
  }
}

receberTexto();