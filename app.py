from flask import Flask, render_template, request
from conversion_utils import ConversionType, Notation, CONVERSION_MAP, random_number, check, convert


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

    
@app.route("/new_conversion", methods=["POST"])
def new_conversion():
    #  Get conversion type from form and convert to enum
    conversion_type_str = request.form.get("conversion_type")
    conversion_type = ConversionType[conversion_type_str]

    #  Use mapping to fill in variables
    mapping = CONVERSION_MAP[conversion_type]
    original_notation = mapping['original_notation']
    new_notation = mapping['new_notation']

    #  Create string representatives
    original_notation_str = original_notation.name.lower()
    new_notation_str = new_notation.name.lower()

    #  Generate random number
    generated_number = random_number(original_notation)
    
    return render_template("conversion.html", original_notation=original_notation_str, new_notation=new_notation_str, original_value=generated_number, conversion_type=conversion_type_str)

@app.route("/check_answer", methods=["POST"])
def check_answer():
    #  Use conversion type to get values from mapping
    conversion_type_str = request.form.get("conversion_type")
    conversion_type = ConversionType[conversion_type_str]

    mapping = CONVERSION_MAP[conversion_type]
    original_notation = mapping['original_notation']
    new_notation = mapping['new_notation']

    #  Get values from form
    original_value = request.form.get("original_value")
    user_answer = request.form.get("answer")

    #  Create string representatives
    original_notation_str = original_notation.name.lower()
    new_notation_str = new_notation.name.lower()

    #  Call functions
    correct_answer = convert(original_notation, new_notation, original_value)
    is_correct = check(correct_answer, user_answer)
    
    return render_template("result.html", is_correct=is_correct, correct_answer=correct_answer, user_answer=user_answer, original_value=original_value, original_notation=original_notation_str, new_notation=new_notation_str)
    

