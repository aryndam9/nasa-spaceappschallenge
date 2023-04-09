from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def normalize(x, bounds):
    return bounds['desired']['lower'] + (x - bounds['actual']['lower']) * (bounds['desired']['upper'] - bounds['desired']['lower']) / (bounds['actual']['upper'] - bounds['actual']['lower'])

# the API prefix
api_altmetric = "http://api.altmetric.com/v1/doi/"
api_citation_total = "https://opencitations.net/index/coci/api/v1/citations/"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        doi = request.form['doi']
        response = requests.get(api_altmetric + doi)

        status_code = response.status_code 

        try:
            if status_code == 200:
                result = response.json()
                title = result['title']
                doi = result['doi']
                is_oa = 0 if result['is_oa'] == False else 1
                cited_by = [key for key in result.keys() if key.startswith('cited_by')]
                wanted_cited_by = ['cited_by_fbwalls_count', 'cited_by_feeds_count', 'cited_by_gplus_count', 'cited_by_msm_count', 'cited_by_posts_count', 'cited_by_rdts_count', 'cited_by_tweeters_count', 'cited_by_videos_count']
                required_cited_by = list(set(wanted_cited_by).intersection(cited_by))
                cited_by_results = sum([float(result[key]) for key in required_cited_by])
                total_citation = requests.get(api_citation_total + doi)
                total_citation_json = total_citation.json()
                total_citation_sum = len(total_citation_json)

                open_metric_score = (total_citation_sum/4)*is_oa + (total_citation_sum/2) + cited_by_results

                return render_template('index.html', title=title, doi=doi, open_metric_score=open_metric_score)
            else:
                return render_template('index.html', error=True)
        except:
            return render_template('index.html', error=True)
    else:
        return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
