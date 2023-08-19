from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
product = pickle.load(open('product.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('site.html',
                           product_name = list(popular_df['product_name'].values),
                           image=list(popular_df['product_url'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/indexx')
def recommend_ui():
    return render_template('indexx.html')

@app.route('/recommend_product',methods=['post'])
def recommend():
    user_input = request.form.get('q')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = product[product['product_name'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('product_name')['product_name'].values))
        item.extend(list(temp_df.drop_duplicates('product_name')['product_url'].values))

        data.append(item)

    print(data)

    return render_template('indexx.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)