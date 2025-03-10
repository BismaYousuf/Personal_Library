# import streamlit as st
# import json
# import os

# # File to store library data
# LIBRARY_FILE = "library.json"

# # Load Library Function
# def load_library():
#     if os.path.exists(LIBRARY_FILE):
#         with open(LIBRARY_FILE, "r") as f:
#             return json.load(f)
#     return []

# # Save Library Function
# def save_library(library):
#     with open(LIBRARY_FILE, "w") as f:
#         json.dump(library, f, indent=4)

# # Load the library
# library = load_library()

# # Streamlit UI
# st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="wide")

# st.title("📚 Personal Library Manager")

# # Sidebar Menu
# menu = st.sidebar.radio("📌 Menu", ["📖 Add Book", "🔍 Search Books", "📚 View Library", "📊 Statistics"])

# # Add a Book
# if menu == "📖 Add Book":
#     st.header("📖 Add a New Book")

#     with st.form("add_book_form"):
#         title = st.text_input("📚 Book Title", placeholder="Enter the book title")
#         author = st.text_input("✍️ Author", placeholder="Enter the author's name")
#         year = st.number_input("📅 Publication Year", min_value=1000, max_value=2100, step=1)
#         genre = st.text_input("🎭 Genre", placeholder="Enter book genre")
#         read_status = st.radio("📖 Have you read this book?", ["Yes", "No"])

#         submitted = st.form_submit_button("➕ Add Book")

#         if submitted:
#             if title and author and genre:
#                 book = {
#                     "title": title.strip(),
#                     "author": author.strip(),
#                     "year": int(year),
#                     "genre": genre.strip(),
#                     "read": read_status == "Yes",
#                 }
#                 library.append(book)
#                 save_library(library)
#                 st.success("✅ Book added successfully!")
#             else:
#                 st.error("⚠️ Please fill in all fields!")

# # Search Books
# elif menu == "🔍 Search Books":
#     st.header("🔍 Search for a Book")

#     search_type = st.radio("Search by:", ["Title", "Author"])
#     search_query = st.text_input("🔎 Enter your search term", placeholder="Type here...")

#     if search_query:
#         results = [
#             book for book in library if search_query.lower() in book[search_type.lower()].lower()
#         ]

#         if results:
#             st.write(f"✅ Found {len(results)} matching books:")
#             st.table(results)
#         else:
#             st.warning("❌ No books found with that search term.")

# # View All Books
# elif menu == "📚 View Library":
#     st.header("📚 Your Library")

#     if library:
#         st.table(library)
#     else:
#         st.warning("⚠️ Your library is empty. Add books first!")

# # Display Statistics
# elif menu == "📊 Statistics":
#     st.header("📊 Library Statistics")

#     total_books = len(library)
#     read_books = sum(1 for book in library if book["read"])

#     if total_books > 0:
#         read_percentage = (read_books / total_books) * 100
#     else:
#         read_percentage = 0

#     st.metric("📚 Total Books", total_books)
#     st.metric("📖 Books Read", f"{read_books} ({read_percentage:.1f}%)")

# # Footer
# st.sidebar.write("---")
# st.sidebar.write("📌 **Developed with ❤️ Bisma Yousuf**")




import streamlit as st
import json
import os

# File to store library data
LIBRARY_FILE = "library.json"

# Load Library Function
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

# Save Library Function
def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

# Load the library
library = load_library()

# Streamlit UI Configuration
st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="wide")

# Custom Styling with Background
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4 !important;
        }
        .stApp {
            background: linear-gradient(to right, #e3f2fd, #bbdefb);
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 16px !important;
            border-radius: 8px !important;
        }
        .stTextInput>div>div>input {
            border-radius: 8px !important;
        }
        .stRadio>div>label {
            font-weight: bold !important;
        }
        .metric-container {
            display: flex;
            gap: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("📚 Personal Library Manager")
st.markdown("Manage your personal book collection effortlessly.")

# Sidebar Menu
menu = st.sidebar.radio("📌 Menu", ["📖 Add Book", "🔍 Search Books", "📚 View Library", "📊 Statistics"])

# Add a Book
if menu == "📖 Add Book":
    st.header("📖 Add a New Book")
    with st.form("add_book_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("📚 Book Title", placeholder="Enter book title")
            author = st.text_input("✍️ Author", placeholder="Enter author's name")
        with col2:
            year = st.number_input("📅 Publication Year", min_value=1000, max_value=2100, step=1)
            genre = st.text_input("🎭 Genre", placeholder="Enter book genre")
        
        read_status = st.radio("📖 Have you read this book?", ["Yes", "No"], horizontal=True)
        submitted = st.form_submit_button("➕ Add Book")
        
        if submitted:
            if title and author and genre:
                book = {
                    "title": title.strip(),
                    "author": author.strip(),
                    "year": int(year),
                    "genre": genre.strip(),
                    "read": read_status == "Yes",
                }
                library.append(book)
                save_library(library)
                st.success("✅ Book added successfully!")
            else:
                st.error("⚠️ Please fill in all fields!")

# Search Books
elif menu == "🔍 Search Books":
    st.header("🔍 Search for a Book")
    search_type = st.radio("Search by:", ["Title", "Author"], horizontal=True)
    search_query = st.text_input("🔎 Enter your search term", placeholder="Type here...")
    
    if search_query:
        results = [book for book in library if search_query.lower() in book[search_type.lower()].lower()]
        if results:
            st.success(f"✅ Found {len(results)} matching books:")
            st.dataframe(results, use_container_width=True)
        else:
            st.warning("❌ No books found with that search term.")

# View All Books
elif menu == "📚 View Library":
    st.header("📚 Your Library")
    if library:
        st.dataframe(library, use_container_width=True)
    else:
        st.warning("⚠️ Your library is empty. Add books first!")

# Display Statistics
elif menu == "📊 Statistics":
    st.header("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    
    st.markdown('<div class="metric-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📚 Total Books", total_books)
    with col2:
        st.metric("📖 Books Read", f"{read_books} ({read_percentage:.1f}%)")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.sidebar.markdown("""
---
📌 **Developed with ❤️ by Bisma Yousuf**
""")