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

"""
def highlight_sentences(cell):
    if isinstance(cell, str):
        return 'background-color: yellow'
    return ''
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    csv_file = None

    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.xlsx'):
            if not os.path.exists('input'):
                os.makedirs('input')
            if not os.path.exists('output'):
                os.makedirs('output')
            save_location = os.path.join('input', file.filename)
            file.save(save_location)
            
            sentences_df = pd.read_excel(file)
            sentences = sentences_df['Text']
            emb = co.embed(texts = list(sentences),model='embed-english-v2.0').embeddings
            num_sentences = len(emb)
            similarities = np.zeros((num_sentences, num_sentences))

            for i in range(num_sentences):
                for j in range(i, num_sentences):
                    similarity = np.dot(emb[i], emb[j])/(np.linalg.norm(emb[i]) * np.linalg.norm(emb[j]))
                    similarity_percentage = 0.5 * (1 + similarity) * 100
                    similarities[i, j] = similarity_percentage
                    similarities[j, i] = similarity_percentage

            distance_df = pd.DataFrame(similarities, index = sentences, columns = sentences)

            #styled_df = distance_df.style.applymap(highlight_cells)
            
            csv_filename = 'Sentence_similarity.xlsx'
            distance_df.to_excel('output/Sentence_similarity.xlsx', engine = 'openpyxl')
            csv_file = csv_filename

            return redirect(url_for('download'))

    return render_template('index.html')

@app.route('/download')
def download():
    return render_template('download.html', files = os.listdir('output'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    app.run(debug=False)
        
