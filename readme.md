# Simple Banking System

A CSCI 1063U Python-based command-line banking system that allows users to create and manage bank accounts with deposit, withdrawal, and transaction history tracking capabilities.

## Features

- **Account Management**: Create and manage multiple bank accounts with unique IDs
- **Deposit & Withdrawal**: Deposit and withdraw money from accounts with transaction descriptions
- **Transaction History**: Track all transactions with timestamps and descriptions
- **Data Persistence**: Save and load bank data from disk using pickle serialization
- **Input Validation**: Robust error handling for invalid inputs (negative amounts, insufficient balance, etc.)
- **Interactive CLI**: User-friendly command-line interface for all banking operations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Daniel-S-Allen/Mini-Project-2-Simple-Banking-System.git
cd Mini-Project-2-Simple-Banking-System
```

## Usage

### Run

In a terminal, run `python main.py`

### Available Commands:
- `create`: Create a new account with specified ID and initial balance
- `select`: Switch to an existing account
- `list`: Display all account IDs in the bank
- `deposit`: Add money to the current account
- `withdraw`: Remove money from the current account
- `view`: Display current account balance and transaction history
- `quit`: Save all data and exit the program

## Requirements
- Python 3.10+
- pytest (optional, for running tests)
