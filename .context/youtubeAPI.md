### Setup and Installation Commands

Source: https://developers.google.com/youtube/reporting/guides/authorization/server-side-web-apps

Commands to initialize the project directory, install the Google API client library, and start the local development server.

```bash
mkdir ~/php-oauth2-example
cd ~/php-oauth2-example
```

```bash
composer require google/apiclient:^2.15.0
```

```bash
php -S localhost:8080 ~/php-oauth2-example
```

--------------------------------

### PHP: Setup and Run OAuth2 Example

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps?hl=ru

This example demonstrates the initial setup steps for a PHP application using the Google API Client Library to authenticate and retrieve YouTube channel information. Ensure you have Composer installed and the client secret JSON file.

```bash
mkdir ~/php-oauth2-example
cd ~/php-oauth2-example
```

```bash
composer require google/apiclient:"^2.15.0"
```

```bash
php -S localhost:8080 ~/php-oauth2-example
```

--------------------------------

### Setup Node.js Project Environment

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=fa

Commands to initialize a directory and install the Google API client library for Node.js.

```bash
mkdir ~/nodejs-oauth2-example
cd ~/nodejs-oauth2-example
```

```bash
npm install googleapis
```

```bash
node .\main.js
```

--------------------------------

### PHP - Setup Local Environment

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Commands to set up a local directory and install the Google API Client Library for PHP using Composer.

```bash
mkdir ~/php-oauth2-example
cd ~/php-oauth2-example
```

```bash
composer require google/apiclient:"^2.15.0"
```

--------------------------------

### Create Project Directory

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Creates a new directory for the Node.js OAuth2 example and changes into it. This is part of the setup process before installing dependencies.

```bash
mkdir ~/nodejs-oauth2-example
cd ~/nodejs-oauth2-example
```

--------------------------------

### Run the Go Quickstart

Source: https://developers.google.com/youtube/v3/quickstart/go

Command to execute the quickstart script.

```bash
go run quickstart.go
```

--------------------------------

### Execute Node.js Quickstart

Source: https://developers.google.com/youtube/v3/quickstart/nodejs

Command to run the quickstart script in the terminal.

```bash
node quickstart.js
```

--------------------------------

### Webapp2 Request Handler Setup

Source: https://developers.google.com/youtube/v3/code_samples/python_appengine?hl=de

Sets up a webapp2 request handler for the application. This example maps all paths to the MainHandler.

```python
app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
], debug=True)
```

--------------------------------

### Install Google API Client Library for Node.js

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Installs the Google API Client Library for Node.js using npm. This is a prerequisite for running the Node.js OAuth2 example.

```bash
npm install googleapis
```

--------------------------------

### Start a local web server

Source: https://developers.google.com/youtube/v3/quickstart/js

Commands to serve local files for testing API requests. Choose the version corresponding to your installed Python environment.

```bash
python -m SimpleHTTPServer 8000
```

```bash
python -m http.server 8000
```

--------------------------------

### Run Node.js Example

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Executes the Node.js OAuth2 example using the Node.js runtime. Ensure the `main.js` file is created with the example content.

```bash
node .\main.js
```

--------------------------------

### Run Quickstart Script

Source: https://developers.google.com/youtube/v3/quickstart/ruby

Command to execute the Ruby quickstart script. The first run will initiate an authorization process.

```bash
ruby quickstart.rb
```

--------------------------------

### Command-line argument examples

Source: https://developers.google.com/youtube/partner/guides/upload

Examples of command-line flags used to configure video upload parameters.

```bash
--file="/home/path/to/file.mov"
```

```bash
--channelId="UC_x5XG1OV2P6uZZ5FSM9Ttw"
```

```bash
--title="Summer vacation in California"
```

```bash
--description="Had a great time surfing in Santa Cruz"
```

```bash
--category=22
```

```bash
--keywords="surfing, beach volleyball"
```

```bash
--privacyStatus="private"
```

```bash
--policyId="S309961703555739"
```

--------------------------------

### Create Directory and Navigate

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=fa

Commands to create a new directory for the PHP OAuth2 example and change into it. This is a prerequisite for setting up the example.

```bash
mkdir ~/php-oauth2-example
cd ~/php-oauth2-example
```

--------------------------------

### Configure Flask Web Server

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Example line used in Flask applications to start a local web server for OAuth flows.

```python
app.run('localhost', 8080, debug=True)
```

--------------------------------

### Set up YouTube Data API Ruby Quickstart Sample

Source: https://developers.google.com/youtube/v3/quickstart/ruby

Initializes the Ruby sample code for the YouTube Data API quickstart. Ensure you replace placeholder values for REDIRECT_URI, CLIENT_SECRETS_PATH, and CREDENTIALS_PATH with your specific details.

```ruby
# Sample Ruby code for user authorization

require 'rubygems'
gem 'google-api-client', '>0.7'
require 'google/apis'
require 'google/apis/youtube_v3'
require 'googleauth'
require 'googleauth/stores/file_token_store'

require 'fileutils'
require 'json'

# REPLACE WITH VALID REDIRECT_URI FOR YOUR CLIENT
REDIRECT_URI = 'http://localhost'
APPLICATION_NAME = 'YouTube Data API Ruby Tests'

# REPLACE WITH NAME/LOCATION OF YOUR client_secrets.json FILE
CLIENT_SECRETS_PATH = 'client_secret.json'

# REPLACE FINAL ARGUMENT WITH FILE WHERE CREDENTIALS WILL BE STORED
CREDENTIALS_PATH = File.join(Dir.home, '.credentials',
                             "youtube-quickstart-ruby-credentials.yaml")


```

--------------------------------

### Install Ruby Client Library

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Install the Google APIs Client Library for Ruby using gem.

```bash
gem install google-api-client
```

--------------------------------

### Run Asset Reference Upload Example

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example?hl=he

Execute the asset reference upload example from the command line. Ensure you have the necessary reference file, asset title, and owner information. Use the --help flag for a full list of options.

```bash
python asset_reference_upload_example.py --reference_file=REFERENCE_FILE     --asset_title=ASSET_TITLE --owner=OWNER
```

```bash
python asset_reference_upload_example.py --help
```

--------------------------------

### Run PHP Built-in Web Server

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=fa

Start the PHP built-in web server to run the OAuth 2.0 example. This command serves files from the specified directory on localhost:8080.

```bash
php -S localhost:8080 ~/php-oauth2-example
```

--------------------------------

### Initiate Resumable Upload Example

Source: https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol

A concrete example of a POST request to initiate a session, including the video resource body.

```http
POST /upload/youtube/v3/videos?uploadType=resumable&part=snippet,status,contentDetails HTTP/1.1
Host: www.googleapis.com
Authorization: Bearer AUTH_TOKEN
Content-Length: 278
Content-Type: application/json; charset=UTF-8
X-Upload-Content-Length: 3000000
X-Upload-Content-Type: video/*

{
  "snippet": {
    "title": "My video title",
    "description": "This is a description of my video",
    "tags": ["cool", "video", "more keywords"],
    "categoryId": 22
  },
  "status": {
    "privacyStatus": "public",
    "embeddable": True,
    "license": "youtube"
  }
}
```

--------------------------------

### Install PHP Client Library

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Use Composer to install the Google APIs Client Library for PHP.

```bash
php composer.phar require google/apiclient:^2.0
```

--------------------------------

### Create Podfile and Install Dependencies

Source: https://developers.google.com/youtube/v3/quickstart/ios

Use this command in the Terminal to create a Podfile with the Google API Client for YouTube and Google Sign-In libraries, then install them and open the Xcode workspace.

```bash
cat << EOF > Podfile &&
platform :ios, '8.0'
target 'QuickstartApp' do
    pod 'GoogleAPIClientForREST/YouTube', '~> 1.2.1'
    pod 'Google/SignIn', '~> 3.0.3'
end
EOF
pod install &&
open QuickstartApp.xcworkspace

```

--------------------------------

### PHP YouTube Reporting API Setup

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list

Sets up the Google API client library for PHP, including composer installation instructions and autoloading. Requires the google/apiclient library.

```PHP
if (!file_exists(__DIR__ . '/vendor/autoload.php')) {
  throw new \Exception('please run "composer require google/apiclient:~2.2.0" in "' . __DIR__ . '"');
}

require_once __DIR__ . '/vendor/autoload.php';
session_start();


define('CREDENTIALS_PATH', '~/.credentials/youtube-php.json');

```

--------------------------------

### Run YouTube Partner API Asset Reference Upload Example

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example?hl=bn

This command-line script uploads asset references to the YouTube Partner API. Ensure you have a 'client_secrets.json' file configured for OAuth 2.0 authentication. You can get help by running the script with the --help flag.

```python
Usage:
  $ python asset_reference_upload_example.py --reference_file=REFERENCE_FILE \
      --asset_title=ASSET_TITLE --owner=OWNER

You can also get help on all the command-line flags the program understands  
by running:

  $ python asset_reference_upload_example.py --help  
```

--------------------------------

### Command Line Usage Examples

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=es-419

Example command line arguments for executing the reporting job script.

```bash
python create_reporting_job.py --name='<name>'
python create_reporting_job.py --content-owner='<CONTENT OWNER ID>'
python create_reporting_job.py --content-owner='<CONTENT_OWNER_ID>' --report-type='<REPORT_TYPE_ID>' --name='<REPORT_NAME>'
```

--------------------------------

### Install Google API Client Libraries

Source: https://developers.google.com/youtube/analytics/reference/reports/query

Install the required Python packages for the Google APIs Client Library and authentication.

```bash
pip install --upgrade google-api-python-client
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```

--------------------------------

### Install Ruby API Dependencies

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps

Commands to install the Google Auth library and Sinatra framework for Ruby.

```bash
gem install googleauth
```

```bash
gem install sinatra
```

--------------------------------

### Install YouTube Data API client libraries

Source: https://developers.google.com/youtube/v3/quickstart/nodejs

Use npm to install the required Google APIs and authentication libraries for the Node.js project.

```bash
npm install googleapis --save
npm install google-auth-library --save
```

--------------------------------

### Install Ruby Dependencies

Source: https://developers.google.com/youtube/reporting/guides/authorization/server-side-web-apps

Commands to install the Google Auth library, specific API client gems, and the Sinatra framework.

```bash
gem install googleauth
```

```bash
gem install google-apis-drive_v3 google-apis-calendar_v3
```

```bash
gem install sinatra
```

--------------------------------

### YouTube IFrame Player API - Examples

Source: https://developers.google.com/youtube/iframe_api_reference?hl=ko

Examples demonstrating how to use the YouTube IFrame Player API.

```APIDOC
## YouTube IFrame Player API - Examples

### Description
This section provides examples of how to use the YouTube IFrame Player API, including integrating with existing `<iframe>` elements.

### Using an Existing `<iframe>` Element

- **Example**: Demonstrates how to use the API with an existing `<iframe>` element. (Specific code not provided in source text, but the capability is mentioned).

```

--------------------------------

### Install Google API Client Library for Ruby

Source: https://developers.google.com/youtube/v3/quickstart/ruby

Installs the necessary Google API client library for Ruby. Use this command in your terminal.

```bash
gem install google-api-client

```

--------------------------------

### Initialize Node.js Project

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps?hl=fa

Commands to create a project directory and install the Google API client library.

```bash
mkdir ~/nodejs-oauth2-example
cd ~/nodejs-oauth2-example
```

```bash
npm install googleapis
```

--------------------------------

### iframe Player Integration Example

Source: https://developers.google.com/youtube/js_api_reference?hl=pt-br

An updated example demonstrating how to use the YouTube API with an existing `<iframe>` element.

```APIDOC
## iframe Player Integration Example

### Description
This update adds an example to the Examples section that demonstrates how to integrate the YouTube API with an existing `<iframe>` element on a webpage.

### Example Usage

Refer to the updated Examples section for a demonstration of using the API with an existing `<iframe>`.
```

--------------------------------

### Install Google API Client Library for PHP

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=fa

Use Composer to install the Google API Client Library for PHP. Ensure you are in the project directory before running this command.

```bash
composer require google/apiclient:"^2.15.0"
```

--------------------------------

### Example Updates

Source: https://developers.google.com/youtube/js_api_reference?hl=de

Updates to the Examples section of the documentation.

```APIDOC
## Example Updates

### Using API with Existing `<iframe>`
An example has been added to demonstrate how to use the API with an existing `<iframe>` element.

### Loading a Video Player
The example for manually creating the `<iframe>` tag has been updated to include a closing `</iframe>` tag. This is necessary because the `onYouTubeIframeAPIReady` function is only called if the closing `</iframe>` element is present.
```

--------------------------------

### GET /reports - Top 10 Most Started Playlists in US

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=fa

Retrieves the 10 playlists started most frequently by viewers in the United States.

```APIDOC
## GET /reports

### Description
Retrieves the 10 playlists from the content owner's channels that viewers in the United States started watching most frequently.

### Parameters
#### Query Parameters
- **dimensions** (string) - Required - playlist
- **metrics** (string) - Required - playlistStarts,playlistViews,playlistEstimatedMinutesWatched,playlistAverageViewDuration
- **filters** (string) - Required - country==US
- **maxResults** (integer) - Required - 10
- **sort** (string) - Required - -playlistStarts
```

--------------------------------

### Get video start bytes

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

Deprecated method that returns the number of bytes the video file started loading from; currently always returns 0.

```JavaScript
player. getVideoStartBytes ():Number
```

--------------------------------

### HTTP GET Request to YouTube Channels

Source: https://developers.google.com/youtube/v3/guides/auth/installed-apps

Use this example for making a GET request to the youtube.channels endpoint. Ensure you include your access token in the Authorization header.

```http
GET /youtube/v3/channels?part=snippet&mine=true HTTP/1.1
Host: www.googleapis.com
**Authorization: Bearer access_token**
```

--------------------------------

### YouTube Data API v3 Python Example

Source: https://developers.google.com/youtube/v3/code_samples/python_appengine

This snippet shows a complete Python application for searching Freebase topics and then retrieving YouTube videos for a selected topic. It requires API key setup and enabling specific Google APIs.

```python
API_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
FREEBASE_SEARCH_URL = "https://www.googleapis.com/freebase/v1/search?%s"
QUERY_TERM = "dog"

class MainHandler(webapp2.RequestHandler):

  def get(self):
    if API_KEY == 'REPLACE_ME':
      self.response.write(REGISTRATION_INSTRUCTIONS)
    else:
      # Present a list of Freebase topic IDs for the query term
      self.list_topics(QUERY_TERM)

  def list_topics(self, QUERY_TERM):
    # Retrieve a list of Freebase topics associated with the query term
    freebase_params = dict(query=QUERY_TERM, key=API_KEY)
    freebase_url = FREEBASE_SEARCH_URL % urllib.urlencode(freebase_params)
    freebase_response = json.loads(urllib.urlopen(freebase_url).read())

    if len(freebase_response["result"]) == 0:
      exit("No matching terms were found in Freebase.")

    # Create a page that shows a select box listing the topics.
    # When the user selects a topic and submits the form,
    # the 'post' method below will handle the form submission and
    # retrieve videos for the selected topic.
    select_topic_page = ('''
        <html>
          <body>
            <p>The following topics were found:</p>
            <form method="post">
              <select name="topic">
    ''')
    for result in freebase_response["result"]:
      select_topic_page += ('<option value="' + result["mid"] + '">' + result.get("name", "Unknown") + '</option>')

    select_topic_page += '''
              </select>
              <p><input type="submit" /></p>
            </form>
          </body>
        </html>
    '''

    # Display the HTML page listing the topic choices.
    self.response.out.write(select_topic_page)

  def post(self):
    topic_id = self.request.get('topic')

    # Service for calling the YouTube API
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=API_KEY)

    # Execute the search request using default query term and retrieved topic.
    search_response = youtube.search().list(
      part = 'id,snippet',
      type = 'video',
      topicId = topic_id
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
      videos.append(search_result)

    template_values = {
      'videos': videos
    }

    self.response.headers['Content-type'] = 'text/html'
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
], debug=True)

```

```python
import os
import urllib
import webapp2
import jinja2

from apiclient.discovery import build
from optparse import OptionParser

import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

REGISTRATION_INSTRUCTIONS = """
    You must set up a project and get an API key to run this code. Please see
    the instructions for creating a project and a key at <a
    href="https://developers.google.com/youtube/registering_an_application"
    >https://developers.google.com/youtube/registering_an_application</a>.
    <br><br>
    Make sure that you have enabled the YouTube Data API (v3) and the Freebase
    API for your project."""

# Set API_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API and Freebase API

```

--------------------------------

### Install Google Auth Library for Ruby

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Install the Google Auth Library for Ruby using gem. Requires Ruby 2.6 or greater.

```bash
gem install googleauth
```

--------------------------------

### Install Google API Client Libraries for Ruby

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Install the client libraries for Drive and Calendar Google APIs using gem. Requires Ruby 2.6 or greater.

```bash
gem install google-apis-drive_v3 google-apis-calendar_v3
```

--------------------------------

### Example: Subscribe to GoogleDevelopers Channel

Source: https://developers.google.com/youtube/v3/docs/subscriptions/insert?hl=ru

This example demonstrates how to subscribe the authenticated user to the GoogleDevelopers channel. Modify the `snippet.resourceId.channelId` to subscribe to a different channel.

```JSON
{
  "snippet": {
    "resourceId": {
      "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw"
    }
  }
}
```

--------------------------------

### HTTP GET Request with Access Token Query Parameter

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=fa

This example shows how to make a GET request to the same API endpoint using the access_token as a query string parameter. This is an alternative to using the Authorization header.

```http
GET https://www.googleapis.com/youtubepartner/v1/contentOwners?access_token=access_token&fetchMine=true
```

--------------------------------

### Iframe Player API Example

Source: https://developers.google.com/youtube/iframe_api_reference?hl=it

An example demonstrating how to use the YouTube API with an existing iframe element.

```APIDOC
## Iframe Player API Example

### Description
This example demonstrates how to integrate the YouTube API with an existing `<iframe>` element on a webpage.

### Usage

Refer to the updated Examples section for a demonstration of using the API with an existing `<iframe>` element.
```

--------------------------------

### Install Google Authentication Libraries for Python

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Install the required Python libraries for user authorization with Google APIs. These are necessary for handling authentication flows.

```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```

--------------------------------

### Get current playback time

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

Returns the elapsed time in seconds since the video started playing.

```JavaScript
player. getCurrentTime ():Number
```

--------------------------------

### Install Google APIs Client Library for Node.js

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Install the necessary Node.js package for interacting with Google APIs. This command should be run in your project directory.

```bash
npm install googleapis --save
```

--------------------------------

### GET /reports (Playlist Reports)

Source: https://developers.google.com/youtube/analytics/sample-requests

Retrieves playlist-specific metrics including views, watch time, and starts.

```APIDOC
## GET /reports

### Description
Retrieves country-specific playlist metrics or top started playlists in the U.S.

### Parameters
#### Query Parameters
- **dimensions** (string) - Required - country or playlist
- **metrics** (string) - Required - playlistViews,playlistEstimatedMinutesWatched,playlistStarts,averageTimeInPlaylist
- **filters** (string) - Optional - country==US
- **maxResults** (integer) - Optional - 10
- **sort** (string) - Required - -playlistEstimatedMinutesWatched or -playlistStarts
```

--------------------------------

### Install Google API Client Library for PHP

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Use Composer to install the Google APIs Client Library for PHP. Requires PHP 8.0 or greater.

```bash
composer require google/apiclient:^2.15.0
```

--------------------------------

### Upload Video Command-Line Arguments

Source: https://developers.google.com/youtube/v3/guides/uploading_a_video?hl=es

Example of how to execute the upload script with various video metadata arguments.

```bash
python upload_video.py --file="/tmp/test_video_file.flv" \
                       --title="Summer vacation in California" \
                       --description="Had fun surfing in Santa Cruz" \
                       --keywords="surfing,Santa Cruz" \
                       --category="22" \
                       --privacyStatus="private"
```

--------------------------------

### GET /jobs/{jobId}/reports

Source: https://developers.google.com/youtube/analytics/revision_history?hl=bn

Lists reports for a specific job, with new parameters to filter by the data start time.

```APIDOC
## GET /jobs/{jobId}/reports

### Description
Lists reports for a specific job. New parameters allow filtering reports based on the date range of the data contained within the report.

### Method
GET

### Endpoint
/jobs/{jobId}/reports

### Parameters
#### Path Parameters
- **jobId** (string) - Required - The ID of the job for which to list reports.

#### Query Parameters
- **startTimeAtOrAfter** (string) - Optional - The API response should only contain reports if the earliest data in the report is on or after the specified date.
- **startTimeBefore** (string) - Optional - The API response should only contain reports if the earliest data in the report is before the specified date.
```

--------------------------------

### iframe Player API Example

Source: https://developers.google.com/youtube/js_api_reference?hl=id

An example demonstrating how to use the YouTube iframe player API with an existing iframe element.

```APIDOC
## iframe Player API Example

### Description
This example demonstrates how to integrate the YouTube Player API with an existing `<iframe>` element on a webpage.

### Usage
Ensure the `onYouTubeIframeAPIReady` function is defined globally. This function is called automatically when the API is ready.

### HTML Structure
```html
<div id="player"></div>

<script>
  // Load the IFrame Player API code asynchronously.
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // Replace the 'my-video-id' with the actual video ID.
  var videoId = 'my-video-id';

  // This function creates an <iframe> (and YouTube player) after the API code downloads.
  function onYouTubeIframeAPIReady() {
    new YT.Player('player', {
      height: '390',
      width: '640',
      videoId: videoId,
      events: {
        'onReady': onPlayerReady
      }
    });
  }

  // The API will call this function when the video player is ready.
  function onPlayerReady(event) {
    event.target.playVideo();
  }
</script>
```
```

--------------------------------

### iframe Player API Ready Event Example

Source: https://developers.google.com/youtube/js_api_reference?hl=pt-br

An updated example demonstrating the correct structure for the `onYouTubeIframeAPIReady` function, including the necessary closing `</iframe>` tag.

```APIDOC
## iframe Player API Ready Event Example

### Description
This update modifies the example in the 'Loading a video player' section to include the closing `</iframe>` tag. This is necessary because the `onYouTubeIframeAPIReady` function is only called if the closing `</iframe>` element is present.

### Example Snippet

```html
<iframe id="player" type="text/html" width="640" height="390"
  src="//www.youtube.com/embed/VIDEO_ID?enablejsapi=1"
  frameborder="0"></iframe>

<script>
  function onYouTubeIframeAPIReady() {
    // Player initialization code here
  }
</script>
```

**Note**: Ensure the closing `</iframe>` tag is present for `onYouTubeIframeAPIReady` to be invoked.
```

--------------------------------

### YouTube Data API v3 Go Quickstart Implementation

Source: https://developers.google.com/youtube/v3/quickstart/go

A complete Go script to authenticate via OAuth 2.0 and fetch channel statistics for a specific username.

```go
// Sample Go code for user authorization

package main

import (
  "encoding/json"
  "fmt"
  "log"
  "io/ioutil"
  "net/http"
  "net/url"
  "os"
  "os/user"
  "path/filepath"

  "golang.org/x/net/context"
  "golang.org/x/oauth2"
  "golang.org/x/oauth2/google"
  "google.golang.org/api/youtube/v3"
)

const missingClientSecretsMessage = `
Please configure OAuth 2.0
`

// getClient uses a Context and Config to retrieve a Token
// then generate a Client. It returns the generated Client.
func getClient(ctx context.Context, config *oauth2.Config) *http.Client {
  cacheFile, err := tokenCacheFile()
  if err != nil {
    log.Fatalf("Unable to get path to cached credential file. %v", err)
  }
  tok, err := tokenFromFile(cacheFile)
  if err != nil {
    tok = getTokenFromWeb(config)
    saveToken(cacheFile, tok)
  }
  return config.Client(ctx, tok)
}

// getTokenFromWeb uses Config to request a Token.
// It returns the retrieved Token.
func getTokenFromWeb(config *oauth2.Config) *oauth2.Token {
  authURL := config.AuthCodeURL("state-token", oauth2.AccessTypeOffline)
  fmt.Printf("Go to the following link in your browser then type the "+
    "authorization code: \n%v\n", authURL)

  var code string
  if _, err := fmt.Scan(&code); err != nil {
    log.Fatalf("Unable to read authorization code %v", err)
  }

  tok, err := config.Exchange(oauth2.NoContext, code)
  if err != nil {
    log.Fatalf("Unable to retrieve token from web %v", err)
  }
  return tok
}

// tokenCacheFile generates credential file path/filename.
// It returns the generated credential path/filename.
func tokenCacheFile() (string, error) {
  usr, err := user.Current()
  if err != nil {
    return "", err
  }
  tokenCacheDir := filepath.Join(usr.HomeDir, ".credentials")
  os.MkdirAll(tokenCacheDir, 0700)
  return filepath.Join(tokenCacheDir,
    url.QueryEscape("youtube-go-quickstart.json")), err
}

// tokenFromFile retrieves a Token from a given file path.
// It returns the retrieved Token and any read error encountered.
func tokenFromFile(file string) (*oauth2.Token, error) {
  f, err := os.Open(file)
  if err != nil {
    return nil, err
  }
  t := &oauth2.Token{}
  err = json.NewDecoder(f).Decode(t)
  defer f.Close()
  return t, err
}

// saveToken uses a file path to create a file and store the
// token in it.
func saveToken(file string, token *oauth2.Token) {
  fmt.Printf("Saving credential file to: %s\n", file)
  f, err := os.OpenFile(file, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0600)
  if err != nil {
    log.Fatalf("Unable to cache oauth token: %v", err)
  }
  defer f.Close()
  json.NewEncoder(f).Encode(token)
}

func handleError(err error, message string) {
  if message == "" {
    message = "Error making API call"
  }
  if err != nil {
    log.Fatalf(message + ": %v", err.Error())
  }
}

func channelsListByUsername(service *youtube.Service, part string, forUsername string) {
  call := service.Channels.List(part)
  call = call.ForUsername(forUsername)
  response, err := call.Do()
  handleError(err, "")
  fmt.Println(fmt.Sprintf("This channel's ID is %s. Its title is '%s', " +
              "and it has %d views.",
              response.Items[0].Id,
              response.Items[0].Snippet.Title,
              response.Items[0].Statistics.ViewCount))
}


func main() {
  ctx := context.Background()

  b, err := ioutil.ReadFile("client_secret.json")
  if err != nil {
    log.Fatalf("Unable to read client secret file: %v", err)
  }

  // If modifying these scopes, delete your previously saved credentials
  // at ~/.credentials/youtube-go-quickstart.json
  config, err := google.ConfigFromJSON(b, youtube.YoutubeReadonlyScope)
  if err != nil {
    log.Fatalf("Unable to parse client secret file to config: %v", err)
  }
  client := getClient(ctx, config)
  service, err := youtube.New(client)

  handleError(err, "Error creating YouTube client")

  channelsListByUsername(service, "snippet,contentDetails,statistics", "GoogleDevelopers")
}
```

--------------------------------

### Configure Command-Line Arguments and Initialize Upload

Source: https://developers.google.com/youtube/v3/guides/uploading_a_video

Sets up command-line arguments for video metadata and initiates the authenticated upload process.

```python
if __name__ == '__main__':
  argparser.add_argument("--file", required=True, help="Video file to upload")
  argparser.add_argument("--title", help="Video title", default="Test Title")
  argparser.add_argument("--description", help="Video description",
    default="Test Description")
  argparser.add_argument("--category", default="22",
    help="Numeric video category. " +
      "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
  argparser.add_argument("--keywords", help="Video keywords, comma separated",
    default="")
  argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
    default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")
  args = argparser.parse_args()

  if not os.path.exists(args.file):
    exit("Please specify a valid file using the --file= parameter.")

  youtube = get_authenticated_service(args)
  try:
    initialize_upload(youtube, args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
```

--------------------------------

### Sub-selection syntax example

Source: https://developers.google.com/youtube/partner/guides/performance

Example of using parentheses to select specific sub-fields within an array.

```text
items(title,author/uri)
```

--------------------------------

### Install Google API Client Library for Python

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Install the Google API Python client library and authentication libraries using pip. Requires Python 3.7 or greater.

```bash
pip install --upgrade google-api-python-client
```

```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```

```bash
pip install --upgrade flask
```

```bash
pip install --upgrade requests
```

--------------------------------

### Initialize YouTube API Quickstart in Node.js

Source: https://developers.google.com/youtube/v3/quickstart/nodejs

This script handles OAuth 2.0 authentication, token storage, and channel data retrieval. Ensure 'client_secret.json' is present in the working directory before execution.

```javascript
var fs = require('fs');
var readline = require('readline');
var {google} = require('googleapis');
var OAuth2 = google.auth.OAuth2;

// If modifying these scopes, delete your previously saved credentials
// at ~/.credentials/youtube-nodejs-quickstart.json
var SCOPES = ['https://www.googleapis.com/auth/youtube.readonly'];
var TOKEN_DIR = (process.env.HOME || process.env.HOMEPATH ||
    process.env.USERPROFILE) + '/.credentials/';
var TOKEN_PATH = TOKEN_DIR + 'youtube-nodejs-quickstart.json';

// Load client secrets from a local file.
fs.readFile('client_secret.json', function processClientSecrets(err, content) {
  if (err) {
    console.log('Error loading client secret file: ' + err);
    return;
  }
  // Authorize a client with the loaded credentials, then call the YouTube API.
  authorize(JSON.parse(content), getChannel);
});

/**
 * Create an OAuth2 client with the given credentials, and then execute the
 * given callback function.
 *
 * @param {Object} credentials The authorization client credentials.
 * @param {function} callback The callback to call with the authorized client.
 */
function authorize(credentials, callback) {
  var clientSecret = credentials.installed.client_secret;
  var clientId = credentials.installed.client_id;
  var redirectUrl = credentials.installed.redirect_uris[0];
  var oauth2Client = new OAuth2(clientId, clientSecret, redirectUrl);

  // Check if we have previously stored a token.
  fs.readFile(TOKEN_PATH, function(err, token) {
    if (err) {
      getNewToken(oauth2Client, callback);
    } else {
      oauth2Client.credentials = JSON.parse(token);
      callback(oauth2Client);
    }
  });
}

/**
 * Get and store new token after prompting for user authorization, and then
 * execute the given callback with the authorized OAuth2 client.
 *
 * @param {google.auth.OAuth2} oauth2Client The OAuth2 client to get token for.
 * @param {getEventsCallback} callback The callback to call with the authorized
 *     client.
 */
function getNewToken(oauth2Client, callback) {
  var authUrl = oauth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: SCOPES
  });
  console.log('Authorize this app by visiting this url: ', authUrl);
  var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  rl.question('Enter the code from that page here: ', function(code) {
    rl.close();
    oauth2Client.getToken(code, function(err, token) {
      if (err) {
        console.log('Error while trying to retrieve access token', err);
        return;
      }
      oauth2Client.credentials = token;
      storeToken(token);
      callback(oauth2Client);
    });
  });
}

/**
 * Store token to disk be used in later program executions.
 *
 * @param {Object} token The token to store to disk.
 */
function storeToken(token) {
  try {
    fs.mkdirSync(TOKEN_DIR);
  } catch (err) {
    if (err.code != 'EEXIST') {
      throw err;
    }
  }
  fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
    if (err) throw err;
    console.log('Token stored to ' + TOKEN_PATH);
  });
}

/**
 * Lists the names and IDs of up to 10 files.
 *
 * @param {google.auth.OAuth2} auth An authorized OAuth2 client.
 */
function getChannel(auth) {
  var service = google.youtube('v3');
  service.channels.list({
    auth: auth,
    part: 'snippet,contentDetails,statistics',
    forUsername: 'GoogleDevelopers'
  }, function(err, response) {
    if (err) {
      console.log('The API returned an error: ' + err);
      return;
    }
    var channels = response.data.items;
    if (channels.length == 0) {
      console.log('No channel found.');
    } else {
      console.log('This channel\'s ID is %s. Its title is \'%s\', and ' +
                  'it has %s views.',
                  channels[0].id,
                  channels[0].snippet.title,
                  channels[0].statistics.viewCount);
    }
  });
}
```

--------------------------------

### GET /reports - Playlist Traffic Source Metrics

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=ru

Retrieves playlist views, starts, and estimated watch time aggregated by traffic source.

```APIDOC
## GET /reports

### Description
Retrieves playlist views, playlist starts, and playlist estimated watch time for playlists in one or more of a content owner's channels, aggregated by traffic source.

### Parameters
#### Query Parameters
- **dimensions** (string) - Required - "day,insightTrafficSourceType"
- **metrics** (string) - Required - "playlistViews,playlistStarts,playlistEstimatedMinutesWatched"
- **filters** (string) - Required - "channel==CHANNEL_ID" (Replace CHANNEL_ID with comma-separated list of up to 500 channel IDs)
```

--------------------------------

### Python Reporting Job Setup

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/reportTypes/list?hl=pt-br

Initial setup for a Python script to create reporting jobs using the YouTube Reporting API.

```python
#!/usr/bin/python

# Create a reporting job for the authenticated user's channel or
# for a content owner that the user's account is linked to.
# Usage example:
# python create_reporting_job.py --name='<name>'
# python create_reporting_job.py --content-owner='<CONTENT OWNER ID>'
# python create_reporting_job.py --content-owner='<CONTENT_OWNER_ID>' --report-type='<REPORT_TYPE_ID>' --name='<REPORT_NAME>'

import argparse
import os

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
```

--------------------------------

### Start HTTP Server

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps?hl=ko

Create and start an HTTP server using the configured Express application. The server listens on port 8080.

```javascript
const server = http.createServer(app);
server.listen(8080);
```

--------------------------------

### GET /reports (Channel Analytics)

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=pt-br

Examples of retrieving various channel-level reports including aggregated metrics, country-specific data, and top-performing videos.

```APIDOC
## GET /reports

### Description
Retrieves analytics reports for a YouTube channel or content owner based on specified dimensions and metrics.

### Method
GET

### Parameters
#### Query Parameters
- **ids** (string) - Required - The ID of the channel (channel==MINE) or content owner (contentOwner==CONTENT_OWNER_ID).
- **startDate** (string) - Required - Start date in YYYY-MM-DD format.
- **endDate** (string) - Required - End date in YYYY-MM-DD format.
- **metrics** (string) - Required - Comma-separated list of metrics (e.g., views, comments, likes).
- **dimensions** (string) - Optional - Comma-separated list of dimensions (e.g., day, video, insightTrafficSourceType).
- **filters** (string) - Optional - Filters for the report (e.g., country==US).
- **sort** (string) - Optional - Sort order for results (e.g., -views, day).
- **maxResults** (integer) - Optional - Maximum number of rows to return.

### Request Example
GET /reports?ids=channel==MINE&startDate=2023-09-01&endDate=2024-03-31&metrics=estimatedMinutesWatched,views,likes,subscribersGained&dimensions=video&maxResults=10&sort=-estimatedMinutesWatched
```

--------------------------------

### Install GRPC Tools for Python

Source: https://developers.google.com/youtube/v3/live/streaming-live-chat

Installs the necessary GRPC libraries for Python development. These are required for generating client libraries from .proto files.

```bash
pip install grpcio
pip install grpcio-tools

```

--------------------------------

### Execute Go Sample

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Run the Go script from the command line.

```bash
go run sample.go
```

--------------------------------

### Create Reporting Job Example

Source: https://developers.google.com/youtube/reporting/v1/code_samples/python?hl=pl

Example usage for creating a reporting job. This involves listing available report types and then creating a new job.

```python
# Create a reporting job for the authenticated user's channel or
# for a content owner that the user's account is linked to.
# Usage example:
# python create_reporting_job.py --name='<name>'
# python create_reporting_job.py --content-owner='<CONTENT OWNER ID>'
```

--------------------------------

### List Content Owners via HTTP GET

Source: https://developers.google.com/youtube/partner/guides/auth/devices

Examples of calling the contentOwners.list endpoint using either an Authorization header or a query string parameter.

```HTTP
GET /youtubepartner/v1/contentOwners?fetchMine=true HTTP/1.1
Host: www.googleapis.com
**Authorization: Bearer access_token**
```

```HTTP
GET https://www.googleapis.com/youtubepartner/v1/contentOwners?access_token=access_token&fetchMine=true
```

--------------------------------

### Main Execution Block

Source: https://developers.google.com/youtube/partner/code_samples/python?hl=ja

Sets up logging, parses command-line arguments, authenticates services, and orchestrates the video upload, asset creation, claiming, and advertising setup process. Includes error handling for missing parameters.

```python
if __name__ == '__main__':
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )

  args = parse_args()

  if args.file is None or not os.path.exists(args.file):
    logging.error("Please specify a valid file using the --file= parameter.")
    exit(1)

  # The channel ID value has a format like "UC..." and must identify a channel
  # managed by the YouTube content owner associated with the authenticated user.
  # You can use the YouTube Data API's youtube.channels.list method to
  # retrieve a list of managed channels and their IDs. (To do so, set the
  # "part" parameter value to "snippet", the "managedByMe" parameter value to
  # "true" and the "onBehalfOfContentOwner" parameter to the content owner ID.
  # The "get_content_owner_id" method in this code sample shows how
  # to retrieve the content owner ID.
  if args.channelId is None:
    logging.error("Please specify a channel ID via the --channelId= parameter.")
    exit(1)

  (youtube, youtube_partner) = get_authenticated_services(args)

  content_owner_id = get_content_owner_id(youtube_partner)
  logging.info("Authenticated as content owner ID '%s'." % content_owner_id)

  (video_id, duration_seconds) = upload(youtube, content_owner_id, args)
  logging.info("Successfully uploaded video ID '%s'." % video_id)

  file_size_bytes = os.path.getsize(args.file)
  logging.debug("Uploaded %d bytes in %0.2f seconds (%0.2f megabytes/second)." %
    (file_size_bytes, duration_seconds,
      (file_size_bytes / (1024 * 1024)) / duration_seconds))

  asset_id = create_asset(youtube_partner, content_owner_id,
    args.title, args.description)
  logging.info("Created new asset ID '%s'." % asset_id)

  set_asset_ownership(youtube_partner, content_owner_id, asset_id)
  logging.info("Successfully set asset ownership.")

  claim_id = claim_video(youtube_partner, content_owner_id, asset_id,
    video_id, args.policyId)
  logging.info("Created new claim ID '%s'." % claim_id)

  set_advertising_options(youtube_partner, content_owner_id, video_id)
  logging.info("Successfully set advertising options.")

  logging.info("All done!")

```

--------------------------------

### Main Execution Block

Source: https://developers.google.com/youtube/partner/code_samples/python?hl=it

Sets up logging, parses command-line arguments, authenticates services, and orchestrates the video upload, asset creation, claiming, and advertising setup process. Exits with an error if the file or channel ID is not provided.

```python
if __name__ == '__main__':
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
  )

  args = parse_args()

  if args.file is None or not os.path.exists(args.file):
    logging.error("Please specify a valid file using the --file= parameter.")
    exit(1)

  # The channel ID value has a format like "UC..." and must identify a channel
  # managed by the YouTube content owner associated with the authenticated user.
  # You can use the YouTube Data API's youtube.channels.list method to
  # retrieve a list of managed channels and their IDs. (To do so, set the
  # "part" parameter value to "snippet", the "managedByMe" parameter value to
  # "true" and the "onBehalfOfContentOwner" parameter to the content owner ID.
  # The "get_content_owner_id" method in this code sample shows how
  # to retrieve the content owner ID.
  if args.channelId is None:
    logging.error("Please specify a channel ID via the --channelId= parameter.")
    exit(1)

  (youtube, youtube_partner) = get_authenticated_services(args)

  content_owner_id = get_content_owner_id(youtube_partner)
  logging.info("Authenticated as content owner ID '%s'." % content_owner_id)

  (video_id, duration_seconds) = upload(youtube, content_owner_id, args)
  logging.info("Successfully uploaded video ID '%s'." % video_id)

  file_size_bytes = os.path.getsize(args.file)
  logging.debug("Uploaded %d bytes in %0.2f seconds (%0.2f megabytes/second)." %
    (file_size_bytes, duration_seconds,
      (file_size_bytes / (1024 * 1024)) / duration_seconds))

  asset_id = create_asset(youtube_partner, content_owner_id,
      args.title, args.description)
  logging.info("Created new asset ID '%s'." % asset_id)

  set_asset_ownership(youtube_partner, content_owner_id, asset_id)
  logging.info("Successfully set asset ownership.")

  claim_id = claim_video(youtube_partner, content_owner_id, asset_id,
      video_id, args.policyId)
  logging.info("Created new claim ID '%s'." % claim_id)

  set_advertising_options(youtube_partner, content_owner_id, video_id)
  logging.info("Successfully set advertising options.")

  logging.info("All done!")
```

--------------------------------

### Example Authorization Redirect URL

Source: https://developers.google.com/youtube/v3/quickstart/ruby

An example of the URL format that might be returned after a user grants authorization, containing an authorization code.

```http
http://localhost/?code=**4/nr_1TspmmQPFyifh7nz...OFo#**
```

--------------------------------

### YouTube Analytics API Examples

Source: https://developers.google.com/youtube/analytics/revision_history?hl=bn

Demonstrates how to call the YouTube Analytics API using various client libraries. These examples are useful for understanding API integration.

```java
// Java client library example (content not provided in source)
```

```javascript
// JavaScript client library example (content not provided in source)
```

```python
# Python client library example (content not provided in source)
```

```ruby
# Ruby client library example (content not provided in source)
```

--------------------------------

### Initialize Google Client and Authenticate

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=fr

Sets up the Google API client, handles OAuth 2.0 authentication, and stores/refreshes credentials. Ensure you have a 'client_secrets_php.json' file and have enabled the YouTube Data API.

```php
require_once __DIR__ . '/vendor/autoload.php';
session_start();


define('CREDENTIALS_PATH', '~/.credentials/youtube-php.json');

$longOptions = array(
  'contentOwner::',
  'downloadUrl::',
  'includeSystemManaged::',
  'jobId::',
  'outputFile::',
);

$options = getopt('', $longOptions);

$CONTENT_OWNER_ID = ($options['contentOwner'] ? $options['contentOwner'] : '');
$DOWNLOAD_URL = (array_key_exists('downloadUrl', $options) ?
                 $options['downloadUrl'] : '');
$INCLUDE_SYSTEM_MANAGED = (array_key_exists('includeSystemManaged', $options) ?
                           $options['includeSystemManaged'] : '');
$JOB_ID = (array_key_exists('jobId', $options) ? $options['jobId'] : '');
$OUTPUT_FILE = (array_key_exists('outputFile', $options) ?
                $options['outputFile'] : '');

/*
 * You can obtain an OAuth 2.0 client ID and client secret from the
 * {{ Google Cloud Console }} <{{ https://cloud.google.com/console }}>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope(
      'https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);

    //fclose($fp);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}
```

--------------------------------

### Initialize YouTube API Client

Source: https://developers.google.com/youtube/v3/guides/searching_by_topic

Sets up the Google API client and discovers the YouTube API service. Ensure the YouTube Data API is enabled for your project and replace 'REPLACE_ME' with your actual developer key.

```ruby
DEVELOPER_KEY = 'REPLACE_ME'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_service
  client = Google::APIClient.new(
    :key => DEVELOPER_KEY,
    :authorization => nil,
    :application_name => $PROGRAM_NAME,
    :application_version => '1.0.0'
  )
  youtube = client.discovered_api(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION)

  return client, youtube
end
```

--------------------------------

### Get Daily Playlist Traffic Sources

Source: https://developers.google.com/youtube/analytics/sample-requests

Retrieves daily playlist view counts, starts, and watch time aggregated by traffic source. Metrics are sorted chronologically by day.

```text
dimensions=day,insightTrafficSourceType
metrics=views,estimatedMinutesWatched,playlistStarts,playlistViews
sort=day
```

--------------------------------

### HTTP GET Request with Authorization Header

Source: https://developers.google.com/youtube/reporting/guides/authorization/client-side-web-apps

Example of calling the YouTube Analytics API's reports.query endpoint using the Authorization: Bearer header. Replace 'access_token' with your actual token.

```HTTP
GET /youtube/analytics/v1/reports?ids=channel%3D%3DMINE&start-date=2016-05-01&end-date=2016-06-30&metrics=views HTTP/1.1
Host: www.googleapis.com
Authorization: Bearer access_token
```

--------------------------------

### Install Google APIs Node.js Client

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Install the Google APIs Node.js Client and related packages using npm. Requires a supported Node.js release.

```bash
npm install googleapis crypto express express-session
```

--------------------------------

### Authentication and Client Setup

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs.reports/list?hl=bn

This section details the process of setting up the Google API client, handling OAuth 2.0 authentication, and managing credentials.

```APIDOC
## Authentication and Client Setup

### Description
This function sets up the Google API client, handles OAuth 2.0 authentication, and loads or obtains credentials.

### Method
N/A (Function definition)

### Endpoint
N/A

### Parameters
None

### Request Example
N/A

### Response
- **Google_Client** (object) - An authenticated Google API client object.

### Response Example
N/A
```

--------------------------------

### Get Playlist Traffic Sources by Country

Source: https://developers.google.com/youtube/analytics/sample-requests

Retrieves playlist views, starts, and watch time aggregated by traffic source for a specific country. The `filters` parameter specifies the country code.

```text
dimensions=insightTrafficSourceType
metrics=views,estimatedMinutesWatchedplaylistStarts,playlistViews
filters=country==US
```

--------------------------------

### Install Google Auth Libraries for Python

Source: https://developers.google.com/youtube/v3/quickstart/python

Install the google-auth-oauthlib and google-auth-httplib2 libraries using pip. These are necessary for handling user authorization with OAuth 2.0.

```bash
pip install --upgrade google-auth-oauthlib google-auth-httplib2
```

--------------------------------

### Install YouTube Player Helper via CocoaPods

Source: https://developers.google.com/youtube/v3/guides/ios_youtube_helper

Add this line to your Podfile to install the library using CocoaPods. Replace x.y.z with the latest pod version.

```ruby
pod "youtube-ios-player-helper", "~> x.y.z"
```

--------------------------------

### OAuth 2.0 Web Server Flow (Python/Flask)

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=fa

Python Flask example for the OAuth 2.0 web server flow using the Requests library. It handles user authorization, token exchange, and API calls. Ensure you have Flask and Requests installed.

```python
import json
import flask
import requests

app = flask.Flask(__name__)

# To get these credentials (CLIENT_ID CLIENT_SECRET) and for your application, visit
# https://console.cloud.google.com/apis/credentials.
CLIENT_ID = '123456789.apps.googleusercontent.com'
CLIENT_SECRET = 'abc123'  # Read from a file or environmental variable in a real app

# Access scopes for two non-Sign-In scopes: Read-only Drive activity and Google Calendar.
SCOPE = 'https://www.googleapis.com/auth/youtubepartner https://www.googleapis.com/auth/calendar.readonly'

# Indicate where the API server will redirect the user after the user completes
# the authorization flow. The redirect URI is required. The value must exactly
# match one of the authorized redirect URIs for the OAuth 2.0 client, which you
# configured in the API Console. If this value doesn't match an authorized URI,
# you will get a 'redirect_uri_mismatch' error.
REDIRECT_URI = 'http://example.com/oauth2callback'

@app.route('/')
def index():
  if 'credentials' not in flask.session:
    return flask.redirect(flask.url_for('oauth2callback'))

  credentials = json.loads(flask.session['credentials'])

  if credentials['expires_in'] <= 0:
    return flask.redirect(flask.url_for('oauth2callback'))
  else: 
    # User authorized the request. Now, check which scopes were granted.
    if 'https://www.googleapis.com/auth/drive.metadata.readonly' in credentials['scope']:
      # User authorized read-only Drive activity permission.
      # Example of using Google Drive API to list filenames in user's Drive.
      headers = {'Authorization': 'Bearer {}'.format(credentials['access_token'])}
      req_uri = 'https://youtube.googleapis.com/youtubePartner/v1/contentOwners'
      r = requests.get(req_uri, headers=headers).text
    else:
      # User didn't authorize read-only Drive activity permission.
      # Update UX and application accordingly
      r = 'User did not authorize Drive permission.'

    # Check if user authorized Calendar read permission.
    if 'https://www.googleapis.com/auth/calendar.readonly' in credentials['scope']:
      # User authorized Calendar read permission.
      # Calling the APIs, etc.
      r += 'User authorized Calendar permission.'
    else:
      # User didn't authorize Calendar read permission.
      # Update UX and application accordingly
      r += 'User did not authorize Calendar permission.'

  return r

@app.route('/oauth2callback')
def oauth2callback():
  if 'code' not in flask.request.args:
    state = str(uuid.uuid4())
    flask.session['state'] = state
    # Generate a url that asks permissions for the Drive activity
    # and Google Calendar scope. Then, redirect user to the url.
    auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
                '&client_id={}&redirect_uri={}&scope={}&state={}').format(CLIENT_ID, REDIRECT_URI,
                                                                          SCOPE, state)
    return flask.redirect(auth_uri)
  else:
    if 'state' not in flask.request.args or flask.request.args['state'] != flask.session['state']:
      return 'State mismatch. Possible CSRF attack.', 400

    auth_code = flask.request.args.get('code')
    data = {'code': auth_code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code'}

    # Exchange authorization code for access and refresh tokens (if access_type is offline)
    r = requests.post('https://oauth2.googleapis.com/token', data=data)
    flask.session['credentials'] = r.text
    return flask.redirect(flask.url_for('index'))

if __name__ == '__main__':
  import uuid
  app.secret_key = str(uuid.uuid4())
  app.debug = False
  app.run()
```

--------------------------------

### HTTP/REST Request for Incremental Authorization

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=it

This example demonstrates an HTTP GET request to the Google OAuth 2.0 authorization endpoint, including the `include_granted_scopes=true` parameter. This allows the application to request access to YouTube Analytics data, combining it with any previously granted scopes.

```http
GET https://accounts.google.com/o/oauth2/v2/auth?
  scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyt-analytics.readonly&
  access_type=offline&
  response_type=code&
  state=security_token%3D138rk%3Btarget_url%3Dhttp...index&
  redirect_uri=http%3A%2F%2Flocalhost%2Foauth2callback&
  client_id=client_id&
  **include_granted_scopes=true**
```

--------------------------------

### Subscription Resource Example

Source: https://developers.google.com/youtube/v3/docs/subscriptions/insert

A subscription resource must include the `snippet.resourceId` property to identify the channel being subscribed to. This example shows the basic structure.

```JSON
{
  "snippet": {
    "resourceId": {
      "channelId": "CHANNEL_ID"
    }
  }
}
```

--------------------------------

### Configure Logging and Parse Command-Line Options

Source: https://developers.google.com/youtube/partner/guides/upload?hl=tr

Sets up basic logging for the script and parses command-line arguments, including file path, channel ID, video title, description, and policy ID. Exits with an error if essential parameters are missing.

```python
if __name__ == '__main__':
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )

  options = parse_options()

  if options.file is None or not os.path.exists(options.file):
    logging.error("Please specify a valid file using the --file= parameter.")
    exit(1)

  # The channel ID looks something like "UC..." and needs to correspond to a
  # channel managed by the YouTube content owner authorizing the request.
  # youtube.channels.list(part="snippet", managedByMe=true,
  #                       onBehalfOfContentOwner=*CONTENT_OWNER_ID*)
  # can be used to retrieve a list of managed channels and their channel IDs.
  # See https://developers.google.com/youtube/v3/docs/channels/list
  if options.channelId is None:
    logging.error("Please specify a channel ID via the --channelId= parameter.")
    exit(1)

  (youtube, youtube_partner) = get_authenticated_services()

  content_owner_id = get_content_owner_id(youtube_partner)
  logging.info("Authorized by content owner ID '%s'." % content_owner_id)
```

--------------------------------

### Get YouTube Reporting Service Client

Source: https://developers.google.com/youtube/reporting/v1/code_samples/php

Initializes and returns a Google_Client object configured for the YouTube Reporting API. Handles authentication by loading existing credentials or guiding the user through the OAuth 2.0 flow. Ensure the YouTube Data API is enabled for your project.

```php
<?php

/**
 * This sample supports the following use cases:
 *
 * 1. Retrieve reporting jobs by content owner:
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID"
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID" --includeSystemManaged==True
 * 2. Retrieving list of downloadable reports for a particular job:
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID" --jobId="JOB_ID"
 * 3. Download a report:
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID" --downloadUrl="DOWNLOAD_URL" --outputFile="report.txt"
 */

/**
 * Library Requirements
 *
 * 1. Install composer (https://getcomposer.org)
 * 2. On the command line, change to this directory (api-samples/php)
 * 3. Require the google/apiclient library
 *    $ composer require google/apiclient:~2.0
 */
if (!file_exists(__DIR__ . '/vendor/autoload.php')) {
  throw new \Exception('please run "composer require google/apiclient:~2.2.0" in "' . __DIR__ .'"');
}

require_once __DIR__ . '/vendor/autoload.php';
session_start();


define('CREDENTIALS_PATH', '~/.credentials/youtube-php.json');

$longOptions = array(
  'contentOwner::',
  'downloadUrl::',
  'includeSystemManaged::',
  'jobId::',
  'outputFile::',
);

$options = getopt('', $longOptions);

$CONTENT_OWNER_ID = ($options['contentOwner'] ? $options['contentOwner'] : '');
$DOWNLOAD_URL = (array_key_exists('downloadUrl', $options) ?
                 $options['downloadUrl'] : '');
$INCLUDE_SYSTEM_MANAGED = (array_key_exists('includeSystemManaged', $options) ?
                           $options['includeSystemManaged'] : '');
$JOB_ID = (array_key_exists('jobId', $options) ? $options['jobId'] : '');
$OUTPUT_FILE = (array_key_exists('outputFile', $options) ?
                $options['outputFile'] : '');

/*
 * You can obtain an OAuth 2.0 client ID and client secret from the
 * {{ Google Cloud Console }} <{{ https://cloud.google.com/console }}>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope(
      'https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);

    //fclose($fp);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}

/**
 * Expands the home directory alias '~' to the full path.
 * @param string $path the path to expand.
 * @return string the expanded path.
 */
function expandHomeDirectory($path) {
  $homeDirectory = getenv('HOME');
  if (empty($homeDirectory)) {
    $homeDirectory = getenv('HOMEDRIVE') . getenv('HOMEPATH');
  }
  return str_replace('~', realpath($homeDirectory), $path);
}

/**
 * Returns a list of reporting jobs. (jobs.listJobs)
 *
 * @param Google_Service_YouTubereporting $youtubeReporting YouTube Reporting service object.
 * @param string $onBehalfOfContentOwner A content owner ID.
 */
function listReportingJobs(Google_Service_YouTubeReporting $youtubeReporting,
    $onBehalfOfContentOwner = '', $includeSystemManaged = False) {
  $reportingJobs = $youtubeReporting->jobs->listJobs(
      array('onBehalfOfContentOwner' => $onBehalfOfContentOwner,
            'includeSystemManaged' => $includeSystemManaged));

```

--------------------------------

### Install Flask for Python Web Applications

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Install the Flask web application framework using pip. This is required if you are running Python samples that function as web servers.

```bash
pip install --upgrade flask
```

--------------------------------

### Initialize Gradle Project Structure

Source: https://developers.google.com/youtube/v3/quickstart/java?hl=pt-br

Commands to create the basic directory structure for a Java project.

```bash
$ gradle init --type basic
$ mkdir -p src/main/java src/main/resources
```

--------------------------------

### Handle OAuth2 Callback and Get Tokens

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps?hl=ko

Process the callback from Google's OAuth 2.0 server. This route exchanges the authorization code for access and refresh tokens, verifies the state parameter, and sets the credentials for subsequent API calls. It also includes an example of listing YouTube channels.

```javascript
app.get('/oauth2callback', async (req, res) => {
  // Handle the OAuth 2.0 server response
  let q = url.parse(req.url, true).query;

  if (q.error) { // An error response e.g. error=access_denied
    console.log('Error:' + q.error);
  } else if (q.state !== req.session.state) { //check state value
    console.log('State mismatch. Possible CSRF attack');
    res.end('State mismatch. Possible CSRF attack');
  } else { // Get access and refresh tokens (if access_type is offline)
    let { tokens } = await oauth2Client.getToken(q.code);
    oauth2Client.setCredentials(tokens);

    /** Save credential to the global variable in case access token was refreshed.
      * ACTION ITEM: In a production app, you likely want to save the refresh token
      *              in a secure persistent database instead. */
    userCredential = tokens;
    
    // Example of using YouTube API to list channels.
    var service = google.youtube('v3');
    service.channels.list({
      auth: oauth2Client,
      part: 'snippet,contentDetails,statistics',
      forUsername: 'GoogleDevelopers'
    }, function (err, response) {
      if (err) {
        console.log('The API returned an error: ' + err);
        return;
      }
      var channels = response.data.items;
      if (channels.length == 0) {
        console.log('No channel found.');
      } else {
        console.log('This channel\'s ID is %s. Its title is \'%s\', and ' + 
          'it has %s views.',
          channels[0].id,
          channels[0].snippet.title,
          channels[0].statistics.viewCount);
      }
    });
  }
});
```

--------------------------------

### Install or Update Google APIs Client Library

Source: https://developers.google.com/youtube/v3/quickstart/php

Use Composer to install or update the Google APIs Client Library for PHP in your project.

```bash
composer require google/apiclient:^2.0
```

```bash
composer update google/apiclient --with-dependencies
```

--------------------------------

### GET /v2/reports

Source: https://developers.google.com/youtube/analytics/v1/reference/reports/query

This method lets you retrieve many different Analytics reports. Each request uses query parameters to specify a channel ID or content owner, a start date, an end date, and at least one metric. You can also provide additional query parameters, such as dimensions, filters, and sorting instructions.

```APIDOC
## GET /v2/reports

### Description
Retrieves various YouTube Analytics reports based on specified parameters like channel ID, dates, metrics, dimensions, and filters.

### Method
GET

### Endpoint
https://youtubeanalytics.googleapis.com/v2/reports

### Parameters
#### Query Parameters
- **ids** (string) - Required - The ID of the channel or content owner for which to retrieve analytics data.
- **start-date** (string) - Required - The start date for the report in YYYY-MM-DD format.
- **end-date** (string) - Required - The end date for the report in YYYY-MM-DD format.
- **metrics** (string) - Required - A comma-separated list of metrics to retrieve (e.g., `views,likes,dislikes`).
- **dimensions** (string) - Optional - A comma-separated list of dimensions to aggregate data by (e.g., `day,country`).
- **filters** (string) - Optional - A comma-separated list of filters to apply to the data (e.g., `country==US`).
- **sort** (string) - Optional - A comma-separated list of sorting instructions (e.g., `views:-1` for descending order of views).

### Request Example
```json
{
  "example": "GET https://youtubeanalytics.googleapis.com/v2/reports?ids=channel==CHANNEL_ID&start-date=2023-01-01&end-date=2023-01-31&metrics=views,likes&dimensions=day"
}
```

### Response
#### Success Response (200)
- **columnHeaders** (array) - Contains information about the columns in the report data.
- **rows** (array) - An array of data rows, where each row is an array of values corresponding to the column headers.
- **totals** (array) - An array of total values for each metric.
- **metadata** (object) - Contains metadata about the report.

#### Response Example
```json
{
  "example": {
    "columnHeaders": [
      {
        "name": "day",
        "columnType": "DIMENSION"
      },
      {
        "name": "views",
        "columnType": "METRIC"
      },
      {
        "name": "likes",
        "columnType": "METRIC"
      }
    ],
    "rows": [
      ["2023-01-01", "1000", "50"],
      ["2023-01-02", "1200", "60"]
    ],
    "totals": ["2200", "110"],
    "metadata": {
      "channelId": "CHANNEL_ID"
    }
  }
}
```
```

--------------------------------

### Creating YT.Player Objects

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

Examples demonstrating how to create and initialize YT.Player objects, including using existing iframes and handling player readiness and state changes.

```APIDOC
## Creating YT.Player Objects

### Description
Examples demonstrating how to create and initialize YT.Player objects, including using existing iframes and handling player readiness and state changes.

### Example 1: Use API with existing <iframe>

This example shows how to use the API with an existing `<iframe>` element. Ensure the `enablejsapi` parameter is set to `1` in the `src` URL or the `enablejsapi` attribute is set to `true` on the `<iframe>` element.

#### `onPlayerReady` Function
This function is called when the player is ready. It can be used to change the player's border color.

#### `onPlayerStateChange` Function
This function is called when the player's state changes. It can be used to dynamically change the player's border color based on the current state (e.g., green for playing, red for paused).

### Code Example

```html
<iframe id="player" type="text/html" width="640" height="360"
  src="http://www.youtube.com/embed/VIDEO_ID?enablejsapi=1"
  frameborder="0"></iframe>

<script>
  var player;
  function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  }

  function onPlayerReady(event) {
    // Access the player instance via event.target
    event.target.setOption('captions', 'fontSize', 1); // Example: Set caption font size
    event.target.playVideo();
  }

  function onPlayerStateChange(event) {
    // Handle player state changes, e.g., change border color
    var playerElement = document.getElementById('player');
    switch(event.data) {
      case YT.PlayerState.PLAYING:
        playerElement.style.borderColor = 'green';
        break;
      case YT.PlayerState.PAUSED:
        playerElement.style.borderColor = 'red';
        break;
      case YT.PlayerState.BUFFERING:
        playerElement.style.borderColor = 'blue';
        break;
    }
  }
</script>
```
```

--------------------------------

### Get YouTube Data API Go Client Library

Source: https://developers.google.com/youtube/v3/quickstart/go

Use `go get` to download the necessary Go packages for interacting with the YouTube Data API and handling OAuth2 authentication.

```bash
go get -u google.golang.org/api/youtube/v3
go get -u golang.org/x/oauth2/...
```

--------------------------------

### Create a Claim and Set Advertising Options

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=es

Initializes a claim resource for a video and asset, then updates the video's advertising options to include TrueView formats.

```php
// Create a claim resource. Identify the video being claimed, the asset
    // that represents the claimed content, the type of content being claimed,
    // and the policy that you want to apply to the claimed video.
    $claim = new Google_Service_YouTubePartner_Claim();
    $claim->setAssetId($assetId);
    $claim->setVideoId($videoId);
    $claim->setPolicy($policy);
    $claim->setContentType("audiovisual");

    // Insert the created claim.
    $claimInsertResponse = $youtubePartner->claims->insert($claim,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    # Enable ads for the video. This example enables the TrueView ad format.
    $option = new Google_Service_YouTubePartner_VideoAdvertisingOption();
    $option->setAdFormats(array("trueview_instream"));
    $setAdvertisingResponse = $youtubePartner->videoAdvertisingOptions->update(
        $videoId, $option, array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### Upload a Reference using PHP

Source: https://developers.google.com/youtube/partner/code_samples/php

This script demonstrates the full workflow of creating an asset, setting ownership and match policies, and performing a resumable upload of a reference video.

```php
<?php

/**
 * This sample creates an asset, asset ownership, match policy and uploads a reference video by:
 *
 * 1. Finding the content owner ID with "youtubePartner.contentOwners.list" method
 * 2. Creating an asset with "youtubePartner.assets.insert" method
 * 3. Configure ownership on the asset with "youtubePartner.ownership.update" method
 * 4. Configure the asset's match policy with "youtubePartner.assetMatchPolicy.update" method
 * 5. Creating a refererence with "youtubePartner.reference.insert" method
 * 6. Uploading a reference video with "youtube.videos.insert" utilizing "Google_MediaFileUpload"
 *
 * @author Ibrahim Ulukaya
*/


// Call set_include_path() as needed to point to your client library.
require_once 'Google/Client.php';
require_once 'Google/Service/YouTube.php';
require_once 'Google/Service/YouTubePartner.php';
session_start();

/*
 * You can acquire an OAuth 2.0 service account name and private key file from the
 * Google API Console <https://console.cloud.google.com/>
 * For more information about using OAuth 2.0 Service Accounts to access Google APIs, please see:
 * <https://developers.google.com/accounts/docs/OAuth2ServiceAccount>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
$OAUTH2_SERVICE_ACCOUNT_NAME = 'REPLACE ME';

// Make sure you keep your key.p12 file in a secure location, and isn't
// readable by others.
$OAUTH2_KEY_FILE = '/super/secret/path/to/key.p12';

$client = new Google_Client();

// Define an object that will be used to make all API requests.
$youtube = new Google_Service_YouTube($client);

// YouTube Partner object used to make Content ID API requests.
$youtubePartner = new Google_Service_YouTubePartner($client);

if (isset($_SESSION['service_token'])) {
  $client->setAccessToken($_SESSION['service_token']);
}

/* Load the key in PKCS 12 format. You need to download this from the
 * Google API Console when the service account was created.
 * Please read https://developers.google.com/youtube/partner/guides/oauth2_for_service_accounts
 * for info on configuration.
 */
$key = file_get_contents($OAUTH2_KEY_FILE);
$cred = new Google_Auth_AssertionCredentials(
    $OAUTH2_SERVICE_ACCOUNT_NAME,
    array('https://www.googleapis.com/auth/youtubepartner'),
    $key);
$client->setAssertionCredentials($cred);


if($client->getAuth()->isAccessTokenExpired()) {
  $client->getAuth()->refreshTokenWithAssertion($cred);
}

$_SESSION['service_token'] = $client->getAccessToken();

  try{

    // REPLACE this value with the path to the file you are uploading
    // as a reference.
    $referenceVideoPath = "/path/to/file.mp4";

    // Call the contentOwners.list method to retrieve the ID of the content
    // owner associated with the currently authenticated user's account.
    $contentOwnersListResponse = $youtubePartner->contentOwners->listContentOwners(
        array('fetchMine' => true));
    $contentOwnerId = $contentOwnersListResponse['items'][0]['id'];


    // Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
```

--------------------------------

### API Key and Registration Instructions

Source: https://developers.google.com/youtube/v3/code_samples/python_appengine?hl=de

Provides instructions for setting up a project, obtaining an API key, and enabling necessary APIs (YouTube Data API v3, Freebase API).

```html
REGISTRATION_INSTRUCTIONS = """
    You must set up a project and get an API key to run this code. Please see
    the instructions for creating a project and a key at <a
    href="https://developers.google.com/youtube/registering_an_application"
    >https://developers.google.com/youtube/registering_an_application</a>.
    <br><br>
    Make sure that you have enabled the YouTube Data API (v3) and the Freebase
    API for your project."

# Set API_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API and Freebase API
```

--------------------------------

### PlaylistItems: insert Request Body Example

Source: https://developers.google.com/youtube/v3/docs/playlistItems/insert?hl=de

Example of a playlistItem resource to be sent in the request body for inserting a video into a playlist. Ensure 'snippet.playlistId' and 'snippet.resourceId' are correctly specified.

```json
{
  "snippet": {
    "playlistId": "YOUR_PLAYLIST_ID",
    "resourceId": {
      "kind": "youtube#video",
      "videoId": "YOUR_VIDEO_ID"
    },
    "position": 0
  },
  "contentDetails": {
    "note": "This is a note for the playlist item."
  }
}
```

--------------------------------

### OAuth 2.0 Redirect Response Examples

Source: https://developers.google.com/youtube/partner/guides/auth/client-side-web-apps

Examples of hash fragment responses containing access tokens or error messages returned to the redirect URI.

```text
https://oauth2.example.com/callback#access_token=4/P7q7W91&token_type=Bearer&expires_in=3600
```

```text
https://oauth2.example.com/callback#error=access_denied
```

--------------------------------

### Initialize Reporting API Client

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=vi

Sets up the environment, dependencies, and command-line options for the report retrieval script.

```php
if (!file_exists(__DIR__ . '/vendor/autoload.php')) {
  throw new \Exception('please run "composer require google/apiclient:~2.2.0" in "' . __DIR__ .'"');
}

require_once __DIR__ . '/vendor/autoload.php';
session_start();


define('CREDENTIALS_PATH', '~/.credentials/youtube-php.json');

$longOptions = array(
  'contentOwner::',
  'downloadUrl::',
  'includeSystemManaged::',
  'jobId::',
  'outputFile::',
);

$options = getopt('', $longOptions);

$CONTENT_OWNER_ID = ($options['contentOwner'] ? $options['contentOwner'] : '');
$DOWNLOAD_URL = (array_key_exists('downloadUrl', $options) ?
                 $options['downloadUrl'] : '');
$INCLUDE_SYSTEM_MANAGED = (array_key_exists('includeSystemManaged', $options) ?
                           $options['includeSystemManaged'] : '');
$JOB_ID = (array_key_exists('jobId', $options) ? $options['jobId'] : '');
$OUTPUT_FILE = (array_key_exists('outputFile', $options) ?
                $options['outputFile'] : '');
```

--------------------------------

### Collection-level field selection examples

Source: https://developers.google.com/youtube/partner/guides/performance

Examples of field strings used to filter collection-level API responses.

```text
items
```

```text
etag,items
```

```text
items/title
```

```text
context/facets/label
```

```text
items/pagemap/*/title
```

--------------------------------

### Configure Service and Call YouTube API in Ruby

Source: https://developers.google.com/youtube/v3/live/guides/auth/server-side-web-apps

Initializes the YouTube service, sets authorization credentials, and retrieves live broadcasts.

```Ruby
youtube = Google::Apis::YoutubeV3::YouTubeService.new
```

```Ruby
youtube.authorization = credentials
```

```Ruby
broadcasts = youtube.list_liveBroadcasts('id,snippet', mine: true)
```

```Ruby
broadcasts = youtube.list_liveBroadcasts('id,snippet', mine: true)
```

--------------------------------

### Search API - Ruby Example

Source: https://developers.google.com/youtube/v3/docs/search/list?hl=ar

This example demonstrates how to use the Ruby client library to call the search.list method of the YouTube Data API v3. It retrieves search results for a given query and categorizes them into videos, channels, and playlists.

```APIDOC
## POST /youtube/v3/search

### Description
Retrieves a collection of search results that match the specified query (as defined in the API documentation).

### Method
POST

### Endpoint
/youtube/v3/search

### Parameters
#### Query Parameters
- **part** (string) - Required - Specifies a comma-separated list of one or more search resource properties that the API response should include. The supported properties are id and snippet.
- **q** (string) - Required - The search string to execute.
- **maxResults** (integer) - Optional - The maximum number of items to return in the result list.

### Request Example
```ruby
require 'rubygems'
gem 'google-api-client', '>0.7'
require 'google/api_client'
require 'trollop'

DEVELOPER_KEY = 'REPLACE_ME'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_service
  client = Google::APIClient.new(
    :key => DEVELOPER_KEY,
    :authorization => nil,
    :application_name => $PROGRAM_NAME,
    :application_version => '1.0.0'
  )
  youtube = client.discovered_api(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION)
  return client, youtube
end

def main
  opts = Trollop::options do
    opt :q, 'Search term', :type => String, :default => 'Google'
    opt :max_results, 'Max results', :type => :int, :default => 25
  end

  client, youtube = get_service

  begin
    search_response = client.execute!(
      :api_method => youtube.search.list,
      :parameters => {
        :part => 'snippet',
        :q => opts[:q],
        :maxResults => opts[:max_results]
      }
    )

    videos = []
    channels = []
    playlists = []

    search_response.data.items.each do |search_result|
      case search_result.id.kind
        when 'youtube#video'
          videos << "#{search_result.snippet.title} (#{search_result.id.videoId})"
        when 'youtube#channel'
          channels << "#{search_result.snippet.title} (#{search_result.id.channelId})"
        when 'youtube#playlist'
          playlists << "#{search_result.snippet.title} (#{search_result.id.playlistId})"
      end
    end

    puts "Videos:\n", videos, "\n"
    puts "Channels:\n", channels, "\n"
    puts "Playlists:\n", playlists, "\n"
  rescue Google::APIClient::TransmissionError => e
    puts e.result.body
  end
end

main
```

### Response
#### Success Response (200)
- **items** (array) - The search results.
  - **id** (object) - The ID of the search result.
    - **kind** (string) - The type of the search result (e.g., 'youtube#video', 'youtube#channel', 'youtube#playlist').
    - **videoId** (string) - The ID of the video.
    - **channelId** (string) - The ID of the channel.
    - **playlistId** (string) - The ID of the playlist.
  - **snippet** (object) - The snippet of the search result.
    - **title** (string) - The title of the search result.

#### Response Example
```json
{
  "items": [
    {
      "id": {
        "kind": "youtube#video",
        "videoId": "dQw4w9WgXcQ"
      },
      "snippet": {
        "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)"
      }
    },
    {
      "id": {
        "kind": "youtube#channel",
        "channelId": "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
      },
      "snippet": {
        "title": "Rick Astley"
      }
    }
  ]
}
```

### Errors
- **badRequest (400)** - `invalidChannelId`: The `channelId` parameter specified an invalid channel ID.
- **badRequest (400)** - `invalidLocation`: The `location` and/or `locationRadius` parameter value was formatted incorrectly.
- **badRequest (400)** - `invalidRelevanceLanguage`: The `relevanceLanguage` parameter value was formatted incorrectly.
- **badRequest (400)** - `invalidSearchFilter`: The request contains an invalid combination of search filters and/or restrictions. Note that you must set the `type` parameter to `video` if you set either the `forContentOwner` or `forMine` parameters to `true`. You must also set the `type` parameter to `video` if you set a value for the `eventType`, `videoCaption`, `videoCategoryId`, `videoDefinition`, `videoDimension`, `videoDuration`, `videoEmbeddable`, `videoLicense`, `videoSyndicated`, or `videoType` parameters.
```

--------------------------------

### Example Calculation of Cuepoint Time Offset

Source: https://developers.google.com/youtube/v3/live

Example calculation demonstrating the offset time range based on provided values for elapsed time, broadcast delay, and the buffer (\u2206).

```text
[(485000), (535000)]
```

--------------------------------

### Execute PHP Sample

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Run the PHP script from the command line.

```bash
php sample.php
```

--------------------------------

### Upload and Monetize Video Example (Python)

Source: https://developers.google.com/youtube/partner/guides/upload

This Python script demonstrates uploading a YouTube video, creating an asset, claiming the video, and applying a monetization policy. It requires Python 2.5+, the google-api-python-client library, and a client_secrets.json file for authentication.

```python
import argparse
import httplib2
import os

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets

# Explicitly cache the flow
FLOW = None

def get_authenticated_service(scopes):
  global FLOW
  if FLOW is None:
    FLOW = flow_from_clientsecrets(
        'client_secrets.json', 
        scope=scopes,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')

  # The install flow is not recommended by the security best practices, but it is the simplest for 
  # many use cases. 
  auth_uri = FLOW.step1_recreate_authorization_url()

  # Display the authorization URL to the user and ask for the code.
  print 'Go to the following link in your browser. Then try to repeat the steps.'
  print auth_uri

  while True:
    auth_code = raw_input('Enter the authorization code: ')
    if auth_code > "":
      break
  creds = FLOW.step2_exchange(auth_code)
  return build('youtube', 'v3', http=httplib2.Http(), credentials=creds)

def main():
  argparser = argparse.ArgumentParser()
  argparser.add_argument('--file', help='Upload file', required=True)
  argparser.add_argument('--title', help='Video title', default='Test Video Title')
  argparser.add_argument('--description', help='Video description', default='Test Video Description')
  argparser.add_argument('--keywords', help='Video keywords, comma separated',)
  argparser.add_argument('--category', default='22', help='Video category ID')
  argparser.add_argument('--privacyStatus', default='private', help='Video privacy status (private, public, unlisted)')
  args = argparser.parse_args()

  # Call the YouTube Data API service name 'youtube' and version 'v3'. 
  youtube = get_authenticated_service(
      ["https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtube.force-ssl"]
  )
  try:
    body={'snippet': {'title': args.title,
                      'description': args.description,
                      'tags': args.keywords.split(","),
                      'categoryId': args.category
                     },
            'status': {'privacyStatus': args.privacyStatus}
           }

    # Call the videos.insert method to create a new video.
    insert_request = youtube.videos().insert(
      body=body,
      part='snippet,status'
    )
    # Replace file path with actual file path
    insert_request.media.file = args.file
    response = insert_request.execute()

    print response

  except Exception as e:
    print e

if __name__ == '__main__':
  main()

```

--------------------------------

### YouTube Content ID API Sample Usage

Source: https://developers.google.com/youtube/partner/guides/migration_xml_to_api?hl=de

Demonstrates how to run the command-line sample for the YouTube Content ID API. Shows basic usage, help command, and detailed logging.

```bash
python yt_partner_api.py --file="/path/to/reference/file"
```

```bash
python yt_partner_api.py --help
```

```bash
python yt_partner_api.py --logging_level=DEBUG \
     --file="/path/to/reference/file"
```

--------------------------------

### Top 10 Most Started Playlists in the United States

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=ru

Retrieves the 10 playlists most frequently started by viewers in the United States, sorted by playlist starts in descending order. Requires `sort` parameter and `maxResults` set to 10 or less.

```APIDOC
## GET /analytics/v1/data

### Description
Retrieves the 10 playlists that viewers in the United States started watching most frequently, sorted by number of playlist starts in descending order. Requires `sort` parameter and `maxResults` set to 10 or less.

### Method
GET

### Endpoint
/analytics/v1/data

### Query Parameters
- **dimensions** (string) - Required - e.g., `playlist`
- **metrics** (string) - Required - e.g., `playlistStarts,views,estimatedMinutesWatched,averageViewDuration`
- **filters** (string) - Required - e.g., `country==US`
- **maxResults** (integer) - Required - Maximum number of results, must be 10 or less.
- **sort** (string) - Required - e.g., `-playlistStarts` (descending by playlist starts)

### Request Example
```json
{
  "dimensions": "playlist",
  "metrics": "playlistStarts,views,estimatedMinutesWatched,averageViewDuration",
  "filters": "country==US",
  "maxResults": 10,
  "sort": "-playlistStarts"
}
```

### Response
#### Success Response (200)
- **playlistStarts** (integer) - Number of times playlists were started.
- **views** (integer) - Number of views.
- **estimatedMinutesWatched** (integer) - Estimated minutes watched.
- **averageViewDuration** (number) - Average view duration.

#### Response Example
```json
{
  "kind": "youtubeAnalytics#resultTable",
  "rows": [
    ["PLAYLIST_ID", 5000, 100000, 500000, 3.5]
  ],
  "columnHeaders": [
    {"name": "playlist", "columnType": "DIMENSION"},
    {"name": "playlistStarts", "columnType": "METRIC"},
    {"name": "views", "columnType": "METRIC"},
    {"name": "estimatedMinutesWatched", "columnType": "METRIC"},
    {"name": "averageViewDuration", "columnType": "METRIC"}
  ]
}
```
```

--------------------------------

### Initialize YouTube Reporting API in PHP

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=zh-tw

Sets up the PHP client library and parses command-line arguments for reporting tasks.

```php
<?php

/**
 * This sample supports the following use cases:
 *
 * 1. Retrieve reporting jobs by content owner:
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID"
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID" --includeSystemManaged==True
 * 2. Retrieving list of downloadable reports for a particular job:
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID" --jobId="JOB_ID"
 * 3. Download a report:
 *    Ex: php retrieve_reports.php  --contentOwner=="CONTENT_OWNER_ID" --downloadUrl="DOWNLOAD_URL" --outputFile="report.txt"
 */

/**
 * Library Requirements
 *
 * 1. Install composer (https://getcomposer.org)
 * 2. On the command line, change to this directory (api-samples/php)
 * 3. Require the google/apiclient library
 *    $ composer require google/apiclient:~2.0
 */
if (!file_exists(__DIR__ . '/vendor/autoload.php')) {
  throw new \Exception('please run "composer require google/apiclient:~2.2.0" in "' . __DIR__ .'"');
}

require_once __DIR__ . '/vendor/autoload.php';
session_start();


define('CREDENTIALS_PATH', '~/.credentials/youtube-php.json');

$longOptions = array(
  'contentOwner::',
  'downloadUrl::',
  'includeSystemManaged::',
  'jobId::',
  'outputFile::',
);

$options = getopt('', $longOptions);

$CONTENT_OWNER_ID = ($options['contentOwner'] ? $options['contentOwner'] : '');
$DOWNLOAD_URL = (array_key_exists('downloadUrl', $options) ?
                 $options['downloadUrl'] : '');
$INCLUDE_SYSTEM_MANAGED = (array_key_exists('includeSystemManaged', $options) ?
                           $options['includeSystemManaged'] : '');
$JOB_ID = (array_key_exists('jobId', $options) ? $options['jobId'] : '');
```

--------------------------------

### Initialize YouTube API Client

Source: https://developers.google.com/youtube/v3/code_samples/ruby?hl=ko

Sets up the Google API client with required gems and authentication scopes for read-only access.

```ruby
#!/usr/bin/ruby

require 'rubygems'
gem 'google-api-client', '>0.7'
require 'google/api_client'
require 'google/api_client/client_secrets'
require 'google/api_client/auth/file_storage'
require 'google/api_client/auth/installed_app'

# This OAuth 2.0 access scope allows for read-only access to the authenticated
```

--------------------------------

### Resource-level field selection examples

Source: https://developers.google.com/youtube/partner/guides/performance

Examples of field strings used to filter single resource API responses.

```text
title
```

```text
author/uri
```

```text
links/*/href
```

--------------------------------

### Configure Flask Application

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=he

Sets environment variables for local development and starts the Flask server.

```python
if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification.
  # ACTION ITEM for developers:
  #     When running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  # This disables the requested scopes and granted scopes check.
  # If users only grant partial request, the warning would not be thrown.
  os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

  # Specify a hostname and port that are set as a valid redirect URI
  # for your API project in the Google API Console.
  app.run('localhost', 8080, debug=True)
```

--------------------------------

### Initiate Resumable Upload with MediaFileUpload

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=es

Prepares for a resumable upload of a reference video. This involves setting the defer flag on the client, creating a reference resource, and initializing a Google_Http_MediaFileUpload object with chunk size and file size.

```php
// Specify the size of each chunk of data, in bytes. Set a higher value for
    // reliable connection as fewer chunks lead to faster uploads. Set a lower
    // value for better recovery on less reliable connections.
    $chunkSizeBytes = 1 * 1024 * 1024;

    // Setting the defer flag to true tells the client to return a request which can be called
    // with ->execute(); instead of making the API call immediately.
    $client->setDefer(true);

    // Create a reference resource. Set the asset ID associated with the
    // reference, and identify the type of reference content being uploaded.
    $reference = new Google_Service_YouTubePartner_Reference();
    $reference->setAssetId($assetId);
    $reference->setContentType("video");

    // Create a request for the API's references.insert method to insert the reference resource
    // while uploading the reference video.
    $insertRequest = $youtubePartner->references->insert($reference,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    // Create a MediaFileUpload object for resumable uploads.
    $media = new Google_Http_MediaFileUpload(
        $client,
        $insertRequest,
        'video/*',
        null,
        true,
        $chunkSizeBytes
    );
    $media->setFileSize(filesize($referenceVideoPath));
```

--------------------------------

### Create a Claim and Set Advertising Options

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=id

Initializes a policy and claim resource to monetize a video, then updates the video's advertising options to enable TrueView ads.

```php
$policy = new Google_Service_YouTubePartner_Policy();
    $policyRule = new Google_Service_YouTubePartner_PolicyRule();
    $policyRule->setAction("monetize");
    $policy->setRules(array($policyRule));

    // Create a claim resource. Identify the video being claimed, the asset
    // that represents the claimed content, the type of content being claimed,
    // and the policy that you want to apply to the claimed video.
    $claim = new Google_Service_YouTubePartner_Claim();
    $claim->setAssetId($assetId);
    $claim->setVideoId($videoId);
    $claim->setPolicy($policy);
    $claim->setContentType("audiovisual");

    // Insert the created claim.
    $claimInsertResponse = $youtubePartner->claims->insert($claim,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    # Enable ads for the video. This example enables the TrueView ad format.
    $option = new Google_Service_YouTubePartner_VideoAdvertisingOption();
    $option->setAdFormats(array("trueview_instream"));
    $setAdvertisingResponse = $youtubePartner->videoAdvertisingOptions->update(
        $videoId, $option, array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### Run Node.js Code Sample

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Execute your Node.js API sample from the command line. Ensure the sample file is in the same directory as your client_secrets.json or that the path is correctly specified.

```bash
node sample.js
```

--------------------------------

### Upload a file in chunks - PUT request example

Source: https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol

This example demonstrates the format of a PUT request to upload the first chunk of a file. Ensure Content-Length is the size of the chunk and Content-Range specifies the byte range being uploaded within the total file size.

```http
PUT UPLOAD_URL HTTP/1.1
Authorization: Bearer AUTH_TOKEN
Content-Length: 524888
Content-Type: video/*
Content-Range: bytes 0-524287/2000000

{bytes 0-524287}
```

--------------------------------

### Define Script Command-Line Arguments

Source: https://developers.google.com/youtube/v3/guides/uploading_a_video

Examples of individual command-line arguments for the upload script.

```bash
Example: --file="/home/path/to/file.mov"
```

```bash
Example: --title="Summer vacation in California"
```

```bash
Example: --description="Had fun surfing in Santa Cruz"
```

```bash
Example: --category="22"
```

```bash
Example: --keywords="surfing"
```

```bash
Example: --privacyStatus="private"
```

--------------------------------

### Initialize YouTube Partner Service Account Client

Source: https://developers.google.com/youtube/partner/code_samples/php

Sets up the Google Client with service account credentials for YouTube Partner API access.

```php
<?php

/**
 * This sample uploads, claims and monetizes a video by :
 *
 * 1. Finding the content owner ID via "youtubePartner.contentOwners.listContentOwners" method
 * 2. Uploading the video via "youtube.videos.insert" with utilizing "Google_MediaFileUpload"
 * 3. Creating an asset via "youtubePartner.assets.insert" method
 * 4. Creating ownership on the asset via "youtubePartner.ownership.update" method
 * 5. Claiming the video with the asset and a policy via "youtubePartner.claims.insert"
 * 6. Enabling the TrueView advertising on the video via "youtubePartner.videoAdvertisingOptions.update"
 *
 * @author Ibrahim Ulukaya
*/


// Call set_include_path() as needed to point to your client library.
require_once 'Google/Client.php';
require_once 'Google/Service/YouTube.php';
require_once 'Google/Service/YouTubePartner.php';
session_start();

/*
 * You can acquire an OAuth 2.0 service account name and private key file from the
 * Google API Console <https://console.cloud.google.com/>
 * For more information about using OAuth 2.0 Service Accounts to access Google APIs, please see:
 * <https://developers.google.com/accounts/docs/OAuth2ServiceAccount>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
$OAUTH2_SERVICE_ACCOUNT_NAME = 'REPLACE ME';

// Make sure you keep your key.p12 file in a secure location, and isn't
// readable by others.
$OAUTH2_KEY_FILE = '/super/secret/path/to/key.p12';

$client = new Google_Client();

// Define an object that will be used to make all API requests.
$youtube = new Google_Service_YouTube($client);

// YouTube Partner object used to make Content ID API requests.
$youtubePartner = new Google_Service_YouTubePartner($client);

if (isset($_SESSION['service_token'])) {
  $client->setAccessToken($_SESSION['service_token']);
}

/* Load the key in PKCS 12 format. You need to download this from the
 * Google API Console when the service account was created.
 * Please read https://developers.google.com/youtube/partner/guides/oauth2_for_service_accounts
 * for info on configuration.
 */
$key = file_get_contents($OAUTH2_KEY_FILE);
$cred = new Google_Auth_AssertionCredentials(
    $OAUTH2_SERVICE_ACCOUNT_NAME,
    array('https://www.googleapis.com/auth/youtubepartner'),
    $key);
$client->setAssertionCredentials($cred);


if($client->getAuth()->isAccessTokenExpired()) {
  $client->getAuth()->refreshTokenWithAssertion($cred);
}
```

--------------------------------

### HTML Document Structure for Assets Labels Example

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=es

Basic HTML structure for a web page displaying the results of the Assets Labels Example. It includes a title and a placeholder for dynamic content generated by PHP.

```html
<!doctype html>
<html>
<head>
<title>Assets Labels Example</title>
</head>
<body>
  <?=$htmlBody?>
</body>
</html>
```

--------------------------------

### Execute Python Sample

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Run the Python script from the command line.

```bash
python sample.py
```

--------------------------------

### Initialize API Client

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=he

Sets up the YouTube Reporting service object for API requests.

```php
// Define an object that will be used to make all API requests.
$client = getClient();
// YouTube Reporting object used to make YouTube Reporting API requests.
$youtubeReporting = new Google_Service_YouTubeReporting($client);

if ($CONTENT_OWNER_ID) {
  if (!$DOWNLOAD_URL && !$JOB_ID) {
    listReportingJobs($youtubeReporting, $CONTENT_OWNER_ID,
                      $INCLUDE_SYSTEM_MANAGED);
  } else if ($JOB_ID) {
```

--------------------------------

### API Response Example

Source: https://developers.google.com/youtube/v3/getting-started

This is an example of an API response that includes only specific fields from the video resource's snippet object, as requested by the API.

```json
{
 "videos": [
  {
   "id": "7lCDEmM",
   "snippet": {
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "title": "Google I/O 101: Q&A On Using Google APIs",
    "categoryId": "28"
   },
   "statistics": {
    "viewCount": "3057",
    "likeCount": "25",
    "dislikeCount": "0",
    "favoriteCount": "17",
    "commentCount": "12"
   }
  }
 ]
}
```

--------------------------------

### Authentication and Client Initialization

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=es-419

This snippet demonstrates how to set up the Google_Client for YouTube Reporting, including authentication and scope configuration.

```APIDOC
## Authentication and Client Initialization

### Description
Initializes the Google_Client with necessary credentials and scopes for accessing the YouTube Reporting API. It handles loading existing credentials or guiding the user through the OAuth 2.0 authorization flow.

### Method
N/A (Initialization function)

### Endpoint
N/A

### Parameters
None

### Request Body
None

### Request Example
```php
require_once __DIR__ . '/vendor/autoload.php';
session_start();

// ... (other setup code)

$client = getClient();
$youtubeReporting = new Google_Service_YouTubereporting($client);
```

### Response
- **Google_Client**: An authenticated Google_Client object.

### Response Example
```php
// Returns an authenticated Google_Client object
```
```

--------------------------------

### Execute Ruby Sample

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Run the Ruby script from the command line.

```bash
ruby sample.rb
```

--------------------------------

### Example YouTube Playlist Embed URL

Source: https://developers.google.com/youtube/player_parameters

An example of a YouTube playlist embed URL, showing the required 'PL' prefix for the playlist ID.

```html
https://www.youtube.com/embed?listType=playlist&list=**PLC77007E23FF423C6**
```

--------------------------------

### YouTube Analytics API CSV Response Example

Source: https://developers.google.com/youtube/analytics/reference/reports/query

An example of a CSV formatted response from the YouTube Analytics API, showing dimensions and metrics.

```csv
day, views, likes, ...
"2012-01-01", 12.0, 3, ...
"2012-01-02", 16.0, 2, ...
"2012-01-03", 18.0, 8, ...
...
```

--------------------------------

### Initialize Flask app and API service details

Source: https://developers.google.com/youtube/v3/live/guides/auth/server-side-web-apps?hl=ko

Set up a Flask application instance and define constants for the YouTube API service name and version. A secret key is required for Flask applications.

```python
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

app = flask.Flask(__name__)
# Note: A secret key is included in the sample so that it works.
# If you use this code in your application, replace this with a truly secret
```

--------------------------------

### Create and Configure YouTube Assets

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=tr

Initializes an asset with metadata and registers it with the YouTube Partner API.

```php
$metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];
```

--------------------------------

### Create New Gradle Project

Source: https://developers.google.com/youtube/v3/quickstart/java

Use Gradle to initialize a new basic Java project structure. Ensure you create the necessary directories for main Java code and resources.

```bash
$ gradle init --type basic
$ mkdir -p src/main/java src/main/resources

```

--------------------------------

### Initialize OAuth2 Client and Scopes

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps?hl=de

Set up the OAuth2 client with your credentials and define the necessary API scopes. Ensure you replace placeholders with your actual client ID, client secret, and redirect URL.

```javascript
const http = require('http');
const https = require('https');
const url = require('url');
const { google } = require('googleapis');
const crypto = require('crypto');
const express = require('express');
const session = require('express-session');

/**
 * To use OAuth2 authentication, we need access to a CLIENT_ID, CLIENT_SECRET, AND REDIRECT_URI.
 * To get these credentials for your application, visit
 * https://console.cloud.google.com/apis/credentials.
 */
const oauth2Client = new google.auth.OAuth2(
  YOUR_CLIENT_ID,
  YOUR_CLIENT_SECRET,
  YOUR_REDIRECT_URL
);

// Access scopes for YouTube API
const scopes = [
  'https://www.googleapis.com/auth/youtube.force-ssl'
];

/* Global variable that stores user credential in this code example.
 * ACTION ITEM for developers:
 *   Store user's refresh token in your data store if
 *   incorporating this code into your real app.
 *   For more information on handling refresh tokens, 
 *   see https://github.com/googleapis/google-api-nodejs-client#handling-refresh-tokens
 */
let userCredential = null;
```

--------------------------------

### HTTP GET Request for LiveStreams

Source: https://developers.google.com/youtube/v3/live/docs/liveStreams/list

This is the base HTTP GET request to retrieve a list of live streams. Ensure you have the necessary authorization scopes.

```http
GET https://www.googleapis.com/youtube/v3/liveStreams
```

--------------------------------

### Initialize and Use Google API Services in PHP

Source: https://developers.google.com/youtube/reporting/guides/authorization/server-side-web-apps

Set the access token on the client, build the service object, and execute API requests.

```php
$client->setAccessToken($access_token);
```

```php
$youtube = new Google_Service_YouTubeAnalytics($client);
```

```php
$report = $youtube->reports->query('channel==MINE', '2016-05-01', '2016-06-30', 'views');
```

--------------------------------

### Initialize Google Authentication with Sinatra

Source: https://developers.google.com/youtube/reporting/guides/authorization/server-side-web-apps?hl=tr

Sets up Google authentication using Sinatra, including client ID, scopes, token store, and callback URI. Requires a client_secret.json file and a Redis instance.

```ruby
require 'googleauth'
require 'googleauth/web_user_authorizer'
require 'googleauth/stores/redis_token_store'

require 'google/apis/youtube_analytics_v1'
require 'google/apis/calendar_v3'

require 'sinatra'

configure do
  enable :sessions

  # Required, call the from_file method to retrieve the client ID from a
  # client_secret.json file.
  set :client_id, Google::Auth::ClientId.from_file('/path/to/client_secret.json')

  # Required, scope value
  # Access scopes for two non-Sign-In scopes: Read-only Drive activity and Google Calendar.
  scope = ['Google::Apis::DriveV3::AUTH_DRIVE_METADATA_READONLY',
           'Google::Apis::CalendarV3::AUTH_CALENDAR_READONLY']

  # Required, Authorizers require a storage instance to manage long term persistence of
  # access and refresh tokens.
  set :token_store, Google::Auth::Stores::RedisTokenStore.new(redis: Redis.new)

  # Required, indicate where the API server will redirect the user after the user completes
  # the authorization flow. The redirect URI is required. The value must exactly
  # match one of the authorized redirect URIs for the OAuth 2.0 client, which you
  # configured in the API Console. If this value doesn't match an authorized URI,
  # you will get a 'redirect_uri_mismatch' error.
  set :callback_uri, '/oauth2callback'
```

--------------------------------

### Run Java Code Sample with Gradle

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Execute your Java API sample locally using Gradle. This command assumes your project is set up according to the provided build.gradle configuration.

```bash
gradle -q run
```

--------------------------------

### HTTP GET Request for CommentThreads

Source: https://developers.google.com/youtube/v3/docs/commentThreads/list?hl=es

This is the base HTTP GET request to retrieve comment threads. You will need to append parameters to this URL to filter the results.

```http
GET https://www.googleapis.com/youtube/v3/commentThreads
```

--------------------------------

### Authentication and Client Setup

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list

This snippet demonstrates how to set up the Google API client with OAuth 2.0 credentials and scopes for accessing YouTube reporting data.

```APIDOC
## Authentication and Client Setup

### Description
This section details the process of obtaining OAuth 2.0 credentials from the Google Cloud Console and configuring the Google API client for PHP to access the YouTube Data API and YouTube Reporting API.

### Method
N/A (Client Setup)

### Endpoint
N/A (Client Setup)

### Parameters
N/A

### Request Example
N/A

### Response
N/A

## PHP Code for `getClient()` function

```php
<?php

/**
 * Returns an authorized Google_Client object.
 * 
 * @return Google_Client the authorized client object
 */
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope('https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: '; 
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }
  return $client;
}

/**
 * Expands the home directory alias '~' to the full path.
 * @param string $path the path to expand.
 * @return string the expanded path.
 */
function expandHomeDirectory($path) {
  $homeDirectory = getenv('HOME');
  if (empty($homeDirectory)) {
    $homeDirectory = getenv('HOMEDRIVE') . getenv('HOMEPATH');
  }
  return str_replace('~', realpath($homeDirectory), $path);
}

?>
```
```

--------------------------------

### Example Member Resource Snippet

Source: https://developers.google.com/youtube/v3/docs/members

Illustrates how membership duration and level access are represented in the Member resource. This example shows a member who has been active since June 2020, with a total duration of 7 months, and has accessed level 1 for the entire duration and level 2 since August 2020.

```json
"membershipsDetails": {
  "membershipsDuration": {
    "memberSince": "2020-06-01T12:00:00",
    "memberTotalDurationMonths": 7,
  },
  "membershipsDurationAtLevel": [
    {
      "level": "level_1_ID",
      "memberSince": "2020-06-01T12:00:00",
      "memberTotalDurationMonths": 7
    },
    {
      "level": "level_2_ID",
      "memberSince": "2020-08-01T12:00:00",
      "memberTotalDurationMonths": 2
    },
  ]
}
```

--------------------------------

### API Initialization and Loading

Source: https://developers.google.com/youtube/js_api_reference?hl=ko

Instructions on how to load the YouTube IFrame Player API and initialize the player.

```APIDOC
## GET /youtube/iframe_api

### Description
Guidance on loading the IFrame Player API and ensuring proper initialization.

### Method
GET

### Endpoint
/youtube/iframe_api

### Initialization
- The `onYouTubeIframeAPIReady` function must be implemented to initialize the player.
- The API code URL is `http://www.youtube.com/iframe_api`.

### Embedding
- When manually creating the `<iframe>` tag, ensure a closing `</iframe>` tag is present for `onYouTubeIframeAPIReady` to be called.
- Recommended player dimensions: 16:9 players should be at least 480 pixels wide and 270 pixels tall. Minimum viewport size is 200px by 200px.
```

--------------------------------

### Example Calculation of Offset Times

Source: https://developers.google.com/youtube/v3/live/getting-started

Example calculation of offset times in milliseconds, given specific values for elapsed time, broadcast delay, and the buffer (Δ).

```plaintext
elapsed_time=540000
broadcast_delay=60000
Δ=5000

Possible range of offset times: [(485000), (535000)]
```

--------------------------------

### Insert a Private Video Example

Source: https://developers.google.com/youtube/v3/docs/videos/insert?hl=bn

This example demonstrates how to insert a video with its privacy status set to 'private'. The 'id', 'snippet.title', and 'snippet.categoryId' properties are required for this operation.

```json
{
  "id": "video_id",
  "snippet": {
    "title": "My Private Video Title",
    "categoryId": "22"
  },
  "status": {
    "privacyStatus": "private"
  }
}
```

--------------------------------

### Initialize YouTube API Service

Source: https://developers.google.com/youtube/v3/code_samples/python_appengine?hl=de

Sets up the YouTube API service with your developer key. Ensure the YouTube Data API is enabled for your project.

```python
DEVELOPER_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# ... later in the code ...
youtube = build(
  YOUTUBE_API_SERVICE_NAME,
  YOUTUBE_API_VERSION,
  developerKey=DEVELOPER_KEY)
```

--------------------------------

### Set up OAuth 2.0 Flow

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example?hl=ja

Initializes the OAuth 2.0 flow for authenticating with the YouTube Partner API. Ensure the CLIENT_SECRETS file is correctly configured.

```python
FLOW = flow_from_clientsecrets(CLIENT_SECRETS,
            scope='https://www.googleapis.com/auth/youtubepartner',
            message=MISSING_CLIENT_SECRETS_MESSAGE)
```

--------------------------------

### Configure YouTube Data API Environment

Source: https://developers.google.com/youtube/v3/code_samples/python_appengine?hl=fr

Setup imports, Jinja2 environment, and registration instructions for the YouTube Data API.

```python
import os
import urllib
import webapp2
import jinja2

from apiclient.discovery import build
from optparse import OptionParser

import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

REGISTRATION_INSTRUCTIONS = """
    You must set up a project and get an API key to run this code. Please see
    the instructions for creating a project and a key at <a
    href="https://developers.google.com/youtube/registering_an_application"
    >https://developers.google.com/youtube/registering_an_application</a>.
    <br><br>
    Make sure that you have enabled the YouTube Data API (v3) and the Freebase
    API for your project."""

# Set API_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API and Freebase API
```

--------------------------------

### Create and Configure YouTube Partner Assets

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=es

Initializes an asset resource with metadata and inserts it into the YouTube Partner API.

```php
// many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];
```

--------------------------------

### Configure Asset Ownership and Match Policy

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=ja

Sets up territory-based ownership and defines a track policy for assets. Requires an initialized YouTube Partner service instance.

```php
// Great Britain and Poland.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("include");
    $owners->setTerritories(array("PL","GB"));

    // Define the rights that the owner owns for the asset.
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId,
        $ownership, array('onBehalfOfContentOwner' => $contentOwnerId));

    $requiredTerritories = new Google_Service_YouTubePartner_TerritoryCondition();
    $requiredTerritories->setTerritories(array());
    $requiredTerritories->setType("exclude");

    // Create a "track" policy for the asset. The policy specifies the
    // conditions when the policy will be applied by defining a duration,
    // territories where the policy applies, and the type of content that an
    // uploaded video must match.
    $everywherePolicyCondition = new Google_Service_YouTubePartner_Conditions();
    $everywherePolicyCondition->setContentMatchType(array("video"));
    $everywherePolicyCondition->setRequiredTerritories($requiredTerritories);
    $everywherePolicyCondition->setReferenceDuration(array("low" => 10));

    // Create a policy rule and associate the conditions with the rule.
    $trackEverywhereRule = new Google_Service_YouTubePartner_PolicyRule();
    $trackEverywhereRule->setAction("track");
    $trackEverywhereRule->setConditions($everywherePolicyCondition);

    // Associate the policy rule with an assetMatchPolicy resource.
    $assetMatchPolicy = new Google_Service_YouTubePartner_AssetMatchPolicy();
    $assetMatchPolicy->setRules(array($trackEverywhereRule));


    // Update the asset's match policy
    $youtubePartner->assetMatchPolicy->update($assetId, $assetMatchPolicy,
        array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### Create Reporting Job Script Header

Source: https://developers.google.com/youtube/analytics/v1/code_samples/python?hl=pt-br

Initial setup for a script to create a new reporting job.

```python
#!/usr/bin/python

# Create a reporting job for the authenticated user's channel or
# for a content owner that the user's account is linked to.
# Usage example:
# python create_reporting_job.py --name='<name>'
```

--------------------------------

### HTTP GET Request for Videos: list

Source: https://developers.google.com/youtube/v3/docs/videos/list?hl=es

This is the base HTTP GET request URL for the Videos: list method. You will append parameters to this URL to specify your query.

```http
GET https://www.googleapis.com/youtube/v3/videos
```

--------------------------------

### Install Requests Library for Python

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Install the requests HTTP library for Python using pip. This library is commonly used for making HTTP requests in Python samples.

```bash
pip install --upgrade requests
```

--------------------------------

### Initialize YouTube API Client

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs.reports/list?hl=zh-cn

Configures the Google_Client with OAuth 2.0 credentials and handles token persistence. Requires a valid client_secrets_php.json file.

```php
$OUTPUT_FILE = (array_key_exists('outputFile', $options) ?
                $options['outputFile'] : '');

/*
 * You can obtain an OAuth 2.0 client ID and client secret from the
 * {{ Google Cloud Console }} <{{ https://cloud.google.com/console }}>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope(
      'https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);

    //fclose($fp);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}
```

--------------------------------

### Create and Configure YouTube Partner Assets

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=de

Initializes an asset resource with metadata and type, then inserts it into the YouTube Partner API.

```php
// Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];
```

--------------------------------

### Load Video with Existing iframe

Source: https://developers.google.com/youtube/js_api_reference?hl=ja

This example demonstrates how to use the API with an existing `<iframe>` element on the page.

```javascript
var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('existing-iframe-id', {
    events: {
      'onReady': onPlayerReady
    }
  });
}

function onPlayerReady(event) {
  event.target.playVideo();
}
```

--------------------------------

### Retrieve top 10 most started playlists in the U.S.

Source: https://developers.google.com/youtube/analytics/sample-requests

Lists the 10 most frequently started playlists in the U.S. Requires maxResults set to 10 or less and a sort parameter.

```text
dimensions=playlist
metrics=playlistStarts,views,estimatedMinutesWatched,averageViewDuration
filters=country==US
maxResults=10
sort=-playlistStarts
```

--------------------------------

### Curl GET Request with Authorization Header

Source: https://developers.google.com/youtube/v3/guides/auth/installed-apps

This curl command demonstrates making a GET request to the YouTube channels endpoint using the preferred Authorization header method.

```curl
curl -H "Authorization: Bearer access_token" https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true
```

--------------------------------

### Create and Configure YouTube Assets and Policies

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=id

Initializes an asset, sets ownership metadata, and defines a match policy for content tracking.

```php
$asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset in
    // Great Britain and Poland.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("include");
    $owners->setTerritories(array("PL","GB"));

    // Define the rights that the owner owns for the asset.
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId,
        $ownership, array('onBehalfOfContentOwner' => $contentOwnerId));

    $requiredTerritories = new Google_Service_YouTubePartner_TerritoryCondition();
    $requiredTerritories->setTerritories(array());
    $requiredTerritories->setType("exclude");

    // Create a "track" policy for the asset. The policy specifies the
    // conditions when the policy will be applied by defining a duration,
    // territories where the policy applies, and the type of content that an
    // uploaded video must match.
    $everywherePolicyCondition = new Google_Service_YouTubePartner_Conditions();
    $everywherePolicyCondition->setContentMatchType(array("video"));
    $everywherePolicyCondition->setRequiredTerritories($requiredTerritories);
    $everywherePolicyCondition->setReferenceDuration(array("low" => 10));

    // Create a policy rule and associate the conditions with the rule.
    $trackEverywhereRule = new Google_Service_YouTubePartner_PolicyRule();
    $trackEverywhereRule->setAction("track");
    $trackEverywhereRule->setConditions($everywherePolicyCondition);

    // Associate the policy rule with an assetMatchPolicy resource.
    $assetMatchPolicy = new Google_Service_YouTubePartner_AssetMatchPolicy();
    $assetMatchPolicy->setRules(array($trackEverywhereRule));


    // Update the asset's match policy
    $youtubePartner->assetMatchPolicy->update($assetId, $assetMatchPolicy,
        array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### Loading a Video Player

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

This snippet demonstrates how to initialize a YouTube player using the `onYouTubeIframeAPIReady` function and configure player options.

```APIDOC
## Loading a Video Player

After the API's JavaScript code loads, the API will call the `onYouTubeIframeAPIReady` function, at which point you can construct a `YT.Player` object to insert a video player on your page.

```javascript
var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: 'M7lc1UVf-VE',
    playerVars: {
      'playsinline': 1
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}
```

### Player Options

The `YT.Player` constructor accepts an object with the following properties:

- **`width`** (number) – The width of the video player. Default is `640`.
- **`height`** (number) – The height of the video player. Default is `390`.
- **`videoId`** (string) – The YouTube video ID.
- **`playerVars`** (object) – Player parameters for customization.
- **`events`** (object) – Event listeners for player events.
```

--------------------------------

### Create and Configure YouTube Partner Assets

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=de

Initializes an asset resource, sets metadata, and inserts it into the YouTube Partner API.

```php
$metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];
```

--------------------------------

### Access Token Response Example

Source: https://developers.google.com/youtube/v3/guides/auth/client-side-web-apps

This is an example of a successful OAuth 2.0 access token response, which includes the access token, token type, expiration time, and granted scopes.

```json
{
    "access_token": "1/fFAGRNJru1FTz70BzhT3Zg",
    "expires_in": 3920,
    "token_type": "Bearer",
    "scope": "https://www.googleapis.com/auth/youtube.force-ssl",
    "refresh_token": "1//xEoDL4iW3cxlI7yDbSRFYNG01kVKM2C-259HOF2aQbI"
  }
```

--------------------------------

### Initialize YouTube Reporting API Client in PHP

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/create

Sets up the Google Client with OAuth 2.0 credentials and scopes required for the YouTube Reporting API.

```php
<?php

/**
 * This sample creates a reporting job by:
 *
 * 1. Listing the available report types using the "reportTypes.list" method.
 * 2. Creating a reporting job using the "jobs.create" method.
 *
 * @author Ibrahim Ulukaya
 */

/**
 * Library Requirements
 *
 * 1. Install composer (https://getcomposer.org)
 * 2. On the command line, change to this directory (api-samples/php)
 * 3. Require the google/apiclient library
 *    $ composer require google/apiclient:~2.0
 */
if (!file_exists(__DIR__ . '/vendor/autoload.php')) {
  throw new \Exception('please run "composer require google/apiclient:~2.0" in "' . __DIR__ .'"');
}

require_once __DIR__ . '/vendor/autoload.php';
session_start();

/*
 * You can acquire an OAuth 2.0 client ID and client secret from the
 * {{ Google Cloud Console }} <{{ https://cloud.google.com/console }}>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
$OAUTH2_CLIENT_ID = 'REPLACE_ME';
$OAUTH2_CLIENT_SECRET = 'REPLACE_ME';

$client = new Google_Client();
$client->setClientId($OAUTH2_CLIENT_ID);
$client->setClientSecret($OAUTH2_CLIENT_SECRET);

/*
 * This OAuth 2.0 access scope allows for read access to the YouTube Analytics monetary reports for
 * authenticated user's account. Any request that retrieves earnings or ad performance metrics must
 * use this scope.
 */
$client->setScopes('https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
$redirect = filter_var('http://' . $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF'],
    FILTER_SANITIZE_URL);
$client->setRedirectUri($redirect);

// YouTube Reporting object used to make YouTube Reporting API requests.
$youtubeReporting = new Google_Service_YouTubeReporting($client);

// Check if an auth token exists for the required scopes
$tokenSessionKey = 'token-' . $client->prepareScopes();
if (isset($_GET['code'])) {
  if (strval($_SESSION['state']) !== strval($_GET['state'])) {
    die('The session state did not match.');
  }

  $client->authenticate($_GET['code']);
  $_SESSION[$tokenSessionKey] = $client->getAccessToken();
  header('Location: ' . $redirect);
}
```

--------------------------------

### Webapp2 Request Handler Setup

Source: https://developers.google.com/youtube/v3/code_samples/python_appengine

Sets up a basic webapp2 request handler to serve YouTube search results. Requires Jinja2 for templating and the `build` function from `apiclient.discovery`.

```python
import os
import urllib
import webapp2
import jinja2

from apiclient.discovery import build
from optparse import OptionParser

import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

REGISTRATION_INSTRUCTIONS = """
    You must set up a project and get an API key to run this code. Please see
    the instructions for creating a project and a key at <a
    href="https://developers.google.com/youtube/registering_an_application"
    >https://developers.google.com/youtube/registering_an_application</a>.
    <br><br>
    Make sure that you have enabled the YouTube Data API (v3) and the Freebase
    API for your project."

# Set API_KEY to the "API key" value from the Google Developers Console:
# https://console.developers.google.com/project/_/apiui/credential
# Please ensure that you have enabled the YouTube Data API and Freebase API

DEVELOPER_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class MainHandler(webapp2.RequestHandler):
   
   def get(self):
        if DEVELOPER_KEY == "REPLACE_ME":
          self.response.write("""You must set up a project and get an API key
                                 to run this project.  Please visit 
				 <landing page> to do so.""")
        else:
          youtube = build(
            YOUTUBE_API_SERVICE_NAME, 
            YOUTUBE_API_VERSION, 
            developerKey=DEVELOPER_KEY)
          search_response = youtube.search().list(
            q="Hello",
            part="id,snippet",
            maxResults=5
          ).execute()
        
          videos = []
          channels = []
          playlists = []
        
          for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("%s (%s)" % (search_result["snippet"]["title"], 
                  search_result["id"]["videoId"]))
            elif search_result["id"]["kind"] == "youtube#channel":
                channels.append("%s (%s)" % (search_result["snippet"]["title"], 
                  search_result["id"]["channelId"]))
            elif search_result["id"]["kind"] == "youtube#playlist":
                playlists.append("%s (%s)" % (search_result["snippet"]["title"], 
                  search_result["id"]["playlistId"]))
        
          template_values = {
           'videos': videos,
           'channels': channels,
           'playlists': playlists
          }
       
	  self.response.headers['Content-type'] = 'text/plain' 
          template = JINJA_ENVIRONMENT.get_template('index.html')
          self.response.write(template.render(template_values))
        
app = webapp2.WSGIApplication([
  ('/.*', MainHandler),
], debug=True)
```
```

--------------------------------

### Constructing API Requests

Source: https://developers.google.com/youtube/v3/sample_requests

Examples showing the abbreviated base URL format used in documentation versus the full URL required for actual requests.

```HTTP
GET {base-URL}/channels?part=contentDetails
                       &mine=true

```

```HTTP
GET https://www.googleapis.com/youtube/v3/channels?part=contentDetails
                                                  &mine=true

```

--------------------------------

### GET Live Chat Messages HTTP Request

Source: https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list?hl=es-419

Use this HTTP GET request to retrieve live chat messages for a specified chat. The API returns messages from oldest to newest.

```HTTP
GET https://www.googleapis.com/youtube/v3/liveChat/messages
```

--------------------------------

### HTTP GET Request with Authorization Header

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=fa

Use this method to make a GET request to the contentOwners.list endpoint with an access token in the Authorization header. Ensure your access token is correctly formatted.

```http
GET /youtubepartner/v1/contentOwners?fetchMine=true HTTP/1.1
Host: www.googleapis.com
**Authorization: Bearer access_token**
```

--------------------------------

### Initialize YouTube Reporting API Client

Source: https://developers.google.com/youtube/reporting/v1/reports

Sets up the YouTubeReporting service instance using OAuth 2.0 credentials and the required monetary reporting scope.

```java
List<String> scopes = Lists.newArrayList("https://www.googleapis.com/auth/yt-analytics-monetary.readonly");

try {
    // Authorize the request.
    Credential credential = Auth.authorize(scopes, "retrievereports");

    // This object is used to make YouTube Reporting API requests.
    youtubeReporting = new YouTubeReporting.Builder(Auth.HTTP_TRANSPORT, Auth.JSON_FACTORY, credential)
            .setApplicationName("youtube-cmdline-retrievereports-sample").build();
```

--------------------------------

### iOS App Store URL Example

Source: https://developers.google.com/youtube/reporting/guides/authorization/installed-apps?hl=de

This is an example of an Apple App Store URL, where the Store ID is the numerical string at the end of the URL. This ID is used to identify your app on the App Store.

```plaintext
https://apps.apple.com/app/google/id284815942
```

--------------------------------

### Playlist Reports - Playlist Metrics

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=ru

Retrieves playlist-specific metrics (playlist views, starts, estimated minutes watched, views per start) for playlists within the content owner's channels.

```APIDOC
## GET /api/reports/playlists

### Description
Retrieves total playlist starts, playlist estimated minutes watched, playlist views, and views per playlist start for playlists in the content owner's channels. The `playlistViews` metric counts only video views that occurred in the context of a playlist.

### Method
GET

### Endpoint
/api/reports/playlists

### Query Parameters
- **metrics** (string) - Required - Comma-separated list of playlist metrics to retrieve (e.g., playlistViews,playlistStarts,playlistEstimatedMinutesWatched,viewsPerPlaylistStart).

### Response
#### Success Response (200)
- **playlists** (array) - List of playlists with their associated metrics.

#### Response Example
{
  "playlists": [
    {
      "playlistId": "PLAYLIST_ID_1",
      "playlistViews": "50000",
      "playlistStarts": "10000",
      "playlistEstimatedMinutesWatched": "250000",
      "viewsPerPlaylistStart": "5"
    },
    {
      "playlistId": "PLAYLIST_ID_2",
      "playlistViews": "40000",
      "playlistStarts": "8000",
      "playlistEstimatedMinutesWatched": "200000",
      "viewsPerPlaylistStart": "5"
    }
  ]
}
```

--------------------------------

### Creating a YT.Player Object

Source: https://developers.google.com/youtube/iframe_api_reference?hl=zh-cn

Example demonstrating how to create a YT.Player object and associate it with an existing iframe element, including handling player readiness and state changes.

```APIDOC
## Example: Creating a YT.Player Object

### Example 1: Using the API with an Existing <iframe>

In this example, an `<iframe>` element on the page is defined to be used by the API. Note that the player's `src` URL must have the `enablejsapi` parameter set to `1`, or the `enablejsapi` attribute of the `<iframe>` element must be set to `true`.

When the player is ready, the `onPlayerReady` function changes the color of the border around the player to orange. The `onPlayerStateChange` function then changes the color of the border around the player based on the current player state (e.g., green when playing, red when paused, blue when buffering, and so on).

```html
<iframe id="player" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/VIDEO_ID?enablejsapi=1" frameborder="0"></iframe>

<script>
  var player;
  function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  }

  function onPlayerReady(event) {
    event.target.playVideo();
  }

  var done = false;
  function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
      setTimeout(stopVideo, 6000);
      done = true;
    }
  }
  function stopVideo() {
    player.stopVideo();
  }
</script>
```
```

--------------------------------

### HTTP GET Request for Live Broadcasts

Source: https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list

This is the base HTTP GET request to retrieve a list of YouTube live broadcasts. No specific parameters are shown here, but query parameters can be appended to filter the results.

```http
GET https://www.googleapis.com/youtube/v3/liveBroadcasts
```

--------------------------------

### Set up YouTube Partner API Flow

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example?hl=tr

Initializes the OAuth 2.0 flow for YouTube Partner API authentication. Ensure CLIENT_SECRETS is correctly configured.

```python
FLOW = flow_from_clientsecrets(CLIENT_SECRETS,
           scope='https://www.googleapis.com/auth/youtubepartner',
           message=MISSING_CLIENT_SECRETS_MESSAGE)
```

--------------------------------

### PlaylistItems: update - Update Item Position Example

Source: https://developers.google.com/youtube/v3/docs/playlistItems/update?hl=fr

This example demonstrates updating the position of an item within a playlist. The request requires 'id', 'snippet.playlistId', and 'snippet.resourceId' to identify the item, and modifies the 'snippet.position' property.

```json
{
  "id": "YOUR_PLAYLIST_ITEM_ID",
  "snippet": {
    "playlistId": "YOUR_PLAYLIST_ID",
    "position": 0,
    "resourceId": {
      "kind": "youtube#video",
      "videoId": "YOUR_VIDEO_ID"
    }
  }
}
```

--------------------------------

### Initialize and Use Google API Services in Python

Source: https://developers.google.com/youtube/reporting/guides/authorization/server-side-web-apps

Build the service object using the discovery library and execute API requests.

```python
from googleapiclient.discovery import build

youtube = build('youtubeAnalytics', 'v1', credentials=credentials)
```

```python
report = youtube.reports().query(ids='channel==MINE', start_date='2016-05-01', end_date='2016-06-30', metrics='views').execute()
```

--------------------------------

### Update Caption Track Example

Source: https://developers.google.com/youtube/v3/docs/captions/update?hl=de

This example demonstrates how to update a caption track. You must provide existing snippet values for videoId, language, and name. You can change the draft status and upload a new caption file.

```json
{
  "snippet": {
    "videoId": "VIDEO_ID",
    "language": "en",
    "name": "English",
    "isDraft": true
  }
}
```

--------------------------------

### Prepare Video Upload Request

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=pt-br

Sets up the video snippet with title, description, tags, category, and privacy status. This prepares the video resource for insertion.

```php
$snippet = new Google_Service_YouTube_VideoSnippet();
    $snippet->setTitle("Test title");
    $snippet->setDescription("Test description");
    $snippet->setTags(array("tag1", "tag2"));

    $snippet->setCategoryId("22");

    $status = new Google_Service_YouTube_VideoStatus();
    $status->privacyStatus = "public";

    $video = new Google_Service_YouTube_Video();
    $video->setSnippet($snippet);
    $video->setStatus($status);
```

--------------------------------

### Create and claim an asset

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=zh-cn

Demonstrates creating an asset, setting ownership, defining a monetization policy, and claiming a video.

```php
// Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId, $ownership,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    // Define a monetization policy for the asset.
    $policy = new Google_Service_YouTubePartner_Policy();
    $policyRule = new Google_Service_YouTubePartner_PolicyRule();
    $policyRule->setAction("monetize");
    $policy->setRules(array($policyRule));

    // Create a claim resource. Identify the video being claimed, the asset
    // that represents the claimed content, the type of content being claimed,
    // and the policy that you want to apply to the claimed video.
    $claim = new Google_Service_YouTubePartner_Claim();
    $claim->setAssetId($assetId);
    $claim->setVideoId($videoId);
    $claim->setPolicy($policy);
    $claim->setContentType("audiovisual");

    // Insert the created claim.
    $claimInsertResponse = $youtubePartner->claims->insert($claim,
        array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### Playlist View Counts and Watch Time by Playback Location

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=bn

Retrieves playlist view counts, watch time, and starts aggregated by the type of page or application where playbacks occurred. Results are sorted by playlist starts.

```APIDOC
## GET /analytics/v1/playlist_performance

### Description
This query retrieves the number of playlist views, playlist estimated watch time, and playlist starts for all playlists in a content owner's channels. Results are aggregated based on the type of page or application where video playbacks occurred, and results are sorted in descending order by playlist starts.

### Method
GET

### Endpoint
/analytics/v1/playlist_performance

### Parameters
#### Query Parameters
- **dimensions** (string) - Required - e.g., `insightPlaybackLocationType`
- **metrics** (string) - Required - e.g., `playlistViews,playlistEstimatedMinutesWatched,playlistStarts`
- **sort** (string) - Optional - e.g., `-playlistStarts`

### Request Example
```json
{
  "query": "dimensions=insightPlaybackLocationType&metrics=playlistViews,playlistEstimatedMinutesWatched,playlistStarts&sort=-playlistStarts"
}
```

### Response
#### Success Response (200)
- **playlistViews** (integer) - Number of playlist views.
- **playlistEstimatedMinutesWatched** (integer) - Estimated minutes watched for playlists.
- **playlistStarts** (integer) - Number of playlist starts.
- **insightPlaybackLocationType** (string) - The type of page or application where playback occurred.
```

--------------------------------

### Python Client Setup for Reporting API

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/reportTypes/list

Initializes the Python environment and imports necessary libraries for the YouTube Reporting API.

```python
#!/usr/bin/python

# Create a reporting job for the authenticated user's channel or
# for a content owner that the user's account is linked to.
# Usage example:
# python create_reporting_job.py --name='<name>'
# python create_reporting_job.py --content-owner='<CONTENT OWNER ID>'
# python create_reporting_job.py --content-owner='<CONTENT_OWNER_ID>' --report-type='<REPORT_TYPE_ID>' --name='<REPORT_NAME>'

import argparse
import os

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains

# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
```

--------------------------------

### Create Reporting Job with PHP Client Library

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/reportTypes/list?hl=bn

This sample demonstrates how to create a reporting job using the PHP client library. It first lists available report types and then creates a new job.

```php
<?php

/**
 * This sample creates a reporting job by:
 *
 * 1. Listing the available report types using the "reportTypes.list" method.
 * 2. Creating a reporting job using the "jobs.create" method.
 *
 * @author Ibrahim Ulukaya
 */

/**
 * Library Requirements
 *
 * 1. Install composer (https://getcomposer.org)
 * 2. On the command line, change to this directory (api-samples/php)
 * 3. Require the google/apiclient library
 *    $ composer require google/apiclient:~2.0
 */
if (!file_exists(__DIR__ . '/vendor/autoload.php')) {
  throw new \Exception('please run "composer require google/apiclient:~2.0" in "' . __DIR__ .'"');
}

require_once __DIR__ . '/vendor/autoload.php';
session_start();

/*
 * You can acquire an OAuth 2.0 client ID and client secret from the
 * {{ Google Cloud Console }} <{{ https://cloud.google.com/console }}>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
$OAUTH2_CLIENT_ID = 'REPLACE_ME';
$OAUTH2_CLIENT_SECRET = 'REPLACE_ME';

$client = new Google_Client();
$client->setClientId($OAUTH2_CLIENT_ID);
$client->setClientSecret($OAUTH2_CLIENT_SECRET);

/*
 * This OAuth 2.0 access scope allows for read access to the YouTube Analytics monetary reports for
 * authenticated user's account. Any request that retrieves earnings or ad performance metrics must
 * use this scope.
 */
$client->setScopes('https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
$redirect = filter_var('http://' . $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF'],
    FILTER_SANITIZE_URL);
$client->setRedirectUri($redirect);

// YouTube Reporting object used to make YouTube Reporting API requests.
$youtubeReporting = new Google_Service_YouTubeReporting($client);

// Check if an auth token exists for the required scopes
$tokenSessionKey = 'token-' . $client->prepareScopes();
if (isset($_GET['code'])) {
  if (strval($_SESSION['state']) !== strval($_GET['state'])) {
    die('The session state did not match.');
  }

  $client->authenticate($_GET['code']);
  $_SESSION[$tokenSessionKey] = $client->getAccessToken();

```

--------------------------------

### Statistics for a specific playlist

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=fa

Retrieves total playlist starts, estimated minutes watched, views, playlist views, and views per playlist start for a specific playlist. Can also retrieve aggregate statistics for multiple playlists.

```APIDOC
## GET /analytics/v1/playlistStatistics

### Description
Retrieves statistics for a specific playlist or multiple playlists.

### Method
GET

### Endpoint
/analytics/v1/playlistStatistics

### Query Parameters
- **metrics** (string) - Required - Comma-separated list of metrics to retrieve (e.g., `views,estimatedMinutesWatched,playlistStarts,playlistViews,viewsPerPlaylistStart`).
- **filters** (string) - Required - Filter criteria, typically `playlist==PLAYLIST_ID` or a comma-separated list of playlist IDs (up to 500).

### Request Example
```json
{
  "metrics": "views,estimatedMinutesWatched,playlistStarts,playlistViews,viewsPerPlaylistStart",
  "filters": "playlist==PLAYLIST_ID"
}
```

### Response
#### Success Response (200)
- **views** (integer) - Total views for the playlist.
- **estimatedMinutesWatched** (integer) - Estimated minutes watched for the playlist.
- **playlistStarts** (integer) - Total times the playlist was started.
- **playlistViews** (integer) - Total views within the playlist.
- **viewsPerPlaylistStart** (number) - Average views per playlist start.

#### Response Example
```json
{
  "rows": [
    [
      10000,
      50000,
      1000,
      12000,
      1.2
    ]
  ]
}
```
```

--------------------------------

### HTTP GET Request to YouTube Analytics API (Authorization Header)

Source: https://developers.google.com/youtube/reporting/guides/authorization/installed-apps

Use this method to make a GET request to the YouTube Analytics API, including the access token in the Authorization header. This is the preferred method over query parameters.

```http
GET /youtube/analytics/v1/reports?ids=channel%3D%3DMINE&start-date=2016-05-01&end-date=2016-06-30&metrics=views HTTP/1.1
Host: www.googleapis.com
**Authorization: Bearer access_token**
```

--------------------------------

### Main Execution Flow

Source: https://developers.google.com/youtube/partner/code_samples/python?hl=ar

Demonstrates the orchestration of asset management tasks including authentication, label creation, and asset updates.

```python
if __name__ == '__main__':
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )
  
  args = argparser.parse_args()

  youtube_partner = get_authenticated_service(args)

  content_owner_id = get_content_owner_id(youtube_partner)
  logging.info("Authenticated as CMS user ID '%s'." % content_owner_id)

  asset_label_name = create_asset_label(youtube_partner, content_owner_id, "label1");

  list_asset_labels(youtube_partner, content_owner_id)

  asset1 = create_asset(youtube_partner, content_owner_id, "asset1")
  logging.info("Created new asset ID '%s'." % asset1["id"])

  asset1 = update_asset(youtube_partner, content_owner_id, asset1, [asset_label_name, "label3"])
  logging.info("Added asset labels '%s %s' to '%s'." % (asset1["label"][0], asset1["label"][1], asset1["id"]))

  asset2 = create_asset(youtube_partner, content_owner_id, "asset2")
  logging.info("Created new asset ID '%s'." % asset2["id"])

  asset2 = update_asset(youtube_partner, content_owner_id, asset2, ["label3"])
  logging.info("Added asset label '%s' to '%s'." % (asset2["label"][0], asset2["id"]))

  list_asset_labels(youtube_partner, content_owner_id)

  # AssetSearch may not be able to return the expected results right away, as there is a delay
  # in indexing the assets with labels for the asset search after they are added.
  # Second run of the code sample after this delay will return the expected assets
  # of the previous run.

  search_asset(youtube_partner, content_owner_id, "label1, label3", None)

  search_asset(youtube_partner, content_owner_id, "label1, label3", True)

  logging.info("All done!")
```

--------------------------------

### GET /members

Source: https://developers.google.com/youtube/v3/docs/guideCategories

Lists members for a channel.

```APIDOC
## GET /members

### Description
Lists members (formerly known as "sponsors") for a channel. The API request must be authorized by the channel owner.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/members
```

--------------------------------

### Initiate Resumable Video Upload

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=bn

Prepares for a resumable upload of a reference video. It sets up the MediaFileUpload object with chunk size, file size, and the insert request. Requires the YouTube Partner Service, client object, asset ID, and reference video path.

```php
$chunkSizeBytes = 1 * 1024 * 1024;

    $client->setDefer(true);

    $reference = new Google_Service_YouTubePartner_Reference();
    $reference->setAssetId($assetId);
    $reference->setContentType("video");

    $insertRequest = $youtubePartner->references->insert($reference,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    $media = new Google_Http_MediaFileUpload(
        $client,
        $insertRequest,
        'video/*',
        null,
        true,
        $chunkSizeBytes
    );
    $media->setFileSize(filesize($referenceVideoPath));
```

--------------------------------

### Authentication and Client Initialization

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=th

This snippet demonstrates how to initialize the Google_Client, set authentication credentials, and obtain an access token for the YouTube Reporting API. It includes logic for handling existing credentials and requesting new authorization.

```APIDOC
## Authentication and Client Initialization

### Description
This section details the process of setting up authentication for the YouTube Reporting API using OAuth 2.0. It covers obtaining client credentials, configuring the Google Client, and managing access tokens, including refreshing expired tokens.

### Method
N/A (Client-side setup)

### Endpoint
N/A

### Parameters
N/A

### Request Example
```php
// Example of client initialization (not a direct API call)
$client = getClient();
```

### Response
N/A (Returns a configured Google_Client object)
```

--------------------------------

### Get and Set Module Options

Source: https://developers.google.com/youtube/iframe_api_reference

Commands to retrieve or update specific settings for a given module.

```javascript
player.getOption(module, option);
```

```javascript
player.setOption(module, option, value);
```

--------------------------------

### Example: Retrieve regions with Spanish (Mexico) language preference

Source: https://developers.google.com/youtube/v3/docs/i18nRegions/list

This example demonstrates how to retrieve a list of content regions, specifying the 'es_MX' language for the response text values using the 'hl' parameter. The default value for 'hl' is 'en_US'.

```HTTP
GET https://www.googleapis.com/youtube/v3/i18nRegions?hl=es_MX
```

--------------------------------

### Initialize OAuth2 Client and Scopes

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps?hl=ar

Sets up the OAuth2 client with your application's credentials and defines the necessary API access scopes. Ensure you replace placeholder values with your actual credentials.

```javascript
const http = require('http');
const https = require('https');
const url = require('url');
const { google } = require('googleapis');
const crypto = require('crypto');
const express = require('express');
const session = require('express-session');

/**
 * To use OAuth2 authentication, we need access to a CLIENT_ID, CLIENT_SECRET, AND REDIRECT_URI.
 * To get these credentials for your application, visit
 * https://console.cloud.google.com/apis/credentials.
 */
const oauth2Client = new google.auth.OAuth2(
  YOUR_CLIENT_ID,
  YOUR_CLIENT_SECRET,
  YOUR_REDIRECT_URL
);

// Access scopes for YouTube API
const scopes = [
  'https://www.googleapis.com/auth/youtube.force-ssl'
];

/* Global variable that stores user credential in this code example.
 * ACTION ITEM for developers:
 *   Store user's refresh token in your data store if
 *   incorporating this code into your real app.
 *   For more information on handling refresh tokens,
 *   see https://github.com/googleapis/google-api-nodejs-client#handling-refresh-tokens
 */
let userCredential = null;
```

--------------------------------

### Initialize OAuth2 Client and Define Scopes

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=es

Set up the OAuth2 client with your application's credentials and define the API scopes required for authentication. Ensure you replace placeholders with your actual client ID, client secret, and redirect URL.

```javascript
const http = require('http');
const https = require('https');
const url = require('url');
const { google } = require('googleapis');
const crypto = require('crypto');
const express = require('express');
const session = require('express-session');

/**
 * To use OAuth2 authentication, we need access to a CLIENT_ID, CLIENT_SECRET, AND REDIRECT_URI.
 * To get these credentials for your application, visit
 * https://console.cloud.google.com/apis/credentials.
 */
const oauth2Client = new google.auth.OAuth2(
  YOUR_CLIENT_ID,
  YOUR_CLIENT_SECRET,
  YOUR_REDIRECT_URL
);

// Access scopes for two non-Sign-In scopes: Read-only Drive activity and Google Calendar.
const scopes = [
  'https://www.googleapis.com/auth/youtubepartner',
  'https://www.googleapis.com/auth/calendar.readonly'
];

/* Global variable that stores user credential in this code example.
 * ACTION ITEM for developers:
 *   Store user's refresh token in your data store if
 *   incorporating this code into your real app.
 *   For more information on handling refresh tokens, 
 *   see https://github.com/googleapis/google-api-nodejs-client#handling-refresh-tokens
 */
let userCredential = null;
```

--------------------------------

### Daily playlist views for a content owner

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=fa

Retrieves metrics for daily user interactions with videos in the content owner's playlists, including playlist views, starts, estimated minutes watched, and views per playlist start.

```APIDOC
## GET /analytics/v1/playlistReports/dailyViews

### Description
Retrieves daily playlist views and related in-playlist metrics for a content owner.

### Method
GET

### Endpoint
/analytics/v1/playlistReports/dailyViews

### Query Parameters
- **dimensions** (string) - Required - `day`.
- **metrics** (string) - Required - Comma-separated list of in-playlist metrics (e.g., `playlistViews,playlistStarts,playlistEstimatedMinutesWatched,viewsPerPlaylistStart`).
- **sort** (string) - Required - `day`.

### Request Example
```json
{
  "dimensions": "day",
  "metrics": "playlistViews,playlistStarts,playlistEstimatedMinutesWatched,viewsPerPlaylistStart",
  "sort": "day"
}
```

### Response
#### Success Response (200)
- **day** (date) - The date of the report.
- **playlistViews** (integer) - Total views within playlists.
- **playlistStarts** (integer) - Total times playlists were started.
- **playlistEstimatedMinutesWatched** (integer) - Estimated minutes watched within playlists.
- **viewsPerPlaylistStart** (number) - Average views per playlist start.

#### Response Example
```json
{
  "rows": [
    [
      "2023-10-26",
      8000,
      800,
      40000,
      1.1
    ]
  ]
}
```
```

--------------------------------

### Configure OAuth 2.0 client with Ruby

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Initialize a client using a JSON secrets file, define required scopes, and set up a token store for persistent access.

```ruby
require 'googleauth'
require 'googleauth/web_user_authorizer'
require 'googleauth/stores/redis_token_store'

require 'google/apis/youtubePartner_v1'
require 'google/apis/calendar_v3'

# Required, call the from_file method to retrieve the client ID from a
# client_secret.json file.
client_id = Google::Auth::ClientId.from_file('/path/to/client_secret.json')

# Required, scope value 
# Access scopes for two non-Sign-In scopes: Read-only Drive activity and Google Calendar.
scope = ['Google::Apis::DriveV3::AUTH_DRIVE_METADATA_READONLY',
         'Google::Apis::CalendarV3::AUTH_CALENDAR_READONLY']

# Required, Authorizers require a storage instance to manage long term persistence of
# access and refresh tokens.
token_store = Google::Auth::Stores::RedisTokenStore.new(redis: Redis.new)

# Required, indicate where the API server will redirect the user after the user completes
# the authorization flow. The redirect URI is required. The value must exactly
# match one of the authorized redirect URIs for the OAuth 2.0 client, which you
# configured in the API Console. If this value doesn't match an authorized URI,
# you will get a 'redirect_uri_mismatch' error.
callback_uri = '/oauth2callback'

# To use OAuth2 authentication, we need access to a CLIENT_ID, CLIENT_SECRET, AND REDIRECT_URI
# from the client_secret.json file. To get these credentials for your application, visit
```

--------------------------------

### GET /liveStreams

Source: https://developers.google.com/youtube/v3/live/docs

Retrieves a list of video streams.

```APIDOC
## GET /liveStreams

### Description
Returns a list of video streams that match the API request parameters.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/liveStreams
```

--------------------------------

### Upload, Claim, and Monetize Video (PHP)

Source: https://developers.google.com/youtube/partner/code_samples/php

This PHP sample demonstrates how to upload a YouTube video, claim it using an asset, and apply monetization policies. It requires OAuth 2.0 authentication and the YouTube Data and Partner APIs. Ensure the YouTube Data API is enabled for your project.

```php
<?php

/**
 * This sample uploads, claims and monetizes a video by :
 *
 * 1. Finding the content owner ID via "youtubePartner.contentOwners.listContentOwners" method
 * 2. Uploading the video via "youtube.videos.insert" with utilizing "Google_MediaFileUpload"
 * 3. Creating an asset via "youtubePartner.assets.insert" method
 * 4. Creating ownership on the asset via "youtubePartner.ownership.update" method
 * 5. Claiming the video with the asset and a policy via "youtubePartner.claims.insert"
 * 6. Enabling the TrueView advertising on the video via "youtubePartner.videoAdvertisingOptions.update"
 *
 * @author Ibrahim Ulukaya
*/


// Call set_include_path() as needed to point to your client library.
require_once 'Google/Client.php';
require_once 'Google/Service/YouTube.php';
require_once 'Google/Service/YouTubePartner.php';
session_start();

/*
 * You can acquire an OAuth 2.0 client ID and client secret from the
 * Google API Console <https://console.cloud.google.com/>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
$OAUTH2_CLIENT_ID = 'REPLACE ME';
$OAUTH2_CLIENT_SECRET = 'REPLACE ME';

$client = new Google_Client();
$client->setClientId($OAUTH2_CLIENT_ID);
$client->setClientSecret($OAUTH2_CLIENT_SECRET);
$client->setScopes('https://www.googleapis.com/auth/youtubepartner');
$redirect = filter_var('http://' . $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF'],
    FILTER_SANITIZE_URL);
$client->setRedirectUri($redirect);

// Define an object that will be used to make all API requests.
$youtube = new Google_Service_YouTube($client);

// YouTube Partner object used to make Content ID API requests.
$youtubePartner = new Google_Service_YouTubePartner($client);

if (isset($_GET['code'])) {
  if (strval($_SESSION['state']) !== strval($_GET['state'])) {
    die('The session state did not match.');
  }

  $client->authenticate($_GET['code']);
  $_SESSION['token'] = $client->getAccessToken();
  header('Location: ' . $redirect);
}

if (isset($_SESSION['token'])) {
  $client->setAccessToken($_SESSION['token']);
}

// Check to ensure that the access token was successfully acquired.
if ($client->getAccessToken()) {
  try{

    // Call the contentOwners.list method to retrieve the ID of the content
    // owner associated with the currently authenticated user's account.

```

--------------------------------

### GET /channels

Source: https://developers.google.com/youtube/v3/code_samples/code_snippets

Retrieves information about YouTube channels.

```APIDOC
## GET /channels

### Description
Retrieves information about one or more YouTube channels. You can identify channels by their ID, username, or handle.

### Method
GET

### Endpoint
/channels

### Query Parameters
- **id** (string) - Optional - The ID of the channel(s) to retrieve.
- **forHandle** (string) - Optional - Retrieves the channel associated with the given YouTube Handle.
- **forUsername** (string) - Optional - Retrieves the channel associated with the given YouTube username.
- **mine** (boolean) - Optional - Indicates that the API should only return channels owned by the user authorizing the request.
- **part** (string) - Optional - Specifies the parts of the channel resource that should be included in the response.

### Request Example
```json
{
  "example": "GET /channels?id=UC_x5XG1OV2P6uZZ5FSM9Ttw"
}
```

### Response
#### Success Response (200)
- **items** (array) - A list of channel resources.

#### Response Example
{
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "example_etag",
      "id": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
      "snippet": {
        "title": "Google Developers",
        "description": "The official YouTube channel for Google Developers.",
        "customUrl": "@GoogleDevelopers"
      },
      "statistics": {
        "viewCount": "1000000",
        "subscriberCount": "500000",
        "videoCount": "1000"
      }
    }
  ]
}
```

--------------------------------

### Initialize Flask app and API service details

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=de

Initialize a Flask application and define constants for the YouTube Partner API service name and version. A secret key is required for Flask applications.

```python
API_SERVICE_NAME = 'youtubePartner'
API_VERSION = 'v1'

app = flask.Flask(__name__)
# Note: A secret key is included in the sample so that it works.
# If you use this code in your application, replace this with a truly secret
```

--------------------------------

### Load Video Player with Iframe Tag

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

Example demonstrating how to manually create an `<iframe>` tag to load the YouTube player. Ensure the closing `</iframe>` tag is present for `onYouTubeIframeAPIReady` to be called.

```html
<iframe id="player" type="text/html" width="640" height="360" src="http://www.youtube.com/embed/VIDEO_ID?enablejsapi=1&version=3" frameborder="0" allowfullscreen></iframe>
```

--------------------------------

### GET /jobs

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=vi

Retrieves a list of reporting jobs.

```APIDOC
## GET /jobs

### Description
Retrieves a list of reporting jobs.

### Method
GET

### Endpoint
/jobs
```

--------------------------------

### GET /musicReleases

Source: https://developers.google.com/youtube/partner/reference/rest/v1/musicReleases

Retrieves a list of music releases.

```APIDOC
## GET /musicReleases

### Description
Retrieves a list of music releases.

### Method
GET

### Endpoint
/musicReleases

### Parameters
#### Query Parameters
- **pageSize** (integer) - Optional - The maximum number of music releases to return.
- **pageToken** (string) - Optional - A page token, received from a previous `list` call.

### Response
#### Success Response (200)
- **musicReleases** (array) - A list of music releases.
  - **name** (string) - The resource name of the music release. Format: releases/{release}
  - **title** (string) - The title of this release.
  - **artists** (array) - List of artists for the release. Each artist object contains:
    - **name** (string) - The resource name of the artist. Format: artists/{artist}
    - **displayName** (string) - The display name of the artist.
  - **playlistId** (string) - The OMV-preferred playlist.
  - **hasOpenChangeRequest** (boolean) - The release has at least one ChangeRequest in open status.

#### Response Example
```json
{
  "musicReleases": [
    {
      "name": "releases/12345",
      "title": "Example Album Title",
      "artists": [
        {
          "name": "artists/67890",
          "displayName": "Example Artist"
        }
      ],
      "playlistId": "PLabcdef12345",
      "hasOpenChangeRequest": false
    }
  ],
  "nextPageToken": "CAUQAA"
}
```
```

--------------------------------

### Initialize OAuth2 flow and storage

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example

Sets up the authentication flow and manages credential storage using a local file.

```python
  # Set up a Flow object to be used if we need to authenticate.
  FLOW = flow_from_clientsecrets('client_secrets.json',
      scope='https://www.googleapis.com/auth/youtubepartner',
      message='error message')

  # The Storage object stores the credentials. If it doesn't exist, or if
  # the credentials are invalid or expired, run through the native client flow.
  storage = Storage('yt_partner_api.dat')
  credentials = storage.get()
  
  if (credentials is None or credentials.invalid or
      credentials.token_expiry <= datetime.now()):
    credentials = run(FLOW, storage)
```

--------------------------------

### Create Reference Resource for Upload

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=ru

Creates a reference resource, linking it to the asset ID and specifying the content type as 'video'. This prepares the API for uploading the actual reference video.

```php
// Create a reference resource. Set the asset ID associated with the
    // reference, and identify the type of reference content being uploaded.
    $reference = new Google_Service_YouTubePartner_Reference();
    $reference->setAssetId($assetId);
    $reference->setContentType("video");

    // Create a request for the API's references.insert method to insert the reference resource
    // while uploading the reference video.
    $insertRequest = $youtubePartner->references->insert($reference,
        array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### GET /claims

Source: https://developers.google.com/youtube/partner/reference/errors

Retrieves details for a specific claim.

```APIDOC
## GET /claims

### Description
Retrieves a specific claim by ID.

### Method
GET

### Parameters
#### Query Parameters
- **claimId** (string) - Required - The ID of the claim.

### Response
#### Error Handling
- **notFound (404)**: The claim cannot be found.
```

--------------------------------

### GET /claimHistory

Source: https://developers.google.com/youtube/partner/reference/errors

Retrieves the history of a specific claim.

```APIDOC
## GET /claimHistory

### Description
Retrieves the history for a specific claim.

### Method
GET

### Parameters
#### Query Parameters
- **claimId** (string) - Required - The ID of the claim.

### Response
#### Error Handling
- **notFound (404)**: The claim cannot be found.
- **required (400)**: The request does not specify a value for the required claimId parameter.
```

--------------------------------

### Set Access Token and Call YouTube API in PHP

Source: https://developers.google.com/youtube/v3/live/guides/auth/server-side-web-apps

Configures a Google Client with an access token and initializes the YouTube Data API service to list broadcasts.

```PHP
$client->setAccessToken($access_token);
```

```PHP
$youtube = new Google_Service_YouTube($client);
```

```PHP
$broadcasts = $youtube->liveBroadcasts->listLiveBroadcasts('id,snippet', [ 'mine' => true ]);
```

--------------------------------

### GET /campaigns

Source: https://developers.google.com/youtube/partner/reference/errors

Retrieves details for a specific campaign.

```APIDOC
## GET /campaigns

### Description
Retrieves a campaign by its ID.

### Method
GET

### Parameters
#### Query Parameters
- **resource_id** (string) - Required - The ID of the campaign to retrieve.

### Response
#### Error Handling
- **notFound (404)**: The campaign cannot be found.
- **required (400)**: The request does not specify a campaign ID.
```

--------------------------------

### Initialize OAuth 2.0 Flow and Storage

Source: https://developers.google.com/youtube/partner/first_request?hl=ja

Sets up the OAuth 2.0 flow using client secrets and defines a storage object for credentials. Ensure 'client_secrets.json' exists and 'yt_partner_api.dat' is accessible.

```python
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import Storage

# Set up a Flow object to be used if we need to authenticate.
FLOW = flow_from_clientsecrets('client_secrets.json',
    scope='https://www.googleapis.com/auth/youtubepartner',
    message='error message')

# The Storage object stores the credentials. If the credentials are invalid
# or expired and the script isn't working, delete the file specified below
# and run the script again.
storage = Storage('yt_partner_api.dat')
credentials = storage.get()
```

--------------------------------

### Initialize YT.Player with custom volume

Source: https://developers.google.com/youtube/iframe_api_reference

Creates a player with specific dimensions and sets the volume to maximum upon the onReady event.

```javascript
function onYouTubeIframeAPIReady() {
  var player;
  player = new YT.Player('player', {
    width: 1280,
    height: 720,
    videoId: 'M7lc1UVf-VE',
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange,
      'onError': onPlayerError
    }
  });
}

function onPlayerReady(event) {
  event.target.setVolume(100);
  event.target.playVideo();
}
```

--------------------------------

### GET /assets

Source: https://developers.google.com/youtube/partner/reference/errors

Errors related to listing assets.

```APIDOC
## GET /assets

### Description
Errors returned when listing assets.

### Parameters
#### Query Parameters
- **id** (string) - Optional - The list of asset IDs to retrieve. Limit is 50 IDs per request.

### Response
#### Error Responses
- **400 (invalidValue)** - The number of asset IDs provided exceeds the limit of 50.
```

--------------------------------

### Prepare for Resumable Video Upload

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=zh-tw

Configures the client and creates a reference resource for uploading a video. Sets chunk size for resumable uploads and defers the API call.

```php
$chunkSizeBytes = 1 * 1024 * 1024;

    $client->setDefer(true);
```

```php
$reference = new Google_Service_YouTubePartner_Reference();
    $reference->setAssetId($assetId);
    $reference->setContentType("video");
```

```php
$insertRequest = $youtubePartner->references->insert($reference,
        array('onBehalfOfContentOwner' => $contentOwnerId));
```

```php
$media = new Google_Http_MediaFileUpload(
        $client,
        $insertRequest,
        'video/*',
        null,
        true,
        $chunkSizeBytes
    );
    $media->setFileSize(filesize($referenceVideoPath));
```

--------------------------------

### Statistics for a specific playlist

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=ru

Retrieves total playlist starts, estimated minutes watched, views, playlist views, and views per playlist start for a specific playlist. Can accept a single playlist ID or a comma-separated list of up to 500 playlist IDs.

```APIDOC
## GET /analytics/v1/playlist/statistics

### Description
Retrieves statistics for a specific playlist or multiple playlists.

### Method
GET

### Endpoint
/analytics/v1/playlist/statistics

### Query Parameters
- **metrics** (string) - Required - Comma-separated list of metrics to retrieve (e.g., views,estimatedMinutesWatched,playlistStarts,playlistViews,viewsPerPlaylistStart).
- **filters** (string) - Required - Filter criteria, typically 'playlist==PLAYLIST_ID' or 'playlist==ID1,ID2,...'.

### Request Example
```json
{
  "metrics": "views,estimatedMinutesWatched,playlistStarts,playlistViews,viewsPerPlaylistStart",
  "filters": "playlist==PLAYLIST_ID"
}
```

### Response
#### Success Response (200)
- **rows** (array) - Contains the requested metrics for the specified playlist(s).

#### Response Example
```json
{
  "kind": "youtubeAnalytics#resultTable",
  "columnHeaders": [
    {
      "name": "playlist",
      "columnType": "DIMENSION"
    },
    {
      "name": "views",
      "columnType": "METRIC"
    }
  ],
  "rows": [
    ["PLabcdef12345", 15000]
  ]
}
```
```

--------------------------------

### Execute Python Sample Script

Source: https://developers.google.com/youtube/analytics/reference/reports/query

Run the YouTube Analytics API sample script from the terminal.

```bash
python yt_analytics_v2.py
```

--------------------------------

### Main Execution Flow

Source: https://developers.google.com/youtube/partner/guides/upload?hl=fr

Orchestrates the authentication, upload, asset creation, ownership, claiming, and ad configuration process.

```python
if __name__ == '__main__':
  logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
  )

  options = parse_options()

  if options.file is None or not os.path.exists(options.file):
    logging.error("Please specify a valid file using the --file= parameter.")
    exit(1)

  # The channel ID looks something like "UC..." and needs to correspond to a
  # channel managed by the YouTube content owner authorizing the request.
  # youtube.channels.list(part="snippet", managedByMe=true,
  #                       onBehalfOfContentOwner=*CONTENT_OWNER_ID*)
  # can be used to retrieve a list of managed channels and their channel IDs.
  # See https://developers.google.com/youtube/v3/docs/channels/list
  if options.channelId is None:
    logging.error("Please specify a channel ID via the --channelId= parameter.")
    exit(1)

  (youtube, youtube_partner) = get_authenticated_services()

  content_owner_id = get_content_owner_id(youtube_partner)
  logging.info("Authorized by content owner ID '%s'." % content_owner_id)

  (video_id, duration_seconds) = upload(youtube, content_owner_id, options)
  logging.info("Successfully uploaded video ID '%s'." % video_id)

  file_size_bytes = os.path.getsize(options.file)
  logging.debug("Uploaded %d bytes in %0.2f seconds (%0.2f megabytes/second)." %
    (file_size_bytes, duration_seconds,
      (file_size_bytes / (1024 * 1024)) / duration_seconds))

  asset_id = create_asset(youtube_partner, content_owner_id,
    options.title, options.description)
  logging.info("Created new asset ID '%s'." % asset_id)

  set_asset_ownership(youtube_partner, content_owner_id, asset_id)
  logging.info("Successfully set asset ownership.")

  claim_id = claim_video(youtube_partner, content_owner_id, asset_id,
    video_id, options.policyId)
  logging.info("Successfully claimed video.")

  set_advertising_options(youtube_partner, content_owner_id, video_id)
  logging.info("Successfully set advertising options.")

  logging.info("All done!")
```

--------------------------------

### Contoh HTTP GET dengan Parameter access_token

Source: https://developers.google.com/youtube/v3/live/guides/auth/devices?hl=id

Alternatif untuk otentikasi, gunakan parameter kueri 'access_token' dalam permintaan GET ke YouTube Live Streaming API. Ganti 'access_token' dengan token Anda yang valid.

```http
GET https://www.googleapis.com/youtube/v3/liveBroadcasts?access_token=access_token&part=id%2Csnippet&mine=true
```

--------------------------------

### HTTP GET Request to YouTube Analytics API (Access Token Query Parameter)

Source: https://developers.google.com/youtube/reporting/guides/authorization/installed-apps

This method makes a GET request to the YouTube Analytics API, including the access token as a query string parameter. This is less preferred than using the Authorization header.

```http
GET https://www.googleapis.com/youtube/analytics/v1/reports?access_token=access_token&ids=channel%3D%3DMINE&start-date=2016-05-01&end-date=2016-06-30&metrics=views
```

--------------------------------

### Upload a Video to YouTube in Go

Source: https://developers.google.com/youtube/v3/code_samples/go

Uploads a video file to YouTube. This sample requires the video file path and uses the `Videos.Insert` method with appropriate parameters.

```Go
package main

import (
	"context"
	"flag"
	"log"
	"os"

	"google.golang.org/api/option"
	"google.golang.org/api/youtube/v3"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/google"
)

var (
	videoFilePath = flag.String("file", "", "Path to the video file to upload.")
)

func main() {
	flag.Parse()

	if *videoFilePath == "" {
		log.Fatal("You must provide a video file path.")
	}

	ctx := context.Background()

	// TODO: Use a more robust method for loading client secrets.
	data := []byte(`{
  "installed": {
    "client_id": "YOUR_CLIENT_ID",
    "project_id": "YOUR_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "YOUR_CLIENT_SECRET",
    "redirect_uris": [
      "http://localhost"
    ]
  }
}`)

	config, err := google.ConfigFromJSON(ctx, data, youtube.UploadScope)
	if err != nil {
		log.Fatalf("Unable to parse client secret file: %v", err)
	}

	client := getClient(ctx, config)

	service, err := youtube.NewService(ctx, option.WithHTTPClient(client))
	if err != nil {
		log.Fatalf("Error creating YouTube client: %v", err)
	}

	video := &youtube.Video{
		Snippet: &youtube.VideoSnippet{
			Title:       "test upload",
			Description: "test upload description",
		},
		Status: &youtube.VideoStatus{
			PrivacyStatus: "private", // or "public", "unlisted"
		},
	}

	file, err := os.Open(*videoFilePath)
	if err != nil {
		log.Fatalf("Error opening video file: %v", err)
	}

	defer file.Close()

	call := service.Videos.Insert([]string{"snippet,status"}, video)
	response, err := call.Media(file, "video/*").Do()
	if err != nil {
		log.Fatalf("Error making API call to upload video: %v", err)
	}

	log.Printf("Upload successful! Video ID: %s\n", response.Id)
}

// getClient obtains an authenticated HTTP client.
func getClient(ctx context.Context, config *oauth2.Config) *http.Client {
	// TODO: Implement token retrieval and refresh logic.
	return &http.Client{}
}

```

--------------------------------

### Initialize OAuth 2.0 Client

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs.reports/list?hl=ja

Configures the Google_Client with credentials and scopes. Requires a valid client_secrets_php.json file.

```php
$INCLUDE_SYSTEM_MANAGED = (array_key_exists('includeSystemManaged', $options) ?
                           $options['includeSystemManaged'] : '');
$JOB_ID = (array_key_exists('jobId', $options) ? $options['jobId'] : '');
$OUTPUT_FILE = (array_key_exists('outputFile', $options) ?
                $options['outputFile'] : '');

/*
 * You can obtain an OAuth 2.0 client ID and client secret from the
 * {{ Google Cloud Console }} <{{ https://cloud.google.com/console }}>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope(
      'https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);

    //fclose($fp);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}

/**
 * Expands the home directory alias '~' to the full path.
 * @param string $path the path to expand.
 * @return string the expanded path.
 */
function expandHomeDirectory($path) {
  $homeDirectory = getenv('HOME');
  if (empty($homeDirectory)) {
    $homeDirectory = getenv('HOMEDRIVE') . getenv('HOMEPATH');
  }
  return str_replace('~', realpath($homeDirectory), $path);
}
```

--------------------------------

### ChannelSections Update Request Body Example

Source: https://developers.google.com/youtube/v3/docs/channelSections/update?hl=bn

This example demonstrates the structure of a request body for updating a channel section. You must specify 'snippet.type' and can optionally set 'snippet.title', 'snippet.position', 'contentDetails.playlists', or 'contentDetails.channels'. Omitting a property in an update request will delete its existing value.

```json
{
  "snippet": {
    "type": "singlePlaylists",
    "title": "My Playlist Section",
    "position": 1
  },
  "contentDetails": {
    "playlists": [
      "PL_abcdefg12345"
    ]
  }
}
```

--------------------------------

### GET /captions.download

Source: https://developers.google.com/youtube/v3/guides/implementation/captions

Downloads a specific caption track by ID.

```APIDOC
## GET /captions.download

### Description
Downloads a specific caption track. Requires OAuth 2.0 authorization.

### Method
GET

### Parameters
#### Query Parameters
- **id** (string) - Required - The YouTube caption track ID.
- **tfmt** (string) - Optional - Specifies the desired format for the returned caption track.
- **tlang** (string) - Optional - ISO 639-1 two-letter language code to retrieve a machine-translated version of the caption track.
```

--------------------------------

### Initialize OAuth 2.0 Client and Credentials

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=es

Configures the Google API client with OAuth 2.0 scopes and handles token persistence to the local filesystem.

```php
require_once __DIR__ . '/vendor/autoload.php';
session_start();


define('CREDENTIALS_PATH', '~/.credentials/youtube-php.json');

$longOptions = array(
  'contentOwner::',
  'downloadUrl::',
  'includeSystemManaged::',
  'jobId::',
  'outputFile::',
);

$options = getopt('', $longOptions);

$CONTENT_OWNER_ID = ($options['contentOwner'] ? $options['contentOwner'] : '');
$DOWNLOAD_URL = (array_key_exists('downloadUrl', $options) ?
                 $options['downloadUrl'] : '');
$INCLUDE_SYSTEM_MANAGED = (array_key_exists('includeSystemManaged', $options) ?
                           $options['includeSystemManaged'] : '');
$JOB_ID = (array_key_exists('jobId', $options) ? $options['jobId'] : '');
$OUTPUT_FILE = (array_key_exists('outputFile', $options) ?
                $options['outputFile'] : '');

/*
 * You can obtain an OAuth 2.0 client ID and client secret from the
 * {{ Google Cloud Console }} <{{ https://cloud.google.com/console }}>
 * For more information about using OAuth 2.0 to access Google APIs, please see:
 * <https://developers.google.com/youtube/v3/guides/authentication>
 * Please ensure that you have enabled the YouTube Data API for your project.
 */
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope(
      'https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);

    //fclose($fp);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}

/**
 * Expands the home directory alias '~' to the full path.
 * @param string $path the path to expand.
 * @return string the expanded path.
 */
function expandHomeDirectory($path) {
  $homeDirectory = getenv('HOME');
  if (empty($homeDirectory)) {
    $homeDirectory = getenv('HOMEDRIVE') . getenv('HOMEPATH');
  }
  return str_replace('~', realpath($homeDirectory), $path);
}
```

--------------------------------

### Claim Video and Create Reference

Source: https://developers.google.com/youtube/partner/guides/migration_xml_to_api

Claims a video for an asset and creates a reference for content matching.

```python
   # Claim the video
   body = {'assetId': asset_id,
           'videoId': video_id,
           'policy': monetize_policy,
           'contentType': 'audiovisual'}
   kwargs = {'body': body}
   claim_video = executeOperation(partnerApi, 'claims', 'insert', **kwargs)
   claim_id = claim_video['id']
   print 'claim ID is ' + claim_id

   # Create the reference
   body = {'assetId': asset_id,
           'videoId': video_id,
           'contentType': 'audiovisual'}
   kwargs = {'claimId': claim_id, 'body': body}
   create_reference = executeOperation(partnerApi, 'references', 'insert',
                                       **kwargs)
```

--------------------------------

### GET /youtube/v3/channels

Source: https://developers.google.com/youtube/v3/guides/auth/devices

Retrieves channel information for the authenticated user.

```APIDOC
## GET /youtube/v3/channels

### Description
Retrieves a list of channels for the authenticated user.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/channels

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more resource properties that the API response will include.
- **mine** (boolean) - Optional - Set to true to retrieve the authenticated user's channels.
- **access_token** (string) - Optional - The access token for authentication if not using the Authorization header.

### Request Example
GET /youtube/v3/channels?part=snippet&mine=true HTTP/1.1
Host: www.googleapis.com
Authorization: Bearer access_token
```

--------------------------------

### GET /playlists.list

Source: https://developers.google.com/youtube/v3/docs/errors

Details the error conditions for listing playlists.

```APIDOC
## GET playlists.list

### Description
Retrieves a list of playlists. Returns errors if the channel is closed/suspended or the playlist is inaccessible.

### Method
GET

### Endpoint
playlists.list

### Error Handling
- **forbidden (403)**: channelClosed - Channel is closed.
- **forbidden (403)**: channelSuspended - Channel is suspended.
- **forbidden (403)**: playlistForbidden - Request not authorized or unsupported.
- **notFound (404)**: channelNotFound - Channel not found.
- **notFound (404)**: playlistNotFound - Playlist not found.
- **invalidValue (400)**: playlistOperationUnsupported - Operation not supported for this playlist.
```

--------------------------------

### GET /channels

Source: https://developers.google.com/youtube/v3/docs/errors

Error handling documentation for the channels.list method.

```APIDOC
## GET channels.list

### Description
Returns error messages associated with the channels.list method.

### Method
GET

### Endpoint
channels.list

### Response
#### Error Responses
- **badRequest (400)**: invalidCriteria - A maximum of one of the following filters may be specified: id, mySubscribers, categoryId, mine, managedByMe, forUsername. In case of content owner authentication using the onBehalfOfContentOwner parameter, only the id or managedByMe may be specified.
- **forbidden (403)**: channelForbidden - The channel specified by the id parameter does not support the request or the request is not properly authorized.
- **notFound (404)**: categoryNotFound - The category identified by the categoryId parameter cannot be found.
- **notFound (404)**: channelNotFound - The channel specified in the id parameter cannot be found.
```

--------------------------------

### Queue a playlist using cuePlaylist

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

Use argument syntax to queue a playlist by ID or array of video IDs, or object syntax to specify list types like user uploads.

```javascript
player.cuePlaylist(playlist:String|Array,
                   index:Number,
                   startSeconds:Number):Void
```

```javascript
player.cuePlaylist({listType:String,
                    list:String,
                    index:Number,
                    startSeconds:Number}):Void
```

--------------------------------

### GET /captions.download

Source: https://developers.google.com/youtube/v3/docs/errors

Error codes specific to the captions.download endpoint.

```APIDOC
## GET /captions.download

### Description
Errors returned when attempting to download a caption track.

### Error Details
- **forbidden (403)**: forbidden
- **invalidValue (400)**: couldNotConvert
- **notFound (404)**: captionNotFound
```

--------------------------------

### Main Execution Block

Source: https://developers.google.com/youtube/partner/code_samples/python

Parses command-line arguments, authenticates services, retrieves content owner ID, and lists managed channels. This is the main entry point for the script.

```python
if __name__ == "__main__":
  args = argparser.parse_args()
  (youtube, youtube_partner) = get_authenticated_services(args)
  content_owner_id = get_content_owner_id(youtube_partner)
  list_managed_channels(youtube, content_owner_id)
```

--------------------------------

### GET /activities.list

Source: https://developers.google.com/youtube/v3/docs/errors

Error codes specific to the activities.list endpoint.

```APIDOC
## GET /activities.list

### Description
Errors returned when listing activities for a channel or user.

### Error Details
- **forbidden (403)**: homeParameterDeprecated, forbidden
- **notFound (404)**: channelNotFound, homeChannelNotFound
- **unauthorized (401)**: authorizationRequired
```

--------------------------------

### Video Queueing and Playback Functions

Source: https://developers.google.com/youtube/iframe_api_reference?hl=it

Documentation on using argument and object syntax for video queueing and playback functions, including new properties for controlling playback.

```APIDOC
## Queueing and Playback Functions

### Description
This section explains the usage of argument and object syntax for video queueing and playback functions, and introduces new properties for controlling video playback.

### Function Syntax

*   **Argument Syntax**: Traditional method of calling functions with positional arguments.
*   **Object Syntax**: A more flexible method of calling functions using named properties within an object.

### Video Queueing Functions

All video queueing functions now support both argument and object syntax. Object syntax may support additional functionality not available through argument syntax.

### Playback Control with Object Syntax

When using object syntax for video queueing functions, the following property is supported:

*   **`endSeconds`** (float/integer) - Optional - Specifies the time in seconds when the video should stop playing when `playVideo()` is called.
```

--------------------------------

### Create and Set Asset Metadata

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=ru

Initializes an asset resource, sets its title and description, and associates it with a content owner. This is the first step in registering a new asset.

```php
$metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");
```

--------------------------------

### GET /videos

Source: https://developers.google.com/youtube/v3/code_samples/code_snippets

Retrieves information about specific YouTube videos.

```APIDOC
## GET /videos

### Description
Retrieves information about specific YouTube videos. You can search for videos based on various criteria.

### Method
GET

### Endpoint
/videos

### Query Parameters
- **id** (string) - Optional - The ID of the video(s) to retrieve.
- **chart** (string) - Optional - Specifies a chart to retrieve. Valid values are 'mostPopular'.
- **part** (string) - Optional - Specifies the parts of the video resource that should be included in the response.

### Request Example
```json
{
  "example": "GET /videos?id=dQw4w9WgXcQ"
}
```

### Response
#### Success Response (200)
- **items** (array) - A list of video resources.

#### Response Example
{
  "items": [
    {
      "kind": "youtube#video",
      "etag": "example_etag",
      "id": "dQw4w9WgXcQ",
      "snippet": {
        "publishedAt": "2007-03-14T15:27:30Z",
        "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
        "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        "description": "The official video of 'Never Gonna Give You Up' by Rick Astley...",
        "thumbnails": { ... },
        "channelTitle": "Rick Astley"
      },
      "statistics": {
        "viewCount": "1000000000",
        "likeCount": "10000000",
        "commentCount": "100000"
      }
    }
  ]
}
```

--------------------------------

### Load YouTube Player with Existing iframe

Source: https://developers.google.com/youtube/iframe_api_reference?hl=ko

This example demonstrates how to use the API with an existing `<iframe>` element. The `onYouTubeIframeAPIReady` function is called when the API is ready and the player is initialized.

```javascript
<iframe id="player" type="text/html" width="640" height="360" src="http://www.youtube.com/embed/M7lc1UVf-VE?enablejsapi=1" frameborder="0"></iframe>

<script>
  // Load the IFrame Player API code asynchronously.
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // Replace the 'player' element with an <iframe> and YouTube player
  function onYouTubeIframeAPIReady() {
    new YT.Player('player', {
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  }

  // The API will call this function when the video player is ready.
  function onPlayerReady(event) {
    event.target.playVideo();
  }

  // The API calls this function when the player's state changes.
  function onPlayerStateChange(event) {
    // ...
  }
</script>
```

--------------------------------

### GET /activities

Source: https://developers.google.com/youtube/v3/code_samples/code_snippets

Retrieves a collection of activities associated with a channel.

```APIDOC
## GET /activities

### Description
Retrieves a collection of activities associated with a channel. This can include video uploads, new posts, and other channel updates.

### Method
GET

### Endpoint
/activities

### Query Parameters
- **channelId** (string) - Required - The ID of the channel to retrieve activities for.
- **part** (string) - Optional - Specifies the parts of the activity resource that should be included in the response.

### Response
#### Success Response (200)
- **items** (array) - A list of activity resources.

#### Response Example
{
  "items": [
    {
      "kind": "youtube#activity",
      "etag": "example_etag",
      "id": "activity_id_1",
      "snippet": {
        "publishedAt": "2023-01-01T12:00:00Z",
        "channelId": "channel_id",
        "title": "New video uploaded: Example Video",
        "description": "Check out my latest video!",
        "thumbnails": { ... },
        "channelTitle": "Example Channel"
      }
    }
  ]
}
```

--------------------------------

### GET /media

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=fa

Downloads a report file from a specified URL.

```APIDOC
## GET /media

### Description
Download the report specified by the URL.

### Method
GET

### Endpoint
/media

### Parameters
#### Query Parameters
- **alt** (string) - Required - Set to 'media' for file download.
```

--------------------------------

### GET /reportTypes

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=fr

Retrieves a list of all available report types.

```APIDOC
## GET /reportTypes

### Description
Retrieves a list of report types available for the YouTube Reporting API.

### Method
GET

### Endpoint
reportTypes.listReportTypes

### Response
#### Success Response (200)
- **id** (string) - The unique identifier for the report type.
- **name** (string) - The display name of the report type.
```

--------------------------------

### Load and play a playlist using loadPlaylist

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

Use argument or object syntax to load a playlist and immediately begin playback.

```javascript
player.loadPlaylist(playlist:String|Array,
                    index:Number,
                    startSeconds:Number):Void
```

```javascript
player.loadPlaylist({list:String,
                     listType:String,
                     index:Number,
                     startSeconds:Number}):Void
```

--------------------------------

### GET /reportTypes

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=hi

Retrieves a list of all available report types.

```APIDOC
## GET /reportTypes

### Description
Retrieves a list of report types available for the authenticated user.

### Method
GET

### Endpoint
/reportTypes

### Response
#### Success Response (200)
- **id** (string) - The unique identifier for the report type.
- **name** (string) - The display name of the report type.
```

--------------------------------

### Initialize YouTube Service in Ruby

Source: https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps

Initialize a new YouTube service object for version 3 of the YouTube Data API.

```ruby
youtube = Google::Apis::YoutubeV3::YouTubeService.new
```

--------------------------------

### GET /youtube/partner/reference/rest/v1/uploader/list

Source: https://developers.google.com/youtube/partner/reference/rest/v1/uploader

Retrieves a list of uploaders for a content owner.

```APIDOC
## GET /youtube/partner/reference/rest/v1/uploader/list

### Description
Retrieves a list of uploaders for a content owner.

### Method
GET

### Endpoint
/youtube/partner/reference/rest/v1/uploader/list

### Parameters
#### Query Parameters
- **contentOwnerId** (string) - Required - The ID of the content owner for whom to retrieve uploaders.

### Response
#### Success Response (200)
- **uploaders** (array) - A list of uploader objects.
  - **uploaderName** (string) - The name of the uploader.
  - **kind** (string) - The type of the API resource. For uploader resources, the value is `youtubePartner#uploader`.

#### Response Example
```json
{
  "uploaders": [
    {
      "uploaderName": "ExampleUploader1",
      "kind": "youtubePartner#uploader"
    },
    {
      "uploaderName": "ExampleUploader2",
      "kind": "youtubePartner#uploader"
    }
  ]
}
```
```

--------------------------------

### Authentication and Client Initialization

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=pl

This snippet demonstrates how to initialize a Google_Client for the YouTube Reporting API, including setting authentication credentials and scopes.

```APIDOC
## Initialize Google Client

### Description
Initializes a Google_Client object, loads credentials, and sets the necessary scope for accessing YouTube reporting data.

### Method
N/A (Function Definition)

### Endpoint
N/A

### Parameters
None

### Request Body
None

### Request Example
```php
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope('https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to a file.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}
```

### Response
- **Google_Client** (object) - An authenticated Google_Client instance.
```

--------------------------------

### GET /referenceConflicts

Source: https://developers.google.com/youtube/partner/reference/rest/v1/referenceConflicts

Retrieves a list of all unresolved reference conflicts.

```APIDOC
## GET /referenceConflicts

### Description
Retrieves a list of unresolved reference conflicts.

### Method
GET

### Endpoint
/referenceConflicts
```

--------------------------------

### GET /websites/developers_google_youtube/claim_history

Source: https://developers.google.com/youtube/partner/reference/rest/v1/claimHistory

Retrieves the claim history for a specified claim.

```APIDOC
## GET /websites/developers_google_youtube/claim_history

### Description
Retrieves the claim history for a specified claim.

### Method
GET

### Endpoint
/websites/developers_google_youtube/claim_history

### Parameters
#### Query Parameters
- **claimId** (string) - Required - The unique identifier for the claim.

### Response
#### Success Response (200)
- **claimHistory** (ClaimHistory) - The historical data for the claim.

### Response Example
```json
{
  "claimHistory": {
    "claimEvents": [
      {
        "eventTime": "2023-10-27T10:00:00Z",
        "eventType": "CREATED",
        "reason": "Initial claim submission",
        "source": {
          "type": "USER",
          "userId": "user123"
        },
        "typeDetails": {}
      },
      {
        "eventTime": "2023-10-27T11:30:00Z",
        "eventType": "UPDATED",
        "reason": "Additional information provided",
        "source": {
          "type": "SYSTEM"
        },
        "typeDetails": {
          "updateStatus": "PENDING_REVIEW"
        }
      }
    ]
  }
}
```

### Error Handling
- **404 Not Found**: If the claim ID does not exist.
- **500 Internal Server Error**: If there is a server-side issue.
```

--------------------------------

### Upload Video and Manage Assets

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=fr

Demonstrates retrieving content owner IDs, performing chunked video uploads, and creating assets with ownership metadata.

```php
  try{

    // Call the contentOwners.list method to retrieve the ID of the content
    // owner associated with the currently authenticated user's account.
    $contentOwnersListResponse = $youtubePartner->contentOwners->listContentOwners(
        array('fetchMine' => true));
    $contentOwnerId = $contentOwnersListResponse['items'][0]['id'];

    // REPLACE this value with the path to the file you are uploading.
    $videoPath = "/path/to/file.mp4";

    // REPLACE this value with the ID that uniquely identifies the channel that
    // you are uploading to.
    $channelId = "CHANNEL_ID";

    // Create a snippet with title, description, tags and category ID
    // Create an asset resource and set its snippet metadata and type.
    // This example sets the video's title, description, keyword tags, and
    // video category.
    $snippet = new Google_Service_YouTube_VideoSnippet();
    $snippet->setTitle("Test title");
    $snippet->setDescription("Test description");
    $snippet->setTags(array("tag1", "tag2"));

    // Numeric video category. See
    // https://developers.google.com/youtube/v3/docs/videoCategories/list
    $snippet->setCategoryId("22");

    // Set the video's status to "public". Valid statuses are "public",
    // "private" and "unlisted".
    $status = new Google_Service_YouTube_VideoStatus();
    $status->privacyStatus = "public";

    // Associate the snippet and status objects with a new video resource.
    $video = new Google_Service_YouTube_Video();
    $video->setSnippet($snippet);
    $video->setStatus($status);

    // Specify the size of each chunk of data, in bytes. Set a higher value for
    // reliable connection as fewer chunks lead to faster uploads. Set a lower
    // value for better recovery on less reliable connections.
    $chunkSizeBytes = 1 * 1024 * 1024;

    // Setting the defer flag to true tells the client to return a request which can be called
    // with ->execute(); instead of making the API call immediately.
    $client->setDefer(true);

    // Create a request for the API's videos.insert method to create and upload the video.
    $insertRequest = $youtube->videos->insert("status,snippet", $video,
        array('onBehalfOfContentOwner' => $contentOwnerId,
            'onBehalfOfContentOwnerChannel' => $channelId));

    // Create a MediaFileUpload object for resumable uploads.
    $media = new Google_Http_MediaFileUpload(
        $client,
        $insertRequest,
        'video/*',
        null,
        true,
        $chunkSizeBytes
    );
    $media->setFileSize(filesize($videoPath));


    // Read the media file and upload it chunk by chunk.
    $status = false;
    $handle = fopen($videoPath, "rb");
    while (!$status && !feof($handle)) {
      $chunk = fread($handle, $chunkSizeBytes);
      $status = $media->nextChunk($chunk);
    }

    fclose($handle);

    // Set defer back to false to be able to make other calls after the file upload.
    $client->setDefer(false);

    $videoId = $status['id'];

    // Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));
```

--------------------------------

### Update YouTube Playlist to Enable Podcast Show

Source: https://developers.google.com/youtube/v3/guides/implementation/playlists

This example shows how to update an existing playlist to enable it as a podcast show using the `playlists.update` method. Provide the playlist ID and ensure the `snippet.title` and `snippet.description` are included.

```json
{
  "id": "PLAYLIST_ID",
  "snippet": {
    "title": "New playlist",
    "description": "New playlist description"
  },
  "status": {
    "podcastStatus": "enabled"
  }
}
```

--------------------------------

### GET /youtube/partner/v1/campaigns

Source: https://developers.google.com/youtube/partner/reference/rest/v1/campaigns/list

Retrieves a list of campaigns for a content owner.

```APIDOC
## GET https://youtubepartner.googleapis.com/youtube/partner/v1/campaigns

### Description
Retrieves a list of campaigns associated with a specific content owner.

### Method
GET

### Endpoint
https://youtubepartner.googleapis.com/youtube/partner/v1/campaigns

### Parameters
#### Query Parameters
- **onBehalfOfContentOwner** (string) - Required - Identifies the content owner that the user is acting on behalf of.
- **pageToken** (string) - Optional - Identifies a particular page of results to return, using the nextPageToken from a previous response.

### Request Body
The request body must be empty.

### Response
#### Success Response (200)
- **kind** (string) - The type of the API response (value is youtubePartner#campaignList).
- **items** (array) - A list of Campaign objects.

#### Response Example
{
  "kind": "youtubePartner#campaignList",
  "items": [
    {
      "id": "CAMPAIGN_ID",
      "name": "Campaign Name"
    }
  ]
}
```

--------------------------------

### Authentication and Client Initialization

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=pt-br

This section details how to initialize the Google Client with OAuth 2.0 credentials and set the necessary scopes for accessing YouTube data. It includes steps for loading existing credentials or initiating the OAuth flow for new users.

```APIDOC
## Authentication and Client Initialization

### Description
Initializes the Google Client for API access, including setting up OAuth 2.0 credentials, scopes, and handling token management.

### Method
N/A (This is a setup function)

### Endpoint
N/A

### Parameters
None

### Request Example
N/A

### Response
- **Google_Client** (object) - An authenticated Google Client object.

### Response Example
N/A
```

--------------------------------

### GET /claimSearch

Source: https://developers.google.com/youtube/partner/reference/errors

Searches for claims based on specific criteria.

```APIDOC
## GET /claimSearch

### Description
Searches for claims using filters.

### Method
GET

### Parameters
#### Query Parameters
- **q** (string) - Optional - Search query.
- **asset_id** (string) - Optional - Asset ID filter.
- **video_id** (string) - Optional - Video ID filter.
- **includeThirdPartyClaims** (boolean) - Optional - Only valid with videoId filter.
- **pageToken** (string) - Optional - Token for pagination.

### Response
#### Error Handling
- **badRequest (400)**: Invalid criteria or invalid parameter usage.
- **invalidValue (400)**: Invalid pageToken.
```

--------------------------------

### Initialize YouTube Partner API Service

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example

Sets up the YouTube Partner API service object for making requests. Ensure you have valid credentials and specify the API version.

```python
FLOW = flow_from_clientsecrets(CLIENT_SECRETS, 
            scope='https://www.googleapis.com/auth/youtubepartner',
            message=MISSING_CLIENT_SECRETS_MESSAGE)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

# ... later in main function ...
storage = Storage('yt_partner_api.dat')
credentials = storage.get()
if credentials is None or credentials.invalid:
  credentials = run(FLOW, storage)

http = httplib2.Http()
http = credentials.authorize(http)

service = build("youtubePartner", options.version, http=http, static_discovery=False)
```

--------------------------------

### GET metadataHistory.list

Source: https://developers.google.com/youtube/partner/guides/managing_composition_assets

Retrieves the metadata history for a specified asset.

```APIDOC
## GET metadataHistory.list

### Description
Returns a list of all metadata provided for an asset, regardless of which content owner provided the data.

### Method
GET

### Parameters
#### Query Parameters
- **assetId** (string) - Required - Identifies the asset for which data is being retrieved.
```

--------------------------------

### GET /videoAdvertisingOptions

Source: https://developers.google.com/youtube/partner/docs/v1/videoAdvertisingOptions

Retrieves the advertising settings for a specified video.

```APIDOC
## GET /videoAdvertisingOptions

### Description
Retrieves advertising settings for the specified video.

### Method
GET

### Endpoint
/videoAdvertisingOptions
```

--------------------------------

### POST /package

Source: https://developers.google.com/youtube/partner/reference/rest/v1/package/insert

Inserts a metadata-only package into the YouTube Partner system.

```APIDOC
## POST https://youtubepartner.googleapis.com/youtube/partner/v1/package

### Description
Inserts a metadata-only package using a POST request. This endpoint requires the user to be authorized with the specific YouTube Partner scope.

### Method
POST

### Endpoint
https://youtubepartner.googleapis.com/youtube/partner/v1/package

### Parameters
#### Query Parameters
- **onBehalfOfContentOwner** (string) - Optional - Identifies the content owner that the user is acting on behalf of for accounts associated with multiple content owners.

#### Request Body
- **Package** (object) - Required - An instance of the Package resource defining the metadata.

### Response
#### Success Response (200)
- **status** (string) - The package insert status.
- **errors** (array) - A list of ValidateError objects if any occurred.
- **kind** (string) - The type of the API response (youtubePartner#packageInsert).
- **resource** (object) - The inserted Package resource.

#### Response Example
{
  "status": "success",
  "errors": [],
  "kind": "youtubePartner#packageInsert",
  "resource": { ... }
}
```

--------------------------------

### GET /youtube/v3/playlistItems

Source: https://developers.google.com/youtube/analytics/v1/sample-application

Retrieves a list of items from a specified playlist.

```APIDOC
## GET /youtube/v3/playlistItems

### Description
Retrieves a list of items from a specified playlist.

### Method
GET

### Parameters
#### Query Parameters
- **playlistId** (string) - Required - The ID of the playlist to retrieve items from.
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more resource properties that the API response will include.
```

--------------------------------

### Playlist View Counts and Watch Time by Playback Location

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=ru

Retrieves view counts, playlist views, estimated watch time, and playlist starts for a channel's playlists, aggregated by playback location type. Results are sorted by playlist starts in descending order.

```APIDOC
## GET /analytics/v1/data

### Description
Retrieves view counts, playlist views, estimated watch time, and playlist starts for a channel's playlists, aggregated by playback location type. Results are sorted by playlist starts in descending order.

### Method
GET

### Endpoint
/analytics/v1/data

### Query Parameters
- **dimensions** (string) - Required - e.g., `insightPlaybackLocationType`
- **metrics** (string) - Required - e.g., `views,estimatedMinutesWatched,playlistStarts,playlistViews`
- **sort** (string) - Required - e.g., `-playlistStarts` (descending by playlist starts)

### Request Example
```json
{
  "dimensions": "insightPlaybackLocationType",
  "metrics": "views,estimatedMinutesWatched,playlistStarts,playlistViews",
  "sort": "-playlistStarts"
}
```

### Response
#### Success Response (200)
- **views** (integer) - Aggregated video metric for views.
- **estimatedMinutesWatched** (integer) - Estimated minutes watched.
- **playlistStarts** (integer) - In-playlist metric for playlist starts.
- **playlistViews** (integer) - In-playlist metric for playlist views.

#### Response Example
```json
{
  "kind": "youtubeAnalytics#resultTable",
  "rows": [
    ["CHANNEL", 100000, 500000, 1000, 5000]
  ],
  "columnHeaders": [
    {"name": "insightPlaybackLocationType", "columnType": "DIMENSION"},
    {"name": "views", "columnType": "METRIC"},
    {"name": "estimatedMinutesWatched", "columnType": "METRIC"},
    {"name": "playlistStarts", "columnType": "METRIC"},
    {"name": "playlistViews", "columnType": "METRIC"}
  ]
}
```
```

--------------------------------

### Playlist Performance Metrics

Source: https://developers.google.com/youtube/analytics/sample-requests

Retrieve total playlist starts, estimated minutes watched, playlist views, and views per playlist start for playlists within a content owner's channels. The `playlistViews` metric specifically counts views within a playlist context.

```text
metrics=playlistViews,playlistStarts,playlistEstimatedMinutesWatched,viewsPerPlaylistStart
```

--------------------------------

### Queueing Functions: loadVideoById

Source: https://developers.google.com/youtube/js_api_reference

Demonstrates the two syntaxes (argument and object) for calling queueing functions like `loadVideoById`. The object syntax offers additional flexibility, such as specifying `endSeconds`.

```APIDOC
## Queueing Functions: loadVideoById

Queueing functions allow loading and playing videos or playlists. The API supports both argument and object syntaxes for calling these functions.

### Argument Syntax

```javascript
loadVideoById("bHQqvYy5KYo", 5, "large")
```

### Object Syntax

```javascript
loadVideoById({
  'videoId': 'bHQqvYy5KYo',
  'startSeconds': 5,
  'endSeconds': 60
});
```

**Note**: The object syntax supports properties like `endSeconds` which are not available in the argument syntax.
```

--------------------------------

### Initialize YouTube Partner API Flow

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example?hl=es-419

Sets up the OAuth 2.0 flow for authenticating with the YouTube Partner API. Ensure CLIENT_SECRETS and MISSING_CLIENT_SECRETS_MESSAGE are defined elsewhere.

```python
FLOW = flow_from_clientsecrets(CLIENT_SECRETS, 
            scope='https://www.googleapis.com/auth/youtubepartner',
            message=MISSING_CLIENT_SECRETS_MESSAGE)
```

--------------------------------

### Statistics for a specific playlist

Source: https://developers.google.com/youtube/analytics/sample-requests?hl=bn

Retrieves total playlist starts, estimated minutes watched, views, playlist views, and views per playlist start for a specific playlist. Can also retrieve aggregate statistics for multiple playlists by providing a comma-separated list of up to 500 playlist IDs.

```APIDOC
## Statistics for a specific playlist

### Description
Retrieves total playlist starts, estimated minutes watched, views, playlist views, and views per playlist start for a specific playlist. Note that to run this query in the APIs Explorer, you must replace the string `PLAYLIST_ID` in the `filters` parameter value with the playlist ID for a playlist in one of the content owner's channels.

To retrieve aggregate statistics for multiple playlists, you can also replace the string `PLAYLIST_ID` with a comma-separated list of up to 500 playlists IDs for playlists in the content owner's channels.

### Method
GET

### Endpoint
/youtube/v3/playlistReports

### Parameters
#### Query Parameters
- **metrics** (string) - Required - Comma-separated list of metrics to retrieve. Example: `views,estimatedMinutesWatched,playlistStarts,playlistViews,viewsPerPlaylistStart`
- **filters** (string) - Required - Filter criteria. Example: `playlist==PLAYLIST_ID` or `playlist==ID1,ID2,...
- **sort** (string) - Optional - Sorting order for the results.
- **maxResults** (integer) - Optional - The maximum number of results to return.
- **startDate** (date) - Optional - The start date for the report.
- **endDate** (date) - Optional - The end date for the report.

### Response
#### Success Response (200)
- **rows** (array) - An array of objects, where each object contains the requested metrics for the specified playlist(s).

#### Response Example
```json
{
  "rows": [
    {
      "playlistId": "PLAYLIST_ID",
      "views": "10000",
      "estimatedMinutesWatched": "50000",
      "playlistStarts": "1000",
      "playlistViews": "15000",
      "viewsPerPlaylistStart": "15"
    }
  ]
}
```
```

--------------------------------

### GET /channels.list

Source: https://developers.google.com/youtube/v3/revision_history

Retrieves information about a channel, now supporting the forUsername parameter.

```APIDOC
## GET /channels.list

### Description
Retrieves information about a channel. You can now specify a YouTube username to retrieve channel details.

### Method
GET

### Endpoint
/channels.list

### Parameters
#### Query Parameters
- **forUsername** (string) - Optional - The YouTube username of the channel to retrieve.
```

--------------------------------

### Create and Configure Asset

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=it

Creates a new asset resource and defines ownership rights for the content owner.

```PHP
    // Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));
```

--------------------------------

### Implement ViewController Logic

Source: https://developers.google.com/youtube/v3/quickstart/ios?ver=objc

Configures the UI, handles authentication callbacks, and executes YouTube API queries.

```objective-c
#import "ViewController.h"

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Configure Google Sign-in.
    GIDSignIn* signIn = [GIDSignIn sharedInstance];
    signIn.delegate = self;
    signIn.uiDelegate = self;
    signIn.scopes = [NSArray arrayWithObjects:kGTLRAuthScopeYouTubeReadonly, nil];
    [signIn signInSilently];

    // Add the sign-in button.
    self.signInButton = [[GIDSignInButton alloc] init];
    [self.view addSubview:self.signInButton];

    // Create a UITextView to display output.
    self.output = [[UITextView alloc] initWithFrame:self.view.bounds];
    self.output.editable = false;
    self.output.contentInset = UIEdgeInsetsMake(20.0, 0.0, 20.0, 0.0);
    self.output.autoresizingMask = UIViewAutoresizingFlexibleHeight | UIViewAutoresizingFlexibleWidth;
    self.output.hidden = true;
    [self.view addSubview:self.output];

    // Initialize the service object.
    self.service = [[GTLRYouTubeService alloc] init];
}

- (void)signIn:(GIDSignIn *)signIn
didSignInForUser:(GIDGoogleUser *)user
     withError:(NSError *)error {
    if (error != nil) {
        [self showAlert:@"Authentication Error" message:error.localizedDescription];
        self.service.authorizer = nil;
    } else {
        self.signInButton.hidden = true;
        self.output.hidden = false;
        self.service.authorizer = user.authentication.fetcherAuthorizer;
        [self fetchChannelResource];
    }
}


// Construct a query and retrieve the channel resource for the GoogleDevelopers
// YouTube channel. Display the channel title, description, and view count.
- (void)fetchChannelResource {
    GTLRYouTubeQuery_ChannelsList *query =
    [GTLRYouTubeQuery_ChannelsList queryWithPart:@"snippet,statistics"];
  query.identifier = @"UC_x5XG1OV2P6uZZ5FSM9Ttw";
  // To retrieve data for the current user's channel, comment out the previous
  // line (query.identifier ...) and uncomment the next line (query.mine ...).
  // query.mine = true;

  [self.service executeQuery:query
                    delegate:self
           didFinishSelector:@selector(displayResultWithTicket:finishedWithObject:error:)];
}

// Process the response and display output
- (void)displayResultWithTicket:(GTLRServiceTicket *)ticket
             finishedWithObject:(GTLRYouTube_ChannelListResponse *)channels
                          error:(NSError *)error {
  if (error == nil) {
    NSMutableString *output = [[NSMutableString alloc] init];
    if (channels.items.count > 0) {
      [output appendString:@"Channel information:\n"];
      for (GTLRYouTube_Channel *channel in channels) {
        NSString *title = channel.snippet.title;
        NSString *description = channel.snippet.description;
        NSNumber *viewCount = channel.statistics.viewCount;
        [output appendFormat:@"Title: %@\nDescription: %@\nViewCount: %@\n", title, description, viewCount];
      }
    } else {
      [output appendString:@"Channel not found."];
    }
    self.output.text = output;
  } else {
    [self showAlert:@"Error" message:error.localizedDescription];
  }
}


// Helper for showing an alert
- (void)showAlert:(NSString *)title message:(NSString *)message {
    UIAlertController *alert =
    [UIAlertController alertControllerWithTitle:title
                                        message:message
                                 preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction *ok =
    [UIAlertAction actionWithTitle:@"OK"
                             style:UIAlertActionStyleDefault
                           handler:^(UIAlertAction * action)
     {
```

--------------------------------

### GET /videos/list

Source: https://developers.google.com/youtube/v3/revision_history

Retrieves a list of videos with support for region-specific charts.

```APIDOC
## GET /videos/list

### Description
Retrieves a list of videos. Now supports filtering by region code when using the chart parameter.

### Method
GET

### Endpoint
/videos/list

### Parameters
#### Query Parameters
- **chart** (string) - Required - The chart to retrieve.
- **regionCode** (string) - Optional - ISO 3166-1 alpha-2 country code identifying the content region.
```

--------------------------------

### GET /commentThreads.list

Source: https://developers.google.com/youtube/v3/revision_history

Retrieves a list of comment threads with support for ordering.

```APIDOC
## GET /commentThreads.list

### Description
Retrieves a list of comment threads. 

### Method
GET

### Endpoint
/commentThreads.list

### Parameters
#### Query Parameters
- **order** (string) - Optional - Specifies the order in which the API response should list comment threads (time or relevance). Defaults to time.
```

--------------------------------

### GET /search.list

Source: https://developers.google.com/youtube/v3/revision_history?hl=bn

Searches for resources with support for relevance language filtering.

```APIDOC
## GET /search.list

### Description
Returns a list of search results matching the query parameters.

### Method
GET

### Parameters
#### Query Parameters
- **relevanceLanguage** (string) - Optional - Requests results most relevant to a particular language.
```

--------------------------------

### GET /search

Source: https://developers.google.com/youtube/v3/revision_history?hl=bn

Search for videos with an added filter for developer-uploaded content.

```APIDOC
## GET /search.list

### Description
Retrieves search results with an optional filter to restrict results to videos uploaded via the developer's application.

### Method
GET

### Endpoint
/search.list

### Query Parameters
- **forDeveloper** (boolean) - Optional - If true, restricts search to videos uploaded via the developer's application.
- **q** (string) - Optional - Search query term.
```

--------------------------------

### Full Python Code Sample for Asset Reference Upload

Source: https://developers.google.com/youtube/partner/asset_reference_upload_example?hl=hi

This script handles asset, ownership, and reference creation for the YouTube Partner API. Ensure you have a 'client_secrets.json' file configured for OAuth 2.0 authentication. Run with --help for detailed usage instructions.

```python
#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#  
# Copyright (C) 2012 Google Inc.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# 		http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
  
"""Simple command-line sample for Youtube partner API.  
  
Command-line application that creates asset, asset ownership, match policy  
and reference.  
  
Usage:  
	$ python asset_reference_upload_example.py --reference_file=REFERENCE_FILE \  
		--asset_title=ASSET_TITLE --owner=OWNER  
  
You can also get help on all the command-line flags the program understands  
by running:  
  
	$ python asset_reference_upload_example.py --help  
"""  
  
__author__ = 'mateuszz+pub@google.com (Mateusz Zięba)'  
  
import httplib2  
import logging  
import sys  
import optparse  
import os  
  
from apiclient.discovery import build  
from apiclient.errors import HttpError  
from apiclient.http import MediaFileUpload  
from oauth2client.file import Storage  
from oauth2client.client import AccessTokenRefreshError  
from oauth2client.client import flow_from_clientsecrets  
from oauth2client.tools import run  
  
# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains  
# the OAuth 2.0 information for this application, including its client_id and  
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from  
# the Google API Console at  
# https://console.cloud.google.com/.  
# See the "Registering your application" instructions for an explanation  
# of how to find these values:  
# https://developers.google.com/youtube/partner/guides/registering_an_application  
CLIENT_SECRETS = 'client_secrets.json'  
  
# Helpful message to display if the CLIENT_SECRETS file is missing.  
MISSING_CLIENT_SECRETS_MESSAGE = """  
WARNING: Please configure OAuth 2.0  
  
To make this sample run you need to populate the client_secrets.json  
file found at:  
  
%s  
  
with information from the API Console  
<https://console.cloud.google.com/>.  
  
""" % os.path.join(os.path.dirname(__file__), CLIENT_SECRETS)  
  
```

--------------------------------

### GET /liveChat/moderators

Source: https://developers.google.com/youtube/v3/live/docs

Lists all moderators for a specific YouTube live chat.

```APIDOC
## GET /liveChat/moderators

### Description
Lists moderators for a live chat. The request must be authorized by the owner of the live broadcast's channel.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/liveChat/moderators
```

--------------------------------

### GET /commentThreads.list

Source: https://developers.google.com/youtube/v3/guides/implementation/comments?hl=pt-br

Retrieves a list of comment threads from a video or channel.

```APIDOC
## GET /commentThreads.list

### Description
Retrieves a list of comment threads for a specific video or channel.

### Method
GET

### Endpoint
/youtube/v3/youtube.commentThreads.list

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include. Use 'snippet' for top-level comments or 'snippet,replies' to include replies.
- **videoId** (string) - Optional - The ID of the video for which to retrieve comments.
- **channelId** (string) - Optional - The ID of the channel for which to retrieve comments.
- **allThreadsRelatedToChannelId** (string) - Optional - Retrieves all comment threads associated with the specified channel.
```

--------------------------------

### Create a reporting job in Java

Source: https://developers.google.com/youtube/analytics/v1/code_samples/java

This sample demonstrates how to authenticate, list available report types, and create a new reporting job using the YouTube Reporting API.

```java
/*
 * Copyright (c) 2015 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied. See the License for the specific language governing permissions and limitations under
 * the License.
 */

package com.google.api.services.samples.youtube.cmdline.reporting;

import com.google.api.client.auth.oauth2.Credential;
import com.google.api.client.googleapis.json.GoogleJsonResponseException;
import com.google.api.services.samples.youtube.cmdline.Auth;
import com.google.api.services.youtubereporting.YouTubeReporting;
import com.google.api.services.youtubereporting.model.Job;
import com.google.api.services.youtubereporting.model.ListReportTypesResponse;
import com.google.api.services.youtubereporting.model.ReportType;
import com.google.common.collect.Lists;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

/**
 * This sample creates a reporting job by:
 *
 * 1. Listing the available report types using the "reportTypes.list" method.
 * 2. Creating a reporting job using the "jobs.create" method.
 *
 * @author Ibrahim Ulukaya
 */
public class CreateReportingJob {

    /**
     * Define a global instance of a YouTube Reporting object, which will be used to make
     * YouTube Reporting API requests.
     */
    private static YouTubeReporting youtubeReporting;


    /**
     * Create a reporting job.
     *
     * @param args command line args (not used).
     */
    public static void main(String[] args) {

        /*
         * This OAuth 2.0 access scope allows for read access to the YouTube Analytics monetary reports for
         * authenticated user's account. Any request that retrieves earnings or ad performance metrics must
         * use this scope.
         */
        List<String> scopes = Lists.newArrayList("https://www.googleapis.com/auth/yt-analytics-monetary.readonly");

        try {
            // Authorize the request.
            Credential credential = Auth.authorize(scopes, "createreportingjob");

            // This object is used to make YouTube Reporting API requests.
            youtubeReporting = new YouTubeReporting.Builder(Auth.HTTP_TRANSPORT, Auth.JSON_FACTORY, credential)
                    .setApplicationName("youtube-cmdline-createreportingjob-sample").build();

            // Prompt the user to specify the name of the job to be created.
            String name = getNameFromUser();

            if (listReportTypes()) {
              createReportingJob(getReportTypeIdFromUser(), name);
            }
        } catch (GoogleJsonResponseException e) {
            System.err.println("GoogleJsonResponseException code: " + e.getDetails().getCode()
                    + " : " + e.getDetails().getMessage());
            e.printStackTrace();

        } catch (IOException e) {
            System.err.println("IOException: " + e.getMessage());
            e.printStackTrace();
        } catch (Throwable t) {
            System.err.println("Throwable: " + t.getMessage());
            t.printStackTrace();
        }
    }

    /**
     * Lists report types. (reportTypes.listReportTypes)
     * @return true if at least one report type exists
     * @throws IOException
     */
    private static boolean listReportTypes() throws IOException {
        // Call the YouTube Reporting API's reportTypes.list method to retrieve report types.
        ListReportTypesResponse reportTypesListResponse = youtubeReporting.reportTypes().list()
            .execute();
        List<ReportType> reportTypeList = reportTypesListResponse.getReportTypes();

        if (reportTypeList == null || reportTypeList.isEmpty()) {
          System.out.println("No report types found.");
          return false;
        } else {
            // Print information from the API response.
            System.out.println("\n================== Report Types ==================\n");
            for (ReportType reportType : reportTypeList) {
                System.out.println("  - Id: " + reportType.getId());
                System.out.println("  - Name: " + reportType.getName());
                System.out.println("\n-------------------------------------------------------------\n");
           }
        }
        return true;
    }

    /**
     * Creates a reporting job. (jobs.create)
     *
     * @param reportTypeId Id of the job's report type.
```

--------------------------------

### Cue video by URL

Source: https://developers.google.com/youtube/iframe_api_reference

Prepares a video for playback using a fully qualified YouTube player URL.

```javascript
player.cueVideoByUrl(mediaContentUrl:String,
                     startSeconds:Number):Void
```

```javascript
player.cueVideoByUrl({mediaContentUrl:String,
                      startSeconds:Number,
                      endSeconds:Number}):Void
```

--------------------------------

### GET /videoCategories

Source: https://developers.google.com/youtube/v3/docs/videoCategories/list?hl=es-419

Retrieves a list of categories that can be associated with YouTube videos.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/videoCategories

### Description
Returns a list of categories that can be associated with YouTube videos.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/videoCategories

### Parameters
#### Query Parameters
- **part** (string) - Required - The videoCategory resource properties that the API response will include. Set to 'snippet'.
- **id** (string) - Optional - A comma-separated list of video category IDs.
- **regionCode** (string) - Optional - The ISO 3166-1 alpha-2 country code to return categories available in that country.
- **hl** (string) - Optional - The language that should be used for text values in the API response.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type.
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - Token to retrieve the next page.
- **prevPageToken** (string) - Token to retrieve the previous page.
- **pageInfo** (object) - Paging information for the result set.
- **items** (list) - A list of video categories.
```

--------------------------------

### GET /search

Source: https://developers.google.com/youtube/v3/docs/search/list

Documentation for the search endpoint parameters and response structure.

```APIDOC
## GET /search

### Description
This endpoint allows searching for YouTube videos with various filtering options. Note that many parameters require the `type` parameter to be set to `video`.

### Method
GET

### Parameters
#### Query Parameters
- **videoEmbeddable** (string) - Optional - Restrict search to embeddable videos. Requires type=video.
- **videoLicense** (string) - Optional - Filter by license (any, creativeCommon, youtube). Requires type=video.
- **videoPaidProductPlacement** (string) - Optional - Filter by paid promotion (any, true). Requires type=video.
- **videoSyndicated** (string) - Optional - Restrict to syndicated videos (any, true). Requires type=video.
- **videoType** (string) - Optional - Filter by video type (any, episode, movie). Requires type=video.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type.
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - Token for the next page.
- **prevPageToken** (string) - Token for the previous page.
- **regionCode** (string) - Region code used for the search.
- **pageInfo** (object) - Paging information.
- **items** (list) - List of search results.

#### Response Example
{
  "kind": "youtube#searchListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "prevPageToken": "string",
  "regionCode": "string",
  "pageInfo": {
    "totalResults": 0,
    "resultsPerPage": 0
  },
  "items": []
}
```

--------------------------------

### GET /youtube/v3/playlists

Source: https://developers.google.com/youtube/v3/docs/playlists/list?hl=es-419

Retrieves a list of playlists that match the request criteria.

```APIDOC
## GET /youtube/v3/playlists

### Description
Retrieves a list of playlists that match the request criteria.

### Method
GET

### Endpoint
/youtube/v3/playlists

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include.
- **channelId** (string) - Optional - Returns the playlists owned by the specified channel.
- **hl** (string) - Optional - The hl parameter instructs the API to return localized resource metadata for a specific language.
- **id** (string) - Optional - Specifies a comma-separated list of the YouTube playlist ID(s) for the resource(s) that are being retrieved.
- **maxResults** (integer) - Optional - Specifies the maximum number of items that should be returned in the result set.
- **mine** (boolean) - Optional - Set to true to retrieve playlists owned by the authenticated user.
- **onBehalfOfContentOwner** (string) - Optional - Indicates that the request is being made on behalf of a content owner.
- **onBehalfOfContentOwnerChannel** (string) - Optional - Indicates that the request is being made on behalf of a specific channel.
- **pageToken** (string) - Optional - The pageToken parameter identifies a specific page in the result set that should be returned.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type (youtube#playlistListResponse).
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - The token for the next page in the result set.
- **prevPageToken** (string) - The token for the previous page in the result set.
- **pageInfo** (object) - Encapsulates paging information.
- **items[]** (list) - A list of playlists that match the request criteria.

### Error Handling
- **400 (invalidValue)**: playlistOperationUnsupported - The API does not support the ability to list the specified playlist.
- **403 (forbidden)**: channelClosed - The channel specified has been closed.
- **403 (forbidden)**: channelSuspended - The channel specified has been suspended.
- **403 (forbidden)**: playlistForbidden - The playlist does not support the request or is not properly authorized.
- **404 (notFound)**: channelNotFound - The channel specified cannot be found.
- **404 (notFound)**: playlistNotFound - The playlist identified cannot be found.
```

--------------------------------

### Upload Video using Go Client Library

Source: https://developers.google.com/youtube/v3/docs/videos/insert?hl=id

Uploads a video to your YouTube channel using the Go client library. Ensure you have authenticated and set up the necessary scopes. The video details and file path are configurable via command-line flags.

```Go
package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"

	"google.golang.org/api/youtube/v3"
)

var (
	filename    = flag.String("filename", "", "Name of video file to upload")
	title       = flag.String("title", "Test Title", "Video title")
	description = flag.String("description", "Test Description", "Video description")
	category    = flag.String("category", "22", "Video category")
	keywords    = flag.String("keywords", "", "Comma separated list of video keywords")
	privacy     = flag.String("privacy", "unlisted", "Video privacy status")
)

func main() {
	flag.Parse()

	if *filename == "" {
		log.Fatalf("You must provide a filename of a video file to upload")
	}

	client := getClient(youtube.YoutubeUploadScope)

	service, err := youtube.New(client)
	if err != nil {
		log.Fatalf("Error creating YouTube client: %v", err)
	}

	upload := &youtube.Video{
		Snippet: &youtube.VideoSnippet{
			Title:       *title,
			Description: *description,
			CategoryId:  *category,
		},
		Status: &youtube.VideoStatus{PrivacyStatus: *privacy},
	}

	// The API returns a 400 Bad Request response if tags is an empty string.
	if strings.Trim(*keywords, "") != "" {
		upload.Snippet.Tags = strings.Split(*keywords, ",")
	}

	call := service.Videos.Insert("snippet,status", upload)

	file, err := os.Open(*filename)
	defer file.Close()
	if err != nil {
		log.Fatalf("Error opening %v: %v", *filename, err)
	}

	response, err := call.Media(file).Do()
	handleError(err, "")
	fmt.Printf("Upload successful! Video ID: %v\n", response.Id)
}


```

--------------------------------

### Upload Video using .NET Client Library

Source: https://developers.google.com/youtube/v3/docs/videos/insert?hl=es

This example shows how to upload a video to YouTube using the .NET client library. It requires a 'client_secrets.json' file for authentication and specifies the video's title, description, tags, and privacy status.

```C#
using System;
using System.IO;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;

using Google.Apis.Auth.OAuth2;
using Google.Apis.Services;
using Google.Apis.Upload;
using Google.Apis.Util.Store;
using Google.Apis.YouTube.v3;
using Google.Apis.YouTube.v3.Data;

namespace Google.Apis.YouTube.Samples
{
  /// <summary>
  /// YouTube Data API v3 sample: upload a video.
  /// Relies on the Google APIs Client Library for .NET, v1.7.0 or higher.
  /// See https://developers.google.com/api-client-library/dotnet/get_started
  /// </summary>
  internal class UploadVideo
  {
    [STAThread]
    static void Main(string[] args)
    {
      Console.WriteLine("YouTube Data API: Upload Video");
      Console.WriteLine("==============================");

      try
      {
        new UploadVideo().Run().Wait();
      }
      catch (AggregateException ex)
      {
        foreach (var e in ex.InnerExceptions)
        {
          Console.WriteLine("Error: " + e.Message);
        }
      }

      Console.WriteLine("Press any key to continue...");
      Console.ReadKey();
    }

    private async Task Run()
    {
      UserCredential credential;
      using (var stream = new FileStream("client_secrets.json", FileMode.Open, FileAccess.Read))
      {
        credential = await GoogleWebAuthorizationBroker.AuthorizeAsync(
            GoogleClientSecrets.Load(stream).Secrets,
            // This OAuth 2.0 access scope allows an application to upload files to the
            // authenticated user's YouTube channel, but doesn't allow other types of access.
            new[] { YouTubeService.Scope.YoutubeUpload },
            "user",
            CancellationToken.None
        );
      }

      var youtubeService = new YouTubeService(new BaseClientService.Initializer() 
      {
        HttpClientInitializer = credential,
        ApplicationName = Assembly.GetExecutingAssembly().GetName().Name
      });

      var video = new Video();
      video.Snippet = new VideoSnippet();
      video.Snippet.Title = "Default Video Title";
      video.Snippet.Description = "Default Video Description";
      video.Snippet.Tags = new string[] { "tag1", "tag2" };
      video.Snippet.CategoryId = "22"; // See https://developers.google.com/youtube/v3/docs/videoCategories/list
      video.Status = new VideoStatus();
      video.Status.PrivacyStatus = "unlisted"; // or "private" or "public"
      var filePath = @"REPLACE_ME.mp4"; // Replace with path to actual movie file.

      using (var fileStream = new FileStream(filePath, FileMode.Open))
      {
        var videosInsertRequest = youtubeService.Videos.Insert(video, "snippet,status", fileStream, "video/*");
        videosInsertRequest.ProgressChanged += videosInsertRequest_ProgressChanged;
        videosInsertRequest.ResponseReceived += videosInsertRequest_ResponseReceived;

        await videosInsertRequest.UploadAsync();

```

--------------------------------

### GET /membershipsLevels/list

Source: https://developers.google.com/youtube/v3/docs/membershipsLevels

Lists membership levels for the channel that authorized the request.

```APIDOC
## GET /membershipsLevels/list

### Description
Lists membership levels for the channel that authorized the request. This endpoint is restricted to individual creators of channel-memberships-enabled YouTube channels.

### Method
GET

### Endpoint
/membershipsLevels/list

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type (youtube#membershipsLevel).
- **etag** (etag) - The Etag of this resource.
- **id** (string) - The unique ID assigned to the membership level.
- **snippet** (object) - Contains details about the membership level.
- **snippet.creatorChannelId** (string) - The YouTube channel ID of the creator.
- **snippet.levelDetails** (object) - Data about the membership level.
- **snippet.levelDetails.displayName** (string) - The level's display name.

#### Response Example
{
  "kind": "youtube#membershipsLevel",
  "etag": "etag",
  "id": "string",
  "snippet": {
    "creatorChannelId": "string",
    "levelDetails": {
      "displayName": "string"
    }
  }
}
```

--------------------------------

### POST /youtube/partner/v1/campaigns

Source: https://developers.google.com/youtube/partner/reference/rest/v1/campaigns/insert

This endpoint facilitates the creation of a new campaign for a content owner. The request requires a POST method to the specified URL. The `onBehalfOfContentOwner` query parameter specifies the content owner the user is acting on behalf of. The request body must contain a `Campaign` instance, and a successful response returns the newly created `Campaign`.

```APIDOC
## POST /youtube/partner/v1/campaigns

### Description
Creates a new campaign for a content owner.

### Method
POST

### Endpoint
`https://youtubepartner.googleapis.com/youtube/partner/v1/campaigns`

### Query Parameters
- **onBehalfOfContentOwner** (string) - Required - The content owner that the user is acting on behalf of.

### Request Body
- **Campaign** (object) - Required - An instance of the Campaign object.

### Request Example
```json
{
  "campaign": {
    "name": "My New Campaign",
    "ownerId": "12345"
  }
}
```

### Response
#### Success Response (200)
- **Campaign** (object) - The newly created Campaign instance.

#### Response Example
```json
{
  "campaign": {
    "id": "campaign-abc",
    "name": "My New Campaign",
    "ownerId": "12345",
    "creationDate": "2023-10-27T10:00:00Z"
  }
}
```

### Authorization Scopes
- `https://www.googleapis.com/auth/youtubepartner`
```

--------------------------------

### GET /membershipsLevels.list

Source: https://developers.google.com/youtube/v3/docs/errors

Error handling documentation for listing membership levels.

```APIDOC
## GET membershipsLevels.list

### Description
Retrieves a list of membership levels for a channel. Returns an error if channel memberships are not enabled.

### Method
GET

### Endpoint
membershipsLevels.list

### Response
#### Error Responses
- **badRequest (400)**: channelMembershipsNotEnabled
```

--------------------------------

### GET /members.list

Source: https://developers.google.com/youtube/v3/docs/errors

Error handling documentation for listing channel members.

```APIDOC
## GET members.list

### Description
Retrieves a list of members for a channel. Errors occur if memberships are not enabled or if parameters like mode, pageToken, or filterByMemberChannelId are invalid.

### Method
GET

### Endpoint
members.list

### Response
#### Error Responses
- **badRequest (400)**: channelMembershipsNotEnabled, invalidMode, invalidPageToken, invalidHasAccessToLevel, invalidFilterByMemberChannelId
```

--------------------------------

### Authentication and Client Initialization

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs.reports/list?hl=zh-tw

This snippet demonstrates how to initialize a Google_Client object, set authentication credentials, and manage access tokens for the YouTube Reporting API.

```APIDOC
## Authentication and Client Initialization

### Description
This function initializes a Google_Client, sets up authentication using client secrets, defines API scopes, and handles the retrieval and storage of OAuth 2.0 access and refresh tokens. It also includes logic for refreshing expired tokens.

### Method
N/A (Function Definition)

### Endpoint
N/A

### Parameters
None

### Request Example
N/A

### Response
- **Google_Client** (object) - An authenticated Google_Client instance.

### Response Example
N/A
```

--------------------------------

### Initialize OAuth2 Client and Express Server

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=es-419

Configures the OAuth2 client with credentials and sets up an Express server with session management.

```javascript
const http = require('http');
const https = require('https');
const url = require('url');
const { google } = require('googleapis');
const crypto = require('crypto');
const express = require('express');
const session = require('express-session');

/**
 * To use OAuth2 authentication, we need access to a CLIENT_ID, CLIENT_SECRET, AND REDIRECT_URI.
 * To get these credentials for your application, visit
 * https://console.cloud.google.com/apis/credentials.
 */
const oauth2Client = new google.auth.OAuth2(
  YOUR_CLIENT_ID,
  YOUR_CLIENT_SECRET,
  YOUR_REDIRECT_URL
);

// Access scopes for two non-Sign-In scopes: Read-only Drive activity and Google Calendar.
const scopes = [
  'https://www.googleapis.com/auth/youtubepartner',
  'https://www.googleapis.com/auth/calendar.readonly'
];

/* Global variable that stores user credential in this code example.
 * ACTION ITEM for developers:
 *   Store user's refresh token in your data store if
 *   incorporating this code into your real app.
 *   For more information on handling refresh tokens,
 *   see https://github.com/googleapis/google-api-nodejs-client#handling-refresh-tokens
 */
let userCredential = null;

async function main() {
  const app = express();

  app.use(session({
    secret: 'your_secure_secret_key', // Replace with a strong secret
    resave: false,
    saveUninitialized: false,
  }));

  // Example on redirecting user to Google's OAuth 2.0 server.
  app.get('/', async (req, res) => {
    // Generate a secure random state value.
    const state = crypto.randomBytes(32).toString('hex');
    // Store state in the session
    req.session.state = state;

    // Generate a url that asks permissions for the Drive activity and Google Calendar scope
    const authorizationUrl = oauth2Client.generateAuthUrl({
      // 'online' (default) or 'offline' (gets refresh_token)
      access_type: 'offline',
      /** Pass in the scopes array defined above.
        * Alternatively, if only one scope is needed, you can pass a scope URL as a string */
      scope: scopes,
      // Enable incremental authorization. Recommended as a best practice.
      include_granted_scopes: true,
      // Include the state parameter to reduce the risk of CSRF attacks.
      state: state
    });

    res.redirect(authorizationUrl);
  });

  // Receive the callback from Google's OAuth 2.0 server.
  app.get('/oauth2callback', async (req, res) => {
    // Handle the OAuth 2.0 server response
    let q = url.parse(req.url, true).query;

    if (q.error) { // An error response e.g. error=access_denied
      console.log('Error:' + q.error);
    } else if (q.state !== req.session.state) { //check state value
      console.log('State mismatch. Possible CSRF attack');
      res.end('State mismatch. Possible CSRF attack');
    } else { // Get access and refresh tokens (if access_type is offline)
      let { tokens } = await oauth2Client.getToken(q.code);
      oauth2Client.setCredentials(tokens);

      /** Save credential to the global variable in case access token was refreshed.
        * ACTION ITEM: In a production app, you likely want to save the refresh token
        *              in a secure persistent database instead. */
      userCredential = tokens;
      
      // User authorized the request. Now, check which scopes were granted.
      if (tokens.scope.includes('https://www.googleapis.com/auth/youtubepartner'))
      {
        // User authorized read-only Drive activity permission.
        // Example of using Google Drive API to list filenames in user's Drive.
        const drive = google.drive('v3');
        drive.files.list({
          auth: oauth2Client,
          pageSize: 10,
          fields: 'nextPageToken, files(id, name)',
        }, (err1, res1) => {
          if (err1) return console.log('The API returned an error: ' + err1);
          const files = res1.data.files;
          if (files.length) {
            console.log('Files:');
            files.map((file) => {
              console.log(`${file.name} (${file.id})`);
            });
          } else {
            console.log('No files found.');
          }
        });
      }
      else
      {
        // User didn't authorize read-only Drive activity permission.
        // Update UX and application accordingly
      }

      // Check if user authorized Calendar read permission.
      if (tokens.scope.includes('https://www.googleapis.com/auth/calendar.readonly'))
      {
        // User authorized Calendar read permission.
        // Calling the APIs, etc.
      }
      else
      {
        // User didn't authorize Calendar read permission.
        // Update UX and application accordingly
      }
    }
  });

  // Example on revoking a token
  app.get('/revoke', async (req, res) => {
    // Build the string for the POST request
    let postData = "token=" + userCredential.access_token;

    // Options for POST request to Google's OAuth 2.0 server to revoke a token
    let postOptions = {
```

--------------------------------

### GET /channelSections.list

Source: https://developers.google.com/youtube/v3/docs/errors

Details regarding error responses for the channelSections.list endpoint.

```APIDOC
## GET channelSections.list

### Description
Retrieves a list of channel sections for a channel. This documentation focuses on the error conditions associated with this method.

### Error Handling
| Error type | Error detail | Description |
|---|---|---|
| forbidden (403) | channelSectionForbidden | The requester is not allowed to access the requested channel sections. |
| invalidValue (400) | idInvalid | The request specifies an invalid channel section ID. |
| invalidValue (400) | invalidCriteria | The request couldn't be completed because the filter criteria are invalid. |
| notFound (404) | channelNotFound | The channel associated with the request cannot be found. |
| notFound (404) | channelSectionNotFound | The channel section associated with the request cannot be found. |
```

--------------------------------

### GET /jobs

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=zh-cn

Lists all reporting jobs associated with the authenticated account.

```APIDOC
## GET /jobs

### Description
Retrieves a list of all reporting jobs for the authenticated user.

### Method
GET

### Endpoint
/jobs

### Response
#### Success Response (200)
- **jobs** (List<Job>) - A list of reporting job objects containing Id, Name, and ReportTypeId.
```

--------------------------------

### Upload a Video and Create an Asset

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=ar

Demonstrates the process of uploading a video file in chunks and creating an associated asset in the YouTube Partner system.

```php
// owner associated with the currently authenticated user's account.
    $contentOwnersListResponse = $youtubePartner->contentOwners->listContentOwners(
        array('fetchMine' => true));
    $contentOwnerId = $contentOwnersListResponse['items'][0]['id'];

    // REPLACE this value with the path to the file you are uploading.
    $videoPath = "/path/to/file.mp4";

    // REPLACE this value with the ID that uniquely identifies the channel that
    // you are uploading to.
    $channelId = "CHANNEL_ID";

    // Create a snippet with title, description, tags and category ID
    // Create an asset resource and set its snippet metadata and type.
    // This example sets the video's title, description, keyword tags, and
    // video category.
    $snippet = new Google_Service_YouTube_VideoSnippet();
    $snippet->setTitle("Test title");
    $snippet->setDescription("Test description");
    $snippet->setTags(array("tag1", "tag2"));

    // Numeric video category. See
    // https://developers.google.com/youtube/v3/docs/videoCategories/list
    $snippet->setCategoryId("22");

    // Set the video's status to "public". Valid statuses are "public",
    // "private" and "unlisted".
    $status = new Google_Service_YouTube_VideoStatus();
    $status->privacyStatus = "public";

    // Associate the snippet and status objects with a new video resource.
    $video = new Google_Service_YouTube_Video();
    $video->setSnippet($snippet);
    $video->setStatus($status);

    // Specify the size of each chunk of data, in bytes. Set a higher value for
    // reliable connection as fewer chunks lead to faster uploads. Set a lower
    // value for better recovery on less reliable connections.
    $chunkSizeBytes = 1 * 1024 * 1024;

    // Setting the defer flag to true tells the client to return a request which can be called
    // with ->execute(); instead of making the API call immediately.
    $client->setDefer(true);

    // Create a request for the API's videos.insert method to create and upload the video.
    $insertRequest = $youtube->videos->insert("status,snippet", $video,
        array('onBehalfOfContentOwner' => $contentOwnerId,
            'onBehalfOfContentOwnerChannel' => $channelId));

    // Create a MediaFileUpload object for resumable uploads.
    $media = new Google_Http_MediaFileUpload(
        $client,
        $insertRequest,
        'video/*',
        null,
        true,
        $chunkSizeBytes
    );
    $media->setFileSize(filesize($videoPath));


    // Read the media file and upload it chunk by chunk.
    $status = false;
    $handle = fopen($videoPath, "rb");
    while (!$status && !feof($handle)) {
      $chunk = fread($handle, $chunkSizeBytes);
      $status = $media->nextChunk($chunk);
    }

    fclose($handle);

    // Set defer back to false to be able to make other calls after the file upload.
    $client->setDefer(false);

    $videoId = $status['id'];

    // Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId, $ownership,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    // Define a monetization policy for the asset.
    $policy = new Google_Service_YouTubePartner_Policy();
    $policyRule = new Google_Service_YouTubePartner_PolicyRule();
    $policyRule->setAction("monetize");
    $policy->setRules(array($policyRule));

    // Create a claim resource. Identify the video being claimed, the asset
    // that represents the claimed content, the type of content being claimed,
```

--------------------------------

### GET /jobs

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=fa

Lists all reporting jobs available for the authenticated user.

```APIDOC
## GET /jobs

### Description
Lists all reporting jobs for the authenticated user.

### Method
GET

### Endpoint
/jobs

### Response
#### Success Response (200)
- **jobs** (List<Job>) - A list of reporting jobs.
```

--------------------------------

### GET /reports/{reportId}

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs.reports

Retrieves the metadata for a specific report instance.

```APIDOC
## GET /reports/{reportId}

### Description
Retrieves the metadata for a specific report.

### Method
GET

### Endpoint
/reports/{reportId}

### Response
#### Success Response (200)
- **id** (string) - The report ID.
- **jobId** (string) - The ID of the reporting job.
- **startTime** (timestamp) - The start time of the data period.
- **endTime** (timestamp) - The end time of the data period.
- **createTime** (timestamp) - The time the report was created.
- **jobExpireTime** (timestamp) - The time the job will stop generating new reports.
- **downloadUrl** (string) - The URL to download the report.
```

--------------------------------

### GET reports.listJobsReports

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=fa

Lists all reports generated by a specific reporting job.

```APIDOC
## GET reports.listJobsReports

### Description
Lists reports created by a specific job.

### Method
GET

### Parameters
#### Path Parameters
- **jobId** (string) - Required - The ID of the job.

#### Query Parameters
- **onBehalfOfContentOwner** (string) - Optional - A content owner ID.
```

--------------------------------

### ViewController Implementation for YouTube API Interaction

Source: https://developers.google.com/youtube/v3/quickstart/ios

This implementation file configures Google Sign-In, sets up the UI elements, initializes the YouTube service, and handles the authentication callback to fetch channel data.

```objective-c
#import "ViewController.h"

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Configure Google Sign-in.
    GIDSignIn* signIn = [GIDSignIn sharedInstance];
    signIn.delegate = self;
    signIn.uiDelegate = self;
    signIn.scopes = [NSArray arrayWithObjects:kGTLRAuthScopeYouTubeReadonly, nil];
    [signIn signInSilently];

    // Add the sign-in button.
    self.signInButton = [[GIDSignInButton alloc] init];
    [self.view addSubview:self.signInButton];

    // Create a UITextView to display output.
    self.output = [[UITextView alloc] initWithFrame:self.view.bounds];
    self.output.editable = false;
    self.output.contentInset = UIEdgeInsetsMake(20.0, 0.0, 20.0, 0.0);
    self.output.autoresizingMask = UIViewAutoresizingFlexibleHeight | UIViewAutoresizingFlexibleWidth;
    self.output.hidden = true;
    [self.view addSubview:self.output];

    // Initialize the service object.
    self.service = [[GTLRYouTubeService alloc] init];
}

- (void)signIn:(GIDSignIn *)signIn
didSignInForUser:(GIDGoogleUser *)user
     withError:(NSError *)error {
    if (error != nil) {
        [self showAlert:@"Authentication Error" message:error.localizedDescription];
        self.service.authorizer = nil;
    } else {
        self.signInButton.hidden = true;
        self.output.hidden = false;
        self.service.authorizer = user.authentication.fetcherAuthorizer;
        [self fetchChannelResource];
    }
}


// Construct a query and retrieve the channel resource for the GoogleDevelopers
// YouTube channel. Display the channel title, description, and view count.
- (void)fetchChannelResource {
    GTLRYouTubeQuery_ChannelsList *query = 
    [GTLRYouTubeQuery_ChannelsList queryWithPart:@"snippet,statistics"];
  query.identifier = @"UC_x5XG1OV2P6uZZ5FSM9Ttw";
  // To retrieve data for the current user's channel, comment out the previous
  // line (query.identifier ...) and uncomment the next line (query.mine ...).
  // query.mine = true;

  [self.service executeQuery:query
                    delegate:self
           didFinishSelector:@selector(displayResultWithTicket:finishedWithObject:error:)];
}

// Process the response and display output
- (void)displayResultWithTicket:(GTLRServiceTicket *)ticket
             finishedWithObject:(GTLRYouTube_ChannelListResponse *)channels
                          error:(NSError *)error {
  if (error == nil) {
    NSMutableString *output = [[NSMutableString alloc] init];
    if (channels.items.count > 0) {
      [output appendString:@"Channel information:\n"];
      for (GTLRYouTube_Channel *channel in channels) {
        NSString *title = channel.snippet.title;
        NSString *description = channel.snippet.description;
        NSNumber *viewCount = channel.statistics.viewCount;
        [output appendFormat:@"Title: %@\nDescription: %@\nViewCount: %@\n", title, description, viewCount];
      }
    } else {
      [output appendString:@"Channel not found."];
    }
    self.output.text = output;
  } else {
    [self showAlert:@"Error" message:error.localizedDescription];
  }
}


// Helper for showing an alert
- (void)showAlert:(NSString *)title message:(NSString *)message {
    UIAlertController *alert = 
    [UIAlertController alertControllerWithTitle:title
                                        message:message
                                 preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction *ok = 
    [UIAlertAction actionWithTitle:@"OK"
                             style:UIAlertActionStyleDefault
                           handler:^(UIAlertAction * action) 
     {

```

--------------------------------

### GET /media/{reportUrl}

Source: https://developers.google.com/youtube/reporting/v1/code_samples/php?hl=es-419

Downloads a report file from the specified URL.

```APIDOC
## GET /media/{reportUrl}

### Description
Download the report specified by the URL.

### Method
GET

### Endpoint
/media/{reportUrl}

### Parameters
#### Path Parameters
- **reportUrl** (string) - Required - The URL of the report to be downloaded.

#### Query Parameters
- **alt** (string) - Required - Set to 'media' to indicate a media download.
```

--------------------------------

### GET /ownershipHistory.list

Source: https://developers.google.com/youtube/partner/revision_history

Retrieves the most recent ownership data for each content owner.

```APIDOC
## GET /ownershipHistory.list

### Description
Retrieves the most recent ownership data for each content owner. If a content owner has submitted data through multiple sources, the list includes the most recent data for each source.

### Method
GET
```

--------------------------------

### Initialize YouTube Reporting API Client (PHP)

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list

Initializes the YouTube Reporting API client and sets up the main logic for retrieving or downloading reports based on provided arguments.

```php
// Define an object that will be used to make all API requests.
$client = getClient();
// YouTube Reporting object used to make YouTube Reporting API requests.
$youtubeReporting = new Google_Service_YouTubeReporting($client);

if ($CONTENT_OWNER_ID) {
  if (!$DOWNLOAD_URL && !$JOB_ID) {
    listReportingJobs($youtubeReporting, $CONTENT_OWNER_ID,
                      $INCLUDE_SYSTEM_MANAGED);
  } else if ($JOB_ID) {
    listReportsForJob($youtubeReporting, $JOB_ID, $CONTENT_OWNER_ID);
  } else if ($DOWNLOAD_URL && $OUTPUT_FILE) {
    downloadReport($youtubeReporting, $DOWNLOAD_URL, $OUTPUT_FILE);
  }
}

?>
```

--------------------------------

### GET videoAdvertisingOptions.getEnabledAds

Source: https://developers.google.com/youtube/partner/revision_history

Retrieves enabled advertising options for a claimed video.

```APIDOC
## GET videoAdvertisingOptions.getEnabledAds

### Description
Retrieves the enabled advertising options for a specific claimed video.

### Method
GET

### Response
#### Success Response (200)
- **id** (string) - The ID that YouTube uses to uniquely identify the claimed video associated with the settings.
- **adBreaks** (list) - A list of objects containing information about ad break points.
- **adsOnEmbeds** (boolean) - Indicates whether YouTube can show ads when the video is played in an embedded player.
- **countriesRestriction** (list) - A list of objects identifying territories and ad formats used during playbacks.
```

--------------------------------

### GET /youtube/partner/v1/whitelists

Source: https://developers.google.com/youtube/partner/reference/rest

Retrieves a list of whitelisted channels for a content owner.

```APIDOC
## GET /youtube/partner/v1/whitelists

### Description
Retrieves a list of whitelisted channels for a content owner.

### Method
GET

### Endpoint
/youtube/partner/v1/whitelists
```

--------------------------------

### GET /spreadsheetTemplates

Source: https://developers.google.com/youtube/partner/reference/rest/v1/spreadsheetTemplate

Retrieves a list of spreadsheet templates for a content owner.

```APIDOC
## GET /spreadsheetTemplates

### Description
Retrieves a list of spreadsheet templates for a content owner.

### Method
GET

### Endpoint
/spreadsheetTemplates

### Response
#### Success Response (200)
- **status** (string) - The template status.
- **templateType** (string) - The template type.
- **templateName** (string) - The template name.
- **templateContent** (string) - The template content.
- **kind** (string) - The type of the API resource (youtubePartner#spreadsheetTemplate).
```

--------------------------------

### Upload Video and Manage Assets

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=ru

Demonstrates retrieving content owner IDs, performing resumable video uploads, and creating/updating assets.

```PHP
  try{

    // Call the contentOwners.list method to retrieve the ID of the content
    // owner associated with the currently authenticated user's account.
    $contentOwnersListResponse = $youtubePartner->contentOwners->listContentOwners(
        array('fetchMine' => true));
    $contentOwnerId = $contentOwnersListResponse['items'][0]['id'];

    // REPLACE this value with the path to the file you are uploading.
    $videoPath = "/path/to/file.mp4";

    // REPLACE this value with the ID that uniquely identifies the channel that
    // you are uploading to.
    $channelId = "CHANNEL_ID";

    // Create a snippet with title, description, tags and category ID
    // Create an asset resource and set its snippet metadata and type.
    // This example sets the video's title, description, keyword tags, and
    // video category.
    $snippet = new Google_Service_YouTube_VideoSnippet();
    $snippet->setTitle("Test title");
    $snippet->setDescription("Test description");
    $snippet->setTags(array("tag1", "tag2"));

    // Numeric video category. See
    // https://developers.google.com/youtube/v3/docs/videoCategories/list
    $snippet->setCategoryId("22");

    // Set the video's status to "public". Valid statuses are "public",
    // "private" and "unlisted".
    $status = new Google_Service_YouTube_VideoStatus();
    $status->privacyStatus = "public";

    // Associate the snippet and status objects with a new video resource.
    $video = new Google_Service_YouTube_Video();
    $video->setSnippet($snippet);
    $video->setStatus($status);

    // Specify the size of each chunk of data, in bytes. Set a higher value for
    // reliable connection as fewer chunks lead to faster uploads. Set a lower
    // value for better recovery on less reliable connections.
    $chunkSizeBytes = 1 * 1024 * 1024;

    // Setting the defer flag to true tells the client to return a request which can be called
    // with ->execute(); instead of making the API call immediately.
    $client->setDefer(true);

    // Create a request for the API's videos.insert method to create and upload the video.
    $insertRequest = $youtube->videos->insert("status,snippet", $video,
        array('onBehalfOfContentOwner' => $contentOwnerId,
            'onBehalfOfContentOwnerChannel' => $channelId));

    // Create a MediaFileUpload object for resumable uploads.
    $media = new Google_Http_MediaFileUpload(
        $client,
        $insertRequest,
        'video/*',
        null,
        true,
        $chunkSizeBytes
    );
    $media->setFileSize(filesize($videoPath));


    // Read the media file and upload it chunk by chunk.
    $status = false;
    $handle = fopen($videoPath, "rb");
    while (!$status && !feof($handle)) {
      $chunk = fread($handle, $chunkSizeBytes);
      $status = $media->nextChunk($chunk);
    }

    fclose($handle);

    // Set defer back to false to be able to make other calls after the file upload.
    $client->setDefer(false);

    $videoId = $status['id'];

    // Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId, $ownership,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    // Define a monetization policy for the asset.
```

--------------------------------

### GET /youtube/partner/v1/references/{referenceId}

Source: https://developers.google.com/youtube/partner/reference/rest/v1/references/get

Retrieves information about a specific YouTube reference.

```APIDOC
## GET /youtube/partner/v1/references/{referenceId}

### Description
Retrieves information about the specified reference.

### Method
GET

### Endpoint
https://youtubepartner.googleapis.com/youtube/partner/v1/references/{referenceId}

### Parameters
#### Path Parameters
- **referenceId** (string) - Required - The YouTube reference ID of the reference being retrieved.

#### Query Parameters
- **onBehalfOfContentOwner** (string) - Optional - Identifies the content owner that the user is acting on behalf of.

### Response
#### Success Response (200)
- **Reference** (object) - The response body contains an instance of the Reference object.

### Authorization
Requires the following OAuth scope: https://www.googleapis.com/auth/youtubepartner
```

--------------------------------

### AppDelegate Implementation for Google Sign-In

Source: https://developers.google.com/youtube/v3/quickstart/ios

This implementation file configures the AppDelegate to initialize Google Sign-In with a client ID and handle URL callbacks for authentication.

```objective-c
#import "AppDelegate.h"

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Initialize Google sign-in.
    [GIDSignIn sharedInstance].clientID = @"<YOUR_CLIENT_ID>";

    return YES;
}

- (BOOL)application:(UIApplication *)application
            openURL:(NSURL *)url
  sourceApplication:(NSString *)sourceApplication
         annotation:(id)annotation {
    return [[GIDSignIn sharedInstance] handleURL:url
                               sourceApplication:sourceApplication
                                      annotation:annotation];
}


@end
```

--------------------------------

### GET /youtube/partner/v1/claims/{claimId}

Source: https://developers.google.com/youtube/partner/reference/rest/v1/claims/get

Retrieves a specific claim by its unique claimId.

```APIDOC
## GET https://youtubepartner.googleapis.com/youtube/partner/v1/claims/{claimId}

### Description
Retrieves a specific claim by ID.

### Method
GET

### Endpoint
https://youtubepartner.googleapis.com/youtube/partner/v1/claims/{claimId}

### Parameters
#### Path Parameters
- **claimId** (string) - Required - The claim ID of the claim being retrieved.

#### Query Parameters
- **onBehalfOfContentOwner** (string) - Optional - Identifies the content owner that the user is acting on behalf of.

### Request Body
The request body must be empty.

### Response
#### Success Response (200)
- **Claim** (object) - Returns an instance of the Claim object.
```

--------------------------------

### Initialize OAuth2 Client and Define Scopes

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=ar

Sets up the OAuth2 client with your application's credentials and defines the necessary API scopes for accessing YouTube Partner Program and Google Calendar data. Ensure you replace placeholder values with your actual credentials.

```javascript
const http = require('http');
const https = require('https');
const url = require('url');
const { google } = require('googleapis');
const crypto = require('crypto');
const express = require('express');
const session = require('express-session');

/**
 * To use OAuth2 authentication, we need access to a CLIENT_ID, CLIENT_SECRET, AND REDIRECT_URI.
 * To get these credentials for your application, visit
 * https://console.cloud.google.com/apis/credentials.
 */
const oauth2Client = new google.auth.OAuth2(
  YOUR_CLIENT_ID,
  YOUR_CLIENT_SECRET,
  YOUR_REDIRECT_URL
);

// Access scopes for two non-Sign-In scopes: Read-only Drive activity and Google Calendar.
const scopes = [
  'https://www.googleapis.com/auth/youtubepartner',
  'https://www.googleapis.com/auth/calendar.readonly'
];

/* Global variable that stores user credential in this code example.
 * ACTION ITEM for developers:
 *   Store user's refresh token in your data store if
 *   incorporating this code into your real app.
 *   For more information on handling refresh tokens,
 *   see https://github.com/googleapis/google-api-nodejs-client#handling-refresh-tokens
 */
let userCredential = null;
```

--------------------------------

### GET /youtube/partner/v1/assets

Source: https://developers.google.com/youtube/partner/reference/rest/v1/assets/list

Retrieves a paginated list of assets for a content owner.

```APIDOC
## GET /youtube/partner/v1/assets

### Description
Retrieves a list of assets. Authorization requires the `https://www.googleapis.com/auth/youtubepartner` scope.

### Method
GET

### Endpoint
`https://youtubepartner.googleapis.com/youtube/partner/v1/assets`

### Parameters
#### Query Parameters
- **fetchMatchPolicy** (boolean) - Optional - Whether to include match policy information.
- **fetchMetadata** (boolean) - Optional - Whether to include asset metadata.
- **fetchOwnership** (boolean) - Optional - Whether to include ownership information.
- **fetchOwnershipConflicts** (boolean) - Optional - Whether to include ownership conflicts.
- **id** (string) - Optional - Filter by specific asset ID.
- **onBehalfOfContentOwner** (string) - Optional - The content owner ID to act on behalf of.

### Response
#### Success Response (200)
- **kind** (string) - The type of the API resource.
- **items** (array) - A list of asset resources.
```

--------------------------------

### Create a Claim and Set Advertising Options

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=ar

Uses the YouTube Partner API to associate a video with an asset via a claim and enables TrueView ad formats.

```php
$claim = new Google_Service_YouTubePartner_Claim();
    $claim->setAssetId($assetId);
    $claim->setVideoId($videoId);
    $claim->setPolicy($policy);
    $claim->setContentType("audiovisual");

    // Insert the created claim.
    $claimInsertResponse = $youtubePartner->claims->insert($claim,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    # Enable ads for the video. This example enables the TrueView ad format.
    $option = new Google_Service_YouTubePartner_VideoAdvertisingOption();
    $option->setAdFormats(array("trueview_instream"));
    $setAdvertisingResponse = $youtubePartner->videoAdvertisingOptions->update(
        $videoId, $option, array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### Main Execution Script

Source: https://developers.google.com/youtube/analytics/v1/code_samples/python?hl=ja

Orchestrates the authentication, user input, and job creation process.

```python
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  # The 'name' option specifies the name that will be used for the reporting job.
  parser.add_argument('--content-owner', default='',
      help='ID of content owner for which you are retrieving jobs and reports.')
  parser.add_argument('--include-system-managed', default=False,
      help='Whether the API response should include system-managed reports')
  parser.add_argument('--name', default='',
    help='Name for the reporting job. The script prompts you to set a name ' +
         'for the job if you do not provide one using this argument.')
  parser.add_argument('--report-type', default=None,
    help='The type of report for which you are creating a job.')
  args = parser.parse_args()

  youtube_reporting = get_authenticated_service()

  try:
    # Prompt user to select report type if they didn't set one on command line.
    if not args.report_type:
      if list_report_types(youtube_reporting,
                           onBehalfOfContentOwner=args.content_owner,
                           includeSystemManaged=args.include_system_managed):
        args.report_type = get_report_type_id_from_user()
    # Prompt user to set job name if not set on command line.
    if not args.name:
      args.name = prompt_user_to_set_job_name()
    # Create the job.
    if args.report_type:
      create_reporting_job(youtube_reporting,
                           args,
                           onBehalfOfContentOwner=args.content_owner)
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
```

--------------------------------

### GET ownership.get

Source: https://developers.google.com/youtube/partner/guides/managing_composition_assets

Returns the ownership data defined for a specified asset.

```APIDOC
## GET ownership.get

### Description
Returns the ownership data defined for a specified asset. If a viewId is provided, it returns the canonical set of ownership data for the composition view.

### Method
GET

### Parameters
#### Query Parameters
- **assetId** (string) - Required - Identifies the asset.
```

--------------------------------

### GET /youtubepartner/v1/contentOwners

Source: https://developers.google.com/youtube/partner/guides/auth/devices

Retrieves a list of content owners for the authenticated user.

```APIDOC
## GET /youtubepartner/v1/contentOwners

### Description
Retrieves a list of content owners associated with the authenticated user.

### Method
GET

### Endpoint
https://www.googleapis.com/youtubepartner/v1/contentOwners

### Parameters
#### Query Parameters
- **fetchMine** (boolean) - Required - Set to true to fetch content owners for the authenticated user.
- **access_token** (string) - Optional - The access token for authentication if not using the Authorization header.
```

--------------------------------

### Call YouTube API using Ruby Client Library

Source: https://developers.google.com/youtube/reporting/revision_history

Demonstrates how to call the YouTube API using the Ruby client library. Ensure the Ruby client library is set up correctly.

```ruby
require "google/apis/youtube_v3"
require "googleauth"

api_key = "YOUR_API_KEY"
youtube = Google::Apis::YoutubeV3::YouTubeService.new
youtube.key = api_key

response = youtube.list_channel("snippet,statistics", id: "UCBR8-60-B28hp2BmDPdntcQ") # Example Channel ID
puts response.to_json
```

--------------------------------

### Select User Account with Permissions

Source: https://developers.google.com/youtube/v3/quickstart/android?hl=fa

Handles account selection by checking for GET_ACCOUNTS permission and launching an account picker if necessary.

```java
@AfterPermissionGranted(REQUEST_PERMISSION_GET_ACCOUNTS)
    private void chooseAccount() {
        if (EasyPermissions.hasPermissions(
                this, Manifest.permission.GET_ACCOUNTS)) {
            String accountName = getPreferences(Context.MODE_PRIVATE)
                    .getString(PREF_ACCOUNT_NAME, null);
            if (accountName != null) {
                mCredential.setSelectedAccountName(accountName);
                getResultsFromApi();
            } else {
                // Start a dialog from which the user can choose an account
                startActivityForResult(
                        mCredential.newChooseAccountIntent(),
                        REQUEST_ACCOUNT_PICKER);
            }
        } else {
            // Request the GET_ACCOUNTS permission via a user dialog
            EasyPermissions.requestPermissions(
                    this,
                    "This app needs to access your Google account (via Contacts).",
                    REQUEST_PERMISSION_GET_ACCOUNTS,
                    Manifest.permission.GET_ACCOUNTS);
        }
    }
```

--------------------------------

### GET /youtubeAnalytics/v1/reports

Source: https://developers.google.com/youtube/analytics/v1/sample-application

Queries YouTube Analytics data for a specific video.

```APIDOC
## GET /youtubeAnalytics/v1/reports

### Description
Queries YouTube Analytics data for a specific video.

### Method
GET

### Parameters
#### Query Parameters
- **start-date** (string) - Required - The start date for the report (YYYY-MM-DD).
- **end-date** (string) - Required - The end date for the report (YYYY-MM-DD).
- **ids** (string) - Required - A comma-separated list of channel IDs, formatted as 'channel==channelId'.
- **dimensions** (string) - Required - The dimension for the report (e.g., 'day').
- **sort** (string) - Optional - The sort order for the report.
- **metrics** (string) - Required - The metrics to retrieve (e.g., 'views').
- **filters** (string) - Required - Filters for the report (e.g., 'video==videoId').
```

--------------------------------

### GET /youtube/v3/videos

Source: https://developers.google.com/youtube/analytics/v1/sample-application

Retrieves metadata for one or more videos based on their IDs.

```APIDOC
## GET /youtube/v3/videos

### Description
Retrieves metadata for one or more videos based on their IDs.

### Method
GET

### Parameters
#### Query Parameters
- **id** (string) - Required - A comma-separated string of video IDs.
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more resource properties that the API response will include.
```

--------------------------------

### GET reports.query

Source: https://developers.google.com/youtube/analytics/v1/content_owner_video_reports

Retrieves analytics reports for a specified content owner.

```APIDOC
## GET reports.query

### Description
Retrieves a content owner report containing metrics for channels linked to a specified YouTube content owner.

### Method
GET

### Endpoint
reports.query

### Parameters
#### Query Parameters
- **ids** (string) - Required - The content owner ID in the format 'contentOwner==OWNER_NAME'.

### Request Example
GET /reports.query?ids=contentOwner==OWNER_NAME&startDate=2023-01-01&endDate=2023-01-31&metrics=views,estimatedRevenue&dimensions=day
```

--------------------------------

### Initialize YouTube Partner API OAuth 2.0 Configuration

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=ko

Defines the client secrets file path, API scopes, and initializes the Flask application instance.

```python
# -*- coding: utf-8 -*-

import os
import flask
import json
import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

# This variable specifies the name of a file that contains the OAuth 2.0
# information for this application, including its client_id and client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# The OAuth 2.0 access scope allows for access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtubepartner',
          'https://www.googleapis.com/auth/calendar.readonly']
API_SERVICE_NAME = 'youtubePartner'
API_VERSION = 'v1'

app = flask.Flask(__name__)
# Note: A secret key is included in the sample so that it works.
# If you use this code in your application, replace this with a truly secret
```

--------------------------------

### Create a YouTube Claim and Set Advertising Options

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=fr

Configures a policy rule, creates a claim for a video asset, and updates advertising formats for the claimed video.

```php
$policyRule = new Google_Service_YouTubePartner_PolicyRule();
    $policyRule->setAction("monetize");
    $policy->setRules(array($policyRule));

    // Create a claim resource. Identify the video being claimed, the asset
    // that represents the claimed content, the type of content being claimed,
    // and the policy that you want to apply to the claimed video.
    $claim = new Google_Service_YouTubePartner_Claim();
    $claim->setAssetId($assetId);
    $claim->setVideoId($videoId);
    $claim->setPolicy($policy);
    $claim->setContentType("audiovisual");

    // Insert the created claim.
    $claimInsertResponse = $youtubePartner->claims->insert($claim,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    # Enable ads for the video. This example enables the TrueView ad format.
    $option = new Google_Service_YouTubePartner_VideoAdvertisingOption();
    $option->setAdFormats(array("trueview_instream"));
    $setAdvertisingResponse = $youtubePartner->videoAdvertisingOptions->update(
        $videoId, $option, array('onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### Initialize YT.Player with player parameters

Source: https://developers.google.com/youtube/iframe_api_reference

Configures player behavior using playerVars, such as enabling autoplay and hiding controls.

```javascript
function onYouTubeIframeAPIReady() {
  var player;
  player = new YT.Player('player', {
    videoId: 'M7lc1UVf-VE',
    playerVars: { 'autoplay': 1, 'controls': 0 },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange,
      'onError': onPlayerError
    }
  });
}
```

--------------------------------

### GET /subscriptions/list

Source: https://developers.google.com/youtube/v3/revision_history

Retrieves a list of the authenticated user's subscriptions or subscribers.

```APIDOC
## GET /subscriptions/list

### Description
Retrieves a list of subscriptions. Use the mySubscribers parameter to retrieve the authenticated user's subscribers.

### Method
GET

### Endpoint
/subscriptions/list

### Parameters
#### Query Parameters
- **mySubscribers** (boolean) - Optional - If true, retrieves a list of the authenticated user's subscribers.
```

--------------------------------

### GET /videos.list

Source: https://developers.google.com/youtube/v3/revision_history

Retrieves video resources with optional live streaming metadata.

```APIDOC
## GET /videos.list

### Description
Retrieves a list of videos. You can now include the `liveStreamingDetails` part to get metadata about live broadcasts.

### Method
GET

### Endpoint
/videos.list

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more resource properties that the API response will include. Include `liveStreamingDetails` to retrieve live broadcast metadata.
```

--------------------------------

### Initialize Google::Auth::WebUserAuthorizer

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Set up a WebUserAuthorizer for handling user authorization flows in a web application. Requires client ID, scope, token store, and callback URI.

```ruby
authorizer = Google::Auth::WebUserAuthorizer.new(client_id, scope,
                                                token_store, callback_uri)
```

--------------------------------

### GET /channels.list

Source: https://developers.google.com/youtube/v3/revision_history

Retrieves channel information, now supporting lookup by YouTube handle.

```APIDOC
## GET /channels.list

### Description
Retrieves a list of channels that match the request criteria.

### Method
GET

### Endpoint
/youtube/v3/channels

### Parameters
#### Query Parameters
- **forHandle** (string) - Optional - Retrieve information about a channel by specifying its YouTube handle.
```

--------------------------------

### Parse Command-Line Options

Source: https://developers.google.com/youtube/partner/guides/upload?hl=id

Parses command-line arguments for video uploads, including file path, title, description, category, keywords, privacy status, policy ID, and channel ID. Ensure all required options are provided.

```python
def parse_options():
  parser = OptionParser()
  parser.add_option("--file", dest="file", help="Video file to upload")
  parser.add_option("--title", dest="title", help="Video title",
    default="Test Title")
  parser.add_option("--description", dest="description",
    help="Video description",
    default="Test Description")
  parser.add_option("--category", dest="category",
    help="Numeric video category. " +
      "See https://developers.google.com/youtube/v3/docs/videoCategories/list",
    default="22")
  parser.add_option("--keywords", dest="keywords",
    help="Video keywords, comma separated", default="")
  parser.add_option("--privacyStatus", dest="privacyStatus",
    help="Video privacy status: public, private or unlisted",
    default="public")
  parser.add_option("--policyId", dest="policyId",
    help="Optional id of a saved claim policy")
  parser.add_option("--channelId", dest="channelId",
    help="Id of the channel to upload to. Must be managed by your CMS account")
  (options, args) = parser.parse_args()

  return options
```

--------------------------------

### GET /search/list

Source: https://developers.google.com/youtube/v3/revision_history?hl=fa

Retrieves search results with new filtering and sorting capabilities.

```APIDOC
## GET /search/list

### Description
Retrieves search results with new filtering and sorting capabilities.

### Method
GET

### Endpoint
/search/list

### Parameters
#### Query Parameters
- **forMine** (boolean) - Optional - Restricts search to the authenticated user's videos.
- **order** (string) - Optional - Sorts results (e.g., 'title', 'videoCount').
- **safeSearch** (string) - Optional - Indicates whether search results should include restricted content.
```

--------------------------------

### GET /channels

Source: https://developers.google.com/youtube/v3/revision_history?hl=id

Retrieves channel information including the new contentOwnerDetails part.

```APIDOC
## GET /channels

### Description
Retrieves channel details. The API now supports the `contentOwnerDetails` part for the `channel` resource, which contains data relevant to YouTube partners linked to the channel.

### Method
GET

### Endpoint
/channels

### Parameters
#### Query Parameters
- **part** (string) - Required - The `part` parameter must include `contentOwnerDetails` to retrieve the new information.
```

--------------------------------

### Initialize and execute API requests

Source: https://developers.google.com/youtube/reporting/v1/code_samples/php

Initializes the YouTube Reporting service and routes requests based on provided variables.

```php
// Define an object that will be used to make all API requests.
$client = getClient();
// YouTube Reporting object used to make YouTube Reporting API requests.
$youtubeReporting = new Google_Service_YouTubeReporting($client);

if ($CONTENT_OWNER_ID) {
  if (!$DOWNLOAD_URL && !$JOB_ID) {
    listReportingJobs($youtubeReporting, $CONTENT_OWNER_ID,
                      $INCLUDE_SYSTEM_MANAGED);
  } else if ($JOB_ID) {
    listReportsForJob($youtubeReporting, $JOB_ID, $CONTENT_OWNER_ID);
  } else if ($DOWNLOAD_URL && $OUTPUT_FILE) {
    downloadReport($youtubeReporting, $DOWNLOAD_URL, $OUTPUT_FILE);
  }
}
```

--------------------------------

### POST /playlists

Source: https://developers.google.com/youtube/v3/docs/playlists/insert?hl=ar

Creates a playlist. A call to this method has a quota cost of 50 units. This example creates a new playlist in your channel. You must use the `snippet.title` property to set the playlist's title. All of the other properties are optional.

```APIDOC
## POST /playlists

### Description
Creates a new playlist in your channel. You must use the `snippet.title` property to set the playlist's title. All of the other properties are optional.

### Method
POST

### Endpoint
https://www.googleapis.com/youtube/v3/playlists

### Parameters
#### Request Body
- **snippet.title** (string) - Required - The title of the playlist.

### Request Example
{
  "snippet": {
    "title": "My Awesome Playlist"
  }
}

### Response
#### Success Response (200)
- **kind** (string) - Identifies this as a Playlist resource.
- **etag** (string) - The ETag of the response.
- **id** (string) - The ID of the created playlist.
- **snippet** (object) - The snippet object contains basic details about the playlist.
  - **publishedAt** (string) - The date and time that the playlist was created.
  - **channelId** (string) - The ID of the channel that owns the playlist.
  - **title** (string) - The title of the playlist.
  - **description** (string) - The description of the playlist.
  - **thumbnails** (object) - A map of image files and their sizes.
  - **channelTitle** (string) - The title of the channel that owns the playlist.
  - **defaultLanguage** (string) - The default language of the playlist.
  - **localized** (object) - The localized title and description of the playlist.
    - **title** (string) - The localized title of the playlist.
    - **description** (string) - The localized description of the playlist.
  - **defaultTab** (string) - The default tab for the playlist.
  - **publishedAt** (string) - The date and time that the playlist was created.

### Response Example
{
  "kind": "youtube#playlist",
  "etag": "_XYZabc123",
  "id": "PL_abcdefg12345",
  "snippet": {
    "publishedAt": "2023-01-01T10:00:00Z",
    "channelId": "UCxxxxxxxxxxxxxxxxx",
    "title": "My Awesome Playlist",
    "description": "",
    "thumbnails": {
      "default": {
        "url": "https://example.com/default.jpg"
      }
    },
    "channelTitle": "My Channel",
    "defaultLanguage": "en",
    "localized": {
      "title": "My Awesome Playlist",
      "description": ""
    },
    "defaultTab": "videos"
  }
}

### Authorization
This request requires authorization with at least one of the following scopes:
- `https://www.googleapis.com/auth/youtubepartner`
- `https://www.googleapis.com/auth/youtube`
- `https://www.googleapis.com/auth/youtube.force-ssl`
```

--------------------------------

### GET /liveStreams

Source: https://developers.google.com/youtube/v3/live/docs/liveStreams/list?hl=es

Retrieves a list of live streams that match the request criteria.

```APIDOC
## GET /liveStreams

### Description
Retrieves a list of live streams that match the request criteria.

### Method
GET

### Endpoint
/liveStreams

### Parameters
#### Query Parameters
- **part** (string) - Required - Specifies a comma-separated list of one or more liveStream resource properties (id, snippet, cdn, status).
- **id** (string) - Optional - Comma-separated list of YouTube stream IDs.
- **mine** (boolean) - Optional - If true, returns streams owned by the authenticated user.
- **maxResults** (unsigned integer) - Optional - Maximum number of items to return (0-50).
- **onBehalfOfContentOwner** (string) - Optional - CMS user acting on behalf of the content owner.
- **onBehalfOfContentOwnerChannel** (string) - Optional - YouTube channel ID for content partners.
- **pageToken** (string) - Optional - Identifies a specific page in the result set.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type.
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - Token for the next page.
- **prevPageToken** (string) - Token for the previous page.
- **pageInfo** (object) - Paging information.
- **items** (list) - List of live streams.

#### Response Example
{
  "kind": "youtube#liveStreamListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "prevPageToken": "string",
  "pageInfo": {
    "totalResults": 0,
    "resultsPerPage": 0
  },
  "items": []
}
```

--------------------------------

### GET /liveBroadcasts

Source: https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list?hl=th

Retrieves a list of live broadcasts that match the request criteria.

```APIDOC
## GET /liveBroadcasts

### Description
Retrieves a list of live broadcasts that match the request criteria.

### Method
GET

### Endpoint
/liveBroadcasts

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include.
- **broadcastStatus** (string) - Optional - Filter broadcasts by their status.
- **broadcastType** (string) - Optional - Filter broadcasts by their type.
- **id** (string) - Optional - Specifies a comma-separated list of YouTube broadcast IDs.
- **maxResults** (integer) - Optional - The maximum number of items that should be returned in the result set.
- **mine** (boolean) - Optional - If set to true, returns broadcasts owned by the authenticated user.
- **onBehalfOfContentOwner** (string) - Optional - Indicates that the request is being made on behalf of a content owner.
- **onBehalfOfContentOwnerChannel** (string) - Optional - Indicates that the request is being made on behalf of a specific channel.
- **pageToken** (string) - Optional - The token that identifies a specific page in the result set.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type (youtube#liveBroadcastListResponse).
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - Token to retrieve the next page.
- **prevPageToken** (string) - Token to retrieve the previous page.
- **pageInfo** (object) - Encapsulates paging information.
- **items** (list) - A list of broadcasts that match the request criteria.
```

--------------------------------

### POST /playlists

Source: https://developers.google.com/youtube/v3/docs/playlists/insert?hl=es-419

Creates a playlist. A call to this method has a quota cost of 50 units. This example creates a new playlist in your channel. You must use the `snippet.title` property to set the playlist's title. All of the other properties are optional.

```APIDOC
## POST /playlists

### Description
Creates a new playlist in your channel. You must use the `snippet.title` property to set the playlist's title. All of the other properties are optional.

### Method
POST

### Endpoint
https://www.googleapis.com/youtube/v3/playlists

### Parameters
#### Request Body
- **snippet.title** (string) - Required - The title of the playlist.

### Request Example
{
  "snippet": {
    "title": "My Awesome Playlist"
  }
}

### Response
#### Success Response (200)
- **kind** (string) - Identifies this as a playlist resource.
- **etag** (string) - The ETag of the response.
- **id** (string) - The ID of the created playlist.
- **snippet** (object) - The snippet object contains basic details about the playlist.
  - **publishedAt** (string) - The date and time that the playlist was created.
  - **channelId** (string) - The ID of the channel that owns the playlist.
  - **title** (string) - The title of the playlist.
  - **description** (string) - The description of the playlist.
  - **thumbnails** (object) - A map of thumbnail sizes to URIs. For example:
    - **default** (object)
      - **url** (string)
    - **medium** (object)
      - **url** (string)
    - **high** (object)
      - **url** (string)
  - **channelTitle** (string) - The title of the channel that owns the playlist.
  - **localized** (object)
    - **title** (string)
    - **description** (string)
  - **defaultLanguage** (string)
  - **defaultLanguageId** (string)
  - **tags** (array of strings)
  - **defaultLanguage** (string)
  - **defaultLanguageId** (string)
  - **tags** (array of strings)

### Errors
Refer to the YouTube Data API error codes documentation.

### Authorization
This request requires authorization with at least one of the following scopes:
- `https://www.googleapis.com/auth/youtubepartner`
- `https://www.googleapis.com/auth/youtube`
- `https://www.googleapis.com/auth/youtube.force-ssl`
```

--------------------------------

### GET /liveBroadcasts

Source: https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list?hl=bn

Describes the structure of the response returned when listing live broadcasts.

```APIDOC
## GET /liveBroadcasts

### Description
Retrieves a list of live broadcasts that match the request criteria.

### Method
GET

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type (youtube#liveBroadcastListResponse).
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - Token to retrieve the next page of results.
- **prevPageToken** (string) - Token to retrieve the previous page of results.
- **pageInfo** (object) - Encapsulates paging information.
  - **totalResults** (integer) - Total number of results in the result set.
  - **resultsPerPage** (integer) - Number of results included in the response.
- **items** (list) - A list of broadcasts that match the request criteria.

### Errors
- **insufficientPermissions** (insufficientLivePermissions) - The request is not authorized to retrieve the live broadcast.
- **insufficientPermissions** (liveStreamingNotEnabled) - The user is not enabled to stream live video on YouTube.
```

--------------------------------

### Install Google API Client Library for Python

Source: https://developers.google.com/youtube/v3/code_samples/code_snippet_instructions

Upgrade the Google API client library for Python using pip. This is a prerequisite for running Python code samples.

```bash
pip install --upgrade google-api-python-client
```

--------------------------------

### Complete YouTube Partner API Sample Script

Source: https://developers.google.com/youtube/partner/guides/upload

A full Python script demonstrating video upload, claiming, and monetization using the YouTube Partner API. Includes command-line argument parsing and retry logic.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample for Youtube Partner API.

Command-line application that creates an asset, uploads and claims a video for that asset.

Usage:
  $ python upload_monetize_video_example.py --file=VIDEO_FILE --channelID=CHANNEL_ID \
      [--title=VIDEO_TITLE] [--description=VIDEO_DESCRIPTION] [--category=CATEGORY_ID] \
      [--keywords=KEYWORDS] [--privacyStatus=PRIVACY_STATUS] [--policyId=POLICY_ID] 

You can also get help on all the command-line flags the program understands
by running:

  $ python upload_monetize_video_example.py --help
"""

__author__ = 'jeffy+pub@google.com (Jeffrey Posnick)'

import httplib
import httplib2
import logging
import os
import random
import sys
import time

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run
from optparse import OptionParser


# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, httplib.NotConnected,
  httplib.IncompleteRead, httplib.ImproperConnectionState,
  httplib.CannotSendRequest, httplib.CannotSendHeader,
  httplib.ResponseNotReady, httplib.BadStatusLine,)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = (500, 502, 503, 504,)

# The message associated with the HTTP 401 error that's returned when a request
# is authorized by a user whose account is not associated with a YouTube
# content owner.
INVALID_CREDENTIALS = "Invalid Credentials"

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from

```

--------------------------------

### GET /youtube.playlists.list (Authenticated User)

Source: https://developers.google.com/youtube/v3/guides/implementation/playlists?hl=es

Retrieves the playlists of the currently authenticated user.

```APIDOC
## GET /youtube.playlists.list

### Description
Retrieves the playlists of the currently authenticated user.

### Method
GET

### Endpoint
/youtube.playlists.list

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include.
- **mine** (boolean) - Required - Set to true to retrieve playlists owned by the authenticated user.
```

--------------------------------

### Initialize Video Upload

Source: https://developers.google.com/youtube/v3/guides/uploading_a_video?hl=ar

Prepares the video metadata and initiates a resumable upload to the YouTube Data API. Handles tags, title, description, category, and privacy status.

```python
def initialize_upload(youtube, options):
  tags = None
  if options.keywords:
    tags = options.keywords.split(",")

  body=dict(
    snippet=dict(
      title=options.title,
      description=options.description,
      tags=tags,
      categoryId=options.category
    ),
    status=dict(
      privacyStatus=options.privacyStatus
    )
  )

  # Call the API's videos.insert method to create and upload the video.
  insert_request = youtube.videos().insert(
    part=",".join(body.keys()),
    body=body,
    # The chunksize parameter specifies the size of each chunk of data, in
    # bytes, that will be uploaded at a time. Set a higher value for
    # reliable connections as fewer chunks lead to faster uploads. Set a lower
    # value for better recovery on less reliable connections.
    #
    # Setting "chunksize" equal to -1 in the code below means that the entire
    # file will be uploaded in a single HTTP request. (If the upload fails,
    # it will still be retried where it left off.) This is usually a best
    # practice, but if you're using Python older than 2.6 or if you're
    # running on App Engine, you should set the chunksize to something like
    # 1024 * 1024 (1 megabyte).
    media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True))

  resumable_upload(insert_request)
```

--------------------------------

### GET /captions.list

Source: https://developers.google.com/youtube/v3/guides/implementation/captions

Retrieves a list of caption tracks associated with a specific video.

```APIDOC
## GET /captions.list

### Description
Retrieves a list of caption tracks that are available for a specific video. Requires OAuth 2.0 authorization.

### Method
GET

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more caption resource properties that the API response will include.
- **videoId** (string) - Required - The YouTube video ID that uniquely identifies the video for which you are retrieving captions.
```

--------------------------------

### GET /videos

Source: https://developers.google.com/youtube/v3/docs/videos/list?hl=bn

Retrieves a list of videos based on specified filters or IDs.

```APIDOC
## GET /videos

### Description
Returns a list of videos that match the API request parameters.

### Method
GET

### Endpoint
/videos

### Parameters
#### Query Parameters
- **part** (string) - Required - Comma-separated list of one or more video resource properties (e.g., snippet, contentDetails, statistics).
- **chart** (string) - Optional - Identifies the chart to retrieve (e.g., mostPopular).
- **id** (string) - Optional - Comma-separated list of YouTube video IDs.
- **myRating** (string) - Optional - Returns videos liked or disliked by the authenticated user (like, dislike).
- **hl** (string) - Optional - Language code for localized resource metadata.
- **maxHeight** (unsigned integer) - Optional - Maximum height of the embedded player (72-8192).
- **maxResults** (unsigned integer) - Optional - Maximum number of items to return (1-50).
- **maxWidth** (unsigned integer) - Optional - Maximum width of the embedded player (72-8192).
- **onBehalfOfContentOwner** (string) - Optional - CMS user acting on behalf of a content owner.
- **pageToken** (string) - Optional - Token to retrieve the next page of results.
```

--------------------------------

### Initialize Authenticated API Services

Source: https://developers.google.com/youtube/partner/code_samples/python?hl=ja

Handles OAuth 2.0 flow and builds the YouTube and YouTube Partner service objects.

```python
# Authorize the request and store authorization credentials.
def get_authenticated_services(args):
  flow = flow_from_clientsecrets(
    CLIENT_SECRETS_FILE,
    scope=" ".join(YOUTUBE_SCOPES),
    message=MISSING_CLIENT_SECRETS_MESSAGE
  )

  storage = Storage(CACHED_CREDENTIALS_FILE)
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))

  youtube_partner = build(YOUTUBE_CONTENT_ID_API_SERVICE_NAME,
    YOUTUBE_CONTENT_ID_API_VERSION,
    http=credentials.authorize(httplib2.Http()),
    static_discovery=False)

  return (youtube, youtube_partner)
```

--------------------------------

### GET /youtube/v3/videos

Source: https://developers.google.com/youtube/v3/docs/videos/list?hl=bn

Retrieves a list of videos that match the API request parameters.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/videos

### Description
Returns a list of videos that match the API request parameters. A call to this method has a quota cost of 1 unit.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/videos
```

--------------------------------

### Upload Video and Manage Assets

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=es-419

Demonstrates retrieving content owner IDs, performing chunked video uploads, and creating/updating assets with ownership metadata.

```php
  try{

    // Call the contentOwners.list method to retrieve the ID of the content
    // owner associated with the currently authenticated user's account.
    $contentOwnersListResponse = $youtubePartner->contentOwners->listContentOwners(
        array('fetchMine' => true));
    $contentOwnerId = $contentOwnersListResponse['items'][0]['id'];

    // REPLACE this value with the path to the file you are uploading.
    $videoPath = "/path/to/file.mp4";

    // REPLACE this value with the ID that uniquely identifies the channel that
    // you are uploading to.
    $channelId = "CHANNEL_ID";

    // Create a snippet with title, description, tags and category ID
    // Create an asset resource and set its snippet metadata and type.
    // This example sets the video's title, description, keyword tags, and
    // video category.
    $snippet = new Google_Service_YouTube_VideoSnippet();
    $snippet->setTitle("Test title");
    $snippet->setDescription("Test description");
    $snippet->setTags(array("tag1", "tag2"));

    // Numeric video category. See
    // https://developers.google.com/youtube/v3/docs/videoCategories/list
    $snippet->setCategoryId("22");

    // Set the video's status to "public". Valid statuses are "public",
    // "private" and "unlisted".
    $status = new Google_Service_YouTube_VideoStatus();
    $status->privacyStatus = "public";

    // Associate the snippet and status objects with a new video resource.
    $video = new Google_Service_YouTube_Video();
    $video->setSnippet($snippet);
    $video->setStatus($status);

    // Specify the size of each chunk of data, in bytes. Set a higher value for
    // reliable connection as fewer chunks lead to faster uploads. Set a lower
    // value for better recovery on less reliable connections.
    $chunkSizeBytes = 1 * 1024 * 1024;

    // Setting the defer flag to true tells the client to return a request which can be called
    // with ->execute(); instead of making the API call immediately.
    $client->setDefer(true);

    // Create a request for the API's videos.insert method to create and upload the video.
    $insertRequest = $youtube->videos->insert("status,snippet", $video,
        array('onBehalfOfContentOwner' => $contentOwnerId,
            'onBehalfOfContentOwnerChannel' => $channelId));

    // Create a MediaFileUpload object for resumable uploads.
    $media = new Google_Http_MediaFileUpload(
        $client,
        $insertRequest,
        'video/*',
        null,
        true,
        $chunkSizeBytes
    );
    $media->setFileSize(filesize($videoPath));


    // Read the media file and upload it chunk by chunk.
    $status = false;
    $handle = fopen($videoPath, "rb");
    while (!$status && !feof($handle)) {
      $chunk = fread($handle, $chunkSizeBytes);
      $status = $media->nextChunk($chunk);
    }

    fclose($handle);

    // Set defer back to false to be able to make other calls after the file upload.
    $client->setDefer(false);

    $videoId = $status['id'];

    // Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId, $ownership,
```

--------------------------------

### Search Assets by Labels

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=vi

This snippet demonstrates searching for assets that have specific labels. It includes examples for finding assets with all provided labels and assets with any of the provided labels.

```php
    // Search for assets having both 'label1' and 'label2' labels.
    // The results should include "asset1" after indexing is succesfully finished.
    $assetSearchResponse1 = $youtubePartner->assetSearch->listAssetSearch(
        array('labels' => "label1, label2", 'onBehalfOfContentOwner' => $contentOwnerId));
```

```php
    // Search for assets having at least one of 'label1' and 'label2' labels.
    // The results should include "asset1" and "asset2" after indexing is succesfully finished.
    $assetSearchResponse2 = $youtubePartner->assetSearch->listAssetSearch(
        array('labels' => "label1, label2", 'includeAnyProvidedlabel' => true,
            'onBehalfOfContentOwner' => $contentOwnerId));
```

--------------------------------

### GET /videos

Source: https://developers.google.com/youtube/v3/docs/videos/list?hl=de

Retrieves a list of videos that match the API request parameters.

```APIDOC
## GET /videos

### Description
Returns a list of videos that match the API request parameters.

### Method
GET

### Endpoint
/videos

### Parameters
#### Query Parameters
- **part** (string) - Required - Specifies a comma-separated list of one or more video resource properties that the API response will include.
- **chart** (string) - Optional - Identifies the chart that you want to retrieve (e.g., mostPopular).
- **id** (string) - Optional - Specifies a comma-separated list of the YouTube video ID(s) for the resource(s) that are being retrieved.
- **myRating** (string) - Optional - Returns videos liked or disliked by the authenticated user (like, dislike).
- **hl** (string) - Optional - Instructs the API to retrieve localized resource metadata for a specific application language.
- **maxHeight** (unsigned integer) - Optional - Specifies the maximum height of the embedded player (72-8192).
- **maxResults** (unsigned integer) - Optional - Specifies the maximum number of items that should be returned (1-50).
- **maxWidth** (unsigned integer) - Optional - Specifies the maximum width of the embedded player (72-8192).
- **onBehalfOfContentOwner** (string) - Optional - Indicates that the request's authorization credentials identify a YouTube CMS user acting on behalf of the content owner.
- **pageToken** (string) - Optional - Identifies a specific page in the result set that should be returned.
```

--------------------------------

### Implement Account Selection with Permissions

Source: https://developers.google.com/youtube/v3/quickstart/android?hl=ja

Handles account selection using EasyPermissions for GET_ACCOUNTS access and persists the selected account name.

```java
    @AfterPermissionGranted(REQUEST_PERMISSION_GET_ACCOUNTS)
    private void chooseAccount() {
        if (EasyPermissions.hasPermissions(
                this, Manifest.permission.GET_ACCOUNTS)) {
            String accountName = getPreferences(Context.MODE_PRIVATE)
                    .getString(PREF_ACCOUNT_NAME, null);
            if (accountName != null) {
                mCredential.setSelectedAccountName(accountName);
                getResultsFromApi();
            } else {
                // Start a dialog from which the user can choose an account
                startActivityForResult(
                        mCredential.newChooseAccountIntent(),
                        REQUEST_ACCOUNT_PICKER);
            }
        } else {
            // Request the GET_ACCOUNTS permission via a user dialog
            EasyPermissions.requestPermissions(
                    this,
                    "This app needs to access your Google account (via Contacts).",
                    REQUEST_PERMISSION_GET_ACCOUNTS,
                    Manifest.permission.GET_ACCOUNTS);
        }
    }
```

--------------------------------

### GET /youtube/v3/videos

Source: https://developers.google.com/youtube/v3/docs/videos/list?hl=es

Retrieves a list of videos that match the API request parameters.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/videos

### Description
Returns a list of videos that match the API request parameters. This method supports retrieving videos by ID, popularity, or user-specific ratings.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/videos

### Parameters
#### Query Parameters
- **id** (string) - Optional - A comma-separated list of YouTube video IDs.
- **regionCode** (string) - Optional - The country code for which to retrieve popular videos.
- **videoCategoryId** (string) - Optional - The category ID for filtering popular videos.
- **rating** (string) - Optional - Used to filter by user rating (e.g., 'like' or 'dislike').

### Request Example
GET https://www.googleapis.com/youtube/v3/videos?part=snippet&id=Ks-_Mh1QhMc

### Response
#### Success Response (200)
- **items** (array) - A list of video resources that match the request criteria.
```

--------------------------------

### Create and Configure an Asset

Source: https://developers.google.com/youtube/partner/code_samples/php

Inserts an asset resource and defines its ownership and monetization policy.

```php
// Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId, $ownership,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    // Define a monetization policy for the asset.
    $policy = new Google_Service_YouTubePartner_Policy();
    $policyRule = new Google_Service_YouTubePartner_PolicyRule();
    $policyRule->setAction("monetize");
    $policy->setRules(array($policyRule));

    // Create a claim resource. Identify the video being claimed, the asset
    // that represents the claimed content, the type of content being claimed,
    // and the policy that you want to apply to the claimed video.
```

--------------------------------

### GET /videoCategories

Source: https://developers.google.com/youtube/v3/docs/videoCategories/list?hl=zh-tw

Retrieves a list of video categories that can be used in YouTube videos.

```APIDOC
## GET /videoCategories

### Description
Retrieves a list of video categories that can be used in YouTube videos.

### Method
GET

### Endpoint
/videoCategories

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more resource properties that the API response will include.
- **hl** (string) - Optional - The hl parameter specifies the language that should be used for text values in the API response.
- **id** (string) - Optional - The id parameter specifies a comma-separated list of video category IDs for the resources that you are retrieving.
- **regionCode** (string) - Optional - The regionCode parameter instructs the API to return the list of video categories available in the specified country.

### Response
#### Success Response (200)
- **items** (array) - A list of video categories that match the API request parameters.

#### Error Handling
- **404 (notFound)**: videoCategoryNotFound - The video category identified by the id parameter cannot be found.
```

--------------------------------

### Initialize YouTube Reporting API Service

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=de

Sets up the OAuth 2.0 flow and builds the API service object.

```python
import argparse
import os

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains

# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = 'client_secret.json'

# This OAuth 2.0 access scope allows for read access to the YouTube Analytics monetary reports for
# authenticated user's account. Any request that retrieves earnings or ad performance metrics must
# use this scope.
SCOPES = ['https://www.googleapis.com/auth/yt-analytics-monetary.readonly']
API_SERVICE_NAME = 'youtubereporting'
API_VERSION = 'v1'

# Authorize the request and store authorization credentials.
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
```

--------------------------------

### GET /videoCategories.list

Source: https://developers.google.com/youtube/v3/docs/videoCategories/list?hl=vi

Retrieves a list of video categories that can be used in YouTube videos.

```APIDOC
## GET /videoCategories.list

### Description
Retrieves a list of video categories that can be used in YouTube videos.

### Method
GET

### Endpoint
/videoCategories.list

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more resource properties that the API response will include.
- **hl** (string) - Optional - The hl parameter specifies the language that should be used for text values in the API response.
- **id** (string) - Optional - The id parameter specifies a comma-separated list of the YouTube video category ID(s) for the resource(s) that are being retrieved.
- **regionCode** (string) - Optional - The regionCode parameter instructs the API to return the list of video categories available in the specified country.

### Response
#### Error Handling
- **notFound (404)**: The video category identified by the id parameter cannot be found.
```

--------------------------------

### Manage and Search YouTube Assets with Labels

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=id

Demonstrates creating assets, updating their labels, and performing searches based on label criteria. Note that asset indexing may cause a delay in search results.

```php
    array('onBehalfOfContentOwner' => $contentOwnerId));

    // Call the assets.insert() method to create another asset.
    // This code reuses the $asset and $metadata variables created earlier,
    // but updates the title in the metadata before creating the asset.
    // The code then extracts the unique asset ID from the API response.
    $metadata->setTitle("asset2");
    $assetInsertResponse2 = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId2 = $assetInsertResponse2['id'];

    // Modify the list of asset labels associated with the asset resource, then call
    // the assets.update() method to update the resource.
    $assetInsertResponse2['label'] = array("label2");
    $assetUpdateResponse2 = $youtubePartner->assets->update($assetId2, $assetInsertResponse2,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    // Retrieve asset labels that have been defined by the content owner. This list of labels
    // can be compared to the list retrieved earlier to see the effect of the API call.
    $assetLabelsListResponseAfter = $youtubePartner->assetLabels->listAssetLabels(
        array('onBehalfOfContentOwner' => $contentOwnerId));

    /*
     * AssetSearch may not be able to return the expected results right away, as there is a delay
     * in indexing the assets with labels for the asset search after they are added.
     * If you run this code sample a second time, you should see the assets created in
     * the previous run.
     */
    // Search for assets having both 'label1' and 'label2' labels.
    // The results should include "asset1" after indexing is succesfully finished.
    $assetSearchResponse1 = $youtubePartner->assetSearch->listAssetSearch(
        array('labels' => "label1, label2", 'onBehalfOfContentOwner' => $contentOwnerId));

    // Search for assets having at least one of 'label1' and 'label2' labels.
    // The results should include "asset1" and "asset2" after indexing is succesfully finished.
    $assetSearchResponse2 = $youtubePartner->assetSearch->listAssetSearch(
        array('labels' => "label1, label2", 'includeAnyProvidedlabel' => true,
            'onBehalfOfContentOwner' => $contentOwnerId));
```

```php
    $htmlBody .= "<h3>Content owner</h3><ul>";
    $htmlBody .= sprintf('<li>Content owner %s</li>',
        $contentOwnerId);
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Asset label created</h3><ul>";
    $htmlBody .= sprintf('<li>%s</li>',
        $assetLabelName);
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Asset Labels Before</h3><ul>";
    foreach ($assetLabelsListResponseBefore['items'] as $labelItem) {
      $htmlBody .= sprintf('<li>%s</li>', $labelItem['labelName']);
    }
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Asset created</h3><ul>";
    $htmlBody .= sprintf('<li>%s</li>', $assetId1);
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Added asset labels</h3><ul>";
    $htmlBody .= sprintf('<li>%s %s to %s</li>', $assetInsertResponse1['label'][0],
         $assetInsertResponse1['label'][1], $assetId1);
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Asset created</h3><ul>";
    $htmlBody .= sprintf('<li>%s</li>', $assetId2);
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Added asset labels</h3><ul>";
    $htmlBody .= sprintf('<li>%s to %s</li>', $assetInsertResponse2['label'][0], $assetId2);
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Asset Labels After</h3><ul>";
    foreach ($assetLabelsListResponseAfter['items'] as $labelItem) {
      $htmlBody .= sprintf('<li>%s</li>', $labelItem['labelName']);
    }
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Asset labeled with label1 and label2 </h3><ul>";
    foreach ($assetSearchResponse1['items'] as $assetItem) {
      $htmlBody .= sprintf('<li>%s</li>', $assetItem['id']);
    }
    $htmlBody .= '</ul>';

    $htmlBody .= "<h3>Asset labeled with label1 and/or label2 </h3><ul>";
    foreach ($assetSearchResponse2['items'] as $assetItem) {
      $htmlBody .= sprintf('<li>%s</li>', $assetItem['id']);
    }
    $htmlBody .= '</ul>';

    } catch (Google_Service_Exception $e) {
      $htmlBody .= sprintf('<p>A service error occurred: <code>%s</code></p>',
          htmlspecialchars($e->getMessage()));
    } catch (Google_Exception $e) {
      $htmlBody .= sprintf('<p>An client error occurred: <code>%s</code></p>',
          htmlspecialchars($e->getMessage()));
    }
```

```html
<!doctype html>
    <html>
    <head>
    <title>Assets Labels Example</title>
    </head>
    <body>
      <?=$htmlBody?>
    </body>
    </html>
```

--------------------------------

### GET /videoAbuseReportReasons

Source: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list

Retrieves a list of reasons that can be used to report abusive videos.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/videoAbuseReportReasons

### Description
Retrieve a list of reasons that can be used to report abusive videos.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/videoAbuseReportReasons

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies the videoAbuseReportReason resource parts that the API response will include. Supported values are id and snippet.
- **hl** (string) - Optional - The hl parameter specifies the language that should be used for text values in the API response. The default value is en_US.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type.
- **etag** (etag) - The Etag of this resource.
- **items[]** (list) - A list of videoAbuseReportReason resources.

#### Response Example
{
  "kind": "youtube#videoAbuseReportReasonListResponse",
  "etag": "etag",
  "items": [
    "videoAbuseReportReason resource"
  ]
}
```

--------------------------------

### Queueing Functions

Source: https://developers.google.com/youtube/iframe_api_reference

This section covers queueing functions that allow loading and playing videos, playlists, or lists of user uploads. It explains two syntaxes: argument syntax and object syntax.

```APIDOC
## Queueing Functions

Queueing functions allow you to load and play a video, a playlist, or another list of videos. The API supports two syntaxes for calling these functions: argument syntax and object syntax.

### Argument Syntax

Requires function arguments to be listed in a prescribed order.

### Object Syntax

Lets you pass an object as a single parameter, defining properties for the function arguments. This syntax may support additional functionality not available in the argument syntax.

### Example: `loadVideoById`

#### Argument Syntax Example
```javascript
loadVideoById("bHQqvYy5KYo", 5, "large")
```

#### Object Syntax Example
```javascript
loadVideoById({
  'videoId': 'bHQqvYy5KYo',
  'startSeconds': 5,
  'endSeconds': 60
});
```

**Note**: The object syntax supports the `endSeconds` property, which is not supported by the argument syntax.
```

--------------------------------

### GET /subscriptions

Source: https://developers.google.com/youtube/v3/docs/subscriptions/list?hl=es-419

Retrieves a list of subscriptions that match the API request parameters.

```APIDOC
## GET /subscriptions

### Description
Retrieves a list of YouTube subscriptions based on the provided filters and parameters.

### Method
GET

### Endpoint
/subscriptions

### Parameters
#### Query Parameters
- **part** (string) - Required - Comma-separated list of one or more subscription resource properties (contentDetails, id, snippet, subscriberSnippet).
- **channelId** (string) - Optional - YouTube channel ID to filter subscriptions.
- **id** (string) - Optional - Comma-separated list of YouTube subscription IDs.
- **mine** (boolean) - Optional - Set to true to retrieve the authenticated user's subscriptions.
- **myRecentSubscribers** (boolean) - Optional - Set to true to retrieve subscribers of the authenticated user in reverse chronological order.
- **mySubscribers** (boolean) - Optional - Set to true to retrieve subscribers of the authenticated user.
- **forChannelId** (string) - Optional - Comma-separated list of channel IDs to filter subscriptions.
- **maxResults** (unsigned integer) - Optional - Maximum number of items to return (0-50, default 5).
- **onBehalfOfContentOwner** (string) - Optional - YouTube CMS user acting on behalf of a content owner.
- **onBehalfOfContentOwnerChannel** (string) - Optional - YouTube channel ID for content partners.
- **order** (string) - Optional - Sorting method (alphabetical, relevance, unread).
- **pageToken** (string) - Optional - Token for pagination.
```

--------------------------------

### GET /playlists

Source: https://developers.google.com/youtube/v3/docs/playlists/list?hl=fa

Retrieves a list of playlists that match the API request parameters.

```APIDOC
## GET /playlists

### Description
Retrieves a list of YouTube playlists based on the provided filters and parameters.

### Method
GET

### Endpoint
/playlists

### Parameters
#### Query Parameters
- **part** (string) - Required - Comma-separated list of one or more playlist resource properties (contentDetails, id, localizations, player, snippet, status).
- **channelId** (string) - Optional - Returns only the specified channel's playlists.
- **id** (string) - Optional - Comma-separated list of YouTube playlist IDs.
- **mine** (boolean) - Optional - If true, returns playlists owned by the authenticated user.
- **hl** (string) - Optional - Language code for localized resource metadata.
- **maxResults** (unsigned integer) - Optional - Maximum number of items to return (0-50).
- **onBehalfOfContentOwner** (string) - Optional - CMS user acting on behalf of a content owner.
- **onBehalfOfContentOwnerChannel** (string) - Optional - YouTube channel ID for content partners.
- **pageToken** (string) - Optional - Identifies a specific page in the result set.

### Response
#### Success Response (200)
- **kind** (string) - The type of the API response.
- **etag** (string) - The ETag of the response.
- **nextPageToken** (string) - Token for the next page of results.
- **prevPageToken** (string) - Token for the previous page of results.
- **pageInfo** (object) - Information about the result set.
- **items** (array) - List of playlist resources.

#### Response Example
{
  "kind": "youtube#playlistListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "prevPageToken": "string",
  "pageInfo": {
    "totalResults": 0,
    "resultsPerPage": 5
  },
  "items": []
}
```

--------------------------------

### Loading a Video Player

Source: https://developers.google.com/youtube/iframe_api_reference

This snippet demonstrates how to initialize a YouTube player using the `YT.Player` constructor after the API's JavaScript code has loaded. It shows the `onYouTubeIframeAPIReady` function and the parameters for player construction.

```APIDOC
## Loading a Video Player

After the API's JavaScript code loads, the API will call the `onYouTubeIframeAPIReady` function, at which point you can construct a `YT.Player` object to insert a video player on your page.

### Constructor Parameters

1.  **DOM Element or ID**: The ID of the HTML element where the `<iframe>` tag will be inserted. This element will be replaced by the `<iframe>`.
2.  **Player Options Object**: An object containing properties to customize the player:
    *   `width` (number) - The width of the video player. Default is `640`.
    *   `height` (number) - The height of the video player. Default is `390`.
    *   `videoId` (string) - The YouTube video ID to load.
    *   `playerVars` (object) - Player parameters for customization.
    *   `events` (object) - Event listeners for player events (e.g., `onReady`, `onStateChange`).

### Request Example
```javascript
var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: 'M7lc1UVf-VE',
    playerVars: {
      'playsinline': 1
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}
```

### Alternative: Using an `<iframe>` Tag

Alternatively, you can create the `<iframe>` tag yourself. In this case, `width`, `height`, `videoId`, and player parameters are specified in the `<iframe>` tag's attributes and `src` URL. Include the `origin` parameter for security.

### Request Example
```html
<iframe id="player" type="text/html" width="640" height="390"
  src="http://www.youtube.com/embed/M7lc1UVf-VE?enablejsapi=1&origin=http://example.com"
  frameborder="0"></iframe>
```
```

--------------------------------

### GET /youtube/v3/playlists

Source: https://developers.google.com/youtube/v3/docs/playlists/list?hl=fr

Retrieves a list of playlists that match the API request parameters.

```APIDOC
## GET /youtube/v3/playlists

### Description
Returns a collection of playlists that match the API request parameters. This endpoint supports pagination and filtering by channel or ID.

### Method
GET

### Endpoint
/youtube/v3/playlists

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include.
- **channelId** (string) - Optional - Returns the playlists owned by the specified channel.
- **id** (string) - Optional - Returns the playlists with the specified IDs.
- **maxResults** (integer) - Optional - The maximum number of items that should be returned in the result set.
- **mine** (boolean) - Optional - Set to true to return playlists owned by the authenticated user.
- **pageToken** (string) - Optional - The token that identifies a specific page in the result set that should be returned.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type (youtube#playlistListResponse).
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - Token for the next page of results.
- **prevPageToken** (string) - Token for the previous page of results.
- **pageInfo** (object) - Encapsulates paging information.
- **items** (list) - A list of playlists that match the request criteria.

### Errors
- **400 (invalidValue)**: playlistOperationUnsupported - The API does not support the ability to list the specified playlist.
- **403 (forbidden)**: channelClosed, channelSuspended, playlistForbidden - Access denied due to channel status or authorization.
- **404 (notFound)**: channelNotFound, playlistNotFound - The specified channel or playlist could not be found.
```

--------------------------------

### Call YouTube API using Python Client Library

Source: https://developers.google.com/youtube/reporting/revision_history

Demonstrates how to call the YouTube API using the Python client library. Ensure the Python client library is installed and authenticated.

```python
from googleapiclient.discovery import build

api_key = "YOUR_API_KEY"
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part="snippet,statistics",
    id="UCBR8-60-B28hp2BmDPdntcQ" # Example Channel ID
)
try:
    response = request.execute()
    print(response)
except Exception as e:
    print(e)
```

--------------------------------

### GET /playlists

Source: https://developers.google.com/youtube/v3/docs/playlists/list?hl=fr

Retrieves a collection of playlists that match the API request parameters.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/playlists

### Description
Returns a collection of playlists that match the API request parameters. You can retrieve playlists owned by a specific channel or retrieve playlists by their unique IDs.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/playlists

### Parameters
#### Query Parameters
- **channelId** (string) - Optional - Retrieves playlists owned by the specified YouTube channel.
- **mine** (boolean) - Optional - If set to true, retrieves playlists created in the authorized user's YouTube channel.
- **onBehalfOfContentOwner** (string) - Optional - Used by content owners to retrieve playlists for a particular owned channel.
- **onBehalfOfContentOwnerChannel** (string) - Optional - Used by content owners to retrieve playlists for a particular owned channel.
```

--------------------------------

### Create a YouTube Playlist using .NET

Source: https://developers.google.com/youtube/v3/code_samples/dotnet?hl=fr

Use this snippet to create a new private playlist in a user's YouTube channel. It requires the Google APIs Client Library for .NET and a 'client_secrets.json' file for authentication. The playlist is initially set to public in this example.

```csharp
using System;
using System.IO;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;

using Google.Apis.Auth.OAuth2;
using Google.Apis.Services;
using Google.Apis.Upload;
using Google.Apis.Util.Store;
using Google.Apis.YouTube.v3;
using Google.Apis.YouTube.v3.Data;

namespace Google.Apis.YouTube.Samples
{
  /// <summary>
  /// YouTube Data API v3 sample: create a playlist.
  /// Relies on the Google APIs Client Library for .NET, v1.7.0 or higher.
  /// See https://developers.google.com/api-client-library/dotnet/get_started
  /// </summary>
  internal class PlaylistUpdates
  {
    [STAThread]
    static void Main(string[] args)
    {
      Console.WriteLine("YouTube Data API: Playlist Updates");
      Console.WriteLine("==================================");

      try
      {
        new PlaylistUpdates().Run().Wait();
      }
      catch (AggregateException ex)
      {
        foreach (var e in ex.InnerExceptions)
        {
          Console.WriteLine("Error: " + e.Message);
        }
      }

      Console.WriteLine("Press any key to continue...");
      Console.ReadKey();
    }

    private async Task Run()
    {
      UserCredential credential;
      using (var stream = new FileStream("client_secrets.json", FileMode.Open, FileAccess.Read))
      {
        credential = await GoogleWebAuthorizationBroker.AuthorizeAsync(
            GoogleClientSecrets.Load(stream).Secrets,
            // This OAuth 2.0 access scope allows for full read/write access to the
            // authenticated user's account.
            new[] { YouTubeService.Scope.Youtube },
            "user",
            CancellationToken.None,
            new FileDataStore(this.GetType().ToString())
        );
      }

      var youtubeService = new YouTubeService(new BaseClientService.Initializer()
      {
        HttpClientInitializer = credential,
        ApplicationName = this.GetType().ToString()
      });

      // Create a new, private playlist in the authorized user's channel.
      var newPlaylist = new Playlist();
      newPlaylist.Snippet = new PlaylistSnippet();
      newPlaylist.Snippet.Title = "Test Playlist";
      newPlaylist.Snippet.Description = "A playlist created with the YouTube API v3";
      newPlaylist.Status = new PlaylistStatus();
      newPlaylist.Status.PrivacyStatus = "public";
      newPlaylist = await youtubeService.Playlists.Insert(newPlaylist, "snippet,status").ExecuteAsync();

      // Add a video to the newly created playlist.
      var newPlaylistItem = new PlaylistItem();
      newPlaylistItem.Snippet = new PlaylistItemSnippet();
      newPlaylistItem.Snippet.PlaylistId = newPlaylist.Id;
      newPlaylistItem.Snippet.ResourceId = new ResourceId();
      newPlaylistItem.Snippet.ResourceId.Kind = "youtube#video";
      newPlaylistItem.Snippet.ResourceId.VideoId = "GNRMeaz6QRI";
      newPlaylistItem = await youtubeService.PlaylistItems.Insert(newPlaylistItem, "snippet").ExecuteAsync();

      Console.WriteLine("Playlist item id {0} was added to playlist id {1}.", newPlaylistItem.Id, newPlaylist.Id);
    }
  }
}

PlaylistUpdates.cs

```

--------------------------------

### GET /playlists

Source: https://developers.google.com/youtube/v3/docs/playlists/list?hl=es-419

Retrieves a list of playlists that match the API request parameters.

```APIDOC
## GET /playlists

### Description
Retrieves a list of YouTube playlists based on specified filters.

### Method
GET

### Endpoint
/playlists

### Parameters
#### Query Parameters
- **part** (string) - Required - Comma-separated list of one or more playlist resource properties (contentDetails, id, localizations, player, snippet, status).
- **channelId** (string) - Optional - Returns only the specified channel's playlists.
- **id** (string) - Optional - Comma-separated list of YouTube playlist IDs.
- **mine** (boolean) - Optional - If true, returns playlists owned by the authenticated user.
- **hl** (string) - Optional - Language code for localized resource metadata.
- **maxResults** (unsigned integer) - Optional - Maximum number of items to return (0-50).
- **onBehalfOfContentOwner** (string) - Optional - CMS user acting on behalf of a content owner.
- **onBehalfOfContentOwnerChannel** (string) - Optional - YouTube channel ID for content partners.
- **pageToken** (string) - Optional - Identifies a specific page in the result set.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource type (youtube#playlistListResponse).
- **etag** (etag) - ETag of the response.
- **nextPageToken** (string) - Token for the next page of results.
- **prevPageToken** (string) - Token for the previous page of results.
- **pageInfo** (object) - Information about the result set.
- **items** (array) - List of playlist resources.

#### Response Example
{
  "kind": "youtube#playlistListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "prevPageToken": "string",
  "pageInfo": {
    "totalResults": 0,
    "resultsPerPage": 0
  },
  "items": []
}
```

--------------------------------

### Manually Create iframe Tag for YouTube Player

Source: https://developers.google.com/youtube/iframe_api_reference?hl=de

This example demonstrates how to manually create the `<iframe>` tag for embedding a YouTube player. Ensure the closing `</iframe>` tag is present, as the `onYouTubeIframeAPIReady` function is only called if it exists.

```html
<iframe id="player" width="640" height="360" src="https://www.youtube.com/embed/M7lc1UVf-VE" frameborder="0" allowfullscreen></iframe>
```

--------------------------------

### GET /i18nRegions

Source: https://developers.google.com/youtube/v3/docs/i18nRegions/list?hl=ar

Retrieves a list of content regions that the YouTube website supports.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/i18nRegions

### Description
Returns a list of content regions that the YouTube website supports.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/i18nRegions

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies the i18nRegion resource properties that the API response will include. Set the parameter value to snippet.
- **hl** (string) - Optional - The hl parameter specifies the language that should be used for text values in the API response. The default value is en_US.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type. The value will be youtube#i18nRegionListResponse.
- **etag** (etag) - The Etag of this resource.
- **items** (list) - A list of regions where YouTube is available.

#### Response Example
{
  "kind": "youtube#i18nRegionListResponse",
  "etag": "etag",
  "items": [
    "i18nRegion resource"
  ]
}
```

--------------------------------

### GET /i18nRegions

Source: https://developers.google.com/youtube/v3/docs/guideCategories

Returns a list of content regions that the YouTube website supports.

```APIDOC
## GET /i18nRegions

### Description
Returns a list of content regions that the YouTube website supports.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/i18nRegions
```

--------------------------------

### Playlists Methods - `onBehalfOfContentOwner` Parameter

Source: https://developers.google.com/youtube/v3/revision_history?hl=fa

Details on the support for the `onBehalfOfContentOwner` parameter in playlist methods.

```APIDOC
## Playlists Methods - `onBehalfOfContentOwner` Parameter

### Description
This section details the addition of the `onBehalfOfContentOwner` parameter to several playlist-related methods.

### Methods

*   `playlists.insert`
*   `playlists.update`
*   `playlists.delete`

### Parameters

#### `onBehalfOfContentOwner` (string)

*   **Description**: Allows operations to be performed on behalf of a content owner. This parameter is already supported for several other methods.

### Note
This parameter enables content owners to manage playlists programmatically.
```

--------------------------------

### GET /search

Source: https://developers.google.com/youtube/v3/docs/guideCategories/list

Retrieves search results matching specified query parameters.

```APIDOC
## GET /search

### Description
Returns a collection of search results that match the query parameters specified in the API request.

### Method
GET

### Endpoint
/search
```

--------------------------------

### playlists.insert

Source: https://developers.google.com/youtube/v3/docs/errors?hl=ru

Error handling documentation for creating playlists.

```APIDOC
## POST playlists.insert

### Description
Creates a new playlist. Errors occur if validation fails or limits are exceeded.

### Method
POST

### Parameters
#### Request Body
- **snippet.title** (string) - Required - The title of the playlist.
- **localizations** (object) - Optional - Localization settings.

### Response
#### Error Handling
- **400 Bad Request**: defaultLanguageNotSetError, localizationValidationError, maxPlaylistExceeded, invalidPlaylistSnippet, playlistTitleRequired
- **403 Forbidden**: playlistForbidden
```

--------------------------------

### Initialize MainActivity for YouTube Data API

Source: https://developers.google.com/youtube/v3/quickstart/android

Defines the main activity class, sets up the UI components, and initializes Google account credentials for API access.

```java
package com.example.quickstart;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GoogleApiAvailability;
import com.google.api.client.extensions.android.http.AndroidHttp;
import com.google.api.client.googleapis.extensions.android.gms.auth.GoogleAccountCredential;
import com.google.api.client.googleapis.extensions.android.gms.auth.GooglePlayServicesAvailabilityIOException;
import com.google.api.client.googleapis.extensions.android.gms.auth.UserRecoverableAuthIOException;

import com.google.api.client.http.HttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.client.util.ExponentialBackOff;

import com.google.api.services.youtube.YouTubeScopes;

import com.google.api.services.youtube.model.*;

import android.Manifest;
import android.accounts.AccountManager;
import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.text.TextUtils;
import android.text.method.ScrollingMovementMethod;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import pub.devrel.easypermissions.AfterPermissionGranted;
import pub.devrel.easypermissions.EasyPermissions;

public class MainActivity extends Activity
    implements EasyPermissions.PermissionCallbacks {
    GoogleAccountCredential mCredential;
    private TextView mOutputText;
    private Button mCallApiButton;
    ProgressDialog mProgress;

    static final int REQUEST_ACCOUNT_PICKER = 1000;
    static final int REQUEST_AUTHORIZATION = 1001;
    static final int REQUEST_GOOGLE_PLAY_SERVICES = 1002;
    static final int REQUEST_PERMISSION_GET_ACCOUNTS = 1003;

    private static final String BUTTON_TEXT = "Call YouTube Data API";
    private static final String PREF_ACCOUNT_NAME = "accountName";
    private static final String[] SCOPES = { YouTubeScopes.YOUTUBE_READONLY };

    /**
     * Create the main activity.
     * @param savedInstanceState previously saved instance data.
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        LinearLayout activityLayout = new LinearLayout(this);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.MATCH_PARENT);
        activityLayout.setLayoutParams(lp);
        activityLayout.setOrientation(LinearLayout.VERTICAL);
        activityLayout.setPadding(16, 16, 16, 16);

        ViewGroup.LayoutParams tlp = new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT);

        mCallApiButton = new Button(this);
        mCallApiButton.setText(BUTTON_TEXT);
        mCallApiButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mCallApiButton.setEnabled(false);
                mOutputText.setText("");
                getResultsFromApi();
                mCallApiButton.setEnabled(true);
            }
        });
        activityLayout.addView(mCallApiButton);

        mOutputText = new TextView(this);
        mOutputText.setLayoutParams(tlp);
        mOutputText.setPadding(16, 16, 16, 16);
        mOutputText.setVerticalScrollBarEnabled(true);
        mOutputText.setMovementMethod(new ScrollingMovementMethod());
        mOutputText.setText(
                "Click the '" + BUTTON_TEXT +"' button to test the API.");
        activityLayout.addView(mOutputText);

        mProgress = new ProgressDialog(this);
        mProgress.setMessage("Calling YouTube Data API ...");

        setContentView(activityLayout);

        // Initialize credentials and service object.
        mCredential = GoogleAccountCredential.usingOAuth2(
                getApplicationContext(), Arrays.asList(SCOPES))
                .setBackOff(new ExponentialBackOff());
    }
```

--------------------------------

### GET /membershipsLevels

Source: https://developers.google.com/youtube/v3/docs/guideCategories/list

Retrieves a collection of membershipsLevel resources owned by the authorized channel.

```APIDOC
## GET /membershipsLevels

### Description
Returns a collection of zero or more membershipsLevel resources owned by the channel that authorized the API request.

### Method
GET

### Endpoint
/membershipsLevels
```

--------------------------------

### GET /comments

Source: https://developers.google.com/youtube/v3/docs/comments/markAsSpam

Returns a list of comments that match the API request parameters.

```APIDOC
## GET /comments

### Description
Returns a list of comments that match the API request parameters.

### Method
GET

### Endpoint
/comments
```

--------------------------------

### GET /youtube/v3/comments

Source: https://developers.google.com/youtube/v3/docs/comments/list?hl=fa

Retrieves a list of comments that match the API request parameters.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/comments

### Description
Returns a list of comments that match the API request parameters.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/comments

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more comment resource properties that the API response will include (id, snippet).
- **id** (string) - Optional - Specifies a comma-separated list of comment IDs for the resources that are being retrieved.
- **parentId** (string) - Optional - Specifies the ID of the comment for which replies should be retrieved.
- **maxResults** (unsigned integer) - Optional - Specifies the maximum number of items that should be returned (1-100, default 20).
- **pageToken** (string) - Optional - Identifies a specific page in the result set that should be returned.
- **textFormat** (string) - Optional - Indicates whether the API should return comments formatted as HTML or as plain text (html, plainText).

### Response
#### Success Response (200)
- **kind** (string) - The type of the API response (youtube#commentListResponse).
- **etag** (etag) - The ETag of the response.
- **nextPageToken** (string) - Identifies the next page of the result that can be retrieved.
- **pageInfo** (object) - Information about the result set.
- **items** (array) - A list of comment resources.

#### Response Example
{
  "kind": "youtube#commentListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "pageInfo": {
    "totalResults": 0,
    "resultsPerPage": 0
  },
  "items": []
}
```

--------------------------------

### Initialize Google Web User Authorizer

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps

Initializes the Google::Auth::WebUserAuthorizer with client ID, scope, token store, and callback URI. Ensure client_secret.json contains the necessary credentials.

```ruby
set :authorizer, Google::Auth::WebUserAuthorizer.new(settings.client_id, settings.scope,
                          settings.token_store, callback_uri: settings.callback_uri)
```

--------------------------------

### GET /commentThreads

Source: https://developers.google.com/youtube/v3/docs/commentThreads/list?hl=bn

Retrieves a list of comment threads based on specified filters.

```APIDOC
## GET /commentThreads

### Description
Returns a list of comment threads that match the API request parameters.

### Method
GET

### Endpoint
/commentThreads

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include (id, replies, snippet).
- **allThreadsRelatedToChannelId** (string) - Optional - Instructs the API to return all comment threads associated with the specified channel.
- **id** (string) - Optional - Specifies a comma-separated list of comment thread IDs for the resources that should be retrieved.
- **videoId** (string) - Optional - Instructs the API to return comment threads associated with the specified video ID.
- **maxResults** (unsigned integer) - Optional - Specifies the maximum number of items that should be returned (1-100, default 20).
- **moderationStatus** (string) - Optional - Limits the returned comment threads to a particular moderation state (heldForReview, likelySpam, published).
- **order** (string) - Optional - Specifies the order in which the API response should list comment threads (time, relevance).
- **pageToken** (string) - Optional - Identifies a specific page in the result set that should be returned.
- **searchTerms** (string) - Optional - Limits the API response to only contain comments that contain the specified search terms.
- **textFormat** (string) - Optional - Instructs the API to return the comments in html or plainText format.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type.
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - The token that can be used to retrieve the next page in the result set.
- **pageInfo** (object) - Encapsulates paging information for the result set.
- **items** (list) - A list of comment threads that match the request criteria.

#### Response Example
{
  "kind": "youtube#commentThreadListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "pageInfo": {
    "totalResults": 0,
    "resultsPerPage": 0
  },
  "items": []
}
```

--------------------------------

### Authenticate with OAuth 2.0

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=pl

Initializes the Google Client and handles token storage and refreshing.

```php
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope(
      'https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);

    //fclose($fp);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}
```

--------------------------------

### Update Channel Branding Settings

Source: https://developers.google.com/youtube/v3/docs/channels/update?hl=es

This example updates the description and default language for the authorizing channel. It requires the `brandingSettings` part.

```json
{
  "id": "CHANNEL_ID",
  "snippet": {
    "title": "My channel",
    "defaultLanguage": "en"
  }
}
```

--------------------------------

### GET /channels

Source: https://developers.google.com/youtube/v3/docs/channels?hl=th

Retrieves a list of YouTube channels based on specified criteria.

```APIDOC
## GET /channels

### Description
Retrieves channel information including snippet, statistics, status, and branding settings.

### Method
GET

### Endpoint
/channels

### Response
#### Success Response (200)
- **snippet** (object) - Channel details
- **statistics** (object) - Channel metrics
- **status** (object) - Privacy information and 'made for kids' status
```

--------------------------------

### GET /channels

Source: https://developers.google.com/youtube/v3/docs/channels/list

Retrieves a collection of channel resources that match the request criteria.

```APIDOC
## GET /channels

### Description
Retrieves a collection of channel resources that match the request criteria. This endpoint allows fetching channel details using various identifiers and filters.

### Method
GET

### Endpoint
/channels

### Parameters
#### Query Parameters
- **part** (string) - Required - A comma-separated list of one or more channel resource properties to include in the response. Possible values include: `auditDetails`, `brandingSettings`, `contentDetails`, `contentOwnerDetails`, `id`, `localizations`, `snippet`, `statistics`, `status`, `topicDetails`.
- **categoryId** (string) - Deprecated. Specifies a YouTube guide category.
- **forHandle** (string) - Required - Specifies a YouTube handle (e.g., `GoogleDevelopers` or `@GoogleDevelopers`) to retrieve the associated channel.
- **forUsername** (string) - Required - Specifies a YouTube username to retrieve the associated channel.
- **id** (string) - Required - A comma-separated list of YouTube channel IDs for the resources to retrieve.
- **managedByMe** (boolean) - Optional - Requires authorization. Returns channels managed by the content owner specified in `onBehalfOfContentOwner`. Set to `true`.
- **mine** (boolean) - Optional - Requires authorization. Returns channels owned by the authenticated user. Set to `true`.
- **hl** (string) - Optional - Instructs the API to retrieve localized resource metadata for a specific application language. The value must be a language code supported by the YouTube website.
- **maxResults** (unsigned integer) - Optional - The maximum number of items to return in the result set. Acceptable values are 0 to 50. Defaults to 5.
- **onBehalfOfContentOwner** (string) - Optional - Requires authorization. Indicates that the request's authorization credentials identify a YouTube CMS user acting on behalf of the content owner specified in the parameter value.
- **pageToken** (string) - Optional - Identifies a specific page in the result set to return.

### Request Body
Do not provide a request body when calling this method.

### Response
#### Success Response (200)
- **kind** (string) - The type of resource.
- **etag** (string) - The ETag of the response.
- **nextPageToken** (string) - Token to retrieve the next page of results.
- **prevPageToken** (string) - Token to retrieve the previous page of results.
- **pageInfo** (object) - Information about the pagination of the results.
  - **totalResults** (integer) - The total number of results.
  - **resultsPerPage** (integer) - The number of results per page.
- **items** (array) - An array of channel resources.

#### Response Example
```json
{
  "kind": "youtube#channelListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "prevPageToken": "string",
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    channel Resource
  ]
}
```
```

--------------------------------

### Configure OAuth2 Client and Express Server

Source: https://developers.google.com/youtube/partner/guides/auth/server-side-web-apps?hl=ja

Initializes the OAuth2 client with credentials and sets up an Express server with session management.

```javascript
const http = require('http');
const https = require('https');
const url = require('url');
const { google } = require('googleapis');
const crypto = require('crypto');
const express = require('express');
const session = require('express-session');

/**
 * To use OAuth2 authentication, we need access to a CLIENT_ID, CLIENT_SECRET, AND REDIRECT_URI.
 * To get these credentials for your application, visit
 * https://console.cloud.google.com/apis/credentials.
 */
const oauth2Client = new google.auth.OAuth2(
  YOUR_CLIENT_ID,
  YOUR_CLIENT_SECRET,
  YOUR_REDIRECT_URL
);

// Access scopes for two non-Sign-In scopes: Read-only Drive activity and Google Calendar.
const scopes = [
  'https://www.googleapis.com/auth/youtubepartner',
  'https://www.googleapis.com/auth/calendar.readonly'
];

/* Global variable that stores user credential in this code example.
 * ACTION ITEM for developers:
 *   Store user's refresh token in your data store if
 *   incorporating this code into your real app.
 *   For more information on handling refresh tokens,
 *   see https://github.com/googleapis/google-api-nodejs-client#handling-refresh-tokens
 */
let userCredential = null;

async function main() {
  const app = express();

  app.use(session({
    secret: 'your_secure_secret_key', // Replace with a strong secret
    resave: false,
    saveUninitialized: false,
  }));
```

--------------------------------

### GET /captions

Source: https://developers.google.com/youtube/v3/docs/captions/list?hl=es-419

Returns a list of caption tracks that are associated with a specified video.

```APIDOC
## GET https://www.googleapis.com/youtube/v3/captions

### Description
Returns a list of caption tracks that are associated with a specified video. Note that the API response does not contain the actual captions; use the captions.download method to retrieve a caption track.

### Method
GET

### Endpoint
https://www.googleapis.com/youtube/v3/captions

### Parameters
#### Query Parameters
- **part** (string) - Required - The part parameter specifies the caption resource parts that the API response will include (e.g., id, snippet).
- **videoId** (string) - Required - The video ID of the video for which the API should return caption tracks.
- **id** (string) - Optional - A comma-separated list of IDs that identify the caption resources that should be retrieved.
- **onBehalfOfContentOwner** (string) - Optional - Indicates that the request's authorization credentials identify a YouTube CMS user acting on behalf of the content owner.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type (youtube#captionListResponse).
- **etag** (etag) - The Etag of this resource.
- **items** (list) - A list of captions that match the request criteria.

#### Response Example
{
  "kind": "youtube#captionListResponse",
  "etag": "etag",
  "items": [
    "caption Resource"
  ]
}
```

--------------------------------

### Prepare Video Upload Request

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=es

Sets up the video snippet with title, description, tags, and category ID, and defines the video's privacy status. This prepares the video resource for insertion.

```php
$videoPath = "/path/to/file.mp4";
$channelId = "CHANNEL_ID";

$snippet = new Google_Service_YouTube_VideoSnippet();
$snippet->setTitle("Test title");
$snippet->setDescription("Test description");
$snippet->setTags(array("tag1", "tag2"));

$snippet->setCategoryId("22");

$status = new Google_Service_YouTube_VideoStatus();
$status->privacyStatus = "public";

$video = new Google_Service_YouTube_Video();
$video->setSnippet($snippet);
$video->setStatus($status);
```

--------------------------------

### Upload Video using .NET Client Library

Source: https://developers.google.com/youtube/v3/docs/videos/insert?hl=ar

This .NET code sample calls the API's `videos.insert` method to upload a video. It requires the Google APIs Client Library for .NET and a `client_secrets.json` file for authentication. Replace `REPLACE_ME.mp4` with the actual video file path.

```C#
using System;
using System.IO;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;

using Google.Apis.Auth.OAuth2;
using Google.Apis.Services;
using Google.Apis.Upload;
using Google.Apis.Util.Store;
using Google.Apis.YouTube.v3;
using Google.Apis.YouTube.v3.Data;

namespace Google.Apis.YouTube.Samples
{
  /// <summary>
  /// YouTube Data API v3 sample: upload a video.
  /// Relies on the Google APIs Client Library for .NET, v1.7.0 or higher.
  /// See https://developers.google.com/api-client-library/dotnet/get_started
  /// </summary>
  internal class UploadVideo
  {
    [STAThread]
    static void Main(string[] args)
    {
      Console.WriteLine("YouTube Data API: Upload Video");
      Console.WriteLine("==============================");

      try
      {
        new UploadVideo().Run().Wait();
      }
      catch (AggregateException ex)
      {
        foreach (var e in ex.InnerExceptions)
        {
          Console.WriteLine("Error: " + e.Message);
        }
      }

      Console.WriteLine("Press any key to continue...");
      Console.ReadKey();
    }

    private async Task Run()
    {
      UserCredential credential;
      using (var stream = new FileStream("client_secrets.json", FileMode.Open, FileAccess.Read))
      {
        credential = await GoogleWebAuthorizationBroker.AuthorizeAsync(
            GoogleClientSecrets.Load(stream).Secrets,
            // This OAuth 2.0 access scope allows an application to upload files to the
            // authenticated user's YouTube channel, but doesn't allow other types of access.
            new[] { YouTubeService.Scope.YoutubeUpload },
            "user",
            CancellationToken.None
        );
      }

      var youtubeService = new YouTubeService(new BaseClientService.Initializer()
      {
        HttpClientInitializer = credential,
        ApplicationName = Assembly.GetExecutingAssembly().GetName().Name
      });

      var video = new Video();
      video.Snippet = new VideoSnippet();
      video.Snippet.Title = "Default Video Title";
      video.Snippet.Description = "Default Video Description";
      video.Snippet.Tags = new string[] { "tag1", "tag2" };
      video.Snippet.CategoryId = "22"; // See https://developers.google.com/youtube/v3/docs/videoCategories/list
      video.Status = new VideoStatus();
      video.Status.PrivacyStatus = "unlisted"; // or "private" or "public"
      var filePath = @"REPLACE_ME.mp4"; // Replace with path to actual movie file.

      using (var fileStream = new FileStream(filePath, FileMode.Open))
      {
        var videosInsertRequest = youtubeService.Videos.Insert(video, "snippet,status", fileStream, "video/*");
        videosInsertRequest.ProgressChanged += videosInsertRequest_ProgressChanged;
        videosInsertRequest.ResponseReceived += videosInsertRequest_ResponseReceived;

        await videosInsertRequest.UploadAsync();

```

--------------------------------

### GET /captions/{id}

Source: https://developers.google.com/youtube/v3/docs/captions/download

Downloads a caption track associated with a specific ID.

```APIDOC
## GET /captions/{id}

### Description
Downloads a caption track. The response is a binary file with a Content-Type of application/octet-stream.

### Method
GET

### Endpoint
/captions/{id}

### Parameters
#### Path Parameters
- **id** (string) - Required - The ID of the caption track to download.

### Response
#### Success Response (200)
- **binary file** (application/octet-stream) - The caption track data.

### Errors
- **403 Forbidden**: The permissions associated with the request are not sufficient.
- **400 InvalidValue**: The caption track data could not be converted to the requested language or format.
- **404 NotFound**: The caption track could not be found.
```

--------------------------------

### Create and Configure Asset Ownership

Source: https://developers.google.com/youtube/partner/code_samples/php?hl=pl

Creates a new asset, sets its metadata, and defines ownership rights for the content owner.

```php
// Create an asset resource and set its metadata and type. Assets support
    // many metadata fields, but this sample only sets a title and description.
    $asset = new Google_Service_YouTubePartner_Asset();
    $metadata = new Google_Service_YouTubePartner_Metadata();
    $metadata->setTitle("Test asset title");
    $metadata->setDescription("Test asset description");
    $asset->setMetadata($metadata);
    $asset->setType("web");

    // Insert the asset resource. Extract its unique asset ID from the API
    // response.
    $assetInsertResponse = $youtubePartner->assets->insert($asset,
        array('onBehalfOfContentOwner' => $contentOwnerId));
    $assetId = $assetInsertResponse['id'];

    // Create a territory owner with owner, ratio, type and territories
    // Set the asset's ownership data. This example identifies the content
    // owner associated with the authenticated user's account as the asset's
    // owner. It indicates that the content owner owns 100% of the asset
    // worldwide.
    $owners = new Google_Service_YouTubePartner_TerritoryOwners();
    $owners->setOwner($contentOwnerId);
    $owners->setRatio(100);
    $owners->setType("exclude");
    $owners->setTerritories(array());

    // Create ownership with a territory owner
    $ownership = new Google_Service_YouTubePartner_RightsOwnership();
    $ownership->setGeneral(array($owners));

    // Update the asset's ownership with the rights data defined above.
    $ownershipUpdateResponse = $youtubePartner->ownership->update($assetId, $ownership,
        array('onBehalfOfContentOwner' => $contentOwnerId));

    // Define a monetization policy for the asset.
```

--------------------------------

### GET /activities

Source: https://developers.google.com/youtube/v3/docs/activities/list?hl=ru

Retrieves a list of channel activities based on specified filters.

```APIDOC
## GET /activities

### Description
Returns a list of channel activities that match the request criteria.

### Method
GET

### Endpoint
/activities

### Parameters
#### Query Parameters
- **part** (string) - Required - Specifies a comma-separated list of one or more activity resource properties that the API response will include (contentDetails, id, snippet).
- **channelId** (string) - Optional - Specifies a unique YouTube channel ID to return activities for.
- **home** (boolean) - Optional - Deprecated. Returns items similar to those a logged-out user would see on the YouTube home page.
- **mine** (boolean) - Optional - If true, retrieves a feed of the authenticated user's activities.
- **maxResults** (unsigned integer) - Optional - The maximum number of items to return (0-50, default 5).
- **pageToken** (string) - Optional - Identifies a specific page in the result set.
- **publishedAfter** (datetime) - Optional - Earliest date and time for an activity to be included (ISO 8601).
- **publishedBefore** (datetime) - Optional - Date and time before which an activity must have occurred (ISO 8601).
- **regionCode** (string) - Optional - ISO 3166-1 alpha-2 country code to return results for.

### Response
#### Success Response (200)
- **kind** (string) - Identifies the API resource's type.
- **etag** (etag) - The Etag of this resource.
- **nextPageToken** (string) - Token to retrieve the next page.
- **prevPageToken** (string) - Token to retrieve the previous page.
- **pageInfo** (object) - Encapsulates paging information.
- **items[]** (list) - A list of activities that match the request criteria.

#### Response Example
{
  "kind": "youtube#activityListResponse",
  "etag": "etag",
  "nextPageToken": "string",
  "prevPageToken": "string",
  "pageInfo": {
    "totalResults": 0,
    "resultsPerPage": 0
  },
  "items": []
}
```

--------------------------------

### GET /reports (Annotations)

Source: https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports

Provides performance statistics for individual annotations on videos.

```APIDOC
## GET /reports

### Description
This report provides statistics for annotations that display during videos on a content owner's channels. The report ID is `content_owner_annotations_a1`.

### Method
GET

### Parameters
#### Query Parameters
- **ids** (string) - Required - The report ID: `content_owner_annotations_a1`

### Dimensions
date, channel_id, video_id, claimed_status, uploader_type, live_or_on_demand, subscribed_status, country_code, annotation_type, annotation_id

### Metrics
annotation_click_through_rate, annotation_close_rate, annotation_impressions, annotation_clickable_impressions, annotation_closable_impressions, annotation_clicks, annotation_closes
```

--------------------------------

### Define OAuth 2.0 and API Constants

Source: https://developers.google.com/youtube/partner/code_samples/python?hl=ko

Sets up file paths for credentials and defines API service names, versions, and OAuth scopes.

```python
INVALID_CREDENTIALS = "Invalid Credentials"

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google API Console at
# https://console.cloud.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secrets.json"

# The local file used to store the cached OAuth 2 credentials after going
# through a one-time browser-based login.
CACHED_CREDENTIALS_FILE = "%s-oauth2.json" % sys.argv[0]

YOUTUBE_SCOPES = (
  # This OAuth 2.0 access scope allows for full read/write access to the
  # authenticated user's account.
  "https://www.googleapis.com/auth/youtube",
  # This OAuth 2.0 scope grants access to YouTube Content ID API functionality.
  "https://www.googleapis.com/auth/youtubepartner",)
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_CONTENT_ID_API_SERVICE_NAME = "youtubePartner"
YOUTUBE_CONTENT_ID_API_VERSION = "v1"
```

--------------------------------

### Authentication and Client Initialization

Source: https://developers.google.com/youtube/reporting/v1/reference/rest/v1/jobs/list?hl=zh-tw

This section details the process of obtaining and initializing a Google_Client object for accessing Google APIs, specifically focusing on YouTube Data API and OAuth 2.0 authentication.

```APIDOC
## Authentication

### Description
Obtain an OAuth 2.0 client ID and client secret from the Google Cloud Console. Ensure the YouTube Data API is enabled for your project. This process is crucial for authenticating requests to Google APIs.

### Resources
- Google Cloud Console: https://cloud.google.com/console
- OAuth 2.0 for Google APIs: https://developers.google.com/youtube/v3/guides/authentication

### PHP Example (getClient function)
```php
function getClient() {
  $client = new Google_Client();
  $client->setAuthConfigFile('client_secrets_php.json');
  $client->addScope('https://www.googleapis.com/auth/yt-analytics-monetary.readonly');
  $client->setRedirectUri('urn:ietf:wg:oauth:2.0:oob');
  $client->setAccessType('offline');

  // Load previously authorized credentials from a file.
  $credentialsPath = expandHomeDirectory(CREDENTIALS_PATH);
  if (file_exists($credentialsPath)) {
    $accessToken = json_decode(file_get_contents($credentialsPath), true);
  } else {
    // Request authorization from the user.
    $authUrl = $client->createAuthUrl();
    printf('Open the following link in your browser:\n%s\n', $authUrl);
    print 'Enter verification code: ';
    $authCode = trim(fgets(STDIN));

    // Exchange authorization code for an access token.
    $accessToken = $client->authenticate($authCode);
    $refreshToken = $client->getRefreshToken();

    // Store the credentials to disk.
    if(!file_exists(dirname($credentialsPath))) {
      mkdir(dirname($credentialsPath), 0700, true);
    }
    file_put_contents($credentialsPath, json_encode($accessToken));
    printf('Credentials saved to %s\n', $credentialsPath);
  }
  $client->setAccessToken($accessToken);

  // Refresh the token if it's expired.
  if ($client->isAccessTokenExpired()) {
    $client->fetchAccessTokenWithRefreshToken($client->getRefreshToken());
    file_put_contents($credentialsPath, json_encode($client->getAccessToken()));
  }

  return $client;
}

/**
 * Expands the home directory alias '~' to the full path.
 * @param string $path the path to expand.
 * @return string the expanded path.
 */
function expandHomeDirectory($path) {
  $homeDirectory = getenv('HOME');
  if (empty($homeDirectory)) {
    $homeDirectory = getenv('HOMEDRIVE') . getenv('HOMEPATH');
  }
  return str_replace('~', realpath($homeDirectory), $path);
}
```
```

--------------------------------

### GET /v1/jobs

Source: https://developers.google.com/youtube/reporting/v1/reference/rest

Lists all reporting jobs that have been scheduled for a channel or content owner.

```APIDOC
## GET /v1/jobs

### Description
Lists reporting jobs that have been scheduled for a channel or content owner. Each resource in the response contains an id property, which specifies the ID that YouTube uses to uniquely identify the job.

### Method
GET

### Endpoint
/v1/jobs
```

--------------------------------

### GET /videoAdvertisingOptions/{videoId}

Source: https://developers.google.com/youtube/partner/reference/rest/v1/videoAdvertisingOptions/get

Retrieves the advertising settings for a specified YouTube video.

```APIDOC
## GET /videoAdvertisingOptions/{videoId}

### Description
Retrieves advertising settings for the specified video.

### Method
GET

### Endpoint
https://youtubepartner.googleapis.com/youtube/partner/v1/videoAdvertisingOptions/{videoId}

### Parameters
#### Path Parameters
- **videoId** (string) - Required - The YouTube video ID of the video for which you are retrieving advertising settings.

#### Query Parameters
- **onBehalfOfContentOwner** (string) - Optional - Identifies the content owner that the user is acting on behalf of. This parameter supports users whose accounts are associated with multiple content owners.

### Request Body
The request body must be empty.

### Response
#### Success Response (200)
- **VideoAdvertisingOption** (object) - The response body contains an instance of VideoAdvertisingOption.

### Authorization
Requires the following OAuth scope: https://www.googleapis.com/auth/youtubepartner
```

--------------------------------

### Implement onYouTubeIframeAPIReady

Source: https://developers.google.com/youtube/iframe_api_reference?hl=fa

This function must be implemented to initialize player objects once the API has finished loading.

```javascript
onYouTubeIframeAPIReady
```

--------------------------------

### Example Media Playlist in Live Stream

Source: https://developers.google.com/youtube/v3/live/guides/hls-ingestion

Shows a Media Playlist file from the middle of a live stream, featuring a non-zero EXT-X-MEDIA-SEQUENCE.

```m3u8
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:4
#EXT-X-MEDIA-SEQUENCE:2680

#EXTINF:3.975,
fileSequence2680.ts
#EXTINF:3.941,
fileSequence2681.ts
#EXTINF:3.975,
fileSequence2682.ts
```

--------------------------------

### GET /youtube/partner/v1/uploader

Source: https://developers.google.com/youtube/partner/reference/rest/v1/uploader/list

Retrieves a list of uploaders associated with a specified content owner.

```APIDOC
## GET https://youtubepartner.googleapis.com/youtube/partner/v1/uploader

### Description
Retrieves a list of uploaders for a content owner. This endpoint requires the `https://www.googleapis.com/auth/youtubepartner` OAuth scope.

### Method
GET

### Endpoint
https://youtubepartner.googleapis.com/youtube/partner/v1/uploader

### Parameters
#### Query Parameters
- **onBehalfOfContentOwner** (string) - Required - Identifies the content owner that the user is acting on behalf of.

### Request Body
The request body must be empty.

### Response
#### Success Response (200)
- **kind** (string) - The type of the API response (value is `youtubePartner#uploaderList`).
- **items** (array) - A list of uploader (`youtubePartner#uploader`) resources.

#### Response Example
{
  "kind": "youtubePartner#uploaderList",
  "items": [
    {
      "id": "uploader_id_example"
    }
  ]
}
```

--------------------------------

### List and Create Reporting Jobs in Java

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=pt-br

Methods to list available report types, create new reporting jobs, and prompt user input for job configuration.

```java
    .execute();
        List<ReportType> reportTypeList = reportTypesListResponse.getReportTypes();

        if (reportTypeList == null || reportTypeList.isEmpty()) {
          System.out.println("No report types found.");
          return false;
        } else {
            // Print information from the API response.
            System.out.println("\n================== Report Types ==================\n");
            for (ReportType reportType : reportTypeList) {
                System.out.println("  - Id: " + reportType.getId());
                System.out.println("  - Name: " + reportType.getName());
                System.out.println("\n-------------------------------------------------------------\n");
           }
        }
        return true;
    }

    /**
     * Creates a reporting job. (jobs.create)
     *
     * @param reportTypeId Id of the job's report type.
     * @param name name of the job.
     * @throws IOException
     */
    private static void createReportingJob(String reportTypeId, String name)
        throws IOException {
        // Create a reporting job with a name and a report type id.
        Job job = new Job();
        job.setReportTypeId(reportTypeId);
        job.setName(name);

        // Call the YouTube Reporting API's jobs.create method to create a job.
        Job createdJob = youtubeReporting.jobs().create(job).execute();

        // Print information from the API response.
        System.out.println("\n================== Created reporting job ==================\n");
        System.out.println("  - ID: " + createdJob.getId());
        System.out.println("  - Name: " + createdJob.getName());
        System.out.println("  - Report Type Id: " + createdJob.getReportTypeId());
        System.out.println("  - Create Time: " + createdJob.getCreateTime());
        System.out.println("\n-------------------------------------------------------------\n");
    }

    /*
     * Prompt the user to enter a name for the job. Then return the name.
     */
    private static String getNameFromUser() throws IOException {

        String name = "";

        System.out.print("Please enter the name for the job [javaTestJob]: ");
        BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));
        name = bReader.readLine();

        if (name.length() < 1) {
            // If nothing is entered, defaults to "javaTestJob".
          name = "javaTestJob";
        }

        System.out.println("You chose " + name + " as the name for the job.");
        return name;
    }

    /*
     * Prompt the user to enter a report type id for the job. Then return the id.
     */
    private static String getReportTypeIdFromUser() throws IOException {

        String id = "";

        System.out.print("Please enter the reportTypeId for the job: ");
        BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));
        id = bReader.readLine();

        System.out.println("You chose " + id + " as the report type Id for the job.");
        return id;
    }
}
```

--------------------------------

### GET /policies

Source: https://developers.google.com/youtube/partner/reference/rest/v1/policies/list?hl=tr

Retrieves a list of saved policies for the authenticated content owner.

```APIDOC
## GET https://youtubepartner.googleapis.com/youtube/partner/v1/policies

### Description
Retrieves a list of the content owner's saved policies.

### Method
GET

### Endpoint
https://youtubepartner.googleapis.com/youtube/partner/v1/policies

### Parameters
#### Query Parameters
- **id** (string) - Optional - A comma-separated list of policy IDs to retrieve.
- **onBehalfOfContentOwner** (string) - Optional - Identifies the content owner for whom the user is acting.
- **sort** (enum) - Optional - Specifies the order of the results (e.g., TIME_UPDATED_ASC, TIME_UPDATED_DESC).

### Request Body
The request body must be empty.

### Response
#### Success Response (200)
- **kind** (string) - The type of API response (youtubePartner#policyList).
- **items** (array) - A list of Policy objects.

#### Response Example
{
  "kind": "youtubePartner#policyList",
  "items": [
    {
      "policy": "object"
    }
  ]
}
```

--------------------------------

### Authorize and Execute YouTube Reporting API Workflow

Source: https://developers.google.com/youtube/reporting/v1/reports?hl=zh-tw

Initializes the YouTube Reporting service and executes the sequence of listing jobs, retrieving reports, and downloading a file.

```java
List<String> scopes = Lists.newArrayList("https://www.googleapis.com/auth/yt-analytics-monetary.readonly");

        try {
            // Authorize the request.
            Credential credential = Auth.authorize(scopes, "retrievereports");

            // This object is used to make YouTube Reporting API requests.
            youtubeReporting = new YouTubeReporting.Builder(Auth.HTTP_TRANSPORT, Auth.JSON_FACTORY, credential)
                    .setApplicationName("youtube-cmdline-retrievereports-sample").build();

            if (listReportingJobs()) {
              if(retrieveReports(getJobIdFromUser())) {
                downloadReport(getReportUrlFromUser());
              }
            }
        } catch (GoogleJsonResponseException e) {
            System.err.println("GoogleJsonResponseException code: " + e.getDetails().getCode()
                    + " : " + e.getDetails().getMessage());
            e.printStackTrace();

        } catch (IOException e) {
            System.err.println("IOException: " + e.getMessage());
            e.printStackTrace();
        } catch (Throwable t) {
            System.err.println("Throwable: " + t.getMessage());
            t.printStackTrace();
        }
    }
```