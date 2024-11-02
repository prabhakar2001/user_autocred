import streamlit as st
from datetime import datetime
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
import random
import string

# Firebase configuration for pyrebase (for user authentication and real-time database)
firebaseConfig = {
    "apiKey": "AIzaSyDMBLeFCxnMcYBAhS3l_-Vu5n5jYAeb5Ew",
    "authDomain": "proj-58848.firebaseapp.com",
    "projectId": "proj-58848",
    "databaseURL": "https://proj-58848-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "proj-58848.firebasestorage.app",
    "messagingSenderId": "674440611624",
    "appId": "1:674440611624:web:006d23886fb29f7098321d"
}

# Initialize Firebase with pyrebase for Authentication and Realtime Database
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db_rtdb = firebase.database()

# Initialize Firestore Database with firebase_admin SDK if not already initialized
if not firebase_admin._apps:
    firebase_cred = credentials.Certificate({
        "type": "service_account",
        "project_id": "proj-58848",
        "private_key_id": "9118b569aabadcfd157f9b0a8b69b03fc3626317",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC2iSuXpwAXKGLl\nfuYZa/4uTMNSXwhVr7pe4ioocjCbmpejgQUZquV8Xic1QxaaOprFpdRuYoGZaOKi\nnFhcUVUhkoQTdAgc0mE3AyBQtMH5dmiQ6OShW5IVaiQIjSk+1iz2ujO2dedXFJkK\nf8o4nh4sN+tNjNehTmKPY8BpH9boyIxjUwUXZGpedX7mwAfzMkSY1hPoH+Wc4ZdC\nKtGTN6bTpkV0LHzoWdLvZUE58e6+SRQn82WX2yOuRsCm1fI144ytrHriaA4nAG1R\nNSVULhQiSvs0IFuBELShNOYDbtPHGTwACVmmnswoJBmkTD0kITpw3V0j6jOI7ymW\nOz4v1MONAgMBAAECggEABNxu6HYX+gXnNrsw6VQ0OJgIJMog5v54vtMhRUkS0B06\nh/reuTORMsUwU4PkXU1No6rW/YbEP2LvYJFvIJJBhQhDJsasLdXqcdq0jxtC0sZo\nLxSMr8Fh1aePqxluekM3S+2WHl6FP48hKwocYNkEVUm6vsRCVjdH4UKwtC8wlXiX\nEcdegKzWm3AP2CrJjjG02ftLNDomf/a7BANam3KTasemfOAMfZV6c8rMW2eNIqgd\nBklPQyBONI5DRkwvfH52cUiJe1d8CjsglOPYQh+Juquhz2HQ3oKtNGf/mynlR1zM\nLz86tyCtNxP9Jn6HRULQSN/R6QqGvPRNN8Tnh1nanwKBgQDZORpYsBX+AhitWAQE\naUUB3Svrk4nsfrh++cEOwvX/j5Gq7rFGI/+l27gPRyFFQcTC2hTsrO5BT1g1AU8b\nNR0W7xeCNR30oIGiw6hHg6qeP+DpWJ+DpOQzAaU4CV0rV0tPd1FcFNkJv7oaAGfN\n4X2PPtrcY/uIv3rSX0BG1rX1LwKBgQDXHuRdXbUdxfn5Se/gXiJDlecXIvEDYiCe\nqhOvtzD+6dzTeS8moKAqkq3VUeRAqv4UQZJ/8/ruekNOpfj9Ar+LxNzg/cNKA/DG\nLelIP/2Xy6fEHXnajhquutQalYFRpwwjeUV0MhCxF3YB6o0QDVaYtyo2HDP9sW/q\nQDBFGEpcAwKBgGLa8tuDny6Ow643jPR499emULOP3EfNT6cxgCN4pD0emDtDD1gN\nT+2qNXR2eXSsPqAyYS1ocbE1K75LjzWhkVB7lKZECBLo7LYm9rE9AWutRGzNUSK2\n6scvq4H5+PWdb3+FnHgcYL1oDIiCwLrYMKz8/NspgTI1ee69PGJAmmQvAoGBAJgF\nwsigcmAKCq+7KoPawkgU5WyaSsxjSj4WXzcsNLnQtzfTShj4JngvlB1OdAmnTUsv\nU8KMvuZNDMfFzwGuMYMqqhVt/9aMlljXFSbz4dimGXckhXqINh8I9N+ci/kSHifr\nicOlpdoghEqyYOHZKztdJb17jNpZzIc0uWf61IHVAoGAFHWRmvE/yK4n3g85sEwZ\nWnMfb9NgIA109c79JA2YJ9cMOSBboGYb7dtgkQ0JosU+OMq+8x4OvTEYRNHOVi2C\nEg0eJlgLrksT2A8tndADOo3+n3igDptqM30cGDpewNGOHCDS4aHMVWuUa1suqXzk\nWP3an8LS7xp4yP0AI8LU5JM=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-u5ghi@proj-58848.iam.gserviceaccount.com",
        "client_id": "117984377403170508973",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-u5ghi%40proj-58848.iam.gserviceaccount.com"
    })
    firebase_admin.initialize_app(firebase_cred)
