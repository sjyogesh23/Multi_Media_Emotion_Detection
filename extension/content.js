document.addEventListener("copy", function () {
  chrome.runtime.sendMessage({ action: "copy" });
});
