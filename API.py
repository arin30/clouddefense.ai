import requests

def consumeGETRequestSync():
    data = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "record.document": "SOME_JOURNAL"
                        }
                    },
                    {
                        "match": {
                            "record.articleTitle": "farmers"
                        }
                    }
                ],
                "must_not": [],
                "should": []
            }
        },
        "from": 0,
        "size": 50,
        "sort": [],
        "facets": {}
    }

    url = 'https://www.clouddefense.ai/kubernetes-security-posture-management-kspm/'
    headers = {"Accept": "application/json"}

    # Make the GET request with params and headers
    response = requests.get(url, params=data, headers=headers)

    print("code:", response.status_code)
    print("******************")
    print("headers:", response.headers)
    print("******************")
    print("content:", response.text)

consumeGETRequestSync()
