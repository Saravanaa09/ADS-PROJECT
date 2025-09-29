// app.js

// Adds two numbers
function add(a, b) {
    return a + b;
}

// Subtracts second number from first
function subtract(a, b) {
    return a - b;
}

// Multiplies two numbers
function multiply(a, b) {
    return a * b;
}

// Divides first number by second
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

// Export functions for testing
module.exports = { add, subtract, multiply, divide };
