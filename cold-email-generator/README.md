# Cold Email Generator (GenAI Project 1)

This project automates the process of generating cold emails tailored to job postings on company career pages.

## 🚀 Project Workflow
1. Scrape job postings from a company’s career page using LangChain.
2. Use LLaMA (via Groq API) to extract structured job details (role, skills, experience, description).
3. Store and retrieve relevant skills/portfolio links from ChromaDB (vector database).
4. Generate a professional cold email to the client using extracted job details + Our experience portfolio for the client.
5. Display results in a simple Streamlit UI.

## 📂 Project Structure

