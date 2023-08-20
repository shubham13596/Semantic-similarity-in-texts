import cohere
import os
import pandas as pd
from flask import Flask, render_template, request, send_file, redirect, url_for, send_from_directory
import numpy as np
from scipy.spatial.distance import euclidean

app = Flask(__name__)

#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv())

co = cohere.Client(os.environ['COHERE_API_KEY'])

@app.route('/', methods=['GET', 'POST'])
def index():
    csv_file = None

    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            save_location = os.path.join('input', file.filename)
            file.save(save_location)
            
            sentences_df = pd.read_excel(file)
            sentences = sentences_df['Discussion point']
            emb = co.embed(texts = list(sentences),model='embed-english-v2.0').embeddings
            num_sentences = len(emb)
            distances = np.zeros((num_sentences, num_sentences))

            for i in range(num_sentences):
                for j in range(i + 1, num_sentences):
                    distance = euclidean(emb[i], emb[j])
                    distances[i, j] = distance
                    distances[j, i] = distance

            distance_df = pd.DataFrame(distances)
            csv_filename = 'pairwise_distances2.csv'
            distance_df.to_csv('output/pairwise_distances2.csv', index=False, header=False)
            csv_file = csv_filename
            #return send_from_directory('output', csv_file)
            return redirect(url_for('download'))

    return render_template('index.html')

@app.route('/download')
def download():
    return render_template('download.html', files = os.listdir('output'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    app.run(debug=True)
        
