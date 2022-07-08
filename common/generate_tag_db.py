import os
import pandas as pd
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

class generate_tag_db():
    '''
    The class provides functions, where you can search analyzed tags for each image.    
    '''
    def __init__(self
                ,subscription_key
                ,cv_endpoint
                ,language
                ,features
                ,tag_db_file
                ,tag_db_columns
                ,upload_dir):
        # Azure Subscription
        self.subscription_key = subscription_key
        # Azure Computer Vision(CV)
        ## Endpoint of CV
        self.cv_endpoint = cv_endpoint
        ## Set language in CV
        self.language = language
        ## Set features to be extracted in CV
        self.features = features
        # Set tag db file, which stores tags predicted by Azure CV 
        self.tag_db_file = tag_db_file
        # Set columns for tag db file
        self.tag_db_columns = tag_db_columns
        # tag db
        self.df_tag_db = None
        # Set directory for storing images
        self.upload_dir = upload_dir
        # Set how many images are shown in display
        self.topN = 5

    def read_image(self
                    ,wkdir : str
                    ,image_file : str):
        '''
        - Input
            wkdir: path to image
            image_file: file name of image
        - Process
            Open the image file
        - Output
            Stream I/O of image file        
        '''
        read_image_path = os.path.join(wkdir, image_file)
        return open(read_image_path, "rb")

    def load_tag_db(self) -> pd.DataFrame():
        '''
        - Process
            Load/Initialize tag db
        - Output
            tag db
        '''
        if os.path.exists(self.tag_db_file):
            print('file exists!')
            df_tag_db = pd.read_pickle(self.tag_db_file)
        else:
            df_tag_db = pd.DataFrame([], columns=self.tag_db_columns)
        return df_tag_db

    def generate_tag_database(self
                    ,image_file: str) -> pd.DataFrame():
        '''
        - Input
            image_file: file name of image
        - Process
            After loading image, consume Azure CV, and parse the results
        - Output
            Parsed tag information predicted by Azure CV
        '''
        ## Load image
        image_data = self.read_image(self.upload_dir, image_file)

        ## Analyze image with Computer Vision
        computervision_client = ComputerVisionClient(self.cv_endpoint
                                                ,CognitiveServicesCredentials(self.subscription_key))
        results_local = computervision_client.analyze_image_in_stream(image_data
                                                                    ,self.features
                                                                    ,language=self.language)

        ## extract tags
        list_tag_db = [[image_file, tag.name, tag.confidence] for tag in results_local.tags]
        return pd.DataFrame(list_tag_db, columns=self.tag_db_columns)

    def analyze_insert_tag(self
                        ,image_file: str) -> None:
        '''
        - Input
            image_file: file name of image
        - Process
            - Load tag db, if exists
            - Analyze image with Azure CV
            - Insert the analyzed results into tag db
        - Output
            Dataframe with analyzed tags in full
        '''
        ## Load tag_db 
        self.df_tag_db = self.load_tag_db()
        self.df_tag_db = self.df_tag_db[self.df_tag_db['image_name'] != image_file]

        ## Analyze image with Azure CV
        df_tag_db_tmp = self.generate_tag_database(image_file)

        ## insert records into tag db
        if os.path.exists(self.tag_db_file):
            df_tag_db = pd.read_pickle(self.tag_db_file)
            df_tag_db = pd.concat([df_tag_db, df_tag_db_tmp], axis=0)
        else:
            df_tag_db = df_tag_db_tmp
        df_tag_db = df_tag_db.reset_index(drop=True)
        df_tag_db.to_pickle(self.tag_db_file)
        return df_tag_db_tmp

    def extract_records_from_db_with_word(self
                                        ,word) -> list:
        self.df_tag_db =self.load_tag_db()
        return self.df_tag_db[self.df_tag_db['tag'] == word].sort_values(self.tag_db_columns[2], ascending=False)
