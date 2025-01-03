Here’s your updated **README.md** file based on your requirements:

---

# VAT Information Assistant

A **Streamlit-based web application** designed to assist users with VAT-related queries in Bahrain. The application leverages **OpenAI's GPT-4**, **Pinecone**, and **Streamlit Cloud** to provide detailed or brief responses based on user input.

---

## Features

- **Interactive UI**: Users can type questions and choose the level of detail for the response.
- **Level of Detail**: Choose between a **Brief** or **Detailed** response.
- **Responsive Search**: Integrates **Pinecone vector database** to retrieve relevant content efficiently.
- **Customizable UI**: Styled with KPMG's theme colors for a professional look.
- **Secure Key Management**: API keys managed securely with **Streamlit Secrets**.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: OpenAI GPT-4
- **Database**: Pinecone Vector Database
- **Deployment**: Streamlit Cloud

---

## Installation

### Prerequisites

- Python 3.9 or above
- Git installed

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/vat-assistant.git
   cd vat-assistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.streamlit/secrets.toml` file:
     ```toml
     [api_keys]
     OPENAI_API_KEY = "your_openai_api_key"
     PINECONE_API_KEY = "your_pinecone_api_key"
     ```

4. **Run the App Locally**:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser at `http://localhost:8501`.

---

## Deployment

The application is hosted on **Streamlit Cloud**. To deploy:

1. Push your code to a GitHub repository.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud).
3. Connect your repository and deploy the app.
4. Add API keys in the **Secrets** section of Streamlit Cloud in this format:
   ```toml
   [api_keys]
   OPENAI_API_KEY = "your_openai_api_key"
   PINECONE_API_KEY = "your_pinecone_api_key"
   ```

---

## File Structure

```
vat-assistant/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Dependencies
├── .streamlit/
│   ├── secrets.toml        # API keys (not included in GitHub)
│   └── config.toml         # Streamlit theme configuration
└── README.md               # Project documentation
```

---

Let me know if you need further adjustments!