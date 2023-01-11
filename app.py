import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image

model = pickle.load(open("job_postings.pkl", "rb"))
app_mode = st.sidebar.radio('Select Page', ['Home', 'Prediction'])
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)
if app_mode == 'Home':
    html_temp = """
        <div style='background-color: teal; padding:10px'>
        <h2 style='color:white; text-align:center;'>Job Posting Classifier: </h2>
        <h3 style='color:white; text-align:center;'>Real/Fake </h3>
        </div>"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image("""https://imagevars.gulfnews.com/2020/09/07/Fake-job-offer_1746917114d_original-ratio.jpg""")

elif app_mode == 'Prediction':
    def add_bg_from_url():
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background-image: url("https://res.cloudinary.com/jerrick/image/upload/c_scale,q_auto/5e68f566ddce58001c542e16.jpg");
                 background-attachment: fixed;
                 background-size: cover
             }}
             </style>
             """,
            unsafe_allow_html=True
        )


    add_bg_from_url()
    st.title('Job Posting Classifier: Real/Fake')
    st.markdown("For predicting if job posting is real/fake please enter the details.")
    st.subheader('Enter the details:')

    telecommuting = st.radio('Is work from home or remote work allowed?', options=['Yes', 'No'])
    if telecommuting == 'Yes':
        telecommuting = 1
    else:
        telecommuting = 0

    has_company_logo = st.radio('Does the job posting have a company logo?', options=['Yes', 'No'])
    if has_company_logo == 'Yes':
        has_company_logo = 1
    else:
        has_company_logo = 0

    has_questions = st.radio('Does the job posting have questions?', options=['Yes', 'No'])
    if has_questions == 'Yes':
        has_questions = 1
    else:
        has_questions = 0

    employment_type = st.selectbox('What is the employment type?',
                                   ('Select', 'Contract', 'Not Specified', 'Full-time', 'Other', 'Part-time',
                                    'Temporary'))
    # Set dummy variables to zero
    employment_type_Contract, employment_type_Not_Specified = 0, 0
    employment_type_Full_time, employment_type_Other = 0, 0
    employment_type_Part_time, employment_type_Temporary = 0, 0

    if employment_type == 'Contract':
        employment_type_Contract = 1
    elif employment_type == 'Not_Specified':
        employment_type_Not_Specified = 1
    elif employment_type == 'Full-time':
        employment_type_Full_time = 1
    elif employment_type == 'Other':
        employment_type_Other = 1
    elif employment_type == 'Part-time':
        employment_type_Part_time = 1
    elif employment_type == 'Temporary':
        employment_type_Temporary = 1

    required_experience = st.selectbox('What is the required experience?',
                                       ('Select', 'Not Applicable', 'Internship', 'Entry level', 'Mid-Senior level',
                                        'Associate', 'Executive', 'Director', 'Not_Specified'))

    required_experience_Not_Applicable, required_experience_Not_Specified = 0, 0
    required_experience_Internship, required_experience_Entry_level = 0, 0
    required_experience_Mid_Senior_level, required_experience_Associate = 0, 0
    required_experience_Executive, required_experience_Director = 0, 0

    if required_experience == 'Not Applicable':
        required_experience_Not_Applicable = 1
    elif required_experience == 'Internship':
        required_experience_Internship = 1
    elif required_experience == 'Entry level':
        required_experience_Entry_level = 1
    elif required_experience == 'Mid-Senior level':
        required_experience_Mid_Senior_level = 1
    elif required_experience == 'Associate':
        required_experience_Associate = 1
    elif required_experience == 'Executive':
        required_experience_Executive = 1
    elif required_experience == 'Director':
        required_experience_Director = 1
    elif required_experience == 'Not_Specified':
        required_experience_Not_Specified = 1

    required_education = st.selectbox('What is the required education?',
                                      (
                                      'Select', 'Unspecified', 'Vocational - HS Diploma', 'Some High School Coursework',
                                      'High School or equivalent',
                                      'Some College Coursework Completed', 'Certification', 'Vocational',
                                      'Vocational - Degree', "Bachelor's Degree",
                                      "Master's Degree", 'Associate Degree', 'Professional', 'Doctorate',
                                      'Not_Specified'))

    required_education_Unspecified, required_education_Vocational___HS_Diploma = 0, 0
    required_education_Some_High_School_Coursework, required_education_High_School_or_equivalent = 0, 0
    required_education_Some_College_Coursework_Completed, required_education_Certification = 0, 0
    required_education_Bachelor_s_Degree, required_education_Master_s_Degree = 0, 0
    required_education_Vocational, required_education_Vocational___Degree = 0, 0
    required_education_Associate_Degree, required_education_Professional = 0, 0
    required_education_Doctorate, required_education_Not_Specified = 0, 0

    if required_education == 'Unspecified':
        required_education_Unspecified = 1
    elif required_education == 'Vocational - HS Diploma':
        required_education_Vocational___HS_Diploma = 1
    elif required_education == 'Some High School Coursework':
        required_education_Some_High_School_Coursework = 1
    elif required_education == 'High School or equivalent':
        required_education_High_School_or_equivalent = 1
    elif required_education == 'Some College Coursework Completed':
        required_education_Some_College_Coursework_Completed = 1
    elif required_education == 'Certification':
        required_education_Certification = 1
    elif required_education == "Bachelor's Degree":
        required_education_Bachelor_s_Degree = 1
    elif required_education == 'Vocational - Degree':
        required_education_Vocational___Degree = 1
    elif required_education == "Master's Degree":
        required_education_Master_s_Degree = 1
    elif required_education == 'Vocational':
        required_education_Vocational = 1
    elif required_education == 'Associate Degree':
        required_education_Associate_Degree = 1
    elif required_education == 'Professional':
        required_education_Professional = 1
    elif required_education == 'Doctorate':
        required_education_Doctorate = 1
    elif required_education == 'Not_Specified':
        required_education_Not_Specified = 1

    industry = st.selectbox("'Please choose which industry the job posting is relevant to?",
                            ("Select", "Not_Specified", "Marketing and Advertising", "Computer Software",
                             "Hospital & Health Care", "Online Media", "Information Technology and Services",
                             "Financial Services", "Management Consulting",
                             "Events Services", "Internet", "Facilities Services", "Consumer Electronics",
                             "Telecommunications", "Consumer Services", "Construction",
                             "Oil & Energy", "Education Management", "Building Materials", "Banking",
                             "Food & Beverages", "Food Production",
                             "Health, Wellness and Fitness", "Insurance", "E-Learning", "Cosmetics",
                             "Staffing and Recruiting",
                             "Venture Capital & Private Equity", "Leisure, Travel & Tourism", "Human Resources",
                             "Pharmaceuticals", "Farming", "Legal Services",
                             "Luxury Goods & Jewelry", "Machinery", "Real Estate",
                             "Mechanical or Industrial Engineering", "Public Relations and Communications",
                             "Consumer Goods", "Medical Practice", "Electrical/Electronic Manufacturing", "Hospitality",
                             "Music", "Market Research", "Automotive",
                             "Philanthropy", "Utilities", "Primary/Secondary Education", "Logistics and Supply Chain",
                             "Design", "Gambling & Casinos", "Accounting",
                             "Environmental Services", "Mental Health Care", "Investment Management",
                             "Apparel & Fashion", "Media Production",
                             "Publishing", "Medical Devices", "Information Services", "Retail", "Sports",
                             "Computer Games", "Chemicals", "Aviation & Aerospace",
                             "Business Supplies and Equipment", "Program Development", "Computer Networking",
                             "Biotechnology", "Civic & Social Organization", "Religious Institutions",
                             "Warehousing", "Airlines/Aviation", "Writing and Editing", "Restaurants",
                             "Outsourcing/Offshoring", "Transportation/Trucking/Railroad",
                             "Wireless", "Investment Banking", "Nonprofit Organization Management", "Libraries",
                             "Computer Hardware", "Broadcast Media", "Printing",
                             "Graphic Design", "Entertainment", "Wholesale", "Research", "Animation",
                             "Government Administration", "Capital Markets",
                             "Computer & Network Security", "Semiconductors", "Security and Investigations",
                             "Architecture & Planning",
                             "Maritime", "Fund-Raising", "Higher Education", "Renewables & Environment",
                             "Motion Pictures and Film",
                             "Law Practice", "Government Relations", "Packaging and Containers", "Sporting Goods",
                             "Mining & Metals", "Import and Export",
                             "International Trade and Development", "Professional Training & Coaching", "Textiles",
                             "Commercial Real Estate", "Law Enforcement",
                             "Package/Freight Delivery", "Translation and Localization", "Photography",
                             "Industrial Automation", "Wine and Spirits", "Public Safety", "Civil Engineering",
                             "Military",
                             "Defense & Space", "Veterinary", "Executive Office", "Performing Arts",
                             "Individual & Family Services", "Public Policy",
                             "Nanotechnology", "Museums and Institutions", "Fishery", "Plastics", "Furniture",
                             "Shipbuilding", "Alternative Dispute Resolution", "Ranching"))

    industry_Not_Specified, industry_Marketing_and_Advertising, industry_Computer_Software = 0, 0, 0
    industry_Hospital___Health_Care, industry_Online_Media, industry_Information_Technology_and_Services = 0, 0, 0
    industry_Financial_Services, industry_Management_Consulting, industry_Events_Services = 0, 0, 0
    industry_Internet, industry_Facilities_Services, industry_Consumer_Electronics = 0, 0, 0
    industry_Telecommunications, industry_Consumer_Services, industry_Construction = 0, 0, 0
    industry_Oil___Energy, industry_Education_Management, industry_Building_Materials = 0, 0, 0
    industry_Banking, industry_Food___Beverages, industry_Food_Production = 0, 0, 0
    industry_Health__Wellness_and_Fitness, industry_Insurance, industry_E_Learning = 0, 0, 0
    industry_Cosmetics, industry_Staffing_and_Recruiting, industry_Venture_Capital___Private_Equity = 0, 0, 0
    industry_Leisure_Travel___Tourism, industry_Human_Resources, industry_Pharmaceuticals = 0, 0, 0
    industry_Farming, industry_Legal_Services, industry_Luxury_Goods___Jewelry, industry_Machinery = 0, 0, 0, 0
    industry_Real_Estate, industry_Mechanical_or_Industrial_Engineering, industry_Public_Relations_and_Communications = 0, 0, 0
    industry_Consumer_Goods, industry_Medical_Practice, industry_Electrical_Electronic_Manufacturing = 0, 0, 0
    industry_Hospitality, industry_Music, industry_Market_Research, industry_Automotive = 0, 0, 0, 0
    industry_Philanthropy, industry_Utilities, industry_Primary_Secondary_Education = 0, 0, 0
    industry_Logistics_and_Supply_Chain, industry_Design, industry_Gambling___Casinos, industry_Accounting = 0, 0, 0, 0
    industry_Environmental_Services, industry_Mental_Health_Care, industry_Investment_Management = 0, 0, 0
    industry_Apparel___Fashion, industry_Media_Production, industry_Publishing = 0, 0, 0
    industry_Medical_Devices, industry_Information_Services, industry_Retail, industry_Sports = 0, 0, 0, 0
    industry_Computer_Games, industry_Chemicals, industry_Aviation___Aerospace, industry_Business_Supplies_and_Equipment = 0, 0, 0, 0
    industry_Program_Development, industry_Computer_Networking, industry_Biotechnology = 0, 0, 0
    industry_Civic___Social_Organization, industry_Religious_Institutions, industry_Warehousing = 0, 0, 0
    industry_Airlines_Aviation, industry_Writing_and_Editing, industry_Restaurants = 0, 0, 0
    industry_Outsourcing_Offshoring, industry_Transportation_Trucking_Railroad, industry_Wireless = 0, 0, 0
    industry_Investment_Banking, industry_Nonprofit_Organization_Management, industry_Libraries = 0, 0, 0
    industry_Computer_Hardware, industry_Broadcast_Media, industry_Printing = 0, 0, 0
    industry_Graphic_Design, industry_Entertainment, industry_Wholesale, industry_Research, industry_Animation = 0, 0, 0, 0, 0
    industry_Government_Administration, industry_Capital_Markets, industry_Computer___Network_Security = 0, 0, 0
    industry_Semiconductors, industry_Security_and_Investigations, industry_Architecture___Planning = 0, 0, 0
    industry_Maritime, industry_Fund_Raising, industry_Higher_Education, industry_Renewables___Environment = 0, 0, 0, 0
    industry_Motion_Pictures_and_Film, industry_Law_Practice, industry_Government_Relations = 0, 0, 0
    industry_Packaging_and_Containers, industry_Sporting_Goods, industry_Mining___Metals = 0, 0, 0
    industry_Import_and_Export, industry_International_Trade_and_Development, industry_Professional_Training___Coaching = 0, 0, 0
    industry_Textiles, industry_Commercial_Real_Estate = 0, 0
    industry_Law_Enforcement, industry_Package_Freight_Delivery, industry_Translation_and_Localization = 0, 0, 0
    industry_Photography, industry_Industrial_Automation, industry_Wine_and_Spirits = 0, 0, 0
    industry_Public_Safety, industry_Civil_Engineering, industry_Military = 0, 0, 0
    industry_Defense___Space, industry_Veterinary, industry_Executive_Office = 0, 0, 0
    industry_Performing_Arts, industry_Individual___Family_Services, industry_Public_Policy = 0, 0, 0
    industry_Nanotechnology, industry_Museums_and_Institutions, industry_Fishery = 0, 0, 0
    industry_Plastics, industry_Furniture, industry_Shipbuilding = 0, 0, 0
    industry_Alternative_Dispute_Resolution, industry_Ranching = 0, 0

    if industry == "Not_Specified":
        industry_Not_Specified = 1
    elif industry == "Marketing and Advertising":
        industry_Marketing_and_Advertising = 1
    elif industry == "Computer Software":
        industry_Computer_Software = 1
    elif industry == "Hospital & Health Care":
        industry_Hospital___Health_Care = 1
    elif industry == "Online Media":
        industry_Online_Media = 1
    elif industry == "Information Technology and Services":
        industry_Information_Technology_and_Services = 1
    elif industry == "Financial Services":
        industry_Financial_Services = 1
    elif industry == "Management Consulting":
        industry_Management_Consulting = 1
    elif industry == "Events Services":
        industry_Events_Services = 1
    elif industry == "Internet":
        industry_Internet = 1
    elif industry == "Facilities Services":
        industry_Facilities_Services = 1
    elif industry == "Consumer Electronics":
        industry_Consumer_Electronics = 1
    elif industry == "Telecommunications":
        industry_Telecommunications = 1
    elif industry == "Consumer Services":
        industry_Consumer_Services = 1
    elif industry == "Construction":
        industry_Construction = 1
    elif industry == "Oil & Energy":
        industry_Oil___Energy = 1
    elif industry == "Education Management":
        industry_Education_Management = 1
    elif industry == "Building Materials":
        industry_Building_Materials = 1
    elif industry == "Banking":
        industry_Banking = 1
    elif industry == "Food & Beverages":
        industry_Food___Beverages = 1
    elif industry == "Food Production":
        industry_Food_Production = 1
    elif industry == "Health, Wellness and Fitness":
        industry_Health__Wellness_and_Fitness = 1
    elif industry == "Insurance":
        industry_Insurance = 1
    elif industry == "E-Learning":
        industry_E_Learning = 1
    elif industry == "Cosmetics":
        industry_Cosmetics = 1
    elif industry == "Staffing and Recruiting":
        industry_Staffing_and_Recruiting = 1
    elif industry == "Venture Capital & Private Equity":
        industry_Venture_Capital___Private_Equity = 1
    elif industry == "Leisure, Travel & Tourism":
        industry_Leisure_Travel___Tourism = 1
    elif industry == "Human Resources":
        industry_Human_Resources = 1
    elif industry == "Pharmaceuticals":
        industry_Pharmaceuticals = 1
    elif industry == "Farming":
        industry_Farming = 1
    elif industry == "Legal Services":
        industry_Legal_Services = 1
    elif industry == "Luxury Goods & Jewelry":
        industry_Luxury_Goods___Jewelry = 1
    elif industry == "Machinery":
        industry_Machinery = 1
    elif industry == "Real Estate":
        industry_Real_Estate = 1
    elif industry == "Mechanical or Industrial Engineering":
        industry_Mechanical_or_Industrial_Engineering = 1
    elif industry == "Public Relations and Communications":
        industry_Public_Relations_and_Communications = 1
    elif industry == "Consumer Goods":
        industry_Consumer_Goods = 1
    elif industry == "Medical Practice":
        industry_Medical_Practice = 1
    elif industry == "Electrical/Electronic Manufacturing":
        industry_Electrical_Electronic_Manufacturing = 1
    elif industry == "Hospitality":
        industry_Hospitality = 1
    elif industry == "Music":
        industry_Music = 1
    elif industry == "Market Research":
        industry_Market_Research = 1
    elif industry == "Automotive":
        industry_Automotive = 1
    elif industry == "Philanthropy":
        industry_Philanthropy = 1
    elif industry == "Utilities":
        industry_Utilities = 1
    elif industry == "Primary/Secondary Education":
        industry_Primary_Secondary_Education = 1
    elif industry == "Logistics and Supply Chain":
        industry_Logistics_and_Supply_Chain = 1
    elif industry == "Design":
        industry_Design = 1
    elif industry == "Gambling & Casinos":
        industry_Gambling___Casinos = 1
    elif industry == "Accounting":
        industry_Accounting = 1
    elif industry == "Environmental Services":
        industry_Environmental_Services = 1
    elif industry == "Mental Health Care":
        industry_Mental_Health_Care = 1
    elif industry == "Investment Management":
        industry_Investment_Management = 1
    elif industry == "Apparel & Fashion":
        industry_Apparel___Fashion = 1
    elif industry == "Media Production":
        industry_Media_Production = 1
    elif industry == "Publishing":
        industry_Publishing = 1
    elif industry == "Medical Devices":
        industry_Medical_Devices = 1
    elif industry == "Information Services":
        industry_Information_Services = 1
    elif industry == "Retail":
        industry_Retail = 1
    elif industry == "Sports":
        industry_Sports = 1
    elif industry == "Computer Games":
        industry_Computer_Games = 1
    elif industry == "Chemicals":
        industry_Chemicals = 1
    elif industry == "Aviation & Aerospace":
        industry_Aviation___Aerospace = 1
    elif industry == "Business Supplies and Equipment":
        industry_Business_Supplies_and_Equipment = 1
    elif industry == "Program Development":
        industry_Program_Development = 1
    elif industry == "Computer Networking":
        industry_Computer_Networking = 1
    elif industry == "Biotechnology":
        industry_Biotechnology = 1
    elif industry == "Civic & Social Organization":
        industry_Civic___Social_Organization = 1
    elif industry == "Religious Institutions":
        industry_Religious_Institutions = 1
    elif industry == "Warehousing":
        industry_Warehousing = 1
    elif industry == "Airlines/Aviation":
        industry_Airlines_Aviation = 1
    elif industry == "Writing and Editing":
        industry_Writing_and_Editing = 1
    elif industry == "Restaurants":
        industry_Restaurants = 1
    elif industry == "Outsourcing/Offshoring":
        industry_Outsourcing_Offshoring = 1
    elif industry == "Transportation/Trucking/Railroad":
        industry_Transportation_Trucking_Railroad = 1
    elif industry == "Wireless":
        industry_Wireless = 1
    elif industry == "Investment Banking":
        industry_Investment_Banking = 1
    elif industry == "Nonprofit Organization Management":
        industry_Nonprofit_Organization_Management = 1
    elif industry == "Libraries":
        industry_Libraries = 1
    elif industry == "Computer Hardware":
        industry_Computer_Hardware = 1
    elif industry == "Broadcast Media":
        industry_Broadcast_Media = 1
    elif industry == "Printing":
        industry_Printing = 1
    elif industry == "Graphic Design":
        industry_Graphic_Design = 1
    elif industry == "Entertainment":
        industry_Entertainment = 1
    elif industry == "Wholesale":
        industry_Wholesale = 1
    elif industry == "Research":
        industry_Research = 1
    elif industry == "Animation":
        industry_Animation = 1
    elif industry == "Government Administration":
        industry_Government_Administration = 1
    elif industry == "Capital Markets":
        industry_Capital_Markets = 1
    elif industry == "Computer & Network Security":
        industry_Computer___Network_Security = 1
    elif industry == "Semiconductors":
        industry_Semiconductors = 1
    elif industry == "Security and Investigations":
        industry_Security_and_Investigations = 1
    elif industry == "Architecture & Planning":
        industry_Architecture___Planning = 1
    elif industry == "Maritime":
        industry_Maritime = 1
    elif industry == "Fund-Raising":
        industry_Fund_Raising = 1
    elif industry == "Higher Education":
        industry_Higher_Education = 1
    elif industry == "Renewables & Environment":
        industry_Renewables___Environment = 1
    elif industry == "Motion Pictures and Film":
        industry_Motion_Pictures_and_Film = 1
    elif industry == "Law Practice":
        industry_Law_Practice = 1
    elif industry == "Government Relations":
        industry_Government_Relations = 1
    elif industry == "Packaging and Containers":
        industry_Packaging_and_Containers = 1
    elif industry == "Sporting Goods":
        industry_Sporting_Goods = 1
    elif industry == "Mining & Metals":
        industry_Mining___Metals = 1
    elif industry == "Import and Export":
        industry_Import_and_Export = 1
    elif industry == "International Trade and Development":
        industry_International_Trade_and_Development = 1
    elif industry == "Professional Training & Coaching":
        industry_Professional_Training___Coaching = 1
    elif industry == "Textiles":
        industry_Textiles = 1
    elif industry == "Commercial Real Estate":
        industry_Commercial_Real_Estate = 1
    elif industry == "Law Enforcement":
        industry_Law_Enforcement = 1
    elif industry == "Package/Freight Delivery":
        industry_Package_Freight_Delivery = 1
    elif industry == "Translation and Localization":
        industry_Translation_and_Localization = 1
    elif industry == "Photography":
        industry_Photography = 1
    elif industry == "Industrial Automation":
        industry_Industrial_Automation = 1
    elif industry == "Wine and Spirits":
        industry_Wine_and_Spirits = 1
    elif industry == "Public Safety":
        industry_Public_Safety = 1
    elif industry == "Civil Engineering":
        industry_Civil_Engineering = 1
    elif industry == "Military":
        industry_Military = 1
    elif industry == "Defense & Space":
        industry_Defense___Space = 1
    elif industry == "Veterinary":
        industry_Veterinary = 1
    elif industry == "Executive Office":
        industry_Executive_Office = 1
    elif industry == "Performing Arts":
        industry_Performing_Arts = 1
    elif industry == "Individual & Family Services":
        industry_Individual___Family_Services = 1
    elif industry == "Public Policy":
        industry_Public_Policy = 1
    elif industry == "Nanotechnology":
        industry_Nanotechnology = 1
    elif industry == "Museums and Institutions":
        industry_Museums_and_Institutions = 1
    elif industry == "Fishery":
        industry_Fishery = 1
    elif industry == "Plastics":
        industry_Plastics = 1
    elif industry == "Furniture":
        industry_Furniture = 1
    elif industry == "Shipbuilding":
        industry_Shipbuilding = 1
    elif industry == "Alternative Dispute Resolution":
        industry_Alternative_Dispute_Resolution = 1
    elif industry == "Ranching":
        industry_Ranching = 1

    function = st.selectbox("What Type Of Function Mentioned",
                            ("Select", "Marketing", "Customer Service", "Not_Specified",
                             "Sales", "Health Care Provider", "Management", "Information Technology", "Other",
                             "Engineering", "Administrative", "Design", "Production", "Education", "Supply Chain",
                             "Business Development", "Product Management", "Financial Analyst", "Consulting",
                             "Human Resources",
                             "Project Management", "Manufacturing", "Public Relations", "Strategy/Planning",
                             "Advertising",
                             "Finance", "General Business", "Research", "Accounting/Auditing", "Art/Creative",
                             "Quality Assurance",
                             "Data Analyst", "Business Analyst", "Writing/Editing", "Distribution", "Science",
                             "Training",
                             "Purchasing", "Legal"))

    function_Marketing, function_Customer_Service, function_Not_Specified = 0, 0, 0
    function_Sales, function_Health_Care_Provider, function_Management = 0, 0, 0
    function_Information_Technology, function_Other, function_Engineering, function_Administrative = 0, 0, 0, 0
    function_Business_Development, function_Product_Management, function_Financial_Analyst = 0, 0, 0
    function_Consulting, function_Human_Resources, function_Project_Management = 0, 0, 0
    function_Manufacturing, function_Public_Relations, function_Strategy_Planning = 0, 0, 0
    function_Advertising, function_Finance, function_General_Business = 0, 0, 0
    function_Research, function_Accounting_Auditing, function_Art_Creative = 0, 0, 0
    function_Quality_Assurance, function_Data_Analyst, function_Business_Analyst = 0, 0, 0
    function_Writing_Editing, function_Distribution, function_Science = 0, 0, 0
    function_Training, function_Purchasing, function_Legal, function_Design, function_Production = 0, 0, 0, 0, 0
    function_Education, function_Supply_Chain = 0, 0

    if function == "Marketing":
        function_Marketing = 1
    elif function == "Customer Service":
        function_Customer_Service = 1
    elif function == "Not_Specified":
        function_Not_Specified = 1
    elif function == "Sales":
        function_Sales = 1
    elif function == "Health Care Provider":
        function_Health_Care_Provider = 1
    elif function == "Management":
        function_Management = 1
    elif function == "Information Technology":
        function_Information_Technology = 1
    elif function == "Other":
        function_Other = 1
    elif function == "Engineering":
        function_Engineering = 1
    elif function == "Administrative":
        function_Administrative = 1
    elif function == "Business Development":
        function_Business_Development = 1
    elif function == "Product Management":
        function_Product_Management = 1
    elif function == "Financial Analyst":
        function_Financial_Analyst = 1
    elif function == "Consulting":
        function_Consulting = 1
    elif function == "Human Resources":
        function_Human_Resources = 1
    elif function == "Project Management":
        function_Project_Management = 1
    elif function == "Manufacturing":
        function_Manufacturing = 1
    elif function == "Public Relations":
        function_Public_Relations = 1
    elif function=="Strategy/Planning":
        function_Strategy_Planning=1
    elif function == "Advertising":
        function_Advertising = 1
    elif function == "Finance":
        function_Finance = 1
    elif function == "General Business":
        function_General_Business = 1
    elif function == "Research":
        function_Research = 1
    elif function == "Accounting/Auditing":
        function_Accounting_Auditing = 1
    elif function == "Art/Creative":
        function_Art_Creative = 1
    elif function == "Quality Assurance":
        function_Quality_Assurance = 1
    elif function == "Data Analyst":
        function_Data_Analyst = 1
    elif function == "Business Analyst":
        function_Business_Analyst = 1
    elif function == "Writing/Editing":
        function_Writing_Editing = 1
    elif function == "Distribution":
        function_Distribution = 1
    elif function == "Science":
        function_Science = 1
    elif function == "Training":
        function_Training = 1
    elif function == "Purchasing":
        function_Purchasing = 1
    elif function == "Legal":
        function_Legal = 1
    elif function=="Design":
        function_Design=1
    elif function == "Production":
        function_Production = 1
    elif function == "Education":
        function_Education = 1
    elif function=="Supply Chain":
        function_Supply_Chain=1








    inputs = [[telecommuting, has_company_logo, has_questions, employment_type_Contract, employment_type_Not_Specified,
               employment_type_Full_time, employment_type_Other, employment_type_Part_time, employment_type_Temporary,required_experience_Associate,
               required_experience_Director,required_experience_Entry_level,required_experience_Executive,required_experience_Internship,
               required_experience_Mid_Senior_level,required_experience_Not_Applicable, required_experience_Not_Specified,

               required_education_Associate_Degree,required_education_Bachelor_s_Degree,required_education_Certification,
               required_education_Doctorate,required_education_High_School_or_equivalent,required_education_Master_s_Degree,
               required_education_Not_Specified,required_education_Professional,required_education_Some_College_Coursework_Completed,
               required_education_Some_High_School_Coursework,required_education_Unspecified,required_education_Vocational,
               required_education_Vocational___Degree,required_education_Vocational___HS_Diploma,

               industry_Accounting,industry_Airlines_Aviation,industry_Alternative_Dispute_Resolution,industry_Animation,
               industry_Apparel___Fashion,industry_Architecture___Planning,industry_Automotive,industry_Aviation___Aerospace,
               industry_Banking,industry_Biotechnology,industry_Broadcast_Media,industry_Building_Materials,industry_Business_Supplies_and_Equipment,
               industry_Capital_Markets,industry_Chemicals,industry_Civic___Social_Organization,industry_Civil_Engineering,
               industry_Commercial_Real_Estate,industry_Computer___Network_Security,industry_Computer_Games,industry_Computer_Hardware,
               industry_Computer_Networking,industry_Computer_Software,industry_Construction,industry_Consumer_Electronics,
               industry_Consumer_Goods,industry_Consumer_Services,industry_Cosmetics,industry_Defense___Space,industry_Design,
               industry_E_Learning,industry_Education_Management,industry_Electrical_Electronic_Manufacturing,industry_Entertainment,
               industry_Environmental_Services,industry_Events_Services,industry_Executive_Office,industry_Facilities_Services,
               industry_Farming,industry_Financial_Services,industry_Fishery,industry_Food___Beverages,industry_Food_Production,
               industry_Fund_Raising,industry_Furniture,industry_Gambling___Casinos,industry_Government_Administration,industry_Government_Relations,
               industry_Graphic_Design,industry_Health__Wellness_and_Fitness,industry_Higher_Education,industry_Hospital___Health_Care,industry_Hospitality,
               industry_Human_Resources,industry_Import_and_Export,industry_Individual___Family_Services,industry_Industrial_Automation,
               industry_Information_Services,industry_Information_Technology_and_Services,industry_Insurance,industry_International_Trade_and_Development,
               industry_Internet,industry_Investment_Banking,industry_Investment_Management,industry_Law_Enforcement,industry_Law_Practice,
               industry_Legal_Services,industry_Leisure_Travel___Tourism,industry_Libraries,industry_Logistics_and_Supply_Chain,
               industry_Luxury_Goods___Jewelry,industry_Machinery,industry_Management_Consulting,industry_Maritime,industry_Market_Research,
               industry_Marketing_and_Advertising,industry_Mechanical_or_Industrial_Engineering,industry_Media_Production,industry_Medical_Devices,
               industry_Medical_Practice,industry_Mental_Health_Care,industry_Military,industry_Mining___Metals,industry_Motion_Pictures_and_Film,
               industry_Museums_and_Institutions,industry_Music,industry_Nanotechnology,industry_Nonprofit_Organization_Management,
               industry_Not_Specified,industry_Oil___Energy,industry_Online_Media,industry_Outsourcing_Offshoring,industry_Package_Freight_Delivery,
               industry_Packaging_and_Containers,industry_Performing_Arts,industry_Pharmaceuticals,industry_Philanthropy,industry_Photography,
               industry_Plastics,industry_Primary_Secondary_Education,industry_Printing,industry_Professional_Training___Coaching,
               industry_Program_Development,industry_Public_Policy,industry_Public_Relations_and_Communications,industry_Public_Safety,
               industry_Publishing,industry_Ranching,industry_Real_Estate,industry_Religious_Institutions,industry_Renewables___Environment,
               industry_Research,industry_Restaurants,industry_Retail,industry_Security_and_Investigations,industry_Semiconductors,
               industry_Shipbuilding,industry_Sporting_Goods,industry_Sports,industry_Staffing_and_Recruiting,industry_Telecommunications,
               industry_Textiles,industry_Translation_and_Localization,industry_Transportation_Trucking_Railroad,industry_Utilities,
               industry_Venture_Capital___Private_Equity,industry_Veterinary,industry_Warehousing,industry_Wholesale,industry_Wine_and_Spirits,
               industry_Wireless,industry_Writing_and_Editing,

               function_Accounting_Auditing,function_Administrative,function_Advertising,function_Art_Creative,
               function_Business_Analyst,function_Business_Development,function_Consulting,function_Customer_Service,
               function_Data_Analyst,function_Design,function_Distribution,function_Education,function_Engineering,
               function_Finance,function_Financial_Analyst,function_General_Business,function_Health_Care_Provider,
               function_Human_Resources,function_Information_Technology,function_Legal,function_Management,function_Manufacturing,
               function_Marketing,function_Not_Specified,function_Other,function_Product_Management,function_Production,
               function_Project_Management,function_Public_Relations,function_Purchasing,function_Quality_Assurance,
               function_Research,function_Sales,function_Science,function_Strategy_Planning,function_Supply_Chain,function_Training,
               function_Writing_Editing]]

    result = model.predict(inputs)
    if st.button('Get Your Prediction'):

        if result == 0:
            st.success('The given job posting is Real')
        else:
            st.error('The given job posting is Fake')