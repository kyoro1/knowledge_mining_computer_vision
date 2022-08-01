import streamlit as st
import configparser
from common.generate_tag_db import *

## Setting
config_ini = configparser.ConfigParser()
config_ini.read('./common/config.ini', encoding='utf-8')

### Azure Subscription
subscription_key = config_ini['Azure']['subscription_key']

### Azure Computer Vision
cv_endpoint = config_ini['Azure']['cv_endpoint']
language = config_ini['Azure']['language']
#features = ['objects', 'tags']
features = ['tags']
SSL_check = False

### tag db, upload directory
tag_db_file = 'df_tag_db.pkl'
tag_db_columns = ['image_name', 'tag', 'confidence']
upload_dir = './upload_images'

## Read class
gt = generate_tag_db(subscription_key=subscription_key
                    ,cv_endpoint=cv_endpoint
                    ,language=language
                    ,features=features
                    ,tag_db_file=tag_db_file
                    ,tag_db_columns=tag_db_columns
                    ,upload_dir=upload_dir
                    ,SSL_check=SSL_check)

with st.sidebar:
    word = st.text_input('Search words', 'type your words')

    topN = st.number_input(label='Insert a number for topN'
                            ,min_value=3
                            ,max_value=20
                            ,step = 1)
    search_result_N = st.number_input(label='Input number of search results'
                            ,min_value=3
                            ,max_value=10
                            ,step=1)
    gt.topN = int(topN)

    uploaded_file = st.file_uploader("Choose a file to store your image", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        ## File exist?
        saved_image_files = os.listdir(gt.upload_dir)
        if uploaded_file.name in saved_image_files:
            st.warning('File already exists!')
        else:
            image_path = os.path.join(gt.upload_dir, uploaded_file.name)
            ## Save image
            with open(image_path, 'wb') as f:
                f.write(uploaded_file.read())

            df_tag_db = gt.analyze_insert_tag(uploaded_file.name)
            st.info(f'Saved {uploaded_file.name}, and analyzed results are ..')
            st.dataframe(df_tag_db)

### Search results
df_search_result = gt.extract_records_from_db_with_word(word)
#st.dataframe(df_search_result)

### Count search records
unique_image_num = df_search_result[gt.tag_db_columns[0]].nunique()

### Define how many images are shown
continuation_num = min(5, unique_image_num, search_result_N)

if len(df_search_result) <= 0:
    st.error('No image found')
else:
    image_name = gt.tag_db_columns[0]
    images = list(df_search_result[image_name])
    col1, col2= st.columns(2)
    ## Present headers for images & tags
    with col1:
        st.write('images')
    with col2:
        st.write('tags')
    ## Present analyzed results
    for i in range(continuation_num):
        col1, col2= st.columns(2)
        ## Show image in the left
        with col1:
            st.image(os.path.join(gt.upload_dir, images[i]))
        ## Show tags in the right
        with col2:
            df_search = gt.load_tag_db()
            df_tag_confidence = df_search[df_search.image_name == images[i]][gt.tag_db_columns[1:]].sort_values(gt.tag_db_columns[2], ascending=False)
            df_tag_confidence = df_tag_confidence[:gt.topN]
            st.dataframe(df_tag_confidence)
