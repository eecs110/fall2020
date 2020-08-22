import collections
import pandas as pd
import json
import sys
import traceback


def _flatten(d:dict, parent_key:str='', sep:str='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(_flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_image_html(image_url:str):
    '''
    Creates an image (HTML)
        * image_url (str): [Required] The url of the image.
    Returns an HTML image tag (str).
    '''
    from IPython.display import Image
    return Image(url=image_url)._repr_html_()

def flatten_for_pandas(data:list):
    '''
    Converts a list of nested dictionaries into a list of flattened 
    dictionaries that can be more easilty displayed using pandas.
        * data (list): [Required] a list of dictionaries
    Returns a flattened list of dictionaries (list).
    '''
    flattened_list = []
    count = 1
    for item in data:
        item = _flatten(item)
        item['num'] = count
        flattened_list.append(item)
        count += 1
    return flattened_list
    
def get_dataframe(data:list):
    '''
    Converts a list of dictionaries into a flattened pandas dataframe.
    '''
    flattened_list = flatten_for_pandas(data)
    return pd.DataFrame(flattened_list).set_index('num')

def get_jupyter_styling():
    return """
        <style>
            .rendered_html img { 
                display: inline-block; 
                vertical-align: baseline;
                max-width: 200px !important;
                margin-right: 20px !important;
            }
            .rendered_html td, .rendered_html th { text-align: left !important; }
        </style>
        """

def get_error_message(e, url=None):
    errors = []
    if url:
        errors.append('This URL is invalid: ' + url)
    tokens = traceback.format_exc().split('\n')
    if len(tokens):
        errors.extend(tokens[0:3])
    return '\n'.join(errors)
