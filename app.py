import streamlit as st
from recommender import recommend, movies

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")
st.header("🎥 Movie Recommendation System")
st.markdown("##### Discover your next favorite movie with smart recommendations 🍿")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie to get recommendations:", movie_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    st.subheader("Top 5 Recommendations:")

    # Display in columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx])
            st.caption(names[idx])

if __name__ == '__main__':
    # movie recommendation UI code yahan tak chalega

    # 👇 Footer
    st.markdown(
    """<div style='text-align: center; font-size: small;'>
    Made with ❤️ by <a href="https://github.com/Rohan048" target="_blank">Rohan Rai</a>
    </div>""",
    unsafe_allow_html=True
)

