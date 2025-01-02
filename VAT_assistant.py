import streamlit as st
import openai
from pinecone import Pinecone
import os

oa_api_key = os.getenv("OPENAI_API_KEY")
pc_api_key = os.getenv("PINECONE_API_KEY")

# Ensure the API key is set
if not pc_api_key:
    raise ValueError("API key not found. Set PINECONE_API_KEY in your environment or secrets.")

# Initialize Pinecone
pc = Pinecone(api_key=pc_api_key, environment="us-east-1-aws")
index_name = "vat-docs-index"
index = pc.Index(index_name)

# Ensure the API key is set
if not oa_api_key:
    raise ValueError("API key not found. Set OPENAI_API_KEY in your environment or secrets.")

# Initialize OpenAI embeddings
openai.api_key = oa_api_key

# Function to query Pinecone and OpenAI
def get_answer(query, level_of_detail):
    # Generate query embedding
    response = openai.embeddings.create(
        input=query,
        model="text-embedding-ada-002"
    )
    embedding = response.data[0].embedding

    # Query Pinecone
    results = index.query(vector=embedding, top_k=3, include_metadata=True)

    matches = results.get("matches", [])
    if not matches:
        return "No relevant documents were found for your query."

    # Construct context from Pinecone results
    context = "\n\n".join(
        [f"Document: {match['metadata']['document']}\nPage: {match['metadata']['page']}\nContent: {match['metadata']['content']}" for match in matches]
    )

    # Pass context and query to OpenAI for a detailed answer
    prompt = f"""
    The following is a collection of excerpts from VAT-related documents:

    {context}

    Based on the above information and by citing the data used, answer the following query in an accurate manner:

    Make sure you dont mention in the answer that this is based on the collection of excerpts rather say the source it is from which is the vat laws documents name in the meta data along with page number and source link to document on nbr website in bahrain, make the answer easy to read, well formatted and section and keep the references at the end of the answer while making the important figures or facts in bold or underlined.

    If the excerpts are not related to the documents or the data do not match please state that this data is not available in the knowledge base of this assistant and guide the user to the FAQs page of the nbr website (https://www.nbr.gov.bh/vat_faqs) and write some follow up questions for the user to ask.

    Make your answer {level_of_detail}

    Query: {query}
    """

    response = openai.chat.completions.create(
        model="gpt-4", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in VAT-related questions in Bahrain."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6  
    )
    return response.choices[0].message.content

# Streamlit UI
st.image("https://cdn.cookielaw.org/logos/80f0f529-1935-4858-b3ef-fd87711f2bef/699a7583-6beb-4fe7-909d-7657f4335b39/f780793e-468c-4577-b438-75739082e83a/KPMG_NoCP_RGB_280.png", width=200)
st.title("VAT Information Assistant")

# Input text box
st.header("Ask your question:")
user_query = st.text_input("Type your question here:", value="")

# User selects the level of detail
level_of_detail = st.radio("Choose the level of detail for the answer:", ["Brief", "Detailed"], index=1)

if st.button("Get Answer", type="primary", use_container_width=True):
    if user_query.strip():
        with st.spinner("Fetching answer..."):
            try:
                answer = get_answer(user_query, level_of_detail)
                st.success("Answer: \n" + answer)
                # st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please ask a question.")
