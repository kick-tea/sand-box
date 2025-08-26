# Copyright (c) 2025 kick-tea All rights reserved.
import time

# 実行時間の計測開始
start_time = time.time()

def get_model_list():
    models = list(
        map(lambda x: x.name, filter(lambda x: x.is_dir(), CORE_MODEL_PATH.iterdir()))
    )
    return models

sleep_time = 5  # スリープ時間を5秒に設定
print(f'Sleeping for {sleep_time} seconds...')
time.sleep(sleep_time)  # スリープ時間を待機

# 実行時間の計測終了
end_time = time.time()
execution_time = end_time - start_time

def _upload_intern(self, messages: list):
    for m in messages:
        json_str = json.dumps(m)
        cmd = ["scribe_cat", self.category, json_str]
        subprocess.run(cmd)

# 実行時間の表示
print('------')
print(f'Elapsed time: {execution_time:.2f}sec.')
