import pandas as pd

def read_dat_file(filename):
    """
    Read .dat file, discards some row headers and returns appropriate values.
    Parameters
    ----------
    filename : string with path and filename do .dat file
    Returns
    -------
    df : pandas.DataFrame
        A pandas dataframe contatining the data.
    """
    df = pd.read_csv(filename, skiprows=3)
    df_aux = pd.read_csv(filename, header=1)
    df.columns = df_aux.columns

    cols_to_drop = ['RECORD', 'Excedente_Avg', 'Compra_Avg']
    for col in cols_to_drop:
        if col in df.columns:
            df = df.drop([col], axis=1)

    for column in df.columns:
        if column != "TIMESTAMP":
            df[column] = df[column].astype('float')
    # Drop column 'RECORD' (if present) because from june 2019 is is no longer used
    return df