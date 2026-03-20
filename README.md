🤖 Smart Support AI: Sentiment & Opinion Mining Agent
An end-to-end intelligence tool that uses Azure AI Services to analyze customer support tickets. This application doesn't just detect mood; it performs deep Opinion Mining to identify specific product issues and customer feedback in real-time.

🚀 Key Features
Granular Opinion Mining: Automatically extracts specific "Aspects" (e.g., Shipping, Quality, Price) and the customer's sentiment toward them.

Automated Escalation: Triggers a high-priority "Manager Alert" visual for negative sentiment.

Interactive Dashboard: Built with Streamlit and Pandas for a professional, searchable data experience.

Dated Reporting: Generates downloadable CSV reports with automated timestamps for historical record-keeping.

Secure Architecture: Implements industry-standard environment variable management to protect sensitive credentials.

🛠️ Tech Stack
Cloud: Microsoft Azure (AI Language Service)

Frontend: Streamlit

Data Handling: Pandas

Language: Python 3.x

Security: Python-Dotenv

⚙️ Setup & Installation
Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the root directory (refer to .env.example) and add your Azure credentials:

Plaintext
AZURE_LANGUAGE_KEY=your_actual_key_here
AZURE_LANGUAGE_ENDPOINT=your_endpoint_url_here
Run the Application:

Bash
streamlit run app.py
📊 Business Value
This tool reduces the manual labor required to categorize feedback. By identifying specific pain points (like "slow delivery" or "expensive pricing") within a larger message, businesses can route issues to the correct departments instantly, improving customer satisfaction and response times.
