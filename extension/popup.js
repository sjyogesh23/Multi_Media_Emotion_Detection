chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === "updatePopup") {
    const data = message.data;
    const selectedTextElement = document.getElementById("selectedText");

    // Show "Text Copied" when message is received but before evaluation
    selectedTextElement.innerHTML = `<p>Text Copied: ${data.selected_text}</p>`;

    // Show the evaluation result once it's received from the server
    selectedTextElement.innerHTML += `
      <p>Overall Emotion: ${data.wholeText.emotion}</p>
      <p>IPC: ${data.wholeText.IPC}</p>
      <p>Link: <a href="${data.wholeText.Link}" target="_blank">${data.wholeText.Link}</a></p>
    `;

    // Show emotions for each sentence
    data.sentences.forEach((sentence) => {
      selectedTextElement.innerHTML += `
        <hr />
        <p>Sentence: ${sentence.Sentence}</p>
        <p>Emotion: ${sentence.Emotion}</p>
        <p>IPC: ${sentence.IPC}</p>
        <p>Link: <a href="${sentence.Link}" target="_blank">${sentence.Link}</a></p>
      `;
    });
  }
});
