chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.action === "copy") {
    chrome.tabs.executeScript(
      {
        code: "window.getSelection().toString();",
      },
      function (selection) {
        console.log("Selected text:", selection[0]);
        fetch("http://localhost:5000/analyze-text", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text: selection[0] }),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Server response:", data);
            chrome.runtime.sendMessage({
              action: "updatePopup",
              data: {
                ...data,
                selected_text: selection[0],
                is_evaluating: false,
              },
            });
          })
          .catch((error) => console.error("Error:", error));
      }
    );
  }
});
