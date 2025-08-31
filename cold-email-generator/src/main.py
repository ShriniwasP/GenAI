"""
Cold Email Generator - Main Pipeline
Author: Shriniwas P
Project: GenAI Project 1
"""

import pandas as pd
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import chromadb

# === 1. Initialize LLM ===
def load_llm():
    """Initialize Groq LLaMA model."""
    return ChatGroq(model="llama2-70b-chat", temperature=0.2)

# === 2. Extract Job Details ===
def extract_job_details(job_description: str, llm):
    """Use LLM to extract structured job details from a raw description."""
    prompt = ChatPromptTemplate.from_template(
        """
        Extract the following details from the job description:
        - Role
        - Required Skills
        - Experience
        - Location
        - Summary

        Job Description:
        {jd}
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(jd=job_description)

# === 3. Setup ChromaDB ===
def init_vector_db():
    """Initialize ChromaDB for portfolio/skills retrieval."""
    client = chromadb.Client()
    collection = client.get_or_create_collection("portfolio")
    return collection

# === 4. Generate Cold Email ===
def generate_email(job_details: dict, portfolio_links: list, llm):
    """Generate a cold email based on job details + portfolio."""
    prompt = ChatPromptTemplate.from_template(
        """
        Write a professional cold email to a client based on:
        - Job Role: {role}
        - Skills: {skills}
        - Experience: {experience}
        - Portfolio Links: {portfolio}

        Email should be polite, concise, and highlight relevant expertise.
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(
        role=job_details.get("role", ""),
        skills=", ".join(job_details.get("skills", [])),
        experience=job_details.get("experience", ""),
        portfolio=", ".join(portfolio_links)
    )

# === 5. Main Pipeline ===
if __name__ == "__main__":
    llm = load_llm()

    # Example job description (later will be scraped dynamically)
    jd_text = """
    We are looking for a Data Scientist with 3+ years of experience in Python,
    NLP, and Machine Learning. Location: Mumbai.
    """

    # Extract job details
    details = extract_job_details(jd_text, llm)
    print("Extracted Details:", details)

    # Setup portfolio DB
    db = init_vector_db()
    portfolio = ["https://portfolio.com/project1", "https://portfolio.com/project2"]

    # Generate email
    email_text = generate_email(details, portfolio, llm)
    print("\nGenerated Cold Email:\n", email_text)

