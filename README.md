# 🧠 Unsupervised Learning Clustering Web App

A Streamlit-based web application that enables users to perform clustering on village-related datasets using unsupervised learning algorithms like **KMeans**, **DBSCAN**, and **Hierarchical Clustering**. The app visualizes clustering results on two selected features and evaluates performance using the **Silhouette Score**.

---

## 📁 Application file Structure

```
UNSUPERVISED_ANALYSIS/
│
├── streamlit_app.py                      # Main Flask application
├── final_colored_records.csv   # Dataset for clustering
├── templates/
│   ├── index.html              # Frontend form for feature/algorithm selection
│   └── village.jpg             # Optional image used in the web UI
```

---

## 🚀 Features

- Interactive web UI to select X and Y features from the dataset.
- Choice between **KMeans**, **DBSCAN**, and **Agglomerative Clustering**.
- Displays silhouette score to evaluate clustering performance.
- Visual output showing colored clusters on a 2D scatter plot.
- Intuitive error handling for duplicate feature selections.

---

## ▶️ How to Run the App

1. Make sure the file `final_colored_records.csv` is present in the root directory.
2. Run the streamlit application:

```bash
streamlit run streamlit_app.py
```

3. Open your browser and visit: https://kerala-village-clustering-visualization.streamlit.app/
4. Choose two features and a clustering algorithm, then submit the form to see the clustering plot and silhouette score.

---

## 🧠 Algorithms Supported

| Algorithm      | Parameters |
|----------------|------------|
| KMeans         | Number of clusters (K), init method |
| DBSCAN         | Epsilon (eps) |
| Hierarchical   | Linkage method |

---

## 📈 Example Output

Once submitted, the app will generate a scatter plot with clusters colored by algorithm output and display a silhouette score like:

```
Plot of Feature X vs Feature Y with KMeans Clustering (Silhouette Score: 0.61)
```

---

## 🔧 Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Scikit-learn**

---

## 🧠 Skills Demonstrated

- Web development with Flask
- Unsupervised learning (KMeans, DBSCAN, Hierarchical Clustering)
- Data visualization with Matplotlib
- Evaluation metrics (Silhouette Score)
- User input handling and dynamic plot generation

---
**Author**: Deepesh Yadav

## 🙌 Acknowledgments

- Developed by Deepesh Yadav
- Dataset: `final_colored_records.csv` (village data)

---
