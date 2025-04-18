# Absence Tracker App

This is a simple Flask-based web application that allows users to submit absence requests via a styled HTML form. The project was built as part of my portfolio to demonstrate modern web deployment practices using **Azure App Service** and **GitHub integration**.

## 🚀 Technologies Used

- **Python & Flask** – Lightweight backend built with Python and Flask for routing and handling form data.
- **HTML & CSS** – Frontend templates using `index.html` and `submit.html`, located in the `templates` folder.
- **GitHub** – All project code is stored in a public GitHub repository, used for version control and deployment.
- **Azure App Service** – The live application is hosted on Microsoft Azure using App Service and deployed automatically via GitHub Actions.

## 🛠️ How It Was Built

1. **Local Development**
   - Created a Flask app with form routing and rendering using `render_template()`.
   - Styled the pages with embedded CSS for a polished and clean UI.

2. **Version Control with GitHub**
   - Created a public GitHub repository to host the project.
   - Added all files (`app.py`, HTML templates, requirements.txt) and pushed to `main` branch.

3. **Deployment with Azure**
   - Created a new Azure Web App via the Azure Portal.
   - Connected the Azure App Service to my GitHub repository.
   - Enabled GitHub Actions for continuous deployment on new commits to `main`.

4. **Live Deployment**
   - Azure automatically pulls and builds the app when changes are committed.
   - Accessible via the Azure-provided domain:  
     (https://absence-tracker-raymond-avhrawc8ddhcdehc.centralus-01.azurewebsites.net/)

## 💡 Lessons & Takeaways

- Learned how to connect GitHub with Azure for automated deployments.
- Understood the structure of Flask apps and how templates are rendered.
- Gained experience using cloud infrastructure to host web applications publicly.

## 📁 Project Structure

