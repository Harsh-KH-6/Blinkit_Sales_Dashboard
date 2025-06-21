# Blinkit Sales Dashboard

![Blinkit Logo](assets/blinkit_logo.webp)

A modern, interactive sales analytics dashboard built with Python, Dash, and Plotly, designed to provide actionable insights into Blinkit sales data. This dashboard enables users to filter, visualize, and download sales data with ease, making it ideal for business analysts, data scientists, and decision-makers.

---

## 🚀 Live Demo

**You can view the live deployed dashboard here:** [https://blinkit-sales-dashboard.onrender.com](https://blinkit-sales-dashboard.onrender.com)

---

## 🚀 Features

- **Interactive Filtering:**  
  Filter sales data by Item Type, Outlet Type, and Location Tier using dropdowns and radio buttons.
- **Key Performance Indicators (KPIs):**  
  Instantly view Total Revenue, Total Units Sold, Average MRP, and Average Discount.
- **Rich Visualizations:**  
  - Horizontal bar chart of revenue by item type  
  - Donut pie chart of revenue by outlet type  
  - Scatter plot of MRP vs. revenue, colored by fat content and sized by visibility  
  - Line chart of revenue trends by outlet establishment year and identifier
- **Data Download:**  
  Download the currently filtered dataset as a CSV file with a single click.
- **Responsive UI:**  
  Clean, modern, and mobile-friendly interface with branding.

---

## 📊 Data Overview

The dashboard uses the `Blinkit_Sales.xlsx` dataset, which includes (but is not limited to) the following columns:

- `Item_Type`: Category of the item sold
- `Outlet_Type`: Type of outlet (e.g., Supermarket, Grocery Store)
- `Outlet_Location_Type`: Location tier (e.g., Tier 1, Tier 2, Tier 3)
- `Item_Outlet_Sales`: Sales revenue for the item at the outlet
- `Item_MRP`: Maximum Retail Price of the item
- `Item_Fat_Content`: Fat content category of the item
- `Item_Visibility`: Visibility score of the item in the outlet
- `Outlet_Establishment_Year`: Year the outlet was established
- `Outlet_Identifier`: Unique identifier for each outlet

> **Note:** The dashboard automatically adds `Unit_Sales` (set to 1 for each row) and computes `Revenue` from `Item_Outlet_Sales`.

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Blinit_Dashboard
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas plotly dash openpyxl
   ```

3. **Place your data:**
   - Ensure `Blinkit_Sales.xlsx` is in the project root.

4. **Run the dashboard:**
   ```bash
   python blinkit_dashboard.py
   ```
   - The app will be available at `http://127.0.0.1:8050/` by default.

---

## 🧑‍💻 Skills Demonstrated

- **Prompt Engineering:**  
  Designed and implemented user-friendly prompts and controls for dynamic data filtering and visualization.
- **Data Visualization:**  
  Leveraged Plotly Express for advanced, interactive charts and KPIs.
- **Dash Web App Development:**  
  Built a responsive, multi-component dashboard using Dash and HTML/CSS.
- **Data Wrangling:**  
  Utilized Pandas for data cleaning, transformation, and aggregation.
- **UI/UX Design:**  
  Applied modern design principles for a clean, branded, and intuitive user experience.
- **Python Programming:**  
  Demonstrated modular, readable, and maintainable code structure.
- **Export Functionality:**  
  Enabled seamless download of filtered data for further analysis.
- **AI-Assisted Data Analysis:**  
  Utilized ChatGPT and Julius.ai to accelerate data exploration, code generation, and dashboard design decisions.

---

## 📄 License

MIT License.  
© 2025 Blinkit Insights • Made by Harsh 

---

## 🙏 Acknowledgements

- [Dash by Plotly](https://dash.plotly.com/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)

---

**Feel free to fork, use, and contribute!** 
