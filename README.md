# 🛒 E-Commerce Sales & Customer Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/SQL-SQLite-orange?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas" />
  <img src="https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge" />
</p>

<p align="center">
  <b>Turn e-commerce transactions into meaningful business insights 📊</b>
</p>

---

## 🚀 Live Dashboard

<p align="center">

### 🌐 [**TRY THE LIVE STREAMLIT DASHBOARD →**](https://ecommerce-sales-analysis-sql-fvzszzdahsj6vdc3yzoqzh.streamlit.app/)

</p>

Explore sales performance, customer behavior, category revenue, regional trends, and monthly growth through an interactive dashboard.

---

## 📌 About The Project

**E-Commerce Sales & Customer Analysis** is an end-to-end data analytics project built using **SQL, Python, SQLite, Pandas, and Streamlit**.

The project analyzes **6,692 e-commerce orders from 400 customers** to uncover patterns in:

- 💰 Revenue
- 🛍️ Product categories
- 👥 Customer behavior
- 🌎 Regional performance
- 📅 Monthly sales
- 📈 Revenue growth
- 🏆 High-value customers

The analysis combines **SQL-based business queries** with an interactive **Streamlit dashboard** to make the insights easy to explore.

---

# 🎯 Business Questions

The project focuses on answering practical business questions:

| Question | Analysis |
|---|---|
| 💰 What generates the most revenue? | Category revenue analysis |
| 🛍️ Which category performs best? | Category ranking |
| 🌎 Which region performs best? | Regional revenue analysis |
| 👥 Who are the highest-value customers? | Customer ranking |
| 📅 When are sales highest? | Monthly revenue trends |
| 📈 Is revenue growing? | MoM growth analysis |
| 🏆 Who are the top customers? | Revenue + order ranking |

---

# 📊 Dataset

> ⚠️ **Important:** This is a **synthetically generated dataset** created specifically for this project.

The dataset was generated using `generate_data.py` with realistic patterns such as:

- Seasonal demand
- Festive-season sales spikes
- Category-specific price ranges
- Customer distributions
- Regional distributions

The dataset is **not scraped from or sourced from any real company**.

### 👥 Customers

**400 customers**

| Column | Description |
|---|---|
| `customer_id` | Unique customer identifier |
| `region` | Customer region |
| `signup_date` | Customer registration date |

### 🛍️ Orders

**6,692 orders**

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `customer_id` | Customer reference |
| `order_date` | Date of purchase |
| `category` | Product category |
| `quantity` | Number of items |
| `unit_price` | Price per item |
| `revenue` | Total order revenue |

📅 **Data Period:** September 2025 – August 2026

---

# 💡 Key Business Insights

## 🥇 Top Revenue Category

### 🛍️ Electronics → **66.35%**

Electronics generated approximately **66.35% of total revenue**, making it the strongest-performing category.

---

## 🌎 Regional Performance

### 🥇 North Region

The **North region** generated the highest total revenue:

**₹16.47M**

### 💰 Highest Revenue per Active Customer

The **Central region** achieved the highest revenue per active customer:

**₹180,314.77**

---

## 📅 Peak Sales Month

### 🎉 December 2025

December generated the highest monthly revenue:

**₹10.33M**

This aligns with the festive-season demand pattern incorporated into the synthetic dataset.

---

## 📈 Month-over-Month Growth

The dataset recorded approximately:

### **3.25% Average MoM Growth**

This was calculated using SQL window functions and monthly revenue analysis.

---

## 🏆 Top Customer

The highest-value customer:

**CUST0298**

generated approximately:

### **₹450,540**

across:

### **29 orders**

---

# 🧠 SQL Analysis

This project demonstrates practical SQL skills used in real-world analytics.

### 🔗 Joins

Used `JOIN` operations to combine customer and order information.

### 📊 Aggregation

Used:

```sql
GROUP BY
SUM()
AVG()
COUNT()
```

for revenue, customer, order, and category analysis.

### 🏆 Ranking

Used:

```sql
RANK()
```

to identify high-value customers and rank business performance.

### 📈 Trend Analysis

Used:

```sql
LAG()
```

to calculate month-over-month revenue changes.

### Other SQL Concepts

- `SELECT`
- `WHERE`
- `ORDER BY`
- `GROUP BY`
- `JOIN`
- Aggregate functions
- Window functions
- Date-based analysis
- Customer-level aggregation
- Category-level aggregation
- Regional analysis

---

# 📊 Interactive Streamlit Dashboard

The project is deployed as an interactive **Streamlit dashboard**.

### 🎛️ Interactive Filters

Users can explore the data using:

