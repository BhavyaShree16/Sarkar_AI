# Sarkar_AI – AI-Powered Government Schemes Assistance

Sarkar_AI is a Python-based chatbot that helps users explore and understand various Indian government schemes. It supports multiple languages and answers questions using real government documents.

---

## 🧠 Features

- Answer questions about government schemes
- Works in multiple Indian languages
- Uses real PDF documents as knowledge source
- Gives accurate responses using RAG (Retrieval-Augmented Generation)
- Simple chatbot interface (can be integrated with any frontend)

---

## 🛠️ Technologies Used

- **Python**
- **Flask** – For building the backend API
- **LangChain** – To manage RAG pipeline
- **ChromaDB** – For storing and retrieving document embeddings
- **Groq API** – For generating LLM-based answers
- **Google Translate API** – For multilingual support
- **PyPDF / pdfminer** – For reading PDFs

---

## 🚀 How It Works

1. Load government PDFs
2. Convert them into embeddings using sentence transformers
3. User asks a question (in any language)
4. Question is translated to English → passed through RAG → answer generated
5. Answer is translated back to the original language and shown to user

---

