import requests, re, os, sys

def get_webpage(url):
    # Send an HTTP GET request to the URL
    headers = {
        'User-Agent': 'curl/7.68.0'
    }
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


# download all
for i in range(49):
    url = 'https://wordpress.org/plugins/browse/popular/page/%d/' % i
    page = get_webpage(url)
    
    # gather plugin urls
    match = re.findall('"https://wordpress.org/plugins/([a-zA-Z0-9_-]+)/" rel="bookmark"', page)
    match = list(set(match))
    print(match)

    # go to download page for each plugins
    for s in match:
        url = 'https://wordpress.org/plugins/%s/' % s
        page = get_webpage(url)
        if page:
            # get download link
            match = re.findall('"https://downloads.wordpress.org/plugin/([a-zA-Z0-9_.-]+)zip">Download', page)
            match = list(set(match))
            print(match)
            try:
                link = "https://downloads.wordpress.org/plugin/%szip" % match[0]
                os.system("wget %s" % link)
            except:
                print("can't find link. skip")
            input()

