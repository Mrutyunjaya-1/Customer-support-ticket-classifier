# Customer Support Ticket Classifier

## Overview

This project is an AI-powered Customer Support Ticket Classifier built using:

- Gemini API
- LangChain
- Pydantic Output Parser
- Streamlit

The application automatically:
- Classifies customer tickets
- Assigns priority
- Routes tickets to the correct support queue
- Generates a professional response draft

---

## Features

- Billing / Technical / General ticket classification
- Priority prediction
- Routing queue assignment
- AI-generated response drafting
- Streamlit web interface
- Structured JSON output using Pydantic

---

## Technologies Used

- Python
- Gemini API
- LangChain
- Streamlit
- Pydantic

---

## Project Structure

```bash
customer-support-ticket-classifier/
│
├── app.py
├── model.py
├── parser.py
├── prompt.py
├── requirements.txt
├── .env
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Example Input

```text
I was charged twice for my subscription.
```

---

## Example Output

```json
{
  "category": "Billing",
  "priority": "High",
  "routing_queue": "Billing Support",
  "response_draft": "We apologize for the inconvenience..."
}
```

---

## Future Improvements

- Multi-language support
- Sentiment analysis
- Ticket summarization
- Database integration
- Admin dashboard

---

## Live Application
- https://customer-support-ticket-classifier-kycer9evdorecbpuwtgsjb.streamlit.app/

---

## Author

Mrutyunjaya Debata
