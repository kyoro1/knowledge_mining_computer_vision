# Overview
This repository provides search experience with your images by [Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/). Using [streamlit](https://streamlit.io/) framework, we can easily build an app, and customize it with your preferences.

# Prerequisites

- [Python environment](https://www.python.org/)
- [Azure subscription](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/fundamental-concepts#azure-terminology)
    - [Computer vision](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=vision%2Cwindows#create-a-new-azure-cognitive-services-resource) resource
- Your image files with `jpg`, `jpeg` or `png` format[^1]

# How to build an app

## 1. Install necessary libraries

- Please execute the following in your terminal:
    ```sh
    pip install -r ./requirements.txt
    ```

## 2. Configure the environment

- By using `common/config.ini`, you can specify the setting. See [this page](/common/REAME.md) in detail.
    ```sh
    [Azure]
    subscription_key = 12345xxxyyy
    cv_endpoint = https://xxxx.cognitiveservices.azure.com/
    language = ja
    ```

## 3. Run streamlit app with your terminal:

- Run the app
    ```sh
    streamlit run ./st_app.py
    ```

- You will find the following message. Then, copy and pate the URL in your browser[^2]:

    ```
    You can now view your Streamlit app in your browser.
    Local URL: http://localhost:8501
    Network URL: http://xxx.xxx.xxx.xxx:8501
    ```

- Once you successfully run your app, you will see:
    ![top page](/docs/images/top_page.png)

# How to use the app

## 1. Register image

- In registering your image, select your image in your local folder
    ![browse image](/docs/images/browse_image.png)

- Once you select your image, you will find the analyzed result[^3]:
    ![analyzed image](/docs/images/analized_results.png)

## 2. Search image

- If you input your interest by word, your will find the search results:
    ![Search result](/docs/images/search_results.png)

## 3. Customize your preferences
If you want to more results, change the prarmeters:

- topN: `5` tags are shown in each picture
    ![topN](/docs/images/topN.png)

- Search result: `4` search results are shown
    ![Search results](/docs/images/search_results_number.png)

## 4. Further usage

- If you want to generate search index with your images, follow the instructions:
    - Delete `df_tag_db.pkl` file, and all images from `upload_images` directories.
    - Follow the instruction `1. Register image`.


# Directory structure

```
├─common
│  ├─config.ini         : Configuration file. Generate it by yourself
│  └─generate_tag_db.py : Main functions
├─docs                  : Defines this repository
├─upload_images         : Store uploaded images
│  └─images             : Your images
├─ df_tag_db.pkl        : Defines search index as pandas DataFrame
├─ st_app.py            : App in streamlit
└─ README.md            : Instruction of the repository
```

# References
- Azure Computer Vision
    - [Quick Start: Image analysis with Computer Vision](https://docs.microsoft.com/ja-jp/azure/cognitive-services/computer-vision/quickstarts-sdk/image-analysis-client-library?tabs=visual-studio&pivots=programming-language-python)
    - [Call the Image Analysis API in Azure Computer Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/how-to/call-analyze-image?tabs=python)
    - [computer_vision_samples in github](https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/blob/master/samples/vision/computer_vision_samples.py)
- Streamlit
    - [How to build stream app](https://docs.streamlit.io/library/api-reference)


[^1]: Refer to [detailed requirements for images](https://docs.microsoft.com/ja-jp/azure/cognitive-services/computer-vision/quickstarts-sdk/image-analysis-client-library?tabs=visual-studio&pivots=programming-language-python)

[^2]: Go to [streamlit doc](https://docs.streamlit.io/library/get-started) for more reference. 

[^3]: As we see, the presented tags are in Japanese. If you want to change the displayed language, change `language` in `common/config.ini` as `en`, for example. Go [here](/common/REAME.md), if you need more detail.
