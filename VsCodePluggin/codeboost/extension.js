// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
function activate(context) {
  // Use the console to output diagnostic information (console.log) and errors (console.error)
  // This line of code will only be executed once when your extension is activated
  console.log('Congratulations, your extension "codeboost" is now active!');

  // The command has been defined in the package.json file
  // Now provide the implementation of the command with  registerCommand
  // The commandId parameter must match the command field in package.json
  let disposable = vscode.commands.registerCommand(
    "codeboost.findKeywords",
    async function () {
      // Prompt the user to enter a set of keywords
      const keywordsString = await vscode.window.showInputBox({
        prompt: "Enter a set of keywords separated by commas",
      });

      // If the user cancels the input box, return early
      if (!keywordsString) {
        return;
      }

      // Split the keywords into an array
      const keywords = keywordsString
        .split(",")
        .map((keyword) => keyword.trim());

      // Get the active editor's text and search for the keywords
      const editor = vscode.window.activeTextEditor;
      const text = editor.document.getText();
      const matchedKeywords = keywords.filter((keyword) =>
        text.includes(keyword)
      );

      // If no keywords were matched, show a notification and return
      if (matchedKeywords.length === 0) {
        vscode.window.showInformationMessage(
          "No matching keywords found in the file."
        );
        return;
      }

      // Show a notification with the matched keywords
      vscode.window.showInformationMessage(
        `Matching keywords: ${matchedKeywords.join(", ")}`
      );
    }
  );

  context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
