import pandas as pd

def txt_to_csv(data, savepath):
    df = pd.read_csv(data, sep='\s+')
    df.columns = ["Time", "Audio"]
    cols = list(df.columns)
    for header in cols:
        df[header].apply(lambda x: '%.7f' % x)
    df.to_csv(savepath, index=False)


if __name__ == "__main__":
    for i in range (0, 3):
        data = f"data/Lab_4/music/music{i}_raw.txt"
        savepath = f"data/Lab_4/music/music{i}_csv.csv"
        txt_to_csv(data, savepath)
