import streamlit as st

from langchain_core.output_parsers import PydanticOutputParser

from parser import TicketClassification
from prompt import prompt
from model import llm


parser = PydanticOutputParser(
    pydantic_object=TicketClassification
)


st.set_page_config(
    page_title="Customer Support Ticket Classifier",
    page_icon="🎫",
    layout="centered"
)


st.title("🎫 Customer Support Ticket Classifier")

st.markdown(
    "AI-powered ticket classification using Gemini + LangChain"
)


ticket = st.text_area(
    "Enter Customer Ticket",
    height=150
)


if st.button("Analyze Ticket"):

    if ticket:

        final_prompt = prompt.format(
            ticket=ticket,
            format_instructions=parser.get_format_instructions()
        )

        response = llm.invoke(final_prompt)

        parsed_output = parser.parse(response.content)

        st.success("Ticket Processed Successfully")

        st.markdown(
            f"### 📂 Category\n{parsed_output.category}"
        )

        st.markdown(
            f"### ⚡ Priority\n{parsed_output.priority}"
        )

        st.markdown(
            f"### 🛠 Routing Queue\n{parsed_output.routing_queue}"
        )

        st.markdown(
            f"### 💬 Response Draft\n{parsed_output.response_draft}"
        )

    else:
        st.warning("Please enter a customer ticket.")