# knowledge_mining_computer_vision

# Overview

This repository provides search experience with your images by [Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/).

With [stramlit](https://streamlit.io/) framework, we can easily build an app, and customize with your preferences.

# Prerequisites

- [Python environment](https://www.python.org/)
- [Azure subscription](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/fundamental-concepts#azure-terminology)

# How to build an app

1. Install necessary libraries in python:

    ```sh
    pip install -r ./requirement.txt
    ```

2. Configure the environment in `common/config.ini`:

    ```sh
    [Azure]
    subscription_key = 12345xxxyyy
    cv_endpoint = https://xxxx.cognitiveservices.azure.com/
    language = ja
    ```

    | variables        | description                                                             |
    | ---------------- | ----------------------------------------------------------------------- |
    | subscription_key | Azure subscription                                                      |
    | cv_endpoint      | Rest Endpoint URL provided by Azure Computer Vision                     |
    | language         | Used for the language specifying the language in Azure Computer Vision. |


3. Run streamlit app with your terminal:

    ```sh
    streamlit run ./st_app.py
    ```

    You will find the following message, and please copy and pate the URL in your browser:

    ```
    You can now view your Streamlit app in your browser.
    Local URL: http://localhost:8501
    Network URL: http://xxx.xxx.xxx.xxx:8501
    ```

    For more reference about streamlit, please go to [streamlit doc](https://docs.streamlit.io/library/get-started).

    You can see the following page, if you successfully run your app:

    ![top page](/docs/images/top_page.png)

# How to use the app

1. Register image

    In order to register your image, please select your image in your local folder

    ![browse image](/docs/images/browse_image.png)

    Once you select your image, you will find the analyzed result:

    ![analyzed image](/docs/images/analized_results.png)

    As we see, the presented tags are in Japanese. If you change the language, please change `language` in `common/config.ini` as `en`, for example.

2. Search image

    If you input your interest by word, your will find the search results:

    ![Search result](/docs/images/search_results.png)

3. Customize your preferences

    If you want to more results, please change the prarmeters:

    - topN: `5` tags are shown in each picture
    ![topN](/docs/images/topN.png)

    - Search result: `4` search results are shown
    ![Search results](/docs/images/search_results_number.png)


# Directory structure

```
├─common
│  └─config.ini         : configuration like Azure subscription, etc
│  └─generate_tag_db.py : Main functions
├─docs                  : It defines this repository
├─upload_images         : Store uploaded images
│  └─images
├─ st_app.py             : App in streamlit
└─ REAME.md              : Instruction of the repository
```

# References
- [Call the Image Analysis API in Azure Computer Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/how-to/call-analyze-image?tabs=python)
- [How to build stream app](https://docs.streamlit.io/library/api-reference)