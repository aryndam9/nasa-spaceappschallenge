from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# def open_score(is_oa, cited_by_social, total_citation_sum):
#     normalized_is_oa = is_oa / max(is_oa, cited_by_social, total_citation_sum)
#     normalized_cited_by_social = cited_by_social / max(is_oa, cited_by_social, total_citation_sum)
#     normalized_total_citation_sum = total_citation_sum / max(is_oa, cited_by_social, total_citation_sum)

#     open_metric_score = ((normalized_is_oa * 0.25) + (normalized_cited_by_social * 0.25) + (normalized_total_citation_sum * 0.5)) * 100

#     return open_metric_score

def open_score(is_oa, cited_by_social, total_citation_sum):
    # final_number = ((x - min(x, y, z)) / (max(x, y, z) - min(x, y, z)) * 0.25
# + (y - min(x, y, z)) / (max(x, y, z) - min(x, y, z)) * 0.25
# + (z - min(x, y, z)) / (max(x, y, z) - min(x, y, z)) * 0.5) * 100
    
    final_number = ((is_oa - min(is_oa, cited_by_social, total_citation_sum)) / (max(is_oa, cited_by_social, total_citation_sum) - min(is_oa, cited_by_social, total_citation_sum)) * 0.25
+ (cited_by_social - min(is_oa, cited_by_social, total_citation_sum)) / (max(is_oa, cited_by_social, total_citation_sum) - min(is_oa, cited_by_social, total_citation_sum)) * 0.25
+ (total_citation_sum - min(is_oa, cited_by_social, total_citation_sum)) / (max(is_oa, cited_by_social, total_citation_sum) - min(is_oa, cited_by_social, total_citation_sum)) * 0.5) * 100
    
    return final_number


# the API prefix
api_altmetric = "http://api.altmetric.com/v1/doi/"
api_citation_total = "https://opencitations.net/index/coci/api/v1/citations/"

@app.route('/', methods=['GET', 'POST'])
def home():

    open_metric_score = None  # reset open_metric_score to None



    if request.method == 'POST':
        doi = request.form['doi']
        response = requests.get(api_altmetric + doi)

        status_code = response.status_code 

        try:
            if status_code == 200:
                result = response.json()
                title = result['title']
                doi = result['doi']
                is_oa = 0 if result['is_oa'] == False else 25
                cited_by_social = result['cited_by_posts_count']
                
                total_citation = requests.get(api_citation_total + doi)
                total_citation_json = total_citation.json()
                total_citation_sum = len(total_citation_json)

                open_metric_score = open_score(is_oa, cited_by_social, total_citation_sum)

                return render_template('index.html', title=title, doi=doi, open_metric_score=round(open_metric_score, 2))
            else:
                return render_template('index.html', error=True)
        except:
            return render_template('index.html', error=True)
    else:
        return render_template('index.html', open_metric_score=open_metric_score)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
