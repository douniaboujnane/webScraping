import pandas as pd

async def save_data_to_csv(data, filename='centris_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, encoding='utf-8-sig')
    print(f"Data saved to {filename}")
