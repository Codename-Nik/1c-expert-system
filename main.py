import clips
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        env = clips.Environment()
        env.load('static/clips_rules/rules.clp')
        env.reset()

        env.assert_string(f'(business (industry {request.form["industry"]})')  
        env.run()  

        for fact in env.facts():
            if "recomendation" in str(fact):
                result = str(fact).split('"')[1]
                return render_template('index.html', result=result)
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)