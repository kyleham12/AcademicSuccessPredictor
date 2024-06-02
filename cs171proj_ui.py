import tkinter as tk
from tkinter import messagebox, font
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import load_model
import pandas as pd

label_encoder_app_mode = LabelEncoder()
app_mode_options = ["1 - 1st phase - general contingent", "2 - Ordinance No. 612/93", "5 - 1st phase - special contingent (Azores Island)", "7 - Holders of other higher courses", "10 - Ordinance No. 854-B/99", "15 - International student (bachelor)", "16 - 1st phase - special contingent (Madeira Island)", "17 - 2nd phase - general contingent", "18 - 3rd phase - general contingent", "26 - Ordinance No. 533-A/99, item b2) (Different Plan)", "27 - Ordinance No. 533-A/99, item b3 (Other Institution)", "39 - Over 23 years old", "42 - Transfer", "43 - Change of course", "44 - Technological specialization diploma holders", "51 - Change of institution/course", "53 - Short cycle diploma holders", "57 - Change of institution/course (International)"]
label_encoder_app_mode.fit(app_mode_options)

label_encoder_course = LabelEncoder()
course_options = ["33 - Biofuel Production Technologies", "171 - Animation and Multimedia Design", "8014 - Social Service (evening attendance)", "9003 - Agronomy", "9070 - Communication Design", "9085 - Veterinary Nursing", "9119 - Informatics Engineering", "9130 - Equinculture", "9147 - Management", "9238 - Social Service", "9254 - Tourism", "9500 - Nursing", "9556 - Oral Hygiene", "9670 - Advertising and Marketing Management", "9773 - Journalism and Communication", "9853 - Basic Education", "9991 - Management (evening attendance)"]
label_encoder_course.fit(course_options)

label_encoder_prev_qual = LabelEncoder()
prev_qual_options = ["1 - Secondary education", "2 - Higher education - bachelor's degree", "3 - Higher education - degree", "4 - Higher education - master's", "5 - Higher education - doctorate", "6 - Frequency of higher education", "9 - 12th year of schooling - not completed", "10 - 11th year of schooling - not completed", "12 - Other - 11th year of schooling", "14 - 10th year of schooling", "15 - 10th year of schooling - not completed", "19 - Basic education 3rd cycle (9th/10th/11th year) or equiv.", "38 - Basic education 2nd cycle (6th/7th/8th year) or equiv.", "39 - Technological specialization course", "40 - Higher education - degree (1st cycle)", "42 - Professional higher technical course", "43 - Higher education - master (2nd cycle)"]
label_encoder_prev_qual.fit(prev_qual_options)

label_encoder_mother_qual = LabelEncoder()
mother_qual_options = ["1 - Secondary Education - 12th Year of Schooling or Eq.", "2 - Higher Education - Bachelor's Degree", "3 - Higher Education - Degree", "4 - Higher Education - Master's", "5 - Higher Education - Doctorate", "6 - Frequency of Higher Education", "9 - 12th Year of Schooling - Not Completed", "10 - 11th Year of Schooling - Not Completed", "11 - 7th Year (Old)", "12 - Other - 11th Year of Schooling", "14 - 10th Year of Schooling", "18 - General commerce course", "19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.", "22 - Technical-professional course", "26 - 7th year of schooling", "27 - 2nd cycle of the general high school course", "29 - 9th Year of Schooling - Not Completed", "30 - 8th year of schooling", "34 - Unknown", "35 - Can't read or write", "36 - Can read without having a 4th year of schooling", "37 - Basic education 1st cycle (4th/5th year) or equiv.", "38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.", "39 - Technological specialization course", "40 - Higher education - degree (1st cycle)", "41 - Specialized higher studies course", "42 - Professional higher technical course", "43 - Higher Education - Master (2nd cycle)", "44 - Higher Education - Doctorate (3rd cycle)"]
label_encoder_mother_qual.fit(mother_qual_options)