- 🌎 Region
- 🛍️ Category
- 📅 Date Range

### 📌 Dashboard Metrics

The dashboard provides insights into:

- 💰 Total Revenue
- 🛒 Total Orders
- 👥 Customers
- 📦 Category Performance
- 🌎 Regional Performance
- 📅 Monthly Revenue
- 📈 Growth Trends
- 🏆 Top Customers

---

# 🔄 Project Workflow

```text
                    🛒 E-COMMERCE DATA
                           │
                           ▼
                  📄 Generate Dataset
                           │
                           ▼
                    🗄️ SQLite Database
                           │
                           ▼
                    🔍 SQL Queries
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          💰 Revenue    👥 Customer   🛍️ Category
           Analysis      Analysis      Analysis
              │            │            │
              └────────────┼────────────┘
                           ▼
                    🐍 Python + Pandas
                           │
                           ▼
                   📊 Data Visualization
                           │
                           ▼
                  🎨 Streamlit Dashboard
                           │
                           ▼
                     🚀 LIVE ANALYSIS
```

---

# 🛠️ Tech Stack

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />

<img src="https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />

<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />

<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />

<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />

<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" />

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />

<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />

</p>

---

# 📂 Project Structure

```text
Ecommerce-Sales-Analysis-SQL/
│
├── 📄 app.py
├── 📄 generate_data.py
├── 📄 load_to_sqlite.py
├── 📄 queries.sql
├── 📄 analysis.py
├── 📄 requirements.txt
│
├── 📊 customers.csv
├── 🛒 orders.csv
├── 🗄️ ecommerce.db
│
├── 📈 monthly_revenue_trend.png
└── 📊 category_revenue_share.png
```

---

# 🚀 Run Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Salma1612/Ecommerce-Sales-Analysis-SQL.git
```

```bash
cd Ecommerce-Sales-Analysis-SQL
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Generate the Dataset

```bash
python generate_data.py
```

This creates:

```text
customers.csv
orders.csv
```

---

## 4️⃣ Load Data into SQLite

```bash
python load_to_sqlite.py
```

This creates:

```text
ecommerce.db
```

---

## 5️⃣ Run SQL Analysis

```bash
python analysis.py
```

This executes the SQL queries and generates analysis results and charts.

---

## 6️⃣ Launch Streamlit

```bash
streamlit run app.py
```

The dashboard will open in your browser. 🎉

---

# 🌐 Try It Online

<p align="center">

🚀 **No installation required!**

### 👉 [OPEN THE LIVE DASHBOARD](https://ecommerce-sales-analysis-sql-fvzszzdahsj6vdc3yzoqzh.streamlit.app/)

</p>

---

# 📈 Skills Demonstrated

This project demonstrates practical experience with:

### 🐍 Python
- Data processing
- Pandas
- Data visualization
- Streamlit development

### 🗄️ SQL
- Joins
- Aggregations
- Window functions
- Ranking
- Time-series analysis

### 📊 Data Analytics
- Exploratory Data Analysis
- KPI analysis
- Customer analytics
- Revenue analysis
- Trend analysis
- Business insights

### 💻 Deployment
- Streamlit
- Git
- GitHub

---

# 💼 Business Value

The techniques demonstrated in this project can help businesses:

- Identify high-performing products
- Understand customer purchasing behavior
- Find valuable customer segments
- Compare regional performance
- Monitor revenue growth
- Identify seasonal demand patterns
- Support data-driven decision making

---

# 🔮 Future Improvements

Potential extensions include:

- 🤖 Customer segmentation using clustering
- 📈 Sales forecasting
- 🎯 Customer lifetime value prediction
- 🛍️ Product recommendation system
- 📊 Advanced KPI dashboard
- 🔎 RFM customer segmentation
- ☁️ Cloud database integration
- 📱 Mobile-friendly dashboard

---

# 👩‍💻 Author

## **Shaik Salma**

**B.Tech CSE (AI & ML)**

Interested in:

`Data Science` • `Machine Learning` • `Artificial Intelligence` • `Software Development`

<p align="center">

<a href="https://github.com/Salma1612">
<img src="https://img.shields.io/badge/GitHub-Salma1612-black?style=for-the-badge&logo=github" />
</a>

<a href="https://www.linkedin.com/in/sksalma1612">
<img src="https://img.shields.io/badge/LinkedIn-Shaik%20Salma-blue?style=for-the-badge&logo=linkedin" />
</a>

</p>

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
🚀 Try the live dashboard  
💬 Share your feedback

---

<p align="center">

### 🛒 Turning Data Into Decisions 📊

**Built with Python • SQL • Analytics • Streamlit**

</p>
