import pandas as pd
from pathlib import Path

# Constants
EXCEL_PATH = Path("../Prueba_Tecnica_Practicante.xlsx")  # Path to the Excel file containing case data
SHEET_NAME = "Casos"  # Name of the sheet to load from the Excel file
OUTPUT_PATH = Path("./df_casos_bd.xlsx")  # Path where the transformed DataFrame will be saved as an Excel file
DATE_FORMAT = "%d/%m/%Y"  # Format to be used for date representation

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
        excel_data = pd.ExcelFile(file_path)
        df = excel_data.parse(sheet_name)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError as e:
        raise ValueError(f"Could not load sheet '{sheet_name}': {e}")

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the initial DataFrame into the specified format.
    
    Parameters:
        df (pd.DataFrame): The original DataFrame.

    Returns:
        pd.DataFrame: The transformed DataFrame.
    """
    # Forward fill null values in the 'Red' column without using inplace
    df['Red'] = df['Red'].ffill()
    
    # Use melt to transform the DataFrame from wide to long format
    df_melted = df.melt(id_vars=["Red", "Tipo"], var_name="Fecha", value_name="Cant_Casos")
    
    # Convert the 'Fecha' column to datetime format and format it to the specified date format
    df_melted['Fecha'] = pd.to_datetime(df_melted['Fecha']).dt.strftime(DATE_FORMAT)
    
    return df_melted

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
    Main function to execute the data transformation and export process.
    """
    # Load data from the 'Casos' sheet
    casos_df = load_excel_data(EXCEL_PATH, SHEET_NAME)
    
    # Transform the data to the specified format
    df_casos_bd = transform_data(casos_df)
    
    # Export the DataFrame to an Excel file
    save_to_excel(df_casos_bd, OUTPUT_PATH)

if __name__ == "__main__":
    main()