label_encoder_father_qual = LabelEncoder()
father_qual_options = ["1 - Secondary Education - 12th Year of Schooling or Eq." ,"2 - Higher Education - Bachelor's Degree", "3 - Higher Education - Degree", "4 - Higher Education - Master's", "5 - Higher Education - Doctorate", "6 - Frequency of Higher Education", "9 - 12th Year of Schooling - Not Completed", "10 - 11th Year of Schooling - Not Completed", "11 - 7th Year (Old)", "12 - Other - 11th Year of Schooling", "13 - 2nd year complementary high school course", "14 - 10th Year of Schooling", "18 - General commerce course", "19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.", "20 - Complementary High School Course", "22 - Technical-professional course", "25 - Complementary High School Course - not concluded", "26 - 7th year of schooling", "27 - 2nd cycle of the general high school course", "29 - 9th Year of Schooling - Not Completed", "30 - 8th year of schooling", "31 - General Course of Administration and Commerce", "33 - Supplementary Accounting and Administration", "34 - Unknown", "35 - Can't read or write", "36 - Can read without having a 4th year of schooling", "37 - Basic education 1st cycle (4th/5th year) or equiv.", "38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.", "39 - Technological specialization course", "40 - Higher education - degree (1st cycle)", "41 - Specialized higher studies course", "42 - Professional higher technical course", "43 - Higher Education - Master (2nd cycle)", "44 - Higher Education - Doctorate (3rd cycle)"]
label_encoder_father_qual.fit(father_qual_options)

label_encoder_tuition_fees = LabelEncoder()
tuition_fees_options = ["1 - Yes", "0 - No"]
label_encoder_tuition_fees.fit(tuition_fees_options)

label_encoder_mother_occu = LabelEncoder()
mother_occu_options = ["0 - Student", "1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers", "2 - Specialists in Intellectual and Scientific Activities", "3 - Intermediate Level Technicians and Professions", "4 - Administrative staff", "5 - Personal Services, Security and Safety Workers and Sellers", "6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", "7 - Skilled Workers in Industry, Construction and Craftsmen", "8 - Installation and Machine Operators and Assembly Workers", "9 - Unskilled Workers", "10 - Armed Forces Professions", "90 - Other Situation", "99 - (blank)", "122 - Health professionals", "123 - teachers", "125 - Specialists in information and communication technologies (ICT)", "131 - Intermediate level science and engineering technicians and professions", "132 - Technicians and professionals, of intermediate level of health", "134 - Intermediate level technicians from legal, social, sports, cultural and similar services", "141 - Office workers, secretaries in general and data processing operators", "143 - Data, accounting, statistical, financial services and registry-related operators", "144 - Other administrative support staff", "151 - personal service workers", "152 - sellers", "153 - Personal care workers and the like", "171 - Skilled construction workers and the like, except electricians", "173 - Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like", "175 - Workers in food processing, woodworking, clothing and other industries and crafts", "191 - cleaning workers", "192 - Unskilled workers in agriculture, animal production, fisheries and forestry", "193 - Unskilled workers in extractive industry, construction, manufacturing and transport", "194 - Meal preparation assistants"]
label_encoder_mother_occu.fit(mother_occu_options)

label_encoder_father_occu = LabelEncoder()
father_occu_options = ["0 - Student", "1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers", "2 - Specialists in Intellectual and Scientific Activities", "3 - Intermediate Level Technicians and Professions", "4 - Administrative staff", "5 - Personal Services, Security and Safety Workers and Sellers", "6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", "7 - Skilled Workers in Industry, Construction and Craftsmen", "8 - Installation and Machine Operators and Assembly Workers", "9 - Unskilled Workers", "10 - Armed Forces Professions", "90 - Other Situation", "99 - (blank)", "101 - Armed Forces Officers", "102 - Armed Forces Sergeants", "103 - Other Armed Forces personnel", "112 - Directors of administrative and commercial services", "114 - Hotel, catering, trade and other services directors", "121 - Specialists in the physical sciences, mathematics, engineering and related techniques", "122 - Health professionals", "123 - teachers", "124 - Specialists in finance, accounting, administrative organization, public and commercial relations", "131 - Intermediate level science and engineering technicians and professions", "132 - Technicians and professionals, of intermediate level of health", "134 - Intermediate level technicians from legal, social, sports, cultural and similar services", "135 - Information and communication technology technicians", "141 - Office workers, secretaries in general and data processing operators", "143 - Data, accounting, statistical, financial services and registry-related operators", "144 - Other administrative support staff", "151 - personal service workers", "152 - sellers", "153 - Personal care workers and the like", "154 - Protection and security services personnel", "161 - Market-oriented farmers and skilled agricultural and animal production workers", "163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence", "171 - Skilled construction workers and the like, except electricians", "172 - Skilled workers in metallurgy, metalworking and similar", "174 - Skilled workers in electricity and electronics", "175 - Workers in food processing, woodworking, clothing and other industries and crafts", "181 - Fixed plant and machine operators", "182 - assembly workers", "183 - Vehicle drivers and mobile equipment operators", "192 - Unskilled workers in agriculture, animal production, fisheries and forestry", "193 - Unskilled workers in extractive industry, construction, manufacturing and transport", "194 - Meal preparation assistants", "195 - Street vendors (except food) and street service providers"]
label_encoder_father_occu.fit(father_occu_options)

