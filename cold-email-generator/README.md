# Cold Email Generator (GenAI Project 1)

This project automates the process of generating cold emails tailored to job postings on company career pages.

## 🚀 Project Workflow
1. Scrape job postings from a company’s career page using LangChain.
2. Use LLaMA (via Groq API) to extract structured job details (role, skills, experience, description).
3. Store and retrieve relevant skills/portfolio links from ChromaDB (vector database).
4. Generate a professional cold email to the client using extracted job details + Our experience portfolio for the client.
5. Display results in a simple Streamlit UI.

## 📂 Project Structure
```
cold-email-generator/
├── src/
│   ├── main.py          # Main pipeline
│   ├── utils.py         # Helper functions
│   ├── chains.py        # Job extraction & email generation chains
│   ├── portfolio.py     # Portfolio database integration
├── app/
│   ├── main.py          # Streamlit UI
│   └── resource/
│       └── my_portfolio.csv  # Tech stack to portfolio links
├── docs/
│   └── project_details.docx  # Original project notes
├── requirements.txt
└── README.md
```

## 🛠️ Tech Stack
- **Python 3.10**
- **LangChain** – framework for building LLM apps  
- **Groq API (LLaMA models)** – job extraction & email generation  
- **ChromaDB** – lightweight vector database for portfolio/skills retrieval  
- **Streamlit** – web UI  
- **Sentence-Transformers** – embeddings for similarity search  
- **Pandas, NumPy** – data handling

## ⚙️ Setup & Run
1. Clone the repository:
 ```
git clone https://github.com/ShriniwasP/GenAI.git
cd GenAI/cold-email-generator
```
2. Create & Activate environment
   ```
conda create -n venv python=3.10
conda activate venv
```
3. Install dependencies
   ```
pip install -r requirements.txt
```
4. Run the streamlit app
   ```
streamlit run app/main.py
```
