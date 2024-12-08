import streamlit as st
import pandas as pd

def main():
    st.title('Excel Sheet Selector')
    
    # File uploader widget
    uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx'])
    
    if uploaded_file is not None:
        # Load the Excel file without any data to quickly fetch sheet names
        xl = pd.ExcelFile(uploaded_file)
        
        # Get the sheet names
        sheet_names = xl.sheet_names
        
        # Display a checklist for the user to select sheets
        selected_sheets = st.multiselect("Select sheets to display:", options=sheet_names)
        
        # Initialize an empty DataFrame to store consolidated data
        benevolence_df = pd.DataFrame()

        # Process each selected sheet
        for sheet in selected_sheets:
            # Load the sheet, skipping the first three rows
            df = pd.read_excel(uploaded_file, sheet_name=sheet, skiprows=3)
            # Concatenate each DataFrame to the consolidated DataFrame
            benevolence_df = pd.concat([benevolence_df, df], ignore_index=True)      
        
        st.dataframe(benevolence_df)
        
        # Count values for Attendees, Guests, and Non-Attendees
        attendee_count = benevolence_df.iloc[:, 2].value_counts().get("Attendee", 0)
        guest_count = benevolence_df.iloc[:, 2].value_counts().get("Guest", 0)
        non_attendee_count = benevolence_df.iloc[:, 2].value_counts().get("Non Attendee", 0)
        
        # Calculate the total contacts
        total_contacts = attendee_count + guest_count + non_attendee_count
        
        # Convert relevant columns to strings to avoid errors
        benevolence_df.iloc[:, 4] = benevolence_df.iloc[:, 4].astype(str)
        benevolence_df.iloc[:, 5] = benevolence_df.iloc[:, 5].astype(str)
        benevolence_df.iloc[:, 6] = benevolence_df.iloc[:, 6].astype(str)
        benevolence_df.iloc[:, 7] = benevolence_df.iloc[:, 7].astype(str)
        benevolence_df.iloc[:, 8] = benevolence_df.iloc[:, 8].astype(str)
        
        # Count occurrences of "Yes" for each column
        hospital_visit_count = benevolence_df.iloc[:, 4].str.count("Yes").sum()
        home_visit_count = benevolence_df.iloc[:, 5].str.count("Yes").sum()
        public_visit_count = benevolence_df.iloc[:, 6].str.count("Yes").sum()
        prayed_for_count = benevolence_df.iloc[:, 7].str.count("Yes").sum()
        accepted_christ_count = benevolence_df.iloc[:, 8].str.count("Yes").sum()
        
        # Create a summary table using a DataFrame
        summary_data = {
            "Category": ["Regular Attendee", "Guest", "Non-Attendee", "Contacts", 
                         "Hospital Visit", "Home Visit", "Public Visit", "Prayed For", "Accepted Christ"],
            "Count": [attendee_count, guest_count, non_attendee_count, total_contacts, 
                      hospital_visit_count, home_visit_count, public_visit_count, prayed_for_count, accepted_christ_count]
        }
        summary_df = pd.DataFrame(summary_data)
        
        # Display the summary table
        st.write("Summary Table")
        st.table(summary_df)

if __name__ == "__main__":
    main()
