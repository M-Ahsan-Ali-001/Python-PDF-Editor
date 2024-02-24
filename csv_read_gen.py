from flask import Flask,request
from flask_cors import CORS
import pandas as pd
import json
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict, PdfName

app = Flask(__name__)
CORS(app)

@app.route('/')
def helloworld():
    return "API is working!"

@app.route("/generateResult", methods=['POST'])

def genReport():
    print("*************************here*****************")
    csv_Read = pd.read_excel("E:\\test.xlsx")

    data= request.get_data()
    data = json.loads(data)
    print(data["name"])
    hold = csv_Read[ csv_Read["Name"]  ==data['name']]
    hold_list = hold.columns
    x =list(hold[hold.columns[0]])
    print(x)


    # Load PDF
    input_pdf = PdfReader("C:\\Users\\\\Downloads\\result_temp.pdf")

    # Assuming you have a list of field names and text values
    field_names = ["(Text1)", "(Text2)", "(0)", "(1)", "(2)", "(3)","(Text4)"]
    field_values = ["english", "john doe", "johndoe@example.com", "1", "4", "5", "32"]

# Update fields
    for page in input_pdf.pages:
              annotations = page['/Annots']

              for annotation in annotations:
                  field_name = annotation.get(PdfName.T)
                  print(field_name)
                  if field_name in field_names:
                   index = field_names.index(field_name)
                   x =list(hold[hold.columns[index]])
                   annotation.update(
                   {PdfName.V: '{}'.format(x[0]), PdfName.Ff: 1})

    # Save PDF
    output_pdf = PdfWriter()
    output_pdf.addpage(page)
    output_pdf.write('C:\\Users\\\\Downloads\\output.pdf')
    return request.get_data()



if __name__ =="__main__":
    app.run(debug=True,port=5001)