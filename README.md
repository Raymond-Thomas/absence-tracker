# Absence Tracker App

[![Deploy to Azure](https://img.shields.io/badge/Deployed%20on-Azure-blue?logo=microsoftazure)](https://absence-tracker-raymond-avhrawc8ddhcdehc.centralus-01.azurewebsites.net/)
[![Build Status](https://dev.azure.com/rayjthomas2160/absence-tracker-pipeline/_apis/build/status%2FRaymond-Thomas.absence-tracker?branchName=main)](https://dev.azure.com/rayjthomas2160/absence-tracker-pipeline/_build/latest?definitionId=1&branchName=main)

This is a simple Flask-based web application that allows users to submit absence requests via a styled HTML form. The project was built as part of my portfolio to demonstrate modern web deployment practices using **Azure App Service**, **Azure DevOps**, and **GitHub integration**.

---

## 🚀 Technologies Used

- **Python & Flask** – Lightweight backend built with Python and Flask for routing and handling form data.
- **HTML & CSS** – Frontend templates using `index.html` and `submit.html`, located in the `templates` folder.
- **GitHub** – Source code is stored in a public GitHub repository and linked to Azure DevOps.
- **Azure App Service** – The live application is hosted on Microsoft Azure. The app is deployed using Azure DevOps pipelines triggered by GitHub commits.
- **Azure DevOps** – CI/CD pipeline automates building and deploying the application on every push to `main`.

---

## 🛠️ How It Was Built

1. **Local Development**
   - Created a Flask app with form routing and HTML rendering using `render_template()`.
   - Styled pages with embedded CSS for a polished and clean UI.

2. **Version Control with GitHub**
   - Created a public GitHub repository to host the project.
   - Managed code through version control and organized into branches.

3. **Deployment with Azure**
   - Set up an Azure Web App using the Azure Portal.
   - Connected the Azure App Service to my Azure DevOps pipeline using a secure service connection.
   - Configured an `azure-pipelines.yml` file to define build and deployment steps triggered by commits to the `main` branch.

4. **Live Deployment**
   - Azure DevOps automates the deployment pipeline from GitHub to Azure App Service.
   - The application is publicly accessible via:  
     [https://absence-tracker-raymond-avhrawc8ddhcdehc.centralus-01.azurewebsites.net](https://absence-tracker-raymond-avhrawc8ddhcdehc.centralus-01.azurewebsites.net)

---

## 📦 Deployment Details

This app is live and deployed on [Azure App Service](https://absence-tracker-raymond.azurewebsites.net).  
CI/CD is fully configured using [Azure DevOps Pipelines](https://dev.azure.com/rayjthomas2160/absence-tracker-pipeline/) and GitHub.

The pipeline runs automatically on every push to the `main` branch:
- Installs dependencies
- Prepares the environment
- Deploys to the Azure App Service

⚠️ *Pipeline execution is currently pending free-tier approval from Microsoft. Once approved, updates will deploy automatically.*

---

## 💡 Lessons & Takeaways

- Learned how to set up automated deployments using Azure DevOps and GitHub
- Gained experience configuring YAML pipelines and cloud deployment workflows
- Strengthened Flask development skills, frontend/backend integration, and cloud hosting

---

## 🔗 Links

- 🔗 [Live App](https://absence-tracker-raymond.azurewebsites.net/)
- 🔗 [GitHub Repo](https://github.com/Raymond-Thomas/absence-tracker)
- 🔗 [Azure DevOps Pipeline](https://dev.azure.com/rayjthomas2160/absence-tracker-pipeline/)



