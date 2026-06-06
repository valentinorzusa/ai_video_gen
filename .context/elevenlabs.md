### System Prompt Example for Tool Usage Guidance

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/client-tools

This example illustrates how to provide explicit instructions in the system prompt to guide the agent on when to use a specific tool, improving tool calling accuracy.

```plaintext
Use `check_order_status` when the user inquires about the status of their order, such as 'Where is my order?' or 'Has my order shipped yet?'.
```

--------------------------------

### Start development server

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/next-js

Run the development server to test the Next.js setup and access the application in your browser.

```shell
npm run dev
```

--------------------------------

### Start Conversation with Dynamic Variables (JavaScript)

Source: https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables

This JavaScript example demonstrates how to start a conversational AI session, including requesting microphone access and passing dynamic variables to the `startSession` method.

```javascript
import { Conversation } from '@elevenlabs/client';

class VoiceAgent {
  ...

  async startConversation() {
    try {
        // Request microphone access
        await navigator.mediaDevices.getUserMedia({ audio: true });

        this.conversation = await Conversation.startSession({
            agentId: 'agent_id_goes_here', // Replace with your actual agent ID

            dynamicVariables: {
                user_name: 'Angelo'
            },

            ... add some callbacks here
        });
    } catch (error) {
        console.error('Failed to start conversation:', error);
        alert('Failed to start conversation. Please ensure microphone access is granted.');
    }
  }
}
```

--------------------------------

### Get Studio Project using ElevenLabs SDK in Python

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example shows how to fetch a Studio project using the ElevenLabs Python SDK. Initialize the client and invoke the 'get' method with the project ID.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.get(
    project_id="project_id",
)
```

--------------------------------

### Minimal React SDK Agent Conversation Example

Source: https://elevenlabs.io/docs/eleven-agents/libraries/react

This example demonstrates how to connect to an agent and allow users to start and end a voice conversation using `ConversationProvider` and conversation hooks.

```tsx
import {
  ConversationProvider,
  useConversationControls,
  useConversationStatus,
} from '@elevenlabs/react';

function App() {
  return (
    <ConversationProvider>
      <Agent />
    </ConversationProvider>
  );
}

function Agent() {
  const { startSession, endSession } = useConversationControls();
  const { status } = useConversationStatus();

  if (status === 'connected') {
    return <button onClick={endSession}>End</button>;
  }

  return (
    <button onClick={() => startSession({ agentId: 'agent_7101k5zvyjhmfg983brhmhkd98n6' })}>
      Start
    </button>
  );
}
```

--------------------------------

### Stream Voice Preview using Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/text-to-voice/stream

This Go example demonstrates how to make a GET request to stream a voice preview using the standard net/http package.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Initialize npm and Install Dependencies

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/java-script

Set up npm project and install Vite and ElevenLabs client library required for the web client.

```bash
npm init -y
npm install vite @elevenlabs/client
```

--------------------------------

### Install Backend Dependencies

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/java-script

npm command to install Express, CORS, and dotenv packages required for the backend server setup.

```bash
npm install express cors dotenv
```

--------------------------------

### SDK Examples - Get Conversation Audio

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get-audio

Code examples demonstrating how to retrieve conversation audio using various SDK implementations including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift.

```APIDOC
## SDK Implementation Examples

### TypeScript
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.audio.get("conversation_id");
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.audio.get(
    conversation_id="conversation_id",
)
```

### Go
```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {
	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio"
	req, _ := http.NewRequest("GET", url, nil)
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)
	fmt.Println(res)
	fmt.Println(string(body))
}
```

### Ruby
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Get.new(url)
response = http.request(request)
puts response.read_body
```

### Java
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")
  .asString();
```

### PHP
```php
<?php
require_once('vendor/autoload.php');
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio');
echo $response->getBody();
```

### C#
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

### Swift
```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})
dataTask.resume()
```
```

--------------------------------

### Get a Batch Call (Ruby)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get

Example of fetching batch call information with a GET request using Ruby's Net::HTTP.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Start Frontend Development Server

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/java-script

Shell command to start the frontend development server using npm.

```shell
npm run dev:frontend
```

--------------------------------

### Get Source File URL with Go HTTP Request

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-source-file-url

This example illustrates how to make a direct HTTP GET request in Go to retrieve the source file URL.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/source-file-url"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Knowledge Base Document from File using ElevenLabs SDK

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-file

These examples demonstrate how to upload a file to create a knowledge base document using the official ElevenLabs SDKs. Ensure the SDK is installed and configured with your API key.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.createFromFile({});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.create_from_file(
    file="example_file",
)
```

--------------------------------

### Get Conversation Audio using Go net/http

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This Go example makes a GET request to the ElevenLabs API to retrieve conversation audio. It constructs the URL, sends the request, and prints the response.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Example: System Prompt Hardening

Source: https://elevenlabs.io/docs/eleven-agents/best-practices/guardrails

This example demonstrates how to structure a system prompt using the "# Guardrails" heading to define critical behavioral rules for an ElevenLabs agent.

```mdx
# Guardrails

- Only provide information that is publicly documented about ElevenLabs products, pricing, and features.
- Do not speculate about unreleased features, internal roadmaps, or future pricing changes.
- If you cannot resolve an issue with available documentation or tools, clearly explain the limitation and offer to escalate to a human support representative.
```

--------------------------------

### Get a Batch Call (C# RestSharp)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get

Example of making a GET request to get batch call information using RestSharp in C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Studio Project via HTTP Request in Swift

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example performs an HTTP GET request to fetch a Studio project using 'URLSession' in Swift. Replace 'project_id' in the URL with the actual project identifier.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Install Production Dependencies

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/twilio

Install core runtime packages for the ElevenLabs SDK, Express web framework, WebSocket integration, and Twilio.

```bash
npm install @elevenlabs/elevenlabs-js express express-ws twilio
```

--------------------------------

### Get Project Snapshot with PHP HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

Use the Guzzle HTTP client library for PHP to make a GET request. Requires the Guzzle package to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id');

echo $response->getBody();
```

--------------------------------

### Initialize ElevenLabs Project

Source: https://elevenlabs.io/docs/eleven-agents/operate/cli

Create the basic project structure with configuration and registry files for ElevenLabs agents.

```bash
elevenlabs agents init
```

--------------------------------

### Get Conversation Topics (PHP Guzzle)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/topics/get

Send a GET request using Guzzle HTTP client in PHP to get conversation topics. Ensure Guzzle is installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/topics', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Get Studio Project via HTTP Request in Go

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example makes a direct HTTP GET request to the ElevenLabs API to retrieve a Studio project. Replace 'project_id' with the actual project identifier.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Install ElevenLabs JavaScript SDK

Source: https://elevenlabs.io/docs/eleven-api/resources/libraries/javascript-scribe

Install the ElevenLabs client library using npm, yarn, or pnpm.

```shell
npm install @elevenlabs/client
```

```shell
yarn add @elevenlabs/client
```

```shell
pnpm install @elevenlabs/client
```

--------------------------------

### Get Conversation Audio using C# RestSharp

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This C# example demonstrates fetching conversation audio using the RestSharp library. It creates a client, prepares a GET request, and executes it.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Clone and set up the connector repository

Source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/telephony/vonage

Clone the `elevenlabs-agent-ws-connector` repository from GitHub and prepare the environment by copying the example `.env` file.

```bash
git clone https://github.com/nexmo-se/elevenlabs-agent-ws-connector.git
cd elevenlabs-agent-ws-connector
cp .env.example .env
```

--------------------------------

### GET /v1/convai/conversation/get-signed-url

Source: https://elevenlabs.io/docs/api-reference/conversations/get-signed-url

Get a signed URL to start a conversation with an agent that requires authorization. This endpoint provides the necessary URL for secure conversation initiation.

```APIDOC
## GET /v1/convai/conversation/get-signed-url

### Description
Get a signed url to start a conversation with an agent with an agent that requires authorization

### Method
GET

### Endpoint
/v1/convai/conversation/get-signed-url

### Parameters
#### Query Parameters
- **agent_id** (string) - Required - The id of the agent you're taking the action on.
- **include_conversation_id** (boolean) - Optional - Whether to include a conversation_id with the response. If included, the conversation_signature cannot be used again. (Default: false)
- **branch_id** (string/null) - Optional - The ID of the branch to use
- **environment** (string/null) - Optional - The environment to use for resolving environment variables (e.g. 'production', 'staging'). Defaults to 'production'.

#### Header Parameters
- **xi-api-key** (string) - Optional

### Response
#### Success Response (200)
- **signed_url** (string) - The signed URL to start the conversation.

#### Response Example
```json
{
  "signed_url": "https://example.com/signed-conversation-url"
}
```
```

--------------------------------

### Get Conversation Audio using Ruby Net::HTTP

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This Ruby example demonstrates how to fetch conversation audio using the `Net::HTTP` library. It sets up the URL, creates a GET request, and prints the response body.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Initialize Node.js Project

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/twilio

Commands to create a new project directory, navigate into it, and initialize a new Node.js project using npm.

```bash
mkdir elevenlabs-twilio
cd elevenlabs-twilio
npm init -y
```

--------------------------------

### Get Source File URL with Java Unirest

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-source-file-url

This example uses the Unirest library in Java to make a GET request for the source file URL.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/source-file-url")
  .asString();
```

--------------------------------

### Get Conversation Topics (C# RestSharp)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/topics/get

Execute a GET request using RestSharp in C# to retrieve conversation topics. Install the RestSharp NuGet package in your project.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Phone Number Details in Java

Source: https://elevenlabs.io/docs/api-reference/phone-numbers/get

Use this Java example with Unirest to send a GET request for phone number details. Remember to replace 'phone_number_id' in the URL.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id")
  .asString();
```

--------------------------------

### Create Knowledge Base Folder with Go

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder

Perform an HTTP POST request in Go to create a new folder. This example uses standard library packages for HTTP requests.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/folder"

	payload := strings.NewReader("{\n  \"name\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Initialize Supabase project locally

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/telegram-bot

Create a new local Supabase project after installing the Supabase CLI.

```bash
supabase init
```

--------------------------------

### Get Conversation Audio using ElevenLabs Python SDK

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This example shows how to fetch conversation audio using the ElevenLabs Python SDK. It initializes the client and calls the `get` method with the required conversation ID.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.audio.get(
    conversation_id="conversation_id",
)
```

--------------------------------

### Get Studio Project via HTTP Request in PHP (Guzzle)

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example uses Guzzle HTTP client to make a GET request to retrieve a Studio project. Remember to replace 'project_id' in the URL with the correct project ID.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id');

echo $response->getBody();
```

--------------------------------

### List Available Models Across Languages

Source: https://elevenlabs.io/docs/api-reference/models/list

These examples demonstrate how to retrieve a list of all available ElevenLabs models using various SDKs and direct HTTP requests. Ensure necessary client libraries are installed and configured for each language.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.models.list();
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.models.list()
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/models"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/models")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/models');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/models");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/models")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Conversation Topics (Swift URLSession)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/topics/get

Perform a GET request in Swift using URLSession to fetch conversation topics. This example demonstrates setting headers and handling the response.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Start Local Supabase Stack

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming-and-caching-with-supabase

Use this command to initialize and run your local Supabase services, including the database and other necessary components.

```bash
supabase start
```

--------------------------------

### System Prompt Example for Complex Tool Scenarios

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/client-tools

This example demonstrates how to provide context in the system prompt for complex tool usage, such as pre-checking availability before scheduling a meeting.

```plaintext
Before scheduling a meeting with `schedule_meeting`, check the user's calendar for availability using check_availability to avoid conflicts.
```

--------------------------------

### Get Conversation Topics (Go HTTP Request)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/topics/get

Perform a GET request in Go to retrieve conversation topics. This example uses standard library packages for HTTP communication.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/topics"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Next.js project

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/next-js

Initialize a new Next.js application with the default configuration.

```bash
npm create next-app my-conversational-agent
```

--------------------------------

### Get Tool Executions using Swift HTTP Request (URLSession)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-executions

Execute a GET request in Swift using URLSession to retrieve tool executions. This example sets up the request headers and body for the API call.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools/tool_id/executions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Studio Project using ElevenLabs SDK in TypeScript

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example demonstrates how to retrieve a specific Studio project using the ElevenLabs TypeScript SDK. Initialize the client and call the 'get' method with the project ID.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.get("project_id", {});
}
main();
```

--------------------------------

### Create Project Directory

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/raspberry-pi-voice-assistant

Create a new directory for the voice assistant project and navigate into it.

```bash
mkdir eleven-voice-assistant
cd eleven-voice-assistant
```

--------------------------------

### Get Phone Number Details in C#

Source: https://elevenlabs.io/docs/api-reference/phone-numbers/get

This C# example uses RestSharp to perform a GET request for phone number details. Replace 'phone_number_id' in the URL with the actual ID.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Conversation Audio using ElevenLabs TypeScript SDK

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This example demonstrates how to retrieve conversation audio using the ElevenLabs TypeScript SDK. It initializes the client and calls the `get` method with a conversation ID.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.audio.get("conversation_id");
}
main();
```

--------------------------------

### Create Test Folder in Go

Source: https://elevenlabs.io/docs/api-reference/tests/test-folders/create

This example demonstrates how to make an HTTP POST request to create a new test folder. The folder will be named 'string'.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/folders"

	payload := strings.NewReader("{\n  \"name\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Install ElevenLabs Node.js Library

Source: https://elevenlabs.io/docs/api-reference/introduction

Use npm to install the official ElevenLabs Node.js library in your project directory.

```bash
npm install @elevenlabs/elevenlabs-js
```

--------------------------------

### Express Server Setup with OpenAI Client

Source: https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm

Initializes Express application with JSON middleware and OpenAI client configuration. Required setup before defining streaming endpoints.

```typescript
import express, { Request, Response } from 'express';
import OpenAI from 'openai';

const app = express();
app.use(express.json());

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
```

--------------------------------

### Upload Music using ElevenLabs SDK

Source: https://elevenlabs.io/docs/api-reference/music/upload

These examples demonstrate how to upload music files using the official ElevenLabs SDKs. Ensure the SDK is installed and configured with your API key.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.upload({});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.upload(
    file="example_file",
)
```

--------------------------------

### Recommended Tool Parameter Description: Explicit Format

Source: https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide

This snippet shows how to provide explicit format examples in tool parameter descriptions, guiding the LLM to generate correctly formatted values for tool calls.

```mdx
## `lookupAccount` tool parameters

- `email` (required): "The user's email in standard email format, e.g. 'john@gmail.com'."
- `phone` (required): "The user's phone number as digits only, e.g. '5551234567'."
- `confirmation_code` (required): "The user's confirmation code as a single alphanumeric string without spaces, e.g. 'ABC123'."
```

--------------------------------

### Initialize agent with system tools in Python

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools

Python SDK example for creating an ElevenLabs agent with end_call and language_detection system tools. Requires the elevenlabs package and API key.

```python
from elevenlabs import (
    ConversationalConfig,
    ElevenLabs,
    AgentConfig,
    PromptAgent,
    PromptAgentInputToolsItem_System,
)

# Initialize the client
elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

# Create system tools
end_call_tool = PromptAgentInputToolsItem_System(
    name="end_call",
    description=""  # Optional: Customize when the tool should be triggered
)

language_detection_tool = PromptAgentInputToolsItem_System(
    name="language_detection",
    description=""  # Optional: Customize when the tool should be triggered
)

# Create the agent configuration with both tools
conversation_config = ConversationalConfig(
    agent=AgentConfig(
        prompt=PromptAgent(
            tools=[end_call_tool, language_detection_tool]
        )
    )
)

# Create the agent
response = elevenlabs.conversational_ai.agents.create(
    conversation_config=conversation_config
)
```

--------------------------------

### Get Tool Executions using Go HTTP Request

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-executions

Perform a GET request in Go to the ElevenLabs API endpoint for tool executions. This example uses the standard 'net/http' package.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/tools/tool_id/executions"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### System Prompt for Voice Switching Instructions

Source: https://elevenlabs.io/docs/eleven-agents/customization/voice/multi-voice-support

This example shows how the system automatically adds instructions to the agent's prompt, informing the LLM about available voices and the markup syntax to use.

```text
When a message should be spoken by a particular person, use markup: "<CHARACTER>message</CHARACTER>" where CHARACTER is the character label.

Available voices are as follows:
- default: any text outside of the CHARACTER tags
- Joe: Whenever Joe is speaking
- Spanish: For any Spanish words or phrases
- Narrator: For narrative descriptions
```

--------------------------------

### Get Conversational AI Test Summaries

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/summaries

This example demonstrates how to retrieve summaries for specified conversational AI tests using various SDKs and HTTP clients. Provide a list of 'test_ids' to get their corresponding summaries.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.summaries({
        testIds: [
            "test_id_1",
            "test_id_2",
        ],
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.summaries(
    test_ids=[
        "test_id_1",
        "test_id_2"
    ],
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/summaries"

	payload := strings.NewReader("{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/summaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agent-testing/summaries")
  .header("Content-Type", "application/json")
  .body("{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agent-testing/summaries', [
  'body' => '{
  "test_ids": [
    "test_id_1",
    "test_id_2"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/summaries");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"test_ids\": [\n    \"test_id_1\",\n    \"test_id_2\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["test_ids": ["test_id_1", "test_id_2"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/summaries")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Tool Configuration in Go

Source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create

This snippet illustrates how to make a direct HTTP POST request in Go to create a tool configuration.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs"

	payload := strings.NewReader("{\n  \"tool_name\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Install and initialize Tailwind CSS for Next.js

Source: https://elevenlabs.io/docs/eleven-agents/libraries/web-sockets

Installs Tailwind CSS, PostCSS, and Autoprefixer, then initializes Tailwind CSS configuration for a Next.js project. This is optional for styling.

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

--------------------------------

### Install ElevenLabs JavaScript SDK

Source: https://elevenlabs.io/docs/eleven-agents/libraries/java-script

Install the @elevenlabs/client package using npm, yarn, or pnpm. Choose the package manager appropriate for your project.

```shell
npm install @elevenlabs/client
# or
yarn add @elevenlabs/client
# or
pnpm install @elevenlabs/client
```

--------------------------------

### Get Conversation Audio using PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This PHP example utilizes the Guzzle HTTP client to make a GET request for conversation audio. It prints the body of the HTTP response.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio');

echo $response->getBody();
```

--------------------------------

### Install ElevenLabs SDK and dependencies

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue

Install the ElevenLabs SDK and dotenv library for loading environment variables. Choose the package manager and language appropriate for your project.

```python
pip install elevenlabs
pip install python-dotenv
```

```typescript
npm install @elevenlabs/elevenlabs-js
npm install dotenv
```

--------------------------------

### List Studio Projects

Source: https://elevenlabs.io/docs/api-reference/studio/get-projects

Use the ElevenLabs SDK or direct HTTP requests to retrieve a list of all studio projects. This example demonstrates a GET request to the /v1/studio/projects endpoint.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.list();
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.list()
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Conversation Audio using Java Unirest

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This Java example uses the Unirest library to perform a GET request to the ElevenLabs API for conversation audio. It retrieves the response as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")
  .asString();
```

--------------------------------

### Install ElevenLabs React SDK

Source: https://elevenlabs.io/docs/eleven-agents/libraries/react

Install the ElevenLabs React SDK package using npm, yarn, or pnpm.

```shell
npm install @elevenlabs/react
# or
yarn add @elevenlabs/react
# or
pnpm install @elevenlabs/react
```

--------------------------------

### Example Authorization Header Value

Source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/twilio-integration/sms-otp-verification

This shows an example of the full Authorization header value, combining 'Basic' with the Base64-encoded credentials. This value should be stored as a tool secret.

```text
Basic dkFDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==
```

--------------------------------

### Set Up Python Virtual Environment

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/raspberry-pi-voice-assistant

Create and activate a Python virtual environment to manage project dependencies in isolation.

```bash
python -m venv .venv # Only required the first time you set up the project
source .venv/bin/activate
```

--------------------------------

### Get Studio Project via HTTP Request in C# (RestSharp)

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example shows how to get a Studio project using RestSharp in C#. Update the URL with the specific 'project_id' you wish to retrieve.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Install ElevenLabs SDK

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming

Install the necessary ElevenLabs SDK packages for React or plain JavaScript projects to begin integrating Realtime Scribe.

```bash
npm install @elevenlabs/react @elevenlabs/elevenlabs-js
```

```bash
npm install @elevenlabs/client @elevenlabs/elevenlabs-js
```

--------------------------------

### List Knowledge Base - Go HTTP

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/list

Make a GET request to the knowledge base endpoint using Go's standard http package. Requires manual request setup and response body reading.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Start Next.js Development Server (Bash)

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/upstash-redis

Initiates the Next.js development server locally to run the application.

```bash
pnpm dev
```

--------------------------------

### Get Conversation Audio using Swift URLSession

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

This Swift example uses `URLSession` to perform a GET request to retrieve conversation audio. It handles the asynchronous response and prints the HTTP response.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/conversation_id/audio")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Install elevenlabs with pyaudio extra

Source: https://elevenlabs.io/docs/eleven-agents/libraries/python

Install elevenlabs with the pyaudio extra for default audio input/output support. May require additional system dependencies depending on your OS.

```shell
pip install "elevenlabs[pyaudio]"
# or
poetry add "elevenlabs[pyaudio]"
```

--------------------------------

### Install ElevenLabs Python Library

Source: https://elevenlabs.io/docs/api-reference/introduction

Use pip to install the official ElevenLabs Python bindings.

```bash
pip install elevenlabs
```

--------------------------------

### Install ElevenLabs SDK and dotenv

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/dubbing

Install the necessary ElevenLabs SDK and dotenv library for your chosen programming language.

```python
pip install elevenlabs
pip install python-dotenv
```

```typescript
npm install @elevenlabs/elevenlabs-js
npm install dotenv
```

--------------------------------

### Example: Advertisement with Voiceover Composition Plan

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans

Demonstrates a composition plan for an advertisement, featuring distinct instrumental and voiceover sections with specific styles and spoken lines.

```json
{
  "positive_global_styles": ["upbeat", "modern pop", "energetic", "120 BPM"],
  "negative_global_styles": ["sad", "slow", "dark"],
  "sections": [
    {
      "section_name": "Intro",
      "positive_local_styles": ["instrumental", "catchy hook"],
      "negative_local_styles": ["vocals"],
      "duration_ms": 5000,
      "lines": []
    },
    {
      "section_name": "Voiceover",
      "positive_local_styles": ["spoken voiceover", "confident male voice", "background music"],
      "negative_local_styles": ["singing"],
      "duration_ms": 10000,
      "lines": ["Introducing the future of productivity", "Work smarter, not harder"]
    },
    {
      "section_name": "Outro",
      "positive_local_styles": ["musical sting", "memorable"],
      "negative_local_styles": ["vocals"],
      "duration_ms": 5000,
      "lines": []
    }
  ]
}
```

--------------------------------

### Get Studio Project via HTTP Request in Java (Unirest)

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example demonstrates fetching a Studio project using Unirest in Java. The 'project_id' in the URL should be replaced with the actual project identifier.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id")
  .asString();
```

--------------------------------

### Get Studio Project via HTTP Request in Ruby

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

This example uses Ruby's 'Net::HTTP' to perform a GET request for a Studio project. Ensure to replace 'project_id' in the URL with the target project's ID.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Create Project Directory with Bash

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/java-script

Initialize a new project directory for the ElevenLabs conversational AI application.

```bash
mkdir elevenlabs-conversational-ai
cd elevenlabs-conversational-ai
```

--------------------------------

### Get character usage statistics with PHP Guzzle client

Source: https://elevenlabs.io/docs/api-reference/usage/get

Make a GET request to the ElevenLabs usage endpoint using the Guzzle HTTP client. Requires guzzlehttp/guzzle package installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/usage/character-stats?start_unix=1685574000&end_unix=1688165999');

echo $response->getBody();
```

--------------------------------

### Initialize ElevenLabs SDK and Start Conversation Session (Kotlin)

Source: https://elevenlabs.io/docs/eleven-agents/libraries/kotlin

This snippet demonstrates how to configure and start a conversation session with the ElevenLabs SDK, including setting up various callbacks for connection status, messages, mode changes, and registering a client tool. It supports both public and private agent initialization.

```kotlin
import io.elevenlabs.ConversationClient
import io.elevenlabs.ConversationConfig
import io.elevenlabs.ConversationSession
import io.elevenlabs.ClientTool
import io.elevenlabs.ClientToolResult

// Start a public agent session (token generated for you)
val config = ConversationConfig(
    agentId = "<your_public_agent_id>", // OR conversationToken = "<token>"
    userId = "your-user-id",
    // Optional callbacks
    onConnect = { conversationId ->
        // Called when the conversation is connected and returns the conversation ID. You can access conversationId via session.getId() too
    },
    onMessage = { source, messageJson ->
        // Raw JSON messages from data channel; useful for logging/telemetry
    },
    onModeChange = { mode ->
        // "speaking" | "listening" — drive UI indicators
    },
    onStatusChange = { status ->
        // "connected" | "connecting" | "disconnected"
    },
    onCanSendFeedbackChange = { canSend ->
        // Enable/disable thumbs up/down buttons for feedback reporting
    },
    onUnhandledClientToolCall = { call ->
        // Agent requested a client tool not registered on the device
    },
    onVadScore = { score ->
        // Voice Activity Detection score, range from 0 to 1 where higher values indicate higher confidence of speech
    },
    onAudioAlignment = { alignment ->
        // Character-level timing data for synchronized text display
        val chars = alignment["chars"] as? List<*>
        val startTimes = alignment["char_start_times_ms"] as? List<*>
        val durations = alignment["char_durations_ms"] as? List<*>
        Log.d("ExampleApp", "Audio alignment: $chars")
    },
    // List of client tools the agent can invoke
    clientTools = mapOf(
        "logMessage" to object : ClientTool {
            override suspend fun execute(parameters: Map<String, Any>): ClientToolResult {
                val message = parameters["message"] as? String

                Log.d("ExampleApp", "[INFO] Client Tool Log: $message")
                return ClientToolResult.success("Message logged successfully")
            }
        }
    )
)

// In an Activity context
val session: ConversationSession = ConversationClient.startSession(config, this)
```

--------------------------------

### Get Agent Link - PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/agents/get-link

Retrieve an agent link using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer and sends a GET request to the API endpoint.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/link');

echo $response->getBody();
```

--------------------------------

### Create an Instant Voice Clone with Python or TypeScript

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/instant-voice-cloning

This snippet demonstrates how to create an Instant Voice Clone by providing a voice name and audio files. Ensure your API key and SDK are set up as per the quickstart guide.

```python
# example.py
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from io import BytesIO

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

voice = elevenlabs.voices.ivc.create(
    name="My Voice Clone",
    # Replace with the paths to your audio files.
    # The more files you add, the better the clone will be.
    files=[BytesIO(open("/path/to/your/audio/file.mp3", "rb").read())]
)

print(voice.voice_id)
```

```typescript
// example.mts
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";
import fs from "node:fs";

const elevenlabs = new ElevenLabsClient();

const voice = await elevenlabs.voices.ivc.create({
    name: "My Voice Clone",
    // Replace with the paths to your audio files.
    // The more files you add, the better the clone will be.
    files: [
        fs.createReadStream(
            "/path/to/your/audio/file.mp3",
        ),
    ],
});

console.log(voice.voiceId);
```

--------------------------------

### Get Shared Voices with PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/voices/voice-library/get-shared

Fetch shared voices from the ElevenLabs API using the Guzzle HTTP client in PHP. This example demonstrates making a GET request and echoing the response body.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/shared-voices');

echo $response->getBody();
```

--------------------------------

### Create MCP Server (Go HTTP Request)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/create

Make a direct HTTP POST request in Go to create an MCP server. This example shows how to construct the request body with server configuration and handle the response.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers"

	payload := strings.NewReader("{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Stream Voice Preview using PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/text-to-voice/stream

This PHP example uses GuzzleHttp to send a GET request and retrieve the streamed voice preview.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream');

echo $response->getBody();
```

--------------------------------

### Create Knowledge Base Folder with Go

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/create-folder

This snippet demonstrates how to create a new folder in an ElevenLabs knowledge base using a standard Go HTTP client.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/folder"

	payload := strings.NewReader("{\n  \"name\": \"Project Documentation\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Apply Agent and TTS Overrides in JavaScript

Source: https://elevenlabs.io/docs/eleven-agents/customization/personalization/overrides

Use this JavaScript example to apply overrides for agent prompt, LLM, first message, language, TTS settings, and conversation parameters when starting a session.

```javascript
...
const conversation = await Conversation.startSession({
  ...
  overrides: {
      agent: {
          prompt: {
              prompt: `The customer's bank account balance is ${customer_balance}. They are based in ${customer_location}.`, // Optional: override the system prompt.
              llm: "gpt-4o" // Optional: override the LLM model.
          },
          firstMessage: `Hi ${customer_name}, how can I help you today?`, // Optional: override the first message.
          language: "en" // Optional: override the language.
      },
      tts: {
          voiceId: "custom_voice_id", // Optional: override the voice.
          stability: 0.7, // Optional: override stability (0.0 to 1.0).
          speed: 1.1, // Optional: override speed (0.7 to 1.2).
          similarityBoost: 0.9 // Optional: override similarity boost (0.0 to 1.0).
      },
      conversation: {
          textOnly: true // Optional: enable text-only mode (no audio).
      }
  },
  ...
})
```

--------------------------------

### Initialize ElevenLabs Client - Python

Source: https://elevenlabs.io/docs/api-reference/authentication

Set up the ElevenLabs Python client with your API key for authenticated requests.

```python
from elevenlabs.client import ElevenLabs

