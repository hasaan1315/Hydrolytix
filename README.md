<h1>Hydrolytix – AI Flood Risk Visualization Dashboard</h1>

<h2>Description</h2>
The Hydrolytix Flood Risk Dashboard is an AI-powered web-based tool for visualizing flood risk intelligence in Pakistan. It provides real-time data insights through interactive charts, maps, and filters. Users can analyze rainfall patterns, flood risk levels, affected populations, and relief camp distributions in an easy-to-use interface.

<h2>Languages and Technologies Used</h2>
- <b>Python</b> (Core programming) <br/>
- <b>Dash & Dash-Bootstrap-Components</b> (Web framework & UI) <br/>
- <b>Pandas</b> (Data manipulation) <br/>
- <b>Plotly</b> (Charts & visualizations) <br/>
- <b>GeoPandas / Folium</b> (Geospatial mapping)  

<h2>Environments Used</h2>
- <b>VS Code </b> (Development) <br/>
- <b>Web Browsers (Chrome, Firefox, Edge)</b> <br/> 

<h2>Dashboard Walk-through:</h2>

<p align="center">
  <b>Rainfall & Risk Chart</b> <br/>
  <img src="https://i.postimg.cc/zBTtQKrV/image.png" style="max-height: 500px; width: auto;" alt="Rainfall Risk Chart"/>
  <br /><br />

<p align="center">
  <b>Flood Risk Distribution (Pie Chart)</b> <br/>
  <img src="https://i.postimg.cc/43xHqgRt/image.png" style="max-height: 500px; width: auto;" alt="Flood Risk Pie Chart"/>
  <br /><br />

<p align="center">
  <b>Interactive Map with City Markers</b> <br/>
  <img src="https://i.postimg.cc/8PySwQ4x/image.png" style="max-height: 500px; width: auto;" alt="Flood Risk Map"/>
  <br /><br />

<p align="center">
  <b>Summary Cards</b> <br/>
  <img src="https://i.postimg.cc/yY2f7L8k/image.png" style="max-height: 500px; width: auto;" alt="Summary Cards"/>
</p>

<h2>Key Features</h2>

- 📅 <b>Weekly Data Filtering:</b> Filter data by selected week  
- 🏙️ <b>City-Specific Analysis:</b> View flood risk per city  
- 📊 <b>Rainfall & Risk Bar Charts:</b> Color-coded by risk level  
- 🥧 <b>Flood Risk Pie Chart:</b> Distribution of risk levels across cities  
- 🗺️ <b>Interactive Map:</b> Location markers sized by rainfall and colored by risk  
- 📌 <b>Summary Cards:</b> Quick stats on affected people and relief camps  

---

<h2>Expected Outcomes</h2>

- ✔️ Improved flood preparedness and risk awareness  
- ✔️ Enhanced decision-making for disaster management authorities  
- ✔️ Real-time data insights for policy and planning  
- ✔️ Better resource allocation during emergencies  
- ✔️ Scalable solution for integration with IoT sensors and satellite data  

---

<h2>Technical Manual</h2>

- <b>Prerequisites:</b> Python 3.7+, pip, Chrome/Firefox/Edge browser  
- <b>Installation:</b>  
  <pre>
  pip install dash dash-bootstrap-components pandas plotly
  </pre>  
- <b>Run the App:</b>  
  <pre>
  python app.py
  </pre>  
- <b>Files Overview:</b>  
  - app.py → Main Dash app (layout, callbacks, processing)  
  - assets/style.css → UI styles  
  - flood_data_with_coordinates.csv → Dataset (City, Week, Rainfall, Risk Level, Affected People, Relief Camps, Latitude, Longitude)  
  - assets/Hydrolytix-Logo.png → Logo  

---

<h2>Conclusion</h2>
Hydrolytix is a data-driven AI solution for flood risk monitoring and visualization in Pakistan. By integrating rainfall data, geospatial mapping, and predictive analytics, it empowers communities and authorities with actionable insights for disaster preparedness and response.
