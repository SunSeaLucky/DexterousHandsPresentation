## Scaffold

This repo follows the executable lecture style from the reference project.
The main entry point is `presentation.py`, split into three section modules:

- `sections/hardware.py`: 硬件
- `sections/companies.py`: 公司
- `sections/algorithms.py`: 算法

Generate the starter trace:

```sh
uv run python execute.py -m presentation
```

View it locally:

```sh
cd trace-viewer
npm install
npm run dev
```

Then open the URL printed by Vite, for example:

```text
http://localhost:5173/?trace=/var/traces/presentation.json
```

## Note

This project is forked from https://github.com/stanford-cs336/spring2025-lectures