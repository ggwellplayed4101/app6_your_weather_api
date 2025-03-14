from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Process the date to remove hyphens
    date_processed = date.replace("-", "")
    
    # Construct the filename
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    
    try:
        df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    except FileNotFoundError:
        return {"error": "Station not found"}, 404

    # Query the dataframe for the processed date
    temperature = df.loc[df['    DATE']==date_processed]['   TG'].squeeze() / 10
    
    # Handle missing temperature values (e.g., -9999)
    if temperature == -9999:
        return {"error": "Temperature data missing for this date"}, 404
    
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True)