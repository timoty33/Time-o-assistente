function trocarPlay() {
  const iconPlay = document.getElementById("iconPlay");
  const circle = document.getElementById("circle");

  if (iconPlay.classList.contains("fa-play")) {
    iconPlay.classList.replace("fa-play", "fa-pause");
    circle.classList.add("active");
  } else {
    iconPlay.classList.replace("fa-pause", "fa-play");
    circle.classList.remove("active");
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