label_encoder_gender = LabelEncoder()
gender_options = ["1 - Male", "0 - Female", "2 - Other", "3 - Prefer not to say"]
label_encoder_gender.fit(gender_options)

label_encoder_scholarship_holder = LabelEncoder()
scholarship_holder_options = ["1 - Yes", "0 - No"]
label_encoder_scholarship_holder.fit(scholarship_holder_options)

scaler = StandardScaler()

fnn_model = load_model('fnn_model.h5')

def predict_outcome():
    try:
        application_mode_encoded = entry_vars['Application mode'].get()
        course_encoded = entry_vars['Course'].get()
        prev_qual_encoded = entry_vars["Previous Qualification"].get()
        mother_qual_encoded = entry_vars["Mother's Qualification"].get()
        father_qual_encoded = entry_vars["Mother's Qualification"].get()
        tuition_fees_encoded = entry_vars['Tuition fees up to date'].get()
        mother_occu_encoded = entry_vars["Mother's Occupation"].get()
        father_occu_encoded = entry_vars["Father's Occupation"].get()
        gender_encoded = entry_vars["Gender"].get()
        scholarship_holder_encoded = entry_vars["Scholarship holder"].get()
        age_at_enrollment = entry_vars["Age at enrollment"].get()
        first_sem_units = entry_vars["Curricular units 1st sem (approved)"].get()
        second_sem_units = entry_vars["Curricular units 2nd sem (approved)"].get()

        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'Application mode': [int(application_mode_encoded)],
            'Course': [int(course_encoded)],
            "Previous Qualification": [int(prev_qual_encoded)],
            "Mother's Qualification": [int(mother_qual_encoded)],
            "Father's Qualification": [int(father_qual_encoded)],
            "Tuition fees up to date": [int(tuition_fees_encoded)],
            "Mother's Occupation": [int(mother_occu_encoded)],
            "Father's Occupation": [int(father_occu_encoded)],
            "Gender": [int(gender_encoded)],
            "Scholarship holder": [int(scholarship_holder_encoded)],
            "Age at enrollment": [int(age_at_enrollment)],
            "Curricular units 1st sem (approved)": [int(first_sem_units)],
            "Curricular units 2nd sem (approved)": [int(second_sem_units)]
        })
        
        input_data_scaled = scaler.fit_transform(input_data)

        prediction = fnn_model.predict(input_data_scaled)

        outcome_label.config(text=f"Predicted Outcome: {'Graduation' if prediction > 0.5 else 'Dropout'}")

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def on_option_selected(field_name, event):
    selected_option = dropdown_vars[field_name].get()
    numeric_part = selected_option.split(' ', 1)[0]
    entry_vars[field_name].set(numeric_part)

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Create the main window
root = tk.Tk()
root.title("Student Outcome Prediction")

canvas = tk.Canvas(root, height=300, width=400)
canvas.pack(side=tk.LEFT, fill=tk.Y)

# Create a Scrollbar and associate it with the Canvas
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a Frame inside the Canvas to hold your UI components
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

dropdown_vars = {
    'Application mode': tk.StringVar(frame),
    'Course': tk.StringVar(frame),
    "Previous Qualification": tk.StringVar(frame),
    "Mother's Qualification": tk.StringVar(frame),
    "Father's Qualification": tk.StringVar(frame),
    "Tuition fees up to date": tk.StringVar(frame),
    "Mother's Occupation": tk.StringVar(frame),
    "Father's Occupation": tk.StringVar(frame),
    "Gender": tk.StringVar(frame),
    "Scholarship holder": tk.StringVar(frame),
    "Age at enrollment": tk.StringVar(frame),
    "Curricular units 1st sem (approved)": tk.StringVar(frame),
    "Curricular units 2nd sem (approved)": tk.StringVar(frame)
}

