// offscreen.js - Handles audio playback in MV3
chrome.runtime.onMessage.addListener((message) => {
  if (message.target === "offscreen-audio") {
    playAudio(message.audioFile, message.volume || 1.0);
  }
});

function playAudio(file, volume) {
  try {
    const audio = new Audio(chrome.runtime.getURL(file));
    audio.volume = volume;
    audio.play().catch(err => console.error("Audio playback error:", err));
  } catch (err) {
    console.error("Failed to create Audio:", err);
  }
}