elevenlabs = ElevenLabs(
  api_key='YOUR_API_KEY',
)
```

--------------------------------

### SDK Examples - Stream Voice Preview

Source: https://elevenlabs.io/docs/api-reference/text-to-voice/stream

Code examples demonstrating how to call the stream voice preview endpoint using various SDK implementations across different programming languages.

```APIDOC
### TypeScript/JavaScript
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.textToVoice.preview.stream("generated_voice_id");
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.text_to_voice.preview.stream(
    generated_voice_id="generated_voice_id",
)
```

### Go
```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {
	url := "https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream"
	req, _ := http.NewRequest("GET", url, nil)
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)
	fmt.Println(res)
	fmt.Println(string(body))
}
```

### Ruby
```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Get.new(url)
response = http.request(request)
puts response.read_body
```

### Java
```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream")
  .asString();
```

### PHP
```php
<?php
require_once('vendor/autoload.php');
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream');
echo $response->getBody();
```

### C#
```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

### Swift
```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
```

--------------------------------

### Navigate to project directory

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/next-js

Change into the newly created Next.js project directory.

```shell
cd my-conversational-agent
```

--------------------------------

### Get Tool Executions using PHP HTTP Request (Guzzle)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-executions

Send a GET request in PHP using Guzzle HTTP client to retrieve tool executions. This requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tools/tool_id/executions', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Stream Voice Preview using Swift URLSession

Source: https://elevenlabs.io/docs/api-reference/text-to-voice/stream

This Swift example uses URLSession to perform a GET request and handle the response for streaming a voice preview.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/text-to-voice/generated_voice_id/stream")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Initialize agent with system tools in JavaScript

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools

JavaScript SDK example for creating an ElevenLabs agent with end_call and language_detection system tools. Requires the @elevenlabs/elevenlabs-js package and API key.

```javascript
import { ElevenLabs } from '@elevenlabs/elevenlabs-js';

// Initialize the client
const elevenlabs = new ElevenLabs({
  apiKey: 'YOUR_API_KEY',
});

// Create the agent with system tools
await elevenlabs.conversationalAi.agents.create({
  conversationConfig: {
    agent: {
      prompt: {
        tools: [
          {
            type: 'system',
            name: 'end_call',
            description: '',
          },
          {
            type: 'system',
            name: 'language_detection',
            description: '',
          },
        ],
      },
    },
  },
});
```

--------------------------------

### Get Conversational AI Dashboard Settings

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/dashboard/get

These examples demonstrate how to retrieve the current dashboard settings for Conversational AI using different programming languages and SDKs.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.dashboard.settings.get();
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.dashboard.settings.get()
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/settings/dashboard"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/settings/dashboard")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/settings/dashboard")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/settings/dashboard');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/settings/dashboard");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings/dashboard")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Voice Sample Audio

Source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-audio

These examples demonstrate how to retrieve an audio sample for a given voice and sample ID. Replace 'voice_id' and 'sample_id' with actual values.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.audio.get("voice_id", "sample_id", {});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.audio.get(
    voice_id="voice_id",
    sample_id="sample_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/audio"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/audio")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/audio")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/audio');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/audio");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/audio")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Install ElevenLabs AI SDK provider

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/vercel-ai-sdk

Install the @ai-sdk/elevenlabs module to enable ElevenLabs transcription support in Vercel AI SDK.

```bash
npm install @ai-sdk/elevenlabs
```

--------------------------------

### Python WebSocket setup with environment variables

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming

Initializes WebSocket connection with dotenv for credential management. Requires asyncio, websockets, and python-dotenv packages.

```python
# Use this example if you are unable to use the SDK
import asyncio
import base64
import json
import websockets
from dotenv import load_dotenv
import os

load_dotenv()
```

--------------------------------

### Install ElevenLabs CLI

Source: https://elevenlabs.io/docs/eleven-agents/quickstart

Install the ElevenLabs Command Line Interface globally using npm to manage agents and interact with the platform.

```bash
npm install -g @elevenlabs/cli
```

--------------------------------

### Create or Get RAG Indexes (Ruby HTTP Request)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/compute-rag-index-batch

Perform an HTTP POST request in Ruby to interact with the ElevenLabs RAG index API. This example sends a JSON payload to create or get indexes.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"document_id\": \"string\",\n      \"create_if_missing\": true,\n      \"model\": \"e5_mistral_7b_instruct\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Create Studio Project with Multipart Form Data - Java

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

Java example using Unirest to POST a multipart form-data request to create a studio project. Includes project metadata fields and file upload capability.

```java
.body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

--------------------------------

### Specifying Tool Parameter Formats for Email

Source: https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide

Demonstrates how to provide explicit format examples for tool parameters, such as an email address, to improve LLM accuracy in constructing tool calls.

```mdx
## `lookupAccount` tool parameters

- `email` (required): "The customer's email address."
```

```mdx
## `lookupAccount` tool parameters

- `email` (required): "The customer's email in standard email format, e.g. 'john.smith@company.com'."
```

--------------------------------

### Get Phone Number Details in Go

Source: https://elevenlabs.io/docs/api-reference/phone-numbers/get

This example demonstrates how to make a GET request to retrieve phone number details using Go's standard net/http library. Replace 'phone_number_id' in the URL with the target ID.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/phone-numbers/phone_number_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Video to Music with Swift HTTP Client

Source: https://elevenlabs.io/docs/api-reference/music/video-to-music

Construct a multipart form-data request manually in Swift by building the body string with boundary delimiters and parameter encoding. Incomplete example showing parameter setup.

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "videos",
    "fileName": "string"
  ],
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "tags",
    "value": 
  ],
  [
    "name": "sign_with_c2pa",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
```

--------------------------------

### Install Debian System Dependencies

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/raspberry-pi-voice-assistant

Install necessary audio libraries on Debian-based systems like Raspberry Pi OS using apt-get.

```bash
sudo apt-get update
sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
```

--------------------------------

### Get WhatsApp Account Information

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/whats-app/accounts/get

These examples demonstrate how to retrieve details for a specific WhatsApp account using its phone number ID. The examples cover both SDK usage and direct HTTP requests across various programming languages.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.whatsappAccounts.get("phone_number_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.whatsapp_accounts.get(
    phone_number_id="phone_number_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body

```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/whatsapp-accounts/phone_number_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Shared Voices with Swift URLSession

Source: https://elevenlabs.io/docs/api-reference/voices/voice-library/get-shared

Make an HTTP GET request to the ElevenLabs shared voices API using Swift's Foundation framework and URLSession. This example demonstrates setting up the request and handling the asynchronous response.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/shared-voices")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Tool Configuration for MCP Server

Source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/get

Use these examples to retrieve the configuration details for a specific tool associated with a Managed Conversational Platform (MCP) server. Replace "mcp_server_id" and "tool_name" with your actual server and tool identifiers.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.toolConfigs.get("mcp_server_id", "tool_name");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tool_configs.get(
    mcp_server_id="mcp_server_id",
    tool_name="tool_name",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body

```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")
  .asString();

```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name');

echo $response->getBody();

```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);

```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()

```

--------------------------------

### POST /v1/audio-native

Source: https://elevenlabs.io/docs/api-reference/audio-native/create

Creates Audio Native enabled project, optionally starts conversion and returns project ID and embeddable HTML snippet.

```APIDOC
## POST /v1/audio-native

### Description
Creates Audio Native enabled project, optionally starts conversion and returns project ID and embeddable HTML snippet.

### Method
POST

### Endpoint
/v1/audio-native

### Parameters
#### Headers
- **xi-api-key** (string) - Optional - 

#### Request Body
- **name** (string) - Required - Project name.
- **image** (string) - Optional - (Deprecated) Image URL used in the player. If not provided, default image set in the Player settings is used.
- **author** (string) - Optional - Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.
- **title** (string) - Optional - Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.
- **small** (boolean) - Optional - (Deprecated) Whether to use small player or not. If not provided, default value set in the Player settings is used. Default: `false`.
- **text_color** (string) - Optional - Text color used in the player. If not provided, default text color set in the Player settings is used.
- **background_color** (string) - Optional - Background color used in the player. If not provided, default background color set in the Player settings is used.
- **sessionization** (integer) - Optional - (Deprecated) Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used. Default: `0`.
- **voice_id** (string) - Optional - Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.
- **model_id** (string) - Optional - TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.
- **file** (string, binary) - Required - Either txt or HTML input file containing the article content. HTML should be formatted as follows '<html><body><div><p>Your content</p><h3>More of your content</h3><p>Some more of your content</p></div></body></html>'
- **auto_convert** (boolean) - Optional - Whether to auto convert the project to audio or not. Default: `false`.
- **apply_text_normalization** (object/null) - Optional - 

### Request Example
```json
{
  "name": "My New Audio Project",
  "file": "<p>This is some content for the audio project.</p>",
  "auto_convert": true
}
```

### Response
#### Success Response (200)
Refer to `AudioNativeCreateProjectResponseModel` schema for details.

#### Error Response (422)
Refer to `HTTPValidationError` schema for details.
```

--------------------------------

### Get Usage By Product Over Time (Go)

Source: https://elevenlabs.io/docs/api-reference/workspace/usage/get-usage-by-product-over-time

Make a direct HTTP POST request in Go to query workspace usage by product over time.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time"

	payload := strings.NewReader("{\n  \"start_time\": 1680307200000,\n  \"end_time\": 1682899200000\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Agent - PHP HTTP

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get

Retrieve an agent using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id');

echo $response->getBody();
```

--------------------------------

### Get Tool - PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/tools/get

Retrieve a tool using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tools/tool_id');

echo $response->getBody();
```

--------------------------------

### Get Source File URL with C# RestSharp

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-source-file-url

This example demonstrates fetching the source file URL using the RestSharp library in C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/source-file-url");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### JavaScript module setup with environment variables

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket

Initializes required modules, loads environment variables, and configures WebSocket URI with API key and model ID. Must be executed before calling conversationAgentDemo().

```javascript
import dotenv from 'dotenv';
import fs from 'fs';
import WebSocket from 'ws';

// Load environment variables
dotenv.config();
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
const VOICE_ID = 'your_voice_id';
const MODEL_ID = 'eleven_flash_v2_5';

const WEBSOCKET_URI = `wss://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}/multi-stream-input?model_id=${MODEL_ID}`;
```

--------------------------------

### Configuring Tool Usage in AI Agent System Prompts

Source: https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide

Provide clear instructions in the system prompt on when and how to use specific tools like getOrderStatus and processRefund, including usage context and error handling.

```mdx
# Tools

You have access to the following tools:

## `getOrderStatus`

Use this tool when a customer asks about their order. Always call this tool before providing order information—never rely on memory or assumptions.

**When to use:**

- Customer asks "Where is my order?"
- Customer provides an order number
- Customer asks about delivery estimates

**How to use:**

1. Collect the order ID from the customer
2. Call `getOrderStatus` with the order ID
3. Present the results to the customer in natural language

**Error handling:**
If the tool returns "Order not found", ask the customer to verify the order number and try again.

## `processRefund`

Use this tool only after verifying:

1. Customer identity has been confirmed
2. Order is eligible for refund (within 30 days, not already refunded)
3. Refund amount is under $500 (escalate to supervisor if over $500)

**Required before calling:**

- Order ID (from `getOrderStatus`)
- Refund reason code
- Customer confirmation

This step is important: Always confirm refund details with the customer before calling this tool.
```

--------------------------------

### Get Shared Voices with Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/voices/voice-library/get-shared

Perform a direct HTTP GET request to the ElevenLabs shared voices API endpoint using Go's standard net/http package. This example demonstrates how to make the request and print the response body.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/shared-voices"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### POST /v1/studio/projects

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

Creates a new Studio project with flexible initialization options. Projects can be initialized as blank, from a document file, from a URL, or from JSON content. Supports configuration of default voices for titles and paragraphs, model selection, and audio quality presets.

```APIDOC
## POST /v1/studio/projects

### Description
Creates a new Studio project. The project can be initialized as blank, from a document, from a URL, or from JSON content. Allows configuration of default voices and audio quality settings.

### Method
POST

### Endpoint
/v1/studio/projects

### Parameters
#### Header Parameters
- **xi-api-key** (string) - Optional - API key for authentication

#### Request Body
- **name** (string) - Required - The name of the Studio project, used for identification only.
- **default_title_voice_id** (string or null) - Optional - The voice_id that corresponds to the default voice used for new titles.
- **default_paragraph_voice_id** (string or null) - Optional - The voice_id that corresponds to the default voice used for new paragraphs.
- **default_model_id** (string or null) - Optional - The ID of the model to be used for this Studio project. Query GET /v1/models to list all available models.
- **from_url** (string or null) - Optional - A URL from which content will be extracted to initialize the Studio project. If set, 'from_document' and 'from_content_json' must be null.
- **from_document** (binary) - Optional - An .epub, .pdf, .txt or similar file to initialize the Studio project with its content. If set, 'from_url' and 'from_content_json' must be null.
- **from_content_json** (string) - Optional - JSON content to initialize the Studio project. If set, 'from_url' and 'from_document' must be null. If none of these three fields are provided, the project initializes as blank.
- **quality_preset** (string) - Optional - Output quality of the generated audio. Must be one of: 'standard' (128kbps, 44.1kHz), 'high' (192kbps, 44.1kHz with improvements), or 'ultra' (192kbps, 44.1kHz with highest improvements).

### Request Example
```json
{
  "name": "My Studio Project",
  "default_title_voice_id": "6lCwbsX1yVjD49QmpkT0",
  "default_paragraph_voice_id": "6lCwbsX1yVjD49QmpkT1",
  "default_model_id": "eleven_monolingual_v1",
  "quality_preset": "high"
}
```

### Response
#### Success Response (200)
- **AddProjectResponseModel** (object) - The created Studio project details

#### Error Response (422)
- **HTTPValidationError** (object) - Validation error details
```

--------------------------------

### Get Conversation Tag - PHP

Source: https://elevenlabs.io/docs/api-reference/conversations/tags/get

Retrieve a conversation tag using the Guzzle HTTP client in PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tags/tag_id');

echo $response->getBody();
```

--------------------------------

### Install Development Dependencies

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/twilio

Install development-specific packages for TypeScript support, environment variable loading, and project execution.

```bash
npm i @types/node @types/express @types/express-ws @types/ws dotenv tsx typescript
```

--------------------------------

### Install ElevenLabs CLI

Source: https://elevenlabs.io/docs/eleven-agents/operate/cli

Install the ElevenLabs CLI globally using your preferred package manager. Node.js v16.0.0 or higher is required.

```bash
npm install -g @elevenlabs/cli
```

```bash
pnpm add -g @elevenlabs/cli
```

```bash
yarn global add @elevenlabs/cli
```

--------------------------------

### List Knowledge Base - C# HTTP

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/list

Make a GET request using RestSharp library for C#. Requires client and request object setup.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Studio Project Chapter - Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/add-chapter

Uses Go's standard net/http package to make a POST request to the ElevenLabs API. Requires manual JSON payload construction and header management.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters"

	payload := strings.NewReader("{\n  \"name\": \"Chapter 1\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Speaker Audio - PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-separated-speaker-audio

Retrieve speaker audio using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/speakers/speaker_id/audio');

echo $response->getBody();
```

--------------------------------

### Create Music Composition Plan with Prompt

Source: https://elevenlabs.io/docs/api-reference/music/create-composition-plan

This snippet demonstrates how to generate a music composition plan using a text prompt. It shows examples across various programming languages, utilizing both SDKs and direct HTTP requests to the `/v1/music/plan` endpoint.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.compositionPlan.create({
        prompt: "string",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.composition_plan.create(
    prompt="string",
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/music/plan"

	payload := strings.NewReader("{\n  \"prompt\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/music/plan")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"prompt\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/plan")
  .header("Content-Type", "application/json")
  .body("{\n  \"prompt\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/plan', [
  'body' => '{
  "prompt": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/plan");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"prompt\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["prompt": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/plan")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Topics - PHP HTTP Request

Source: https://elevenlabs.io/docs/api-reference/conversations/topics/get

Retrieve conversation topics using Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/topics');

echo $response->getBody();
```

--------------------------------

### List MCP Server Tools

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/list-tools

Use these examples to retrieve all tools configured for a specific MCP server. Replace 'mcp_server_id' with the actual ID of your MCP server.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.tools.list("mcp_server_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tools.list(
    mcp_server_id="mcp_server_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body

```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools")
  .asString();

```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools');

echo $response->getBody();

```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);

```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()

```

--------------------------------

### Get Voice Sample Waveform

Source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/get-waveform

These examples demonstrate how to retrieve the waveform of a specific voice sample from the ElevenLabs API. Replace 'voice_id' and 'sample_id' with actual values.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.waveform.get("voice_id", "sample_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.waveform.get(
    voice_id="voice_id",
    sample_id="sample_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/waveform"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/waveform")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/waveform")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/waveform');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/waveform");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id/waveform")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Execute Python Example Script

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries

Runs the Python script to demonstrate the effect of the pronunciation dictionary.

```python
python example.py
```

--------------------------------

### Python async main entry point

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket

Entry point for running the Python conversation agent demo using asyncio. Execute this to start the async conversation flow.

```python
if __name__ == "__main__":
    asyncio.run(conversation_agent_demo())
```

--------------------------------

### Get Pronunciation Dictionary by ID (Multi-language)

Source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/get

Use these examples to retrieve a specific pronunciation dictionary by its unique identifier. Ensure you replace 'pronunciation_dictionary_id' with the actual ID.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.get("pronunciation_dictionary_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.get(
    pronunciation_dictionary_id="pronunciation_dictionary_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/pronunciation-dictionaries/pronunciation_dictionary_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any);
  } else {
    let httpResponse = response as? HTTPURLResponse;
    print(httpResponse);
  }
})

dataTask.resume();
```

--------------------------------

### Get Secret - PHP HTTP Request

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/get

Retrieve a workspace secret using the Guzzle HTTP client library for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Convert Speech-to-Speech using ElevenLabs Python SDK

Source: https://elevenlabs.io/docs/api-reference/speech-to-speech/convert

This example shows how to use the ElevenLabs Python SDK for speech-to-speech conversion. Provide the voice ID, output format, and the audio input.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="xi-api-key",
)

client.speech_to_speech.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128",
    audio="example_audio",
)
```

--------------------------------

### Get workspace settings with PHP HTTP client

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/get

Retrieve workspace settings using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/settings', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Create Voice using ElevenLabs SDK

Source: https://elevenlabs.io/docs/api-reference/voices/ivc/create

Shows how to create a voice using the ElevenLabs SDK. The Python example demonstrates including files for voice creation.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.ivc.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.ivc.create(
    files=["example_files"],
)

```

--------------------------------

### Install voice-stream package for audio input

Source: https://elevenlabs.io/docs/eleven-agents/libraries/web-sockets

Installs the `voice-stream` package, which handles microphone access, audio streaming, and base64 encoding for ElevenLabs API.

```bash
npm install voice-stream
```

--------------------------------

### Initialize ElevenLabs Client - Node.js

Source: https://elevenlabs.io/docs/api-reference/authentication

Set up the ElevenLabs Node.js client with your API key for authenticated requests.

```javascript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: 'YOUR_API_KEY',
});
```

--------------------------------

### Create Agent Draft (Swift)

Source: https://elevenlabs.io/docs/api-reference/agents/drafts/create

This Swift example demonstrates how to construct the request payload and make a POST call to create a new agent draft. It includes defining the agent's workflow with various nodes and edges.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "workflow": [
    "edges": [
      "entry_to_tool_a": [
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": ["condition": "Tool A condition"]
      ],
      "start_to_entry": [
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": []
      ],
      "tool_a_to_failure": [
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": ["successful": false]
      ],
      "tool_a_to_tool_b": [
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": ["successful": true]
      ],
      "tool_b_to_agent_transfer": [
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": []
      ],
      "tool_b_to_conversation": [
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": ["condition": "Conversation condition"]
      ],
      "tool_b_to_end": [
        "source": "tool_node_b",
        "target": "success_end",
        "forward_condition": ["condition": "End condition"]
      ],
      "tool_b_to_phone": [
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": ["expression": ["children": [
              ["name": "force_phone_transfer"],
              [
                "prompt": "Phone condition",
                "value_schema": [
                  "description": "Phone condition",
                  "type": "boolean"
                ]
              ],
              [
                "left": ["name": "mode"],
                "right": ["value": "dev"]
              ]
            ]]]
      ]
    ],
    "nodes": [
      "entry_node": [
        "conversation_config": [],
        "edge_order": ["entry_to_tool_a"],
        "label": "Entry"
      ],
      "failure_node": [
        "conversation_config": [],
        "label": "Failure"
      ],
      "start_node": ["edge_order": ["start_to_entry"]],
      "success_conversation": [
        "conversation_config": [],
        "label": "Success A"
      ],
      "success_end": [],
      "success_phone": ["transfer_destination": ["phone_number": "+1234567890"]],
      "success_transfer": ["agent_id": "success_transfer_agent"],
      "tool_node_a": [
        "edge_order": ["tool_a_to_failure", "tool_a_to_tool_b"],
        "tools": [["tool_id": "tool_a"], ["tool_id": "tool_b"]]
      ],
      "tool_node_b": [
        "edge_order": ["tool_b_to_conversation", "tool_b_to_end", "tool_b_to_phone", "tool_b_to_agent_transfer"],
        "tools": [["tool_id": "tool_a"]]
      ]
    ]
  ],
  "name": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get MCP Server - PHP HTTP Request

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/get

Retrieve MCP server details using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id');

echo $response->getBody();
```

--------------------------------

### Retrieve Voice with PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/voices/get

Uses the Guzzle HTTP client library for PHP to make a GET request to the ElevenLabs API. Requires Guzzle installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/voices/voice_id');

echo $response->getBody();
```

--------------------------------

### Retrieve a Studio Project Chapter

Source: https://elevenlabs.io/docs/api-reference/studio/get-chapter

