# DigitalOrgel
## 使用技術
Python, JSON  
## 作成時期
2023年夏ごろ制作→2024年春に修正
## 概要
jsonで記述した楽譜データを元に、音楽を生成するpythonのソフトです。
## 特徴
1. 8bit音楽っぽい(使っている波形が単純だから)
2. 音楽生成を、波形の数式を記述するとこから始めている(Drumsの音源もpythonで生成した)
3. 一般的な楽譜で書きづらいリズムも表現できる(各音符の始点を数字で記述するから)
4. 任意の周波数の波形を生成できる(frequencies.jsonを編集することによって)
## 使用例
〇EMOTION.wav  
EMOTION.jsonのデータをdigitalOrgel.pyに入力した際に出力された音声データです  
以下のリンクから試聴することも出来ます  
https://drive.google.com/file/d/119XmY5yf-PfvYFY4grUMJlMHQ539Bf75/view?usp=sharing
## 使い方
1. DigitalOrgel.pyの8行目の変数pathに、生成したい音楽の楽譜データファイル(json)のパスを書く。
2. DigitalOrgel.pyの11行目の変数songnameに、生成する音声ファイルの名前を書く。
3. digitalOrgel.pyを実行する(wavファイルが出力される)
## jsonファイルの書き方
詳しい構造はEMOTION.jsonを参照。  
"songName"(曲名を記入),"tempo"(テンポを記入),"length"(拍数),"parts"(楽譜データ)をキーに持ちます。  
"parts"の値として、辞書型にした各パートの楽譜データを配列にして記述します。  
声部一つ分の楽譜データの辞書は、"partName"(パートの名前),"volume"(音量、0-100で記述),"tone"(そのパートが音程をもつか),"instrument"(楽器名),"notes"(音符のデータ)をキーに持ちます。  
"tone"の値は"True"か"False"で記述します。"True"であれば音程のある楽器、"False"であれば音程のない楽器として扱います。  
"instruments"に書く楽器は、音程ありの楽器として"sine"(サイン波),"sawtooth"(ノコギリ波),"square"(矩形波),"triangular"(三角波),"pulse"(パルス波)を指定できます。  
音程ありの楽器の信号生成はmakeSound.pyが担っています。  
音程なしの楽器として、"sn"(スネアドラム),"bd"(バスドラム),"hh"(ハイハット)を指定できますが、これらはnotesのキーに記述し(後述)、ここでは"Drums"とだけ記入します。  
その音声はDrumsフォルダのwavファイルから確認できます。(こちらの音声もpythonを使って生成しました)  
"notes"には各音符のデータを記述しますが、音程ありと音程なしで書き方が異なります。  
音程ありの場合：[始点の拍番号,終点の拍番号,音程]を1音符のデータとし、それらを配列の形で記述します。  
音程なしの場合：[始点の拍番号,楽器名,音量(0-100)]を1音符のデータとし、それらを配列の形で記述します。  
## 今後の展望(改善点)
1. 使える楽器を増やす：もっと複雑な波形を生成して使用できるようにする
2. jsonの書き方を見直す：拍番号表記から小節数＋拍番号表記に変える
3. コードを簡潔にする：関数を用いて繰り返し書いてしまっているコードを簡略化する
## 参照
『Pythonではじめる音のプログラミング：コンピュータミュージックの信号処理』(青木直史)  
信号処理方法の多くはこちらを参照しました。  
『EMOTION』(三船栞子, tofubeats作詞作編曲)  
例で示した音楽はこちらの楽曲のサビ部分です。  
