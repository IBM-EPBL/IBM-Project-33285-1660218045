from flask import Flask,request,json

app=Flask(__name__)

food_items={"1":"rice", "2":"bean", "3":"yam" ,"4":"plantain" ,"5":"potato" ,"6":"wheat" }

@app.route('/data',methods=['GET','POST'])
def api():
    if request.method=='GET':
        return food_items
    if request.method=='POST':
        data=request.json
        food_items.update(data)
        return 'data got inserted'

@app.route("/data/<id>",methods=['PUT'])
def update(id):
    data=request.form['item']
    food_items[str(id)]=data
    return 'data updated'

@app.route("/data/<id>",methods=["DELETE"])
def deleteoperation(id):
    food_items.pop(str(id))
    return 'data deleted'

if __name__=='__main__':
    app.run(debug=True)