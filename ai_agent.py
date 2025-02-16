import gradio as gr
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Predefined dataset of questions and answers
predefined_data = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}

def get_answer(user_input: str) -> str:
    """
    Find the most relevant answer from the predefined dataset.

    Args:
        user_input (str): The user's input question.

    Returns:
        str: The most relevant answer or a default response if no match is found.
    """
    user_input = user_input.lower().strip()
    for qa in predefined_data["questions"]:
        if user_input in qa["question"].lower():
            return qa["answer"]
    logging.error(f"No relevant answer found for the question: {user_input}")
    return "I'm sorry, I don't have information on that. Please ask another question about Thoughtful AI's agents."

def chat_interface(user_input: str, chat_history: list) -> list:
    """
    Handle the chat interface logic.

    Args:
        user_input (str): The user's input question.
        chat_history (list): The chat history.

    Returns:
        list: Updated chat history with the new user input and response.
    """
    chat_history = chat_history or []
    response = get_answer(user_input)
    chat_history.append((user_input, response))
    return chat_history

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("### Thoughtful AI Customer Support Agent")
    chatbot = gr.Chatbot(label="Chat")
    user_input = gr.Textbox(label="Your Question")
    submit_button = gr.Button("Submit")
    clear_button = gr.Button("Clear")

    submit_button.click(chat_interface, inputs=[user_input, chatbot], outputs=chatbot)
    clear_button.click(lambda: None, inputs=None, outputs=chatbot, queue=False)

# Launch the app
demo.launch()