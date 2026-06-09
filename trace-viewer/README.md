# Dexterous Presentation Trace Viewer

Local viewer for executable presentation traces.

From the repo root, generate a trace first:

```sh
python execute.py -m presentation
```

Then run the viewer:

```sh
npm install
npm run dev
```

Open:

```text
http://localhost:5173/?trace=/var/traces/presentation.json
```
