import pandas as pd
import streamlit as st
from src.cloud_io import MongoIO
from src.constants import SESSION_PRODUCT_KEY
from src.scrapper.scrape import ScrapeReview

st.set_page_config(
        "Myntra-Review-Scrapper"
                   )

st.title("Myntra Review Scrapper")
st.session_state["data"] = False


def form_input():
    
    product = st.text_input("search product")
    st.session_state[SESSION_PRODUCT_KEY] = product

    no_of_product = st.number_input("No of product to search",step=1,min_value=1)

    if st.button("Scrape Reviews") :
        scrapper = ScrapeReview(
            product_name = product,
            no_of_product = int(no_of_product)
        )
        scrapped_data = scrapper.get_review_data()
        if scrapped_data is not None:
            st.session_state["data"] = True
            mongoio = MongoIO()
            mongoio.store_reviews(product_name=product,
                                reviews=scrapped_data)
            print("Stored Data into mongodb")

        st.dataframe(scrapped_data)

if __name__ == "__main__":
    data = form_input()

