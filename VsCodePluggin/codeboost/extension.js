// The module 'vscode' contains the VS Code extensibility API
const vscode = require("vscode");

// This function is called when the extension is activated.
// It is activated the first time the command is executed.
function activate(context) {
  // This line of code will only be executed once when your extension is activated.
  console.log('Congratulations, your extension "codeboost" is now active!');

  // Register the command "codeboost.findKeywords".
  let disposable = vscode.commands.registerCommand(
    "codeboost.findKeywords",
    async function () {
      // Prompt the user to enter a set of keywords separated by commas.
      const keywordsString = await vscode.window.showInputBox({
        prompt: "Enter a set of keywords separated by commas",
      });
      // If the user cancels the input box, return early.
      if (!keywordsString) {
        return;
      }

      // Split the keywords into an array.
      const keywords = keywordsString
        .split(",")
        .map((keyword) => keyword.trim());

      // Get the active editor's text and search for the keywords.
      const editor = vscode.window.activeTextEditor;
      const text = editor.document.getText();
      const matchedKeywords = keywords.filter((keyword) =>
        text.includes(keyword)
      );

      // If no keywords were matched, show a notification and return.
      if (matchedKeywords.length === 0) {
        vscode.window.showInformationMessage(
          "No matching keywords found in the file."
        );
        return;
      }

      // Show a notification with the matched keywords.
      vscode.window.showInformationMessage(
        `Matching keywords: ${matchedKeywords.join(", ")}`
      );
    }
  );

  // Add the disposable to the context subscriptions.
  context.subscriptions.push(disposable);
}

// This function is called when the extension is deactivated.
function deactivate() {}

// Export the activate and deactivate functions.
module.exports = {
  activate,
  deactivate,
};
