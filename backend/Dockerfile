FROM python:3.10

# 作業ディレクトリ
WORKDIR /app/src

# Poetryをインストール
RUN pip install --upgrade pip \
  && pip install poetry

# プロジェクトの設定ファイルをコピー
COPY pyproject.toml poetry.lock* /app/
COPY data/data.csv /data/

# 依存関係のみをインストール
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-dev

# アプリケーションのコードをコンテナにコピー
COPY . /app

# アプリケーションを実行
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
