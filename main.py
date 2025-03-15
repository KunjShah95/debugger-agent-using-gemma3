import streamlit as st
import ollama

def generate_debugging_response(code_snippet):
    prompt = f"""
    You are TheDebugger, an AI-powered debugging assistant. Analyze the following code snippet, identify errors, suggest fixes, and provide explanations:
    
    ```
    {code_snippet}
    ```
    
    Provide a structured response with:
    - **Error Analysis**
    - **Fix Suggestions**
    - **Explanation**
    """
    
    response = ollama.chat(model='gemma3', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Function to format code (simple example)
def format_code(code_snippet):
    # This is a placeholder for actual formatting logic
    return code_snippet.strip()

# Streamlit UI
st.set_page_config(page_title='TheDebugger Agent', layout='wide')
st.title('🛠️ TheDebugger Agent')
st.write('Enter your code snippet below for AI-powered debugging using Gemma 3.')

code_input = st.text_area('Paste your code here:', height=250)

# New button for formatting code
if st.button('Format Code'):
    if code_input.strip():
        formatted_code = format_code(code_input)
        st.text_area('Formatted Code:', value=formatted_code, height=250)
    else:
        st.warning('Please enter a code snippet to format.')

if st.button('Debug Code'):
    if code_input.strip():
        with st.spinner('Analyzing code...'):
            result = generate_debugging_response(code_input)
        st.subheader('Debugging Results')
        st.markdown(result)
        
        # New button to download results
        st.download_button('Download Results', result, file_name='debugging_results.txt')
    else:
        st.warning('Please enter a code snippet to analyze.')

# New button to clear input
if st.button('Clear Input'):
    st.experimental_rerun()
