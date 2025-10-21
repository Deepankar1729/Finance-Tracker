# 💼 **Finance Tracker — Full Stack Web Development Project**

![Django](https://img.shields.io/badge/Django-5.2.7-green?logo=django)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-4.2.0-38B2AC?logo=tailwind-css)
![Python](https://img.shields.io/badge/Python-3.13.x-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?logo=postgresql)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)

---

## 🎯 **Project Objective**

The **Finance Tracker** is a **Full Stack Web Development Project** built to help users **track, analyze, and improve** their financial habits.  
It provides an intuitive dashboard where users can **track their income, expenses, savings and financial goals**, while also generating **automated reports (CSV)** and **visual analytics (PDF bar charts)**.  
The main objective of this project is to **enhance financial awareness** by giving users actionable insights into their personal finances.

---

## 🚀 **Live Demo**

👉 **[View Live on Render](https://finance-tracker-gsuc.onrender.com/)**  


⚠️ **Note:** Since this project is hosted on Render's free tier, the first load may take some time to start. Please be patient while the app boots up.

---

## 📋 **Features**

### 🧑‍💼 Authentication
- **Login** and **Register** pages for user authentication.  
- Secure session handling and logout functionality.

### 📊 Dashboard
- Displays:
  - **Total Income**
  - **Total Expenses**
  - **Net Savings**
  - **Goals** with progress percentage  
- Responsive and user-friendly interface styled with Tailwind CSS.

### 💸 My Transactions
- View a **list of all transactions** (income and expenses).  
- Includes:
  - **Generate Report** → Exports all transactions as a **CSV file** using Django Import-Export.  
  - **Generate Bar Chart** → Creates and **downloads a clustered bar chart as a PDF file** comparing income and expenses using Matplotlib and NumPy.

### 🎯 My Goals
- Displays user-defined financial goals.  
- Includes a **delete button** for goal removal.

### ➕ Add Transaction
- Form to record a new **income or expense** transaction.

### 🏁 Create Goal
- Form to create a new **financial goal** with target values.

### 🚪 Logout
- Secure logout functionality to end user sessions.

---

## 🛠️ **Tech Stack**

| Component | Technology Used |
|------------|----------------|
| **Backend** | Django |
| **Frontend** | HTML, Tailwind CSS, JavaScript |
| **Database** | PostgreSQL |
| **Charting** | Matplotlib, NumPy |
| **Data Export** | Django Import-Export |
| **Deployment** | Render |

---

## ⚠️ Important Note

The **Forgot Password** button is present on the Login form, but this feature is **not currently implemented**.  
I chose **not to enable it for privacy reasons**, as activating it would require adding my email credentials (email address and password) in the Django `settings.py` file.  

Enabling the Forgot Password functionality is straightforward and **can be done easily** once configured securely.

---

## 🌟 Future Improvements

The Finance Tracker is functional but there are several areas for enhancement:

- 📱 **Responsive Design:** Make the app fully responsive for mobile and tablet devices (currently not fully responsive).    
- ✉️ **Email Notifications:** Notify users when they reach goal milestones or provide transaction summaries.  
- 🌙 **Dark Mode:** Add a dark/light theme toggle for better accessibility and user preference.    
- 🔒 **Enhanced Security:** Implement two-factor authentication (2FA) for improved account security.  
- 📈 **Advanced Analytics:** Provide insights such as spending categories, top expenses, and saving suggestions.  
- 🔑 **Forgot Password Feature:** Implement password reset functionality securely.  

