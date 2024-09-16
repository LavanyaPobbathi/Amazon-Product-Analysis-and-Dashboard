import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import time
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image

# Set page config at the very beginning
st.set_page_config(
    page_title="Amazon Product Analysis Dashboard",
    page_icon="🛒",
    layout="wide",
)

# Custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
    }

    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }

    .css-1d391kg {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    </style>
    """, unsafe_allow_html=True)

# Function to load data efficiently
@st.cache_data
def load_data():
    # Measure loading time
    start_time = time.time()
    df = pd.read_parquet('merge_df.parquet')

    # Optimize data types
    categorical_columns = ['main_category', 'sub_category', 'name']
    for col in categorical_columns:
        df[col] = df[col].astype('category')

    # Calculate loading time and memory usage
    loading_time = time.time() - start_time
    memory_usage = df.memory_usage(deep=True).sum() / (1024**2)  # Convert to MB

    return df, loading_time, memory_usage

# Load data
merge_df, loading_time, memory_usage = load_data()

# Main title
st.title('Amazon Product Analysis Dashboard')
st.subheader('An In-Depth Analysis of 1.1 Million Amazon Products (2023)')

# Sidebar with custom menu
with st.sidebar:
    # If you have a logo image, uncomment the following lines and provide the path to your logo
    # logo = Image.open('logo.png')
    # st.image(logo, use_column_width=True)
    st.title("Navigation")
    page = option_menu(
        menu_title=None,
        options=["Overview", "Category Insights", "Price Analysis", "Rating Insights", "Advanced Visualizations", "Data Handling Techniques", "Key Insights from Dataset"],
        icons=["house", "bar-chart", "tags", "star", "graph-up", "cpu", "journal-text"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#f0f2f6"},
            "icon": {"color": "#1f77b4", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#1f77b4", "color": "white"},
        },
    )
    st.subheader('Data Sampling')
    sample_fraction = st.slider('Select Sample Fraction (%)', 1, 100, 10, step=1)
    sample_fraction = sample_fraction / 100.0  # Convert to decimal
    st.info('This dashboard presents an interactive analysis of Amazon product data, showcasing key insights from your EDA.')

# Apply data sampling based on user input
sample_df = merge_df.sample(frac=sample_fraction, random_state=42).reset_index(drop=True)
st.write(f"Displaying a sample of **{sample_fraction*100:.0f}%** of the data (**{len(sample_df):,}** records).")

# Display data loading and memory usage
with st.container():
    st.subheader('Performance Metrics')
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Data Loading Time (seconds)", f"{loading_time:.2f}")
    with col2:
        st.metric("Memory Usage (MB)", f"{memory_usage:.2f}")

# Handle different pages based on 'page' variable
if page == 'Overview':
    st.header('Dataset Overview')

    # Display key metrics
    with st.container():
        st.subheader('Key Metrics')
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Products", f"{len(merge_df):,}")
        with col2:
            st.metric("Categories", merge_df['main_category'].nunique())
        with col3:
            st.metric("Sub-Categories", merge_df['sub_category'].nunique())
        with col4:
            st.metric("Sample Size", f"{len(sample_df):,}")

    # Sample data
    with st.expander("See Sample Data"):
        st.dataframe(sample_df.head(1000))  # Display first 1000 rows

    # WordCloud of product names
    st.subheader('Most Common Words in Product Names')
    text = ' '.join(sample_df['name'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

elif page == 'Category Insights':
    st.header('Category Analysis')

    col1, col2 = st.columns(2)
    with col1:
        #st.subheader('Top 10 Main Categories')
        top_categories = sample_df['main_category'].value_counts().head(10)
        fig = px.bar(
            top_categories,
            labels={'value': 'Count', 'index': 'Category'},
            color=top_categories.values,
            color_continuous_scale='Tealgrn',
            title='Top 10 Main Categories',
        )
        fig.update_layout(showlegend=False, title_font_size=22)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        #st.subheader('Average Ratings by Main Category')
        avg_ratings = sample_df.groupby('main_category')['ratings'].mean().sort_values(ascending=False)
        fig = px.bar(
            avg_ratings,
            labels={'value': 'Average Rating', 'index': 'Category'},
            color=avg_ratings.values,
            color_continuous_scale='Teal',
            title='Average Ratings by Main Category',
        )
        fig.update_layout(showlegend=False, title_font_size=22)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader('Sub-category Distribution')
    selected_category = st.selectbox('Select a main category', sample_df['main_category'].unique())
    sub_cat_data = sample_df[sample_df['main_category'] == selected_category]['sub_category'].value_counts()
    fig = px.pie(
        sub_cat_data,
        values=sub_cat_data.values,
        names=sub_cat_data.index,
        title=f'Sub-categories in {selected_category}',
        color_discrete_sequence=px.colors.sequential.Tealgrn
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False, title_font_size=22)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Price Analysis':
    st.header('Price Analysis')

    col1, col2 = st.columns(2)
    with col1:
        #st.subheader('Price Distribution')
        fig = px.histogram(
            sample_df, x='actual_price', nbins=50,
            labels={'actual_price': 'Price', 'count': 'Frequency'},
            title='Price Distribution',
            color_discrete_sequence=['#1f77b4']
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        #st.subheader('Discount vs. Actual Price')
        fig = px.scatter(
            sample_df, x='actual_price', y='discount_price',
            color='main_category', hover_data=['name'],
            labels={'actual_price': 'Actual Price', 'discount_price': 'Discount Price'},
            title='Discount vs. Actual Price',
        )
        st.plotly_chart(fig, use_container_width=True)

    #st.subheader('Price Range by Category')
    fig = px.box(
        sample_df, x='main_category', y='actual_price',
        labels={'actual_price': 'Price', 'main_category': 'Category'},
        title='Price Range by Category',
        color='main_category',
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Rating Insights':
    st.header('Rating Analysis')

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Rating Distribution')
        fig = px.histogram(
            sample_df, x='ratings', nbins=20,
            labels={'ratings': 'Rating', 'count': 'Frequency'},
            color_discrete_sequence=['#ff7f0e']
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader('Ratings vs. Number of Ratings')
        fig = px.scatter(
            sample_df, x='ratings', y='no_of_ratings',
            color='main_category', hover_data=['name'],
            labels={'ratings': 'Rating', 'no_of_ratings': 'Number of Ratings'},
        )
        st.plotly_chart(fig, use_container_width=True)

    # Average Ratings Heatmap
    #st.subheader('Average Ratings Heatmap')
    pivot = sample_df.pivot_table(values='ratings', index='main_category',
                                  columns='sub_category', aggfunc='mean')

    fig = px.imshow(
        pivot,
        labels=dict(x="Sub-category", y="Main Category", color="Average Rating"),
        color_continuous_scale='RdBu_r',
        title='Average Ratings Heatmap',
        aspect='auto'
    )

    # Update layout to adjust margins and colorbar size
    fig.update_layout(
        title_font_size=22,
        margin=dict(t=50, l=200, r=50),
        width=1000,
        height=700,
        xaxis={'side': 'bottom'},
    )

    # Adjust colorbar size and position
    fig.update_coloraxes(
        colorbar=dict(
            thickness=20,
            lenmode='fraction',
            len=1.0,
            yanchor='middle',
            y=0.5,
        )
    )

    # Update axis labels and fonts
    fig.update_xaxes(
        tickangle=45,
        tickfont=dict(size=10),
        automargin=True
    )
    fig.update_yaxes(
        tickfont=dict(size=10),
        automargin=True
    )

    st.plotly_chart(fig, use_container_width=False)

elif page == 'Advanced Visualizations':
    st.header('Advanced Insights')

    #st.subheader('Correlation Heatmap')
    corr_matrix = sample_df[['ratings', 'no_of_ratings', 'discount_price', 'actual_price', 'discount_percentage']].corr()
    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        labels=dict(color="Correlation"),
        title='Correlation Heatmap',
        color_continuous_scale='Tealgrn'
    )
    fig.update_layout(title_font_size=22)
    st.plotly_chart(fig, use_container_width=True)

    #st.subheader('Price vs. Ratings by Category')
    fig = px.scatter(
        sample_df, x='actual_price', y='ratings',
        color='main_category', size='no_of_ratings', hover_data=['name'],
        labels={'actual_price': 'Price', 'ratings': 'Rating'},
        title='Price vs. Ratings by Category',
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Top Rated Products')
    top_products = sample_df.sort_values(['ratings', 'no_of_ratings'], ascending=False).head(10)
    st.dataframe(top_products[['name', 'main_category', 'ratings', 'no_of_ratings', 'actual_price']])

elif page == 'Data Handling Techniques':
    st.header('Data Handling Techniques')

    st.write("""
    - **Dataset Size:** Over 1.4 million records.
    - **Efficient Storage:** Data stored in Parquet format for faster read/write operations.
    - **Memory Optimization:** Data types optimized to reduce memory usage by converting categorical columns.
    - **Caching:** Implemented caching to speed up data loading and processing.
    - **User-Controlled Sampling:** Allows adjustment of the data sample size for analysis.
    - **Performance Metrics:** Displayed data loading time and memory usage for transparency.
    """)

    st.subheader('Challenges and Solutions')
    st.write("""
    **Challenges:**
    - Processing and visualizing over 1.4 million records efficiently.
    - Ensuring the dashboard remains responsive and user-friendly.

    **Solutions:**
    - **Data Optimization:** Used Parquet format and optimized data types.
    - **Caching Mechanisms:** Leveraged Streamlit's caching to prevent redundant computations.
    - **User-Controlled Sampling:** Enabled users to adjust the amount of data processed for visualizations.
    """)

elif page == 'Key Insights from Dataset':
    st.header('Key Insights from the Analysis')

    st.subheader('1. Category Distribution')
    st.write("""
    - The Accessories category dominates the dataset, followed by Men's Clothing and Women's Clothing.
    - Categories like Music and Pet Supplies have significantly fewer products.
    """)

    st.subheader('2. Price Distribution Across Categories')
    st.write("""
    - Most categories have a lower price range.
    - Categories like Accessories, Men's Clothing, and Men's Shoes have a broader range of prices with significant outliers.
    - Products in the TV, Audio & Cameras category tend to have higher prices compared to others.
    """)

    st.subheader('3. Discount Price vs Ratings')
    st.write("""
    - Products with higher discounts appear across a wide range of ratings.
    - There is a clustering of ratings around 4.
    - Even high-priced products with significant discounts can achieve high ratings.
    - Customer satisfaction isn't directly tied to product cost.
    """)

    st.subheader('4. Price Difference Impact on Ratings')
    st.write("""
    - No strong linear relationship between price difference and the number of ratings.
    - Products with a higher price difference (higher discounts) tend to have more reviews.
    - Heavily discounted products attract more customer attention and reviews.
    """)

    st.subheader('5. Category-specific Rating Insights')
    st.write("""
    - Categories like Grocery & Gourmet Foods and Pet Supplies tend to have higher average ratings.
    - Categories like Men's Shoes and Home, Kitchen, Pets receive slightly lower average ratings.
    """)

    st.subheader('6. Correlation Between Features')
    st.write("""
    - Strong positive correlation between discount_price and actual_price (0.81).
    - No significant correlation between ratings and pricing variables.
    - Price may not directly influence customer satisfaction.
    """)

    st.subheader('7. Subcategory Rating Analysis')
    st.write("""
    - Subcategories like Air Conditioners, Grocery & Gourmet Foods, and Music have higher ratings.
    - Subcategories like Footwear and TV & Audio Accessories have lower ratings.
    """)

    st.subheader('8. Product Name Analysis')
    st.write("""
    - Common words in product names: Fit, T-Shirt, Regular, Running, and Shoe.
    - Fitness-related products and apparel are prevalent in the dataset.
    """)

    st.subheader('9. Implications for Discount Strategy')
    st.write("""
    - Products with larger price differences attract more customer reviews.
    - Companies could apply targeted discounts to increase customer interaction and potentially boost sales.
    """)

    st.subheader('10. Predictive Modeling Potential')
    st.write("""
    - Price features have little correlation with product ratings.
    - Factors other than price (e.g., product quality, brand reputation) may drive customer satisfaction.
    - Machine learning models could provide insights into what truly impacts customer ratings.
    """)

    st.subheader('11. Areas for Improvement')
    st.write("""
    - Categories like Home, Kitchen, Pets and Men's Shoes have lower average ratings.
    - Companies should focus on quality improvement, customer feedback collection, and better targeting in these categories.
    """)

    st.subheader('12. Potential for Predictive Models')
    st.write("""
    - Models could predict high customer ratings or number of reviews based on product attributes.
    - Recommendation systems using collaborative filtering or content-based methods could be built.
    """)

# Footer
st.markdown("""
    <hr>
    <center>
        <p>Developed by Lavanya Pobbathi | <a href="https://www.linkedin.com/in/lavanya-pobbathi-9b2761223/">LinkedIn</a> | <a href="https://github.com/LavanyaPobbathi">GitHub</a></p>
    </center>
    """, unsafe_allow_html=True)