# Dictionary to store StringVars for entry widgets
entry_vars = {
    'Application mode': tk.StringVar(frame),
    'Course': tk.StringVar(frame),
    "Previous Qualification": tk.StringVar(frame),
    "Mother's Qualification": tk.StringVar(frame),
    "Father's Qualification": tk.StringVar(frame),
    "Tuition fees up to date": tk.StringVar(frame),
    "Mother's Occupation": tk.StringVar(frame),
    "Father's Occupation": tk.StringVar(frame),
    "Gender": tk.StringVar(frame),
    "Scholarship holder": tk.StringVar(frame),
    "Age at enrollment": tk.StringVar(frame),
    "Curricular units 1st sem (approved)": tk.StringVar(frame),
    "Curricular units 2nd sem (approved)": tk.StringVar(frame)
}

for field_name, options in zip(['Application mode', 'Course', "Previous Qualification", "Mother's Qualification", "Father's Qualification", "Tuition fees up to date", "Mother's Occupation", "Father's Occupation", "Gender", "Scholarship holder"], [app_mode_options, course_options, prev_qual_options, mother_qual_options, father_qual_options, tuition_fees_options, mother_occu_options, father_occu_options, gender_options, scholarship_holder_options]):
    
    dropdown_vars[f"{field_name}"].set("Choose Option")
    
    label = tk.Label(frame, text=f"{field_name}")
    label.pack()
    
    option_menu = tk.OptionMenu(frame, dropdown_vars[field_name], *options)
    option_menu.pack()

    entry_widget = tk.Entry(frame, textvariable=entry_vars[field_name])
    entry_widget.pack()

    dropdown_vars[field_name].trace_add('write', lambda *args, field_name=field_name: on_option_selected(field_name, args))

number_label_age = tk.Label(frame, text="Age at enrollment")
number_label_age.pack()
entry_number_age = tk.Entry(frame, textvariable=entry_vars["Age at enrollment"])
entry_number_age.pack()

number_label_first_sem = tk.Label(frame, text="Curricular units 1st sem (approved)")
number_label_first_sem.pack()
entry_number_first_sem = tk.Entry(frame, textvariable=entry_vars["Curricular units 1st sem (approved)"])
entry_number_first_sem.pack()

number_label_second_sem = tk.Label(frame, text="Curricular units 2nd sem (approved)")
number_label_second_sem.pack()
entry_number_second_sem = tk.Entry(frame, textvariable=entry_vars["Curricular units 2nd sem (approved)"])
entry_number_second_sem.pack()

tk.Label(root, text="Welcome to the Graduation Prediction Tool!\n\n", font=font.Font(size=20, weight="bold")).pack()

tk.Label(root, text="                                             What is this tool?\n\nThis tool is designed to predict whether or not college students will graduate college based on the criteria on the left. This tool should be used to help guide students in their future in college, whether that be to continue their collegiate journey or to seek other options. Whichever case, this tool shouldn't be viewed as a crystal ball where the student's fate in question has been decided, rather it should encourage the student to take the approriate steps regarding their education.\n\n", font=font.Font(size=12), justify=tk.LEFT, wraplength=500).pack(padx=10, pady=10)

tk.Label(root, text="                                           How does this tool work?\n\nTo start using the tool, use the menu on the left-hand side to input the student's information. The information in each of the textboxes should be a number corresponding to the choices provided to you by the dropdown menus. Once there are the correct numbers in each of the boxes for the student, you can now press the 'Predict Outcome' button to receive the prediction for the student's collegiate outcome. You can use the tool for multiple students by changing the numbers, and when you are done, you can press the exit button in the top right corner.", font=font.Font(size=12), justify=tk.LEFT, wraplength=500).pack(padx=10, pady=10)

tk.Button(root, text="Predict Outcome", command=predict_outcome).pack()

outcome_label = tk.Label(root, text="", font=font.Font(size=15))
outcome_label.pack()

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

canvas.bind("<MouseWheel>", on_mousewheel)

root.mainloop()