Use these examples to fetch details of a specific chapter within a studio project by its project and chapter IDs. This operation typically requires authentication and valid IDs.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.chapters.get("project_id", "chapter_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.get(
    project_id="project_id",
    chapter_id="chapter_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /v1/audio-native/{project_id}/settings

Source: https://elevenlabs.io/docs/api-reference/audio-native/get-settings

Get player settings for the specific Audio Native project identified by its ID.

```APIDOC
## GET /v1/audio-native/{project_id}/settings

### Description
Get player settings for the specific project.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/audio-native/{project_id}/settings

### Parameters
#### Path Parameters
- **project_id** (string) - Required - The ID of the Studio project.

#### Header Parameters
- **xi-api-key** (string) - Optional - Your API key for authentication.

### Response
#### Success Response (200)
- **enabled** (boolean) - Whether the project is enabled.
- **snapshot_id** (string, null) - The ID of the latest snapshot of the project.
- **settings** (object, null) - The settings of the project.
    - **title** (string) - The title of the project.
    - **image** (string) - The image of the project.
    - **author** (string) - The author of the project.
    - **small** (boolean) - Whether the project is small.
    - **text_color** (string) - The text color of the project.
    - **background_color** (string) - The background color of the project.
    - **sessionization** (integer) - Specifies for how many minutes to persist the session across page reloads.
    - **audio_path** (string, null) - The path of the audio file.
    - **audio_url** (string, null) - The URL of the audio file.
    - **status** (string) - Current state of the project. (Enum: "processing", "ready")

#### Response Example
```json
{
  "enabled": true,
  "snapshot_id": "some_snapshot_id_string",
  "settings": {
    "title": "My Project Title",
    "image": "https://example.com/project_image.jpg",
    "author": "Project Author",
    "small": false,
    "text_color": "#RRGGBB",
    "background_color": "#RRGGBB",
    "sessionization": 60,
    "audio_path": "/path/to/audio.mp3",
    "audio_url": "https://cdn.example.com/audio.mp3",
    "status": "ready"
  }
}
```
```

--------------------------------

### Connect to Agent with Signed URL - Python

Source: https://elevenlabs.io/docs/eleven-agents/customization/authentication

Initialize a Conversation with a signed URL obtained from the server. The signed URL must be used within 15 minutes of generation to establish the session.

```python
# Client-side code using the Python SDK
from elevenlabs.conversational_ai.conversation import (
    Conversation,
    AudioInterface,
    ClientTools,
    ConversationInitiationData
)
import os
from elevenlabs.client import ElevenLabs
api_key = os.getenv("ELEVENLABS_API_KEY")

elevenlabs = ElevenLabs(api_key=api_key)

conversation = Conversation(
  client=elevenlabs,
  agent_id=os.getenv("AGENT_ID"),
  requires_auth=True,
  audio_interface=AudioInterface(),
  config=ConversationInitiationData()
)

async def start_conversation():
  try:
    signed_url = await get_signed_url()
    conversation = Conversation(
      client=elevenlabs,
      url=signed_url,
    )

    conversation.start_session()
  except Exception as error:
    print(f"Failed to start conversation: {error}")
```

--------------------------------

### List Environment Variables with PHP Guzzle

Source: https://elevenlabs.io/docs/api-reference/environment-variables/list

Use the Guzzle HTTP client in PHP to send a GET request to the environment variables API. Requires Guzzle to be installed and autoloaded.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/environment-variables');

echo $response->getBody();
```

--------------------------------

### Install Python Project Dependencies

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/raspberry-pi-voice-assistant

Install the required Python packages for hotword detection and ElevenLabs conversational AI.

```bash
pip install tflite-runtime
pip install librosa
pip install EfficientWord-Net
pip install elevenlabs
pip install "elevenlabs[pyaudio]"
```

--------------------------------

### Create Studio Project with Python SDK

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

Use the ElevenLabs Python client to create a project from a document source. Requires the elevenlabs package.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.create(
    from_document="example_from_document",
)
```

--------------------------------

### Get a Test Folder by ID

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-folders/get

Use these examples to retrieve the details of a specific test folder by its unique identifier. Replace 'folder_id' with the actual ID of the folder you wish to retrieve.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.folders.get("folder_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.folders.get(
    folder_id="folder_id",
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### POST /studio/projects - Add Studio Project

Source: https://elevenlabs.io/docs/changelog/2026/3/9

Create a new studio project. The endpoint now supports agent_settings field using StudioAgentSettingsModel.

```APIDOC
## POST /studio/projects

### Description
Create a new studio project with optional agent settings.

### Method
POST

### Endpoint
/studio/projects

### Request Body
- **agent_settings** (StudioAgentSettingsModel) - Optional - Agent settings for the studio project
```

--------------------------------

### Get a Batch Call (Go)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get

Illustrates making a GET request to retrieve a batch call using Go's net/http package.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Stream Project Snapshot using Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/stream-snapshot

This example demonstrates how to stream a project snapshot using Go's standard HTTP client. It constructs a POST request to the ElevenLabs API endpoint.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id/stream"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get WebRTC Token for Conversational AI

Source: https://elevenlabs.io/docs/api-reference/conversations/get-webrtc-token

Use these code examples to obtain a WebRTC token for a specified conversational AI agent. This token is essential for establishing a WebRTC connection.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.getWebrtcToken({
        agentId: "agent_id",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.get_webrtc_token(
    agent_id="agent_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=agent_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Execute the dialogue generation script

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue

Run the generated example script to produce and play the dialogue audio output.

```python
python example.py
```

```typescript
npx tsx example.mts
```

--------------------------------

### Create Agent Draft (Ruby)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/create

This Ruby example demonstrates how to construct the request body for creating an agent draft, defining its workflow, and then sending the request to the API.

```Ruby
request.body = "{\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"condition\": \"Tool A condition\"\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {}\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"successful\": false\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"successful\": true\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {}\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"condition\": \"Conversation condition\"\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"condition\": \"End condition\"\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"expression\": {\n            \"children\": [\n              {\n                \"name\": \"force_phone_transfer\"\n              },\n              {\n                \"prompt\": \"Phone condition\",\n                \"value_schema\": {\n                  \"description\": \"Phone condition\",\n                  \"type\": \"boolean\"\n                }\n              },\n              {\n                \"left\": {\n                  \"name\": \"mode\"\n                },\n                \"right\": {\n                  \"value\": \"dev\"\n                }\n              }\n            ]\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"conversation_config\": {}\n        ,\n        \"edge_order\": [\n          \"entry_to_tool_a\"\n        ],\n        \"label\": \"Entry\"\n      },\n      \"failure_node\": {\n        \"conversation_config\": {}\n        ,\n        \"label\": \"Failure\"\n      },\n      \"start_node\": {\n        \"edge_order\": [\n          \"start_to_entry\"\n        ]\n      },\n      \"success_conversation\": {\n        \"conversation_config\": {}\n        ,\n        \"label\": \"Success A\"\n      },\n      \"success_end\": {}\n      ,\n      \"success_phone\": {\n        \"transfer_destination\": {\n          \"phone_number\": \"+1234567890\"\n        }\n      },\n      \"success_transfer\": {\n        \"agent_id\": \"success_transfer_agent\"\n      },\n      \"tool_node_a\": {\n        \"edge_order\": [\n          \"tool_a_to_failure\",\n          \"tool_a_to_tool_b\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          },\n          {\n            \"tool_id\": \"tool_b\"\n          }\n        ]\n      },\n      \"tool_node_b\": {\n        \"edge_order\": [\n          \"tool_b_to_conversation\",\n          \"tool_b_to_end\",\n          \"tool_b_to_phone\",\n          \"tool_b_to_agent_transfer\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          }\n        ]\n      }\n    }\n  },\n  \"name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Delete a Voice Sample

Source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/delete

Use these examples to delete a specific voice sample by its voice_id and sample_id. Ensure you have the necessary authentication and client setup for each language's SDK or HTTP client.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.voices.pvc.samples.delete("voice_id", "sample_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.delete(
    voice_id="voice_id",
    sample_id="sample_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id"

	req, _ := http.NewRequest("DELETE", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id");
var request = new RestRequest(Method.DELETE);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples/sample_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### List auth connections with PHP HTTP client

Source: https://elevenlabs.io/docs/api-reference/workspace/auth-connections/list

Make a GET request to the workspace auth-connections endpoint using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/auth-connections', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### List Chapters in a Studio Project

Source: https://elevenlabs.io/docs/api-reference/studio/get-chapters

Use these examples to retrieve all chapters associated with a given studio project ID. Replace 'project_id' with your actual project identifier.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.chapters.list("project_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.list(
    project_id="project_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get RAG Indexes (Multiple Languages)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-rag-index

These examples demonstrate how to retrieve RAG indexes for a specified documentation ID using the ElevenLabs SDKs or direct HTTP calls in different programming languages.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.getDocumentRagIndexes("documentation_id");
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.get_document_rag_indexes(
    documentation_id="documentation_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body

```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")
  .asString();

```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index');

echo $response->getBody();

```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);

```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()

```

--------------------------------

### Create Knowledge Base Documents and Update Agent via Python API

Source: https://elevenlabs.io/docs/eleven-agents/customization/knowledge-base

This example demonstrates how to create knowledge base documents from text, URL, or file, and then attach them to an agent's configuration using the ElevenLabs Python SDK.

```python
# First create the document from text
knowledge_base_document_text = elevenlabs.conversational_ai.knowledge_base.documents.create_from_text(
    text="The airspeed velocity of an unladen swallow (European) is 24 miles per hour or roughly 11 meters per second.",
    name="Unladen Swallow facts",
)

# Alternatively, you can create a document from a URL
knowledge_base_document_url = elevenlabs.conversational_ai.knowledge_base.documents.create_from_url(
    url="https://en.wikipedia.org/wiki/Unladen_swallow",
    name="Unladen Swallow Wikipedia page",
)

# Or create a document from a file
knowledge_base_document_file = elevenlabs.conversational_ai.knowledge_base.documents.create_from_file(
    file=open("/path/to/unladen-swallow-facts.txt", "rb"),
    name="Unladen Swallow Facts",
)

# Then add the document to the agent
agent = elevenlabs.conversational_ai.agents.update(
    agent_id="agent-id",
    conversation_config={
        "agent": {
            "prompt": {
                "knowledge_base": [
                    {
                        "type": "text",
                        "name": knowledge_base_document_text.name,
                        "id": knowledge_base_document_text.id,
                    },
                    {
                        "type": "url",
                        "name": knowledge_base_document_url.name,
                        "id": knowledge_base_document_url.id,
                    },
                    {
                        "type": "file",
                        "name": knowledge_base_document_file.name,
```

--------------------------------

### Install elevenlabs Python package

Source: https://elevenlabs.io/docs/eleven-agents/libraries/python

Install the core elevenlabs package using pip or poetry. Required for all ElevenLabs SDK functionality.

```shell
pip install elevenlabs
# or
poetry add elevenlabs
```

--------------------------------

### Create Knowledge Base Document from URL - Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-url

Make a POST request to the ElevenLabs knowledge base endpoint using Go's standard library. Requires net/http, strings, and io packages.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/url"

	payload := strings.NewReader("{\n  \"url\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Conversational AI Test Folder by ID

Source: https://elevenlabs.io/docs/api-reference/tests/test-folders/get

Retrieve a specific conversational AI test folder using its unique identifier. Examples are provided for various SDKs and direct HTTP requests.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.tests.folders.get("folder_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.folders.get(
    folder_id="folder_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/folders/folder_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Client Tool and Link to Agent via SDK

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/client-tools

Use the ElevenLabs SDK to programmatically create a client tool and then update an existing agent to reference this new tool.

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

tool = elevenlabs.conversational_ai.tools.create(
    tool_config={
        "type": "client",
        "name": "logMessage",
        "description": "Use this client-side tool to log a message to the user's client.",
        "expects_response": False,
        "parameters": [
            {
                "id": "message",
                "type": "string",
                "value_type": "llm_prompt",
                "description": "The message to log in the console.",
                "required": True,
            }
        ],
    }
)

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    conversation_config={
        "agent": {"prompt": {"tool_ids": [tool.id]}},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

const tool = await elevenlabs.conversationalAi.tools.create({
  toolConfig: {
    type: "client",
    name: "logMessage",
    description: "Use this client-side tool to log a message to the user's client.",
    expectsResponse: false,
    parameters: [
      {
        id: "message",
        type: "string",

```

--------------------------------

### POST /v1/studio/projects/{project_id}/convert

Source: https://elevenlabs.io/docs/api-reference/studio/convert-project

Starts conversion of a Studio project and all of its chapters.

```APIDOC
## POST /v1/studio/projects/{project_id}/convert

### Description
Starts conversion of a Studio project and all of its chapters.

### Method
POST

### Endpoint
/v1/studio/projects/{project_id}/convert

### Parameters
#### Path Parameters
- **project_id** (string) - Required - The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

#### Header Parameters
- **xi-api-key** (string) - Optional - API key for authentication.

### Response
#### Success Response (200)
- **status** (string) - The status of the studio project conversion request. If the request was successful, the status will be 'ok'. Otherwise an error message with status 500 will be returned.

#### Response Example
{
  "status": "ok"
}

#### Error Response (422)
- **detail** (array) - Validation Error details.

#### Error Response Example (422)
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

--------------------------------

### List conversations with Go HTTP client

Source: https://elevenlabs.io/docs/api-reference/conversations/list

Make a GET request to the conversations endpoint using Go's standard net/http package. Requires manual request setup and response handling.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/conversations"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Search Workspace Groups with PHP HTTP Client

Source: https://elevenlabs.io/docs/api-reference/workspace/groups/search

Make a GET request to the workspace groups search endpoint using the Guzzle HTTP client for PHP. Requires Guzzle to be installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/workspace/groups/search?name=name');

echo $response->getBody();
```

--------------------------------

### Create Studio Project with Multipart Form Data - C#

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

C# example using RestSharp to POST a multipart form-data request to create a studio project. Requires RestSharp library for HTTP client functionality.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects");
var request = new RestRequest(Method.POST);
```

--------------------------------

### Start Speech to Text Transcription with Webhook

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/webhooks

This snippet demonstrates how to initiate an asynchronous speech-to-text transcription using the ElevenLabs API, enabling webhook notifications for status updates. It shows examples in both Python and TypeScript.

```python
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def transcribe_with_webhook(audio_file):
  try:
    result = elevenlabs.speech_to_text.convert(
      file=audio_file,
      model_id="scribe_v2",
      webhook=True,
    )
    print(f"Transcription started: {result.request_id}")
    return result
  except Exception as e:
    print(f"Error starting transcription: {e}")
    raise e
```

```typescript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

async function transcribeWithWebhook(audioFile) {
  try {
    const result = await elevenlabs.speechToText.convert({
      file: audioFile,
      modelId: 'scribe_v2',
      webhook: true,
    });

    console.log('Transcription started:', result.requestId);
    return result;
  } catch (error) {
    console.error('Error starting transcription:', error);
    throw error;
  }
}
```

--------------------------------

### Create Knowledge Base Folder with Java (Unirest)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder

Use the Unirest library in Java to make a POST request for creating a folder. Include the Content-Type header and JSON body.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/folder")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"string\"\n}")
  .asString();
```

--------------------------------

### Get Knowledge Base Document Content

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-content

These examples demonstrate how to retrieve the content of a specific document from an ElevenLabs Conversational AI knowledge base. They cover both official SDKs and direct HTTP client implementations.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.getContent("documentation_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.get_content(
    documentation_id="documentation_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Knowledge Base Document Chunk

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-chunk

These examples demonstrate how to retrieve a specific chunk from a knowledge base document using various SDKs and HTTP clients. Replace 'documentation_id' and 'chunk_id' with actual values.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.chunk.get("documentation_id", "chunk_id", {});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.chunk.get(
    documentation_id="documentation_id",
    chunk_id="chunk_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/chunk/chunk_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/chunk/chunk_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/chunk/chunk_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/chunk/chunk_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/chunk/chunk_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/chunk/chunk_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create ElevenLabs Agents with Templates

Source: https://elevenlabs.io/docs/eleven-agents/operate/cli

Create new agents using pre-built templates, optionally specifying a template type or skipping the upload. This includes general syntax and specific examples.

```bash
elevenlabs agents add "My Assistant" --template assistant
```

```bash
elevenlabs agents add "Agent Name" [options]
```

```bash
elevenlabs agents add "Customer Support Bot" --template customer-service
```

--------------------------------

### Update Studio Project Content via HTTP POST in Go

Source: https://elevenlabs.io/docs/api-reference/studio/update-content

This example illustrates making a direct HTTP POST request in Go to update Studio project content, using multipart/form-data.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/content"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Knowledge Base Folder with Swift

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder

Make an HTTP POST request in Swift to create a new folder. This example uses URLSession for network communication.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/folder")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Test Folder in Java

Source: https://elevenlabs.io/docs/api-reference/tests/test-folders/create

This example uses Unirest to make an HTTP POST request to create a new test folder. The folder will be named 'string'.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agent-testing/folders")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"string\"\n}")
  .asString();
```

--------------------------------

### Install ElevenLabs Packages Upgrade Skill

Source: https://elevenlabs.io/docs/changelog/2026/4/1

Use this command to install the ElevenLabs Skill, which is designed to help agents upgrade to the new SDK versions.

```bash
npx skills add elevenlabs/packages
```

--------------------------------

### Install React Native SDK and Dependencies

Source: https://elevenlabs.io/docs/eleven-agents/libraries/react-native

Install the core ElevenLabs React Native SDK along with its LiveKit dependencies using npm.

```shell
npm install @elevenlabs/react-native @livekit/react-native @livekit/react-native-webrtc livekit-client
```

--------------------------------

### Create Tool Configuration in Swift

Source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create

This snippet demonstrates how to create a tool configuration using `URLSession` in Swift.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["tool_name": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Translate Dubbing Resource (Multi-language)

Source: https://elevenlabs.io/docs/api-reference/dubbing/resources/translate-segment

These examples demonstrate how to translate a dubbing resource by specifying the dubbing ID, segments to translate, and target languages. Ensure you have the necessary SDKs or HTTP client libraries installed for your chosen language.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.dubbing.resource.translate("dubbing_id", {
        segments: [
            "string",
        ],
        languages: [
            "string",
        ],
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.resource.translate(
    dubbing_id="dubbing_id",
    segments=[
        "string"
    ],
    languages=[
        "string"
    ],
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate"

	payload := strings.NewReader("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")
  .header("Content-Type", "application/json")
  .body("{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate', [
  'body' => '{
  "segments": [
    "string"
  ],
  "languages": [
    "string"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"segments\": [\n    \"string\"\n  ],\n  \"languages\": [\n    \"string\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "segments": ["string"],
  "languages": ["string"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/resource/dubbing_id/translate")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Comprehensive SwiftUI Integration with ElevenLabs SDK

Source: https://elevenlabs.io/docs/eleven-agents/libraries/swift

This example provides a full SwiftUI application structure, including views and a view model, to demonstrate a conversational interface using the ElevenLabs SDK. It covers connection management, message display, and user interaction controls.

```swift
import SwiftUI
import ElevenLabs
import Combine

struct ConversationView: View {
    @StateObject private var viewModel = ConversationViewModel()

    var body: some View {
        VStack(spacing: 20) {
            // Connection status
            Text(viewModel.connectionStatus)
                .font(.headline)
                .foregroundColor(viewModel.isConnected ? .green : .red)

            // Chat messages
            ScrollView {
                LazyVStack(alignment: .leading, spacing: 8) {
                    ForEach(viewModel.messages, id: \.id) { message in
                        MessageBubble(message: message)
                    }
                }
            }
            .frame(maxHeight: 400)

            // Controls
            HStack(spacing: 16) {
                Button(viewModel.isConnected ? "End" : "Start") {
                    Task {
                        if viewModel.isConnected {
                            await viewModel.endConversation()
                        } else {
                            await viewModel.startConversation()
                        }
                    }
                }
                .buttonStyle(.borderedProminent)

                Button(viewModel.isMuted ? "Unmute" : "Mute") {
                    Task { await viewModel.toggleMute() }
                }
                .buttonStyle(.bordered)
                .disabled(!viewModel.isConnected)

                Button("Send Message") {
                    Task { await viewModel.sendTestMessage() }
                }
                .buttonStyle(.bordered)
                .disabled(!viewModel.isConnected)
            }

            // Agent state indicator
            if viewModel.isConnected {
                HStack {
                    Circle()
                        .fill(viewModel.agentState == .speaking ? .blue : .gray)
                        .frame(width: 10, height: 10)
                    Text(viewModel.agentState == .speaking ? "Agent speaking" : "Agent listening")
                        .font(.caption)
                }
            }
        }
        .padding()
    }
}

struct MessageBubble: View {
    let message: Message

    var body: some View {
        HStack {
            if message.role == .user { Spacer() }

            VStack(alignment: .leading) {
                Text(message.role == .user ? "You" : "Agent")
                    .font(.caption)
                    .foregroundColor(.secondary)
                Text(message.content)
                    .padding()
                    .background(message.role == .user ? Color.blue : Color.gray.opacity(0.3))
                    .foregroundColor(message.role == .user ? .white : .primary)
                    .cornerRadius(12)
            }

            if message.role == .agent { Spacer() }
        }
    }
}

@MainActor
class ConversationViewModel: ObservableObject {
    @Published var messages: [Message] = []
    @Published var isConnected = false
    @Published var isMuted = false
    @Published var agentState: AgentState = .listening
    @Published var connectionStatus = "Disconnected"

    private var conversation: Conversation?
    private var cancellables = Set<AnyCancellable>()

    func startConversation() async {
        do {
            conversation = try await ElevenLabs.startConversation(
                agentId: "your-agent-id",
                config: ConversationConfig()
            )
            setupObservers()
        } catch {
            print("Failed to start conversation: \(error)")
            connectionStatus = "Failed to connect"
        }
    }

    func endConversation() async {
        await conversation?.endConversation()
        conversation = nil
        cancellables.removeAll()
    }

    func toggleMute() async {
        try? await conversation?.toggleMute()
    }

    func sendTestMessage() async {
        try? await conversation?.sendMessage("Hello from the app!")
    }

    private func setupObservers() {
        guard let conversation else { return }

        conversation.$messages
            .assign(to: &$_messages)

        conversation.$state
            .map { state in
                switch state {
                case .idle: return "Disconnected"
                case .connecting: return "Connecting..."
                case .active: return "Connected"
                case .ended: return "Ended"
                case .error: return "Error"
                }
            }
            .assign(to: &$_connectionStatus)

        conversation.$state
            .map { $0.isActive }
            .assign(to: &$_isConnected)

        conversation.$isMuted
            .assign(to: &$_isMuted)

        conversation.$agentState
            .assign(to: &$_agentState)
    }
}
```

--------------------------------

### Get a Chapter Snapshot from ElevenLabs Studio Project

Source: https://elevenlabs.io/docs/api-reference/studio/get-chapter-snapshot

This example demonstrates how to retrieve a specific chapter snapshot using various programming languages and their respective HTTP clients or SDKs. Replace 'project_id', 'chapter_id', and 'chapter_snapshot_id' with actual values.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.chapters.snapshots.get("project_id", "chapter_id", "chapter_snapshot_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.snapshots.get(
    project_id="project_id",
    chapter_id="chapter_id",
    chapter_snapshot_id="chapter_snapshot_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots/chapter_snapshot_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Deploy Conversational AI Agent with Percentage Traffic Strategy (Multi-language)

Source: https://elevenlabs.io/docs/api-reference/agents/deployments/create

These examples demonstrate how to deploy a conversational AI agent, specifying a branch ID and a percentage-based traffic distribution for the deployment strategy. The examples cover both SDK usage and direct API calls.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.deployments.create("agent_id", {
        deploymentRequest: {
            requests: [
                {
                    branchId: "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                    deploymentStrategy: {
                        trafficPercentage: 0.5,
                        type: "percentage",
                    },
                },
            ],
        },
    });
}
main();
```

```python
from elevenlabs import ElevenLabs, AgentDeploymentRequest, AgentDeploymentRequestItem, AgentDeploymentPercentageStrategy

client = ElevenLabs()

client.conversational_ai.agents.deployments.create(
    agent_id="agent_id",
    deployment_request=AgentDeploymentRequest(
        requests=[
            AgentDeploymentRequestItem(
                branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                deployment_strategy=AgentDeploymentPercentageStrategy(
                    traffic_percentage=0.5,
                    type="percentage",
                ),
            )
        ],
    ),
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments"

	payload := strings.NewReader("{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments")
  .header("Content-Type", "application/json")
  .body("{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments', [
  'body' => '{
  "deployment_request": {
    "requests": [
      {
        "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        "deployment_strategy": {
          "traffic_percentage": 0.5,
          "type": "percentage"
        }
      }
    ]
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"deployment_request\": {\n    \"requests\": [\n      {\n        \"branch_id\": \"agtbrch_8901k4t9z5defmb8vh3e9361y7nj\",\n        \"deployment_strategy\": {\n          \"traffic_percentage\": 0.5,\n          \"type\": \"percentage\"\n        }\n      }\n    ]\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["deployment_request": ["requests": [
      [
        "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        "deployment_strategy": [
          "traffic_percentage": 0.5,
          "type": "percentage"
        ]
      ]
    ]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
```

--------------------------------

### POST /v1/studio/projects

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

Creates a new Studio project, which can be initialized as blank, from a document, or from a URL.

```APIDOC
## POST /v1/studio/projects

### Description
Creates a new Studio project, it can be either initialized as blank, from a document or from a URL.

### Method
POST

### Endpoint
https://api.elevenlabs.io/v1/studio/projects
```

--------------------------------

### Get Signed URL for Conversational AI Agent

Source: https://elevenlabs.io/docs/api-reference/conversations/get-signed-url

These examples demonstrate how to retrieve a signed URL for an ElevenLabs conversational AI agent using various SDKs and direct HTTP requests. Replace 'agent_id' with your actual agent identifier.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.conversations.getSignedUrl({
        agentId: "agent_id",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.get_signed_url(
    agent_id="agent_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=agent_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Serve Supabase Function Locally

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming-and-caching-with-supabase

Run this command to start your Supabase function locally and observe its logs for debugging and development.

```bash
supabase functions serve
```

--------------------------------

### Synchronize Text Display with Audio Alignment in Swift

Source: https://elevenlabs.io/docs/eleven-agents/libraries/swift

Access character-level timing data to synchronize text display with agent speech. Use either the onAudioAlignment callback or observe latestAudioAlignment publisher to get start times and durations for each character.

```swift
// Using the callback
let config = ConversationConfig(
    onAudioAlignment: { alignment in
        // Character-level timing data
        for (index, char) in alignment.chars.enumerated() {
            let startMs = alignment.charStartTimesMs[index]
            let durationMs = alignment.charDurationsMs[index]
            print("'\(char)' at \(startMs)ms for \(durationMs)ms")
        }
    }
)

// Or observe the published property
conversation.$latestAudioAlignment
    .compactMap { $0 }
    .sink { alignment in
        // Handle alignment updates
    }
    .store(in: &cancellables)
```

--------------------------------

### List MCP Server Tools in Go

Source: https://elevenlabs.io/docs/api-reference/mcp/list-tools

This snippet demonstrates how to list tools for a given MCP server ID using a standard HTTP GET request in Go. It constructs the URL and sends the request.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Usage By Product Over Time (Java)

Source: https://elevenlabs.io/docs/api-reference/workspace/usage/get-usage-by-product-over-time

Execute an HTTP POST request using Unirest in Java to get product usage analytics.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/workspace/analytics/query/usage-by-product-over-time")
  .header("Content-Type", "application/json")
  .body("{\n  \"start_time\": 1680307200000,\n  \"end_time\": 1682899200000\n}")
  .asString();
```

--------------------------------

### GET /v1/speech-to-text/evaluation/analytics

Source: https://elevenlabs.io/docs/changelog/2026/3/23

Get evaluation analytics.

```APIDOC
## GET /v1/speech-to-text/evaluation/analytics

### Description
Get evaluation analytics.

### Method
GET

### Endpoint
/v1/speech-to-text/evaluation/analytics
```

--------------------------------

### Create Dubbing with Python SDK

Source: https://elevenlabs.io/docs/api-reference/dubbing/create

Initializes the ElevenLabs client and calls the `dubbing.create` method with example file parameters.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.create(
    file="example_file",
    csv_file="example_csv_file",
    foreground_audio_file="example_foreground_audio_file",
    background_audio_file="example_background_audio_file",
)
```

--------------------------------

### Install AWS SDKs for S3 Integration

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming

Install the necessary AWS SDK packages for Python (boto3) and TypeScript (@aws-sdk/client-s3, @aws-sdk/s3-request-presigner) to interact with AWS S3.

```bash Python
pip install boto3
```

```bash TypeScript
npm install @aws-sdk/client-s3
npm install @aws-sdk/s3-request-presigner
```

--------------------------------

### GET /v1/user

Source: https://elevenlabs.io/docs/api-reference/user/get

Gets information about the user.

```APIDOC
## GET /v1/user

### Description
Gets information about the user.

### Method
GET

### Endpoint
/v1/user

### Parameters
#### Header Parameters
- **xi-api-key** (string) - Optional

### Response
#### Success Response (200)
Returns a UserResponseModel object.

#### Error Response (422)
Returns a HTTPValidationError object.
```

--------------------------------

### List dubs with HTTP GET request - Java

Source: https://elevenlabs.io/docs/api-reference/dubbing/list

Make a raw HTTP GET request using the Unirest library.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing")
  .asString();
```

--------------------------------

### GET /v1/speech-to-text/evaluation/human-agents/{agent_id}

Source: https://elevenlabs.io/docs/changelog/2026/3/23

Get a human agent.

```APIDOC
## GET /v1/speech-to-text/evaluation/human-agents/{agent_id}

### Description
Get a human agent.

### Method
GET

### Endpoint
/v1/speech-to-text/evaluation/human-agents/{agent_id}

### Parameters
#### Path Parameters
- **agent_id** (string) - Required
```

--------------------------------

### GET /v1/speech-to-text/evaluation/evaluations/{evaluation_id}

Source: https://elevenlabs.io/docs/changelog/2026/3/23

Get a specific evaluation.

```APIDOC
## GET /v1/speech-to-text/evaluation/evaluations/{evaluation_id}

### Description
Get a specific evaluation.

### Method
GET

### Endpoint
/v1/speech-to-text/evaluation/evaluations/{evaluation_id}

### Parameters
#### Path Parameters
- **evaluation_id** (string) - Required
```

--------------------------------

### Get User Subscription (Go)

Source: https://elevenlabs.io/docs/api-reference/user/subscription/get

Make a direct HTTP GET request in Go to fetch the user's subscription information.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/user/subscription"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Agent Draft with Workflow - Java

Source: https://elevenlabs.io/docs/api-reference/agents/drafts/create

Java SDK example using Unirest to POST a workflow configuration to create an agent draft. Includes workflow edges with conditional routing and tool nodes.

```java
.body("{\n  \"workflow\": {\n    \"edges\": {\n      \"entry_to_tool_a\": {\n        \"source\": \"entry_node\",\n        \"target\": \"tool_node_a\",\n        \"forward_condition\": {\n          \"condition\": \"Tool A condition\"\n        }\n      },\n      \"start_to_entry\": {\n        \"source\": \"start_node\",\n        \"target\": \"entry_node\",\n        \"forward_condition\": {}\n      },\n      \"tool_a_to_failure\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"failure_node\",\n        \"forward_condition\": {\n          \"successful\": false\n        }\n      },\n      \"tool_a_to_tool_b\": {\n        \"source\": \"tool_node_a\",\n        \"target\": \"tool_node_b\",\n        \"forward_condition\": {\n          \"successful\": true\n        }\n      },\n      \"tool_b_to_agent_transfer\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_transfer\",\n        \"forward_condition\": {}\n      },\n      \"tool_b_to_conversation\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_conversation\",\n        \"forward_condition\": {\n          \"condition\": \"Conversation condition\"\n        }\n      },\n      \"tool_b_to_end\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_end\",\n        \"forward_condition\": {\n          \"condition\": \"End condition\"\n        }\n      },\n      \"tool_b_to_phone\": {\n        \"source\": \"tool_node_b\",\n        \"target\": \"success_phone\",\n        \"forward_condition\": {\n          \"expression\": {\n            \"children\": [\n              {\n                \"name\": \"force_phone_transfer\"\n              },\n              {\n                \"prompt\": \"Phone condition\",\n                \"value_schema\": {\n                  \"description\": \"Phone condition\",\n                  \"type\": \"boolean\"\n                }\n              },\n              {\n                \"left\": {\n                  \"name\": \"mode\"\n                },\n                \"right\": {\n                  \"value\": \"dev\"\n                }\n              }\n            ]\n          }\n        }\n      }\n    },\n    \"nodes\": {\n      \"entry_node\": {\n        \"conversation_config\": {},\n        \"edge_order\": [\n          \"entry_to_tool_a\"\n        ],\n        \"label\": \"Entry\"\n      },\n      \"failure_node\": {\n        \"conversation_config\": {},\n        \"label\": \"Failure\"\n      },\n      \"start_node\": {\n        \"edge_order\": [\n          \"start_to_entry\"\n        ]\n      },\n      \"success_conversation\": {\n        \"conversation_config\": {},\n        \"label\": \"Success A\"\n      },\n      \"success_end\": {},\n      \"success_phone\": {\n        \"transfer_destination\": {\n          \"phone_number\": \"+1234567890\"\n        }\n      },\n      \"success_transfer\": {\n        \"agent_id\": \"success_transfer_agent\"\n      },\n      \"tool_node_a\": {\n        \"edge_order\": [\n          \"tool_a_to_failure\",\n          \"tool_a_to_tool_b\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          },\n          {\n            \"tool_id\": \"tool_b\"\n          }\n        ]\n      },\n      \"tool_node_b\": {\n        \"edge_order\": [\n          \"tool_b_to_conversation\",\n          \"tool_b_to_end\",\n          \"tool_b_to_phone\",\n          \"tool_b_to_agent_transfer\"\n        ],\n        \"tools\": [\n          {\n            \"tool_id\": \"tool_a\"\n          }\n        ]\n      }\n    }\n  },\n  \"name\": \"string\"\n}")\n  .asString();
```

--------------------------------

### Get Dependent Agents in Java with Unirest

Source: https://elevenlabs.io/docs/api-reference/tools/get-dependent-agents

Use the Unirest library in Java to send a GET request and get dependent agents for a tool ID.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents")
  .asString();
```

--------------------------------

### Get Audio Native Project Settings with Go (HTTP Request)

Source: https://elevenlabs.io/docs/api-reference/audio-native/get-settings

Make a GET request to the ElevenLabs API endpoint for audio native project settings using the standard net/http package.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/audio-native/project_id/settings"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Batch Call Details (Swift)

Source: https://elevenlabs.io/docs/api-reference/batch-calling/get

Perform an HTTP GET request in Swift using URLSession to get batch calling job details.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()

```

--------------------------------

### Run Conversation Agent Demo

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket

Executes the conversation agent demo function. Call this to initialize the WebSocket connection and start the agent.

```JavaScript
conversationAgentDemo();
```

--------------------------------

### GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}

Source: https://elevenlabs.io/docs/changelog/2026/3/23

Get a specific evaluation criterion.

```APIDOC
## GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}

### Description
Get a specific evaluation criterion.

### Method
GET

### Endpoint
/v1/speech-to-text/evaluation/eval-criteria/{criterion_id}

### Parameters
#### Path Parameters
- **criterion_id** (string) - Required
```

--------------------------------

### Get agent branch

Source: https://elevenlabs.io/docs/changelog/2026/1/26

Get a specific branch for an agent.

```APIDOC
## GET /v1/convai/agents/{agent_id}/branches/{branch_id}

### Description
Get a specific branch for an agent.

### Method
GET

### Endpoint
/v1/convai/agents/{agent_id}/branches/{branch_id}

### Parameters
#### Path Parameters
- **agent_id** (string) - Required - The ID of the agent.
- **branch_id** (string) - Required - The ID of the branch.
```

--------------------------------

### Create Knowledge Base Folder with Java

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/create-folder

This snippet demonstrates how to create a new folder in an ElevenLabs knowledge base using the Unirest HTTP client for Java.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/knowledge-base/folder")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Project Documentation\"\n}")
  .asString();
```

--------------------------------

### Get Agent Branch (Go HTTP Request)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/get

Demonstrates how to make a GET request to retrieve an agent branch using Go's standard net/http library.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### GET /v1/convai/secrets/{secret_id}

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

Get a workspace secret by ID.

```APIDOC
## GET /v1/convai/secrets/{secret_id}

### Description
Get a workspace secret by ID.

### Method
GET

### Endpoint
/v1/convai/secrets/{secret_id}

### Parameters
#### Path Parameters
- **secret_id** (string) - Required - The ID of the secret to retrieve.

#### Header Parameters
- **xi-api-key** (string) - Optional - Your API key for authentication.

### Response
#### Success Response (200)
- **Response Body** (object) - A `ConvAIWorkspaceStoredSecretConfig` object representing the requested secret.

#### Error Response (422)
- **Response Body** (object) - A `HTTPValidationError` object indicating validation issues.
```

--------------------------------

### Create Knowledge Base Folder with Python SDK

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder

Utilize the ElevenLabs Python SDK to create a new folder. Make sure the SDK is installed and authenticated.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.create_folder(
    name="string",
)
```

--------------------------------

### GET /v1/workspace/resources/{resource_id}

Source: https://elevenlabs.io/docs/api-reference/workspace/resources/get

Gets the metadata of a resource by ID.

```APIDOC
## GET /v1/workspace/resources/{resource_id}

### Description
Gets the metadata of a resource by ID.

### Method
GET

### Endpoint
/v1/workspace/resources/{resource_id}

### Parameters
#### Path Parameters
- **resource_id** (string) - Required - The unique identifier of the resource.
```

--------------------------------

### Get Audio Native Project Settings with Python SDK

Source: https://elevenlabs.io/docs/api-reference/audio-native/get-settings

Initialize the ElevenLabs client and call the audio_native.get_settings method with the project ID.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_native.get_settings(
    project_id="project_id",
)
```

--------------------------------

### Add Client Tool using ElevenLabs CLI

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/client-tools

Register a new client tool with the ElevenLabs platform using its configuration file via the CLI.

```bash
elevenlabs tools add "logMessage" --type "client" --config-path ./tool_configs/log_message.json
```

--------------------------------

### GET /v1/user/subscription

Source: https://elevenlabs.io/docs/api-reference/user/subscription/get

Gets extended information about the users subscription.

```APIDOC
## GET /v1/user/subscription

### Description
Gets extended information about the users subscription

### Method
GET

### Endpoint
/v1/user/subscription

### Parameters
#### Header Parameters
- **xi-api-key** (string) - Optional -

### Response
#### Success Response (200)
- **ExtendedSubscriptionResponseModel** (object) - Detailed information about the user's subscription.
```

--------------------------------

### Add client tool for direct integration

Source: https://elevenlabs.io/docs/eleven-agents/operate/cli

Register a client-side tool for direct integration without HTTP overhead.

```bash
elevenlabs tools add "Client Function" --type "client" --config-path ./config.json
```

--------------------------------

### GET /v1/convai/test-invocations/{test_invocation_id}

Source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get

Gets a test invocation by ID.

```APIDOC
## GET /v1/convai/test-invocations/{test_invocation_id}

### Description
Gets a test invocation by ID.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/convai/test-invocations/{test_invocation_id}

### Parameters
#### Path Parameters
- **test_invocation_id** (string) - Required - The unique identifier of the test invocation to retrieve.
```

--------------------------------

### GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}/analytics

Source: https://elevenlabs.io/docs/changelog/2026/3/23

Get analytics for a specific criterion.

```APIDOC
## GET /v1/speech-to-text/evaluation/eval-criteria/{criterion_id}/analytics

### Description
Get analytics for a specific criterion.

### Method
GET

### Endpoint
/v1/speech-to-text/evaluation/eval-criteria/{criterion_id}/analytics

### Parameters
#### Path Parameters
- **criterion_id** (string) - Required
```

--------------------------------

### Execute TypeScript Example Script

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries

Runs the TypeScript script to demonstrate the effect of the pronunciation dictionary.

```typescript
npx tsx example.mts
```

--------------------------------

### GET /v1/convai/agent-testing/{test_id}

Source: https://elevenlabs.io/docs/api-reference/tests/get

Gets an agent response test by ID.

```APIDOC
## GET /v1/convai/agent-testing/{test_id}

### Description
Gets an agent response test by ID.

### Method
GET

### Endpoint
/v1/convai/agent-testing/{test_id}

### Parameters
#### Path Parameters
- **test_id** (string) - Required - The ID of the agent response test.
```

--------------------------------

### Configure Agent and TTS Overrides in Swift

Source: https://elevenlabs.io/docs/eleven-agents/customization/personalization/overrides

This Swift example shows how to construct `AgentPrompt`, `AgentConfig`, `TTSConfig`, and `ConversationConfig` objects to apply various overrides during session initiation.

```swift
import ElevenLabsSDK

let promptOverride = ElevenLabsSDK.AgentPrompt(
    prompt: "The customer's bank account balance is \(customer_balance). They are based in \(customer_location).", // Optional: override the system prompt.
    llm: "gpt-4o" // Optional: override the LLM model.
)
let agentConfig = ElevenLabsSDK.AgentConfig(
    prompt: promptOverride, // Optional: override the system prompt.
    firstMessage: "Hi \(customer_name), how can I help you today?", // Optional: override the first message.
    language: .en // Optional: override the language.
)
let ttsConfig = ElevenLabsSDK.TTSConfig(
    voiceId: "custom_voice_id", // Optional: override the voice.
    stability: 0.7, // Optional: override stability (0.0 to 1.0).
    speed: 1.1, // Optional: override speed (0.7 to 1.2).
    similarityBoost: 0.9 // Optional: override similarity boost (0.0 to 1.0).
)
let conversationConfig = ElevenLabsSDK.ConversationConfig(
    textOnly: true // Optional: enable text-only mode (no audio).
)
let overrides = ElevenLabsSDK.ConversationConfigOverride(
    agent: agentConfig, // Optional: override agent settings.
    tts: ttsConfig, // Optional: override TTS settings.
    conversation: conversationConfig // Optional: override conversation settings.
)

let config = ElevenLabsSDK.SessionConfig(
    agentId: "",
    overrides: overrides
)

let conversation = try await ElevenLabsSDK.Conversation.startSession(
  config: config,
  callbacks: callbacks
)
```

--------------------------------

### Create MCP Server (TypeScript SDK)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/create

Use the ElevenLabs TypeScript SDK to create a new MCP server. This example demonstrates how to initialize the client and call the 'create' method with server configuration.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.create({
        config: {
            url: "string",
            name: "string",
        },
    });
}
main();
```

--------------------------------

### GET /v1/models

Source: https://elevenlabs.io/docs/api-reference/models/list

Gets a list of available models from the ElevenLabs API.

```APIDOC
## GET /v1/models

### Description
Gets a list of available models.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/models
```

--------------------------------

### Create and Configure Client Tool via API

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/client-tools

Create a client tool with parameters using the ElevenLabs API, then update an agent to use it. The tool definition includes parameter specifications with type and description.

```javascript
const tool = await elevenlabs.conversationalAi.agents.createTool("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  name: "logMessage",
  description: "Logs a message to the console",
  parameters: [
    {
      name: "message",
      valueType: "llm_prompt",
      description: "The message to log in the console.",
      required: true,
    },
  ],
});

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    agent: { prompt: { toolIds: [tool.id] } },
  },
});
```

--------------------------------

### GET /v1/convai/knowledge-base

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/list

Get a list of available knowledge base documents.

```APIDOC
## GET /v1/convai/knowledge-base

### Description
Get a list of available knowledge base documents.

### Method
GET

### Endpoint
/v1/convai/knowledge-base

### Parameters
#### Query Parameters
- **page_size** (integer) - Optional - How many documents to return at maximum. Can not exceed 100, defaults to 30.
- **search** (string/null) - Optional - If specified, the endpoint returns only such knowledge base documents whose names start with this string.
- **show_only_owned_documents** (boolean) - Optional - If set to true, the endpoint will return only documents owned by you (and not shared from somebody else). Deprecated: use created_by_user_id instead.
- **created_by_user_id** (string/null) - Optional - Filter documents by creator user ID. When set, only documents created by this user are returned. Takes precedence over show_only_owned_documents. Use '@me' to refer to the authenticated user.
- **types** (array/null) - Optional - If present, the endpoint will return only documents of the given types. Allowed values: file, url, text, folder.
- **parent_folder_id** (string/null) - Optional - If set, the endpoint will return only documents that are direct children of the given folder.
- **ancestor_folder_id** (string/null) - Optional - If set, the endpoint will return only documents that are descendants of the given folder.
- **folders_first** (boolean) - Optional - Whether folders should be returned first in the list of documents.
- **sort_direction** (string) - Optional - The direction to sort the results. Allowed values: asc, desc.
- **sort_by** (string/null) - Optional - The field to sort the results by. Allowed values: name, created_at, updated_at, size.
- **cursor** (string/null) - Optional - Used for fetching next page. Cursor is returned in the response.

### Response
#### Success Response (200)
- **schema** (GetKnowledgeBaseListResponseModel) - Successful Response
```

--------------------------------

### Get Agent Summaries (Go)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-summaries

Make a direct HTTP GET request in Go to retrieve summaries for specified conversational AI agents.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22J3Pbu5gP6NNKBscdCdwB%22%2C%22K4Qcu6hQ7OOLCtdeDeXC%22%5D"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### GET /v1/convai/knowledge-base

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/list

Get a list of available knowledge base documents.

```APIDOC
## GET /v1/convai/knowledge-base

### Description
Get a list of available knowledge base documents

### Method
GET

### Endpoint
/v1/convai/knowledge-base
```

--------------------------------

### Retrieve RAG Index Overview

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/rag-index-overview

These examples demonstrate how to fetch an overview of the RAG index using different SDKs and HTTP clients. This endpoint provides information about the current state and contents of the RAG index.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.ragIndexOverview();
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.rag_index_overview()
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/rag-index")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /v1/convai/tags/{tag_id}

Source: https://elevenlabs.io/docs/api-reference/conversations/tags/get

Get a conversation tag by its unique ID.

```APIDOC
## GET /v1/convai/tags/{tag_id}

### Description
Get a conversation tag by ID.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/convai/tags/{tag_id}

### Parameters
#### Path Parameters
- **tag_id** (string) - Required - The ID of the conversation tag.

### Response
#### Success Response (200)
- **tag_id** (string) - The ID of the conversation tag.
- **workspace_id** (string) - The ID of the workspace the tag belongs to.
- **owner_user_id** (string) - The ID of the user who owns the tag.
- **title** (string) - The title of the tag.
- **description** (string, null) - The description of the tag.
- **created_at_unix_secs** (integer) - The Unix timestamp (in seconds) when the tag was created.

#### Response Example
```json
{
  "tag_id": "string",
  "workspace_id": "string",
  "owner_user_id": "string",
  "title": "string",
  "description": "string",
  "created_at_unix_secs": 0
}
```
```

--------------------------------

### Create Podcast with Conversation Mode from URL

Source: https://elevenlabs.io/docs/api-reference/studio/create-podcast

This example demonstrates how to create a new podcast using the ElevenLabs API, specifying a conversation mode with host and guest voices, and providing a URL as the source for the podcast content. This operation typically involves an API call to the /v1/studio/podcasts endpoint.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.createPodcast({
        modelId: "eleven_multilingual_v2",
        mode: {
            type: "conversation",
            conversation: {
                hostVoiceId: "6lCwbsX1yVjD49QmpkTR",
                guestVoiceId: "bYTqZQo3Jz7LQtmGTgwi",
            },
        },
        source: {
            type: "url",
            url: "https://en.wikipedia.org/wiki/Cognitive_science",
        },
    });
}
main();
```

```python
from elevenlabs import ElevenLabs, PodcastConversationModeData, PodcastUrlSource
from elevenlabs.studio import BodyCreatePodcastV1StudioPodcastsPostMode_Conversation

client = ElevenLabs()

client.studio.create_podcast(
    model_id="eleven_multilingual_v2",
    mode=BodyCreatePodcastV1StudioPodcastsPostMode_Conversation(
        conversation=PodcastConversationModeData(
            host_voice_id="6lCwbsX1yVjD49QmpkTR",
            guest_voice_id="bYTqZQo3Jz7LQtmGTgwi",
        ),
    ),
    source=PodcastUrlSource(
        type="url",
        url="https://en.wikipedia.org/wiki/Cognitive_science",
    ),
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/podcasts"

	payload := strings.NewReader("{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"conversation\",\n    \"conversation\": {\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\",\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    }\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/podcasts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"conversation\",\n    \"conversation\": {\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\",\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    }\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/podcasts")
  .header("Content-Type", "application/json")
  .body("{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"conversation\",\n    \"conversation\": {\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\",\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    }\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/podcasts', [
  'body' => '{
  "model_id": "eleven_multilingual_v2",
  "mode": {
    "type": "conversation",
    "conversation": {
      "host_voice_id": "6lCwbsX1yVjD49QmpkTR",
      "guest_voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    }
  },
  "source": {
    "type": "url",
    "url": "https://en.wikipedia.org/wiki/Cognitive_science"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/podcasts");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"type\": \"conversation\",\n    \"conversation\": {\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\",\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\"\n    }\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "model_id": "eleven_multilingual_v2",
  "mode": [
    "type": "conversation",
    "conversation": [
      "host_voice_id": "6lCwbsX1yVjD49QmpkTR",
      "guest_voice_id": "bYTqZQo3Jz7LQtmGTgwi"
    ]
  ],
  "source": [
    "type": "url",
    "url": "https://en.wikipedia.org/wiki/Cognitive_science"
  ]
```

--------------------------------

### Get Dubbing Transcripts via HTTP Request in Swift

Source: https://elevenlabs.io/docs/api-reference/dubbing/transcripts/get

Make an HTTP GET request in Swift to get dubbing transcripts. Ensure the URL includes the correct 'dubbing_id' and 'language_code'.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id/transcripts/language_code/format/srt")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /v1/speech-to-text/evaluation/human-agents/{agent_id}/analytics

Source: https://elevenlabs.io/docs/changelog/2026/3/23

Get analytics for a specific human agent.

```APIDOC
## GET /v1/speech-to-text/evaluation/human-agents/{agent_id}/analytics

### Description
Get analytics for a specific human agent.

### Method
GET

### Endpoint
/v1/speech-to-text/evaluation/human-agents/{agent_id}/analytics

### Parameters
#### Path Parameters
- **agent_id** (string) - Required
```

--------------------------------

### Create Batch Workspace Invites - Go HTTP

Source: https://elevenlabs.io/docs/api-reference/workspace/invites/create-batch

Send bulk invitations using Go's native HTTP client. Requires net/http and io packages.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/workspace/invites/add-bulk"

	payload := strings.NewReader("{\n  \"emails\": [\n    \"john.doe@testmail.com\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Install ElevenAgents Client SDKs Release Candidate

Source: https://elevenlabs.io/docs/changelog/2026/3/23

Use this command to install the release candidate versions of the ElevenAgents client, React, and React Native SDKs to try out the new features and breaking changes.

```bash
npm install @elevenlabs/client@next @elevenlabs/react@next @elevenlabs/react-native@next
```

--------------------------------

### Client Method: startSession

Source: https://elevenlabs.io/docs/eleven-agents/libraries/kotlin

The `startSession` method initiates the WebRTC connection and starts using the microphone to communicate with the ElevenLabs Agents agent. It supports both public and private agents.

```APIDOC
## startSession

### Description
Initiates the WebRTC connection and starts using the microphone to communicate with the ElevenLabs Agents agent.

### Method
Client Method

### Endpoint
ConversationClient.startSession

### Parameters
#### Request Body
- **config** (object) - Required - Configuration object for the session.
  - **agentId** (string) - Required (for public agents) - The ID of the ElevenLabs agent.
  - **conversationToken** (string) - Required (for private agents) - A temporary token for authenticating with private agents. Valid for 10 minutes.
  - **userId** (string) - Optional - An identifier for the user in the conversation.
- **context** (object) - Required - The Android context (e.g., `this` in an Activity).

### Request Example
```kotlin
// Public agent
val session = ConversationClient.startSession(
    config = ConversationConfig(
        agentId = "your-agent-id"
    ),
    context = this
)

// Private agent
val conversationToken = fetchConversationTokenFromServer()
val session = ConversationClient.startSession(
    config = ConversationConfig(
        conversationToken = conversationToken
    ),
    context = this
)

// With userId
val session = ConversationClient.startSession(
    config = ConversationConfig(
        agentId = "your-agent-id",
        userId = "your-user-id"
    ),
    context = this
)
```

### Response
#### Success Response (Session Object)
- **session** (object) - An object representing the active conversation session.
```

--------------------------------

### GET /v1/convai/tools/{tool_id}/dependent-agents

Source: https://elevenlabs.io/docs/api-reference/tools/get-dependent-agents

Get a list of agents depending on this tool.

```APIDOC
## GET /v1/convai/tools/{tool_id}/dependent-agents

### Description
Get a list of agents depending on this tool.

### Method
GET

### Endpoint
/v1/convai/tools/{tool_id}/dependent-agents

### Parameters
#### Path Parameters
- **tool_id** (string) - Required - ID of the requested tool.

#### Query Parameters
- **cursor** (string/null) - Optional - Used for fetching next page. Cursor is returned in the response.
- **page_size** (integer) - Optional - How many documents to return at maximum. Can not exceed 100, defaults to 30.
- **xi-api-key** (string) - Optional - API key for authentication.

### Response
#### Success Response (200)
- **agents** (array of object) - List of agents dependent on the tool. Each object represents an agent and can be one of two types:
  - **DependentAvailableAgentIdentifier**:
    - **type** (string) - Required - Discriminator value: "available".
    - **referenced_resource_ids** (array of string) - Optional - If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
    - **id** (string) - Required - The agent's ID.
    - **name** (string) - Required - The agent's name.
    - **created_at_unix_secs** (integer) - Required - Unix timestamp of creation.
    - **access_level** (string) - Required - The user's access level to the agent ("admin", "editor", "commenter", "viewer").
  - **UnknownDependentAgentIdentifier**:
    - **type** (string) - Required - Discriminator value: "unknown".
    - **referenced_resource_ids** (array of string) - Optional - If the agent is a transitive dependent, contains IDs of the resources that the agent depends on directly.
    - **id** (string) - Required - The agent's ID.
- **branches** (array) - (Definition incomplete in source)
```

--------------------------------

### Create MCP Server (Multi-language)

Source: https://elevenlabs.io/docs/api-reference/mcp/create

Use these code examples to create a new Multi-Channel Proxy (MCP) server. The configuration includes a URL and a name for the server.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.create({
        config: {
            url: "string",
            name: "string",
        },
    });
}
main();
```

```python
from elevenlabs import ElevenLabs, McpServerConfigInput

client = ElevenLabs()

client.conversational_ai.mcp_servers.create(
    config=McpServerConfigInput(
        url="string",
        name="string",
    ),
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers"

	payload := strings.NewReader("{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/mcp-servers")
  .header("Content-Type", "application/json")
  .body("{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/mcp-servers', [
  'body' => '{
  "config": {
    "url": "string",
    "name": "string"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"config\": {\n    \"url\": \"string\",\n    \"name\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["config": [
    "url": "string",
    "name": "string"
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /v1/convai/tools/{tool_id}/dependent-agents

Source: https://elevenlabs.io/docs/api-reference/tools/get-dependent-agents

Get a list of agents depending on this tool.

```APIDOC
## GET /v1/convai/tools/{tool_id}/dependent-agents

### Description
Get a list of agents depending on this tool.

### Method
GET

### Endpoint
/v1/convai/tools/{tool_id}/dependent-agents

### Parameters
#### Path Parameters
- **tool_id** (string) - Required - The ID of the tool for which to retrieve dependent agents.

### Response
#### Success Response (200)
A list of agents that depend on the specified tool.
```

--------------------------------

### GET /v1/convai/knowledge-base/summaries

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-summaries

Gets multiple knowledge base document summaries by their IDs.

```APIDOC
## GET /v1/convai/knowledge-base/summaries

### Description
Gets multiple knowledge base document summaries by their IDs.

### Method
GET

### Endpoint
/v1/convai/knowledge-base/summaries
```

--------------------------------

### Compose Music via Direct HTTP POST Request

Source: https://elevenlabs.io/docs/api-reference/music/compose

These examples illustrate how to make a direct HTTP POST request to the ElevenLabs `/v1/music` endpoint with an empty JSON body using various programming languages.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/music"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/music")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Conversational AI Agent with Go (HTTP Request)

Source: https://elevenlabs.io/docs/api-reference/agents/create

Make a direct HTTP POST request in Go to create a conversational AI agent. This example uses `net/http` for the request.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/create"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### GET /v1/convai/agents/summaries

Source: https://elevenlabs.io/docs/api-reference/agents/get-summaries

Retrieve summaries for specific agents using this GET request.

```APIDOC
## GET /v1/convai/agents/summaries

### Description
Returns summaries for the specified agents.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/convai/agents/summaries
```

--------------------------------

### Get Project Snapshot with C# HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

Use the RestSharp library for C# to make a GET request to the ElevenLabs API. Create a RestClient with the endpoint URL and execute a GET request.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Studio Project Chapter - PHP HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/add-chapter

Uses the Guzzle HTTP client library for PHP. Requires instantiating a Guzzle client and making a POST request with JSON body and headers.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/chapters', [
  'body' => '{
  "name": "Chapter 1"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Initialize Conversation instance with callbacks

Source: https://elevenlabs.io/docs/eleven-agents/libraries/python

Set up a Conversation instance with the ElevenLabs client, agent ID, audio interface, and callback functions for handling agent responses, user transcripts, and optional latency/alignment data.

```python
conversation = Conversation(
    # API client and agent ID.
    elevenlabs,
    agent_id,

    # Assume auth is required when API_KEY is set.
    requires_auth=bool(api_key),

    # Use the default audio interface.
    audio_interface=DefaultAudioInterface(),

    # Simple callbacks that print the conversation to the console.
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"User: {transcript}"),

    # Uncomment if you want to see latency measurements.
    # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),

    # Uncomment if you want to receive audio alignment data with character-level timing.
    # callback_audio_alignment=lambda alignment: print(f"Alignment: {alignment.chars}"),
)
```

--------------------------------

### GET /v1/usage/character-stats

Source: https://elevenlabs.io/docs/api-reference/usage/get

Returns the usage metrics for the current user or the entire workspace they are part of. The response provides a time axis based on the specified aggregation interval (default: day), with usage values for each interval along that axis. Usage is broken down by the selected breakdown type. For example, breakdown type 'voice' will return the usage of each voice for each interval along the time axis. (Deprecated) Use /v1/workspace/analytics/query/usage-by-product-over-time instead.

```APIDOC
## GET /v1/usage/character-stats

### Description
This endpoint is deprecated. Use /v1/workspace/analytics/query/usage-by-product-over-time instead. Returns the usage metrics for the current user or the entire workspace they are part of. The response provides a time axis based on the specified aggregation interval (default: day), with usage values for each interval along that axis. Usage is broken down by the selected breakdown type. For example, breakdown type "voice" will return the usage of each voice for each interval along the time axis.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/usage/character-stats
```

--------------------------------

### GET /v2/voices

Source: https://elevenlabs.io/docs/api-reference/voices/search

Gets a list of all available voices for a user with search, filtering and pagination.

```APIDOC
## GET /v2/voices

### Description
Gets a list of all available voices for a user with search, filtering and pagination.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v2/voices
```

--------------------------------

### Create Knowledge Base Folder with Swift

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/create-folder

This snippet demonstrates how to create a new folder in an ElevenLabs knowledge base using a standard Swift URLSession.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "Project Documentation"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/folder")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Start Expo Development Server with Tunnel

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/expo-react-native

Starts the Expo development server, creating a tunnel to allow access over HTTPS for development purposes.

```bash
npx expo start --tunnel
```

--------------------------------

### Make First API Request with curl

Source: https://elevenlabs.io/docs/api-reference/authentication

Example curl command to test API connectivity. Replace $ELEVENLABS_API_KEY with your actual secret API key.

```bash
curl 'https://api.elevenlabs.io/v1/models' \
  -H 'Content-Type: application/json' \
  -H 'xi-api-key: $ELEVENLABS_API_KEY'
```

--------------------------------

### GET /v1/convai/batch-calling/{batch_id}

Source: https://elevenlabs.io/docs/api-reference/batch-calling/get

Get detailed information about a batch call including all recipients.

```APIDOC
## GET /v1/convai/batch-calling/{batch_id}

### Description
Get detailed information about a batch call including all recipients.

### Method
GET

### Endpoint
/v1/convai/batch-calling/{batch_id}

### Parameters
#### Path Parameters
- **batch_id** (string) - Required - The unique identifier of the batch call.

#### Header Parameters
- **xi-api-key** (string) - Optional - Your Eleven Labs API key.

### Response
#### Success Response (200)
- **Response Body**: Refer to `BatchCallDetailedResponse` schema for details.

#### Error Response (422)
- **Response Body**: Refer to `HTTPValidationError` schema for details.
```

--------------------------------

### Install ElevenLabs Agent Skills

Source: https://elevenlabs.io/docs/eleven-api/resources/agent-tooling

Install the official ElevenLabs skills collection using npm. Required to access reusable building blocks for common ElevenLabs workflows.

```bash
npx skills add elevenlabs/skills
```

--------------------------------

### GET /v1/convai/agents/{agent_id}/branches/{branch_id}

Source: https://elevenlabs.io/docs/api-reference/agents/branches/get

Get information about a single agent branch.

```APIDOC
## GET /v1/convai/agents/{agent_id}/branches/{branch_id}

### Description
Get information about a single agent branch.

### Method
GET

### Endpoint
/v1/convai/agents/{agent_id}/branches/{branch_id}

### Parameters
#### Path Parameters
- **agent_id** (string) - Required - The id of an agent. This is returned on agent creation.
- **branch_id** (string) - Required - Unique identifier for the branch.

#### Header Parameters
- **xi-api-key** (string) - Optional - API key for authentication.

### Response
#### Success Response (200)
- **id** (string) - The unique identifier of the agent branch.
- **name** (string) - The name of the agent branch.
- **agent_id** (string) - The ID of the agent this branch belongs to.
- **description** (string) - A description of the agent branch.
- **created_at** (string) - The timestamp when the agent branch was created.

#### Response Example
```json
{
  "id": "string",
  "name": "string",
  "agent_id": "string",
  "description": "string",
  "created_at": "string"
}
```
```

--------------------------------

### Get Tool Executions using C# HTTP Request (RestSharp)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/get-executions

Perform a GET request in C# using the RestSharp library to get tool executions. Set the content type and an empty JSON body.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id/executions");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Conversational AI Test (Go)

Source: https://elevenlabs.io/docs/api-reference/tests/create

Make a POST request to create a conversational AI test using Go's net/http package. This example includes setting the content type and handling the response.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/create"

	payload := strings.NewReader("{\n  \"name\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}

```

--------------------------------

### GET /v1/convai/knowledge-base/{documentation_id}/dependent-agents

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-agents

Get a list of agents depending on this knowledge base document.

```APIDOC
## GET /v1/convai/knowledge-base/{documentation_id}/dependent-agents

### Description
Get a list of agents depending on this knowledge base document.

### Method
GET

### Endpoint
/v1/convai/knowledge-base/{documentation_id}/dependent-agents

### Parameters
#### Path Parameters
- **documentation_id** - The ID of the knowledge base document.
```

--------------------------------

### Initiate Create Project Request in Java (Partial)

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

This partial Java snippet shows how to begin a POST request to the ElevenLabs Studio Projects API using Unirest, setting the Content-Type header for multipart/form-data.

```Java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
```

--------------------------------

### Create Test Folder - Python SDK

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-folders/create

Use the ElevenLabs Python SDK to create a test folder. Requires the elevenlabs package and an initialized ElevenLabs client.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.folders.create(
    name="Agent Test Suite",
)
```

--------------------------------

### GET /v1/convai/conversations

Source: https://elevenlabs.io/docs/api-reference/conversations/list

Get all conversations of agents that user owns. With option to restrict to a specific agent.

```APIDOC
## GET /v1/convai/conversations

### Description
Get all conversations of agents that user owns. With option to restrict to a specific agent.

### Method
GET

### Endpoint
/v1/convai/conversations

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - Used for fetching next page. Cursor is returned in the response.
- **agent_id** (string) - Optional - The id of the agent you're taking the action on.
- **call_successful** (EvaluationSuccessResult) - Optional - The result of the success evaluation
- **call_start_before_unix** (integer) - Optional - Unix timestamp (in seconds) to filter conversations up to this start date.
- **call_start_after_unix** (integer) - Optional - Unix timestamp (in seconds) to filter conversations after to this start date.
- **call_duration_min_secs** (integer) - Optional - Minimum call duration in seconds.
- **call_duration_max_secs** (integer) - Optional - Maximum call duration in seconds.
- **rating_max** (integer) - Optional - Maximum overall rating (1-5).
- **rating_min** (integer) - Optional - Minimum overall rating (1-5).
- **has_feedback_comment** (boolean) - Optional - Filter conversations with user feedback comments.
- **user_id** (string) - Optional - Filter conversations by the user ID who initiated them.
- **evaluation_params** (array of string) - Optional - Evaluation filters. Repeat param. Format: criteria_id:result. Example: eval=value_framing:success
- **data_collection_params** (array of string) - Optional - Data collection filters. Repeat param. Format: id:op:value where op is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in, pipe-delimit values.
- **tool_names** (array of string) - Optional - Filter conversations by tool names used during the call.
- **tool_names_successful** (array of string) - Optional - Filter conversations by tool names that had successful calls.
- **tool_names_errored** (array of string) - Optional - Filter conversations by tool names that had errored calls.
- **main_languages** (array of string) - Optional - Filter conversations by detected main language (language code).
```

--------------------------------

### GET /v1/convai/conversations/{conversation_id}/audio

Source: https://elevenlabs.io/docs/api-reference/conversations/get-audio

Get the audio recording of a particular conversation by its unique identifier.

```APIDOC
## GET /v1/convai/conversations/{conversation_id}/audio

### Description
Get the audio recording of a particular conversation.

### Method
GET

### Endpoint
/v1/convai/conversations/{conversation_id}/audio

### Parameters
#### Path Parameters
- **conversation_id** (string) - Required - The id of the conversation you're taking the action on.

#### Header Parameters
- **xi-api-key** (string) - Optional - API key for authentication.

### Response
#### Success Response (200)
Description: Successful response

#### Error Response (422)
Description: Validation Error
- **detail** (array of objects) - Details of the validation errors.
  - **loc** (array of string/integer) - Location of the error.
  - **msg** (string) - Error message.
  - **type** (string) - Type of the error.
```

--------------------------------

### GET /v1/convai/agents/{agent_id}/link

Source: https://elevenlabs.io/docs/api-reference/agents/get-link

Get the current link used to share the agent with others.

```APIDOC
## GET /v1/convai/agents/{agent_id}/link

### Description
Get the current link used to share the agent with others.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/convai/agents/{agent_id}/link

### Parameters
#### Path Parameters
- **agent_id** (string) - Required - The id of an agent. This is returned on agent creation.

#### Headers
- **xi-api-key** (string) - Optional - Your ElevenLabs API key.

### Request Example
No request body for GET.

### Response
#### Success Response (200)
- **agent_id** (string) - The ID of the agent.
- **token** (object | null) - The token data for the agent.
  - **agent_id** (string) - The ID of the agent.
  - **conversation_token** (string) - The token for the agent.
  - **expiration_time_unix_secs** (integer | null) - The expiration time of the token in unix seconds.
  - **conversation_id** (string | null) - The ID of the conversation.
  - **purpose** (string) - The purpose of the token. Enum: `signed_url`, `shareable_link`.
  - **token_requester_user_id** (string | null) - The user ID of the entity who requested the token.

#### Response Example (200)
```json
{
  "agent_id": "string",
  "token": {
    "agent_id": "string",
    "conversation_token": "string",
    "expiration_time_unix_secs": 1678886400,
    "conversation_id": "string",
    "purpose": "shareable_link",
    "token_requester_user_id": "string"
  }
}
```

#### Error Response (422) - Validation Error
- **detail** (array of object) - A list of validation errors.
  - **loc** (array of string | integer) - The location of the error.
  - **msg** (string) - The error message.
  - **type** (string) - The type of validation error.

#### Error Response Example (422)
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "agent_id"
      ],
      "msg": "Field required",
      "type": "value_error.missing"
    }
  ]
}
```
```

--------------------------------

### Install ElevenLabs Text-to-Speech Skill

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-speech

Use this command to add the ElevenLabs text-to-speech skill to your project, enabling speech generation from an AI coding assistant.

```bash
npx skills add elevenlabs/skills --skill text-to-speech
```

--------------------------------

### Get Dubbing in Swift

Source: https://elevenlabs.io/docs/api-reference/dubbing/get

Construct an NSMutableURLRequest and use URLSession to perform a GET request for dubbing details.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/dubbing/dubbing_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Studio Project with TypeScript SDK

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

Initialize an ElevenLabsClient and create an empty studio project. Requires the @elevenlabs/elevenlabs-js package.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.create({});
}
main();
```

--------------------------------

### GET /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots

Source: https://elevenlabs.io/docs/api-reference/studio/get-chapter-snapshots

Gets information about all the snapshots of a chapter. Each snapshot can be downloaded as audio. Whenever a chapter is converted a snapshot will automatically be created.

```APIDOC
## GET /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots

### Description
Gets information about all the snapshots of a chapter. Each snapshot can be downloaded as audio. Whenever a chapter is converted a snapshot will automatically be created.

### Method
GET

### Endpoint
/v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots

### Parameters
#### Path Parameters
- **project_id** (string) - Required - The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.
- **chapter_id** (string) - Required - The ID of the chapter to be used. You can use the [List project chapters](/docs/api-reference/studio/get-chapters) endpoint to list all the available chapters.

#### Header Parameters
- **xi-api-key** (string) - Optional - API key for authentication.

### Response
#### Success Response (200)
- **snapshots** (array of ChapterSnapshotResponseModel) - List of chapter snapshots.
  - **chapter_snapshot_id** (string) - The ID of the chapter snapshot.
  - **project_id** (string) - The ID of the project.
  - **chapter_id** (string) - The ID of the chapter.
  - **created_at_unix** (integer) - The creation date of the chapter snapshot.
  - **name** (string) - The name of the chapter snapshot.

#### Response Example
```json
{
  "snapshots": [
    {
      "chapter_snapshot_id": "string",
      "project_id": "string",
      "chapter_id": "string",
      "created_at_unix": 0,
      "name": "string"
    }
  ]
}
```
```

--------------------------------

### Get Dubbing in C#

Source: https://elevenlabs.io/docs/api-reference/dubbing/get

Employ RestSharp to create and execute a GET request to fetch dubbing information.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing/dubbing_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Concise Prompt Instructions (MDX)

Source: https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide

Illustrates the importance of keeping prompt instructions short, clear, and action-based to reduce ambiguity and token usage, thereby enhancing reliability.

```mdx
# Tone

When you're talking to customers, you should try to be really friendly and approachable, making sure that you're speaking in a way that feels natural and conversational, kind of like how you'd talk to a friend, but still maintaining a professional demeanor that represents the company well.
```

```mdx
# Tone

Speak in a friendly, conversational manner while maintaining professionalism.
```

--------------------------------

### Create Test Folder in Ruby

Source: https://elevenlabs.io/docs/api-reference/tests/test-folders/create

This example demonstrates how to make an HTTP POST request to create a new test folder. The folder will be named 'string'.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agent-testing/folders")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Install PyAudio dependencies on macOS

Source: https://elevenlabs.io/docs/eleven-agents/libraries/python

Install required system dependencies for PyAudio on macOS using Homebrew.

```shell
brew install portaudio
```

--------------------------------

### Create Knowledge Base Folder with Ruby

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder

Send an HTTP POST request using Ruby's Net::HTTP library to create a new folder. Set the Content-Type header and request body.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/folder")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Real-time Speech-to-Text with WebSockets in Python

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming

This example demonstrates how to set up a WebSocket connection, send audio chunks, and process real-time transcriptions using Python's asyncio and websockets libraries. It includes functions for sending audio, receiving transcripts, and orchestrating the full transcription process.

```python
                  json.dumps(
                      {
                          "message_type": "input_audio_chunk",
                          "audio_base_64": "",
                          "commit": True,
                          "sample_rate": 16000,
                      }
                  )
              )

          async def receive_transcripts(ws):
              """Receive and process transcripts from the websocket"""
              while True:
                  try:
                      # Wait for 10 seconds for a message
                      # Adjust the timeout in cases where audio files have more than 10 seconds before speech starts, or if the audio is longer than 10 seconds.
                      message = await asyncio.wait_for(ws.recv(), timeout=10.0)
                      data = json.loads(message)

                      if data["message_type"] == "partial_transcript":
                          print(f"Partial: {data['text']}")
                      elif data["message_type"] == "committed_transcript":
                          print(f"Committed: {data['text']}")
                      elif data["message_type"] == "committed_transcript_with_timestamps":
                          print(f"Committed with timestamps: {data['words']}")
                          break
                      elif data["message_type"] == "input_error":
                          print(f"Error: {data}")
                  except asyncio.TimeoutError:
                      print("Timeout waiting for transcript")


          async def transcribe():
              url = "wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v2_realtime"
              headers = {"xi-api-key": os.getenv("ELEVENLABS_API_KEY")}

              async with websockets.connect(url, additional_headers=headers) as ws:
                  # Connection established, wait for session_started
                  session_msg = await ws.recv()
                  print(f"Session started: {session_msg}")

                  # Read audio file (16 kHz, mono, 16-bit PCM, little-endian)
                  with open("/path/to/audio.pcm", "rb") as f:
                      audio_data = f.read()

                  # Run sending and receiving concurrently
                  await asyncio.gather(
                      send_audio(ws, audio_data),
                      receive_transcripts(ws)
                  )


          asyncio.run(transcribe())
```

--------------------------------

### Update an Agent Branch

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/branches/update

Use these examples to modify an existing conversational AI agent branch. The examples demonstrate how to send a PATCH request to the ElevenLabs API with an empty body, indicating no specific fields are being updated in this basic example.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.branches.update("agent_id", "branch_id", {});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.branches.update(
    agent_id="agent_id",
    branch_id="branch_id",
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/branches/branch_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Knowledge Base Folder with PHP (Guzzle)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-folder

Create a new folder using a POST request with Guzzle HTTP client in PHP. Ensure Guzzle is installed via Composer.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/folder', [
  'body' => '{
  "name": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Complete useScribe React Component Example

Source: https://elevenlabs.io/docs/eleven-api/resources/libraries/react-scribe

Full working example of a React component using useScribe with VAD-based commit strategy, microphone input, event handlers, and UI for displaying live and committed transcripts.

```tsx
import { useScribe, CommitStrategy } from '@elevenlabs/react';
import { useEffect } from 'react';

function ScribeDemo() {
  const scribe = useScribe({
    modelId: 'scribe_v2_realtime',
    commitStrategy: CommitStrategy.VAD,
    onSessionStarted: () => console.log('Started'),
    onCommittedTranscript: (data) => console.log('Committed:', data.text),
    onError: (error) => console.error('Error:', error),
  });

  const startMicrophone = async () => {
    const token = await fetchToken();
    await scribe.connect({
      token,
      microphone: {
        echoCancellation: true,
        noiseSuppression: true,
      },
    });
  };

  const handleDisconnect = () => scribe.disconnect();

  const handleClearTranscripts = () => scribe.clearTranscripts();

  useEffect(() => {
    return () => {
      handleDisconnect();
    };
  }, []);

  return (
    <div>
      <h1>Scribe Demo</h1>

      {/* Status */}
      <div>
        Status: {scribe.status}
        {scribe.error && <span>Error: {scribe.error}</span>}
      </div>

      {/* Controls */}
      <div>
        {!scribe.isConnected ? (
          <button onClick={startMicrophone}>Start Recording</button>
        ) : (
          <button onClick={handleDisconnect}>Stop</button>
        )}
        <button onClick={handleClearTranscripts}>Clear</button>
      </div>

      {/* Live Transcript */}
      {scribe.partialTranscript && (
        <div>
          <strong>Live:</strong> {scribe.partialTranscript}
        </div>
      )}

      {/* Committed Transcripts */}
      <div>
        <h2>Transcripts ({scribe.committedTranscripts.length})</h2>
        {scribe.committedTranscripts.map((t) => (
          <div key={t.id}>
            <span>{new Date(t.timestamp).toLocaleTimeString()}</span>
            <p>{t.text}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

--------------------------------

### Get Conversation in Swift

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get

Make a GET request to the ElevenLabs API to retrieve a conversation using URLSession in Swift.

```swift
import Foundation

let headers = ["xi-api-key": "xi-api-key"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/conversations/123")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Studio Project Chapter - Ruby HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/add-chapter

Uses Ruby's Net::HTTP library to make a POST request. Requires setting up URI, HTTP connection with SSL, and manually constructing the JSON body.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Chapter 1\"\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Audio Native Project Settings with Ruby (Net::HTTP)

Source: https://elevenlabs.io/docs/api-reference/audio-native/get-settings

Construct a GET request to the ElevenLabs API using Ruby's Net::HTTP library to fetch project settings.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/audio-native/project_id/settings")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Conversation in C#

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get

Make a GET request to the ElevenLabs API to retrieve a conversation using RestSharp in C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/conversations/123");
var request = new RestRequest(Method.GET);
request.AddHeader("xi-api-key", "xi-api-key");
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Studio Project Chapter - Swift HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/add-chapter

Uses Swift's Foundation URLSession to make a POST request. Requires constructing headers, serializing JSON parameters, and handling the async response.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "Chapter 1"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Generate Initial Music Composition with Detailed Plan

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/music/inpainting

This snippet defines a detailed composition plan with global and local styles, durations, and lines for multiple sections. It then uses `compose_detailed` to generate the initial audio and stores the `song_id` for potential future inpainting.

```python
composition_plan = {
    "positive_global_styles": ["cinematic", "epic", "orchestral", "trailer"],
    "negative_global_styles": ["acoustic", "pop", "minimalistic"],
    "sections": [
        {
            "section_name": "Intro",
            "positive_local_styles": ["low strings", "suspenseful"],
            "negative_local_styles": [],
            "duration_ms": 15000,
            "lines": ["In a world beyond code", "Where sound becomes life"]
        },
        {
            "section_name": "Build",
            "positive_local_styles": ["rising brass", "full orchestra"],
            "negative_local_styles": [],
            "duration_ms": 20000,
            "lines": ["Technology awakens the future", "Shaping every word into power"]
        },
        {
            "section_name": "Bridge",
            "positive_local_styles": ["ethereal choir", "crescendo"],
            "negative_local_styles": [],
            "duration_ms": 15000,
            "lines": ["(ah ah ah ah)"]
        },
        {
            "section_name": "Outro",
            "positive_local_styles": ["deep narration", "epic finale"],
            "negative_local_styles": [],
            "duration_ms": 10000,
            "lines": ["The voice of tomorrow, unleashed", "Elevenlabs"]
        }
    ]
}

response = elevenlabs.music.compose_detailed(
    composition_plan=composition_plan,
    store_for_inpainting=True
)
song_id = response.song_id
```

```typescript
const compositionPlan = {
  positiveGlobalStyles: ['cinematic', 'epic', 'orchestral', 'trailer'],
  negativeGlobalStyles: ['acoustic', 'pop', 'minimalistic'],
  sections: [
    {
      sectionName: 'Intro',
      positiveLocalStyles: ['low strings', 'suspenseful'],
      negativeLocalStyles: [],
      durationMs: 15000,
      lines: ['In a world beyond code', 'Where sound becomes life'],
    },
    {
      sectionName: 'Build',
      positiveLocalStyles: ['rising brass', 'full orchestra'],
      negativeLocalStyles: [],
      durationMs: 20000,
      lines: ['Technology awakens the future', 'Shaping every word into power'],
    },
    {
      sectionName: 'Bridge',
      positiveLocalStyles: ['ethereal choir', 'crescendo'],
      negativeLocalStyles: [],
      durationMs: 15000,
      lines: ['(ah ah ah ah)'],
    },
    {
      sectionName: 'Outro',
      positiveLocalStyles: ['deep narration', 'epic finale'],
      negativeLocalStyles: [],
      durationMs: 10000,
      lines: ['The voice of tomorrow', 'Unleashed'],
    },
  ],
};

const response = await elevenlabs.music.composeDetailed({
  compositionPlan,
  storeForInpainting: true,
});
const songId = response.songId;
```

--------------------------------

### Start Conversation with Dynamic Variables (Swift)

Source: https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables

This Swift snippet illustrates how to define dynamic variables with different types and use them to configure and start a conversational AI session.

```swift
let dynamicVars: [String: DynamicVariableValue] = [
  "customer_name": .string("John Doe"),
  "account_balance": .number(5000.50),
  "user_id": .int(12345),
  "is_premium": .boolean(true)
]

// Create session config with dynamic variables
let config = SessionConfig(
    agentId: "agent_7101k5zvyjhmfg983brhmhkd98n6",
    dynamicVariables: dynamicVars
)

// Start the conversation
let conversation = try await Conversation.startSession(
    config: config
)
```

--------------------------------

### Create Pronunciation Dictionary from File using SDKs

Source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-file

These examples demonstrate how to create a new pronunciation dictionary by uploading a file using the ElevenLabs SDKs for TypeScript and Python.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.pronunciationDictionaries.createFromFile({});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.pronunciation_dictionaries.create_from_file(
    file="example_file",
)
```

--------------------------------

### Create audio-native with Python SDK

Source: https://elevenlabs.io/docs/api-reference/audio-native/create

Use the ElevenLabs Python client to create audio-native content with a file parameter. Requires the elevenlabs package.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_native.create(
    file="example_file",
)
```

--------------------------------

### List Service Account API Keys

Source: https://elevenlabs.io/docs/api-reference/service-accounts/api-keys/list

Use these examples to list all API keys for a given service account ID. Replace 'service_account_user_id' with the actual ID of the service account.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.serviceAccounts.apiKeys.list("service_account_user_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.service_accounts.api_keys.list(
    service_account_user_id="service_account_user_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/service-accounts/service_account_user_id/api-keys")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Manage ElevenLabs Agent Templates

Source: https://elevenlabs.io/docs/eleven-agents/operate/cli

List available agent templates or display the configuration for a specific template.

```bash
elevenlabs agents templates list
```

```bash
elevenlabs agents templates show <template>
```

--------------------------------

### Get a Batch Call (Swift)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get

Illustrates how to fetch batch call data using URLSession with a GET request in Swift.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/batch-calling/batch_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Usage By Product Over Time (Python SDK)

Source: https://elevenlabs.io/docs/api-reference/workspace/usage/get-usage-by-product-over-time

Utilize the ElevenLabs Python SDK to fetch product usage statistics for a given time period.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.workspace.usage.get_usage_by_product_over_time(
    start_time=1680307200000,
    end_time=1682899200000,
)
```

--------------------------------

### Get Workspace Secret with Swift

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

Execute a GET request using URLSession in Swift to obtain a specific workspace secret.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Secret Dependencies - C# HTTP

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

Make a GET request to the secrets dependencies endpoint using RestSharp for C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Studio Project with Multipart Form Data - PHP

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

PHP example using Guzzle HTTP client to POST a multipart form-data request to create a studio project. Demonstrates file upload and form field handling.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects', [
  'multipart' => [
    [
        'name' => 'name',
        'contents' => 'Project 1'
    ],
    [
        'name' => 'from_document',
        'filename' => '<file1>',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

--------------------------------

### Get User Subscription (Ruby)

Source: https://elevenlabs.io/docs/api-reference/user/subscription/get

Perform an HTTP GET request in Ruby to retrieve the user's subscription details.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/user/subscription")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### POST /v1/studio/podcasts

Source: https://elevenlabs.io/docs/api-reference/studio/create-podcast

Create and auto-convert a podcast project. Currently, the LLM cost is covered by us but you will still be charged for the audio generation. In the future, you will be charged for both the LLM and audio generation costs.

```APIDOC
## POST /v1/studio/podcasts

### Description
Create and auto-convert a podcast project. Currently, the LLM cost is covered by us but you will still be charged for the audio generation. In the future, you will be charged for both the LLM and audio generation costs.

### Method
POST

### Endpoint
/v1/studio/podcasts

### Parameters
#### Header Parameters
- **xi-api-key** (string) - Optional - 
- **safety-identifier** (string, null) - Optional - Used for moderation. Your workspace must be allowlisted to use this feature.

#### Request Body
- **mode** (object) - Required - The type of podcast to generate. Can be 'conversation', an interaction between two voices, or 'bulletin', a monologue.
  - **type** (string) - Required - The type of podcast to create. (Enum: "conversation", "bulletin")
  - **conversation** (object) - Required (if type is "conversation") - The voice settings for the conversation.
    - **host_voice_id** (string) - Required - The ID of the host voice.
    - **guest_voice_id** (string) - Required - The ID of the guest voice.
  - **bulletin** (object) - Required (if type is "bulletin") - The voice settings for the bulletin.
    - **host_voice_id** (string) - Required - The ID of the host voice.
- **source** (object) - Required - The source content for the podcast.
  - **type** (string) - Required - The type of source to create. (Enum: "text", "url")
  - **text** (string) - Required (if type is "text") - The text to create the podcast from.
  - **url** (string) - Required (if type is "url") - The URL to create the podcast from.

### Request Example
```json
{
  "mode": {
    "type": "conversation",
    "conversation": {
      "host_voice_id": "some_host_voice_id",
      "guest_voice_id": "some_guest_voice_id"
    }
  },
  "source": {
    "type": "text",
    "text": "Hello, and welcome to our podcast. Today we discuss the future of AI."
  }
}
```

### Response
#### Success Response (200)
- **PodcastProjectResponseModel** (object) - Successful Response. (Schema details not provided in source)

#### Response Example
```json
{
  "message": "Podcast project created successfully",
  "project_id": "some_project_id",
  "status": "processing"
}
```

#### Error Response (422)
- **HTTPValidationError** (object) - Validation Error. (Schema details not provided in source)

#### Error Example
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "mode",
        "type"
      ],
      "msg": "value is not a valid enumeration member",
      "type": "type_error.enum"
    }
  ]
}
```
```

--------------------------------

### GET /v1/user

Source: https://elevenlabs.io/docs/api-reference/user/get

Gets information about the user. This endpoint retrieves the authenticated user's account details and profile information.

```APIDOC
## GET /v1/user

### Description
Gets information about the authenticated user. Returns details about the user's account, subscription, and profile.

### Method
GET

### Endpoint
https://api.elevenlabs.io/v1/user

### Authentication
Required - API Key authentication

### Response
#### Success Response (200)
Returns user account information including subscription details and usage statistics.

### Reference
https://elevenlabs.io/docs/api-reference/user/get
```

--------------------------------

### Create Tool Approval

Source: https://elevenlabs.io/docs/api-reference/mcp/approval-policies/create

Use these examples to create a new tool approval for a specified MCP server. Replace `mcp_server_id`, `toolName`, and `toolDescription` with actual values.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.mcpServers.toolApprovals.create("mcp_server_id", {
        toolName: "string",
        toolDescription: "string",
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tool_approvals.create(
    mcp_server_id="mcp_server_id",
    tool_name="string",
    tool_description="string",
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals"

	payload := strings.NewReader("{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")
  .header("Content-Type", "application/json")
  .body("{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals', [
  'body' => '{
  "tool_name": "string",
  "tool_description": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "tool_name": "string",
  "tool_description": "string"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Agent Draft with PHP

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/drafts/create

Use this PHP example to create a new agent draft. It defines a complex workflow with various nodes and edges, including conditions for forwarding.

```php
<?php

require_once(__DIR__ . '/vendor/autoload.php');

$client = new ujieda
est
estclient('https://api.elevenlabs.io/v1/convai/agents/agent_id/drafts?branch_id=branch_id');
$response = $client->post('{
  "workflow": {
    "edges": {
      "entry_to_tool_a": {
        "source": "entry_node",
        "target": "tool_node_a",
        "forward_condition": {
          "condition": "Tool A condition"
        }
      },
      "start_to_entry": {
        "source": "start_node",
        "target": "entry_node",
        "forward_condition": {}
      },
      "tool_a_to_failure": {
        "source": "tool_node_a",
        "target": "failure_node",
        "forward_condition": {
          "successful": false
        }
      },
      "tool_a_to_tool_b": {
        "source": "tool_node_a",
        "target": "tool_node_b",
        "forward_condition": {
          "successful": true
        }
      },
      "tool_b_to_agent_transfer": {
        "source": "tool_node_b",
        "target": "success_transfer",
        "forward_condition": {}
      },
      "tool_b_to_conversation": {
        "source": "tool_node_b",
        "target": "success_conversation",
        "forward_condition": {
          "condition": "Conversation condition"
        }
      },
      "tool_b_to_end": {
        "target": "success_end",
        "forward_condition": {
          "condition": "End condition"
        }
      },
      "tool_b_to_phone": {
        "source": "tool_node_b",
        "target": "success_phone",
        "forward_condition": {
          "expression": {
            "children": [
              {
                "name": "force_phone_transfer"
              },
              {
                "prompt": "Phone condition",
                "value_schema": {
                  "description": "Phone condition",
                  "type": "boolean"
                }
              },
              {
                "left": {
                  "name": "mode"
                },
                "right": {
                  "value": "dev"
                }
              }
            ]
          }
        }
      }
    },
    "nodes": {
      "entry_node": {
        "conversation_config": {},
        "edge_order": [
          "entry_to_tool_a"
        ],
        "label": "Entry"
      },
      "failure_node": {
        "conversation_config": {},
        "label": "Failure"
      },
      "start_node": {
        "edge_order": [
          "start_to_entry"
        ]
      },
      "success_conversation": {
        "conversation_config": {},
        "label": "Success A"
      },
      "success_end": {},
      "success_phone": {
        "transfer_destination": {
          "phone_number": "+1234567890"
        }
      },
      "success_transfer": {
        "agent_id": "success_transfer_agent"
      },
      "tool_node_a": {
        "edge_order": [
          "tool_a_to_failure",
          "tool_a_to_tool_b"
        ],
        "tools": [
          {
            "tool_id": "tool_a"
          },
          {
            "tool_id": "tool_b"
          }
        ]
      },
      "tool_node_b": {
        "edge_order": [
          "tool_b_to_conversation",
          "tool_b_to_end",
          "tool_b_to_phone",
          "tool_b_to_agent_transfer"
        ],
        "tools": [
          {
            "tool_id": "tool_a"
          }
        ]
      }
    }
  },
  "name": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Get Test Invocation (C# RestSharp)

Source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get

Fetches a test invocation using a GET request with the RestSharp library in C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Test Folder in PHP

Source: https://elevenlabs.io/docs/api-reference/tests/test-folders/create

This example uses GuzzleHttp to make an HTTP POST request to create a new test folder. The folder will be named 'string'.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/agent-testing/folders', [
  'body' => '{
  "name": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Get Summaries (Swift URLSession)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-summaries

Make an HTTP GET request using URLSession in Swift to retrieve document summaries.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%22string%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Summaries (C# RestSharp)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-summaries

Use the RestSharp library in C# to make an HTTP GET request for document summaries.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%22string%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Audio Native Project Settings with Swift (URLSession)

Source: https://elevenlabs.io/docs/api-reference/audio-native/get-settings

Create an NSMutableURLRequest and use URLSession to perform a GET request to the ElevenLabs API for project settings.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/audio-native/project_id/settings")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Summaries (Java Unirest)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-summaries

Use the Unirest library in Java to make an HTTP GET request for document summaries.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%22string%22%5D")
  .asString();
```

--------------------------------

### Expose Local Server with ngrok

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/upstash-redis

Run this command to expose your local server to the internet, enabling ElevenLabs to send webhooks to your development environment.

```bash
ngrok http 3000
```

--------------------------------

### Get Summaries (Ruby HTTP)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-summaries

Make a direct HTTP GET request in Ruby to retrieve document summaries from the API.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%22string%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Summaries (Go HTTP)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-summaries

Make a direct HTTP GET request in Go to retrieve document summaries from the API.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%22string%22%5D"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Initialize WebSocket connection in Python

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts

Set up a WebSocket connection to the ElevenLabs text-to-speech API using the eleven_flash_v2_5 model. Loads API key from environment variables and constructs the WebSocket URI with voice ID and model parameters.

```python
import os
from dotenv import load_dotenv
import websockets

# Load the API key from the .env file
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

voice_id = 'Xb7hH8MSUJpSbSDYk0k2'

# For use cases where latency is important, we recommend using the 'eleven_flash_v2_5' model.
model_id = 'eleven_flash_v2_5'

async def text_to_speech_ws_streaming(voice_id, model_id):
    uri = f"wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream-input?model_id={model_id}"

    async with websockets.connect(uri) as websocket:
       ...
```

--------------------------------

### Get Dubbing in Java

Source: https://elevenlabs.io/docs/api-reference/dubbing/get

Use the Unirest library to send a GET request to the dubbing API and retrieve the response as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/dubbing/dubbing_id")
  .asString();
```

--------------------------------

### Create Studio Project Chapter - Python SDK

Source: https://elevenlabs.io/docs/api-reference/studio/add-chapter

Uses the official ElevenLabs Python SDK to create a chapter. Instantiate an ElevenLabs client and call studio.projects.chapters.create with project_id and name parameters.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.chapters.create(
    project_id="project_id",
    name="Chapter 1",
)
```

--------------------------------

### Get Project Snapshot with Java HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

Use the Unirest library for Java to make a GET request to the ElevenLabs API. The asString() method returns the response as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")
  .asString();
```

--------------------------------

### Get Dubbing in Python

Source: https://elevenlabs.io/docs/api-reference/dubbing/get

Initialize the ElevenLabs client and call the dubbing service's get method with the dubbing ID.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.get(
    dubbing_id="dubbing_id",
)
```

--------------------------------

### Create Knowledge Base Folder with PHP

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/create-folder

This snippet demonstrates how to create a new folder in an ElevenLabs knowledge base using the Guzzle HTTP client for PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/knowledge-base/folder', [
  'body' => '{
  "name": "Project Documentation"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### List dubs with HTTP GET request - C#

Source: https://elevenlabs.io/docs/api-reference/dubbing/list

Make a raw HTTP GET request using the RestSharp library.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/dubbing");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Test Folder in Python

Source: https://elevenlabs.io/docs/api-reference/tests/test-folders/create

Use the ElevenLabs client to create a new test folder for Conversational AI agents. The folder will be named 'string'.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.tests.folders.create(
    name="string",
)
```

--------------------------------

### Configure ElevenLabs Python SDK for Data Residency

Source: https://elevenlabs.io/docs/overview/administration/data-residency

Set up the Python SDK client with EU or India data residency using the ElevenLabsEnvironment parameter. Requires the elevenlabs package and a valid API key.

```python
from elevenlabs import ElevenLabs, ElevenLabsEnvironment

# For EU data residency
client = ElevenLabs(
    api_key="your-api-key",
    environment=ElevenLabsEnvironment.PRODUCTION_EU
)

# For India data residency
client = ElevenLabs(
    api_key="your-api-key",
    environment=ElevenLabsEnvironment.PRODUCTION_IN
)
```

--------------------------------

### GET /v1/models

Source: https://elevenlabs.io/docs/api-reference/authentication

Demonstrates how to make an authenticated GET request to the `/v1/models` endpoint using `curl`, including the `xi-api-key` header.

```APIDOC
## GET /v1/models

### Description
This example shows how to make your first authenticated API request. It demonstrates the correct way to include your API key in the `xi-api-key` header.

### Method
GET

### Endpoint
/v1/models

### Parameters
#### Request Headers
- **Content-Type** (string) - Required - Set to `application/json`.
- **xi-api-key** (string) - Required - Your ElevenLabs API key.

### Request Example
```bash
curl 'https://api.elevenlabs.io/v1/models' \
  -H 'Content-Type: application/json' \
  -H 'xi-api-key: $ELEVENLABS_API_KEY'
```
```

--------------------------------

### Convert Studio Project - Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/convert-project

Make a POST request to the ElevenLabs API using Go's standard net/http package. Requires the project_id in the URL path.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/convert"

	req, _ := http.NewRequest("POST", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Install Python Dependencies for WebSocket Streaming

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket

Install required Python packages for WebSocket communication and environment variable management.

```python
pip install python-dotenv websockets
```

--------------------------------

### Generate composition plan from prompt

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/music

Create a composition plan by providing a detailed music description prompt and desired duration. The API returns structured style guidelines and section breakdowns for music generation.

```python
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
from dotenv import load_dotenv
load_dotenv()

elevenlabs = ElevenLabs(
api_key=os.getenv("ELEVENLABS_API_KEY"),
)

composition_plan = elevenlabs.music.composition_plan.create(
    prompt="Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
    music_length_ms=10000,
)

print(composition_plan)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import "dotenv/config";

const elevenlabs = new ElevenLabsClient();

const compositionPlan = await elevenlabs.music.compositionPlan.create({
  prompt: "Create an intense, fast-paced electronic track for a high-adrenaline video game scene. Use driving synth arpeggios, punchy drums, distorted bass, glitch effects, and aggressive rhythmic textures. The tempo should be fast, 130–150 bpm, with rising tension, quick transitions, and dynamic energy bursts.",
  musicLengthMs: 10000,
});

console.log(JSON.stringify(compositionPlan, null, 2));
```

--------------------------------

### Get Project Snapshot with Ruby HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

Make a GET request using Ruby's Net::HTTP library. Create a URI object, establish an HTTPS connection, and execute the request to retrieve the snapshot.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Install Python dependencies for WebSocket streaming

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts

Install python-dotenv for environment variable management and websockets for WebSocket client functionality.

```python
pip install python-dotenv
pip install websockets
```

--------------------------------

### Get Agent - C# HTTP

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get

Retrieve an agent using RestSharp for C#. Creates a REST client and executes a GET request.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Studio Project Chapter - Java HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/add-chapter

Uses the Unirest library for Java to make a POST request. Requires adding Content-Type header and JSON body as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/chapters")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Chapter 1\"\n}")
  .asString();
```

--------------------------------

### Get Knowledge Base Document Content in Swift

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-content

Perform an asynchronous GET request to retrieve knowledge base document content.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Knowledge Base Document Content in Ruby

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-content

Perform an HTTP GET request to retrieve content from a knowledge base document.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Conversation in PHP

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get

Make a GET request to the ElevenLabs API to retrieve a conversation using Guzzle HTTP client in PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/conversations/123', [
  'headers' => [
    'xi-api-key' => 'xi-api-key',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Start Conversation and Observe State

Source: https://elevenlabs.io/docs/eleven-agents/libraries/swift

Initialize a conversation with an agent and observe connection state and messages using reactive publishers. Optionally pass userId to map conversations to your users.

```swift
import ElevenLabs

// Start a conversation with your agent
let conversation = try await ElevenLabs.startConversation(
    agentId: "your-agent-id",
    userId: "your-end-user-id",
    config: ConversationConfig()
)

// Observe conversation state and messages
conversation.$state
    .sink { state in
        print("Connection state: \(state)")
    }
    .store(in: &cancellables)

conversation.$messages
    .sink { messages in
        for message in messages {
            print("\(message.role): \(message.content)")
        }
    }
    .store(in: &cancellables)

// Send messages and control the conversation
try await conversation.sendMessage("Hello!")
try await conversation.toggleMute()
await conversation.endConversation()
```

--------------------------------

### Get Knowledge Base Size with Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/size

Make a direct HTTP GET request to the ElevenLabs API using Go's net/http package. No SDK required.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent/agent_id/knowledge-base/size"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Install ElevenLabs Voice Changer Skill

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/voice-changer

Install the ElevenLabs Voice Changer skill using npx to enable voice transformation via an AI coding assistant.

```bash
npx skills add elevenlabs/skills --skill voice-changer
```

--------------------------------

### Install ElevenLabs Music Skill

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/music

Use this command to add the ElevenLabs music skill to your AI coding assistant.

```bash
npx skills add elevenlabs/skills --skill music
```

--------------------------------

### Get Conversation in Java

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get

Make a GET request to the ElevenLabs API to retrieve a conversation using the Unirest HTTP client in Java.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/conversations/123")
  .header("xi-api-key", "xi-api-key")
  .asString();
```

--------------------------------

### Get Conversation in Go

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get

Make a GET request to the ElevenLabs API to retrieve a conversation using standard Go HTTP client.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/conversations/123"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("xi-api-key", "xi-api-key")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Push ElevenLabs Agent Configuration to Platform

Source: https://elevenlabs.io/docs/eleven-agents/quickstart

Upload your local agent configuration to the ElevenLabs platform, making it available for deployment and testing.

```bash
elevenlabs agents push --agent "My Assistant"
```

--------------------------------

### Create Project Pronunciation Dictionary

Source: https://elevenlabs.io/docs/api-reference/studio/create-pronunciation-dictionaries

This snippet demonstrates how to create a pronunciation dictionary for a specific project. It includes examples using various ElevenLabs SDKs and direct HTTP POST requests to the API endpoint.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.pronunciationDictionaries.create("project_id", {
        pronunciationDictionaryLocators: [
            {
                pronunciationDictionaryId: "string",
                versionId: "string",
            },
        ],
    });
}
main();
```

```python
from elevenlabs import ElevenLabs, PronunciationDictionaryVersionLocator

client = ElevenLabs()

client.studio.projects.pronunciation_dictionaries.create(
    project_id="project_id",
    pronunciation_dictionary_locators=[
        PronunciationDictionaryVersionLocator(
            pronunciation_dictionary_id="string",
            version_id="string",
        )
    ],
)
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries"

	payload := strings.NewReader("{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")
  .header("Content-Type", "application/json")
  .body("{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries', [
  'body' => '{
  "pronunciation_dictionary_locators": [
    {
      "pronunciation_dictionary_id": "string",
      "version_id": "string"
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"pronunciation_dictionary_locators\": [\n    {\n      \"pronunciation_dictionary_id\": \"string\",\n      \"version_id\": \"string\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["pronunciation_dictionary_locators": [
    [
      "pronunciation_dictionary_id": "string",
      "version_id": "string"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/pronunciation-dictionaries")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /conversations/{conversation_id} - Get Conversation

Source: https://elevenlabs.io/docs/changelog/2026/3/9

Retrieve details of a specific conversation. The endpoint now includes an environment field in conversation records.

```APIDOC
## GET /conversations/{conversation_id}

### Description
Retrieve details of a specific conversation including environment information.

### Method
GET

### Endpoint
/conversations/{conversation_id}

### Path Parameters
- **conversation_id** (string) - Required - The unique identifier of the conversation

### Response
#### Success Response (200)
- **environment** (string) - The environment in which the conversation occurred
```

--------------------------------

### Get Workspace Secret with C# (RestSharp)

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

Retrieve a workspace secret by making a GET request using the RestSharp library in C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Test Folder in Swift

Source: https://elevenlabs.io/docs/api-reference/tests/test-folders/create

This example demonstrates how to make an HTTP POST request to create a new test folder using URLSession. The folder will be named 'string'.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agent-testing/folders")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Workspace Secret with PHP (Guzzle)

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

Fetch a workspace secret using a GET request with the Guzzle HTTP client in PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id');

echo $response->getBody();
```

--------------------------------

### Get Workspace Secret with Java (Unirest)

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

Use the Unirest library in Java to send a GET request and retrieve a workspace secret.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id")
  .asString();
```

--------------------------------

### Create Tool Configuration in Ruby

Source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create

This snippet demonstrates how to send an HTTP POST request in Ruby to create a tool configuration.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tool_name\": \"string\"\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Workspace Secret with Ruby

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

Perform an HTTP GET request in Ruby to fetch a specific workspace secret from the ElevenLabs API.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### POST /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive

Source: https://elevenlabs.io/docs/api-reference/studio/archive-snapshot

Returns a compressed archive of the Studio project's audio.

```APIDOC
## POST /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive

### Description
Returns a compressed archive of the Studio project's audio.

### Method
POST

### Endpoint
/v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive

### Parameters
#### Path Parameters
- **project_id** (string) - Required - The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.
- **project_snapshot_id** (string) - Required - The ID of the Studio project snapshot.

#### Header Parameters
- **xi-api-key** (string) - Optional - 

### Request Example
(No request body for this endpoint)

### Response
#### Success Response (200)
- **Content-Type**: application/octet-stream - Streaming archive data (binary file)

#### Response Example
(Binary data, no JSON example)

#### Error Response (422)
- **detail** (array of object) - Validation Error details
  - **loc** (array of string/integer) - Location of the error
  - **msg** (string) - Error message
  - **type** (string) - Type of error

#### Response Example
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "field_name"
      ],
      "msg": "Field required",
      "type": "value_error.missing"
    }
  ]
}
```
```

--------------------------------

### GET /v1/convai/secrets/{secret_id}/dependencies/{resource_type}

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

Get a paginated list of resources that depend on a specific secret, filtered by resource type.

```APIDOC
## GET /v1/convai/secrets/{secret_id}/dependencies/{resource_type}

### Description
Get paginated list of resources that depend on a specific secret, filtered by resource type.

### Method
GET

### Endpoint
/v1/convai/secrets/{secret_id}/dependencies/{resource_type}

### Parameters
#### Path Parameters
- **secret_id** (string) - Required
- **resource_type** (string) - Required - Enum: tools, agents, phone_numbers

#### Query Parameters
- **page_size** (integer) - Optional - How many dependency items to return per page. Default: 20
- **cursor** (string, null) - Optional - Used for fetching next page. Cursor is returned in the response.

#### Header Parameters
- **xi-api-key** (string) - Optional

### Response
#### Success Response (200)
- **Response Body** (Object) - Successful Response. Schema: GetSecretDependenciesResponseModel
```

--------------------------------

### Get Widget (Ruby)

Source: https://elevenlabs.io/docs/api-reference/widget/get

Perform an HTTP GET request in Ruby to retrieve the widget data for a specified conversational AI agent.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agents/agent_id/widget")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Create Knowledge Base Folder with Ruby

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/create-folder

This snippet demonstrates how to create a new folder in an ElevenLabs knowledge base using a standard Ruby HTTP client.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/folder")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Project Documentation\"\n}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Upload existing audio file for inpainting with ElevenLabs

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/music/inpainting

Upload an existing audio file to store it for inpainting. Optionally extract the composition plan to understand the song structure.

```python
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()
elevenlabs = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))

# Upload an existing audio file for inpainting
response = elevenlabs.music.upload(
    file=open("my-song.mp3", "rb"),
    extract_composition_plan=True  # Optional: extract the composition plan
)
song_id = response.song_id
composition_plan = response.composition_plan  # None if extract_composition_plan is False
```

```typescript
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import 'dotenv/config';
import fs from 'fs';

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

const response = await elevenlabs.music.upload({
  file: fs.createReadStream('my-song.mp3'),
  extractCompositionPlan: true, // Optional: extract the composition plan
});
const songId = response.songId;
const compositionPlan = response.compositionPlan; // undefined if extractCompositionPlan is false
```

--------------------------------

### Get Conversational AI Settings (Swift)

Source: https://elevenlabs.io/docs/api-reference/workspace/get

Make a GET request to retrieve conversational AI settings using URLSession in Swift.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/settings")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Stream Speech-to-Speech Audio using SDK

Source: https://elevenlabs.io/docs/api-reference/speech-to-speech/stream

These examples demonstrate how to stream speech-to-speech audio using the ElevenLabs SDKs, providing a high-level abstraction over the API.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient({
        apiKey: "xi-api-key",
    });
    await client.speechToSpeech.stream("JBFqnCBsd6RMkjVDRZzb", {
        outputFormat: "mp3_44100_128",
    });
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="xi-api-key",
)

client.speech_to_speech.stream(
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    output_format="mp3_44100_128",
    audio="example_audio",
)

```

--------------------------------

### Get Tool - C# RestSharp

Source: https://elevenlabs.io/docs/api-reference/tools/get

Retrieve a tool using the RestSharp library for C#. Creates a GET request and executes it synchronously.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Widget (Go)

Source: https://elevenlabs.io/docs/api-reference/widget/get

Make an HTTP GET request to the ElevenLabs API to fetch the conversational AI agent's widget using Go's net/http package.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/widget"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### List MCP Server Tools in Swift

Source: https://elevenlabs.io/docs/api-reference/mcp/list-tools

This snippet demonstrates how to list tools for a given MCP server ID using `URLSession` in Swift. It constructs a GET request and handles the response asynchronously.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get User Subscription (Swift)

Source: https://elevenlabs.io/docs/api-reference/user/subscription/get

Make an HTTP GET request in Swift using URLSession to retrieve user subscription details.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/user/subscription")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get User Subscription (C# RestSharp)

Source: https://elevenlabs.io/docs/api-reference/user/subscription/get

Fetch user subscription information using RestSharp in C# with an HTTP GET request.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/user/subscription");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### POST /v1/music/plan

Source: https://elevenlabs.io/docs/api-reference/music/create-composition-plan

Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

```APIDOC
## POST /v1/music/plan

### Description
Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

### Method
POST

### Endpoint
https://api.elevenlabs.io/v1/music/plan
```

--------------------------------

### POST /v1/music/plan

Source: https://elevenlabs.io/docs/api-reference/music/create-composition-plan

Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

```APIDOC
## POST /v1/music/plan

### Description
Create a composition plan for music generation. Usage of this endpoint does not cost any credits but is subject to rate limiting depending on your tier.

### Method
POST

### Endpoint
/v1/music/plan

### Parameters
#### Header Parameters
- **xi-api-key** (string) - Optional - Your API key for authentication.

#### Request Body
- **prompt** (MusicPrompt object) - Required - The music prompt containing global styles and song sections.
  - **positive_global_styles** (array of string) - Required - The styles and musical directions that should be present in the entire song. Use English language for best result.
  - **negative_global_styles** (array of string) - Required - The styles and musical directions that should not be present in the entire song. Use English language for best result.
  - **sections** (array of SongSection objects) - Required - The sections of the song.
    - **section_name** (string) - Required - The name of the section. Must be between 1 and 100 characters.
    - **positive_local_styles** (array of string) - Required - The styles and musical directions that should be present in this section. Use English language for best result.
    - **negative_local_styles** (array of string) - Required - The styles and musical directions that should not be present in this section. Use English language for best result.
    - **duration_ms** (integer) - Required - The duration of the section in milliseconds. Must be between 3000ms and 120000ms.
    - **lines** (array of string) - Required - The lyrics of the section. Max 200 characters per line.
    - **source_from** (SectionSource object or null) - Optional - Optional source to extract the section from. Used for inpainting. Only available to enterprise clients with access to the inpainting feature.
      - **song_id** (string) - Required - The ID of the song to source the section from. You can find the song ID in the response headers when you generate a song.
      - **range** (TimeRange object) - Required - The range to extract from the source song.
        - **start_ms** (integer) - Required
        - **end_ms** (integer) - Required
      - **negative_ranges** (array of TimeRange objects) - Optional - The ranges to exclude from the 'range'.
- **model_id** (string) - Optional - The model to use for the generation. Default: "music_v1". Enum: ["music_v1"]

### Request Example
```json
{
  "prompt": {
    "positive_global_styles": [
      "upbeat",
      "electronic"
    ],
    "negative_global_styles": [
      "sad",
      "acoustic"
    ],
    "sections": [
      {
        "section_name": "Intro",
        "positive_local_styles": [
          "synthwave"
        ],
        "negative_local_styles": [],
        "duration_ms": 5000,
        "lines": [
          "Welcome to the future"
        ],
        "source_from": null
      },
      {
        "section_name": "Verse 1",
        "positive_local_styles": [
          "driving beat"
        ],
        "negative_local_styles": [
          "slow"
        ],
        "duration_ms": 10000,
        "lines": [
          "The rhythm takes control",
          "Let your spirit flow"
        ],
        "source_from": {
          "song_id": "some_song_id_123",
          "range": {
            "start_ms": 1000,
            "end_ms": 11000
          },
          "negative_ranges": [
            {
              "start_ms": 5000,
              "end_ms": 6000
            }
          ]
        }
      }
    ]
  },
  "model_id": "music_v1"
}
```

### Response
#### Success Response (200)
- **positive_global_styles** (array of string) - Required - The styles and musical directions that should be present in the entire song. Use English language for best result.
- **negative_global_styles** (array of string) - Required - The styles and musical directions that should not be present in the entire song. Use English language for best result.
- **sections** (array of SongSection objects) - Required - The sections of the song.
  - **section_name** (string) - Required - The name of the section. Must be between 1 and 100 characters.
  - **positive_local_styles** (array of string) - Required - The styles and musical directions that should be present in this section. Use English language for best result.
  - **negative_local_styles** (array of string) - Required - The styles and musical directions that should not be present in this section. Use English language for best result.
  - **duration_ms** (integer) - Required - The duration of the section in milliseconds. Must be between 3000ms and 120000ms.
  - **lines** (array of string) - Required - The lyrics of the section. Max 200 characters per line.
  - **source_from** (SectionSource object or null) - Optional - Optional source to extract the section from. Used for inpainting. Only available to enterprise clients with access to the inpainting feature.

#### Response Example
```json
{
  "positive_global_styles": [
    "upbeat",
    "electronic"
  ],
  "negative_global_styles": [
    "sad",
    "acoustic"
  ],
  "sections": [
    {
      "section_name": "Intro",
      "positive_local_styles": [
        "synthwave"
      ],
      "negative_local_styles": [],
      "duration_ms": 5000,
      "lines": [
        "Welcome to the future"
      ],
      "source_from": null
    }
  ]
}
```

#### Error Response (422) - Validation Error
- **detail** (array of object) - Details about the validation error.

#### Error Response Example (422)
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "prompt",
        "sections",
        0,
        "duration_ms"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```
```

--------------------------------

### Get Test Invocation (Swift URLSession)

Source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get

Retrieves a test invocation by sending a GET request using Swift's URLSession.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Test Invocation (Java Unirest)

Source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get

Retrieves a test invocation using a GET request with the Unirest HTTP client in Java.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id")
  .asString();
```

--------------------------------

### Video to Music with Python SDK

Source: https://elevenlabs.io/docs/api-reference/music/video-to-music

Use the ElevenLabs Python client to convert videos to music by passing a list of video files. Requires the elevenlabs package.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.music.video_to_music(
    videos=["example_videos"],
)
```

--------------------------------

### POST /v1/studio/projects - Create Studio Project

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

Creates a new Studio project with optional voice settings overrides, quality presets, and project metadata. Supports multiple source types and allows configuration of text normalization, target audience, and fiction classification.

```APIDOC
## POST /v1/studio/projects

### Description
Creates a new Studio project with configurable settings including voice overrides, quality presets, text normalization, and project metadata.

### Method
POST

### Endpoint
/v1/studio/projects

### Parameters
#### Request Body (multipart/form-data)
- **name** (string) - Required - The name of the Studio project
- **voice_settings** (array of JSON strings) - Optional - Voice settings overrides for the project
  - Example: `[{"voice_id": "21m00Tcm4TlvDq8ikWAM", "stability": 0.7, "similarity_boost": 0.8, "style": 0.5, "speed": 1.0, "use_speaker_boost": true}]`
- **quality_preset** (string) - Optional - Quality preset for audio output. Enum: `standard`, `high`, `ultra`, `ultra_lossless`. Default: `standard`
- **target_audience** (string) - Optional - Target audience of the project. Enum: `children`, `young adult`, `adult`, `all ages`
- **fiction** (string) - Optional - Whether the content is fiction. Enum: `fiction`, `non-fiction`
- **apply_text_normalization** (string) - Optional - Text normalization mode. Enum: `auto`, `on`, `off`, `apply_english`. Default: `auto`
  - `auto`: System automatically decides whether to apply text normalization
  - `on`: Text normalization always applied
  - `off`: Text normalization skipped
  - `apply_english`: Same as `on` but assumes English text
- **source_type** (string) - Optional - Type of Studio project. Enum: `blank`, `book`, `article`, `genfm`, `video`, `screenplay`
- **create_publishing_read** (boolean) - Optional - If true, creates a corresponding read for direct publishing in draft state. Default: `false`

### Request Example
```json
{
  "name": "My Audio Project",
  "source_type": "article",
  "quality_preset": "high",
  "target_audience": "adult",
  "fiction": "non-fiction",
  "apply_text_normalization": "auto",
  "voice_settings": ["{\"voice_id\": \"21m00Tcm4TlvDq8ikWAM\", \"stability\": 0.7, \"similarity_boost\": 0.8, \"style\": 0.5, \"speed\": 1.0, \"use_speaker_boost\": true}"]
}
```

### Response
#### Success Response (200)
- **creation_progress** (number) - The progress of the project creation (0-100)
- **status** (string) - The status of the project creation action. Enum: `pending`, `creating`, `finished`, `failed`
- **type** (string) - The type of the project creation action. Enum: `blank`, `generate_podcast`, `auto_assign_voices`, `dub_video`, `import_speech`

#### Response Example
```json
{
  "creation_progress": 0.0,
  "status": "pending",
  "type": "blank"
}
```

### Servers
- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io
```

--------------------------------

### GET /v1/studio/projects/{project_id}

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

Returns information about a specific Studio project. This endpoint returns more detailed information about a project than GET /v1/studio.

```APIDOC
## GET /v1/studio/projects/{project_id}

### Description
Returns information about a specific Studio project. This endpoint returns more detailed information about a project than GET /v1/studio.

### Method
GET

### Endpoint
/v1/studio/projects/{project_id}

### Parameters
#### Path Parameters
- **project_id** (string) - Required - The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

#### Query Parameters
- **share_id** (string) - Optional - The share ID of the project

#### Header Parameters
- **xi-api-key** (string) - Optional

### Response
#### Success Response (200)
- **Schema**: ProjectExtendedResponseModel

#### Error Response (422)
- **Schema**: HTTPValidationError
```

--------------------------------

### GET /v1/studio/projects/{project_id}

Source: https://elevenlabs.io/docs/api-reference/studio/get-project

Returns information about a specific Studio project. This endpoint returns more detailed information about a project than GET /v1/studio.

```APIDOC
## GET /v1/studio/projects/{project_id}

### Description
Returns information about a specific Studio project. This endpoint returns more detailed information about a project than `GET /v1/studio`.

### Method
GET

### Endpoint
/v1/studio/projects/{project_id}

### Parameters
#### Path Parameters
- **project_id** (string) - Required - The unique identifier of the Studio project to retrieve.
```

--------------------------------

### Example LLM request with system tools

Source: https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm

Complete OpenAI format request showing how a custom LLM receives system tools including end_call, language_detection, and skip_turn. The model must support function calling to use these tools.

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant. You have access to system tools for managing conversations."
    },
    {
      "role": "user",
      "content": "I think we're done here, thanks for your help!"
    }
  ],
  "model": "your-custom-model",
  "temperature": 0.7,
  "max_tokens": 1000,
  "stream": true,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "end_call",
        "description": "Call this function to end the current conversation when the main task has been completed...",
        "parameters": {
          "type": "object",
          "properties": {
            "reason": {
              "type": "string",
              "description": "The reason for the tool call."
            },
            "message": {
              "type": "string",
              "description": "A farewell message to send to the user along right before ending the call."
            }
          },
          "required": ["reason"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "language_detection",
        "description": "Change the conversation language when the user expresses a language preference explicitly...",
        "parameters": {
          "type": "object",
          "properties": {
            "reason": {
              "type": "string",
              "description": "The reason for the tool call."
            },
            "language": {
              "type": "string",
              "description": "The language to switch to. Must be one of language codes in tool description."
            }
          },
          "required": ["reason", "language"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "skip_turn",
        "description": "Skip a turn when the user explicitly indicates they need a moment to think...",
        "parameters": {
          "type": "object",
          "properties": {
            "reason": {
              "type": "string",
              "description": "Optional free-form reason explaining why the pause is needed."
            }
          },
          "required": []
        }
      }
    }
  ]
}
```

--------------------------------

### Get Summaries (PHP Guzzle)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-summaries

Use the Guzzle HTTP client in PHP to make an HTTP GET request for document summaries.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/summaries?document_ids=%5B%22string%22%5D');

echo $response->getBody();
```

--------------------------------

### Realtime Speech-to-Text with Manual Audio Chunking (Python SDK)

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming

This example demonstrates how to simulate a realtime transcription of an audio file by manually chunking audio and sending it via the ElevenLabs Python SDK. It uses the WebSocket API under the hood with CommitStrategy.MANUAL.

```python
import asyncio
import base64
import os
from dotenv import load_dotenv
from pathlib import Path
from elevenlabs import AudioFormat, CommitStrategy, ElevenLabs, RealtimeEvents, RealtimeAudioOptions
from pydub import AudioSegment
import sys

load_dotenv()

async def main():
    # Initialize the ElevenLabs client
    elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    # Create an event to signal when transcription is complete
    transcription_complete = asyncio.Event()

    # Connect with manual audio chunk mode
    connection = await elevenlabs.speech_to_text.realtime.connect(RealtimeAudioOptions(
        model_id="scribe_v2_realtime",
        audio_format=AudioFormat.PCM_16000,
        sample_rate=16000,
        commit_strategy=CommitStrategy.MANUAL,
        include_timestamps=True,
    ))

    # Set up event handlers
    def on_session_started(data):
        print(f"Session started: {data}")
        # Start sending audio once session is ready
        asyncio.create_task(send_audio())

    def on_partial_transcript(data):
        transcript = data.get('text', '')
        if transcript:
            print(f"Partial: {transcript}")

    def on_committed_transcript(data):
        transcript = data.get('text', '')
        print(f"\nCommitted transcript: {transcript}")

    def on_committed_transcript_with_timestamps(data):
        print(f"Timestamps: {data.get('words', '')}")
        print("-" * 50)
        # Signal that transcription is complete
        transcription_complete.set()

    def on_error(error):
        print(f"Error: {error}")
        transcription_complete.set()

    def on_close():
        print("Connection closed")
        transcription_complete.set()

    # Register event handlers
    connection.on(RealtimeEvents.SESSION_STARTED, on_session_started)
    connection.on(RealtimeEvents.PARTIAL_TRANSCRIPT, on_partial_transcript)
    connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT, on_committed_transcript)
    connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT_WITH_TIMESTAMPS, on_committed_transcript_with_timestamps)
    connection.on(RealtimeEvents.ERROR, on_error)
    connection.on(RealtimeEvents.CLOSE, on_close)

    # Convert audio file to PCM format if necessary
    def load_and_convert_audio(audio_path: str | Path, target_sample_rate: int = 16000) -> bytes:
        try:
            if str(audio_path).lower().endswith('.pcm'):
                with open(audio_path, 'rb') as f:
                    return f.read()

            audio = AudioSegment.from_file(audio_path)
            if audio.channels > 1:
                audio = audio.set_channels(1)
            if audio.frame_rate != target_sample_rate:
                audio = audio.set_frame_rate(target_sample_rate)
            audio = audio.set_sample_width(2)
            return audio.raw_data
        except Exception as e:
            print(f"Error loading audio: {e}")
            sys.exit(1)

    async def send_audio():
        """Send audio chunks from an audio file"""
        audio_file_path = Path("/path/to/audio.mp3")

        try:
            # Read the audio file
            audio_data = load_and_convert_audio(audio_file_path)

            # Split into chunks (1 second of audio = 32000 bytes at 16kHz, 16-bit)
            chunk_size = 32000
            chunks = [audio_data[i:i + chunk_size] for i in range(0, len(audio_data), chunk_size)]

            # Send each chunk
            for i, chunk in enumerate(chunks):
                chunk_base64 = base64.b64encode(chunk).decode('utf-8')
                await connection.send({"audio_base_64": chunk_base64, "sample_rate": 16000})

                # Wait 1 second between chunks (simulating real-time)

```

--------------------------------

### Video to Music with TypeScript SDK

Source: https://elevenlabs.io/docs/api-reference/music/video-to-music

Initialize the ElevenLabsClient and call the video_to_music method with video files. Requires the @elevenlabs/elevenlabs-js package.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.music.videoToMusic({});
}
main();
```

--------------------------------

### Get Knowledge Base Document (Ruby)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-document

Make an HTTP GET request in Ruby to retrieve a document from a knowledge base by its ID.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Project Snapshot with Swift HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

Use Swift's Foundation URLSession to make a GET request to the ElevenLabs API. Configure an NSMutableURLRequest with the endpoint URL and execute the data task asynchronously.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### GET /v1/studio/projects

Source: https://elevenlabs.io/docs/api-reference/studio/get-projects

Returns a list of your Studio projects with metadata.

```APIDOC
## GET /v1/studio/projects

### Description
Returns a list of your Studio projects with metadata.

### Method
GET

### Endpoint
/v1/studio/projects

### Parameters
#### Headers
- **xi-api-key** (string) - Optional - Your API key.

### Response
#### Success Response (200)
- **GetProjectsResponseModel** (object) - Successful Response.

#### Error Response (422)
- **HTTPValidationError** (object) - Validation Error.
```

--------------------------------

### Get Knowledge Base Document (Go)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-document

Make an HTTP GET request in Go to retrieve a document from a knowledge base by its ID.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Test Folder - Go HTTP

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tests/test-folders/create

Create a test folder using Go's standard net/http library. Sends a POST request with JSON payload to the agent-testing/folders endpoint.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agent-testing/folders"

	payload := strings.NewReader("{\n  \"name\": \"Agent Test Suite\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### GET /v1/convai/knowledge-base/{documentation_id}/source-file-url

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-source-file-url

Get a signed URL to download the original source file of a file-type document from the knowledge base.

```APIDOC
## GET /v1/convai/knowledge-base/{documentation_id}/source-file-url

### Description
Get a signed URL to download the original source file of a file-type document from the knowledge base

### Method
GET

### Endpoint
/v1/convai/knowledge-base/{documentation_id}/source-file-url

### Parameters
#### Path Parameters
- **documentation_id** (string) - Required - The id of a document from the knowledge base. This is returned on document addition.

#### Header Parameters
- **xi-api-key** (string) - Optional - API key for authentication.

### Response
#### Success Response (200)
- **signed_url** (string) - Signed URL to download the source file directly

#### Response Example
```json
{
  "signed_url": "https://example.com/signed-url-to-file"
}
```

#### Error Response (422)
- **detail** (array of objects) - Validation error details.

#### Error Response Example (422)
```json
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```
```

--------------------------------

### Get Dubbing in PHP

Source: https://elevenlabs.io/docs/api-reference/dubbing/get

Utilize Guzzle HTTP client to make a GET request to the dubbing endpoint and echo the response body.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing/dubbing_id');

echo $response->getBody();
```

--------------------------------

### Get Dubbing in Ruby

Source: https://elevenlabs.io/docs/api-reference/dubbing/get

Perform a GET request to the dubbing API endpoint using Ruby's Net::HTTP library.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/dubbing/dubbing_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Dubbing in Go

Source: https://elevenlabs.io/docs/api-reference/dubbing/get

Make a GET request to the dubbing endpoint using the standard net/http package to retrieve dubbing details.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/dubbing/dubbing_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### GET /v1/history/{history_item_id}

Source: https://elevenlabs.io/docs/api-reference/history/get

Retrieves a history item. You can use the Get generated items endpoint to retrieve a list of history items.

```APIDOC
## GET /v1/history/{history_item_id}

### Description
Retrieves a history item. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

### Method
GET

### Endpoint
/v1/history/{history_item_id}

### Parameters
#### Path Parameters
- **history_item_id** (string) - Required - ID of the history item to be used. You can use the [Get generated items](/docs/api-reference/history/list) endpoint to retrieve a list of history items.

### Request Example
{}

### Response
#### Success Response (200)
- **Schema**: SpeechHistoryItemResponseModel

#### Response Example
{
  "// Note": "Response structure depends on SpeechHistoryItemResponseModel schema"
}

#### Error Response (422)
- **Schema**: HTTPValidationError
```

--------------------------------

### Run Conversational AI Agent Tests (Go)

Source: https://elevenlabs.io/docs/api-reference/tests/run-tests

Make a direct HTTP POST request in Go to run tests on a conversational AI agent.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/agent_id/run-tests"

	payload := strings.NewReader("{\n  \"tests\": [\n    {\n      \"test_id\": \"string\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Connect to WebSocket with Environment Parameter

Source: https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables

Establish a WebSocket connection to an ElevenLabs Agent, specifying the desired environment using a query parameter.

```text
wss://api.elevenlabs.io/v1/convai/conversation?agent_id=<agent_id>&environment=staging
```

--------------------------------

### Create Knowledge Base Document from URL - Python SDK

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-url

Use the ElevenLabs Python SDK to create a knowledge base document from a URL. Requires the elevenlabs package.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.documents.create_from_url(
    url="string",
)
```

--------------------------------

### List Chapter Snapshots using Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/get-chapter-snapshots

This snippet demonstrates how to retrieve a list of chapter snapshots for a specific project and chapter using Go's standard HTTP client.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/chapters/chapter_id/snapshots"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Start Conversation with Dynamic Variables (Python)

Source: https://elevenlabs.io/docs/eleven-agents/customization/personalization/dynamic-variables

This snippet shows how to initialize an ElevenLabs Conversation object with dynamic variables and custom callbacks, then start a session. It requires AGENT_ID and ELEVENLABS_API_KEY environment variables.

```python
import os
import signal
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

agent_id = os.getenv("AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(api_key=api_key)

dynamic_vars = {
    "user_name": "Angelo",
}

config = ConversationInitiationData(
    dynamic_variables=dynamic_vars
)

conversation = Conversation(
    elevenlabs,
    agent_id,
    config=config,
    # Assume auth is required when API_KEY is set.
    requires_auth=bool(api_key),
    # Use the default audio interface.
    audio_interface=DefaultAudioInterface(),
    # Simple callbacks that print the conversation to the console.
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"User: {transcript}"),
    # Uncomment the below if you want to see latency measurements.
    # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
)

conversation.start_session()

signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())
```

--------------------------------

### Run the ElevenLabs Vonage connector

Source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/telephony/vonage

Start the Node.js connector application to enable the bridge between Vonage and ElevenLabs Agents.

```bash
node elevenlabs-agent-ws-connector.cjs
```

--------------------------------

### Create PVC samples with Go HTTP client

Source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/create

Make a POST request to the ElevenLabs API using Go's net/http package with multipart form-data encoding.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/voices/pvc/voice_id/samples"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"files\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"remove_background_noise\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### WebSocket conversation agent demo - JavaScript

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket

Complete example demonstrating a conversation agent with context management, user interruptions, and multi-turn interactions. Requires ELEVENLABS_API_KEY environment variable and establishes WebSocket connection with proper headers and payload limits.

```javascript
async function conversationAgentDemo() {
  // Connect to WebSocket with API key in headers
  const websocket = new WebSocket(WEBSOCKET_URI, {
    headers: {
      'xi-api-key': ELEVENLABS_API_KEY,
    },
    maxPayload: 16 * 1024 * 1024,
  });

  // Set up event handlers
  websocket.on('open', () => {
    // Initial agent response
    sendTextInContext(
      websocket,
      "Hello! I'm your virtual assistant. I can help you with a wide range of topics. What would you like to know about today?",
      'greeting'
    );

    // Simulate wait time (user listening)
    setTimeout(() => {
      // Simulate user interruption
      console.log("USER INTERRUPTS: 'Can you tell me about the weather?'");

      // Handle the interruption
      handleInterruption(
        websocket,
        'greeting',
        'weather_response',
        "I'd be happy to tell you about the weather. Currently in your area, it's 72 degrees and sunny with a slight chance of rain later this afternoon."
      );

      // Add more to the weather context
      setTimeout(() => {
        continueContext(
          websocket,
          " If you're planning to go outside, you might want to bring a light jacket just in case.",
          'weather_response'
        );

        // Flush at the end of this turn
        flushContext(websocket, 'weather_response');

        // Simulate wait time (user listening)
        setTimeout(() => {
          // Simulate user asking another question
          console.log("USER: 'What about tomorrow?'");

          // Create a new context for this response
          sendTextInContext(
            websocket,
            "Tomorrow's forecast shows temperatures around 75 degrees with partly cloudy skies. It should be a beautiful day overall!",
            'tomorrow_weather'
          );

          // Flush and close this context
          flushContext(websocket, 'tomorrow_weather');
          websocket.send(
            JSON.stringify({
              context_id: 'tomorrow_weather',
              close_context: true,
            })
          );

          // End the conversation
          setTimeout(() => {
            endConversation(websocket);
          }, 2000);
        }, 3000);
      }, 500);
    }, 2000);
  });

  // Handle incoming messages
  websocket.on('message', (message) => {
    try {
      const data = JSON.parse(message);
```

--------------------------------

### Get Secret Dependencies in Swift

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/get-dependencies

This snippet demonstrates how to make a GET request to retrieve the dependencies for a specific secret using URLSession in Swift.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Agent using ElevenLabs client (Python)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/create

Initializes the ElevenLabs client and creates a new conversational AI agent with default settings.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.create()

```

--------------------------------

### List MCP Server Tools in Python

Source: https://elevenlabs.io/docs/api-reference/mcp/list-tools

This snippet demonstrates how to list tools for a given MCP server ID using the ElevenLabs Python SDK. It initializes the client and calls the `list` method.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tools.list(
    mcp_server_id="mcp_server_id",
)

```

--------------------------------

### Get Secret Dependencies in C#

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/workspace/secrets/get-dependencies

This snippet demonstrates how to make a GET request to retrieve the dependencies for a specific secret using RestSharp in C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Stream Audio from URL with ElevenLabs SDK

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/server-side-streaming

This example demonstrates how to stream an audio file from a URL using the official SDK. The 'ffmpeg' tool is required for URL streaming.

```python
from dotenv import load_dotenv
import os
import asyncio
from elevenlabs import ElevenLabs, RealtimeEvents, RealtimeUrlOptions

load_dotenv()

async def main():
    elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    # Create an event to signal when to stop
    stop_event = asyncio.Event()

    # Connect to a streaming audio URL
    connection = await elevenlabs.speech_to_text.realtime.connect(RealtimeUrlOptions(
        model_id="scribe_v2_realtime",
        url="https://npr-ice.streamguys1.com/live.mp3",
        include_timestamps=True,
    ))

    # Set up event handlers
    def on_session_started(data):
        print(f"Session started: {data}")

    def on_partial_transcript(data):
        print(f"Partial: {data.get('text', '')}")

    def on_committed_transcript(data):
        print(f"Committed: {data.get('text', '')}")

    # Committed transcripts with word-level timestamps. Only received when include_timestamps is set to True.
    def on_committed_transcript_with_timestamps(data):
        print(f"Committed with timestamps: {data.get('words', '')}")

    # Errors - will catch all errors, both server and websocket specific errors
    def on_error(error):
        print(f"Error: {error}")
        # Signal to stop on error
        stop_event.set()

    def on_close():
        print("Connection closed")

    # Register event handlers
    connection.on(RealtimeEvents.SESSION_STARTED, on_session_started)
    connection.on(RealtimeEvents.PARTIAL_TRANSCRIPT, on_partial_transcript)
    connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT, on_committed_transcript)
    connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT_WITH_TIMESTAMPS, on_committed_transcript_with_timestamps)
    connection.on(RealtimeEvents.ERROR, on_error)
    connection.on(RealtimeEvents.CLOSE, on_close)

    print("Transcribing audio stream... (Press Ctrl+C to stop)")

    try:
        # Wait until error occurs or connection closes
        await stop_event.wait()
    except KeyboardInterrupt:
        print("\nStopping transcription...")
    finally:
        await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
```

```typescript
import "dotenv/config";
import { ElevenLabsClient, RealtimeEvents } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

const connection = await elevenlabs.speechToText.realtime.connect({
  modelId: "scribe_v2_realtime",
  url: "https://npr-ice.streamguys1.com/live.mp3",
  includeTimestamps: true,
});

connection.on(RealtimeEvents.SESSION_STARTED, (data) => {
  console.log("Session started", data);
});

connection.on(RealtimeEvents.PARTIAL_TRANSCRIPT, (transcript) => {
  console.log("Partial transcript", transcript);
});

connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT, (transcript) => {
  console.log("Committed transcript", transcript);
});

connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT_WITH_TIMESTAMPS, (transcript) => {
  console.log("Committed with timestamps", transcript);
});

connection.on(RealtimeEvents.ERROR, (error) => {
  console.log("Error", error);
});

connection.on(RealtimeEvents.CLOSE, () => {
  console.log("Connection closed");
});
```

--------------------------------

### Get Knowledge Base Document Content in Go

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/get-content

Make a GET request to the ElevenLabs API to fetch knowledge base document content.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/content"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Conversation Tag (Swift)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/tags/get

Make a GET request to the ElevenLabs API to retrieve a conversation tag using Swift's URLSession.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tags/tag_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Conversation Tag (C# RestSharp)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/tags/get

Fetch a conversation tag from the ElevenLabs API using a GET request with the RestSharp library in C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tags/tag_id");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Conversation in Ruby

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/get

Make a GET request to the ElevenLabs API to retrieve a conversation using Ruby's Net::HTTP library.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/conversations/123")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["xi-api-key"] = 'xi-api-key'

response = http.request(request)
puts response.read_body
```

--------------------------------

### Connect to Scribe and Log Transcriptions

Source: https://elevenlabs.io/docs/eleven-api/resources/libraries/javascript-scribe

A minimal example demonstrating how to connect to Scribe, listen for partial and committed transcripts, and close the connection.

```js
import { Scribe, RealtimeEvents } from '@elevenlabs/client';

const token = await fetchTokenFromServer();

const connection = Scribe.connect({
  token,
  modelId: 'scribe_v2_realtime',
  microphone: {
    echoCancellation: true,
    noiseSuppression: true,
  },
});

connection.on(RealtimeEvents.PARTIAL_TRANSCRIPT, (data) => {
  console.log('Partial:', data.text);
});

connection.on(RealtimeEvents.COMMITTED_TRANSCRIPT, (data) => {
  console.log('Committed:', data.text);
});

// Later, close the connection
connection.close();
```

--------------------------------

### Create Agent Deployment with Swift URLRequest

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/deployments/create

Uses Swift's Foundation framework to construct a URLRequest for the ElevenLabs API. Requires manual JSON serialization.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["deployment_request": ["requests": [
      [
        "branch_id": "agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        "deployment_strategy": [
          "traffic_percentage": 0.5,
          "type": "percentage"
        ]
      ]
    ]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/deployments")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
```

--------------------------------

### Get a Batch Call (Java Unirest)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get

Shows how to perform a GET request for a batch call using the Unirest HTTP client in Java.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/batch-calling/batch_id")
  .asString();
```

--------------------------------

### Create Conversational Agent in Python

Source: https://elevenlabs.io/docs/eleven-agents/quickstart

Initialize the ElevenLabs client with API key from environment, define a system prompt for customer support, and create a voice agent with TTS and conversation configuration.

```python
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import os
load_dotenv()

elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)

prompt = """
You are a friendly and efficient virtual assistant for [Your Company Name].
Your role is to assist customers by answering questions about the company's products, services,
and documentation. You should use the provided knowledge base to offer accurate and helpful responses.

Tasks:
- Answer Questions: Provide clear and concise answers based on the available information.
- Clarify Unclear Requests: Politely ask for more details if the customer's question is not clear.

Guidelines:
- Maintain a friendly and professional tone throughout the conversation.
- Be patient and attentive to the customer's needs.
- If unsure about any information, politely ask the customer to repeat or clarify.
- Avoid discussing topics unrelated to the company's products or services.
- Aim to provide concise answers. Limit responses to a couple of sentences and let the user guide you on where to provide more detail.
"""

response = elevenlabs.conversational_ai.agents.create(
    name="My voice agent",
    tags=["test"], # List of tags to help classify and filter the agent
    conversation_config={
        "tts": {
            "voice_id": "aMSt68OGf4xUZAnLpTU8",
            "model_id": "eleven_flash_v2"
        },
        "agent": {
            "first_message": "Hi, this is Rachel from [Your Company Name] support. How can I help you today?",
            "prompt": {
                "prompt": prompt,
            }
        }
    }
)

print("Agent created with ID:", response.agent_id)
```

--------------------------------

### Generate and Modify Composition Plan from Prompt

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans

Create a composition plan from a natural language prompt, then programmatically modify its sections before using it to generate music.

```python
plan = elevenlabs.music.composition_plan.create(
    prompt="An upbeat pop song about summer adventures",
    music_length_ms=60000
)

# Modify the generated plan
plan["sections"][0]["lines"] = ["Custom lyrics here"]

audio = elevenlabs.music.compose(composition_plan=plan)
```

```typescript
const plan = await elevenlabs.music.compositionPlan.create({
  prompt: 'An upbeat pop song about summer adventures',
  musicLengthMs: 60000,
});

// Modify the generated plan
plan.sections[0].lines = ['Custom lyrics here'];

const audio = await elevenlabs.music.compose({ compositionPlan: plan });
```

--------------------------------

### Get Agent Summaries (Ruby)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/get-summaries

Make a direct HTTP GET request in Ruby to retrieve summaries for specified conversational AI agents.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22J3Pbu5gP6NNKBscdCdwB%22%2C%22K4Qcu6hQ7OOLCtdeDeXC%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### List Environment Variables in Go

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list

Make a direct HTTP GET request to the ElevenLabs API endpoint to list environment variables.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/environment-variables"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### List service accounts with Python SDK

Source: https://elevenlabs.io/docs/api-reference/service-accounts/list

Use the ElevenLabs Python SDK to list all service accounts. Initialize the client and call the list method on service_accounts.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.service_accounts.list()
```

--------------------------------

### GET /v1/workspace/resources/{resource_id} (Get resource) - Updated

Source: https://elevenlabs.io/docs/changelog/2026/2/9

Retrieve workspace resource details. Updated to support content templates as a resource type.

```APIDOC
## GET /v1/workspace/resources/{resource_id} (Get resource)

### Description
Retrieve workspace resource details with expanded resource type support.

### Updates
- Added `content_templates` to `WorkspaceResourceType` enum
```

--------------------------------

### Get Secret Dependencies - Swift HTTP

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

Make a GET request to the secrets dependencies endpoint using Swift's URLSession API.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### List dubs with ElevenLabs SDK - Python

Source: https://elevenlabs.io/docs/api-reference/dubbing/list

Initialize the ElevenLabs client and call the dubbing.list() method to retrieve all dubbing projects.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.dubbing.list()
```

--------------------------------

### Get Secret Dependencies - PHP HTTP

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

Make a GET request to the secrets dependencies endpoint using the Guzzle HTTP client for PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools');

echo $response->getBody();
```

--------------------------------

### Agent System Prompt with Dynamic Variables

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/expo-react-native

System prompt template that instructs the agent on available tools and behavior. Includes {{platform}} dynamic variable and references the three client tools: getBatteryLevel, changeBrightness, and flashScreen.

```text
You are a helpful assistant running on {{platform}}. You have access to certain tools that allow you to check the user device battery level and change the display brightness. Use these tools if the user asks about them. Otherwise, just answer the question.
```

--------------------------------

### Upload Music via Direct HTTP POST Request

Source: https://elevenlabs.io/docs/api-reference/music/upload

These examples show how to perform a direct HTTP POST request to the /v1/music/upload endpoint. The request body must be formatted as multipart/form-data.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/music/upload"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/music/upload")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/music/upload")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/music/upload', [
  'multipart' => [
    [
        'name' => 'file',
        'filename' => 'string',
        'contents' => null
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/music/upload");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"string\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"extract_composition_plan\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "file",
    "fileName": "string"
  ],
  [
    "name": "extract_composition_plan",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\"
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/music/upload")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Widget (C#)

Source: https://elevenlabs.io/docs/api-reference/widget/get

Utilize RestSharp in C# to execute an HTTP GET request and obtain the conversational AI agent's widget.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/widget");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Widget (PHP)

Source: https://elevenlabs.io/docs/api-reference/widget/get

Fetch the conversational AI agent's widget using Guzzle HTTP client in PHP with a GET request.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/agent_id/widget');

echo $response->getBody();
```

--------------------------------

### Create PVC samples with Python SDK

Source: https://elevenlabs.io/docs/api-reference/voices/pvc/samples/create

Use the ElevenLabs Python SDK to create voice samples. Pass files as a list and specify the voice_id.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.voices.pvc.samples.create(
    voice_id="voice_id",
    files=["example_files"],
)
```

--------------------------------

### Transcribing Audio Files with useScribe

Source: https://elevenlabs.io/docs/eleven-api/resources/libraries/react-scribe

This example illustrates how to transcribe pre-recorded audio files using `useScribe`. It includes steps for decoding the audio, converting it to PCM16 format, and sending it in chunks for transcription.

```tsx
import { useScribe, AudioFormat } from '@elevenlabs/react';
import { useState } from 'react';

function FileTranscription() {
  const [file, setFile] = useState<File | null>(null);
  const scribe = useScribe({
    modelId: 'scribe_v2_realtime',
    audioFormat: AudioFormat.PCM_16000,
    sampleRate: 16000,
  });

  const transcribeFile = async () => {
    if (!file) return;

    const token = await fetchToken();
    await scribe.connect({ token });

    // Decode audio file
    const arrayBuffer = await file.arrayBuffer();
    const audioContext = new AudioContext({ sampleRate: 16000 });
    const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);

    // Convert to PCM16
    const channelData = audioBuffer.getChannelData(0);
    const pcmData = new Int16Array(channelData.length);

    for (let i = 0; i < channelData.length; i++) {
      const sample = Math.max(-1, Math.min(1, channelData[i]));
      pcmData[i] = sample < 0 ? sample * 32768 : sample * 32767;
    }

    // Send in chunks
    const chunkSize = 4096;
    for (let offset = 0; offset < pcmData.length; offset += chunkSize) {
      const chunk = pcmData.slice(offset, offset + chunkSize);
      const bytes = new Uint8Array(chunk.buffer);
      const base64 = btoa(String.fromCharCode(...bytes));

      scribe.sendAudio(base64);
      await new Promise((resolve) => setTimeout(resolve, 50));
    }

    // Commit transcription
    scribe.commit();
  };

  return (
    <div>
      <input type="file" accept="audio/*" onChange={(e) => setFile(e.target.files?.[0] || null)} />
      <button onClick={transcribeFile} disabled={!file || scribe.isConnected}>
        Transcribe
      </button>

      {scribe.committedTranscripts.map((transcript) => (
        <div key={transcript.id}>{transcript.text}</div>
      ))}
    </div>
  );
}
```

--------------------------------

### Get User Subscription (PHP Guzzle)

Source: https://elevenlabs.io/docs/api-reference/user/subscription/get

Utilize Guzzle HTTP client in PHP to send a GET request for user subscription details.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/user/subscription');

echo $response->getBody();
```

--------------------------------

### Create a seamless loop with a glue section

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/music/inpainting

Define a loop plan using `source_from` to reuse parts of the original song. A 'Glue' section is included for a smooth transition between loop points.

```python
loop_plan = {
    "positive_global_styles": [],
    "negative_global_styles": [],
    "sections": [
        {
            "section_name": "Loop Start",
            "positive_local_styles": [],
            "negative_local_styles": [],
            "duration_ms": 5000,
            "source_from": {
                "song_id": song_id,
                "range": {"start_ms": 3000, "end_ms": 8000}
            },
            "lines": []
        },
        {
            # Glue section - model generates a smooth transition
            "section_name": "Glue",
            "positive_local_styles": [],
            "negative_local_styles": [],
            "duration_ms": 3000,
            "lines": []
        },
        {
            "section_name": "Loop End",
            "positive_local_styles": [],
            "negative_local_styles": [],
            "duration_ms": 5000,
            "source_from": {
                "song_id": song_id,
                "range": {"start_ms": 3000, "end_ms": 8000}
            },
            "lines": []
        }
    ]
}

audio = elevenlabs.music.compose(composition_plan=loop_plan)
```

```typescript
const loopPlan = {
  positiveGlobalStyles: [],
  negativeGlobalStyles: [],
  sections: [
    {
      sectionName: 'Loop Start',
      positiveLocalStyles: [],
      negativeLocalStyles: [],
      durationMs: 5000,
      sourceFrom: {
        songId,
        range: { startMs: 3000, endMs: 8000 },
      },
      lines: [],
    },
    {
      // Glue section - model generates a smooth transition
      sectionName: 'Glue',
      positiveLocalStyles: [],
      negativeLocalStyles: [],
      durationMs: 3000,
      lines: [],
    },
    {
      sectionName: 'Loop End',
      positiveLocalStyles: [],
      negativeLocalStyles: [],
      durationMs: 5000,
      sourceFrom: {
        songId,
        range: { startMs: 3000, endMs: 8000 },
      },
      lines: [],
    },
  ],
};

const audio = await elevenlabs.music.compose({ compositionPlan: loopPlan });
```

--------------------------------

### Get User Subscription (Java Unirest)

Source: https://elevenlabs.io/docs/api-reference/user/subscription/get

Use the Unirest library in Java to make an HTTP GET request for user subscription data.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/user/subscription")
  .asString();
```

--------------------------------

### Get Dependent Agents in C# with RestSharp

Source: https://elevenlabs.io/docs/api-reference/tools/get-dependent-agents

Employ RestSharp in C# to make a GET request to the ElevenLabs API for retrieving dependent agents.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Approval Policy (Go)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/approval-policies/create

Make a POST request to the ElevenLabs API using Go's "net/http" package to create a tool approval policy. Set the "Content-Type" header and provide the "tool_name" and "tool_description" in the request body.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-approvals"

	payload := strings.NewReader("{\n  \"tool_name\": \"string\",\n  \"tool_description\": \"string\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Dependent Agents in Ruby

Source: https://elevenlabs.io/docs/api-reference/tools/get-dependent-agents

Perform an HTTP GET request in Ruby to the ElevenLabs API to retrieve agents dependent on a specific tool.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Test Invocation (PHP Guzzle)

Source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get

Performs a GET request to retrieve a test invocation using the Guzzle HTTP client in PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id');

echo $response->getBody();
```

--------------------------------

### List Project Snapshots Across SDKs and Languages

Source: https://elevenlabs.io/docs/api-reference/studio/get-snapshots

These examples demonstrate how to list project snapshots using the ElevenLabs API in different programming languages. Replace 'project_id' with your actual project identifier.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.snapshots.list("project_id");
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.snapshots.list(
    project_id="project_id",
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Get Environment Variable (Ruby)

Source: https://elevenlabs.io/docs/api-reference/environment-variables/get

Perform an HTTP GET request in Ruby to fetch an environment variable. The response body is printed to the console.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Document RAG Indexes - Java HTTP Client

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-rag-index

Uses the Unirest library to make a GET request. Requires the com.mashape.unirest dependency.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index")
  .asString();
```

--------------------------------

### Get Topics - C# HTTP Request

Source: https://elevenlabs.io/docs/api-reference/conversations/topics/get

Retrieve conversation topics using RestSharp for C#. Constructs a GET request and executes it synchronously.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/agent_id/topics");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Create Tool with Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/tools/create

Make a POST request to the ElevenLabs API using Go's net/http package. Requires manual JSON payload construction and proper header configuration.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/tools"

	payload := strings.NewReader("{\n  \"tool_config\": {\n    \"type\": \"system\",\n    \"name\": \"end_call\",\n    \"params\": {\n      \"system_tool_type\": \"end_call\"\n    },\n    \"description\": \"\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Studio Project with Go HTTP Request

Source: https://elevenlabs.io/docs/api-reference/studio/add-project

Make a POST request to the ElevenLabs API endpoint using Go's net/http package with multipart form-data encoding. Requires proper boundary formatting for the multipart payload.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Conversation Tag - Python

Source: https://elevenlabs.io/docs/api-reference/conversations/tags/get

Retrieve a conversation tag using the ElevenLabs Python SDK. Pass the tag_id parameter to the get method.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.conversations.tags.get(
    tag_id="tag_id",
)
```

--------------------------------

### Set ElevenLabs API key in environment variables

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming-and-caching-with-supabase

Create a `.env` file within the `supabase/functions` directory and add your ElevenLabs API key to it.

```env
# Find / create an API key at https://elevenlabs.io/app/settings/api-keys
ELEVENLABS_API_KEY=your_api_key
```

--------------------------------

### List dubs with HTTP GET request - PHP

Source: https://elevenlabs.io/docs/api-reference/dubbing/list

Make a raw HTTP GET request using the Guzzle HTTP client library.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/dubbing');

echo $response->getBody();
```

--------------------------------

### Connect to Realtime STT with Keyterm Prompting via SDK

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/batch/keyterm-prompting

Connects to the ElevenLabs realtime Speech to Text API using the SDK, specifying a model ID and a list of keyterms for enhanced prompting.

```Python
connection = await elevenlabs.speech_to_text.realtime.connect(RealtimeUrlOptions(
    model_id="scribe_v2_realtime",
    keyterms=["ElevenLabs"],
))
```

```TypeScript
const connection = await elevenlabs.speechToText.realtime.connect({
  modelId: 'scribe_v2_realtime',
  keyterms: ['ElevenLabs'],
});
```

--------------------------------

### List dubs with HTTP GET request - Go

Source: https://elevenlabs.io/docs/api-reference/dubbing/list

Make a raw HTTP GET request to the dubbing endpoint and read the response body.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/dubbing"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Install TypeScript dependencies for WebSocket streaming

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts

Install dotenv for environment variables, @types/dotenv for TypeScript types, and ws for WebSocket client functionality.

```typescript
npm install dotenv
npm install @types/dotenv --save-dev
npm install ws
```

--------------------------------

### Install ElevenLabs React dependency

Source: https://elevenlabs.io/docs/eleven-agents/guides/quickstarts/next-js

Add the ElevenLabs React library to your project for agent integration.

```shell
npm install @elevenlabs/react
```

--------------------------------

### Perform Audio Isolation using ElevenLabs SDKs

Source: https://elevenlabs.io/docs/api-reference/audio-isolation/convert

These examples demonstrate how to use the ElevenLabs SDKs to convert audio files for isolation. Ensure the SDK is properly initialized and authenticated.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.audioIsolation.convert({});
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.audio_isolation.convert(
    audio="example_audio",
)
```

--------------------------------

### startSession

Source: https://elevenlabs.io/docs/eleven-agents/libraries/react

Establishes a connection and starts a conversation with an ElevenLabs Agents agent. It accepts an options object with `signedUrl`, `conversationToken`, or `agentId` being required for authentication. This method returns a promise resolving to a unique `conversationId`.

```APIDOC
## startSession

### Description
Establishes a connection and starts a conversation with an ElevenLabs Agents agent, using either `signedUrl`, `conversationToken`, or `agentId` for authentication. It returns a `conversationId`.

### Method
Client-side method

### Endpoint
N/A

### Parameters
#### Request Body
- **options** (object) - Required - An object containing connection parameters.
  - **agentId** (string) - Required (for public agents) - The ID of the agent. Can be acquired through the ElevenLabs UI.
  - **userId** (string) - Optional - Your own end user ID to map conversations to your users.
  - **signedUrl** (string) - Required (for WebSocket with authorization) - A pre-signed URL obtained from your server for establishing a WebSocket connection.
  - **conversationToken** (string) - Required (for WebRTC with authorization) - A token obtained from your server for establishing a WebRTC connection.

### Request Example
```js
// For public agents
const conversationId = await conversation.startSession({
  agentId: 'agent_7101k5zvyjhmfg983brhmhkd98n6',
  userId: 'user_9302xkm82nds93' // optional field
});

// For WebSocket connection with authorization
const response = await fetch("/signed-url", yourAuthHeaders);
const signedUrl = await response.text();
await conversation.startSession({
  signedUrl
});

// For WebRTC connection with authorization
const response = await fetch("/conversation-token", yourAuthHeaders);
const conversationToken = await response.text();
await conversation.startSession({
  conversationToken
});
```

### Response
#### Success Response (Promise Resolution)
- **conversationId** (string) - A globally unique conversation ID that identifies the started session.

#### Response Example
```
"conv_example123xyz"
```
```

--------------------------------

### Create Agent Deployment with Python SDK

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/agents/deployments/create

Uses the ElevenLabs Python client with typed deployment request objects. Requires the elevenlabs package.

```python
from elevenlabs import ElevenLabs, AgentDeploymentRequest, AgentDeploymentRequestItem, AgentDeploymentPercentageStrategy

client = ElevenLabs()

client.conversational_ai.agents.deployments.create(
    agent_id="agent_id",
    deployment_request=AgentDeploymentRequest(
        requests=[
            AgentDeploymentRequestItem(
                branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                deployment_strategy=AgentDeploymentPercentageStrategy(
                    traffic_percentage=0.5,
                    type="percentage",
                ),
            )
        ],
    ),
)
```

--------------------------------

### Example: Cinematic Instrumental Composition Plan

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans

Illustrates a multi-section composition plan for a cinematic instrumental piece, defining global and local styles, durations, and explicitly excluding vocals.

```json
{
  "positive_global_styles": ["cinematic", "orchestral", "epic", "80 BPM", "D minor"],
  "negative_global_styles": ["vocals", "lyrics", "pop", "electronic"],
  "sections": [
    {
      "section_name": "Tension Build",
      "positive_local_styles": ["low strings tremolo", "building intensity"],
      "negative_local_styles": ["bright"],
      "duration_ms": 15000,
      "lines": []
    },
    {
      "section_name": "Climax",
      "positive_local_styles": ["full orchestra", "brass fanfare", "triumphant"],
      "negative_local_styles": ["quiet"],
      "duration_ms": 15000,
      "lines": []
    },
    {
      "section_name": "Resolution",
      "positive_local_styles": ["gentle strings", "piano melody", "fading out"],
      "negative_local_styles": ["intense"],
      "duration_ms": 10000,
      "lines": []
    }
  ]
}
```

--------------------------------

### Install ElevenLabs React Native SDK Dependencies

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/expo-react-native

Install the ElevenLabs React Native SDK and its required peer dependencies for WebRTC functionality.

```bash
npx expo install @elevenlabs/react-native @livekit/react-native @livekit/react-native-webrtc @config-plugins/react-native-webrtc @livekit/react-native-expo-plugin @livekit/react-native-expo-plugin livekit-client
```

--------------------------------

### List Conversational AI Tools (Go)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/list

Make a direct HTTP GET request in Go to the ElevenLabs API to retrieve conversational AI tools.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/tools"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Legacy tool configuration format (deprecated)

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/agent-tools-deprecation

Deprecated format for specifying tools directly in the prompt using the `tools` array. Do not use in new implementations; this format will be rejected after July 23.

```json
{
  "conversation_config": {
    "agent": {
      "prompt": {
        "tools": [
          {
            "type": "client", 
            "name": "open_url",
            "description": "Open a provided URL in the user's browser."
          },
          {
            "type": "system",
            "name": "end_call", 
            "description": "",
            "response_timeout_secs": 20,
            "params": {
              "system_tool_type": "end_call"
            }
          }
        ]
      }
    }
  }
}
```

--------------------------------

### Start and End an ElevenAgents Conversation

Source: https://elevenlabs.io/docs/eleven-agents/libraries/react-native

Use the `useConversationControls` and `useConversationStatus` hooks to manage the lifecycle of an ElevenAgents conversation, including starting and ending sessions.

```tsx
import { useConversationControls, useConversationStatus } from '@elevenlabs/react-native';
import React from 'react';
import { View, Text, Button } from 'react-native';

function ConversationComponent() {
  const { startSession, endSession } = useConversationControls();
  const { status } = useConversationStatus();

  const handleStart = async () => {
    await startSession({
      agentId: 'agent_7101k5zvyjhmfg983brhmhkd98n6',
    });
  };

  return (
    <View>
      <Text>Status: {status}</Text>
      <Button
        title={status === 'connected' ? 'End' : 'Start'}
        onPress={status === 'connected' ? endSession : handleStart}
      />
    </View>
  );
}
```

--------------------------------

### POST /v1/pronunciation-dictionaries/add-from-file

Source: https://elevenlabs.io/docs/api-reference/pronunciation-dictionaries/create-from-file

Creates a new pronunciation dictionary from a lexicon .PLS file.

```APIDOC
## POST /v1/pronunciation-dictionaries/add-from-file

### Description
Creates a new pronunciation dictionary from a lexicon .PLS file.

### Method
POST

### Endpoint
https://api.elevenlabs.io/v1/pronunciation-dictionaries/add-from-file

### Parameters
#### Request Body
- **file** (file) - Required - The lexicon .PLS file to upload.
- **Content-Type** (string) - Required - Must be `multipart/form-data`.

### Request Example
{}

### Response
#### Success Response (200)
(No explicit details provided in the source text)

#### Response Example
{}
```

--------------------------------

### Create Knowledge Base Document from URL - Swift HTTP Client

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/create-from-url

Make a POST request to the ElevenLabs knowledge base endpoint using URLSession in Swift. Requires Foundation framework.

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["url": "string"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/url")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Agent Chat Response Part: Start Event Structure

Source: https://elevenlabs.io/docs/eleven-agents/customization/events/client-events

Illustrates the JSON structure for an 'agent_chat_response_part' event when the agent's response starts.

```javascript
// Example start event
{
  "type": "agent_chat_response_part",
  "text_response_part": {
    "type": "start",
    "text": "",
    "event_id": "evt_123456"
  }
}
```

--------------------------------

### GET /v1/convai/tools

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/tools/list

Get all available tools in the workspace. This endpoint allows filtering by search term, page size, owner, type, and sorting options.

```APIDOC
## GET /v1/convai/tools

### Description
Get all available tools in the workspace.

### Method
GET

### Endpoint
/v1/convai/tools

### Parameters
#### Query Parameters
- **search** (string | null) - Optional - If specified, the endpoint returns only tools whose names start with this string.
- **page_size** (integer | null) - Optional - How many documents to return at maximum. Can not exceed 100, defaults to 30.
- **show_only_owned_documents** (boolean) - Optional - If set to true, the endpoint will return only tools owned by you (and not shared from somebody else). Deprecated: use created_by_user_id instead. (default: false)
- **created_by_user_id** (string | null) - Optional - Filter tools by creator user ID. When set, only tools created by this user are returned. Takes precedence over show_only_owned_documents. Use '@me' to refer to the authenticated user.
- **types** (array | null) - Optional - If present, the endpoint will return only tools of the given types. (Enum: webhook, client, api_integration_webhook)
- **sort_direction** (string) - Optional - The direction to sort the results. (Enum: asc, desc)
- **sort_by** (string | null) - Optional - The field to sort the results by. (Enum: name, created_at)
- **cursor** (string | null) - Optional - Used for fetching next page. Cursor is returned in the response.

#### Header Parameters
- **xi-api-key** (string) - Optional - API key for authentication.

### Response
#### Success Response (200)
- **ToolsResponseModel** (object) - Successful Response, containing a list of tools.
```

--------------------------------

### Create Agent with Language Detection Tool in Python

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/language-detection

Initialize the ElevenLabs client, define a language detection system tool, configure language presets with localized first messages for multiple languages (Dutch, Finnish, Turkish, Russian, Portuguese), and create the agent. Requires ElevenLabs SDK and valid API key.

```python
from elevenlabs import (
    ConversationalConfig,
    ElevenLabs,
    AgentConfig,
    PromptAgent,
    PromptAgentInputToolsItem_System,
    LanguagePresetInput,
    ConversationConfigClientOverrideInput,
    AgentConfigOverride,
)

# Initialize the client
elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

# Create the language detection tool
language_detection_tool = PromptAgentInputToolsItem_System(
    name="language_detection",
    description=""  # Optional: Customize when the tool should be triggered
)

# Create language presets
language_presets = {
    "nl": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Hoi, hoe gaat het met je?",
                language=None
            ),
            tts=None
        ),
        first_message_translation=None
    ),
    "fi": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                first_message="Hei, kuinka voit?",
            ),
            tts=None
        ),
    ),
    "tr": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Merhaba, nasılsın?",
                language=None
            ),
            tts=None
        ),
    ),
    "ru": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Привет, как ты?",
                language=None
            ),
            tts=None
        ),
    ),
    "pt": LanguagePresetInput(
        overrides=ConversationConfigClientOverrideInput(
            agent=AgentConfigOverride(
                prompt=None,
                first_message="Oi, como você está?",
                language=None
            ),
            tts=None
        ),
    )
}

# Create the agent configuration
conversation_config = ConversationalConfig(
    agent=AgentConfig(
        prompt=PromptAgent(
            tools=[language_detection_tool],
            first_message="Hi how are you?"
        )
    ),
    language_presets=language_presets
)

# Create the agent
response = elevenlabs.conversational_ai.agents.create(
    conversation_config=conversation_config
)
```

--------------------------------

### Get Tool Configuration - C# HTTP Request

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/tool-configuration/get

Make a direct HTTP GET request to retrieve tool configuration using RestSharp for C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs/tool_name");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Configure transfer_to_number tool in Python

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/transfer-to-number

Set up transfer rules with phone and SIP destinations, then create an agent with the transfer tool. Supports conference, blind, and SIP refer transfer types with optional post-dial digits and custom SIP headers.

```python
from elevenlabs import (
    ConversationalConfig,
    ElevenLabs,
    AgentConfig,
    PromptAgent,
    PromptAgentInputToolsItem_System,
    SystemToolConfigInputParams_TransferToNumber,
    PhoneNumberTransfer,
)

# Initialize the client
elevenlabs = ElevenLabs(api_key="YOUR_API_KEY")

# Define transfer rules
transfer_rules = [
    PhoneNumberTransfer(
        transfer_destination={"type": "phone", "phone_number": "+15551234567"},
        condition="When the user asks for billing support.",
        transfer_type="conference",
        post_dial_digits="ww1234"  # Wait 1s, then dial extension 1234 (native Twilio only)
    ),
    PhoneNumberTransfer(
        transfer_destination={"type": "phone", "phone_number": "+15559876543"},
        condition="When the user asks to speak to a human.",
        transfer_type="blind"  # Native Twilio integration only, preserves caller ID, no warm transfer message
    ),
    PhoneNumberTransfer(
        transfer_destination={"type": "sip_uri", "sip_uri": "sip:support@example.com"},
        condition="When the user requests to file a formal complaint.",
        transfer_type="sip_refer",
        custom_sip_headers=[
            {"key": "X-Department", "value": "complaints"},
            {"key": "X-Priority", "value": "high"},
            {"key": "X-Customer-ID", "value": "{{customer_id}}"}
        ]
    )
]

# Create the transfer tool configuration
transfer_tool = PromptAgentInputToolsItem_System(
    type="system",
    name="transfer_to_human",
    description="Transfer the user to a specialized agent based on their request.", # Optional custom description
    params=SystemToolConfigInputParams_TransferToNumber(
        transfers=transfer_rules
    )
)

# Create the agent configuration
conversation_config = ConversationalConfig(
    agent=AgentConfig(
        prompt=PromptAgent(
            prompt="You are a helpful assistant.",
            first_message="Hi, how can I help you today?",
            tools=[transfer_tool],
        )
    )
)

# Create the agent
response = elevenlabs.conversational_ai.agents.create(
    conversation_config=conversation_config
)

# Note: When the LLM decides to call this tool, it needs to provide:
# - transfer_number: The phone number to transfer to (must match one defined in rules).
# - client_message: Message read to the user during transfer.
# - agent_message: Message read to the human operator receiving the call (native Twilio integration only, not used for blind transfers or SIP).
```

--------------------------------

### Get Conversation Tag (PHP Guzzle)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/tags/get

Execute a GET request to the ElevenLabs API for a conversation tag using the Guzzle HTTP client in PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/tags/tag_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Get Conversation Tag (Ruby)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/tags/get

Perform a GET request to the ElevenLabs API for a conversation tag using Ruby's Net::HTTP library.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/tags/tag_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

--------------------------------

### Create Tool Configuration in Java (Unirest)

Source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create

This snippet shows how to create a tool configuration using the Unirest HTTP client library in Java.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs")
  .header("Content-Type", "application/json")
  .body("{\n  \"tool_name\": \"string\"\n}")
  .asString();
```

--------------------------------

### POST /v1/audio-native

Source: https://elevenlabs.io/docs/api-reference/audio-native/create

Creates an Audio Native enabled project and optionally starts the conversion process. Returns a project ID and embeddable HTML snippet that can be used to integrate the audio native content into web applications.

```APIDOC
## POST /v1/audio-native

### Description
Creates an Audio Native enabled project, optionally starts conversion, and returns project ID and embeddable HTML snippet.

### Method
POST

### Endpoint
https://api.elevenlabs.io/v1/audio-native

### Content-Type
multipart/form-data

### Response
#### Success Response (200)
- **project_id** (string) - Unique identifier for the created Audio Native project
- **html_snippet** (string) - Embeddable HTML code for integrating the Audio Native project into web applications

### Reference
https://elevenlabs.io/docs/api-reference/audio-native/create
```

--------------------------------

### Get Conversation Tag (Go)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/conversations/tags/get

Make a GET request to the ElevenLabs API to retrieve a conversation tag using standard Go HTTP client.

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/tags/tag_id"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Knowledge Base Folder with C#

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/knowledge-base/create-folder

This snippet demonstrates how to create a new folder in an ElevenLabs knowledge base using the RestSharp HTTP client for C#.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/folder");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Project Documentation\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get a Batch Call (PHP Guzzle)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/batch-calling/get

Demonstrates retrieving batch call details with a GET request using the Guzzle HTTP client in PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/batch-calling/batch_id');

echo $response->getBody();
```

--------------------------------

### List Environment Variables in Java

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/environment-variables/list

Use the Unirest library in Java to send an HTTP GET request and fetch environment variables.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

--------------------------------

### Get Workspace Secret with Go

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get

Make a GET request to the ElevenLabs API to retrieve a workspace secret using standard Go HTTP client.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Separate Instructions into Clean Sections (MDX)

Source: https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide

Demonstrates how structuring system prompt instructions with markdown headings and clear section boundaries improves model interpretation and reliability by preventing instruction bleed.

```mdx
You are a customer service agent. Be polite and helpful. Never share sensitive data. You can look up orders and process refunds. Always verify identity first. Keep responses under 3 sentences unless the user asks for details.
```

```mdx
# Personality

You are a customer service agent for Acme Corp. You are polite, efficient, and solution-oriented.

# Goal

Help customers resolve issues quickly by looking up orders and processing refunds when appropriate.

# Guardrails

Never share sensitive customer data across conversations.
Always verify customer identity before accessing account information.

# Tone

Keep responses concise (under 3 sentences) unless the user requests detailed explanations.
```

--------------------------------

### Get Secret Dependencies - Java HTTP

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

Make a GET request to the secrets dependencies endpoint using the Unirest HTTP client library for Java.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools")
  .asString();
```

--------------------------------

### Get Secret Dependencies - Ruby HTTP

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

Make a GET request to the secrets dependencies endpoint using Ruby's Net::HTTP library.

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

--------------------------------

### Get Secret Dependencies - Go HTTP

Source: https://elevenlabs.io/docs/api-reference/workspace/secrets/get-dependencies

Make a GET request to the secrets dependencies endpoint using Go's standard HTTP library.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/secrets/secret_id/dependencies/tools"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### List Knowledge Base - Python SDK

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/list

Use the ElevenLabs Python SDK to list all knowledge bases. Instantiate the client and call the list method on the knowledge_base resource.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.knowledge_base.list()
```

--------------------------------

### Get Widget (Swift)

Source: https://elevenlabs.io/docs/api-reference/widget/get

Perform an asynchronous HTTP GET request in Swift using URLSession to retrieve the conversational AI agent's widget.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/agent_id/widget")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### New tool configuration format with tool IDs and built-in tools

Source: https://elevenlabs.io/docs/eleven-agents/customization/tools/agent-tools-deprecation

Recommended format for specifying tools using `tool_ids` for client tools and `built_in_tools` for system tools. Use this format for all new implementations.

```json
{
  "conversation_config": {
    "agent": {
      "prompt": {
        "tool_ids": ["tool_123456789abcdef0"],
        "built_in_tools": {
          "end_call": {
            "name": "end_call",
            "description": "",
            "response_timeout_secs": 20,
            "type": "system",
            "params": {
              "system_tool_type": "end_call"
            }
          },
          "language_detection": null,
          "transfer_to_agent": null,
          "transfer_to_number": null,
          "skip_turn": null
        }
      }
    }
  }
}
```

--------------------------------

### Get Widget (Java)

Source: https://elevenlabs.io/docs/api-reference/widget/get

Use the Unirest library in Java to send an HTTP GET request and retrieve the conversational AI agent's widget.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/agent_id/widget")
  .asString();
```

--------------------------------

### Get Conversational AI Settings (PHP Guzzle)

Source: https://elevenlabs.io/docs/api-reference/workspace/get

Use Guzzle HTTP client to make a GET request for conversational AI settings in PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/settings');

echo $response->getBody();
```

--------------------------------

### Create Tool Configuration in Python

Source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create

This snippet shows how to create a new tool configuration for an MCP server using the ElevenLabs Python SDK.

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.mcp_servers.tool_configs.create(
    mcp_server_id="mcp_server_id",
    tool_name="string",
)
```

--------------------------------

### Get Conversational AI Settings (Go)

Source: https://elevenlabs.io/docs/api-reference/workspace/get

Make a GET request to the conversational AI settings endpoint using Go's net/http package.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/settings"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Schema: SMBToolConfig

Source: https://elevenlabs.io/docs/changelog/2026/3/9

Small business tool configuration schema. Now includes rental and appointment operation types with corresponding parameter schemas.

```APIDOC
## Schema: SMBToolConfig

### Description
Small business tool configuration with support for rental and appointment operations.

### Fields
- **rental_operations** (object) - Optional - Configuration for rental operation types
- **appointment_operations** (object) - Optional - Configuration for appointment operation types
```

--------------------------------

### List MCP Server Tools in C#

Source: https://elevenlabs.io/docs/api-reference/mcp/list-tools

This snippet demonstrates how to list tools for a given MCP server ID using the RestSharp library in C#. It initializes a client and executes a GET request.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tools");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Tool - Go HTTP

Source: https://elevenlabs.io/docs/api-reference/tools/get

Retrieve a tool using Go's standard net/http library. Makes a GET request to the API endpoint.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/tools/tool_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Dependent Agents in Swift

Source: https://elevenlabs.io/docs/api-reference/tools/get-dependent-agents

Send an HTTP GET request using `URLSession` in Swift to retrieve agents dependent on a specified tool ID.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/tools/tool_id/dependent-agents")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create MCP Server (Python SDK)

Source: https://elevenlabs.io/docs/eleven-agents/api-reference/mcp/create

Utilize the ElevenLabs Python SDK to create an MCP server. The 'McpServerConfigInput' object is used to define the server's URL and name.

```python
from elevenlabs import ElevenLabs, McpServerConfigInput

client = ElevenLabs()

client.conversational_ai.mcp_servers.create(
    config=McpServerConfigInput(
        url="string",
        name="string",
    ),
)
```

--------------------------------

### Get Test Invocation (Go HTTP Request)

Source: https://elevenlabs.io/docs/api-reference/tests/test-invocations/get

Performs a GET request to retrieve a test invocation using standard Go HTTP client.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/test-invocations/test_invocation_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Create Expo React Native Project

Source: https://elevenlabs.io/docs/eleven-agents/guides/integrations/expo-react-native

Use npx create-expo-app to initialize a new blank TypeScript Expo project.

```bash
npx create-expo-app@latest --template blank-typescript
```

--------------------------------

### List Conversational AI Tests (C#)

Source: https://elevenlabs.io/docs/api-reference/tests/list

Perform an HTTP GET request in C# using RestSharp to get a list of conversational AI tests.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agent-testing");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Get Knowledge Base Document (Swift)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-document

Make an HTTP GET request in Swift using URLSession to retrieve a document from a knowledge base by its ID.

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Create Tool Configuration in PHP (Guzzle)

Source: https://elevenlabs.io/docs/api-reference/mcp/tool-configuration/create

This snippet demonstrates how to create a tool configuration using the Guzzle HTTP client in PHP.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/convai/mcp-servers/mcp_server_id/tool-configs', [
  'body' => '{
  "tool_name": "string"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

--------------------------------

### Get Knowledge Base Document (C#)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-document

Make an HTTP GET request in C# using RestSharp to retrieve a document from a knowledge base by its ID.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

--------------------------------

### Make First Text-to-Speech Request

Source: https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-speech

This code demonstrates how to initialize the ElevenLabs client, convert text to speech, and play the generated audio using your API key and a specified voice.

```python
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_speech.convert(
    text="The first move is what sets everything in motion.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",  # "George" - browse voices at elevenlabs.io/app/voice-library
    model_id="eleven_v3",
    output_format="mp3_44100_128",
)

play(audio)
```

```typescript
import { ElevenLabsClient, play } from '@elevenlabs/elevenlabs-js';
import 'dotenv/config';

const elevenlabs = new ElevenLabsClient();
const audio = await elevenlabs.textToSpeech.convert(
  'JBFqnCBsd6RMkjVDRZzb', // "George" - browse voices at elevenlabs.io/app/voice-library
  {
    text: 'The first move is what sets everything in motion.',
    modelId: 'eleven_v3',
    outputFormat: 'mp3_44100_128',
  }
);

await play(audio);
```

--------------------------------

### Get Knowledge Base Document (PHP)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-document

Make an HTTP GET request in PHP using Guzzle to retrieve a document from a knowledge base by its ID.

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id');

echo $response->getBody();
```

--------------------------------

### Get Knowledge Base Document (Java)

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-document

Make an HTTP GET request in Java using Unirest to retrieve a document from a knowledge base by its ID.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id")
  .asString();
```

--------------------------------

### Get Project Snapshot with Go HTTP Client

Source: https://elevenlabs.io/docs/api-reference/studio/get-project-snapshot

Make a GET request to the ElevenLabs API using Go's standard net/http package. Construct the URL with project and snapshot IDs, execute the request, and read the response body.

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id/snapshots/project_snapshot_id"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

--------------------------------

### Get Environment Variable (Java Unirest)

Source: https://elevenlabs.io/docs/api-reference/environment-variables/get

Use the Unirest library in Java to send a GET request for an environment variable. The response is returned as a string.

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/environment-variables/env_var_id")
  .asString();
```

--------------------------------

### Retrieve Conversational AI Agent Summaries

Source: https://elevenlabs.io/docs/api-reference/agents/get-summaries

These examples demonstrate how to fetch summaries for conversational AI agents using various SDKs and direct HTTP requests across different programming languages. Provide the `agentIds` to specify which agents to retrieve summaries for.

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.agents.summaries.get({
        agentIds: [
            "string"
        ]
    });
}
main();
```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.conversational_ai.agents.summaries.get(
    agent_ids=[
        "string"
    ]
)
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22string%22%5D"

	req, _ := http.NewRequest("GET", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22string%22%5D")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22string%22%5D")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22string%22%5D');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22string%22%5D");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/convai/agents/summaries?agent_ids=%5B%22string%22%5D")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

--------------------------------

### Main Script for S3 Audio Upload (Partial)

Source: https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming

An incomplete Python script demonstrating how to integrate the S3 upload and presigned URL generation functions into a main application flow.

```python
import os

from dotenv import load_dotenv

load_dotenv()

from text_to_speech_stream import text_to_speech_stream
from s3_uploader import upload_audiostream_to_s3, generate_presigned_url


def main():
    text = "This is James"
```

--------------------------------

### Get Document RAG Indexes - C# HTTP Client

Source: https://elevenlabs.io/docs/api-reference/knowledge-base/get-rag-index

Uses the RestSharp library to make a GET request. Requires the RestSharp NuGet package.

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/convai/knowledge-base/documentation_id/rag-index");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```