db_firestore = firestore.client()

# Function to retrieve client data by email
def get_client_by_email(email):
    doc_ref = db_firestore.collection('clients').where("email", "==", email).limit(1).stream()
    for doc in doc_ref:
        return doc.to_dict()
    return None

# Function to retrieve client data by username
def get_client_by_username(username):
    doc_ref = db_firestore.collection('clients').document(username).get()
    if doc_ref.exists:
        return doc_ref.to_dict()
    return None

# Function to generate a random password
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for i in range(length))

# Function to update the password (without affecting login status)
def update_password(username, password):
    db_firestore.collection('clients').document(username).update({'password': password})

# Function to update login status (active/inactive)
def update_login_status(username, status):
    db_firestore.collection('clients').document(username).update({'login_status': status})

# Sign Up: Verify Email and Retrieve or Generate Credentials
def sign_up():
    st.title("Sign Up")
    email = st.text_input("Enter your registered email:")
    if st.button("Generate Login Credentials"):
        client_data = get_client_by_email(email)
        
        if client_data:
            username = client_data['username']
            password = client_data.get('password')
            
            # If no password exists, generate and store it without changing login status
            if not password:
                password = generate_random_password()
                update_password(username, password)
            
            # Display credentials to the user
            st.success("Login credentials retrieved successfully!")
            st.write(f"**Username**: {username}")
            st.write(f"**Password**: {password}")

            # Store credentials in session state for autofill and sidebar display
            st.session_state['generated_username'] = username
            st.session_state['generated_password'] = password
            st.session_state['credentials_generated'] = True
            st.session_state['signed_up'] = True
            show_login()
        else:
            st.error("This email is not registered. Please contact the admin.")

def show_login():
    st.title("User Login")
    username = st.text_input("Username", value=st.session_state.get('generated_username', ''))
    password = st.text_input("Password", type="password", value=st.session_state.get('generated_password', ''))

    if st.button("Login"):
        client_data = get_client_by_username(username)
        
        if client_data:
            # Check if the user is already logged in
            if client_data['login_status'] == 1:
                st.warning("You are already logged in on another device or session.")
                
                # Option to clear previous session
                if st.button("Clear Previous Session and Login Again"):
                    update_login_status(username, 0)  # Set login status to inactive
                    st.info("Previous session cleared. Please click 'Login' again to continue.")
                    st.experimental_rerun()  # Refresh the page to allow a new login
                return  # Stop further processing until login is retried
            
            # Verify password
            if client_data['password'] == password:
                expiry_date = datetime.strptime(client_data['expiry_date'], '%Y-%m-%d')
                if datetime.now() > expiry_date:
                    st.error(f"Your access expired on {expiry_date.strftime('%Y-%m-%d')}. Please contact admin.")
                else:
                    # Successful login and set login status to active
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = client_data['username']
                    st.session_state['permissions'] = client_data['permissions']
                    st.session_state['expiry_date'] = client_data['expiry_date']
                    update_login_status(username, 1)  # Set login status to active
                    st.success(f"Welcome, {username}!")
            else:
                st.error("Invalid password.")
        else:
            st.error("Username not found.")

# Main Dashboard after login
def main_dashboard():
    username = st.session_state.get('username', 'User')
    permissions = st.session_state.get('permissions', [])
    expiry_date = st.session_state.get('expiry_date', datetime.now().strftime("%Y-%m-%d"))

    st.write(f"Welcome, {username}!")
    st.write(f"Your access expires on: {expiry_date}")

    st.write("### Available Dashboards")
    for dashboard in ['dashboard1', 'dashboard2', 'dashboard3', 'dashboard4', 'dashboard5', 'dashboard6']:
        if dashboard in permissions:
            st.write(f"✔️ {dashboard}")
        else:
            st.write(f"❌ {dashboard} - No Access")

    # Logout button to clear session and reset login status
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        update_login_status(username, 0)  # Reset login status to inactive
        st.experimental_set_query_params()  # Refresh the page

# Handle Navigation
def handle_navigation():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        main_dashboard()
    else:
        choice = st.sidebar.radio("Choose an option", ["Sign Up", "Login"])

        if choice == "Sign Up":
            sign_up()
        else:
            show_login()

# Run the user dashboard
if __name__ == "__main__":
    handle_navigation()
