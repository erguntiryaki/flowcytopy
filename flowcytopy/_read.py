import flowkit as fk
import anndata as ad
import pandas as pd


def read_fcs(path,
             format= 'df',
             source= 'raw'
             ):

    samp = fk.Sample(path)
    if format == 'df':
        dformat = samp.as_dataframe(source= source)
    elif format == 'adata'
        dformat = samp.as_dataframe(source= source)
        dformat = ad.AnnData(X= dformat.to_numpy(),
                             obs= pd.DataFrame(df.index.to_numpy(dtype='str'), columns=['events']).set_index('events'),
                             var= pd.DataFrame(df.columns.to_numpy(dtype='str'), columns=['parameters']).set_index('parameters')
                             )
    else:
        raise ValueError('Selected data format must be DataFrame (df) or AnnData (adata)')

    return = dformat

