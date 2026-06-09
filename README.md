## From

我想要参照项目 /Users/sunsealucky/Desktop/spring2025-lectures 的展示风格，来做一个自己关于灵巧手的展示分享。

## Scaffold

This repo follows the executable lecture style from the reference project.
The main entry point is `presentation.py`, split into three section modules:

- `sections/hardware.py`: 硬件
- `sections/companies.py`: 公司
- `sections/algorithms.py`: 算法

Generate the starter trace:

```sh
python execute.py -m presentation
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
