# Q&A system for an E-learning company  

End to end LLM project based on Google Gemini and Langchain. It's a Q&A system for an e-learning company which sells data related courses and bootcamps. They have thousands of learners who uses discord server or email to ask questions. This system will provide a streamlit based user interface for students where they can ask questions and get answers. 

## Project Highlights

- The company already has a CSV file of FAQs
- Current approach: human staff uses FAQs file to assist their course learners (time-consuming)
- Proposed solution: building an LLM based Q&A system that can reduce the staff workload
- Students should be able to use this system to ask questions directly and get answers within seconds

## Technologies used
  - Langchain + Google Gemini: LLM based Q&A
  - Streamlit: UI
  - Huggingface instructor embeddings: Text embeddings
  - FAISS: Vector databse

## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/laufragor/qna-academy-rag
```
2.Navigate to the project directory:

```bash
  cd qna-academy-rag
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```
## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2.The web app will open in your browser.

- To create a knowledebase of FAQs, click on Create Knownledge Base button. It will take some time, so please wait and chill.
- Now you are ready to ask questions. Type your question in Question box and hit Enter

## Sample Questions
  - Do you guys provide internship and also do you offer EMI payments?
  - Do you have javascript course?
  - Should I learn power bi or tableau?
  - I have a MAC computer. Can I use powerbi on it?
  - I don't see power pivot. how can I enable it?
