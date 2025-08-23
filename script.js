const display = document.getElementById("display");
const historyBox = document.getElementById("history");

let currentInput = "0";
let history = JSON.parse(localStorage.getItem("calcHistory")) || [];

// Update display
function updateDisplay() {
  display.innerText = currentInput;
}

// Update history box
function updateHistory() {
  historyBox.innerHTML = "";
  history.slice(-25).forEach(item => {
    const div = document.createElement("div");
    div.innerText = item;
    historyBox.appendChild(div);
  });
  localStorage.setItem("calcHistory", JSON.stringify(history));
}

// Handle button clicks
function pressKey(key) {
  if (currentInput === "0" && !isNaN(key)) {
    currentInput = key;
  } else {
    currentInput += key;
  }
  updateDisplay();
}

// Clear display
function clearAll() {
  currentInput = "0";
  updateDisplay();
}

// Backspace
function clearOne() {
  currentInput = currentInput.slice(0, -1) || "0";
  updateDisplay();
}

// Evaluate
function calculate() {
  try {
    let result = eval(currentInput.replace(/x/g, "*"));
    history.push(`${currentInput} = ${result}`);
    currentInput = result.toString();
    updateDisplay();
    updateHistory();
  } catch {
    currentInput = "Error";
    updateDisplay();
  }
}

// Initialize
updateDisplay();
updateHistory();
