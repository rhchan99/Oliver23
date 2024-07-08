import pandas as pd
import streamlit as st


# Function to load CSV file
@st.cache_data
def load_csv(file):
    return pd.read_csv(file)


# Function to save DataFrame to CSV
def save_csv(df, filename):
    df.to_csv(filename, index=False)


# Main function to run the Streamlit app
def main():
    st.title("CSV File Editor")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        st.write("Original CSV File:")
        st.dataframe(df)

        # Create a copy of the DataFrame to edit
        editable_df = df.copy()

        st.write("Editable Table:")
        edited_df = st.data_editor(editable_df, num_rows="dynamic")

        if st.button("Save Edited CSV"):
            save_csv(edited_df, "edited_file.csv")
            st.success("Edited CSV saved as 'edited_file.csv'")


if __name__ == "__main__":
    main()
