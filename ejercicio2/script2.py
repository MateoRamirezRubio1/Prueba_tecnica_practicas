import numpy as np
import pandas as pd
from pathlib import Path

# Constants
CASOS_FILE_PATH = Path('../ejercicio1/df_casos_bd.xlsx')  # Path to the cases Excel file
META_FILE_PATH = Path('../Prueba_Tecnica_Practicante.xlsx')  # Path to the goals Excel file
OUTPUT_FILE_PATH = Path('./df_casos_union.xlsx')  # Path for the output Excel file

def load_excel_data(file_path: Path, sheet_name: str) -> pd.DataFrame:
    """
    Load data from a specific sheet in an Excel file.
    
    Parameters:
        file_path (Path): The path to the Excel file.
        sheet_name (str): The name of the sheet to load.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the specified sheet.

    Raises:
        FileNotFoundError: If the specified Excel file does not exist.
        ValueError: If the specified sheet cannot be loaded.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError as e:
        raise ValueError(f"Could not load sheet '{sheet_name}': {e}")

def merge_dataframes(casos_df: pd.DataFrame, meta_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge the cases DataFrame with the goals DataFrame.

    Parameters:
        casos_df (pd.DataFrame): DataFrame containing cases data.
        meta_df (pd.DataFrame): DataFrame containing goals data.

    Returns:
        pd.DataFrame: DataFrame resulting from the merge operation.
    """
    return pd.merge(casos_df, meta_df, on=['Red', 'Tipo'], how='left')

def calculate_cumplimiento(merged_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the compliance percentage and round it up.

    Parameters:
        merged_df (pd.DataFrame): DataFrame containing the combined information.

    Returns:
        pd.DataFrame: DataFrame with the compliance column added.
    """
    # Calculate the compliance percentage
    merged_df['Cumplimiento'] = (merged_df['Cant_Casos'] / merged_df['Meta']) * 100

    # Round up the compliance percentage
    merged_df['Cumplimiento'] = np.ceil(merged_df['Cumplimiento'])
    
    # Format the 'Cumplimiento' column to display as a percentage string
    merged_df['Cumplimiento'] = merged_df['Cumplimiento'].astype(int).astype(str) + '%'
    return merged_df

def save_to_excel(df: pd.DataFrame, output_path: Path) -> None:
    """
    Save the DataFrame to an Excel file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        output_path (Path): The path of the output Excel file.
    """
    df.to_excel(output_path, index=False)
    print(f"File successfully exported to: {output_path}")

def main():
    """
    Main function to execute the loading, transformation, and exporting of data.
    """
    # Load data from the cases and goals files
    casos_df = load_excel_data(CASOS_FILE_PATH, sheet_name='Sheet1')
    meta_df = load_excel_data(META_FILE_PATH, sheet_name='Meta')

    # Merge the DataFrames
    merged_df = merge_dataframes(casos_df, meta_df)

    # Calculate the compliance percentage
    merged_df = calculate_cumplimiento(merged_df)

    # Export the resulting DataFrame to an Excel file
    save_to_excel(merged_df, OUTPUT_FILE_PATH)

if __name__ == "__main__":
    main()
