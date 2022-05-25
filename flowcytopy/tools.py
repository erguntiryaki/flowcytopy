import pacmap as pm
import trimap as tm

def trimap(adata,
           use_rep= 'X_pca',
           copy= False,
           **kwargs):

    tm_reducer = tm.TRIMAP(**kwargs)
    if use_rep == 'X':
        reduced = tm_reducer.fit_transform(adata.X)
    else:
        reduced = tm_reducer.fit_transform(adata.obsm[use_rep])
    adata.obsm['X_trimap'] = reduced
    return  adata if copy else None

def pacmap(adata,
           use_rep= 'X_pca',
           copy= False,
           **kwargs):

    pm_reducer = pm.PaCMAP(**kwargs)
    if use_rep == 'X':
        reduced = pm_reducer.fit_transform(adata.X)
    else:
        reduced = pm_reducer.fit_transform(adata.obsm[use_rep])
    adata.obsm['X_pacmap'] = reduced
    return adata if copy else None
