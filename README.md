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
2. Run `firebase emulators:start --project demo-project` on a new terminal
3. Invoke function that <b>does not have logger</b> "http://127.0.0.1:5001/demo-project/us-central1/no_logger"
   - // TODO: Test on Windows
4. Invoke function that <b>has logger</b> "http://127.0.0.1:5001/demo-project/us-central1/with_logger"
   - // TODO: Test on Windows

## Notes

- No issues on macOS
