# celery-trial

FastAPI の処理を Celery+Redis で管理し Flower で確認するトライアルコード。

## Getting Started
コンテナの起動
```bash
docker compose up --build -d
```

## Containers
起動するコンテナ
- FastAPI - APIエンドポイントの提供
- Redis - データのインメモリストレージ
- Celery - 非同期ジョブの管理
- Flower - ジョブ監視UIの提供

## Endpoints

FastAPI
- http://localhost:8000/run - 処理実行(5s待機)
- http://localhost:8000/result/{job_id} - 結果取得

Flower
- http://localhost:5555 - ジョブの確認
