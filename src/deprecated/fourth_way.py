from powerbiclient import Report, models
import pandas as pd

# Load the report
report = Report("Pair1_Report1.pbix")

# Get the report page
page = report.get_page("Page1")

# Get the visuals on the page
visuals = page.get_visuals()

# Loop through the visuals and extract the data
for visual in visuals:
    # Get the data for the visual
    data = visual.get_data(models.VisualDataRequest(include_visual_data=True))

    # Extract the rows and columns from the data
    rows = data["visual"]["dataPoints"]["rows"]
    columns = data["visual"]["dataPoints"]["columns"]

    # Convert the rows and columns to a Pandas DataFrame
    df = pd.DataFrame(rows, columns=columns)

    # Print the DataFrame
    print(df)
