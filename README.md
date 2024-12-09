# Repro for issue 8002

## Versions

firebase-tools: v13.28.0<br>
node: v20.18.0<br>
firebase_functions: v0.4.2<br>

## Steps to reproduce

1. Install dependencies
   - Run `cd functions`
   - Run `python3.12 -m venv venv`
   - Run `. "./venv/bin/activate" && python3.12 -m pip install -r requirements.txt`
     - Windows: `venv\Scripts\activate && python -m pip install -r requirements.txt`
2. Run `firebase emulators:start --project demo-project` on a new terminal
3. Invoke function that <b>does not have logger</b> "http://127.0.0.1:5001/demo-project/us-central1/no_logger"
   - Browser responds with

```
Hello world!🐦‍⬛ Blackbird
```

4. Invoke function that <b>has logger</b> "http://127.0.0.1:5001/demo-project/us-central1/with_logger"
   - Browser responds with

```
500 Internal Server Error: The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
```

<details>
  <summary>firebase-debug.logs</summary>

```
[debug] [2024-12-09T11:55:02.955Z] ----------------------------------------------------------------------
[debug] [2024-12-09T11:55:02.958Z] Command:       C:\Program Files\nodejs\node.exe C:\Program Files\nodejs\node_modules\firebase-tools\lib\bin\firebase.js emulators:start --project demo-project
[debug] [2024-12-09T11:55:02.958Z] CLI Version:   13.28.0
[debug] [2024-12-09T11:55:02.958Z] Platform:      win32
[debug] [2024-12-09T11:55:02.958Z] Node Version:  v20.12.1
[debug] [2024-12-09T11:55:02.958Z] Time:          Mon Dec 09 2024 19:55:02 GMT+0800 (Philippine Standard Time)
[debug] [2024-12-09T11:55:02.958Z] ----------------------------------------------------------------------
[debug]
[debug] [2024-12-09T11:55:02.960Z] >>> [apiv2][query] GET https://firebase-public.firebaseio.com/cli.json [none]
[debug] [2024-12-09T11:55:03.048Z] > command requires scopes: ["email","openid","https://www.googleapis.com/auth/cloudplatformprojects.readonly","https://www.googleapis.com/auth/firebase","https://www.googleapis.com/auth/cloud-platform"]
[debug] [2024-12-09T11:55:03.048Z] > authorizing via signed-in user (<USER>@gmail.com)
[info] i  emulators: Starting emulators: functions, extensions {"metadata":{"emulator":{"name":"hub"},"message":"Starting emulators: functions, extensions"}}
[info] i  emulators: Detected demo project ID "demo-project", emulated services will use a demo configuration and attempts to access non-emulated services for this project will fail. {"metadata":{"emulator":{"name":"hub"},"message":"Detected demo project ID \"demo-project\", emulated services will use a demo configuration and attempts to access non-emulated services for this project will fail."}}
[debug] [2024-12-09T11:55:03.056Z] [logging] Logging Emulator only supports listening on one address (127.0.0.1). Not listening on ::1
[debug] [2024-12-09T11:55:03.056Z] assigned listening specs for emulators {"user":{"hub":[{"address":"127.0.0.1","family":"IPv4","port":4400},{"address":"::1","family":"IPv6","port":4400}],"ui":[{"address":"127.0.0.1","family":"IPv4","port":4000},{"address":"::1","family":"IPv6","port":4000}],"logging":[{"address":"127.0.0.1","family":"IPv4","port":4500}]},"metadata":{"message":"assigned listening specs for emulators"}}
[debug] [2024-12-09T11:55:03.059Z] [hub] writing locator at C:\Users\ALEJAN~1\AppData\Local\Temp\hub-demo-project.json
[debug] [2024-12-09T11:55:03.071Z] [Extensions] Started Extensions emulator, this is a noop.
[debug] [2024-12-09T11:55:03.074Z] [functions] Functions Emulator only supports listening on one address (127.0.0.1). Not listening on ::1
[debug] [2024-12-09T11:55:03.074Z] [eventarc] Eventarc Emulator only supports listening on one address (127.0.0.1). Not listening on ::1
[debug] [2024-12-09T11:55:03.074Z] [tasks] Cloud Tasks Emulator only supports listening on one address (127.0.0.1). Not listening on ::1
[debug] [2024-12-09T11:55:03.074Z] late-assigned ports for functions and eventarc emulators {"user":{"hub":[{"address":"127.0.0.1","family":"IPv4","port":4400},{"address":"::1","family":"IPv6","port":4400}],"ui":[{"address":"127.0.0.1","family":"IPv4","port":4000},{"address":"::1","family":"IPv6","port":4000}],"logging":[{"address":"127.0.0.1","family":"IPv4","port":4500}],"functions":[{"address":"127.0.0.1","family":"IPv4","port":5001}],"eventarc":[{"address":"127.0.0.1","family":"IPv4","port":9299}],"tasks":[{"address":"127.0.0.1","family":"IPv4","port":9499}]},"metadata":{"message":"late-assigned ports for functions and eventarc emulators"}}
[debug] [2024-12-09T11:55:03.076Z] defaultcredentials: writing to file C:\Users\<USER>\AppData\Roaming\firebase\<USER>s.json
[debug] [2024-12-09T11:55:03.077Z] Setting GAC to C:\Users\<USER>\AppData\Roaming\firebase\<USER>s.json {"metadata":{"emulator":{"name":"functions"},"message":"Setting GAC to C:\\Users\\<USER>\\AppData\\Roaming\\firebase\\<USER>s.json"}}
[debug] [2024-12-09T11:55:03.093Z] [Extensions] Connecting Extensions emulator, this is a noop.
[info] i  functions: Watching "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions" for Cloud Functions... {"metadata":{"emulator":{"name":"functions"},"message":"Watching \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\" for Cloud Functions..."}}
[debug] [2024-12-09T11:55:03.100Z] Customer code is not Node
[debug] [2024-12-09T11:55:03.100Z] Validating python source
[debug] [2024-12-09T11:55:03.100Z] Building python source
[debug] [2024-12-09T11:55:03.102Z] Could not find functions.yaml. Must use http discovery
[debug] [2024-12-09T11:55:03.105Z] Running command with virtualenv: command="C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Scripts\activate.bat", args=["","&&","python.exe","-c","\"import firebase_functions; import os; print(os.path.dirname(firebase_functions.__file__))\""]
[debug] [2024-12-09T11:55:03.222Z] stdout: C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions


[debug] [2024-12-09T11:55:03.227Z] Running admin server with args: ["python.exe","\"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\private\\serving.py\""] and env: {"GCLOUD_PROJECT":"demo-project","K_REVISION":"1","PORT":"80","GOOGLE_CLOUD_QUOTA_PROJECT":"demo-project","FUNCTIONS_EMULATOR":"true","TZ":"UTC","FIREBASE_DEBUG_MODE":"true","FIREBASE_DEBUG_FEATURES":"{\"skipTokenVerification\":true,\"enableCors\":true}","FIREBASE_EMULATOR_HUB":"127.0.0.1:4400","CLOUD_EVENTARC_EMULATOR_HOST":"http://127.0.0.1:9299","CLOUD_TASKS_EMULATOR_HOST":"127.0.0.1:9499","FIREBASE_CONFIG":"{\"storageBucket\":\"demo-project.appspot.com\",\"databaseURL\":\"https://demo-project.firebaseio.com\",\"projectId\":\"demo-project\"}","GOOGLE_APPLICATION_CREDENTIALS":"C:\\Users\\<USER>\\AppData\\Roaming\\firebase\\<USER>s.json","ADMIN_PORT":"8081"} in C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions
[debug] [2024-12-09T11:55:03.227Z] Running command with virtualenv: command="C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Scripts\activate.bat", args=["","&&","python.exe","\"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\private\\serving.py\""]
[info]  * Serving Flask app 'serving'
 * Debug mode: off


[error] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8081


[error] Press CTRL+C to quit


[error] 127.0.0.1 - - [09/Dec/2024 11:55:04] "GET /__/functions.yaml HTTP/1.1" 200 -


[debug] [2024-12-09T11:55:04.028Z] Got response from /__/functions.yaml endpoints:
  no_logger:
    availableMemoryMb: null
    concurrency: null
    entryPoint: no_logger
    httpsTrigger: {}
    ingressSettings: null
    labels: {}
    maxInstances: null
    minInstances: null
    platform: gcfv2
    secretEnvironmentVariables: []
    serviceAccountEmail: null
    timeoutSeconds: null
  with_logger:
    availableMemoryMb: null
    concurrency: null
    entryPoint: with_logger
    httpsTrigger: {}
    ingressSettings: null
    labels: {}
    maxInstances: null
    minInstances: null
    platform: gcfv2
    secretEnvironmentVariables: []
    serviceAccountEmail: null
    timeoutSeconds: null
params: []
requiredAPIs: []
specVersion: v1alpha1


[error] 127.0.0.1 - - [09/Dec/2024 11:55:04] "GET /__/quitquitquit HTTP/1.1" 200 -


[info] +  functions: Loaded functions definitions from source: no_logger, with_logger. {"metadata":{"emulator":{"name":"functions"},"message":"Loaded functions definitions from source: no_logger, with_logger."}}
[info] +  functions[us-central1-no_logger]: http function initialized (http://127.0.0.1:5001/demo-project/us-central1/no_logger). {"metadata":{"emulator":{"name":"functions"},"message":"\u001b[1mhttp\u001b[22m function initialized (http://127.0.0.1:5001/demo-project/us-central1/no_logger)."}}
[info] +  functions[us-central1-with_logger]: http function initialized (http://127.0.0.1:5001/demo-project/us-central1/with_logger). {"metadata":{"emulator":{"name":"functions"},"message":"\u001b[1mhttp\u001b[22m function initialized (http://127.0.0.1:5001/demo-project/us-central1/with_logger)."}}
[info]
┌─────────────────────────────────────────────────────────────┐
│ ✔  All emulators ready! It is now safe to connect your app. │
│ i  View Emulator UI at http://127.0.0.1:4000/               │
└─────────────────────────────────────────────────────────────┘


┌────────────┬────────────────┬──────────────────────────────────┐
│ Emulator   │ Host:Port      │ View in Emulator UI              │
├────────────┼────────────────┼──────────────────────────────────┤
│ Functions  │ 127.0.0.1:5001 │ http://127.0.0.1:4000/functions  │
├────────────┼────────────────┼──────────────────────────────────┤
│ Extensions │ 127.0.0.1:5001 │ http://127.0.0.1:4000/extensions │
└────────────┴────────────────┴──────────────────────────────────┘
  Emulator Hub running at 127.0.0.1:4400
  Other reserved ports: 4500
┌─────────────────────────┬───────────────┬─────────────────────┐
│ Extension Instance Name │ Extension Ref │ View in Emulator UI │
└─────────────────────────┴───────────────┴─────────────────────┘
Issues? Report them at https://github.com/firebase/firebase-tools/issues and attach the *-debug.log files.


[debug] [2024-12-09T11:55:04.081Z] <<< [apiv2][status] GET https://firebase-public.firebaseio.com/cli.json 200
[debug] [2024-12-09T11:55:04.082Z] <<< [apiv2][body] GET https://firebase-public.firebaseio.com/cli.json {"cloudBuildErrorAfter":1594252800000,"cloudBuildWarnAfter":1590019200000,"defaultNode10After":1594252800000,"minVersion":"3.0.5","node8DeploysDisabledAfter":1613390400000,"node8RuntimeDisabledAfter":1615809600000,"node8WarnAfter":1600128000000}
[debug] [2024-12-09T11:55:07.175Z] [work-queue] {"queuedWork":["/demo-project/us-central1/no_logger-2024-12-09T11:55:07.175Z"],"queueLength":1,"runningWork":[],"workRunningCount":0}
[debug] [2024-12-09T11:55:07.175Z] [work-queue] {"queuedWork":[],"queueLength":0,"runningWork":["/demo-project/us-central1/no_logger-2024-12-09T11:55:07.175Z"],"workRunningCount":1}
[debug] [2024-12-09T11:55:07.175Z] Accepted request GET /demo-project/us-central1/no_logger --> us-central1-no_logger
[debug] [2024-12-09T11:55:07.176Z] [functions] Runtime ready! Sending request! {"metadata":{"emulator":{"name":"functions"},"message":"[functions] Runtime ready! Sending request!"}}
[debug] [2024-12-09T11:55:07.176Z] [functions] Got req.url=/demo-project/us-central1/no_logger, mapping to path=/ {"metadata":{"emulator":{"name":"functions"},"message":"[functions] Got req.url=/demo-project/us-central1/no_logger, mapping to path=/"}}
[debug] [2024-12-09T11:55:07.180Z] Running command with virtualenv: command="C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Scripts\activate.bat", args=["","&&","functions-framework"]
[debug] [2024-12-09T11:55:07.189Z] [worker-pool] addWorker(us-central1-no_logger) {"metadata":{"emulator":{"name":"functions"},"message":"[worker-pool] addWorker(us-central1-no_logger)"}}
[debug] [2024-12-09T11:55:07.190Z] [worker-pool] Adding worker with key us-central1-no_logger, total=1 {"metadata":{"emulator":{"name":"functions"},"message":"[worker-pool] Adding worker with key us-central1-no_logger, total=1"}}
[info] >   * Serving Flask app 'no_logger'
 {"user":" * Serving Flask app 'no_logger'\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m  * Serving Flask app 'no_logger'\r"}}
[info] >   * Debug mode: off
 {"user":" * Debug mode: off\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m  * Debug mode: off\r"}}
[info] >  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 {"user":"WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\r"}}
[info] >   * Running on http://127.0.0.1:8739
 {"user":" * Running on http://127.0.0.1:8739\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m  * Running on http://127.0.0.1:8739\r"}}
[info] >  Press CTRL+C to quit
 {"user":"Press CTRL+C to quit\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m Press CTRL+C to quit\r"}}
[info] >  127.0.0.1 - - [09/Dec/2024 11:55:07] "GET /__/health HTTP/1.1" 200 -
 {"user":"127.0.0.1 - - [09/Dec/2024 11:55:07] \"GET /__/health HTTP/1.1\" 200 -\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m 127.0.0.1 - - [09/Dec/2024 11:55:07] \"GET /__/health HTTP/1.1\" 200 -\r"}}
[debug] [2024-12-09T11:55:07.733Z] [worker-us-central1-no_logger-26fbc284-d4e6-4193-9491-a3feab246968]: IDLE {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"[worker-us-central1-no_logger-26fbc284-d4e6-4193-9491-a3feab246968]: IDLE"}}
[debug] [2024-12-09T11:55:07.734Z] [worker-pool] submitRequest(triggerId=us-central1-no_logger) {"metadata":{"emulator":{"name":"functions"},"message":"[worker-pool] submitRequest(triggerId=us-central1-no_logger)"}}
[info] i  functions: Beginning execution of "us-central1-no_logger" {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"Beginning execution of \"us-central1-no_logger\""}}
[debug] [2024-12-09T11:55:07.734Z] [worker-us-central1-no_logger-26fbc284-d4e6-4193-9491-a3feab246968]: BUSY {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"[worker-us-central1-no_logger-26fbc284-d4e6-4193-9491-a3feab246968]: BUSY"}}
[info] >  127.0.0.1 - - [09/Dec/2024 11:55:07] "GET / HTTP/1.1" 200 -
 {"user":"127.0.0.1 - - [09/Dec/2024 11:55:07] \"GET / HTTP/1.1\" 200 -\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m 127.0.0.1 - - [09/Dec/2024 11:55:07] \"GET / HTTP/1.1\" 200 -\r"}}
[debug] [2024-12-09T11:55:07.737Z] Finishing up request with event=pause {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"Finishing up request with event=pause"}}
[info] i  functions: Finished "us-central1-no_logger" in 2.6042ms {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"Finished \"us-central1-no_logger\" in 2.6042ms"}}
[debug] [2024-12-09T11:55:07.737Z] [worker-us-central1-no_logger-26fbc284-d4e6-4193-9491-a3feab246968]: IDLE {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"[worker-us-central1-no_logger-26fbc284-d4e6-4193-9491-a3feab246968]: IDLE"}}
[debug] [2024-12-09T11:55:07.737Z] Finishing up request with event=finish {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"Finishing up request with event=finish"}}
[debug] [2024-12-09T11:55:07.737Z] Finishing up request with event=close {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-no_logger"},"extension":{},"message":"Finishing up request with event=close"}}
[debug] [2024-12-09T11:55:07.737Z] [work-queue] {"queuedWork":[],"queueLength":0,"runningWork":[],"workRunningCount":0}
[debug] [2024-12-09T11:55:07.766Z] Functions emulator received unknown request at path /favicon.ico
[debug] [2024-12-09T11:55:10.021Z] [work-queue] {"queuedWork":["/demo-project/us-central1/with_logger-2024-12-09T11:55:10.021Z"],"queueLength":1,"runningWork":[],"workRunningCount":0}
[debug] [2024-12-09T11:55:10.022Z] [work-queue] {"queuedWork":[],"queueLength":0,"runningWork":["/demo-project/us-central1/with_logger-2024-12-09T11:55:10.021Z"],"workRunningCount":1}
[debug] [2024-12-09T11:55:10.022Z] Accepted request GET /demo-project/us-central1/with_logger --> us-central1-with_logger
[debug] [2024-12-09T11:55:10.022Z] [functions] Runtime ready! Sending request! {"metadata":{"emulator":{"name":"functions"},"message":"[functions] Runtime ready! Sending request!"}}
[debug] [2024-12-09T11:55:10.022Z] [functions] Got req.url=/demo-project/us-central1/with_logger, mapping to path=/ {"metadata":{"emulator":{"name":"functions"},"message":"[functions] Got req.url=/demo-project/us-central1/with_logger, mapping to path=/"}}
[debug] [2024-12-09T11:55:10.025Z] Running command with virtualenv: command="C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Scripts\activate.bat", args=["","&&","functions-framework"]
[debug] [2024-12-09T11:55:10.032Z] [worker-pool] addWorker(us-central1-with_logger) {"metadata":{"emulator":{"name":"functions"},"message":"[worker-pool] addWorker(us-central1-with_logger)"}}
[debug] [2024-12-09T11:55:10.032Z] [worker-pool] Adding worker with key us-central1-with_logger, total=1 {"metadata":{"emulator":{"name":"functions"},"message":"[worker-pool] Adding worker with key us-central1-with_logger, total=1"}}
[info] >   * Serving Flask app 'with_logger'
 {"user":" * Serving Flask app 'with_logger'\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m  * Serving Flask app 'with_logger'\r"}}
[info] >   * Debug mode: off
 {"user":" * Debug mode: off\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m  * Debug mode: off\r"}}
[info] >  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 {"user":"WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\r"}}
[info] >   * Running on http://127.0.0.1:8932
 {"user":" * Running on http://127.0.0.1:8932\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m  * Running on http://127.0.0.1:8932\r"}}
[info] >  Press CTRL+C to quit
 {"user":"Press CTRL+C to quit\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m Press CTRL+C to quit\r"}}
[info] >  [2024-12-09 11:55:10,582] ERROR in app: Exception on /__/health [GET]
 {"user":"[2024-12-09 11:55:10,582] ERROR in app: Exception on /__/health [GET]\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m [2024-12-09 11:55:10,582] ERROR in app: Exception on /__/health [GET]\r"}}
[info] >  Traceback (most recent call last):
 {"user":"Traceback (most recent call last):\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m Traceback (most recent call last):\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 1511, in wsgi_app\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 1511, in wsgi_app\r"}}
[info] >      response = self.full_dispatch_request()
 {"user":"    response = self.full_dispatch_request()\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     response = self.full_dispatch_request()\r"}}
[info] >                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 919, in full_dispatch_request\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 919, in full_dispatch_request\r"}}
[info] >      rv = self.handle_user_exception(e)
 {"user":"    rv = self.handle_user_exception(e)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     rv = self.handle_user_exception(e)\r"}}
[info] >           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 917, in full_dispatch_request\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 917, in full_dispatch_request\r"}}
[info] >      rv = self.dispatch_request()
 {"user":"    rv = self.dispatch_request()\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     rv = self.dispatch_request()\r"}}
[info] >           ^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"         ^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m          ^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 902, in dispatch_request\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 902, in dispatch_request\r"}}
[info] >      return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
 {"user":"    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\functions_framework\execution_id.py", line 106, in wrapper
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\execution_id.py\", line 106, in wrapper\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\execution_id.py\", line 106, in wrapper\r"}}
[info] >      return view_function(*args, **kwargs)
 {"user":"    return view_function(*args, **kwargs)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return view_function(*args, **kwargs)\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\functions_framework\__init__.py", line 142, in view_func
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\__init__.py\", line 142, in view_func\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\__init__.py\", line 142, in view_func\r"}}
[info] >      return function(request._get_current_object())
 {"user":"    return function(request._get_current_object())\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return function(request._get_current_object())\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\https_fn.py", line 447, in on_request_wrapped
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\https_fn.py\", line 447, in on_request_wrapped\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\https_fn.py\", line 447, in on_request_wrapped\r"}}
[info] >      return _core._with_init(func)(request)
 {"user":"    return _core._with_init(func)(request)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return _core._with_init(func)(request)\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\core.py", line 125, in wrapper
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\core.py\", line 125, in wrapper\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\core.py\", line 125, in wrapper\r"}}
[info] >      return fn(*args, **kwargs)
 {"user":"    return fn(*args, **kwargs)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return fn(*args, **kwargs)\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\main.py", line 13, in with_logger
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\main.py\", line 13, in with_logger\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\main.py\", line 13, in with_logger\r"}}
[info] >      logger.log(message)
 {"user":"    logger.log(message)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     logger.log(message)\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\logger.py", line 112, in log
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 112, in log\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 112, in log\r"}}
[info] >      write(_entry_from_args(LogSeverity.NOTICE, *args, **kwargs))
 {"user":"    write(_entry_from_args(LogSeverity.NOTICE, *args, **kwargs))\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     write(_entry_from_args(LogSeverity.NOTICE, *args, **kwargs))\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\logger.py", line 97, in write
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 97, in write\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 97, in write\r"}}
[info] >      print(_json.dumps(_remove_circular(entry), ensure_ascii=False),
 {"user":"    print(_json.dumps(_remove_circular(entry), ensure_ascii=False),\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     print(_json.dumps(_remove_circular(entry), ensure_ascii=False),\r"}}
[info] >    File "C:\Users\<USER>\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 19, in encode
 {"user":"  File \"C:\\Users\\<USER>\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\encodings\\cp1252.py\", line 19, in encode\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\encodings\\cp1252.py\", line 19, in encode\r"}}
[info] >      return codecs.charmap_encode(input,self.errors,encoding_table)[0]
 {"user":"    return codecs.charmap_encode(input,self.errors,encoding_table)[0]\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return codecs.charmap_encode(input,self.errors,encoding_table)[0]\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >  UnicodeEncodeError: 'charmap' codec can't encode characters in position 35-37: character maps to <undefined>
 {"user":"UnicodeEncodeError: 'charmap' codec can't encode characters in position 35-37: character maps to <undefined>\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m UnicodeEncodeError: 'charmap' codec can't encode characters in position 35-37: character maps to <undefined>\r"}}
[debug] [2024-12-09T11:55:10.602Z] [worker-us-central1-with_logger-167715e7-7fd7-4932-bb7f-e87d94c8e0aa]: IDLE {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"[worker-us-central1-with_logger-167715e7-7fd7-4932-bb7f-e87d94c8e0aa]: IDLE"}}
[debug] [2024-12-09T11:55:10.602Z] [worker-pool] submitRequest(triggerId=us-central1-with_logger) {"metadata":{"emulator":{"name":"functions"},"message":"[worker-pool] submitRequest(triggerId=us-central1-with_logger)"}}
[info] i  functions: Beginning execution of "us-central1-with_logger" {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"Beginning execution of \"us-central1-with_logger\""}}
[debug] [2024-12-09T11:55:10.603Z] [worker-us-central1-with_logger-167715e7-7fd7-4932-bb7f-e87d94c8e0aa]: BUSY {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"[worker-us-central1-with_logger-167715e7-7fd7-4932-bb7f-e87d94c8e0aa]: BUSY"}}
[info] >  127.0.0.1 - - [09/Dec/2024 11:55:10] "GET /__/health HTTP/1.1" 500 -
 {"user":"127.0.0.1 - - [09/Dec/2024 11:55:10] \"GET /__/health HTTP/1.1\" 500 -\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m 127.0.0.1 - - [09/Dec/2024 11:55:10] \"GET /__/health HTTP/1.1\" 500 -\r"}}
[info] >  [2024-12-09 11:55:10,604] ERROR in app: Exception on / [GET]
 {"user":"[2024-12-09 11:55:10,604] ERROR in app: Exception on / [GET]\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m [2024-12-09 11:55:10,604] ERROR in app: Exception on / [GET]\r"}}
[info] >  Traceback (most recent call last):
 {"user":"Traceback (most recent call last):\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m Traceback (most recent call last):\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 1511, in wsgi_app\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 1511, in wsgi_app\r"}}
[info] >      response = self.full_dispatch_request()
 {"user":"    response = self.full_dispatch_request()\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     response = self.full_dispatch_request()\r"}}
[info] >                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 919, in full_dispatch_request\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 919, in full_dispatch_request\r"}}
[info] >      rv = self.handle_user_exception(e)
 {"user":"    rv = self.handle_user_exception(e)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     rv = self.handle_user_exception(e)\r"}}
[info] >           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 917, in full_dispatch_request\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 917, in full_dispatch_request\r"}}
[info] >      rv = self.dispatch_request()
 {"user":"    rv = self.dispatch_request()\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     rv = self.dispatch_request()\r"}}
[info] >           ^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"         ^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m          ^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 902, in dispatch_request\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\flask\\app.py\", line 902, in dispatch_request\r"}}
[info] >      return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
 {"user":"    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\functions_framework\execution_id.py", line 106, in wrapper
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\execution_id.py\", line 106, in wrapper\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\execution_id.py\", line 106, in wrapper\r"}}
[info] >      return view_function(*args, **kwargs)
 {"user":"    return view_function(*args, **kwargs)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return view_function(*args, **kwargs)\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\functions_framework\__init__.py", line 142, in view_func
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\__init__.py\", line 142, in view_func\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\functions_framework\\__init__.py\", line 142, in view_func\r"}}
[info] >      return function(request._get_current_object())
 {"user":"    return function(request._get_current_object())\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return function(request._get_current_object())\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\https_fn.py", line 447, in on_request_wrapped
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\https_fn.py\", line 447, in on_request_wrapped\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\https_fn.py\", line 447, in on_request_wrapped\r"}}
[info] >      return _core._with_init(func)(request)
 {"user":"    return _core._with_init(func)(request)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return _core._with_init(func)(request)\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\core.py", line 125, in wrapper
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\core.py\", line 125, in wrapper\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\core.py\", line 125, in wrapper\r"}}
[info] >      return fn(*args, **kwargs)
 {"user":"    return fn(*args, **kwargs)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return fn(*args, **kwargs)\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\main.py", line 13, in with_logger
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\main.py\", line 13, in with_logger\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\main.py\", line 13, in with_logger\r"}}
[info] >      logger.log(message)
 {"user":"    logger.log(message)\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     logger.log(message)\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\logger.py", line 112, in log
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 112, in log\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 112, in log\r"}}
[info] >      write(_entry_from_args(LogSeverity.NOTICE, *args, **kwargs))
 {"user":"    write(_entry_from_args(LogSeverity.NOTICE, *args, **kwargs))\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     write(_entry_from_args(LogSeverity.NOTICE, *args, **kwargs))\r"}}
[info] >    File "C:\Users\<USER>\Desktop\work\firebase-issues\issues-8002\functions\venv\Lib\site-packages\firebase_functions\logger.py", line 97, in write
 {"user":"  File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 97, in write\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\Desktop\\work\\firebase-issues\\issues-8002\\functions\\venv\\Lib\\site-packages\\firebase_functions\\logger.py\", line 97, in write\r"}}
[info] >      print(_json.dumps(_remove_circular(entry), ensure_ascii=False),
 {"user":"    print(_json.dumps(_remove_circular(entry), ensure_ascii=False),\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     print(_json.dumps(_remove_circular(entry), ensure_ascii=False),\r"}}
[info] >    File "C:\Users\<USER>\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 19, in encode
 {"user":"  File \"C:\\Users\\<USER>\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\encodings\\cp1252.py\", line 19, in encode\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m   File \"C:\\Users\\<USER>\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\encodings\\cp1252.py\", line 19, in encode\r"}}
[info] >      return codecs.charmap_encode(input,self.errors,encoding_table)[0]
 {"user":"    return codecs.charmap_encode(input,self.errors,encoding_table)[0]\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m     return codecs.charmap_encode(input,self.errors,encoding_table)[0]\r"}}
[info] >             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 {"user":"           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\r"}}
[info] >  UnicodeEncodeError: 'charmap' codec can't encode characters in position 35-37: character maps to <undefined>
 {"user":"UnicodeEncodeError: 'charmap' codec can't encode characters in position 35-37: character maps to <undefined>\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m UnicodeEncodeError: 'charmap' codec can't encode characters in position 35-37: character maps to <undefined>\r"}}
[debug] [2024-12-09T11:55:10.615Z] Finishing up request with event=pause {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"Finishing up request with event=pause"}}
[info] i  functions: Finished "us-central1-with_logger" in 12.3922ms {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"Finished \"us-central1-with_logger\" in 12.3922ms"}}
[debug] [2024-12-09T11:55:10.615Z] [worker-us-central1-with_logger-167715e7-7fd7-4932-bb7f-e87d94c8e0aa]: IDLE {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"[worker-us-central1-with_logger-167715e7-7fd7-4932-bb7f-e87d94c8e0aa]: IDLE"}}
[debug] [2024-12-09T11:55:10.615Z] Finishing up request with event=finish {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"Finishing up request with event=finish"}}
[debug] [2024-12-09T11:55:10.615Z] Finishing up request with event=close {"metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"Finishing up request with event=close"}}
[debug] [2024-12-09T11:55:10.616Z] [work-queue] {"queuedWork":[],"queueLength":0,"runningWork":[],"workRunningCount":0}
[info] >  127.0.0.1 - - [09/Dec/2024 11:55:10] "GET / HTTP/1.1" 500 -
 {"user":"127.0.0.1 - - [09/Dec/2024 11:55:10] \"GET / HTTP/1.1\" 500 -\r","metadata":{"emulator":{"name":"functions"},"function":{"name":"us-central1-with_logger"},"extension":{},"message":"\u001b[90m> \u001b[39m 127.0.0.1 - - [09/Dec/2024 11:55:10] \"GET / HTTP/1.1\" 500 -\r"}}
```

</details>

## Notes

- No issues on macOS
