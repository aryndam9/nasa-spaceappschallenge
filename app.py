import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def normalize(x, bounds):
    return bounds['desired']['lower'] + (x - bounds['actual']['lower']) * (bounds['desired']['upper'] - bounds['desired']['lower']) / (bounds['actual']['upper'] - bounds['actual']['lower'])

@app.route('/open-metric-score', methods=['GET'])
def get_open_metric_score():
    # the API prefix
    api_altmetric = "http://api.altmetric.com/v1/doi/"
    api_citation_total = "https://opencitations.net/index/coci/api/v1/citations/"
    # Input the DOI of the required paper
    doi = request.args.get('doi')
    # the request from the API
    response = requests.get(api_altmetric + doi)

    status_code = response.status_code 
    # checking to see whether our response worked out
    #  respone code 200 means everything went okay

    try:
        if status_code == 200:
            # convert json to dictionary format
            result = response.json()
            # get the title , doi, is_open access
            title = result['title']
            doi = result['doi']
            is_oa = 0 if result['is_oa'] == False else 1  # this is the article is open access or not
            # get all the columns starting with cited_by
            cited_by = [key for key in result.keys() if key.startswith('cited_by')]
            wanted_cited_by = ['cited_by_fbwalls_count', 'cited_by_feeds_count', 'cited_by_gplus_count', 'cited_by_msm_count', 'cited_by_posts_count', 'cited_by_rdts_count', 'cited_by_tweeters_count', 'cited_by_videos_count']
            # find intersecctin between wanted_cited_by and cited_by
            required_cited_by = list(set(wanted_cited_by).intersection(cited_by))
            # get cols in required_cited_by
            cited_by_results = sum([float(result[key]) for key in required_cited_by]) # this is the total societal engagement
            # get total citations of a paper
            total_citation = requests.get(api_citation_total + doi)
            total_citation_json = total_citation.json()
            total_citation_sum = len(total_citation_json)  # this is the total citation

            # calculate the open metric score
            open_metric_score = (total_citation_sum/4)*is_oa + (total_citation_sum/2) + cited_by_results

            # return the result as JSON object
            return jsonify({
                'title': title,
                'doi': doi,
                'open_metric_score': open_metric_score
            })
        else:
            return jsonify({'error': 'Response code is not 200'})
    except:
        return jsonify({'error': 'Something went wrong'})

if __name__ == '__main__':
    app.run(debug=True)
