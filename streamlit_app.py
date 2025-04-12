import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Load the dataset
data = pd.read_csv('final_colored_records.csv')
feature_names = data.columns.tolist()

st.set_page_config(page_title="Clustering App", layout="wide")
st.title("🧠 Unsupervised Learning Clustering App")

# Sidebar inputs
st.sidebar.header("🔧 Configuration")
x_axis = st.sidebar.selectbox("Select X-axis Feature", feature_names)
y_axis = st.sidebar.selectbox("Select Y-axis Feature", [f for f in feature_names if f != x_axis])

algorithm = st.sidebar.selectbox("Choose Clustering Algorithm", ["KMeans", "DBSCAN", "Hierarchical"])

# Additional parameters based on algorithm
params = {}
if algorithm == "KMeans":
    params["k"] = st.sidebar.slider("Number of Clusters (K)", 2, 10, 3)
    params["init_method"] = st.sidebar.selectbox("Initialization Method", ["k-means++", "random"])
elif algorithm == "DBSCAN":
    params["eps"] = st.sidebar.slider("Epsilon (eps)", 0.1, 5.0, 0.5, step=0.1)
elif algorithm == "Hierarchical":
    params["linkage"] = st.sidebar.selectbox("Linkage Method", ["ward", "complete", "average", "single"])

# Button to run clustering
if st.sidebar.button("Run Clustering"):
    features = data[[x_axis, y_axis]]
    
    # Apply selected algorithm
    if algorithm == "KMeans":
        model = KMeans(n_clusters=params["k"], init=params["init_method"], random_state=42)
    elif algorithm == "DBSCAN":
        model = DBSCAN(eps=params["eps"], min_samples=5)
    elif algorithm == "Hierarchical":
        model = AgglomerativeClustering(n_clusters=2, linkage=params["linkage"])
    else:
        st.error("Invalid algorithm selected.")
        st.stop()

    # Fit and predict clusters
    clusters = model.fit_predict(features)

    # Evaluate
    try:
        score = silhouette_score(features, clusters)
    except:
        score = -1  # In case of only 1 cluster

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(features[x_axis], features[y_axis], c=clusters, cmap='viridis')
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f"{algorithm} Clustering ({x_axis} vs {y_axis})\nSilhouette Score: {score:.2f}")

    st.pyplot(fig)
else:
    st.info("👈 Configure options in the sidebar and click **Run Clustering**")
