# Thoughtful AI Customer Support Agent

This project is a customer support agent for Thoughtful AI, built using Gradio. The agent answers predefined questions about Thoughtful AI's automation agents.

## Features

- Provides answers to predefined questions about Thoughtful AI's agents.
- Uses Gradio for the user interface.
- Logs errors when no relevant answer is found.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai_agent.git
    cd ai_agent
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python ai_agent.py
    ```

2. Open the provided URL in your web browser to interact with the customer support agent.

## Project Structure

- [ai_agent.py](http://_vscodecontentref_/0): Main script containing the logic for the customer support agent.
- `requirements.txt`: List of required Python packages.

## Functions

### [get_answer(user_input: str) -> str](http://_vscodecontentref_/1)

Finds the most relevant answer from the predefined dataset.

**Args:**
- [user_input](http://_vscodecontentref_/2) (str): The user's input question.

**Returns:**
- [str](http://_vscodecontentref_/3): The most relevant answer or a default response if no match is found.

### [chat_interface(user_input: str, chat_history: list) -> list](http://_vscodecontentref_/4)

Handles the chat interface logic.

**Args:**
- [user_input](http://_vscodecontentref_/5) (str): The user's input question.
- [chat_history](http://_vscodecontentref_/6) (list): The chat history.

**Returns:**
- [list](http://_vscodecontentref_/7): Updated chat history with the new user input and response.

## License

This project is licensed under the MIT License. See the LICENSE file for details.