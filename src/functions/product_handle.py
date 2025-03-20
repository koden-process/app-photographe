import pandas as pd
import uuid
from functions.folder_handle import list_folders


class ProductProcessor:
    def __init__( self, path: str, prefixe: str ):
        self.path = path
        self.prefixe = prefixe
        self.folders = list_folders(path)

    def process_folders( self ):
        result = []
        for folder in self.folders:
            df = self.load_csv(folder)
            df = self.add_url_column(df, folder)
            dfs = self.split_dataframes_by_lot(df)
            result.extend(self.create_products_from_dfs(dfs, folder))
        return result

    def load_csv( self, folder: str ) -> pd.DataFrame:
        path_csv = f'{self.path}/{folder}/done.csv'
        return pd.read_csv(path_csv)

    def add_url_column( self, df: pd.DataFrame, folder: str ) -> pd.DataFrame:
        prefixe = f"{self.prefixe}/{folder}/"
        df['url'] = df['uuid'].apply(lambda x: prefixe + x)
        return df

    def split_dataframes_by_lot( self, df: pd.DataFrame ) -> dict:
        dfs = {}
        for lot in df['folder'].unique():
            dfs[lot] = df[df['folder'] == lot].copy()
        return dfs

    def create_products_from_dfs( self, dfs: dict, folder: str ) -> list:
        result = []
        for product, df_product in dfs.items():
            df_product = self.clean_dataframe(df_product)
            datas = df_product.to_dict(orient='records')
            result.append(self.create_product_entry(datas, folder))
        return result

    def clean_dataframe( self, df: pd.DataFrame ) -> pd.DataFrame:
        df.drop(['folder', 'uuid', 'date'], axis=1, inplace=True)
        return df

    def create_product_entry( self, datas: list, folder: str ) -> dict:
        product_uuid = uuid.uuid4()
        print(product_uuid)
        nb_photos = len(datas)
        return {
            'product_uuid': str(product_uuid),
            'product_names': ['package photo programme'],
            'id_tags': [],
            'group_tags': [],
            'subgroup_tags': [],
            'period_tags': [folder],
            'category_tags': [],
            'subcategory_tags': [],
            'subject_tags': [],
            'location_tags': [],
            'source_tags': ['Sébastien HELIGON - photographe'],
            'color_tags': [],
            'size_tags': [],
            'description': f'{nb_photos} photos',
            'img_cover': datas[0]['url'],
            'price': 25,
            'files': datas
        }
